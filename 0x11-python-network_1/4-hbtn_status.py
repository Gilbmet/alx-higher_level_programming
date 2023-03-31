#!/usr/bin/env python3
import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)

print('Body response:')
print(f'\t- type: {type(response.content)}')
print(f'\t- content: {response.content.decode()}')

