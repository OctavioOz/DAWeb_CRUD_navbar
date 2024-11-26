from django.shortcuts import render, redirect
from .models import Clientes

# Create your views here.

def inicio_vistaClientes(request):
    losclientes=Clientes.objects.all()
    return render(request,'gestionarclientes.html', {"misclientes":losclientes})

def registrarclientes(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    metodo_p=request.POST["txtmetodo_p"]
    tipo_cort=request.POST["txttipo_cort"]
    tipo_cab=request.POST["txttipo_cab"]
    fecha_nc=request.POST["txtfecha_nc"]
    guardarclientes=Clientes.objects.create(id=id, nombre=nombre, metodo_p=metodo_p, tipo_cort=tipo_cort, tipo_cab=tipo_cab, fecha_nc=fecha_nc)
    return redirect('clientes')

def seleccionarclientes(request,id):
    clientes=Clientes.objects.get(id=id)
    return render(request,"editarclientes.html", {"misclientes":clientes})

def borrarclientes(request,id):
    clientes=Clientes.objects.get(id=id)
    clientes.delete()
    return redirect('clientes')

def editarclientes(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    metodo_p=request.POST["txtmetodo_p"]
    tipo_cort=request.POST["txttipo_cort"]
    tipo_cab=request.POST["txttipo_cab"]
    fecha_nc=request.POST["txtfecha_nc"]
    clientes=Clientes.objects.get(id=id)
    clientes.nombre=nombre
    clientes.metodo_p=metodo_p
    clientes.tipo_cort=tipo_cort
    clientes.tipo_cab=tipo_cab
    clientes.fecha_nc=fecha_nc
    clientes.save()
    return redirect('clientes')