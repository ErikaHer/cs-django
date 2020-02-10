from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

#Siempre que se crea una vista (5-11)
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Importar modelo
from Login.models import Example2
# Importar Serializer
from Login.serializer import Example2Serializers

class ExampleList2(APIView):
    # Metodo get para solicitar info
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Example2.objects.filter(delete = False)
        # many = True Si aplica si retorno multiples objetos
        serializer = Example2Serializers(queryset, many=True)
        return Response(serializer.data)

class CustonAuthToken(ObtainAuthToken):
    
    def post(self, request, * args, **kwars):
        serializer = self.serializer_class (data = request.data, 
                                            context = {
                                                    'request': request, 
                                                    }
                                            )
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username
        })