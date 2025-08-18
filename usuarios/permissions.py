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
