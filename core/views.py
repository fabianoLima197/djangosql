from django.contrib import messages
from django.shortcuts import render
from .forms import ContatoForm, ProdutoModelForm
from .models import Produto
from django.shortcuts import redirect
# Create your views here.



def index(reguest):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(reguest, 'index.html', context)

def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            '''nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']

            print('Mensagem enviada')
            print(f'Nome: {nome}')
            print(f'Email: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')'''

            messages.success(request, "E-mail Enviado...")
            form = ContatoForm()
        else:
            messages.error(request, 'Erro para enviar mensagem')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():

                form.save()

                '''prod = form.save(commit=False)
            print(f'Nome {prod.nome}')
            print(f'Preço {prod.preco}')
            print(f'Estoque {prod.estoque}')
            print(f'Imagem {prod.imagem}') para testes'''
                messages.success(request, 'Produto Salvo com Sucesso')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar o Produto!!')
        else:
            form = ProdutoModelForm()
        context = {
            'form':form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')