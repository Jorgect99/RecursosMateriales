from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from registration.decorators import unauthenticated_user, allow_users, admin_only
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import ProveedorForm

@login_required(login_url='login')
def home(request):
    return render(request, 'core/index-dashboard.html')

@login_required(login_url='login')
def generar_orden(request):
    context = {}
    form = ProveedorForm()
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_imc')
    context = {'form':form}
    return render(request, 'core/ordenCompra.html', context)

@login_required(login_url='login')
def historial_orden(request):
    return render(request, 'core/historial.html')