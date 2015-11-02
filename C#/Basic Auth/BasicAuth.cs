using System;
using System.IO;
using System.Net;

public class BasicAuth
{
    static public void Main()
    {
        string baseUrl = "{base url}/rest/latest/";
        string username = "API_User";
        string password = "********";

        string resource = "projects";

        HttpWebRequest request = (HttpWebRequest)WebRequest.Create(baseUrl + resource);
        request.Credentials = new NetworkCredential(username, password);
        request.Method = WebRequestMethods.Http.Get;
        request.PreAuthenticate = true;

        HttpWebResponse response = (HttpWebResponse)request.GetResponse();

        Stream stream = response.GetResponseStream();
        StreamReader streamReader = new StreamReader(stream);
        string s = streamReader.ReadToEnd();

        Console.WriteLine(s);
    }
}
