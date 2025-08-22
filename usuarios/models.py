import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext_lazy as _
from auditlog.registry import auditlog


class Usuario(AbstractUser):
    """
    Modelo de usuário unificado para Atendentes, Contatos e Administradores.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class TipoUsuario(models.TextChoices):
        ADMINISTRADOR = "ADMINISTRADOR", _("Administrador")
        ATENDENTE = "ATENDENTE", _("Atendente")
        CONTATO = "CONTATO", _("Contato")

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.CONTATO,
        verbose_name=_("Tipo de Usuário"),
    )
    telefone = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        help_text="Número de telefone do usuário (se aplicável)."
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.tipo_usuario:
            group_name = self.get_tipo_usuario_display()
            group, created = Group.objects.get_or_create(name=group_name)
            self.groups.add(group)

    def __str__(self):
        return self.username


auditlog.register(Usuario)