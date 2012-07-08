#! /usr/bin/env python
#! -*- coding: utf-8 -*-

try:
    import requests
except ImportError:
    raise ImportError("Unable to import requests. Try pip install requests")
try:
    from cement.core import foundation
except ImportError:
    raise ImportError("Unable to import cement. Try pip install cement")
from pprint import pprint


class CoderWall(object):
    BASE_URL = "http://coderwall.com"

    def __init__(self, username):
        self.username = username
        self.data = []
        self.output = {}
        self.fetch_details()
        if None in self.data:
            self.error()

    def fetch_details(self):
        try:
            r = requests.get('/'.join([CoderWall.BASE_URL, self.username]) + '.json')
            self.data.append(r.json if r.ok else None)
        except requests.ConnectionError:
            raise requests.ConnectionError
        except requests.HTTPError:
            raise requests.HTTPError

    def error(self):
        print("User: %s not found" % (self.username))

    def evaluate(self, command_line_params):
        if True not in command_line_params.values():
            self.output = self.data
        else:
            for key, value in command_line_params.iteritems():
                if value:
                    self.output[key] = self.data[0][key]

    def final_output(self):
        if isinstance(self.output, dict):
            for key, val in self.output.iteritems():
                print("==={0}===".format(key))
                pprint(val)
        else:
            pprint(self.output)
        print("===End===")


def resolve_dependecy(command_line_params):
    coderwall = CoderWall(command_line_params['username'])
    command_line_params.pop('username')
    coderwall.evaluate(command_line_params)
    coderwall.final_output()


def main():
    app = foundation.CementApp("CoderWall")
    to_pop = ('debug', 'suppress_output')
    try:
        app.setup()
        app.args.add_argument('username', metavar="USERNAME", help="Pass username of coderwall profile to look for")
        app.args.add_argument('-badges', '--badges', action="store_true", help="Display badges")
        app.args.add_argument('-endorsements', '--endorsements', action="store_true", help="Display Endorsement value")
        app.args.add_argument('-accounts', '--accounts', action="store_true", help="List all accounts")
        app.args.add_argument('-location', '--location', action="store_true", help="Display location")
        app.args.add_argument('-team', '--team', action="store_true", help="List all Teams user is associated with")
        app.run()
        command_line = app.pargs.__dict__
        for key in to_pop:
            command_line.pop(key)
        if command_line['username']:
            resolve_dependecy(command_line)
        else:
            pass
    finally:
        app.close()

if __name__ == "__main__":
    main()
