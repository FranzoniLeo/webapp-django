from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

from django.http import HttpResponse #testes


#novo castro para usuarios#
def cadastro(request):
    if request.method == 'GET':
        return(render(request, 'usuarios/cadastro.html'))
    else:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        #conferencia para usuarios#
        if  not email or not username or not password1 or not password2:
            messages.error(request, "All fields are required")
            return redirect('cadastro')
        
        if  password1 != password2:
            messages.error(request, "The passwords entered do not match")
            return redirect('cadastro')

        mail = User.objects.filter(email = email)   
        if mail:
            messages.error(request, "This email is already in use")
            return redirect('cadastro')  

        user = User.objects.filter(username = username)   
        if user:
            messages.error(request, "This username is already in use")
            return redirect('cadastro')

        user = User.objects.create_user(username,email,password1)   
        user.save()
        
        messages.success(request, "Account created successfully!")
        return redirect('login')

#pagina de login
def logar(request):
    if request.method == 'GET':
        return(render(request, 'usuarios/login.html'))
    else:
        usename_email = request.POST.get('username_email')
        password = request.POST.get('password')

        user = authenticate(username = usename_email, password = password)
        if not user:
            user = authenticate(email = usename_email, password = password)
        if user:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('index')  ######################################### arrumar #############
        else:
            messages.error(request, "Incorrect username or password")
            return redirect('login')

#sair da conta
def sair(request):
    logout(request)
    return redirect('index')

#perfil do usuario
@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')
    