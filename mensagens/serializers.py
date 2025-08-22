from rest_framework import serializers
from mensagens.models import Mensagem

class MensagemCreateSerializer(serializers.Serializer):
    """
    Serializer para criar uma nova mensagem a ser enviada por um atendente.
    """
    canal_id = serializers.UUIDField(write_only=True, help_text="ID do Canal para enviar a mensagem.")
    remetente_id = serializers.UUIDField(write_only=True, help_text="ID do Usuário remetente da mensagem.")
    destinatario_id = serializers.UUIDField(write_only=True, help_text="ID do Usuário (Contato) para quem a mensagem será enviada.")
    conteudo = serializers.CharField(write_only=True, help_text="O conteúdo da mensagem.")

