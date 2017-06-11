from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .form import RegistrationForm


def index(request):
    return render(request, 'home_page/index.html')


def login_user(request):
    if request.user.is_authenticated():
        return render(request, 'home_page/index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'home_page/index.html')
            else:
                return render(request, 'home_page/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home_page/login.html', {'error_message': 'Invalid login'})
    return render(request, 'home_page/login.html')


def logout_user(request):
    if not request.user.is_authenticated():
        return render(request, 'home_page/index.html')
    logout(request)
    return render(request, 'home_page/index.html')


def register(request):
    if request.user.is_authenticated():
        return render(request, 'home_page/index.html')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'home_page/index.html')
    else:
        form = RegistrationForm()
    return render(request, 'home_page/register.html', {'form': form})
