from django.shortcuts import render
from ranking.models import Ranking, Lista


def ranking(request):
    top10 = Ranking.objects.all().order_by('posicao')
    nomeListas = Lista.objects.all().order_by('id')
    return render(request, 'ranking.html', {'top10': top10, 'nomeListas': nomeListas})


