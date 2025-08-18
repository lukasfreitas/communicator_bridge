from django.urls import path
from .views import WebhookTelegramAPIView, TelegramGetmeView, TelegramWebhookConfigView

urlpatterns = [
    path('webhook/', WebhookTelegramAPIView.as_view(), name='telegram-webhook'),
    path('getme/', TelegramGetmeView.as_view(), name='telegram-getme'),
    path('webhook-config/', TelegramWebhookConfigView.as_view(), name='telegram-webhook-config'),
]