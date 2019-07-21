#!/bin/sh

if [ -f 'config.py' ]; then
    echo "config.py already exists!"
else
    echo "url = \nreader = " > config.py
fi

