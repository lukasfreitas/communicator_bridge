from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                             TokenRefreshView)

from usuarios.views import UsuarioLogView

urlpatterns = [
    # Autenticação JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Logs
    path("usuario-logs/<uuid:pk>/", UsuarioLogView.as_view(), name="usuario_logs"),
]
