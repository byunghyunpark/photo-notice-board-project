from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

__all__ = [
    'logout',
]

def logout(request):
    auth_logout(request)
    print('로그아웃')
    return redirect('photo:photo_list')