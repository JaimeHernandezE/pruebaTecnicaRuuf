from django import forms

class CabidaForm(forms.Form):
    x = forms.FloatField(label='Lado X', min_value=0)
    y = forms.FloatField(label='Lado Y', min_value=0)
    a = forms.FloatField(label='Lado A', min_value=0)
    b = forms.FloatField(label='Lado B', min_value=0)
