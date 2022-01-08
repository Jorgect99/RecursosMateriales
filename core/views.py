from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from registration.decorators import unauthenticated_user, allow_users, admin_only
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import ProveedorForm
from .models import *

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
    ordenes = Orden.objects.all();
    countOrdenes = ordenes.count();
    return render(request, 'core/historial.html', locals())

@login_required(login_url='login')
def productos(request, id_proveedor):
    productos = Producto.objects.filter(idProveedor=id_proveedor)
    lista_productos = []
    for p in productos:
        lista_productos.append({"idProducto":p.idProducto, "nombre":p.nombre, "precio":p.precio})
    return JsonResponse({"productos":lista_productos})


# @login_required(login_url='login')
# def generar_orden(request):
#     if request.method == 'POST':
#         nums = []
#         products = []
#         subtotal = 0
#         client = Client.objects.get(id=int(request.POST.get("client")))
#         sale = Orden.objects.create(**{
#             "client": client,
#             "payment_method": request.POST.get("paymethod"),
#         })
#         for n in nums:
#             product = Producto.objects.get(
#                 id=int(request.POST.get("products_"+n)))
#             DetalleOrden.objects.create(**{
#                 "sale": sale,
#                 "product": product,
#                 "price_buy": product.price_buy,
#                 "price_sell": product.price_sell,
#                 "quantity": request.POST.get("qty_"+n),
#             })
#             subtotal += product.price_sell * int(request.POST.get("qty_"+n))

#         sale.subtotal = subtotal
#         sale.iva = subtotal * 0.16
#         sale.total = subtotal * 1.16
#         sale.save()

       
       
