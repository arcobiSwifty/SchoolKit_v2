from django import forms
from .models import Nome
from .models import Declina
from .models import Declinazione

class InserisciNome(forms.ModelForm):

    class Meta:
        model = Nome
        fields = ('nome', 'tema', 'declinazione', 'significato', 'particolarita')

class DeclinaNome(forms.ModelForm):

    class Meta:
        model = Declina
        fields = ('nome',)

class DeclinazioneForm(forms.ModelForm):
    class Meta:
        model = Declinazione
        fields = ('nominativosingolare', 'nominativoplurale', 'genitivosingolare', 'genitivoplurale', 'dativosingolare', 'dativoplurale', 'accusativosingolare', 'accusativoplurale', 'vocativosingolare', 'vocativoplurale', 'ablativosingolare', 'ablativoplurale',
                'nominativosingolareNeutro', 'nominativopluraleNeutro', 'genitivosingolareNeutro', 'genitivopluraleNeutro', 'dativosingolareNeutro', 'dativopluraleNeutro', 'accusativosingolareNeutro', 'accusativopluraleNeutro', 'vocativosingolareNeutro', 'vocativopluraleNeutro', 'ablativosingolareNeutro', 'ablativopluraleNeutro')
