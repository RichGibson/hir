from django.http import HttpResponse
from mezzanine.forms.models import Form
from mezzanine.forms.models import FormEntry
from mezzanine.forms.models import FieldEntry
from mezzanine.forms.forms import EntriesForm
from mezzanine.forms.models import Field
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
#from mezzanine.forms.admin import FormAdmin

#from django.core.management import setup_environ
#import settings
#setup_environ(settings)

from mezzanine.forms.models import *


import sys


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
            print >>sys.stderr,fieldsByID[fieldentry.field_id] 
            entry[fieldsByID[fieldentry.field_id]] = fieldentry
            print >>sys.stderr,fieldentry
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


#for formentry in rv['formentry_list']:
#    print formentry

def list(request, slug=None):
    rv = return_formentry(slug)
    return render_to_response('list.html', {'rv':rv, 'entrylist': rv['entrylist']})

def rawlist(request, slug=None):
    
    rv = return_formentry(slug)
    #rv = Form.objects.all()
    #return render_to_response('rawlist.html', {'rv':rv, 'entrylist': None})
    return render_to_response('rawlist.html', {'rv':rv, 'entrylist': rv['entrylist']})
