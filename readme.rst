CoderWall
====
    Simple Pythonic way to access CoderWall profile.

Built With
----
    - requests
    - Cement

Installtion
----
    ::

        pip install pycoderwall

or


        $wget https://github.com/kracekumar/coderwall/zipball/master
        $unzip -d coderwall
        $sudo python setup.py install

Usage
-----
    ::

    usage: pycoderwall [-h] [--debug] [--quiet] [-badges] [-endorsements]
                   [-accounts] [-location] [-team]
                   USERNAME

positional arguments:
    USERNAME              Pass username of coderwall profile to look for

optional arguments:
  -h, --help            show this help message and exit
  --debug               toggle debug output
  --quiet               suppress all output
  -badges, --badges     Display badges
  -endorsements, --endorsements
                        Display Endorsement values
  -accounts, --accounts
                        List all accounts
  -location, --location
                        Display location
  -team, --team         List all Teams user is associated with



Example
----
    ::

        $pycoderwall kracekumar -accounts

        ===accounts===
        {u'github': u'kracekumar'}
        ===End===

    ::

        $pycoderwall kracekumar -location

        ===location===
        u'Bangalore'
        ===End===

    ::

        $pycoderwall kracekumar
        [{u'accounts': {u'github': u'kracekumar'},
            u'badges': [{u'badge': u'http://cdn.coderwall.com/assets/badges/trex-8f3d5d72233031329b3365d5f16fd5d2.png',
               u'created': u'2012-05-06T10:13:08Z',
               u'description': u'Have at least one original repo where C is the dominant language',
               u'name': u'T-Rex'},
              {u'badge': u'http://cdn.coderwall.com/assets/badges/walrus-a0bb4ddb2394171b632edc953930518d.png',
               u'created': u'2012-04-13T20:32:09Z',
               u'description': u'The walrus is no stranger to variety. Use at least 4 different languages throughout all your repos',
               u'name': u'Walrus'},
              {u'badge': u'http://cdn.coderwall.com/assets/badges/forked1-ccde995368958c2e041acd64d8e4445f.png',
               u'created': u'2012-04-13T20:32:09Z',
               u'description': u'Have a project valued enough to be forked by someone else',
               u'name': u'Forked'},
              {u'badge': u'http://cdn.coderwall.com/assets/badges/charity-6c70c329d56fa13fcab3f07b26f0b178.png',
               u'created': u'2012-04-13T20:32:09Z',
               u'description': u"Fork and commit to someone's open source project in need",
               u'name': u'Charity'},
              {u'badge': u'http://cdn.coderwall.com/assets/badges/python3-dbea87acd2a6e554d626905959150909.png',
               u'created': u'2012-04-13T20:32:09Z',
               u'description': u'Have at least three original repos where Python is the dominant language',
               u'name': u'Python 3'},
              {u'badge': u'http://cdn.coderwall.com/assets/badges/python-4a8e1d5cd7994de0c1330692ba65e2e4.png',
               u'created': u'2012-04-13T20:32:09Z',
               u'description': u'Would you expect anything less? Have at least one original repo where Python is the dominant language',
               u'name': u'Python'},
              {u'badge': u'http://cdn.coderwall.com/assets/badges/labrador-e259d435ad24d216e58ac5bb700ee7a5.png',
               u'created': u'2012-04-13T20:32:08Z',
               u'description': u'Have at least one original repo where C# is the dominant language',
               u'name': u'Lab'}],
        u'endorsements': 0,
        u'location': u'Bangalore',
        u'name': u'kracekumar',
        u'team': None,
        u'username': u'kracekumar'}]
        ===End===

