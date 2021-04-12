from django.urls import path

from editoriales.views import listar_editoriales, detalle_editorial

app_name = 'editoriales'
urlpatterns = [
    path('', listar_editoriales),
    path('<int:editorial_id>/', detalle_editorial),
]