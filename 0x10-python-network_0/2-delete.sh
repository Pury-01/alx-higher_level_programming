#!/bin/bash
# sends DELETE request to the URL passed as first argument
curl -s -X DELETE "$1"; echo ""
