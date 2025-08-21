from django.urls import path
from .views import ListaUsuariosView, UsuarioLogView

urlpatterns = [
    path("", ListaUsuariosView.as_view(), name="usuario-lista"),
    path("<uuid:pk>/logs/", UsuarioLogView.as_view(), name="usuario-logs"),
]
