from django.urls import path

from libros.views import listar_libros, detalle_libro

app_name = 'libros'
urlpatterns = [
    path('', listar_libros),
    path('<int:libro_id>/', detalle_libro),
]