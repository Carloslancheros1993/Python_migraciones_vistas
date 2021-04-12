from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from autores.models import Autor
from autores.serializer import AutorSerializer, CreateAutorSerializer


@api_view(['GET', 'POST'])
def listar_autores(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        serialized = AutorSerializer(autores, many=True)
        return Response(data=serialized.data)

    if request.method == 'POST':
        serialized = CreateAutorSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )
        serialized.save()
        return Response(data=serialized.data)


@api_view(['GET', 'DELETE', 'PUT'])
def detalle_autor(request, autor_id):
    try:
        autor = Autor.objects.get(id=autor_id)
    except ObjectDoesNotExist as error:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data=str(error)
        )

    if request.method == 'GET':
        serialized = AutorSerializer(autor)
        return Response(data=serialized.data)

    if request.method == 'PUT':
        serialized = AutorSerializer(
            instance=autor,
            data=request.data,
            partial=True
        )
        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )
        serialized.save()
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    if request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
