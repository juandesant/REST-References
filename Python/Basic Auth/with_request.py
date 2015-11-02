# This example makes use of the excellent library at python-requests.org
import requests

base_url = "{base url}/rest/latest/"
username = "API_User"
password = "********"

resource = "projects"

response = requests.get(base_url + resource, auth=(username, password))

print response.text

