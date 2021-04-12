from rest_framework.serializers import ModelSerializer

from libros.models import Libro


class LibroSerializer(ModelSerializer):
    class Meta:
        model = Libro
        fields = ('__all__')

class CreateLibroSerializer(ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
