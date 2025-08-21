import uuid
from django.db import models
from django.conf import settings
from Canais.models import Canal

class Mensagem(models.Model):
    """
    Representa uma mensagem trocada entre um Contato e um Atendente
    através de um Canal de comunicação.
    """
    class StatusMensagem(models.TextChoices):
        ENVIADA = 'ENVIADA', 'Enviada'
        ENTREGUE = 'ENTREGUE', 'Entregue'
        LIDA = 'LIDA', 'Lida'
        FALHOU = 'FALHOU', 'Falhou'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Relacionamentos
    canal = models.ForeignKey(
        Canal,
        on_delete=models.PROTECT, # Evita que um canal seja deletado se tiver mensagens
        related_name='mensagens',
        help_text="Canal pelo qual a mensagem foi enviada."
    )
    remetente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mensagens_enviadas',
        help_text="Usuário que enviou a mensagem (Atendente ou Contato)."
    )
    destinatario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mensagens_recebidas',
        help_text="Usuário que recebeu a mensagem (Atendente ou Contato)."
    )
    
    # Conteúdo da Mensagem
    conteudo = models.TextField(
        help_text="O conteúdo textual da mensagem."
    )
    
    # Metadados
    data_envio = models.DateTimeField(
        auto_now_add=True,
        help_text="Data e hora em que a mensagem foi criada."
    )
    status = models.CharField(
        max_length=10,
        choices=StatusMensagem.choices,
        default=StatusMensagem.ENVIADA,
        help_text="O status atual da mensagem."
    )
    
    # Campo para ID da mensagem externa (ex: message_id do Telegram)
    id_externo = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        db_index=True,
        help_text="ID da mensagem no sistema externo (ex: Telegram, WhatsApp)."
    )

    class Meta:
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"
        ordering = ['-data_envio'] # Ordena as mensagens da mais nova para a mais antiga

    def __str__(self):
        return f"De {self.remetente} para {self.destinatario} em {self.data_envio:%d/%m/%Y %H:%M}"