from django.contrib.auth import authenticate as auth_authenticate, login as auth_login
from django.http import HttpResponse
from django.shortcuts import render, redirect

__all__ = [
    'login',
]

def login(request):
    next_path = request.GET.get('next')
    if request.method == 'POST':
        try:
            email = request.POST['email']
            password = request.POST['password']
            user = auth_authenticate(email=email, password=password)

        except KeyError:
            return HttpResponse('KeyError')

        if user is not None:
            auth_login(request, user)
            print('로그인성공')
            return redirect(next_path)

        else:
            print('로그인실패')
            return render(request, 'member/login.html')

    else:
        return render(request, 'member/login.html')