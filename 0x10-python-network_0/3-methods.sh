#!/bin/bash
#takes in a URL and displays all HTTP methods the server will accept.
curl -s -v -L "$1" | grep -o -E '> (GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH) '
