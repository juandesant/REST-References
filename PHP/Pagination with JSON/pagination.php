<?php
$base_url = "{base url}/rest/latest/";
$resource = "projects";
$username = "API_User";
$password = "********";

$allowedResults = 20;
$maxResults = "maxResults=" . $allowedResults;

$resultCount = -1;
$startIndex = 0;

while($resultCount != 0) {
    $startAt = "startAt=" . $startIndex;

    $url = $base_url . $resource . "?" . $startAt . "&" . $maxResults;

    $curl_request = curl_init();
    curl_setopt($curl_request, CURLOPT_URL, $url);
    curl_setopt($curl_request, CURLOPT_USERPWD, "$username:$password");
    curl_setopt($curl_request, CURLOPT_RETURNTRANSFER, 1);

    $result = curl_exec($curl_request);
    curl_close($curl_request);

    $jsonResponse = json_decode($result, true);
    $pageInfo = $jsonResponse['meta']['pageInfo'];
    $startIndex = $pageInfo['startIndex'] + $allowedResults;
    $resultCount = $pageInfo['resultCount'];

    $projects = $jsonResponse['data'];
    foreach($projects as $project) {
        echo $project['fields']['name'] . "\n";
    }
}
?>
