from django.urls import path

from autores.views import listar_autores, detalle_autor

app_name = 'autores'
urlpatterns = [
    path('', listar_autores),
    path('<int:autor_id>/', detalle_autor),
]