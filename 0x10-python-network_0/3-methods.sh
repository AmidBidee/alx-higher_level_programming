#!/bin/bash
# takes a url as arguments and returns all request methods
curl -sX "OPTIONS" $1
