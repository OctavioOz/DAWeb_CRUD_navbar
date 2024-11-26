from django.shortcuts import render, redirect
from .models import Citas

# Create your views here.

def inicio_vistaCitas(request):
    lascitas=Citas.objects.all()
    return render(request,'gestionarcitas.html', {"miscitas":lascitas})

def registrarcitas(request):
    id_cita=request.POST["numid_cita"]
    id_cliente=request.POST["numid_cliente"]
    id_trabajador=request.POST["numid_trabajador"]
    id_corte=request.POST["numid_corte"]
    fecha_cita=request.POST["txtfecha_cita"]
    total=request.POST["txttotal"]
    guardarCitas=Citas.objects.create(id_cita=id_cita, id_cliente=id_cliente, id_trabajador=id_trabajador, id_corte=id_corte, fecha_cita=fecha_cita, total=total)
    return redirect('citas')

def seleccionarcitas(request,id_cita):
    citas=Citas.objects.get(id_cita=id_cita)
    return render(request,"editarcitas.html", {"miscitas":citas})

def borrarcitas(request,id_cita):
    citas=Citas.objects.get(id_cita=id_cita)
    citas.delete()
    return redirect('citas')

def editarcitas(request):
    id_cita=request.POST["numid_cita"]
    id_cliente=request.POST["numid_cliente"]
    id_trabajador=request.POST["numid_trabajador"]
    id_corte=request.POST["numid_corte"]
    fecha_cita=request.POST["txtfecha_cita"]
    total=request.POST["txttotal"]
    citas=Citas.objects.get(id_cita=id_cita)
    citas.id_cliente=id_cliente
    citas.id_trabajador=id_trabajador
    citas.id_corte=id_corte
    citas.fecha_cita=fecha_cita
    citas.total=total
    citas.save()
    return redirect('citas')