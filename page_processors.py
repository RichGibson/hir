#from django import forms
#from django.http import HttpResponseRedirect

import sys
from mezzanine.pages.page_processors import processor_for
from .models import Organization, Residency

#class AuthorForm(forms.Form):
    #name = forms.CharField()
    #email = forms.EmailField()

@processor_for(Organization)
def organization_display(request, page):
    reslist = Residency.objects.filter(organization=page.id)
    return {"reslist": reslist}

@processor_for('list-of-organizations')
def organization_list(request,page):
    orglist = Organization.objects.all()
    return {"orglist": orglist}

@processor_for('list-of-residencies')
def residency_list(request,page):
    reslist = Residency.objects.all()
    # this is where we could do the offer/requires formatting, but 
    # I am doing it in a template_tag. 
    #for res in reslist:
    #    pass    
    return {"reslist": reslist}

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
