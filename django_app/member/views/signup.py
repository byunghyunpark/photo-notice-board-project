from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from member.forms import SignupModelForm

__all__ = [
    'signup',
]

def signup(request):
    context = {}
    if request.method == 'POST':
        form = SignupModelForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, '회원가입 성공')
            return redirect('photo:photo_list')
    else:
        form = SignupModelForm()
        context['form'] = form
    return render(request, 'member/signup.html', context)
