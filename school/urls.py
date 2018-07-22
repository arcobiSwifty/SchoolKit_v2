from django.conf.urls import url
from . import views
from .forms import InserisciNome

urlpatterns = [
		    url(r'^$', views.homePage, name='homePage'),
			url(r'new/$', views.aggiungiNome, name='inserisciNome'),
			url(r'declina/$', views.declina, name='declina'),
			url(r'verificaNome/$', views.controllaNome, name='controllaNome'),
			url(r'declinaNome/$', views.declinaNome, name='declinaNome')
]
