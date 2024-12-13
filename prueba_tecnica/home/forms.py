from django import forms

class CabidaForm(forms.Form):
    x = forms.IntegerField(label='Lado X', min_value=0)
    y = forms.IntegerField(label='Lado Y', min_value=0)
    a = forms.IntegerField(label='Lado A', min_value=0)
    b = forms.IntegerField(label='Lado B', min_value=0)
