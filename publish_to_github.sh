#!/bin/sh
# pelican content -o output -s pelicanconf.py
make publish
ghp-import output
git push origin gh-pages:master
