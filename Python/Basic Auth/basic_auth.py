#!/usr/bin/env python3
import urllib.request, urllib.error, urllib.parse
import base64

base_url = "{base url}/rest/latest/"

# Username and password should be stored according
# to your organization's security policies
username = "API_User"
password = "********"

resource = "projects"

request = urllib.request.Request(base_url + resource)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)

response = urllib.request.urlopen(request);

print(response.read());
