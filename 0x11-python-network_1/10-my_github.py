#!/usr/bin/python3
"""
Module to authenticate with GitHub API and display user ID.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: ./10-my_github.py username token")

    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        json_response = response.json()
        user_id = json_response.get('id')
        print(user_id)
    else:
        print("None")
