from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')  # Redirect to the cars list after successful registration
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

#PRIMEIRO USUARIO
#testeusuario (12345teste)

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

#testeusuario2
#teste12345

def logout_view(request):
    logout(request)
    return redirect('cars_list')
