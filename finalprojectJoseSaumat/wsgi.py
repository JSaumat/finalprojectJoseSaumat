"""
WSGI config for finalprojectJoseSaumat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# import os
#
# from django.core.wsgi import get_wsgi_application

# Sets the environment variable for the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finalprojectJoseSaumat.settings')

# Creates a WSGI application callable used by web servers
application = get_wsgi_application()
