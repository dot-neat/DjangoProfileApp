"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from .models import PersonInfo
from .forms import NameForm
# TODO: Configure your database in settings.py and sync before running tests.
class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()
 

    #def test_add_view(self):

    #def test_duplicate_emails_display_error_message(self):    

    #def test_empty_name_or_email_address_display_error_message(self):

       
    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)

    def test_list(self):
        """Tests the contact page."""
        response = self.client.get('/list')
        self.assertContains(response, 'List', 3, 200)

    def test_add(self):
        """Tests the about page."""
        response = self.client.get('/add')
        self.assertContains(response, 'Add', 3, 200)
