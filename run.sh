#source "$VENV_NAME/bin/activate"
# Activate for windows
# source hillel_venv/Scripts/activate
. hillel_venv/bin/activate

python -m pytest -s "$@"

# run from terminal
# ./run.sh test_selenium_first_steps.py