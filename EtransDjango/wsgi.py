"""
WSGI config for EtransDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EtransDjango.settings')
application = WhiteNoise(application, root=os.path.join(os.path.dirname(__file__), 'static'))
application = get_wsgi_application()

app = application