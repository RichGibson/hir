
from django.db import models
from django.contrib.auth.models import User
from mezzanine.pages.models import Page, RichText

# The members of Page will be inherited by the Author model, such
# as title, slug, etc. For authors we can use the title field to
# store the author's name. For our model definition, we just add
# any extra fields that aren't part of the Page model, in this
# case, date of birth.


class OfferSkeleton(models.Model):
    """What things can be offered to a resident?"""
    slug = models.CharField(max_length=80, blank=True, null=True, 
                help_text="What is being offered. as a slug Ex 'Travel expenses' becomes travel_expenses'")
    label = models.CharField(max_length=80, blank=True, null=True, 
                help_text="What is being offered. Readable prompt Ex 'Travel Expenses'")
    status = models.CharField(max_length=1, blank=True, null=True, default="N", 
                help_text="Is it offered? Y(es), N(o), M(aybe/negotiable)")
    summary = models.CharField(max_length=80, blank=True, null=True, 
                help_text="One line summary of what is being offered")
    notes = models.TextField(blank=True, null=True, 
                help_text="Full description of what is being offered")
    sortorder = models.IntegerField(
                help_text="sort order, Offer items are displayed in this order.")

class RequiredSkeleton(models.Model):
    """What can be required from a resident?"""
    slug = models.CharField(max_length=80, blank=True, null=True, 
                help_text="What is required as a slug Ex 'Give a Talk(s)' becomes 'give_a_talk' ")
    label = models.CharField(max_length=80, blank=True, null=True, 
                help_text="What is required. Readable prompt Ex 'Give a Talk(s)'")
    status = models.CharField(max_length=1, blank=True, null=True, default="N", 
                help_text="Is it required? Y(es), N(o), M(aybe/negotiable)")
    summary = models.CharField(max_length=80, blank=True, null=True, 
                help_text="One line summary of what is required")
    notes = models.TextField(blank=True, null=True, 
                help_text="Full description of what is required")
    sortorder = models.IntegerField(
                help_text="sort order, Required items are displayed in this order.")


class Organization(models.Model):
    name = models.CharField(max_length=200, help_text="The name of your organization",editable=True)
    user = models.ForeignKey(User)
    website = models.CharField(max_length=100, blank=True, null=True,help_text="")
    street_address = models.CharField(max_length=200, blank=True, null=True,help_text="")
    city = models.CharField(max_length=30, blank=True, null=True,help_text="")
    state = models.CharField(max_length=30, blank=True, null=True,help_text="Where applicable")
    postal_code = models.CharField(max_length=30, blank=True, null=True,help_text="Where applicable")
    country = models.CharField(max_length=30, blank=True, null=True,help_text="")
    email = models.CharField(max_length=30,help_text="A contact email for Residency issues")
    phone = models.CharField(max_length=30, blank=True, null=True,help_text="optional")
    #phone = models.CharField(max_length=30, blank=True, null=True,help_text="optional")
    about = models.TextField(blank=True, null=True,help_text="Tell us about your fine space!")



class Residency(models.Model):
    organization = models.ForeignKey("Organization", default=17)
    # we get 'title' from the base Page, to use as a summary of the opportunity for list views.
    about = models.TextField(blank=True, null=True)
    application_instructions = models.TextField(blank=True, null=True)

    offer_travel_check = models.BooleanField(default=None)
    offer_travel_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_housing_check = models.BooleanField(default=None)
    offer_housing_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_food_check = models.BooleanField(default=None)
    offer_food_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_stipend_check = models.BooleanField(default=None)
    offer_stipend_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_studio_check = models.BooleanField(default=None)
    offer_studio_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_tools_check = models.BooleanField(default=None)
    offer_tools_detail=models.CharField(max_length=120, blank=True, null=True)

    offer_additional_detail = models.TextField(blank=True, null=True)

    require_language = models.CharField(max_length=120, blank=True, null=True)

    require_start_date = models.DateField(blank=True, null=True, help_text="Earliest date the residency can start")
    require_end_date   = models.DateField(blank=True, null=True, help_text="Latest date the residency can end")
    require_minimum_stay = models.CharField(max_length=120, blank=True, null=True, help_text="Minimum required length of stay")
    require_maximum_stay = models.CharField(max_length=120, blank=True, null=True, help_text="Minimum required length of stay")
    require_date_detail = models.TextField(blank=True, null=True)

    require_mentoring_check  = models.BooleanField(default=None)
    require_mentoring_detail =models.CharField(max_length=120, blank=True, null=True)

    require_talk_check  = models.BooleanField(default=None)
    require_talk_detail =models.CharField(max_length=120, blank=True, null=True)

    require_workshop_check  = models.BooleanField(default=None)
    require_workshop_detail =models.CharField(max_length=120, blank=True, null=True)

    require_presentation_check  = models.BooleanField(default=None)
    require_presentation_detail =models.CharField(max_length=120, blank=True, null=True)

    require_class_check  = models.BooleanField(default=None)
    require_class_detail =models.CharField(max_length=120, blank=True, null=True)

    require_hackathon_check  = models.BooleanField(default=None)
    require_hackathon_detail =models.CharField(max_length=120, blank=True, null=True)

    require_other_requirements = models.TextField(blank=True, null=True)

