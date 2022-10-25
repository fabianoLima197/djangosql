from django.contrib import messages
from django.shortcuts import render
from .forms import ContatoForm
# Create your views here.



def index(reguest):
    return render(reguest, 'index.html')

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
    return render(request, 'produto.html')

