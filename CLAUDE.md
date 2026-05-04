# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Minimal Python wrapper around Similarweb's undocumented free data endpoint
(`https://data.similarweb.com/api/v1/data?domain=<domain>`). Forked from
[DaWe35/Similarweb-free-API](https://github.com/DaWe35/Similarweb-free-API).
Not a package — two flat scripts intended to be imported or copied into a
parent project.

## Setup & Commands

Environment is managed with `uv`; the only runtime dependency is `requests`.

```bash
uv venv
source .venv/bin/activate
uv pip install requests

python test.py        # runs the smoke test against a hardcoded domain
```

There is no test framework, linter, or build step configured.

## Architecture

- [similar.py](similar.py) — single public function `similarGet(website)`.
  Normalizes input via `urlparse` → `netloc`, strips a leading `www.`, then
  GETs the data endpoint with a desktop Chrome `User-Agent` (the API rejects
  default `python-requests` UAs). Returns parsed JSON on 200, otherwise calls
  `raise_for_status()`.
- [test.py](test.py) — illustrative caller. Wraps `similarGet` in a
  retry-on-exception loop with a 3-second backoff and writes the payload to
  `<SiteName>.json`. The retry loop exists because the upstream API is rate
  limited and occasionally slow; treat that pattern as the recommended usage,
  not test infrastructure.

### Using `similar` from a parent project

When this repo lives as a subfolder of a larger project, `import similar`
won't resolve. Use the dynamic form documented in [test.py](test.py):

```python
import importlib
similar = importlib.import_module("Similarweb-free-API.similar")
```

## Conventions

- README is in Chinese; keep user-facing docs bilingual-friendly (Chinese OK
  for prose, English for code identifiers).
- The `User-Agent` constant in [similar.py](similar.py) is load-bearing — do
  not remove it or replace it with a generic UA.
- Output JSON files (`<SiteName>.json`) and `.venv/` are intentionally not
  gitignored individually; the broad `.gitignore` covers `.venv` but generated
  JSON should be cleaned up manually or added to `.gitignore` if it becomes
  noisy.
