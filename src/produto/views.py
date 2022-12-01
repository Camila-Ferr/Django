import locale
from decimal import Decimal
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from produto.forms import ProdutoForm, QuantidadeForm
from produto.models import Produto




def produto(request):
    return render(request, 'produto/produto.html')


@csrf_exempt
def atualiza_produtos(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        id = form.cleaned_data['id']
        qtd = form.cleaned_data['qtd']

        if (qtd == 0):
            produto = get_object_or_404(Produto, id=id)
            produto.delete()
        else:
            produto = get_object_or_404(Produto, pk=id)
            produto.qtd = qtd
            produto.save()

        lista_de_produtos = Produto.objects.all()
        valor_total = 0
        for produto in lista_de_produtos:
            valor_total += (produto.qtd * produto.preco)

        preco_total = Decimal(valor_total)
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        valor = locale.currency(preco_total, grouping=True)

        return JsonResponse({'qtd': qtd, 'preco_total': valor})
    else:
        raise ValueError('Error')


@csrf_exempt
def lista_produtos(request):
    lista_de_produtos = Produto.objects.all()

    valor_total = 0
    lista_de_forms = []

    for produto in lista_de_produtos:
        valor_total += (produto.qtd * produto.preco)
        lista_de_forms.append(QuantidadeForm(
            initial={'qtd': produto.qtd,
                     'id': produto.id}
        ))

    valor_total = Decimal(valor_total)
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = locale.currency(valor_total, grouping=True)

    return render(request, 'produto/lista_produtos.html',
                  {'listas': zip(lista_de_produtos, lista_de_forms), 'valor_total': valor})


@csrf_exempt
def cadastra_produto(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.POST:
        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            produto = produto_form.save(commit=False)
            produto.save()

            lista_de_produtos = Produto.objects.all()
            valor_total = 0
            for produto in lista_de_produtos:
                valor_total += (produto.qtd * produto.preco)

            preco_total = Decimal(valor_total)
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            valor = locale.currency(preco_total, grouping=True)

            return JsonResponse({'novoProduto': model_to_dict(produto), 'categoria': model_to_dict(produto.categoria),
                                 'preco_total': valor}, safe=False)
    else:
        produto_form = ProdutoForm()
    return render(request, 'produto/cadastra_produto.html', {'form': produto_form})
