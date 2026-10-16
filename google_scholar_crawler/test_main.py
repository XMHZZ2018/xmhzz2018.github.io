"""Guard against publishing a partial table or an error page as citation data."""
import json
import tempfile
import unittest
from pathlib import Path

from main import parse_total, save_results


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


if __name__ == '__main__':
    unittest.main()
