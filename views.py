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
from mezzanine.utils.urls import admin_url, slugify, unique_slug

#from mezzanine.pages.models import Page


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

def list(request, slug=None):
    rv = return_formentry(slug)
    return render_to_response('list.html', {'rv':rv, 'entrylist': rv['entrylist']})

def rawlist(request, slug=None):
    rv = return_formentry(slug)
    for entry in rv['entrydictlist']:
        print >>sys.stderr, "%s" % (entry['name'])
        #for key,field in entry.items():
        #    print >>sys.stderr, "%s: %s" % (key,field.value)
    #rv = Form.objects.all()
    #return render_to_response('rawlist.html', {'rv':rv, 'entrylist': None})
    return render_to_response('rawlist.html', {'rv':rv, 'entrylist': rv['entrydictlist']})

def showorganization(request, organization=None):
    rv = Page.objects.all()
    print >>sys.stderr,"organization, name: ", organization
    #return render_to_response('pages/show_organization.html', {'rv':rv})
    return render_to_response('pages/show_organization.html')
