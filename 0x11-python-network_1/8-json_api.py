#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

sage: ./8-json_api.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
from sys import argv
import requests


if __name__ == "__main__":

    if len(argv) == 1:
        letter = ""
    else:
        letter = argv[1]
    letters = { 'q': letter }
    req = requests.post('http://0.0.0.0:5000/search_user' , data=letters)

    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
