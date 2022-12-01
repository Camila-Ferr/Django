import locale
from decimal import Decimal

from django.contrib.humanize.templatetags.humanize import intcomma
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from produto.forms import ProdutoForm, QuantidadeForm
from produto.models import Produto




def produto(request):
    return render(request, 'produto/produto.html')



def atualiza_produtos(request):
    form = QuantidadeForm(request.POST)
    if form.is_valid():
        id = form.cleaned_data['id']
        quantidade = form.cleaned_data['quantidade']
        precoParcial = 0

        if (quantidade == 0):
            produto = get_object_or_404(Produto, id=id)
            produto.delete()
        else:
            produto = get_object_or_404(Produto, pk=id)
            produto.quantidade = quantidade
            precoParcial = intcomma(float(produto.preco) * int(produto.quantidade))

            precoParcial = Decimal(precoParcial)
            produto.precoParcial = precoParcial
            produto.save()



        listaProdutos = Produto.objects.all()
        valor_total = 0
        for produto in listaProdutos:
            valor_total += (produto.quantidade * produto.preco)



        preco_total = Decimal(valor_total)
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

        valor = locale.currency(preco_total, grouping=True)
        valorParcial = locale.currency(precoParcial, grouping=True)
        print(valorParcial)


        #Retorna um objeto Json contendo essas 3 info
        return JsonResponse({'quantidade': quantidade, 'precoTotal': valor, 'precoParcial': valorParcial})
    else:
        raise ValueError('Error')



def lista_produtos(request):
    listaProdutos = Produto.objects.all()

    valorTotal = 0
    listaForms = []

    for produto in listaProdutos:
        valorTotal += (produto.quantidade * produto.preco)
        listaForms.append(QuantidadeForm(
            initial={'quantidade': produto.quantidade,
                     'id': produto.id}
        ))

    valorTotal = Decimal(valorTotal)
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor = locale.currency(valorTotal, grouping=True)

    return render(request, 'produto/lista.html',
                  {'listas': zip(listaProdutos, listaForms), 'valorTotal': valor})



def cadastra_produto(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.POST:
        produto_form = ProdutoForm(request.POST)
        if produto_form.is_valid():
            produto = produto_form.save(commit=False)
            produto.precoParcial = produto.preco * produto.quantidade
            produto.save()

            listaProdutos = Produto.objects.all()
            valorTotal = 0


            for produto in listaProdutos:
                valorTotal += (produto.quantidade * produto.preco)

            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            valor = locale.currency(Decimal(valorTotal), grouping=True)

            return JsonResponse({'novoProduto': model_to_dict(produto), 'categoria': model_to_dict(produto.categoria),
                                 'precoTotal': valor}, safe=False)
    else:
        produtoForm = ProdutoForm()
    return render(request, 'produto/cadastra.html', {'form': produtoForm})
