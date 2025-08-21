from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from auditlog.models import LogEntry
from .models import Usuario
from .serializers import LogEntrySerializer, UsuarioSerializer
from .permissions import IsAdministrador


class UsuarioLogView(ListAPIView):
    """
    View para listar os logs de um usuário específico.
    """

    serializer_class = LogEntrySerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    def get_queryset(self):
        """
        Retorna os logs para o usuário especificado na URL.
        """
        print("Fetching logs for user with ID:", self.kwargs)
        user_id = self.kwargs["pk"]

        return LogEntry.objects.filter(object_pk=user_id)


class ListaUsuariosView(ListAPIView):
    """
    Endpoint da API que lista todos os usuários.
    Apenas administradores podem acessar.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]