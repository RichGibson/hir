from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from mezzanine.pages.admin import PageAdmin
from .models import Organization,Residency
from .models import OfferSkeleton,RequiredSkeleton

#class OfferSkeletonAdmin(admin.ModelAdmin):
#    list_display  = ('slug', 'status', 'sortorder')
#    search_fields = ('slug','label', 'summary','notes')
#    list_editable = ('status','sortorder')

#class RequiredSkeletonAdmin(admin.ModelAdmin):
#    list_display  = ('slug', 'status', 'sortorder')
#    search_fields = ('slug','label', 'summary','notes')
#    list_editable = ('status','sortorder')

#admin.site.register(OfferSkeleton, OfferSkeletonAdmin)
#admin.site.register(RequiredSkeleton, RequiredSkeletonAdmin)

admin.site.register(Organization, PageAdmin)
admin.site.register(Residency, PageAdmin)
