from django.contrib import messages
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
            messages.success(request, '로그인 성공')
            return redirect(next_path)

        else:
            messages.error(request, '로그인 실패')
            return render(request, 'member/login.html')

    else:
        return render(request, 'member/login.html')