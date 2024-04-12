#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import Request, urlopen

if __name__ == "__main__":
    req = Request("https://alx-intranet.hbtn.io/status")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text)) 
