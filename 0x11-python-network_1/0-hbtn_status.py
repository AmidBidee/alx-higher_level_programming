#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request as request

url = 'https://intranet.hbtn.io/status'

if __name__ == '__main__':
    req = request.Request(url)
    with request.urlopen(req) as response:
        res = response.read()
        print('Body response')
        print(f'\t- {type(res)}')
        print(f'\t- {res}')
        print(f"\t- {res.decode('utf-8')}")