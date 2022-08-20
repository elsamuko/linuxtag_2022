#!/usr/bin/env bash

function indent {
    sed 's/^/    /'
}

function green  {
    echo -e "\033[1;32m$*\033[0m"
}

echo
green "Before venv"
(
    python3 -m pip show pip
    python3 -m pip --version
) | indent

echo
green "Activating venv"
(
    mkdir -p venv
    cd venv || exit
    python3 -m venv .

    source bin/activate
    echo "pip==22.2" > requirements.txt
    python3 -m pip install -r requirements.txt
    python3 -m pip show pip
    python3 -m pip --version

    deactivate
) | indent
