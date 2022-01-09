#!/bin/bash
# takes a url/uri as argument and sends a delete request
curl -s $1 -X DELETE
