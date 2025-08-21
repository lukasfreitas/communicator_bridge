# canais/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from django.conf import settings
from django.http import JsonResponse
from django.urls import reverse
from .services import TelegramApiClient
from .serializers import TelegramUpdateSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# A sua view TelegramGetme reescrita como uma APIView
@method_decorator(csrf_exempt, name='dispatch')
class TelegramGetmeView(APIView):
    def get(self, request, *args, **kwargs):
        telegram_service = TelegramApiClient(settings.TELEGRAM_BOT_ACCESS_TOKEN)
        api_response = telegram_service.Post("getMe")
        return JsonResponse(api_response)

# Sua view para configurar o webhook
@method_decorator(csrf_exempt, name='dispatch')
class TelegramWebhookConfigView(APIView):
    authentication_classes = []
    permission_classes = []

    def dispatch(self, request, *args, **kwargs):
        self.telegram_service = TelegramApiClient(settings.TELEGRAM_BOT_ACCESS_TOKEN)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        webhook_url = request.build_absolute_uri(reverse("telegram-webhook"))
        api_response = self.telegram_service.setWebhook(webhook_url, settings.TELEGRAM_BOT_WEBHOOK_SECRET)
        if api_response and api_response.get("ok"):
            return Response(api_response, status=status.HTTP_200_OK)
        else:
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        api_response = self.telegram_service.Post("getWebhookInfo")
        if api_response and api_response.get("ok"):
            return Response(api_response, status=status.HTTP_200_OK)
        else:
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        api_response = self.telegram_service.Post("deleteWebhook")
        if api_response and api_response.get("ok"):
            return Response(api_response, status=status.HTTP_200_OK)
        else:
            return Response(api_response, status=status.HTTP_400_BAD_REQUEST)

# Sua view para receber as mensagens do webhook
@method_decorator(csrf_exempt, name='dispatch')
class WebhookTelegramAPIView(APIView):
    # A view não precisa de autenticação ou permissões
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = TelegramUpdateSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            
            update_data = serializer.validated_data
            message = update_data['message']
            chat_id = message['chat']['id']
            text = message.get('text')
            print(f"Mensagem recebida do chat {chat_id}: {text}")
            # ... sua lógica de negócio para processar a mensagem ...
            return Response({"status": "Mensagem processada com sucesso."}, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            print(f"Erro de validação: {e.detail}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class MessagesAiAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            print(data)
            mensagem_webhook = data.get("message")
            return Response(
                {"status": "mensagem recebida e processada"}, 
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )