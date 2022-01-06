from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Departamento(models.Model):
    idDepartamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, verbose_name = "Nombre Departamento")
    nombre_encargado = models.CharField(max_length=250, verbose_name = "Nombre Encargado")
    correo =  models.CharField(max_length=250, verbose_name = "Correo")
    telefono = models.CharField(max_length=10, verbose_name = "Telefono")

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
    
    def __str__(self):
        return self.nombre

class Orden(models.Model):
    idOrden = models.AutoField(primary_key=True)
    subtotal = models.FloatField(verbose_name = "Subtotal", default=0)
    total = models.FloatField(verbose_name = "Total", default=0)
    iva = models.FloatField(verbose_name = "IVA", default=0)
    fecha = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de orden")
    condiciones = models.CharField(max_length=250, verbose_name = "Condiciones")
    idDepartamento = models.ForeignKey(Departamento, on_delete = models.CASCADE, related_name='ordenes')
    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'
    
class Proveedor(models.Model):
    idProveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, verbose_name = "Nombre Proveedor")
    correo = models.CharField(max_length=250, verbose_name = "Correo")
    telefono = models.CharField(max_length=10, verbose_name = "Telefono")

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
    
    def __str__(self):
        return self.nombre
        
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, verbose_name = "Nombre Producto")
    precio = models.FloatField(verbose_name = "Precio", default=0)
    descripción = models.CharField(max_length=250, verbose_name = "Descripcion")
    idProveedor = models.ForeignKey(Proveedor, on_delete = models.CASCADE, related_name='productos')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre

class DetalleOrden(models.Model):
    idDetalle = models.AutoField(primary_key=True)
    cantidad = models.FloatField(verbose_name = "Cantidad de Productos", default=0)
    descripción = models.CharField(max_length=250, verbose_name = "Descripcion")
    precio = models.FloatField(verbose_name = "Precio", default=0)
    idOrden = models.ForeignKey(Orden, on_delete = models.CASCADE, related_name='detalles')
    idProducto = models.ForeignKey(Producto, on_delete = models.CASCADE, related_name='ordenes')

    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'


    
