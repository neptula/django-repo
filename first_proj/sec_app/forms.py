from django import forms
from django.forms.fields import CharField, EmailField
from django.forms.widgets import Textarea
from django.core import validators

def check_for_uppercase(value):
    if value[0].islower():
        raise forms.ValidationError("FIRST LETTER SHOULD BE CAPITAL!")


class detail(forms.Form):
    name=forms.CharField(validators=[check_for_uppercase] )
    email=forms.EmailField()
    verify_email=forms.EmailField(label="Enter your email again!")
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean_botcatcher(self):
        botcatcher=self.cleaned_data['botcatcher']
        if len (botcatcher)>0:
            raise forms.ValidationError("GOTTA BOT!")
        return botcatcher

    def clean(self):
        all_clean_data=super().clean() 
        email=all_clean_data['email']   
        vemail=all_clean_data['verify_email']   
        if email!=vemail:
         raise forms.ValidationError("Discrepancy in email entered")