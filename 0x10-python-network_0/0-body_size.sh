#!/bin/bash

if [ "$#" -eq 0 ]; then
	echo "Give url"
	exit 1

 else
	curl -s "$#" | wc -c
fi
