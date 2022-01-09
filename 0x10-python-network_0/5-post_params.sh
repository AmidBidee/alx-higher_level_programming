#!/bin/bash
# takes url as argument sends a post request and displays response body
curl -sfL $1 -X POST -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD"
