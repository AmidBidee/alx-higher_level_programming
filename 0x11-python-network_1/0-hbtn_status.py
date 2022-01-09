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
        print('\t- type: {}'.format(type(res)))
        print('\t- content: {}'.format(res))
        print('\t- utf8 content: {}'.format(res.decode('utf-8')))
