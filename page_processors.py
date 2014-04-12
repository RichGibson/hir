#from django import forms
#from django.http import HttpResponseRedirect

import sys

from django import forms
from django.forms import ModelForm, Textarea

from django.http import HttpResponseRedirect

from mezzanine.pages.page_processors import processor_for
from .models import Organization, Residency

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


@processor_for('add-a-residency-opportunity')
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


@processor_for('add-organization')
def organization_form(request, page):
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


@processor_for('list-of-organizations')
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
