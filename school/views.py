
#from school.coniugazione import PrimaConiugazione
from django.shortcuts import render
from .forms import InserisciNome
from .forms import DeclinaNome
from django.shortcuts import redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.context_processors import csrf
from .models import Nome


def homePage(request):
    return render(request, 'index.html', {})

def aggiungiNome(request):

    if request.method == 'POST':
        form = InserisciNome(request.POST)
        if form.is_valid():
            nome = form.save(commit=False)
            jsonForm = makeJsonFromData(nome.declinazione, nome.nome)
            jsonForm['significato'] = nome.significato
            nome.jsonResponse = jsonForm
            nome.save()
        return redirect('homePage')

    else:
        form = InserisciNome()
        return render(request, 'aggiungiNome.html', {'form': form})

def declina(request):
    form = DeclinaNome()
    return render(request, 'declinaNome.html', {'form': form})

def controllaNome(request):
    mionome = request.POST.get('nome', None)
    print(mionome)
    data = {
         'exists': Nome.objects.filter(nome=mionome).exists()
    }

    return JsonResponse(data)

def declinaNome(request):
    mionome = request.POST.get('nome', None)
    return JsonResponse(Nome.objects.get(nome=mionome).jsonResponse, safe=False)

def makeJsonFromData(declinazioneOconiugazione, nome):
    if declinazioneOconiugazione == 'prima declinazione (ae)':
        return declinaPrimaDeclinazione(nome, 'ros')
    if declinazioneOconiugazione == 'Dseconda':
        return
    if declinazioneOconiugazione == 'Dterza':
        return
    if declinazioneOconiugazione == 'Dquarta':
        return
    if declinazioneOconiugazione == 'Dquinta':
        return
    if declinazioneOconiugazione == 'Cprima':
        return
    if declinazioneOconiugazione == 'Cseconda':
        return
    if declinazioneOconiugazione == 'Cterza':
        return
    if declinazioneOconiugazione == 'Cquarta':
        return
    if declinazioneOconiugazione == 'Cmista':
        return
    if declinazioneOconiugazione == 'invariabile':
        return

def declina_nome(nome, declinazione):
    if declinazione == 'prima declinazione (ae)':
        declinaPrimaDeclinazione(nome, Nome.objects.get(nome=nome).tema) 


def coniuga(verbo, coniugazione):
    declinazione = {}

    return declinazione

def declinaPrimaDeclinazione(nome, tema):
    desinenzaNominativoSingolare = 'a'
    desinenzaNominativoPlurale = 'ae'
    desinenzaGenitivoSingolare = 'ae'
    desinenzaGenitivoPlurale = 'arum'
    desinenzaDativoSingolare = 'ae'
    desinenzaDativoPlurale = 'is'
    desinenzaAccusativoSingolare = 'am'
    desinenzaAccusativoPlurale = 'as'
    desinenzaVocativoSingolare = 'a'
    desinenzaVocativoPlurale = 'ae'
    desinenzaAblativoSingolare = 'a'
    desinenzaAblativoPlurale = 'is'
    jsonResponse = {
        'significato': '',
        'nome': nome,
        'is_nome': 'true',
        'declinazione': 'prima',
        'nominativosingolare': str(tema + desinenzaNominativoSingolare),
        'nominativoplurale': str(tema + desinenzaNominativoPlurale),
        'genitivosingolare': str(tema + desinenzaGenitivoSingolare),
        'genitivoplurale': str(tema + desinenzaGenitivoPlurale),
        'dativosingolare': str(tema + desinenzaGenitivoSingolare),
        'dativoplurale': str(tema + desinenzaGenitivoPlurale),
        'accusativosingolare': str(tema + desinenzaAccusativoSingolare),
        'accusativoplurale': str(tema + desinenzaAccusativoPlurale),
        'vocativosingolare': str(tema + desinenzaVocativoSingolare),
        'vocativoplurale': str(tema + desinenzaVocativoPlurale),
        'ablativosingolare': str(tema + desinenzaAblativoSingolare),
        'ablativoplurale': str(tema + desinenzaAblativoPlurale),
        'significato': '',

        'is_verbo': 'false',
        'primasingolare': '',
        'secondasingolare': '',
        'terzasingolare': '',
        'primaplurale': '',
        'secondaplurale': '',
        'terzaplurale': '',

        'is_avverbio': 'false',
        'avverbio': '',
        'particolarita': 'false',
        }
    print(jsonResponse)
    return jsonResponse
