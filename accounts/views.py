from django.shortcuts import render, redirect
from pyexpat.errors import messages



# Create your views here.
def login(request):
    if request.method == "POST":
        return render(request, 'core/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    from django.contrib import auth
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        messages.sucess(request, 'Usuario logado.')
        return redirect('listar_contato')
    messages.error(request, 'Email ou senha incorretos.')