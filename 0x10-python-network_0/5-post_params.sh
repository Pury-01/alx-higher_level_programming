#!/bin/bash
# sends POST request to the passed URL and display body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
