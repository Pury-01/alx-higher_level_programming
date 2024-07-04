#!/bin/bash
# takes URL as argument, sends a GET request and displays body
curl -s -H "X-School-User-Id: 98" "$1"
