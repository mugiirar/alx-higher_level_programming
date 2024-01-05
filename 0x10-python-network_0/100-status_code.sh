#!/bin/bash
# get request and response
curl -so /dev/null -w "%{http_code}" "$1"
