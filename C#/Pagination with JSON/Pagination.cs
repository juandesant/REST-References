using System;
using System.IO;
using System.Net;
using System.Json;
using System.Collections.Generic;

public class BasicAuth
{
    static public void Main()
    {
        string baseURL = "{base url}/rest/latest/";
        string username = "API_User";
        string password = "********";
        string resource = "projects";

        int allowedResults = 20;
        string maxResults = "maxResults=" + allowedResults;

        long resultCount = -1;
        long startIndex = 0;

        while (resultCount != 0)
        {
            string startAt = "startAt=" + startIndex;

            string url = baseURL + resource + "?" + startAt + "&" + maxResults;

            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            request.Credentials = new NetworkCredential(username, password);
            request.Method = WebRequestMethods.Http.Get;
            request.PreAuthenticate = true;

            HttpWebResponse response = (HttpWebResponse)request.GetResponse();

            Stream stream = response.GetResponseStream();
            StreamReader streamReader = new StreamReader(stream);

            JsonValue json = JsonValue.Parse(streamReader.ReadToEnd());
            JsonObject projectsResponse = json as JsonObject;
            JsonObject meta = (JsonObject) projectsResponse["meta"];
            JsonObject pageInfo = (JsonObject) meta["pageInfo"];

            startIndex = (long) pageInfo["startIndex"] + allowedResults;
            resultCount = (long) pageInfo["resultCount"];

            JsonArray projects = (JsonArray) projectsResponse["data"];
            foreach (JsonObject project in projects)
            {
                JsonObject fields = (JsonObject) project["fields"];
                string name = (string) fields["name"];
                Console.WriteLine(name);
            }
        }
    }
}
