from django.shortcuts import render
from login.models import Divulgacao, Formulario

def login(request):
    divulgacao = Divulgacao.objects.all().order_by('id')
    listaCampos = Formulario.objects.all().order_by('id')
    return render(request, 'login.html', {'divulgacao': divulgacao, 'listaCampos': listaCampos})
