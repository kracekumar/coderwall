#! /usr/bin/env python
#! -*- coding: utf-8 -*-

try:
    import requests
except ImportError:
    raise ImportError("Unable to import requests. Try pip install requests")
try:
    import ujson
except ImportError:
    raise ImportError("Unable to import ujson. Try pip install ujson")
try:
    from cement.core import foundation
except ImportError:
    raise ImportError("Unable to import cement. Try pip install cement")


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
            return r.json if r.ok else None
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


def main():
    app = foundation.CementApp("CoderWall")
    try:
        app.setup()
        app.run()
    finally:
        app.close()

if __name__ == "__main__":
    main()

