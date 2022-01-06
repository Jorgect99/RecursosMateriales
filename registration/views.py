from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, HttpResponseRedirect
from .decorators import unauthenticated_user
from registration.forms import LoginForm

# Create your views here.
@unauthenticated_user
def loginPage(request):
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid(): 
            email = form.cleaned_data['email']
            password =  form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                login(request, user) 
                request.session.set_expiry(18000)
                if not user.is_staff:
                    return HttpResponseRedirect('/')
            else:
                error = "Usuario o contraseña incorrectos, prueba de nuevo."
                context['error'] = error
    else:
        form = LoginForm()
    context['form'] = form
    return render(request, 'registration/login.html', context)

def logoutPage(request):
    logout(request)
    return HttpResponseRedirect('/')