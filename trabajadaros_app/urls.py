from django.urls import path
from trabajadaros_app import views

urlpatterns = [
    path('trabajadores',views.inicio_vistaTrabajadores,name="trabajadores"),
    path("registrartrabajadores/", views.registrartrabajadores, name="registrartrabajadores/"),
    path("borrartrabajadores/<id>",views.borrartrabajadores, name="borrartrabajadores/"),
    path("seleccionartrabajadores/<id>", views.seleccionartrabajadores, name="selecionartrabajadores/"),
    path("editartrabajadores/", views.editartrabajadores, name="editartrabajadores")
]