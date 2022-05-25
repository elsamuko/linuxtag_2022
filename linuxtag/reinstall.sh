#!/usr/bin/env bash

# pip install --upgrade pip
# pip install --upgrade setuptools

function indent {
    sed 's/^/    /'
}

function green  {
    echo -e "\033[1;32m$*\033[0m"
}

green "Removing old package"
python3 -m pip uninstall linuxtag --yes 2>&1 | indent

green "Cleaning build"
python3 setup.py clean --all 2>&1 | indent
rm -rf linuxtag.egg-info

green "Installing new package"
python3 -m pip install --user . 2>&1 | indent
