"""
WSGI config for dpsPortfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dpsPortfolio.settings.base import SETTINGS_FILE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dpsPortfolio.settings.{}'.format(SETTINGS_FILE))

application = get_wsgi_application()
