from django.urls import path
from .views import CanalListaCriaView, CanalDetalheAtualizaDeletaView

urlpatterns = [
    path('', CanalListaCriaView.as_view(), name='canal-lista-cria'),
    path('<int:pk>/', CanalDetalheAtualizaDeletaView.as_view(), name='canal-detalhe'),
]
