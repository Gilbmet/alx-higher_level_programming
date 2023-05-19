#!/usr/bin/python3
"""
Module to send a request to a URL and display the value of
the X-Request-Id header in the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)
