
from django.db import models
from mezzanine.pages.models import Page, RichText

# The members of Page will be inherited by the Author model, such
# as title, slug, etc. For authors we can use the title field to
# store the author's name. For our model definition, we just add
# any extra fields that aren't part of the Page model, in this
# case, date of birth.


class Offer(models.Model):
    """What is being offered to a resident?""""
    slug = models.CharField(max_length=80, blank=True, null=True, 
                help_text="What is being offered. Ex 'Housing'")
    status = models.CharField(max_length=1, blank=True, null=True, default="N", 
                help_text="Is it offered? Y(es), N(o), M(aybe/negotiable)"
    summary = models.CharField(max_length=80, blank=True, null=True, 
                help_text="One line summary of what is being offered")
    notes = models.TextField(blank=True, null=True, 
                help_text="Full description of what is being offered")
    sortorder = models.IntegerField(
                help_text="sort order, Offer items are displayed in this order.")

class Required(models.Model):
    """What is being required from a resident?""""
    slug = models.CharField(max_length=80, blank=True, null=True, 
                help_text="What is required. Ex 'Give a Talk(s)'")
    status = models.CharField(max_length=1, blank=True, null=True, default="N", 
                help_text="Is it required? Y(es), N(o), M(aybe/negotiable)"
    summary = models.CharField(max_length=80, blank=True, null=True, 
                help_text="One line summary of what is required")
    notes = models.TextField(blank=True, null=True, 
                help_text="Full description of what is required")
    sortorder = models.IntegerField(
                help_text="sort order, Required items are displayed in this order.")

class Residency(Page, RichText):
    offer= models.TextField()
    resources= models.TextField()

# follow layout of the hackerspaces.org wiki for now
class Space(Page, RichText):
    name = models.CharField(max_length=200)
    hackerspace = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.CharField(max_length=100)

