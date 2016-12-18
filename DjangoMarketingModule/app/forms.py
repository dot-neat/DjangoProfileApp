"""
Definition of forms.
"""

from django import forms
from app.models import PersonInfo
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.forms import ModelForm

class NameForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = ['name', 'email_address'] 