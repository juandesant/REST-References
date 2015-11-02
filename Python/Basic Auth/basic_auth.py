import urllib2
import base64

base_url = "{basic auth}/rest/latest/"
username = "API_User"
password = "********"

resource = "projects"

request = urllib2.Request(base_url + resource)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)

response = urllib2.urlopen(request);

print response.read();
