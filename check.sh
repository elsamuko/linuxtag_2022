#!/usr/bin/env bash

# sudo apt install mypy
# python3 -m pip install mypy
echo "Running mypy"
mypy --strict linuxtag/linuxtag

# sudo apt install flake8
# python3 -m pip install flake8
echo "Running flake8"
flake8 linuxtag/linuxtag
