from rest_framework import serializers

from .models import Pais
from .models import Ciudad
from .models import Persona
from .models import CalendarioSeguimiento
from .models import Sintoma
from .models import DiaSeguimiento
from .models import Posicion
from .models import Ubicacion
from .models import Transporte
from .models import Contacto
from .models import PersonaContacto


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = '__all__'    

class PersonaSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Persona
        fields = '__all__'

class CalendarioSeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalendarioSeguimiento
        fields = '__all__'    

class SintomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sintoma
        fields = '__all__'  


class DiaSeguimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaSeguimiento
        fields = '__all__'  

class PosicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posicion
        fields = '__all__'    

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = '__all__'    

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = '__all__'    

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = '__all__'    

class PersonaContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaContacto
        fields = '__all__'    


