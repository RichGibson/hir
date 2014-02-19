from __future__ import unicode_literals

import os


print "HERE"
import sys
sys.exit(2)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
print "settings_module:",settings_module
settings_module='settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
