#!/usr/bin/env bash
[ -z "$1" ] && { echo "Usage: $0 <URL>"; exit 1; }
curl -s "$1" | wc -c
