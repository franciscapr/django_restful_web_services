from rest_framework import serializers
from toys.models import Toy

class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy    # Especificamos el modelo
        fields = ('id',    # Incluimos los nombres de los campos que queremos incluir en la serializacion del modelo
                  'name',
                  'description',
                  'release_date',
                  'toy_category',
                  'was_include_in_home')