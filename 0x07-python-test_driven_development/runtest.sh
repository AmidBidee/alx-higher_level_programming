#!/usr/bin/bash
python3 -m doctest -v ./tests/*.txt | tail -2
echo "======== checking code style ========="
echo "--------------------------------------"
pycodestyle *.py
