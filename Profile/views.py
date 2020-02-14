#Siempre que se crea una vista (5-11)
from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

# Importar modelo
from Profile.models import ProfileModel
from Profile.models import CiudadModel
from Profile.models import GeneroModel
from Profile.models import OcupacionModel
from Profile.models import EstadoModel
from Profile.models import EstadoCivilModel
# Importar Serializer
from Profile.serializer import ProfileSerializers
from Profile.serializer import CiudadSerializers
from Profile.serializer import GeneroSerializers
from Profile.serializer import OcupacionSerializers
from Profile.serializer import EstadoSerializers
from Profile.serializer import EstadoCivilSerializers

class CiudadList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = CiudadModel.objects.filter(delete = False)
        # many = True Si aplica si retorno multiples objetos
        serializer = CiudadSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GeneroList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = GeneroModel.objects.filter(delete = False)
        # many = True Si aplica si retorno multiples objetos
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = OcupacionModel.objects.filter(delete = False)
        # many = True Si aplica si retorno multiples objetos
        serializer = OcupacionSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = EstadoModel.objects.filter(delete = False)
        # many = True Si aplica si retorno multiples objetos
        serializer = EstadoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoCivilList(APIView):
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = EstadoCivilModel.objects.filter(delete = False)
        # many = True Si aplica si retorno multiples objetos
        serializer = EstadoCivilSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = EstadoCivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ProfileList(APIView):
    # Metodo get para solicitar info
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = ProfileModel.objects.filter(delete = False)
        # many = True Si aplica si retorno multiples objetos
        serializer = ProfileSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self,request, format=None):
        serializer = ProfileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)