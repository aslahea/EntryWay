#!/bin/bash

# Go to project root if not already there
cd "$(dirname "$0")"

# Run inside Django_Project folder
cd Django_Project

# Apply DB migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Use default port 8000 if $PORT is not set (for local testing)
PORT=${PORT:-8000}

# Start Gunicorn
gunicorn Web_Base.wsgi:application --bind 0.0.0.0:$PORT
