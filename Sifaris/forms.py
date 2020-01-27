from django import forms
from .models import Pizza,Olcu

class Sifaris_Form(forms.ModelForm):
    class Meta:
        model=Pizza
        fields='__all__'

class Elave_sifaris(forms.Form):
    reqem=forms.IntegerField(min_value=2)