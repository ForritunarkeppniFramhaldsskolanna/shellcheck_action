#!/usr/bin/bash
shopt -s nullglob
set -e
shellcheck "$1" --format=json "$2" | python3 parse_output.py
