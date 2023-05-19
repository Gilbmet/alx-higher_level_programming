#!/usr/bin/python3
"""
Module to send a request to a URL and display the response body.
If the HTTP status code is >= 400, it prints an error message.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
