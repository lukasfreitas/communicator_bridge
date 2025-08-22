# canais/models.py

import uuid
from auditlog.registry import auditlog
from django.db import models

class Canal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(
        max_length=50,
        unique=True,
        help_text="Nome do canal de comunicação (ex: 'Telegram', 'Facebook Messenger')"
    )
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('TELEGRAM', 'Telegram'),
            ('FACEBOOK', 'Facebook Messenger'),
            ('SLACK', 'Slack'),
            ('MOCK', 'Canal Mock')
        ],
        help_text="O tipo de plataforma de comunicação"
    )
    configuracao = models.JSONField(
        help_text="Configurações específicas do canal (ex: token do bot, segredo do webhook)"
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True, help_text="Indica se o canal está ativo")

    class Meta:
        verbose_name_plural = "Canais"

    def __str__(self):
        return self.nome
    
auditlog.register(Canal)
