from django.http import HttpResponse
from django.shortcuts import redirect, HttpResponseRedirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            return view_func(request, *args, **kwargs)
            
    return wrapper_func

def allow_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
             
            #print('Working', allowed_roles)
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseRedirect('/')
                
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'areas':
            return HttpResponseRedirect('/')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_func