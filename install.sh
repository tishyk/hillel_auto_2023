#!/bin/bash
# Python and viertualenv installed at this point

EGG_INFO_DIR="*.egg-info"
VENV_NAME="hillel_venv"

echo "Removing existing log temporary files"
rm -rf .*.log
rm -rf ${EGG_INFO_DIR}

echo "Removing existing virtualenv directory <$VENV_NAME>"
rm -rf $VENV_NAME
echo "Creating a new virtualenv <$VENV_NAME>"
python -m virtualenv $VENV_NAME
# Activate for linux
source "$VENV_NAME/bin/activate"
# Activate for windows
hillel_venv/Scripts/activate
pip install -r requirements.txt
pip install -e demo
#pip install -e ./src




