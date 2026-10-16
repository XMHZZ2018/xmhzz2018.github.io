"""Guard against publishing a partial table or an error page as citation data."""
import copy
import json
import traceback
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests

from main import fetch_total, parse_api_total, parse_total, save_results


class CitationTests(unittest.TestCase):
    def test_all_time_total_not_recent_count(self):
        data = parse_total('''<div id="gsc_prf_in">Ziyan Jiang</div>
          <table id="gsc_rsb_st"><tr><td class="gsc_rsb_std">5,721</td>
          <td class="gsc_rsb_std">5,571</td></tr></table>''', 'wDJjd2IAAAAJ')
        self.assertEqual(data['citedby'], 5721)
        self.assertEqual(data['scholar_id'], 'wDJjd2IAAAAJ')

    def test_blocked_or_incomplete_pages_do_not_replace_snapshot(self):
        for html in ['<html>Access denied</html>',
                     '<div id="gsc_prf_in">Ziyan Jiang</div>',
                     '<div id="gsc_prf_in">Ziyan Jiang</div><table id="gsc_rsb_st">'
                     '<td class="gsc_rsb_std">N/A</td></table>']:
            with self.subTest(html=html), tempfile.TemporaryDirectory() as directory:
                path = Path(directory)
                save_results({'citedby': 5653}, path)
                with self.assertRaises(ValueError):
                    save_results(parse_total(html, 'wDJjd2IAAAAJ'), path)
                self.assertEqual(json.loads((path / 'gs_data.json').read_text())['citedby'], 5653)

    def test_zero_is_valid(self):
        data = parse_total('<div id="gsc_prf_in">Name</div><table id="gsc_rsb_st">'
                           '<td class="gsc_rsb_std">0</td></table>', 'id')
        self.assertEqual(data['citedby'], 0)


class ScholarApiTests(unittest.TestCase):
    def setUp(self):
        self.scholar_id = 'wDJjd2IAAAAJ'
        self.payload = {
            'search_metadata': {'status': 'Success'},
            'search_parameters': {'engine': 'google_scholar_author', 'author_id': self.scholar_id},
            'author': {'name': 'Ziyan Jiang'},
            'cited_by': {'table': [
                {'h_index': {'all': 15}},
                {'citations': {'all': 5721, 'since_2021': 5571}},
            ]},
        }

    def test_total_found_by_name_not_table_position(self):
        self.assertEqual(parse_api_total(self.payload, self.scholar_id)['citedby'], 5721)

    def test_invalid_responses_leave_previous_snapshot(self):
        invalid = [None, {}, {'error': 'fake-secret-must-not-appear'}]
        for count in [-1, True, 5.5, '5721', None]:
            payload = copy.deepcopy(self.payload)
            payload['cited_by']['table'][1]['citations']['all'] = count
            invalid.append(payload)
        wrong_author = copy.deepcopy(self.payload)
        wrong_author['search_parameters']['author_id'] = 'different-author'
        invalid.append(wrong_author)
        recent_only = copy.deepcopy(self.payload)
        del recent_only['cited_by']['table'][1]['citations']['all']
        invalid.append(recent_only)
        pending = copy.deepcopy(self.payload)
        pending['search_metadata']['status'] = 'Processing'
        invalid.append(pending)
        for payload in invalid:
            with self.subTest(payload=payload), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                save_results({'citedby': 5721}, root)
                before = (root / 'gs_data.json').read_bytes()
                with self.assertRaises(ValueError):
                    save_results(parse_api_total(payload, self.scholar_id), root)
                self.assertEqual((root / 'gs_data.json').read_bytes(), before)

    def test_zero_is_valid_api_total(self):
        self.payload['cited_by']['table'][1]['citations']['all'] = 0
        self.assertEqual(parse_api_total(self.payload, self.scholar_id)['citedby'], 0)

    @patch.dict('os.environ', {'SERPAPI_API_KEY': ''})
    @patch('main.requests.get')
    def test_missing_key_makes_no_request(self, get):
        with self.assertRaisesRegex(RuntimeError, 'SERPAPI_API_KEY'):
            fetch_total(self.scholar_id)
        get.assert_not_called()

    @patch.dict('os.environ', {'SERPAPI_API_KEY': 'fake-secret-must-not-appear'})
    @patch('main.requests.get')
    def test_api_response_written_in_existing_format(self, get):
        get.return_value = Mock(status_code=200)
        get.return_value.json.return_value = self.payload
        data = fetch_total(self.scholar_id)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            save_results(data, root)
            self.assertEqual(json.loads((root / 'gs_data.json').read_text())['citedby'], 5721)
            self.assertEqual(json.loads((root / 'gs_data_shieldsio.json').read_text())['message'], '5721')
            self.assertNotIn('fake-secret', (root / 'gs_data.json').read_text())

    @patch.dict('os.environ', {'SERPAPI_API_KEY': 'fake-secret-must-not-appear'})
    @patch('main.requests.get')
    def test_failed_requests_do_not_leak_keys(self, get):
        cases = [requests.ConnectionError('https://serpapi.com/?api_key=fake-secret-must-not-appear'),
                 Mock(status_code=401), Mock(status_code=429), Mock(status_code=500),
                 Mock(status_code=200)]
        cases[-1].json.side_effect = ValueError('fake-secret-must-not-appear')
        for case in cases:
            with self.subTest(case=case):
                get.side_effect = case if isinstance(case, Exception) else None
                get.return_value = case
                try:
                    fetch_total(self.scholar_id)
                except (RuntimeError, ValueError):
                    self.assertNotIn('fake-secret-must-not-appear', traceback.format_exc())
                else:
                    self.fail('Failed response accepted')


if __name__ == '__main__':
    unittest.main()
