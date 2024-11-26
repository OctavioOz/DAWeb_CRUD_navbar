from django.urls import path
from clientes_app import views

urlpatterns = [
    path('clientes',views.inicio_vistaClientes,name="clientes"),
    path("registrarclientes/", views.registrarclientes, name="registrarclientes/"),
    path("borrarclientes/<id>",views.borrarclientes, name="borrarclientes/"),
    path("seleccionarclientes/<id>", views.seleccionarclientes, name="selecionarclientes/"),
    path("editarclientes/", views.editarclientes, name="editarclientes")
]