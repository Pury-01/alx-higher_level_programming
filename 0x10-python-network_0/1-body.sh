#!/bin/bash
# takes URL, sends a GET request to the URL, and displays the body of the response
curl -s "$1" -w "%{http_code}" | grep -q "200$"
