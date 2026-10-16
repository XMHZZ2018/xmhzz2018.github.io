"""Fetch a validated Google Scholar total through the SerpApi author API."""
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


def parse_api_total(payload, scholar_id):
    """Reject errors, the wrong profile, and incomplete/invalid citation totals."""
    try:
        if (payload.get('error') or
                payload['search_metadata']['status'] != 'Success' or
                payload['search_parameters']['engine'] != 'google_scholar_author' or
                payload['search_parameters']['author_id'] != scholar_id):
            raise ValueError
        name = payload['author']['name']
        rows = payload['cited_by']['table']
        totals = [row['citations']['all'] for row in rows if 'citations' in row]
        if len(totals) != 1:
            raise ValueError
        count = totals[0]
        if type(count) is not int or count < 0 or not isinstance(name, str) or not name.strip():
            raise ValueError
    except (KeyError, TypeError, ValueError, AttributeError):
        # Do not include response content; provider errors may echo credentials.
        raise ValueError('Invalid Scholar API result; retaining previous citation data') from None
    return {
        'scholar_id': scholar_id,
        'name': name.strip(),
        'citedby': count,
        'updated': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    }


def fetch_total(scholar_id):
    if not re.fullmatch(r'[A-Za-z0-9_-]+', scholar_id):
        raise ValueError('Invalid Google Scholar ID')
    api_key = os.environ.get('SERPAPI_API_KEY', '').strip()
    if not api_key:
        raise RuntimeError('Set the SERPAPI_API_KEY repository Actions secret before running')
    try:
        response = requests.get('https://serpapi.com/search.json', params={
            'engine': 'google_scholar_author',
            'author_id': scholar_id,
            'hl': 'en',
            'api_key': api_key,
        }, timeout=(10, 90), allow_redirects=False)
    except requests.RequestException:
        # Request exception URLs contain the key: never log or chain them.
        raise RuntimeError('Scholar API connection failed; retaining previous data') from None
    if response.status_code != 200:
        raise RuntimeError(f'Scholar API returned HTTP {response.status_code}; '
                           'check the API key and quota; retaining previous data')
    try:
        payload = response.json()
    except ValueError:
        raise ValueError('Scholar API returned invalid JSON; retaining previous data') from None
    return parse_api_total(payload, scholar_id)


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
    print(f"Updated total citations: {data['citedby']} at {data['updated']}")
