#from django import forms
#from django.http import HttpResponseRedirect

from mezzanine.pages.page_processors import processor_for
from .models import Organization, Residency

#class AuthorForm(forms.Form):
    #name = forms.CharField()
    #email = forms.EmailField()

@processor_for(Organization)
def organization_display(request, page):
    reslist = Residency.objects.all()
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
