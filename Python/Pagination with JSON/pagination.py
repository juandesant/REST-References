import requests
import json

base_url = "{base url}/rest/latest/"
username = "API_User"
password = "********"
resource = "projects"

allowedResults = 20
maxResults = "maxResults=" + str(allowedResults)

resultCount = -1
startIndex = 0

while resultCount != 0:
    startAt = "startAt=" + str(startIndex)

    url = base_url + resource + "?" + startAt + "&" + maxResults
    response = requests.get(url, auth=(username, password))
    jsonResponse = json.loads(response.text)

    pageInfo = jsonResponse["meta"]["pageInfo"]
    startIndex = pageInfo["startIndex"] + allowedResults
    resultCount = pageInfo["resultCount"]

    projects = jsonResponse["data"]
    for project in projects:
        print project["fields"]["name"]

