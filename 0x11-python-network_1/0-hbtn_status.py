#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request as request


if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        res = response.read()
        print('Body response:')
        print('\t- {}'.format(type(res)))
        print('\t- {}'.format(res))
        print('\t- {}'.format(res.decode('utf-8')))
