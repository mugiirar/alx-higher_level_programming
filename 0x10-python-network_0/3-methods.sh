#!/bin/bash
# allowed methods
curl -sIX HEADER "$1" | grep -i "Allow" | cut -d " " -f 2-
