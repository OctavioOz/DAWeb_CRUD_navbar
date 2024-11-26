from django.shortcuts import render, redirect
from .models import Prodcutos

# Create your views here.

def inicio_vistaProductos(request):
    losprodcutos=Prodcutos.objects.all()
    return render(request,'gestionarprodcutos.html', {"misprodcutos":losprodcutos})

def registrarprodcutos(request):
    id_producto=request.POST["numid_producto"]
    tipo=request.POST["txttipo"]
    color=request.POST["txtcolor"]
    olor=request.POST["txtolor"]
    gramos=request.POST["txtgramos"]
    uso=request.POST["txtuso"]
    precio=request.POST["numprecio"]
    guardarprodcutos=Prodcutos.objects.create(id_producto=id_producto, tipo=tipo, color=color, olor=olor, gramos=gramos, uso=uso, precio=precio)
    return redirect('productos')

def seleccionarprodcutos(request,id_producto):
    prodcutos=Prodcutos.objects.get(id_producto=id_producto)
    return render(request,"editarprodcutos.html", {"misprodcutos":prodcutos})

def borrarprodcutos(request,id_producto):
    prodcutos=Prodcutos.objects.get(id_producto=id_producto)
    prodcutos.delete()
    return redirect('productos')

def editarprodcutos(request):
    id_producto=request.POST["numid_producto"]
    tipo=request.POST["txttipo"]
    color=request.POST["txtcolor"]
    olor=request.POST["txtolor"]
    gramos=request.POST["txtgramos"]
    uso=request.POST["txtuso"]
    precio=request.POST["numprecio"]
    prodcutos=Prodcutos.objects.get(id_producto=id_producto)
    prodcutos.tipo=tipo
    prodcutos.color=color
    prodcutos.olor=olor
    prodcutos.gramos=gramos
    prodcutos.uso=uso
    prodcutos.precio=precio
    prodcutos.save()
    return redirect('productos')