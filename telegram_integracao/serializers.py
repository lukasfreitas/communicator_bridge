from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    is_bot = serializers.BooleanField()
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255, allow_blank=True, required=False)
    language_code = serializers.CharField(max_length=10, allow_blank=True, required=False)

# Serializer para o objeto 'chat'
class ChatSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=255, allow_blank=True, required=False)
    last_name = serializers.CharField(max_length=255, allow_blank=True, required=False)

# Serializer para a mensagem
class MessageSerializer(serializers.Serializer):
    message_id = serializers.IntegerField()
    from_user = UserSerializer(source='from', read_only=True)  # Mapeia o campo 'from' para 'from_user'
    chat = ChatSerializer()
    date = serializers.IntegerField()
    text = serializers.CharField(max_length=4096, allow_blank=True, required=False)

# Serializer principal para o payload do webhook (a atualização completa)
class TelegramUpdateSerializer(serializers.Serializer):
    update_id = serializers.IntegerField()
    message = MessageSerializer()