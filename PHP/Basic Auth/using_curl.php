# This script uses PHP as a wrapper for curl
<?php
$base_url = "{base url}/rest/latest/";
$username = "API_User";
$password = "********";

$resource = "projects";

$curl_request = curl_init();
curl_setopt($curl_request, CURLOPT_URL, $base_url . $resource);
curl_setopt($curl_request, CURLOPT_USERPWD, "$username:$password");
curl_setopt($curl_request, CURLOPT_RETURNTRANSFER, 1);

$result = curl_exec($curl_request);
curl_close($curl_request);

echo $result;
?>
