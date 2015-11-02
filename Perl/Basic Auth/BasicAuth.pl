#!/usr/bin/env perl
use LWP;

$base_url = "{base url}/rest/latest/";
$username = "API_User";
$password = "********";

$resource = "projects";

my $browser = LWP::UserAgent->new;
my $req = HTTP::Request->new( GET => $base_url . $resource );
$req->authorization_basic( $username, $password );
my $res = $browser->request( $req );

say $res->content;

