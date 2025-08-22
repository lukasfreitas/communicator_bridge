from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Canal
from .serializers import CanalSerializer
from usuarios.permissions import IsAdministrador

class CanalListaCriaView(generics.ListCreateAPIView):
    """
    Endpoint da API para listar e criar Canais.
    Apenas administradores podem acessar.
    """
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer
    # permission_classes = [IsAdministrador]

class CanalDetalheAtualizaDeletaView(generics.RetrieveUpdateDestroyAPIView):
    """
    Endpoint da API para detalhar, atualizar e deletar um Canal.
    Apenas administradores podem acessar.
    """
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer
    # permission_classes = [IsAdministrador]
