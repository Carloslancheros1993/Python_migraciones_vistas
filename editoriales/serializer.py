from rest_framework.serializers import ModelSerializer

from editoriales.models import Editorial


class EditorialSerializer(ModelSerializer):
    class Meta:
        model = Editorial
        fields = ('__all__')

class CreateEditorialSerializer(ModelSerializer):
    class Meta:
        model = Editorial
        fields = '__all__'
