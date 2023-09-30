#!/usr/bin/python3
"""using urllib to send a POST request"""

import sys
from urllib import request
from urllib import parse

if __name__ == "__main__":

    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    data_encoded = parse.urlencode(data).encode('ascii')

    with request.urlopen(url, data=data_encoded) as response:

        print(response.read().decode('utf-8'))
