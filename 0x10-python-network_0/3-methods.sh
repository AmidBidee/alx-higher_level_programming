#!/bin/bash
# takes a url as arguments and returns all request methods
curl $1 -X OPTIONS
