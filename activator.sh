#!/bin/bash

SCRIPT_DIR="$(pwd)"

source $SCRIPT_DIR/venv/bin/activate
python $SCRIPT_DIR/main.py $1 $SCRIPT_DIR
file=$(find $SCRIPT_DIR/temp -type f)

ffmpeg -i "$file" -metadata Container=""  "/home/$(whoami)/Music/$(basename "$file")"

rm -rf $file

exit

