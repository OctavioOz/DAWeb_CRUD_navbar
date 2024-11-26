from django.shortcuts import render, redirect
from .models import Cortes

# Create your views here.

def inicio_vistacortes(request):
    loscortes=Cortes.objects.all()
    return render(request,'gestionarcortes.html', {"miscortes":loscortes})

def registrarcortes(request):
    id_corte=request.POST["numid_corte"]
    nombre_corte=request.POST["txtnombre_corte"]
    tipo_corte=request.POST["txttipo_corte"]
    precio=request.POST["numprecio"]
    guardarCortes=Cortes.objects.create(id_corte=id_corte, nombre_corte=nombre_corte, tipo_corte=tipo_corte, precio=precio)
    return redirect('cortes')

def seleccionarcortes(request,id_corte):
    cortes=Cortes.objects.get(id_corte=id_corte)
    return render(request,"editarcortes.html", {"miscortes":cortes})

def borrarcortes(request,id_corte):
    cortes=Cortes.objects.get(id_corte=id_corte)
    cortes.delete()
    return redirect('cortes')

def editarcortes(request):
    id_corte=request.POST["numid_corte"]
    nombre_corte=request.POST["txtnombre_corte"]
    tipo_corte=request.POST["txttipo_corte"]
    precio=request.POST["numprecio"]
    cortes=Cortes.objects.get(id_corte=id_corte)
    cortes.id_corte=id_corte
    cortes.nombre_corte=nombre_corte
    cortes.tipo_corte=tipo_corte
    cortes.precio=precio
    cortes.save()
    return redirect('cortes')