#!/usr/bin/env bash

# python3 -m pip install mypy
echo "mypy"
mypy --strict linuxtag

# python3 -m pip install flake8
echo "flake8"
flake8 -v linuxtag
