#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# main() is called when the file is executed
def main():

    """Run administrative tasks."""
    # Tell Django which settings module to load *if* none is set already.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviesite.settings')

    try:

        #Import is inside try/except so we can show a friendly error if Django isn’t installed or the venv isn’t activated.
        from django.core.management import execute_from_command_line

    except ImportError as exc:

        # If Django not found error-message is displayed to the user
        raise ImportError(

            # If Django cannot be imported, this is the error message displayed
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"

        ) from exc

    execute_from_command_line(sys.argv)

# Ensures that main only runs when the file is executed directly (not imported).
if __name__ == '__main__':

    main()
