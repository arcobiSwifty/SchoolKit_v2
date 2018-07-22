from django import forms
from .models import Nome
from .models import Declina

class InserisciNome(forms.ModelForm):

    class Meta:
        model = Nome
        fields = ('nome', 'declinazione', 'significato', 'particolarita')

class DeclinaNome(forms.ModelForm):

    class Meta:
        model = Declina
        fields = ('nome',)
