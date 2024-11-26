from django.urls import path
from venta_productos_app import views

urlpatterns = [
    path('venta_producto',views.inicio_vistaVenta_Producto,name="venta_producto"),
    path("registrarventa_productos/", views.registrarventa_productos, name="registrarventa_productos/"),
    path("borrarventa_productos/<id_venta>",views.borrarventa_productos, name="borrarventa_productos/"),
    path("seleccionarventa_productos/<id_venta>", views.seleccionarventa_productos, name="selecionarventa_productos/"),
    path("editarventa_productos/", views.editarventa_productos, name="editarventa_productos")
]