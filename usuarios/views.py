from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser
from auditlog.models import LogEntry
from .serializers import LogEntrySerializer

class UsuarioLogView(ListAPIView):
    """
    View para listar os logs de um usuário específico.
    """
    serializer_class = LogEntrySerializer

    def get_queryset(self):
        """
        Retorna os logs para o usuário especificado na URL.
        """
        print("Fetching logs for user with ID:", self.kwargs)
        user_id = self.kwargs['pk']
    
        return LogEntry.objects.filter(object_pk=user_id)
