from django import forms


class UserForm(forms.Form):
    firstName = forms.CharField(max_length=50)
    lastNName = forms.CharField(max_length=50)
    email = forms.EmailField()
    address = forms.CharField(max_length=150)
    age = forms.IntegerField()
