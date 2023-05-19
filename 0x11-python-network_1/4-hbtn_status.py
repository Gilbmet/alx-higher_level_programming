#!/usr/bin/python3
"""
Module to fetch a URL using the requests package and
display the body of the response.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    content_type = response.headers.get('content-type')
    content = response.text

    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
