#!/bin/bash

# Check if the virtual environment is already activated
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual environment is already activated."
else
    echo "Activating the virtual environment..."
    source env/bin/activate
fi

# Run the Django development server
python manage.py runserver