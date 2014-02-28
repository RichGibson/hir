
#from django.test import TestCase as BaseTestCase
from django.test import TestCase
from django.test import Client

from hir.models import Residency, Organization

from mezzanine.conf import settings

import sys
class test_stuff(TestCase):
    fixtures = ['hir.json']
    print >>sys.stderr, "fixtures? ", fixtures
    def setUp(self):
        # do something to setup tests.
        pass

    def tearDown(self):
       # now clean up
        pass 

    def test_start(self):
        self.assertEqual(1,1)

    def test_home(self):
        """ can we fetch the home page? Do something reasonable?"""
        c = Client()
        response=c.get('/')
        self.assertEqual(len(response.content) > 2000, True) # the home page is > 2000 characters presumably.
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(response.templates[0].name, 'index.html')

    def test_residency_model(self):
        reslist = Residency.objects.all()
        self.assertEqual(len(reslist), 4)
        

    def test_list_of_residencies(self):
        """ we should have some residencies listed. """
        c = Client()
        response = c.get('http://www.hackerinresidence.org/list-of-residencies/')
        #self.assertEqual(len(response.context['reslist']), 5)



