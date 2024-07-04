#!/bin/bash
# takes URL and displays all the http methods the server accept
curl -sI "$1" | grep "Allow" | cut -d ' ' -f 2-
