#!/bin/bash
# takes in url as argument and prints the content-length
curl -sI $1 | grep -i Content-Length | awk '{print $2}'
