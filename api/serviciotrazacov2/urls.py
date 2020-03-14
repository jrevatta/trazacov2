from rest_framework import routers
from django.urls import path, include
from . import views


router = routers.DefaultRouter()

router.register(r'pais', views.PaisViewSet)
router.register(r'ciudad', views.CiudadViewSet)
router.register(r'persona', views.PersonaViewSet)
router.register(r'calendarioseguimiento', views.CalendarioSeguimientoViewSet)
router.register(r'sintoma', views.SintomaViewSet)
router.register(r'diaseguimiento', views.DiaSeguimientoViewSet)
router.register(r'posicion', views.PosicionViewSet)
router.register(r'ubicacion', views.UbicacionViewSet)
router.register(r'transporte', views.TransporteViewSet)
router.register(r'contacto', views.ContactoViewSet)
router.register(r'personacontacto', views.PersonaContactoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]