#!/usr/bin/bash
# displays the size of the body of the response
[ -n "$1" ] && curl -s "$1" | wc -c
