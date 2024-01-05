#!/bin/bash
#allowed methods
curl -IX HEAD "$1" | grep -i "Allow" | cut -d " " -f 2-
