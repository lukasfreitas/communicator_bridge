from rest_framework import serializers
from .models import Canal

class CanalSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Canal.
    """
    class Meta:
        model = Canal
        fields = ['id', 'nome', 'tipo', 'ativo', 'configuracao']
        read_only_fields = ['id']
