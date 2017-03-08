import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#enable search
SQLALCHEMY_TRACK_MODIFICATIONS = True

CSRF_ENABLED = True
SECRET_KEY = 'lalala'

WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 500

# pagination
TOOLS_PER_PAGE = 13

SiteNameString = 'innoSearch'
tabs = [{'tab_href': 'all','Name': 'all',},
        {'tab_href': 'CSI','Name': 'CSI',},
        {'tab_href': 'NDO','Name': 'NDO',},
        {'tab_href': 'Customer Support','Name': 'Customer Support',},
        {'tab_href': 'Operational','Name': 'Operational',},
        {'tab_href': 'Managed Service','Name': 'Managed Service',}]

