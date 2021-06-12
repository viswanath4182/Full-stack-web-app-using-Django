from django import forms

class RegForm(forms.Form):
    name = forms.CharField(max_length=100, )
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    number = forms.IntegerField()


