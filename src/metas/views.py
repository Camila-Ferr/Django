from django.shortcuts import render
from metas.models import CardsMeta,Contas, CalculoMetas

def meta(request):
    cards = CardsMeta.objects.all().order_by('id')
    contas = Contas.objects.all()
    calculoMeta = CalculoMetas.objects.all().order_by('id')
    return render(request, 'meta.html', {'cards': cards, 'contas': contas, 'calculoMeta': calculoMeta})
