from django.urls import path
from mensagens.views import MensagemView

app_name = 'mensagens'

urlpatterns = [
    path('enviar/', MensagemView.as_view(), name='enviar_mensagem'),
]
