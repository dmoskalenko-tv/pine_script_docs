#!/bin/bash
rm -rf build/
make html
python3 processLink.py
