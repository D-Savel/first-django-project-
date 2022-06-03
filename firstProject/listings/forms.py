from django import forms
from listings.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'  # for all fields
        # exclude = ('isMajor',)


class SwapiForm(forms.Form):
    OPTIONS = (
        ("people", 'personnages'),
        ("vehicles", 'vehicules'),
        ("planets", 'planètes'),
        ("starships", 'vaisseaux')
    )
    category = forms.ChoiceField(choices=OPTIONS)
