#!/usr/bin/python3
"""using the GitHub API to siplay my id"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    auth = HTTPBasicAuth(username, password)

    response = requests.get(url, auth=auth)
    print(response.json().get("id"))
