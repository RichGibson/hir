from django.core.management import setup_environ
#from hir import settings
import settings
setup_environ(settings)

from mezzanine.forms.models import *

form_slug = 'organizationspace'
single_form = Form.objects.get(slug=form_slug)
formentry_list=FormEntry.objects.filter(form_id=single_form.id)
label_list = [ ]
field_list = Field.objects.filter(form_id=single_form.id)

print "Fields in form titled '%s' " % single_form.title
for field in field_list:
    print field.id, field.label

print 

entrylist = [ ]

# I want a list of formentries?
# now I build a list of data entries
for formentry in formentry_list:
    fieldentry_list = FieldEntry.objects.filter(entry_id=formentry.id)
    for fieldentry in fieldentry_list:
        entrylist.append(fieldentry)

for entry in entrylist:
    print dir(entry)

print entrylist

"""
Next steps...

routine: pass a form name or slug, get a list of form_entry objects back? 

put that in a view.





"""
