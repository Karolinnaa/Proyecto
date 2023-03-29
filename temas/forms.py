from django import forms
from temas.models import Tema

class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ('titulo', 'descripcion', 'importante')