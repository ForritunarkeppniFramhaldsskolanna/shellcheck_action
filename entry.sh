#!/bin/bash
shopt -s nullglob
set -ex

files=$(eval 'for word in '"$1"'; do echo $word; done')
echo ${files[@]}

if [[ ${#files[@]} -ne 0 ]]; then
    shellcheck $2 --format=json ${files[@]} | python3 parse_output.py
fi
