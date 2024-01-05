#!/bin/bash
#allowed methods
curl -sIX HEAD "$1" | grep -i "Allow" | cut -d " " -f 2-
