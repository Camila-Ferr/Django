from django.shortcuts import render
from inicial.models import Sorteio, Noticia, Carrossel

def index(request):
    listaCarrossel = Carrossel.objects.all().order_by('id')
    listaSorteio = Sorteio.objects.all().order_by('id')
    listaNoticia = Noticia.objects.all().order_by('id')
    return render(request, 'index.html', {'listaCarrossel': listaCarrossel, 'listaSorteio': listaSorteio, 'listaNoticia':listaNoticia})


