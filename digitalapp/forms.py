from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    number = forms.IntegerField(required=True)
    message = forms.CharField(widget=forms.Textarea)