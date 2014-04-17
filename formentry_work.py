from django.core.management import setup_environ
#from hir import settings
import settings
setup_environ(settings)

from mezzanine.forms.models import *
from mezzanine.utils.urls import admin_url, slugify, unique_slug
import sys




####

def return_formentry(slug):
    """ take a form slug, possibly other filter conditions, return form entry
        results.  """

    # A 'form' is the description and fields for a form.
    print >>sys.stderr,"formentry_work slug:%r" % slug
    single_form = Form.objects.get(slug=slug)

    # A 'form entry' represents an instance of filling out a form.
    # this formentry_list contains all of the filled out forms with the 
    # passed in slug.
    formentry_list=FormEntry.objects.filter(form_id=single_form.id)

    label_list = [ ]
    field_list = Field.objects.filter(form_id=single_form.id)
    fieldsByID = {f.id:f for f in field_list}

    #for field in fieldsByID:
    #    print "field_id: %r field: %r" % (field, fieldsByID[field] )

    entrylist = [ ]
    entrydictlist = [ ]

    # I want a list of formentries?
    # now I build a list of data entries
    for formentry in formentry_list:
        entry={} 
        entrydict={} 
        fieldentry_list = FieldEntry.objects.filter(entry_id=formentry.id)
        for fieldentry in fieldentry_list:
            fieldid =fieldentry.field_id
            slug  = slugify(fieldsByID[fieldentry.field_id])
            value =fieldentry.value
            #print "try label:%s slug:%s value:%s " % (fieldsByID[fieldentry.field_id] , slug, fieldentry.value)
            entry[fieldsByID[fieldentry.field_id]] = fieldentry
            entrydict[slug] = value
        entrylist.append(entry)
        entrydictlist.append(entrydict)

    rv = {}
    rv['slug'] = slug
    rv['fieldsByID'] = fieldsByID
    rv['entrylist']=entrylist
    rv['entrydictlist']=entrydictlist
    return rv


####


form_slug = 'organization'
rv = return_formentry(form_slug)
print "---------------------------"
#print rv

import pdb

for field in rv['fieldsByID']:
    print "field: %r" % field


for org in rv['entrydictlist']:
    print "name:%s" % org['name']


sys.exit(2)
# wtf is an entry? Field: FieldEntry?
# 

print "..............."
for entry in rv['entrylist']:
    print "new space.............."
    print "use fields by id"
    print type(entry)
    #pdb.set_trace()
    #print "entry.id: %i:" % entry['id']

    for key,field in entry.items():
        #print key
        print "%s: %s " % (key,field.value)
        print "label? %s" (field.label)

"""
Next steps...

routine: pass a form name or slug, get a list of form_entry objects back? 

put that in a view.





"""
