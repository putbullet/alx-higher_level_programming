#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
from urllib.request import Request, urlopen
from urllib.pare import urlencode
from sys import argv


if __name__ == "__main__":
    """
    takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
    """
url = argv[1]
values = { 'email': argv[2]}
data = urlencode(values)
data = data.encode('ascii')
req = Request(url, data)
with urlopen(req) as response:
    posted = response.read()
    posted_req = posted.decode('utf-8')
print(posted_req)
