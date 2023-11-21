# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
from django.contrib import auth


# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('')  # 그 다음 어딘가로..
        else:
            return render(request, '', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login/login.html')


# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('login/home.html')  # 그 다음 어딘가로...


# 회원가입, 로그인, 로그아웃 모여있는
def home(request):
    return render(request, 'login/home.html')