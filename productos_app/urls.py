from django.urls import path
from productos_app import views

urlpatterns = [
    path('productos',views.inicio_vistaProductos,name="productos"),
    path("registrarprodcutos/", views.registrarprodcutos, name="registrarprodcutos/"),
    path("borrarprodcutos/<id_producto>",views.borrarprodcutos, name="borrarprodcutos/"),
    path("seleccionarprodcutos/<id_producto>", views.seleccionarprodcutos, name="selecionarprodcutos/"),
    path("editarprodcutos/", views.editarprodcutos, name="editarprodcutos")
]