#!/usr/bin/python3
"""
Module to send a POST request to a URL with an email as a
parameter and display the response body.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)
