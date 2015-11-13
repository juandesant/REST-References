#!/usr/bin/env python
# This example makes use of the excellent library at python-requests.org
import requests

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser as ConfigParser
import os

REQUIRED_KEYS = [
    'url_rest', # WS api already uses url
    'account',
    'password',
]

CONFIG_FILES = [
    '/etc/jama.cfg',
    '~/.jama',
    '~/.jamarc'
]

def load_file_config(path=None):
    """
    Loads configuration from file with following content::
    
        [soap]
        url_rest = <REST url endpoint>
        account = <username>
        password = <password>
    
    :param path: path to config file. If not specified, default locations of
    ``/etc/jama.cfg``, ``~/.jama``, and ``~/.jamarc`` are tried.
    """
    config = ConfigParser()
    if path is None:
        config.read([os.path.expanduser(path) for path in CONFIG_FILES])
    else:
        config.read(path)
    
    if not config.has_section('soap'):
        return {}
    
    return dict(
        (key, val)
        for key, val in config.items('soap')
        if key in REQUIRED_KEYS
    )


resource = "projects"

jama_params = load_file_config()

response = requests.get(
                jama_params['url_rest'] + resource,
                auth=(jama_params['account'], jama_params['password'])
)

print response.text

