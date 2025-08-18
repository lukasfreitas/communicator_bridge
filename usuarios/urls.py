from usuarios.views import UsuarioLogView
from django.urls import path

urlpatterns = [
    path("usuario-logs/<uuid:pk>/", UsuarioLogView.as_view(), name="usuario_logs"),
]