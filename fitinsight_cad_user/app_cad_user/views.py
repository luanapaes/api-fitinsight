from django.shortcuts import render
from .models import Usuario

# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def usuario(request):
    #salvar no banco de dados 
    novo_user = Usuario()
    novo_user.nome = request.POST.get('nome')
    novo_user.email = request.POST.get('email')
    novo_user.senha = request.POST.get('pass')
    novo_user.conf_senha = request.POST.get('confpass')
    novo_user.save()
    
    #exibir users em uma nova page
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    # Retornar dados para a página de listagem:
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})