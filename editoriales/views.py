from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from editoriales.models import Editorial
from editoriales.serializer import EditorialSerializer, CreateEditorialSerializer


@api_view(['GET', 'POST'])
def listar_editoriales(request):
    if request.method == 'GET':
        editoriales = Editorial.objects.all()
        serialized = EditorialSerializer(editoriales, many=True)
        return Response(data=serialized.data)

    if request.method == 'POST':
        serialized = CreateEditorialSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serialized.errors
            )
        serialized.save()
        return Response(data=serialized.data)


@api_view(['GET', 'DELETE', 'PUT'])
def detalle_editorial(request, editorial_id):
    try:
        editorial = Editorial.objects.get(id=editorial_id)
    except ObjectDoesNotExist as error:
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data=str(error)
        )

    if request.method == 'GET':
        serialized = EditorialSerializer(editorial)
        return Response(data=serialized.data)

    if request.method == 'PUT':
        serialized = EditorialSerializer(
            instance=editorial,
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
        editorial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
