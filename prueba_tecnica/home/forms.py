from django import forms
from .models import Cabida

class CabidaForm(forms.ModelForm):
    class Meta:
        model = Cabida
        fields = ['lado_a', 'lado_b', 'lado_x', 'lado_y']
