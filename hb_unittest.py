#!/usr/bin/python3

import json
from headerbreakdown import HeaderBreakdown

# header with multiple Host, and User-Agent values
#H1 = "GET /?gws_rd=ssl HTTP/1.1\r\nHost: www.google.com\r\nHost: www.bing.com\r\nHost: www.yahoo.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/99.0\r\nCookie: 1P_JAR=2021-03-13-04"
# header with multiple Host, Method/Path, and User-Agent values
H1 = "GET /?gws_rd=ssl HTTP/1.1\r\nDELETE /AAAA HTTP/1.1\r\nHost: www.google.com\r\nHost: www.bing.com\r\nHost: www.yahoo.com\r\nConnection: keep-alive\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/99.0\r\nCookie: 1P_JAR=2021-03-13-04"
# single header as a plain string (with no \r\n)
# note the nested_direction_* attributes will be type None with this sort of direction-ambiguous header
H2 = "Set-Cookie: k1=v1;k2=v2"
# normal header examples that terminate with \r\n\r\n
H3 = "HTTP/1.1 302 Found\r\nLocation: https://www.google.com/?gws_rd=ssl\r\nCache-Control: private\r\nContent-Type: text/html; charset=UTF-8\r\nDate: Sat, 13 Mar 2021 04:15:44 GMT\r\nServer: gws\r\nContent-Length: 231\r\nX-XSS-Protection: 0\r\nX-Frame-Options: SAMEORIGIN\r\nSet-Cookie: 1P_JAR=2021-03-13-04; expires=Mon, 12-Apr-2021 04:15:44 GMT; path=/; domain=.google.com; Secure; SameSite=none\r\n\r\n"
H4 = "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nSet-Cookie: k1=v1;k2=v2\r\n\r\n"
H5 = "GET / HTTP/1.1\r\nHost: google.com\r\nUser-Agent: BLAHBLAH\r\nAccept: text/plain\r\n\r\n"
H6 = ["GET / HTTP/1.1", "Host: google.com", "User-Agent: BLAHBLAH", "Accept: text/plain"]

h1 = HeaderBreakdown(H1)
h2 = HeaderBreakdown(H2)
h3 = HeaderBreakdown(H3)
h4 = HeaderBreakdown(H4)
h5 = HeaderBreakdown(H5)
h6 = HeaderBreakdown(H6)
#print([type(i) for i in [h1, h2, h3, h4, h5]])

print(":"*50)
print(" parsed h1 ".center(20, "="))
print(json.dumps(h1.parsed, indent=4))
print(" parsed h2 ".center(20, "="))
print(json.dumps(h2.parsed, indent=4))
print(" parsed h3 ".center(20, "="))
print(json.dumps(h3.parsed, indent=4))
print(" parsed h4 ".center(20, "="))
print(json.dumps(h4.parsed, indent=4))
print(" parsed h5 ".center(20, "="))
print(json.dumps(h5.parsed, indent=4))
print(" parsed h6 ".center(20, "="))
print(json.dumps(h6.parsed, indent=4))

print(":"*50)
print(" analyzed h1 ".center(20, "="))
print(json.dumps(h1.analyzed, indent=4))
print(" analyzed h2 ".center(20, "="))
print(json.dumps(h2.analyzed, indent=4))
print(" analyzed h3 ".center(20, "="))
print(json.dumps(h3.analyzed, indent=4))
print(" analyzed h4 ".center(20, "="))
print(json.dumps(h4.analyzed, indent=4))
print(" analyzed h5 ".center(20, "="))
print(json.dumps(h5.analyzed, indent=4))
print(" analyzed h6 ".center(20, "="))
print(json.dumps(h6.analyzed, indent=4))

print(":"*50)
print(h1)
print("DIRECTION", h1._direction)
print("HOST", h1._host)
print("METHOD", h1._method)
print("PATH", h1._path)
print("VERS", h1._httpversion)
print("CODE", h3._responsecode)
print("PHRASE", h3._responsephrase)
print("DIRECTION", h6._direction)
print("HOST", h6._host)
print("METHOD", h6._method)


print(":"*50)
print(h1)