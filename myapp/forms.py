from django import forms
from django.forms import ModelForm
from .models import MainContactModel


class MainContactForm(ModelForm):
    your_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Your Name (will be completely anonymous)'}))
    company_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Company Name'}))
    company_description = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder' : 'Company Description'}))
    issues_faced =forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder' : 'Issues Faced'}))
    class Meta:
        model = MainContactModel
        fields = (
            'your_name',
            'company_name',
            'company_description',
            'time_employed',
            'still_employed',
            'location',
            'issues_faced',
            'awkwardness_rating',
            'gender',
            'sexual_orientation',
        )
  

   
