from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from auditlog.models import LogEntry

from .models import Usuario
from .permissions import IsAdministrador
from .serializers import LogEntrySerializer, UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Endpoint da API para CRUD de Usuários.
    Apenas administradores podem acessar.
    """

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    @action(
        detail=True,
        methods=["get"],
        url_path="logs",
        serializer_class=LogEntrySerializer,
    )
    def logs(self, request, pk=None):
        """
        View para listar os logs de um usuário específico.
        """
        usuario = self.get_object()
        queryset = LogEntry.objects.filter(object_pk=usuario.pk)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
