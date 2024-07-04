#!/bin/bash
# sends DELETE request to the URL passed as first argument
echo ""; curl -s -X DELETE "$1"
