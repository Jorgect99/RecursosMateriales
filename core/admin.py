from django.contrib import admin
from .models import Proveedor, Producto, Departamento, Orden, DetalleOrden


# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Departamento)
admin.site.register(Orden)
admin.site.register(DetalleOrden)