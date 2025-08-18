# Guia de Implementação: Gerenciamento de Permissões

Este documento detalha o processo de configuração de um sistema de gerenciamento de permissões baseado em papéis (`Administrador`, `Atendente`, `Contato`) para a aplicação, utilizando os recursos nativos do Django e o Django REST Framework.

## Passo 1: Ajustar o Modelo de Usuário

A primeira etapa é garantir que seu modelo `Usuario` possa diferenciar os tipos de usuário. Faremos isso adicionando um campo de `choices`.

**Edite o arquivo `usuarios/models.py`:**

```python
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class Usuario(AbstractUser):
    """
    Modelo de usuário customizado.
    """
    class TipoUsuario(models.TextChoices):
        ADMINISTRADOR = 'ADMINISTRADOR', _('Administrador')
        ATENDENTE = 'ATENDENTE', _('Atendente')
        CONTATO = 'CONTATO', _('Contato')

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.CONTATO,
        verbose_name=_('Tipo de Usuário')
    )

    # Adicione seus outros campos aqui, se houver...

    def save(self, *args, **kwargs):
        # Antes de salvar, garantimos que o usuário seja atribuído ao grupo correto.
        super().save(*args, **kwargs)
        if self.tipo_usuario:
            group_name = self.get_tipo_usuario_display() # Pega o nome legível do choice
            group, created = Group.objects.get_or_create(name=group_name)
            self.groups.add(group)

    def __str__(self):
        return self.username
```

**O que fizemos:**
1.  **`TipoUsuario` (Enum):** Criamos uma classe interna para definir as opções de papéis. Usar `TextChoices` é uma boa prática para manter o código limpo e legível.
2.  **`tipo_usuario` (Campo):** Adicionamos um campo `CharField` que armazena o papel do usuário.
3.  **Sobrescrita do `save()`:** Modificamos o método `save` para que, toda vez que um usuário for salvo, ele seja automaticamente associado a um grupo do Django com o nome correspondente ao seu `tipo_usuario`. Isso automatiza a criação e atribuição de grupos.

Após modificar o `models.py`, crie e aplique as migrações:
```bash
python manage.py makemigrations usuarios
python manage.py migrate
```

## Passo 2: Criar Classes de Permissão Customizadas

Para controlar o acesso em suas views da API, vamos criar classes de permissão específicas para cada papel no Django REST Framework.

**Crie um novo arquivo `usuarios/permissions.py`:**

```python
from rest_framework.permissions import BasePermission

class IsAdministrador(BasePermission):
    """
    Permite acesso apenas a usuários do grupo Administrador.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Administrador').exists()

class IsAtendente(BasePermission):
    """
    Permite acesso apenas a usuários do grupo Atendente.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Atendente').exists()

class IsContato(BasePermission):
    """
    Permite acesso apenas a usuários do grupo Contato.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Contato').exists()
```

**O que fizemos:**
- Criamos três classes que herdam de `BasePermission`.
- Cada classe verifica se o usuário que está fazendo a requisição (`request.user`) pertence a um grupo específico (`Administrador`, `Atendente` ou `Contato`).

## Passo 3: Aplicar as Permissões nas Views

Agora, você pode usar essas classes de permissão para proteger suas API endpoints.

**Exemplo de uso no arquivo `usuarios/views.py`:**

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdministrador, IsAtendente

class PainelAdminView(APIView):
    """
    Endpoint de exemplo que só pode ser acessado por Administradores.
    """
    permission_classes = [IsAuthenticated, IsAdministrador]

    def get(self, request, format=None):
        content = {'message': f'Olá, Administrador {request.user.username}!'}
        return Response(content)

class ChatAtendenteView(APIView):
    """
    Endpoint de exemplo que pode ser acessado por Atendentes e Administradores.
    """
    # A permissão é verificada em ordem. Se for Administrador, já passa.
    permission_classes = [IsAuthenticated, IsAdministrador | IsAtendente]

    def get(self, request, format=None):
        content = {'message': f'Olá, Atendente {request.user.username}!'}
        return Response(content)

```

**O que fizemos:**
- Importamos as novas classes de permissão.
- Na `permission_classes` de cada view, adicionamos as permissões desejadas.
- O Django REST Framework permite combinar permissões com operadores lógicos como `|` (OU) e `&` (E), o que torna o sistema muito flexível. Por exemplo, `IsAdministrador | IsAtendente` permite o acesso se o usuário for de *qualquer um* dos dois grupos.

## Conclusão

Com essas três etapas, você terá um sistema de permissões funcional e escalável. A lógica fica centralizada no modelo `Usuario` e nas classes de permissão, tornando suas views mais limpas e a manutenção do código mais simples.

**Próximos Passos Sugeridos:**
- **Permissões a Nível de Objeto:** Para casos mais complexos, como permitir que um atendente edite *apenas* suas próprias mensagens, você pode implementar o método `has_object_permission` nas suas classes de permissão.
- **Django Admin:** Os grupos e as associações de usuários a eles podem ser facilmente visualizados e gerenciados através da interface de administração do Django.
