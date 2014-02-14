from django.core.management import setup_environ
#from hir import settings
import settings
setup_environ(settings)

from mezzanine.forms.models import *
import sys




####

def return_formentry(slug):
    """ take a form slug, possibly other filter conditions, return form entry
        results.  """

    # A 'form' is the description and fields for a form.
    print >>sys.stderr,"slug:%r" % slug
    single_form = Form.objects.get(slug=slug)

    # A 'form entry' represents an instance of filling out a form.
    # this formentry_list contains all of the filled out forms with the 
    # passed in slug.
    formentry_list=FormEntry.objects.filter(form_id=single_form.id)

    label_list = [ ]
    field_list = Field.objects.filter(form_id=single_form.id)
    fieldsByID = {f.id:f for f in field_list}

    #for field in field_list:
    #    print field.id, field.label


    for field in fieldsByID:
        print "field_id: %r field: %r" % (field, fieldsByID[field] )
        #print dir(fieldsByID[field])

    entrylist = [ ]

    # I want a list of formentries?
    # now I build a list of data entries
    for formentry in formentry_list:
        #print dir(formentry)
        entry={} 
        fieldentry_list = FieldEntry.objects.filter(entry_id=formentry.id)
        for fieldentry in fieldentry_list:
            #entrylist.append(fieldentry)
            #print fieldsByID[fieldentry.field_id] 
            entry[fieldsByID[fieldentry.field_id]] = fieldentry
        entrylist.append(entry)

        #print type(formentry)
        #formentry['entrylist'] = entrylist

    for entry in entrylist:
        for key,value in entry.items():
            print key
        #print "%s: %s" % (fieldsByID[entry.field_id],entry.value)

    #print entrylist

    rv = {}
    rv['slug'] = slug
    rv['fieldsByID'] = fieldsByID
    rv['entrylist']=entrylist
    return rv


#form_slug = 'organizationspace'

####

def Xreturn_formentry(slug):
    """ take a form slug, possibly other filter conditions, return form entry
        results.  """

    # A 'form' is the description and fields for a form.
    print >>sys.stderr,"slug:%r" % slug
    
    single_form = Form.objects.get(slug=slug)

    # A 'form entry' represents an instance of filling out a form.
    # this formentry_list contains all of the filled out forms with the 
    # passed in slug.
    formentry_list=FormEntry.objects.filter(form_id=single_form.id)

    label_list = [ ]
    field_list = Field.objects.filter(form_id=single_form.id)
    fieldsByID = {f.id:f for f in field_list}

    #for field in field_list:
    #    print field.id, field.label


    for field in fieldsByID:
        print "field_id: %r field: %r" % (field, fieldsByID[field] )
        #print dir(fieldsByID[field])

    entrylist = [ ]

    # I want a list of formentries?
    # now I build a list of data entries
    for formentry in formentry_list:
        #print dir(formentry)
        fieldentry_list = FieldEntry.objects.filter(entry_id=formentry.id)
        for fieldentry in fieldentry_list:
            entrylist.append(fieldentry)

    #for entry in entrylist:
    #    print "%s: %s" % (fieldsByID[entry.field_id],entry.value)

    rv = {}
    rv['fieldsByID'] = fieldsByID
    rv['entrylist']=entrylist
    return rv




form_slug = 'organizationspace'
rv = return_formentry(form_slug)
print "---------------------------"
#print rv


for entry in rv['entrylist']:
    print "new space.............."
    for key,field in entry.items():
        #print key
        print "%s: %s" % (key,field.value)

"""
Next steps...

routine: pass a form name or slug, get a list of form_entry objects back? 

put that in a view.





"""
