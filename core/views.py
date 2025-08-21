from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class RaizApiView(APIView):
    """
    Esta view apresenta a lista de versões da API.
    """
    def get(self, request, format=None):
        return Response({
            'v1': reverse('raiz-api-v1', request=request, format=format),
        })

class RaizApiV1View(APIView):
    """
    Esta view apresenta os endpoints da v1 da API.
    """
    def get(self, request, format=None):
        return Response({
            'auth': reverse('token_obtain_pair', request=request, format=format),
            'usuarios': reverse('usuario-lista', request=request, format=format),
            'canais': reverse('canal-lista-cria', request=request, format=format),
        })
