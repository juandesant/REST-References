#!/usr/bin/env python3
# This example makes use of the excellent library at python-requests.org
import requests
from getpass import getpass
import argparse
import json

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
response = requests.get(api_url + resource, auth=(args.username, password))

data = json.loads(response.text)
print(json.dumps(data))

