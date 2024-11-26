from django.urls import path
from cortes_app import views

urlpatterns = [
    path('cortes',views.inicio_vistacortes,name="cortes"),
    path("registrarcortes/", views.registrarcortes, name="registrarcortes/"),
    path("borrarcortes/<id_corte>",views.borrarcortes, name="borrarcortes/"),
    path("seleccionarcortes/<id_corte>", views.seleccionarcortes, name="selecionarcortes/"),
    path("editarcortes/", views.editarcortes, name="editarcortes")
]