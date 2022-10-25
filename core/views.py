from django.shortcuts import render

# Create your views here.
def index(reguest):
    return render(reguest, 'index.html')

def contato(request):
    return render(request, 'contato.html')

def produto(request):
    return render(request, 'produto.html')

