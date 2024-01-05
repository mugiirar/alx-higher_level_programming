#!/bin/bash
# get size of the body
if [ "$#" -eq 0 ]; then
	echo "Give url"
	exit 1

else
	curl -s "$#" | wc -c
fi
