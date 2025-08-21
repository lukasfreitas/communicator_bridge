"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RaizApiView, RaizApiV1View

# Padrões de URL da API v1
urls_api_v1 = [
    path('', RaizApiV1View.as_view(), name='raiz-api-v1'),
    # Autenticação
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Apps
    path('usuarios/', include('usuarios.urls')),
    path('canais/', include('Canais.urls')),
    path('integracoes/telegram/', include('telegram_integracao.urls')),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", RaizApiView.as_view(), name='raiz-api'),
    path("api/v1/", include(urls_api_v1)),
]
