#!/bin/bash

resp=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [ "$resp" -eq 200 ]; then
	curl -s "$1"
fi


