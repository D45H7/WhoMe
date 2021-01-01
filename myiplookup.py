#!/usr/bin/python39

import requests

banner = """
##
## MyIP's Lookup
## Using ipify.org
##
"""

req = requests.get("http://api.ipify.org/?format=json")
print("IP publik kamu:",req.json()['ip'])