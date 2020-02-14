#---------AGREGANDO LIBRERIAS FRAMEWORK ---------
from rest_framework import routers, serializers, viewsets

#---------AGREGANDO MODELOS ------------
from Profile.models import ProfileModel
from Profile.models import CiudadModel
from Profile.models import GeneroModel
from Profile.models import OcupacionModel
from Profile.models import EstadoModel
from Profile.models import EstadoCivilModel

class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = CiudadModel
        fields = ('__all__')

class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = GeneroModel
        fields = ('__all__')

class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = OcupacionModel
        fields = ('__all__')

class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstadoModel
        fields = ('__all__')

class EstadoCivilSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivilModel
        fields = ('__all__')

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')