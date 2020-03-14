from rest_framework import viewsets
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
from .serializer import *


class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class CalendarioSeguimientoViewSet(viewsets.ModelViewSet):
    queryset = CalendarioSeguimiento.objects.all()
    serializer_class = CalendarioSeguimientoSerializer

class SintomaViewSet(viewsets.ModelViewSet):
    queryset = Sintoma.objects.all()
    serializer_class = SintomaSerializer

class DiaSeguimientoViewSet(viewsets.ModelViewSet):
    queryset = DiaSeguimiento.objects.all()
    serializer_class = DiaSeguimientoSerializer

class PosicionViewSet(viewsets.ModelViewSet):
    queryset = Posicion.objects.all()
    serializer_class = PosicionSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer

class TransporteViewSet(viewsets.ModelViewSet):
    queryset = Transporte.objects.all()
    serializer_class = TransporteSerializer

class ContactoViewSet(viewsets.ModelViewSet):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer

class PersonaContactoViewSet(viewsets.ModelViewSet):
    queryset = PersonaContacto.objects.all()
    serializer_class = PersonaContactoSerializer


