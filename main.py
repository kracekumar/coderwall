#! /usr/bin/env python
#! -*- coding: utf-8 -*-

import requests
import ujson


class CoderWall(object):
    BASE_URL = "http://coderwall.com"

    def __init__(self, username, to_return=None, format='str'):
        self.username = username
        self.to_return = to_return
        self.format = format
        self.data = self.fetch_details()
        if self.data is None:
            self.error()
        self.output()

    def fetch_details(self):
        try:
            r = requests.get('/'.join([CoderWall.BASE_URL, self.username]) + '.json')
            return r.json if r.ok is None
        except requests.ConnectionError:
            raise requests.ConnectionError
        except requests.HTTPError:
            raise requests.HTTPError

    def output(self):
        if self.format is 'str':
            print ujson.dumps(self.data)
        else:
            print self.data

    def error(self):
        print("User: %s not found" % (self.username))

if __name__ == "__main__":
    CoderWall('kracekumar')
