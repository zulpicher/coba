# users/decorators.py

from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrapper

def siswa_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.role == 'siswa':
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrapper
