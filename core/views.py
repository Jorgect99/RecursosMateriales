from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from registration.decorators import unauthenticated_user, allow_users, admin_only
from django.http import JsonResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import ProveedorForm
from .models import *
import requests

@login_required(login_url='login')
def home(request):
    return render(request, 'core/index-dashboard.html')

@login_required(login_url='login')
def generar_orden(request):
    context = {}
    form = ProveedorForm()
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        idOrden = new_sale(request)
        return HttpResponseRedirect('/detalle-orden/'+str(idOrden))
    context = {'form':form}
    return render(request, 'core/ordenCompra.html', context)

@login_required(login_url='login')
def historial_orden(request):
    ordenes = Orden.objects.filter(idDepartamento=request.user.departamento);
    context = {'ordenes':ordenes}
    return render(request, 'core/historial.html', context)

@login_required(login_url='login')
def productos(request, id_proveedor):
    productos = Producto.objects.filter(idProveedor=id_proveedor)
    lista_productos = []
    for p in productos:
        lista_productos.append({"idProducto":p.idProducto, "nombre":p.nombre, "precio":p.precio})
    return JsonResponse({"productos":lista_productos})

@login_required(login_url='login')
def detalle_orden(request, id_orden):
    orden = Orden.objects.get(pk=id_orden)
    context = {'orden':orden}
    response = requests.get('https://deerland-finanzas.herokuapp.com/solicitud-recursos/'+ str(orden.idSolicitud))
    resp = response.json()
    orden.estatus = resp[0]["ES_Solicitud_R"]
    orden.save() 
    return render(request, "core/detalleOrden.html", context)


def new_sale(request):
    nums = []
    for key in request.POST:
        if "_" in key:
            args = key.split("_")
            if args[1] not in nums:
                nums.append(args[1])

    orden = Orden.objects.create(**{
        "condiciones": request.POST.get("condiciones"),
        "observacion": request.POST.get("observaciones"),
        "firma": request.POST.get("firma"),
        "idDepartamento": request.user.departamento,
        "estatus": "En espera",
        "idProveedor_id": request.POST.get("provedor"),
    })
    
    subtotal = 0
    for n in nums:
        product = Producto.objects.get(
            pk=int(request.POST.get("products_"+n)))
        DetalleOrden.objects.create(**{
            "cantidad": request.POST.get("qty_"+n),
            "descripción": product.descripción,
            "precio": product.precio,
            "idOrden": orden,
            "idProducto": product,
        })
        subtotal += product.precio * int(request.POST.get("qty_"+n))
    
    orden.subtotal = subtotal
    orden.iva = subtotal * 0.16
    orden.total = subtotal * 1.16
    orden.save()

    form_data = {"NombreArea": orden.idDepartamento.nombre, "NombreProveedor": orden.idProveedor.nombre, "Subtotal": orden.subtotal, "IVA": orden.iva, "Total": orden.total, "Firma": orden.firma}
    response = requests.post('https://deerland-finanzas.herokuapp.com/solicitud-recursos/agregar', data=form_data)
    resp = response.json()
    orden.estatus = resp[0]["ES_Solicitud_R"]
    orden.idSolicitud = resp[0]["ID_Solicitud_R"]
    orden.save()  
    return orden.pk