# Citation updates

The homepage reads the newest valid total from `google-scholar-stats/gs_data.json`,
with `assets/data/scholar.json` as an offline fallback. The badge tooltip shows the
successful fetch date. Failed requests never overwrite the saved total.

## One-time setup

1. Get an API key from https://serpapi.com/manage-api-key.
2. Open the repository's Settings → Secrets and variables → Actions.
3. Add a repository secret named `SERPAPI_API_KEY` with the key as its value.
   Never put the key in the source code, a workflow input, or a public issue.
4. In Actions, select **Get Citation Data** → **Run workflow**.
5. Confirm both **Fetch total citations** and **Publish successful snapshot** pass.

The workflow runs daily at 08:17 UTC (01:17 PDT / 00:17 PST), and can also be run
manually. Each run makes one SerpApi Google Scholar Author request, requesting
only the author profile's total rather than fetching individual paper citations.
Allow for extra usage when testing or running it manually. GitHub's scheduled
start time can be delayed.

The provider response must identify the requested Scholar author and include a
successful, nonnegative integer all-time citation total. Authentication, quota,
network, or data-validation errors fail the workflow without publishing a new
snapshot. Missing keys fail with a setup message; request URLs and raw provider
errors are not logged because they may contain credentials.

## Validation

```sh
python -m pip install -r google_scholar_crawler/requirements.txt
python -m unittest discover -s google_scholar_crawler -p 'test_*.py'
```

Tests cover all-time versus recent totals, incorrect profiles, missing/invalid
counts, zero citations, API errors, preservation of saved data, and key redaction.
They do not make API requests or consume credits.
