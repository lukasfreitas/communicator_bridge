from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# O router gera as URLs para o ViewSet (list, create, retrieve, update, destroy)
# e também para a action customizada 'logs'.
router = DefaultRouter()
router.register(r"", views.UsuarioViewSet, basename="usuario")

# As urlpatterns do app agora são simplesmente as URLs geradas pelo router.
urlpatterns = router.urls