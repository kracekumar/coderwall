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
        self.output = []
        self.fetch_details()
        if None in self.output:
            self.error()

    def fetch_details(self):
        try:
            for username in self.username:
                r = requests.get('/'.join([CoderWall.BASE_URL, username]) + '.json')
                self.output.append(r.json if r.ok else None)
        except requests.ConnectionError:
            raise requests.ConnectionError
        except requests.HTTPError:
            raise requests.HTTPError


    def check_badge(self, badges):
        if self.output:
            print self.output

    def error(self):
        print("User: %s not found" % (self.username))


def resolve_dependecy(command_line_params):
    if 'name' in command_line_params:
        coderwall = CoderWall(command_line_params['name'].split())
        command_line_params.pop('name')
        if 'badge' in command_line_params:
            coderwall.check_badge(command_line_params['badge'].split())

def main():
    app = foundation.CementApp("CoderWall")
    to_pop = ('debug', 'suppress_output')
    try:
        app.setup()
        app.args.add_argument('-n', '--name', action="store", metavar="NAME", help="Pass name/names of coderwall profile to look for")
        app.args.add_argument('-b', '--badge', action="store", metavar="BADGE", help="Check whether user has got particular badge/badges or not")
        app.run()
        command_line = app.pargs.__dict__
        for key in to_pop:
            command_line.pop(key)
        print(command_line)
        resolve_dependecy(command_line)
        print("started")
    finally:
        app.close()

if __name__ == "__main__":
    main()

