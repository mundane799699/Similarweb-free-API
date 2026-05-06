import json
import time
import similar

'''
ONLY FOR TESTING
Always watch the response, and exit if Similarweb limit reached! Sometimes Similarweb's response can be slow.

If you want to acces to a parent folder, change:

import similar

To:

import importlib
similar = importlib.import_module("Similarweb-free-API.similar")
'''

try:
    data = similar.similarGet('https://acoda.com')
    json_str = json.dumps(data, indent=2, ensure_ascii=False)
    print(json_str)
    with open(f"{data['SiteName']}.json", 'w', encoding='utf-8') as f:
        f.write(json_str)
except Exception as e:
    print(f"Request failed: {e}")