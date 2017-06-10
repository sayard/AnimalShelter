from django.contrib.auth import authenticate, login
from django.shortcuts import render


def index(request):
    logged_in = False
    return render(request, 'home_page/index.html', {'logged_in': logged_in})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                logged_in = True
                return render(request, 'home_page/index.html', {'logged_in': logged_in})
            else:
                return render(request, 'home_page/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home_page/login.html', {'error_message': 'Invalid login'})
    return render(request, 'home_page/login.html')
