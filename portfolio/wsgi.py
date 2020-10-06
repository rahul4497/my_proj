"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

#application = get_wsgi_application()

import os
import sys
sys.path.append('/opt/bitnami/apps/django/django_projects/my-proj')
os.environ.setdefault("PYTHON_EGG_CACHE", "/opt/bitnami/apps/django/django_projects/my-proj/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my-proj.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
