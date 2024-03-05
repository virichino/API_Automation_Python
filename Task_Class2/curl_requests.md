# CRUD operations and negative cases

All the request were executed from the [ClickUp](https://clickup.com/) API

## GET request

Getting all the goals from the team

```bash

  $ curl -X GET "https://api.clickup.com/api/v2/team/$TeamId/goal?include_completed=true" -H "Authorization: $APIToken" -v|jq
Note: Unnecessary use of -X or --request, GET is already inferred.
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 52.65.208.115:443...
* Connected to api.clickup.com (52.65.208.115) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
*  CAfile: C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
*  CApath: none
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched certs "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0* Using HTTP2, server supports multiplexing
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
} [5 bytes data]
* Using Stream ID: 1 (easy handle 0x242389d28b0)
} [5 bytes data]
> GET /api/v2/team/25747182/goal?include_completed=true HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.80.0
> accept: */*
> authorization: pk_43050475_WP16359UNWJ251JTJO2VTQB97J9IRVC6
>
{ [5 bytes data]
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
} [5 bytes data]
< HTTP/2 200
< date: Tue, 05 Mar 2024 04:02:30 GMT
< content-type: application/json; charset=utf-8
< content-length: 645
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 5030248030338668426
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 98
< x-ratelimit-reset: 1709611403
< timing-allow-origin: *
<
{ [645 bytes data]
100   645  100   645    0     0    410      0  0:00:01  0:00:01 --:--:--   410
* Connection #0 to host api.clickup.com left intact
{
  "goals": [
    {
      "id": "a60847ce-bf55-43e8-a7e0-e4620e734788",
      "pretty_id": "51",
      "name": "new goal automation test",
      "team_id": "25747182",
      "creator": 43050475,
      "owner": null,
      "color": "#757380",
      "date_created": "1701380202843",
      "start_date": null,
      "due_date": null,
      "description": "\n",
      "private": false,
      "archived": false,
      "multiple_owners": true,
      "editor_token": "goal:a60847ce-bf55-43e8-a7e0-e4620e734788:b6918253-1481-4d23-b74a-e394cfe3edc3:4462885d-ddba-4f9b-9391-d2381d724597",
      "date_updated": "1701380202843",
      "last_update": "1701380202843",
      "folder_id": null,
      "pinned": false,
      "owners": [],
      "key_result_count": 0,
      "members": [],
      "group_members": [],
      "percent_completed": 0
    }
  ],
  "folders": []
}

```
## POST request

Creating a new goal

```bash

$ curl -X POST "https://api.clickup.com/api/v2/team/$TeamId/goal" -H "Authorization: $APIToken" -H "Content-Type: application/json" -d '{"name": "Goal Name","due_date": 1568036964079,"description": "Goal Description","multiple_owners": true,"owners": [43050475],"color": "#32a852"}' -v|jq
Note: Unnecessary use of -X or --request, POST is already inferred.
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 3.105.191.228:443...
* Connected to api.clickup.com (3.105.191.228) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
*  CAfile: C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
*  CApath: none
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched certs "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
* Using HTTP2, server supports multiplexing
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
} [5 bytes data]
* Using Stream ID: 1 (easy handle 0x20ece112040)
} [5 bytes data]
> POST /api/v2/team/25747182/goal HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.80.0
> accept: */*
> authorization: pk_43050475_WP16359UNWJ251JTJO2VTQB97J9IRVC6
> content-type: application/json
> content-length: 145
>
{ [5 bytes data]
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
} [5 bytes data]
* We are completely uploaded and fine
{ [5 bytes data]
< HTTP/2 200
< date: Tue, 05 Mar 2024 04:15:13 GMT
< content-type: application/json; charset=utf-8
< content-length: 816
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 301477764428978864
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 98
< x-ratelimit-reset: 1709612135
< timing-allow-origin: *
<
{ [816 bytes data]
100   961  100   816  100   145    433     77  0:00:01  0:00:01 --:--:--   511
* Connection #0 to host api.clickup.com left intact
{
  "goal": {
    "id": "30d08601-5d56-4c1a-97b6-854cfcb0fbdc",
    "pretty_id": "53",
    "name": "Goal Name",
    "team_id": "25747182",
    "creator": 43050475,
    "color": "#32a852",
    "date_created": "1709612113249",
    "start_date": null,
    "due_date": "1568036964079",
    "description": "Goal Description",
    "private": false,
    "archived": false,
    "multiple_owners": true,
    "editor_token": "goal:30d08601-5d56-4c1a-97b6-854cfcb0fbdc:7adae990-ed97-4bc8-90a3-8e7bd263e719:0e612db3-47a2-4562-a535-e0ffcf59cb13",
    "date_updated": "1709612113249",
    "folder_id": null,
    "folder_name": null,
    "members": [],
    "group_members": [],
    "owners": [
      {
        "id": 43050475,
        "username": "carlos tito",
        "email": "crisbelwla@hotmail.com",
        "color": "#006063",
        "profilePicture": null,
        "initials": "CT"
      }
    ],
    "key_results": [],
    "key_result_count": 0,
    "percent_completed": 0,
    "history": [],
    "pretty_url": "https://app.clickup.com/25747182/goals/53"
  }
}
```

## PUT request

Updating a goal

```bash

$ curl -X PUT "https://api.clickup.com/api/v2/goal/30d08601-5d56-4c1a-97b6-854cfcb0fbdc" -H "Authorization: $APIToken" -H "Content-Type: application/json" -d '{"name": "Updated Goal Name","due_date": 1568036964079,"description": "Updated Goal Description","color": "#32a852"}' -v|jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 52.65.208.115:443...
* Connected to api.clickup.com (52.65.208.115) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
*  CAfile: C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
*  CApath: none
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched certs "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0* Using HTTP2, server supports multiplexing
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
} [5 bytes data]
* Using Stream ID: 1 (easy handle 0x1d9dbbc2d20)
} [5 bytes data]
> PUT /api/v2/goal/30d08601-5d56-4c1a-97b6-854cfcb0fbdc HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.80.0
> accept: */*
> authorization: pk_43050475_WP16359UNWJ251JTJO2VTQB97J9IRVC6
> content-type: application/json
> content-length: 116
>
{ [5 bytes data]
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
} [5 bytes data]
* We are completely uploaded and fine
{ [5 bytes data]
< HTTP/2 200
< date: Tue, 05 Mar 2024 04:21:52 GMT
< content-type: application/json; charset=utf-8
< content-length: 832
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 23937701312372758
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 98
< x-ratelimit-reset: 1709612563
< timing-allow-origin: *
<
{ [832 bytes data]
100   948  100   832  100   116    387     53  0:00:02  0:00:02 --:--:--   441
* Connection #0 to host api.clickup.com left intact
{
  "goal": {
    "id": "30d08601-5d56-4c1a-97b6-854cfcb0fbdc",
    "pretty_id": "53",
    "name": "Updated Goal Name",
    "team_id": "25747182",
    "creator": 43050475,
    "color": "#32a852",
    "date_created": "1709612113249",
    "start_date": null,
    "due_date": "1568036964079",
    "description": "Updated Goal Description",
    "private": false,
    "archived": false,
    "multiple_owners": true,
    "editor_token": "goal:30d08601-5d56-4c1a-97b6-854cfcb0fbdc:7adae990-ed97-4bc8-90a3-8e7bd263e719:0e612db3-47a2-4562-a535-e0ffcf59cb13",
    "date_updated": "1709612512162",
    "folder_id": null,
    "folder_name": null,
    "members": [],
    "group_members": [],
    "owners": [
      {
        "id": 43050475,
        "username": "carlos tito",
        "email": "crisbelwla@hotmail.com",
        "color": "#006063",
        "profilePicture": null,
        "initials": "CT"
      }
    ],
    "key_results": [],
    "key_result_count": 0,
    "percent_completed": 0,
    "history": [],
    "pretty_url": "https://app.clickup.com/25747182/goals/53"
  }
}

```
## DELETE request

Deleting a goal

```bash

curl -X DELETE "https://api.clickup.com/api/v2/goal/30d08601-5d56-4c1a-97b6-854cfcb0fbdc" -H "Authorization: $TokenId" -H 'Content-Type: application/json' -v |jq
$ curl -X DELETE "https://api.clickup.com/api/v2/goal/30d08601-5d56-4c1a-97b6-854cfcb0fbdc" -H "Authorization: $APIToken" -H 'Content-Type: application/json' -v |jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 52.65.208.115:443...
* Connected to api.clickup.com (52.65.208.115) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
*  CAfile: C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
*  CApath: none
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched certs "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0* Using HTTP2, server supports multiplexing
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
} [5 bytes data]
* Using Stream ID: 1 (easy handle 0x27f10f420a0)
} [5 bytes data]
> DELETE /api/v2/goal/30d08601-5d56-4c1a-97b6-854cfcb0fbdc HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.80.0
> accept: */*
> authorization: pk_43050475_WP16359UNWJ251JTJO2VTQB97J9IRVC6
> content-type: application/json
>
{ [5 bytes data]
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
} [5 bytes data]
< HTTP/2 200
< date: Tue, 05 Mar 2024 04:24:28 GMT
< content-type: application/json; charset=utf-8
< content-length: 2
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 444572843384018983
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 99
< x-ratelimit-reset: 1709612729
< timing-allow-origin: *
<
{ [2 bytes data]
100     2  100     2    0     0      1      0  0:00:02  0:00:01  0:00:01     1
* Connection #0 to host api.clickup.com left intact
{}
```
## Negative case 1

Triying to create a new goal using an invalid TeamId

```bash
$ curl -X POST "https://api.clickup.com/api/v2/team/$TeamId/goal" -H "Authorization: $APIToken" -H 'Content-Type: application/json' -d '{"name": "Goal Name","due_date": 1568036964079,"description": "Goal Description","multiple_owners": true,"owners": [183],"color": "#32a852"}' -v|jq
Note: Unnecessary use of -X or --request, POST is already inferred.
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 3.105.185.43:443...
* Connected to api.clickup.com (3.105.185.43) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
*  CAfile: C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
*  CApath: none
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched certs "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
* Using HTTP2, server supports multiplexing
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
} [5 bytes data]
* Using Stream ID: 1 (easy handle 0x1d956022070)
} [5 bytes data]
> POST /api/v2/team/25747182/goal HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.80.0
> accept: */*
> authorization: pk_43050475_WP16359UNWJ251JTJO2VTQB97J9IRVC6
> content-type: application/json
> content-length: 140
>
{ [5 bytes data]
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
} [5 bytes data]
* We are completely uploaded and fine
{ [5 bytes data]
< HTTP/2 404
< date: Tue, 05 Mar 2024 04:05:33 GMT
< content-type: application/json; charset=utf-8
< content-length: 175
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 8373195413439022931
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 99
< x-ratelimit-reset: 1709611594
< timing-allow-origin: *
<
{ [175 bytes data]
100   315  100   175  100   140    112     89  0:00:01  0:00:01 --:--:--   202
* Connection #0 to host api.clickup.com left intact
{
  "err": "Team not found",
  "ECODE": "ACCESS_002",
  "meta": {
    "authorization_failures": [
      {
        "object_id": "25747182",
        "object_type": "workspace",
        "workspace_id": 25747182,
        "code": "NOT_FOUND"
      }
    ]
  }
}
```
## Negative case 2

When trying to update a goal using PATCH request, the API does not support that request like using a POST request

```bash
$ curl -X PATCH "https://api.clickup.com/api/v2/goal/30d08601-5d56-4c1a-97b6-854cfcb0fbdc" -H "Authorization: $APIToken" -H "Content-Type: application/json" -d '{"name": "Updated Goal Name","due_date": 1568036964079,"description": "Updated Goal Description","color": "#32a852"}' -v|jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 3.105.185.43:443...
* Connected to api.clickup.com (3.105.185.43) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
*  CAfile: C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
*  CApath: none
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched certs "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0* Using HTTP2, server supports multiplexing
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
} [5 bytes data]
* Using Stream ID: 1 (easy handle 0x1c70cac2d20)
} [5 bytes data]
> PATCH /api/v2/goal/30d08601-5d56-4c1a-97b6-854cfcb0fbdc HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.80.0
> accept: */*
> authorization: pk_43050475_WP16359UNWJ251JTJO2VTQB97J9IRVC6
> content-type: application/json
> content-length: 116
>
{ [5 bytes data]
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
} [5 bytes data]
* We are completely uploaded and fine
{ [5 bytes data]
< HTTP/2 404
< date: Tue, 05 Mar 2024 04:28:25 GMT
< content-type: text/html; charset=utf-8
< content-length: 189
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< x-datadog-trace-id: 6010927831720294078
< content-security-policy: default-src 'none'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 98
< x-ratelimit-reset: 1709612933
< timing-allow-origin: *
<
{ [189 bytes data]
100   305  100   189  100   116    134     82  0:00:01  0:00:01 --:--:--   216jq: parse error: Invalid numeric literal at line 1, column 10

* Connection #0 to host api.clickup.com left intact
```
## Negative case 3

Error using POST request sending an not existing TemplateId to create a new task template

```bash
$ curl -X POST https://api.clickup.com/api/v2/list/187740038/taskTemplate/rhqqe-42 -H "Authorization: $APIToken" -H "Content-Type: application/json" -d '{"name": "New task name"}' -v | jq
Note: Unnecessary use of -X or --request, POST is already inferred.
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 3.105.191.228:443...
* Connected to api.clickup.com (3.105.191.228) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
*  CAfile: C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
*  CApath: none
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched certs "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
* Using HTTP2, server supports multiplexing
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
} [5 bytes data]
* Using Stream ID: 1 (easy handle 0x274c3322090)
} [5 bytes data]
> POST /api/v2/list/187740038/taskTemplate/rhqqe-42 HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.80.0
> accept: */*
> authorization: pk_43050475_WP16359UNWJ251JTJO2VTQB97J9IRVC6
> content-type: application/json
> content-length: 25
>
{ [5 bytes data]
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
} [5 bytes data]
* We are completely uploaded and fine
{ [5 bytes data]
100    25    0     0  100    25      0      3  0:00:08  0:00:07  0:00:01     0
< HTTP/2 404
< date: Tue, 05 Mar 2024 04:58:57 GMT
< content-type: application/json; charset=utf-8
< content-length: 49
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 3200317380705597731
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 98
< x-ratelimit-reset: 1709614770
< timing-allow-origin: *
<
{ [49 bytes data]
100    74  100    49  100    25      5      2  0:00:12  0:00:08  0:00:04    12
* Connection #0 to host api.clickup.com left intact
{
  "err": "Template not found",
  "ECODE": "TEMPLH_019"
}
```
## Negative case 4
Unable to create a new user group because of the limits of using a free version of the app 

```bash
$ curl -X POST "https://api.clickup.com/api/v2/team/$TeamId/group" -H "Authorization: $APIToken" -H "Content-Type: application/json" -d '{"name": "New team name","members": [123456,987654]}' -v | jq
Note: Unnecessary use of -X or --request, POST is already inferred.
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 52.65.208.115:443...
* Connected to api.clickup.com (52.65.208.115) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
*  CAfile: C:/Program Files/Git/mingw64/ssl/certs/ca-bundle.crt
*  CApath: none
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [104 bytes data]
* TLSv1.2 (IN), TLS handshake, Certificate (11):
{ [4943 bytes data]
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
{ [333 bytes data]
* TLSv1.2 (IN), TLS handshake, Server finished (14):
{ [4 bytes data]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
} [70 bytes data]
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.2 (OUT), TLS handshake, Finished (20):
} [16 bytes data]
* TLSv1.2 (IN), TLS handshake, Finished (20):
{ [16 bytes data]
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=*.clickup.com
*  start date: Dec  2 00:00:00 2023 GMT
*  expire date: Dec 30 23:59:59 2024 GMT
*  subjectAltName: host "api.clickup.com" matched certs "*.clickup.com"
*  issuer: C=US; O=Amazon; CN=Amazon RSA 2048 M02
*  SSL certificate verify ok.
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0* Using HTTP2, server supports multiplexing
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
} [5 bytes data]
* Using Stream ID: 1 (easy handle 0x17af3712030)
} [5 bytes data]
> POST /api/v2/team/25747182/group HTTP/2
> Host: api.clickup.com
> user-agent: curl/7.80.0
> accept: */*
> authorization: pk_43050475_WP16359UNWJ251JTJO2VTQB97J9IRVC6
> content-type: application/json
> content-length: 52
>
{ [5 bytes data]
* Connection state changed (MAX_CONCURRENT_STREAMS == 128)!
} [5 bytes data]
* We are completely uploaded and fine
{ [5 bytes data]
< HTTP/2 403
< date: Tue, 05 Mar 2024 05:05:09 GMT
< content-type: application/json; charset=utf-8
< content-length: 108
< server: nginx
< x-dns-prefetch-control: off
< expect-ct: max-age=0
< strict-transport-security: max-age=31536000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-permitted-cross-domain-policies: none
< x-xss-protection: 0
< access-control-allow-origin: *
< access-control-allow-credentials: true
< content-language: en-US
< x-datadog-trace-id: 5705360606853675390
< content-security-policy: frame-ancestors 'self'
< cache-control: no-cache
< cache-control: no-store
< pragma: no-cache
< expires: 0
< x-ratelimit-limit: 100
< x-ratelimit-remaining: 98
< x-ratelimit-reset: 1709615156
< timing-allow-origin: *
<
{ [108 bytes data]
100   160  100   108  100    52     52     25  0:00:02  0:00:02 --:--:--    77
* Connection #0 to host api.clickup.com left intact
{
  "err": "Your plan is limited to {{limit}} usages of Additional Teams, {{usage}} usage.",
  "ECODE": "GROUP_027"
}
```