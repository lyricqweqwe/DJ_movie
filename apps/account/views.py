from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect


def movie_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user=authenticate(username,password)
            if user and user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return render(request, 'login.htm', {'msg', '账号或密码错误'})
        except:
            return render(request, 'login.htm', {'mag': '请求错误'})
    else:
        return render(request, '404.html', {'msg': '请求错误'})

def movie_register(request):
    if request.method == 'GET':
       return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username)
        if user is None:
            user = User.objects.create_user(username=username,password=password)
            login(request,user)
            return redirect('/')
        else:
            return render(request, 'register.html', {'mag': '此用户已经注册请重新注册'})
    else:
        return render(request, '404.html', {'msg': '请求错误'})

@login_required
def movie_logout(request):
    logout(request)