#!/bin/sh
# Rebuild every page and write the deployable flat files to the repo root.
set -e
cd "$(dirname "$0")"
python3 build.py
python3 flatten.py
rm -rf _site
