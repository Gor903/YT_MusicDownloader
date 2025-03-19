#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

source $SCRIPT_DIR/venv/bin/activate
python $SCRIPT_DIR/main.py $1
file=$(find $SCRIPT_DIR/temp -type f)
ffmpeg -i "$file" -metadata Container=""  "/home/$(whoami)/Music/$(basename "$file")"
rm -rf "$SCRIPT_DIR/temp/$(basename "$file")"
exit

