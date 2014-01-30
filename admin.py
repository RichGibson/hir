from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Space,Residency

admin.site.register(Space, PageAdmin)
admin.site.register(Residency, PageAdmin)
