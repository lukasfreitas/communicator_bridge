from auditlog.models import LogEntry
from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo Usuario.

    Converte objetos Usuario para JSON e vice-versa,
    validando os dados recebidos.
    """

    class Meta:
        model = Usuario
        # Campos que serão expostos na API
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "tipo_usuario",
        ]
        # Campos que são apenas para leitura (não podem ser definidos na criação/atualização)
        read_only_fields = ["id"]


class LogEntrySerializer(serializers.ModelSerializer):
    """
    Serializer para o modelo LogEntry.
    """

    class Meta:
        model = LogEntry
        fields = "__all__"