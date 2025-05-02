#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

# Standard Library imports
import os
import sys


def main():

    """Run administrative tasks."""

    # Sets the default settings for Django to this project
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finalprojectJoseSaumat.settings')

    # Attempts to run Django
    try:

        # Imports the function that handles all commands from the manage.py file
        from django.core.management import execute_from_command_line

    # Throws an exception if Django missing
    except ImportError as exc:

        # Error message if Django is not installed or missing
        raise ImportError(

            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"

        ) from exc

    # Executes the command to run the server and make migrations
    execute_from_command_line(sys.argv)

# If this file is called to run it calls the main function
if __name__ == '__main__':

    main()
