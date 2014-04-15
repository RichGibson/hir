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

from django import forms
from django.forms import ModelForm, Textarea
from django.http import HttpResponseRedirect

from models import Organization, Residency

import sys

########################################################################

class OrganizationForm(ModelForm):
    #about = forms.CharField(label="foobar")
    print >>sys.stderr, "organization form up top"
    class Meta:
        print >>sys.stderr, "organization form up top meta"
        model = Organization
        # the form displays the field in the order of this array.
        # maybe use the pages_page.title for our name
        fields=['name', 'website', 'street_address', 'city', 'state',
                'postal_code', 'country', 'email', 'phone', 'about' ]
                #'postal_code', 'country', 'email', 'phone', 'about']

        print >>sys.stderr,"before widgets"
        widgets = {
            'title': Textarea(attrs={'size':'100'}),
            'name': Textarea(attrs={'size':'1', 'rows':'1'}),
            'about': Textarea(attrs={'cols':'150', 'rows':'8'}),
        } 
        print >>sys.stderr,"widgets",widgets
        # i have seen examples with the numbers in quotes, and not in quotes.
        #'about': Textarea(attrs={'cols':'150', 'rows':'8'}),
        # these labels are not being used. The help_text from models is being
        # used.
        labels= {
            'title':'Organization Name',
            'name':'Organzation Name',
            'website':'Website',
            'street_address':'Street Address',
            'city':'City',
            'state':'State if applicable',
            'postal_code':'Postal Code if applicable',
            'country':'Country',
            'email':'Contact Email',
            'phone':'Phone',
        }
            #'about':'About our organization',
    #print >>sys.stderr,"what?"


class ResidencyForm(ModelForm):
    class Meta:
        model=Residency
        #exclude =['title','HEADER1','HEADER2','HEADER3']


@login_required
def residency_form(request, page):
    print >>sys.stderr, "in residency_form"
    form = ResidencyForm()
    if request.method == "POST":
        form = ResidencyForm(request.POST)
        if form.is_valid():
            # process form, like save data
            form.save()
            redirect = request.path + "?submitted=true"
            return HttpResponseRedirect(redirect)
    return {"form": form}


@login_required
def organization_form(request, page):
    """ for add_organization """
    print >>sys.stderr, "in organization_form"
    form = OrganizationForm()
    print >>sys.stderr, "after form=in organization_form"
    if request.method == "POST":
        form = OrganizationForm(request.POST)
        if form.is_valid():
            # process form, like save data
            # hmmm...how do I do this? I want the pages_page.title
            # to be the name field. oh well.
            #form.cleaned_data['title'] = form.cleaned_data['name']
            form.save()
            redirect = request.path + "?submitted=true"
            redirect = "/"
            return HttpResponseRedirect(redirect)
    return {"form": form}


## processor_for('list-of-organizations')
def organization_list(request,page):
    orglist = Organization.objects.all()
    print >>sys.stderr,"organization_list for list-of-organizations"
    return {"orglist": orglist}

@processor_for('list-of-residencies')
def residency_list(request,page):
    print >>sys.stderr,"residency_list for list-of-residencies"
    reslist = Residency.objects.all()
    return {"reslist": reslist}

@processor_for('show-residency')
def show_residency(request,page):
    print >>sys.stderr,"show-residency"

    slug=request.GET.get('res',None)
    print >>sys.stderr,"slug: %r", slug
    res=Residency.objects.filter(slug=slug)[0]

    org=res.organization
    return {"residency": res, "org": org}


@processor_for('add-a-residency-opportunity')
def show_organization(request,page):
    orgslug=request.GET.get('org',None)
    print >>sys.stderr, "add-a-residency-opportunity org:%r" % orgslug
    return


@processor_for('show-organization')
def show_organization(request,page):
    # this is where we could do the offer/requires formatting, but 
    # I am doing it in a template_tag. 
    #for res in reslist:
    #    pass    
    print >>sys.stderr,"show-organization"

    slug=request.GET.get('org',None)
    org=Organization.objects.filter(slug=slug)[0]

    print >>sys.stderr, "org?"
    print >>sys.stderr, org.name
    print >>sys.stderr, org.website
    print >>sys.stderr, org.city
    print >>sys.stderr, org.country
    reslist = Residency.objects.all()
    return {"reslist": reslist, "org":org}

#### this is from the docs.http://mezzanine.jupo.org/docs/content-architecture.html
#### basically exactly what I need :-/

#from django import forms
#from django.http import HttpResponseRedirect
#from mezzanine.pages.page_processors import processor_for
#from .models import Author

#class AuthorForm(forms.Form):
    #name = forms.CharField()
    #email = forms.EmailField()
#
#@processor_for(Author)
#def author_form(request, page):
    #form = AuthorForm()
    #if request.method == "POST":
        #form = AuthorForm(request.POST)
        #if form.is_valid():
            ## Form processing goes here.
            #redirect = request.path + "?submitted=true"
            #return HttpResponseRedirect(redirect)
    ##return {"form": form}
########################################################################
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
    print >>sys.stderr,"views.py list()"
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
