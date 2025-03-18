from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm

# Create your views here.
def home(request): 
    if request.method == 'GET':
        if 'logout' in request.GET: logout(request)
    x = request.user
    if str(request.user) == 'AnonymousUser': x = 'Guest'
    
    return render(request, 'index.html', {'user' : x})

def signup_view(request):
    if request.method == 'POST':
        
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()          # Сохраняем нового пользователя
            login(request, user)        # Выполняем вход
            return redirect('home')     # Перенаправляем на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = LoginForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password) # Проверяем учетные данные
            if user is not None:
                login(request, user)     # Выполняем вход
                return redirect('home')  # Перенаправляем на главную страницу
    return render(request, 'login.html', {'form': form})