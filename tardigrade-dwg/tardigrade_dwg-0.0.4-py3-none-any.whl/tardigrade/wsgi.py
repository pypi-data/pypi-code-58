"""
WSGI config for dwg project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tardigrade.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
