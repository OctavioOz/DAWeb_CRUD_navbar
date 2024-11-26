from django.shortcuts import render, redirect
from .models import Trabajadores

# Create your views here.

def inicio_vistaTrabajadores(request):
    lostrabajadores=Trabajadores.objects.all()
    return render(request,'gestionartrabajadores.html', {"mistrabajadores":lostrabajadores})

def registrartrabajadores(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    num_telefono=request.POST["txtnum_telefono"]
    direccion=request.POST["txtdireccion"]
    fecha_ne=request.POST["txtfecha_ne"]
    fecha_ing=request.POST["txtfecha_ing"]
    guardartrabajadores=Trabajadores.objects.create(id=id, nombre=nombre, apellido=apellido, num_telefono=num_telefono, direccion=direccion, fecha_ne=fecha_ne, fecha_ing=fecha_ing)
    return redirect('trabajadores')

def seleccionartrabajadores(request,id):
    trabajadores=Trabajadores.objects.get(id=id)
    return render(request,"editartrabajadores.html", {"mistrabajadores":trabajadores})

def borrartrabajadores(request,id):
    trabajadores=Trabajadores.objects.get(id=id)
    trabajadores.delete()
    return redirect('trabajadores')

def editartrabajadores(request):
    id=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    apellido=request.POST["txtapellido"]
    num_telefono=request.POST["txtnum_telefono"]
    direccion=request.POST["txtdireccion"]
    fecha_ne=request.POST["txtfecha_ne"]
    fecha_ing=request.POST["txtfecha_ing"]
    trabajadores=Trabajadores.objects.get(id=id)
    trabajadores.nombre=nombre
    trabajadores.apellido=apellido
    trabajadores.num_telefono=num_telefono
    trabajadores.direccion=direccion
    trabajadores.fecha_ne=fecha_ne
    trabajadores.fecha_ing=fecha_ing
    trabajadores.save()
    return redirect('trabajadores')