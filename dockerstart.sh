#!/bin/sh
set -e

# Activate virtual environment
. /home/baklava/.venv/bin/activate

# Start Flask with gunicorn
exec gunicorn --bind 0.0.0.0:8000 app:app
