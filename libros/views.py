from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from libros.models import Libro
from libros.serializer import LibroSerializer, CreateLibroSerializer


@api_view(['GET', 'POST'])
def listar_libros(request):

    if request.method == 'GET':
        libros = Libro.objects.all()
        serialized = LibroSerializer(libros, many=True)
        return Response(data=serialized.data)
        
    if request.method == 'POST':
        serialized = CreateLibroSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )
        serialized.save()
        return Response(data=serialized.data)

@api_view(['GET', 'DELETE', 'PUT'])
def detalle_libro(request, libro_id):
    try:
        libro = Libro.objects.get(id=libro_id)
    except ObjectDoesNotExist as error:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data=str(error)
        )

    if request.method == 'GET':
        serialized = LibroSerializer(libro)
        return Response(data=serialized.data)

    if request.method == 'PUT':
        serialized = LibroSerializer(
            instance=libro,
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
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)