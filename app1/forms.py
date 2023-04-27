from django import forms
from app1.models import *

class Courseform(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        labels = {
            'cname':'COURSE',
            'duration':'DUR',
            'fee':'FEE',
        }