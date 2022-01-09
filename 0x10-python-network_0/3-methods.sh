#!/bin/bash
# takes a url as arguments and returns all request methods
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
