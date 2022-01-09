#!/bin/bash
# takes a url as arguments and returns all request methods
curl -sI $1 -X OPTIONS | grep "Allow" | cut -d " " -f2-
