#!/bin/bash
# takes url as argument and sends get request with a header
curl -sfL $1 -H "X-School-User-Id: 98"
