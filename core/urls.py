from django.urls import path
from . import views

urlpatterns = [
    #paths core
    path('', views.home, name="admindashboard"),
    path('generar-orden', views.generar_orden, name="generar_orden"),
    path('historial-orden', views.historial_orden, name="historial_orden"),
    path('productos/<id_proveedor>', views.productos, name="productos"),
    path('detalle-orden/<id_orden>', views.detalle_orden, name="detalle_orden"),
]