from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify

from parceiro.forms import PesquisaParceiro, ParceiroForm
from parceiro.models import Parceiro



def lista_parceiro(request):
    form = PesquisaParceiro(request.GET)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        lista_de_parceiro = Parceiro.objects.filter(nome__icontains=nome).order_by('nome')

        paginator = Paginator(lista_de_parceiro, 3)
        pagina = request.GET.get('pagina')

        # Retorna a pagina a partir da variavel pagina
        page_obj = paginator.get_page(pagina)

        return render(request, 'parceiro/pesquisa.html', { 'parceiros': page_obj,
                                                                  'form': form,
                                                                  'nome': nome })
    else:
        raise ValueError('Ocorreu um erro inesperado ao tentar recuperar um parceiro.')





def cadastra_parceiro(request):

    if request.method == 'POST':
        # Recupera o valor que esta salvo no objeto sessão com a chave parceiro_id se vier do editar
        parceiro_id = request.session.get('parceiro_id')

        ## Se for diferente de None
        if parceiro_id:
            # Recupera do banco de dados o parceiro q possui o id recuperado
            parceiro = get_object_or_404(Parceiro, pk=parceiro_id)
            # Cria um ParceiroForm a parti da requisição e dos dados do parceiro recuperados do banco de dados
            #o objeto vai existir do criar ou do editar
            parceiro_form = ParceiroForm(request.POST, instance=parceiro)

        else:
            # Se não existir um valor associado a chave parceiro_id no objeto sessão
            parceiro_form = ParceiroForm(request.POST)

        # Faz a validação dos campos do ParceiroForm criado
        if parceiro_form.is_valid():
            # Retornando um objeto que ainda n foi gravado no banco de dados e pode ser alterado
            parceiro = parceiro_form.save(commit=False)
            # Salva no banco de dados
            parceiro.save()

            # Verifica se o parceiro_id é diferente de None
            if parceiro_id:
                messages.add_message(request, messages.INFO, 'Parceiro alterado com sucesso!')
                # deleta do objeto sessão o id associado a chave
                del request.session['parceiro_id']
            else:
                messages.add_message(request, messages.INFO, 'Parceiro cadastrado com sucesso!')

            return redirect('parceiro:exibe_parceiro', id=parceiro.id)
    else:
        try:
            del request.session['parceiro_id']
        except KeyError:
            pass
        parceiro_form = ParceiroForm()

    return render(request, 'parceiro/cadastra.html', {'form': parceiro_form})






def exibe_parceiro(request, id):
    ## Recupera do banco o usuario recem cadastrado passando em pk o id do usuario armazenado no objeto sessão associado a chave fornecedorId
    parceiro = get_object_or_404(Parceiro, pk=id)
    ## Salvar no objeto sessão utilizando a chave fornecedor_id_del o id do fornecedor que foi exibido, para caso seja solicitado a remoção do fornecedor
    request.session['parceiro_id_del'] = id
    return render(request, 'parceiro/exibe.html', {'parceiro': parceiro})





def remove_parceiro(request):
    ## Recupera o id do fornecedor salvo no objeto sessão
    parceiro_id = request.session.get('parceiro_id_del')
    ## Recupera do banco o fornecedor com o id recuperado acima
    parceiro = get_object_or_404(Parceiro, id=parceiro_id)
    ## Deleta o fornecedor do banco de dados
    parceiro.delete()
    ## deleta do objeto sessão o id associado a chave fornecedor_id_del
    del request.session['parceiro_id_del']
    ## Mostra na tela a menssagem Fornecedor removido com sucesso
    messages.add_message(request, messages.INFO, 'Parceiro removido com sucesso.')
    return render(request, 'parceiro/exibe.html', {'parceiro': parceiro})





def edita_parceiro(request, id):
    # Recupera a info do banco de dados
    parceiro = get_object_or_404(Parceiro, pk=id)
    parceiro_form = ParceiroForm(instance=parceiro)
    # Cria no objeto sessão uma atribuição entre parceiro_id e id
    request.session['parceiro_id'] = id
    return render(request, 'parceiro/cadastra.html', {'form': parceiro_form})
















