#!/bin/bash
# get size of the body
if [ "$#" -eq 0 ]; then
	echo "Give url"
	exit 1

else
	echo "curl -s "$#" | wc -c"
fi
