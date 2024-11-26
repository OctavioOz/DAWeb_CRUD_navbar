from django.urls import path
from citas_app import views

urlpatterns = [
    path('citas',views.inicio_vistaCitas,name="citas"),
    path("registrarcitas/", views.registrarcitas, name="registrarcitas/"),
    path("borrarcitas/<id_cita>",views.borrarcitas, name="borrarcitas/"),
    path("seleccionarcitas/<id_cita>", views.seleccionarcitas, name="selecionarcitas/"),
    path("editarcitas/", views.editarcitas, name="editarcitas")
]