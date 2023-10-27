#!/bin/bash
# Python and pip should be installed at this point

EGG_INFO_DIR="*.egg-info"
VENV_NAME="hillel_venv"

echo "Removing existing log temporary files"
rm -rf .*.log
rm -rf ${EGG_INFO_DIR}

echo "Removing existing virtualenv directory <$VENV_NAME>"
rm -rf $VENV_NAME

echo "Removing pytest_cache"
rm -rf .pytest_cache

echo "Creating a new virtualenv <$VENV_NAME>"
pip install virtualenv
python -m virtualenv $VENV_NAME

echo "Virtual environment initialization"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        source "$VENV_NAME/bin/activate"
elif [[ "$OSTYPE" == "darwin"* ]]; then
        # Mac OSX
        source "$VENV_NAME/bin/activate"
elif [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
        source "$VENV_NAME/Scripts/activate"
elif [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
        source "$VENV_NAME/Scripts/activate"
elif [[ "$OSTYPE" == "win32" ]]; then
        # I'm not sure this can happen.
        source "$VENV_NAME/Scripts/activate"
else
        echo "Unknown OS found. Script will be exit"
        exit 1
fi
echo "Installing environment dependencies ..."
pip install -r requirements.txt
pip install -e .
echo "All done"




