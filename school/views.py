
#from school.coniugazione import PrimaConiugazione
from django.shortcuts import render
from .forms import InserisciNome
from .forms import DeclinaNome
from django.shortcuts import redirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.template.context_processors import csrf
from .models import Nome
from .models import Declinazione


def homePage(request):
    return render(request, 'index.html', {})

def aggiungiNome(request):

    if request.method == 'POST':
        form = InserisciNome(request.POST)
        if form.is_valid():
            nome = form.save()
            jsonForm = makeJsonFromData(nome.declinazione, nome.nome, nome.tema, nome.genere)
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
    try:
        obj = Nome.objects.get(nome=mionome)
        return JsonResponse(obj.jsonResponse, safe=False)
    except:
        print('name is not a (nominativo singolare). ')

    try:
        tema = mionome[:-2]
        obj = Nome.objects.get(tema=tema)
        return JsonResponse(obj.jsonResponse, safe=False)
    except:
        print('continuing looking for tema')
    try:
        tema = mionome[:-1]
        obj = Nome.objects.get(tema=tema)
        return JsonResponse(obj.jsonResponse, safe=False)
    except:
        print('continuing looking for tema ')
    try:
        tema = mionome[:-3]
        obj = Nome.objects.get(tema=tema)
        return JsonResponse(obj.jsonResponse, safe=False)
    except:
        print('continuing looking for tema')
    return JsonResponse(Nome.objects.get(nome=mionome).jsonResponse, safe=False)

def makeJsonFromData(declinazioneOconiugazione, nome, tema, genere):

    if declinazioneOconiugazione == 'prima declinazione (ae)':
        return declina_nome(nome, tema, 'primadeclinazione')
    if declinazioneOconiugazione == 'seconda declinazione (i)':
        if genere == 'femminile':
            return declina_nome(nome, tema, 'secondadeclinazione')
        if genere == 'maschile':
            return declina_nome(nome, tema, 'secondadeclinazione')
        if genere == 'neutro':
            return declina_nome_neutro(nome, tema, 'secondadeclinazione')
    if declinazioneOconiugazione == 'terza declinazione (is)': #fix
        if genere == 'femminile' | genere == 'maschile':
            return declina_nome(nome, tema, 'terzadeclinazione')
        else:
            return declina_nome_neutro(nome, tema, 'terzadeclinazione')
    if declinazioneOconiugazione == 'quartadeclinazione':
        return
    if declinazioneOconiugazione == 'quintadeclinazione':
        return
    if declinazioneOconiugazione == 'primaconiugazione':
        return
    if declinazioneOconiugazione == 'secondaconiugazione':
        return
    if declinazioneOconiugazione == 'terzaconiugazione':
        return
    if declinazioneOconiugazione == 'Cquarta':
        return
    if declinazioneOconiugazione == 'Cmista':
        return
    if declinazioneOconiugazione == 'invariabile':
        return



def coniuga(verbo, coniugazione):
    declinazione = {}

    return declinazione

def declina_nome(nome, tema, declinazione):
    #takes: 'nome (nominativo singolare), tema e declinazione e restituisci un jsonresponse'
    declinazione = Declinazione.objects.get(nome=declinazione)
    jsonResponse = {
        'significato': '',
        'nome': nome,
        'is_nome': 'true',
        'declinazione': 'prima',
        'nominativosingolare': str(nome),
        'nominativoplurale': str(tema + declinazione.nominativoplurale),
        'genitivosingolare': str(tema + declinazione.genitivosingolare),
        'genitivoplurale': str(tema + declinazione.genitivoplurale),
        'dativosingolare': str(tema + declinazione.dativosingolare),
        'dativoplurale': str(tema + declinazione.dativoplurale),
        'accusativosingolare': str(tema + declinazione.accusativosingolare),
        'accusativoplurale': str(tema + declinazione.accusativoplurale),
        'vocativosingolare': str(tema + declinazione.vocativosingolare),
        'vocativoplurale': str(tema + declinazione.vocativoplurale),
        'ablativosingolare': str(tema + declinazione.ablativosingolare),
        'ablativoplurale': str(tema + declinazione.ablativoplurale),

        'is_verbo': 'false',
        'primasingolare': '',
        'secondasingolare': '',
        'terzasingolare': '',
        'primaplurale': '',
        'secondaplurale': '',
        'terzaplurale': '',

        'is_aggettivo': 'false',

        'is_avverbio': 'false',
        'avverbio': '',
        'particolarita': 'false',
        }
    print(jsonResponse)
    return jsonResponse

def declina_nome_neutro(nome, tema, declinazione):
        #prende: 'nome (nominativo singolare), tema e declinazione e restituisce: jsonresponse'
        declinazione = Declinazione.objects.get(nome=declinazione)
        jsonResponse = {
            'significato': '',
            'nome': nome,
            'is_nome': 'true',
            'declinazione': 'prima',
            'nominativosingolare': str(nome),
            'nominativoplurale': str(tema + declinazione.nominativopluraleNeutro),
            'genitivosingolare': str(tema + declinazione.genitivosingolareNeutro),
            'genitivoplurale': str(tema + declinazione.genitivopluraleNeutro),
            'dativosingolare': str(tema + declinazione.dativosingolareNeutro),
            'dativoplurale': str(tema + declinazione.dativopluraleNeutro),
            'accusativosingolare': str(tema + declinazione.accusativosingolareNeutro),
            'accusativoplurale': str(tema + declinazione.accusativopluraleNeutro),
            'vocativosingolare': str(tema + declinazione.vocativosingolareNeutro),
            'vocativoplurale': str(tema + declinazione.vocativopluraleNeutro),
            'ablativosingolare': str(tema + declinazione.ablativosingolareNeutro),
            'ablativoplurale': str(tema + declinazione.ablativopluraleNeutro),

            'is_verbo': 'false',
            'primasingolare': '',
            'secondasingolare': '',
            'terzasingolare': '',
            'primaplurale': '',
            'secondaplurale': '',
            'terzaplurale': '',

            'is_aggettivo': 'false',

            'is_avverbio': 'false',
            'avverbio': '',
            'particolarita': 'false',
            }
        print(jsonResponse)
        return jsonResponse
