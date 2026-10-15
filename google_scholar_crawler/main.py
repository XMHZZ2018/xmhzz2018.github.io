"""Read the all-time citation total from one public Google Scholar profile."""
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def parse_total(content, scholar_id):
    soup = BeautifulSoup(content, 'html.parser')
    name = soup.select_one('#gsc_prf_in')
    total = soup.select_one('#gsc_rsb_st .gsc_rsb_std')
    if name is None or total is None:
        raise ValueError('Scholar profile unavailable; retaining previous citation data')
    count = total.get_text(strip=True).replace(',', '')
    if not count.isdecimal():
        raise ValueError('Invalid citation total; retaining previous citation data')
    return {
        'scholar_id': scholar_id,
        'name': name.get_text(' ', strip=True),
        'citedby': int(count),
        'updated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    }


def fetch_total(scholar_id):
    if not re.fullmatch(r'[A-Za-z0-9_-]+', scholar_id):
        raise ValueError('Invalid Google Scholar ID')
    response = requests.get('https://scholar.google.com/citations',
                            params={'user': scholar_id, 'hl': 'en'}, timeout=30)
    response.raise_for_status()
    return parse_total(response.content, scholar_id)


def save_results(data, directory):
    directory.mkdir(parents=True, exist_ok=True)
    (directory / 'gs_data.json').write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    (directory / 'gs_data_shieldsio.json').write_text(json.dumps({
        'schemaVersion': 1, 'label': 'citations', 'message': str(data['citedby'])
    }) + '\n', encoding='utf-8')


if __name__ == '__main__':
    data = fetch_total(os.environ['GOOGLE_SCHOLAR_ID'])
    save_results(data, Path(__file__).parent / 'results')
    print(f"Updated total citations at {data['updated']}")
