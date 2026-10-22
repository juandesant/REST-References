#!/usr/bin/env python3
import urllib.request, urllib.error, urllib.parse
import base64
from getpass import getpass
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description="Access Jama API")
parser.add_argument("-u", "--api-url", required=True, help="Base Jama URL (e.g., https://instance.jamacloud.com/)")
parser.add_argument("-n", "--username", required=True, help="API User name")
args = parser.parse_args()

base_url = args.api_url.rstrip('/')
api_url = f"{base_url}/rest/latest/"

# Username and password should be stored according
# to your organization's security policies
password = getpass(prompt=f"{api_url} API user's password: ")

resource = "projects"

request = urllib.request.Request(base_url + resource)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)

response = urllib.request.urlopen(request);

print(response.read());
