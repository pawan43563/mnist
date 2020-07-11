from django import forms
from .models import SchoolProfile
from django.db import transaction

class SchoolProfileForm(forms.ModelForm):

    class Meta:
        model = SchoolProfile
        exclude = ('sp_school', 'academic_year')

