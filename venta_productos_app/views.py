from django.shortcuts import render, redirect
from .models import Venta_Productos

# Create your views here.

def inicio_vistaVenta_Producto(request):
    lasventa_productos=Venta_Productos.objects.all()
    return render(request,'gestionarventa_productos.html', {"misventaproductos":lasventa_productos})

def registrarventa_productos(request):
    id_venta=request.POST["numid_venta"]
    id_trabajador=request.POST["numid_trabajador"]
    id_cliente=request.POST["numid_cliente"]
    id_producto=request.POST["numid_producto"]
    fecha_venta=request.POST["txtfecha_venta"]
    total=request.POST["txttotal"]
    guardarventa_productos=Venta_Productos.objects.create(id_venta=id_venta, id_trabajador=id_trabajador, id_cliente=id_cliente, id_producto=id_producto,fecha_venta=fecha_venta, total=total)
    return redirect('venta_producto')

def seleccionarventa_productos(request,id_venta):
    venta_productos=Venta_Productos.objects.get(id_venta=id_venta)
    return render(request,"editarventa_productos.html", {"misventaproductos":venta_productos})

def borrarventa_productos(request,id_venta):
    venta_productos=Venta_Productos.objects.get(id_venta=id_venta)
    venta_productos.delete()
    return redirect('venta_producto')

def editarventa_productos(request):
    id_venta=request.POST["numid_venta"]
    id_trabajador=request.POST["numid_trabajador"]
    id_cliente=request.POST["numid_cliente"]
    id_producto=request.POST["numid_producto"]
    fecha_venta=request.POST["txtfecha_venta"]
    total=request.POST["txttotal"]
    venta_productos=Venta_Productos.objects.get(id_venta=id_venta)
    venta_productos.id_trabajador=id_trabajador
    venta_productos.id_cliente=id_cliente
    venta_productos.id_producto=id_producto
    venta_productos.fecha_venta=fecha_venta
    venta_productos.total=total
    venta_productos.save()
    return redirect('venta_producto')