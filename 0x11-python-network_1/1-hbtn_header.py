#!/usr/bin/python3
"""using urllib to send requests"""

import sys
from urllib import request

if __name__ == "__main__":

    url = sys.argv[1]

    with request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
