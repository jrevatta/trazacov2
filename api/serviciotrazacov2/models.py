from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    continente = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = '1. Paises'

    def __str__(self):
        return "{0}".format(self.nombre)

    def __unicode__(self):
        return "{0}".format(self.nombre)

class Ciudad(models.Model):
    TIPO_ESTADO = (
        ('C', 'Controlado'),
        ('E', 'Emergencia'),
        ('Q', 'Cuarentena'),
        ('X', 'Endemica')
    )
    nombre = models.CharField(max_length=100)
    numeroPoblacion = models.IntegerField()
    estado = models.CharField(max_length=1, choices = TIPO_ESTADO, default='C')
    pais_origen  = models.ForeignKey(Pais, blank=True, null = True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = '2. Ciudades'
    def __str__(self):
        return "{0}".format(self.nombre)

    def __unicode__(self):
        return "{0}".format(self.nombre)

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    paterno = models.CharField(max_length=120)
    materno = models.CharField(max_length=120)
    edad = models.IntegerField()
    dni = models.CharField(max_length=15)
    pasaporte = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = '3. Personas'
    def __str__(self):
        return "{0} {1}".format(self.nombre, self.paterno)

    def __unicode__(self):
        return "{0} {1}".format(self.nombre, self.paterno)


class CalendarioSeguimiento(models.Model):
    dia_inicio = models.DateField()
    dia_fin = models.DateField()
    persona = models.ForeignKey(Persona, blank=True, null=True, on_delete=models.SET_NULL)
    class Meta:
        verbose_name = 'Calendario Seguimiento'
        verbose_name_plural = '4. Calendario Seguimiento'
    def __str__(self):
        return "{0} {1}".format(self.dia_inicio, self.dia_fin)

    def __unicode__(self):
        return "{0} {1}".format(self.dia_inicio, self.dia_fin)

class Sintoma(models.Model):
    temperatura = models.FloatField()
    dolor_garganta = models.BinaryField()
    congestion_nasal = models.BinaryField()
    secreccion_nasal = models.BinaryField()
    tos_seca = models.BinaryField()
    cansancio = models.BinaryField()
    dificultad_respirar = models.BinaryField()
    diarrea = models.BinaryField()
    class Meta:
        verbose_name = 'Sintoma'
        verbose_name_plural = '5. Sintomas'
    

    def __str__(self):
        return '{}'.format(self.temperatura)

    def __unicode__(self):
        return '{}'.format(self.temperatura)


class DiaSeguimiento(models.Model):
    dia = models.DateTimeField()
    sintoma = models.ForeignKey(Sintoma,  blank=True, null=True, on_delete=models.SET_NULL)
    calendario = models.ForeignKey(CalendarioSeguimiento,  blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Dia Seguimiento'
        verbose_name_plural = '6 Dias de Seguimiento'
    

    def __str__(self):
        return '{} {}'.format(self.latitud, self.longitud)

    def __unicode__(self):
        return '{} {}'.format(self.latitud, self.longitud)


class Posicion(models.Model):
    latitud = models.IntegerField()
    longitud = models.IntegerField()

    class Meta:
        verbose_name = 'Posicion'
        verbose_name_plural = '7 Posiciones'
    

    def __str__(self):
        return '{} {}'.format(self.latitud, self.longitud)

    def __unicode__(self):
        return '{} {}'.format(self.latitud, self.longitud)


class Ubicacion(models.Model):

    TIPO_UBICACION = (
        ('D', 'Departamento'),
        ('C', 'Cuarto'),
        ('H', 'Habitacion'),
        ('A', 'Casa'),
        ('E', 'Trabajo'), 
        ('U', 'Escuela'),
        ('X', 'Exterior'),
        ('M', 'Mercado')
    )

    tipo_ubicacion = models.CharField(max_length=1, choices=TIPO_UBICACION, default='D')
    direccion = models.CharField(max_length=200, null=True)
    posicion = models.ForeignKey(Posicion, blank=True, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name = 'Ubicacion'
        verbose_name_plural = '8 Ubicaciones'

    def __str__(self):
        return "{} {}".format(self.id, self.tipo_ubicacion)

    def __unicode__(self):
        return "{} {}".format(self.id, self.tipo_ubicacion)


class Transporte(models.Model):
    TIPO_TRANSPORTE = (
        ('A', 'Auto'),
        ('B', 'Bus Viaje'),
        ('C', 'Bus Urbano'),
        ('D', 'Taxi'),
        ('E', 'Avion'), 
        ('F', 'Fluvial'),
        ('G', 'Barco'),
        ('H', 'Moto')
    )    
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()
    tipo = models.CharField(max_length=1, choices=TIPO_TRANSPORTE)
    numero_pasajeros = models.IntegerField()

    class Meta:
        verbose_name = 'Transporte'
        verbose_name_plural = '9 Transporte'

    def __str__(self):
        return "{} {}".format(self.id, self.tipo)

    def __unicode__(self):
        return "{} {}".format(self.id, self.tipo)


class Contacto(models.Model):
    ubicacion = models.ForeignKey(Ubicacion, blank=True, null=True, on_delete=models.SET_NULL)
    transporte = models.ForeignKey(Transporte, blank=True, null=True, on_delete=models.SET_NULL)
    posicion  = models.ForeignKey(Posicion, blank=True, null=True, on_delete=models.SET_NULL)
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = '9 Contacto'

    def __str__(self):
        return "{} {}".format(self.id, self.hora_inicio, self.hora_fin)

    def __unicode__(self):
        return "{} {}".format(self.id, self.hora_inicio, self.hora_fin)


class PersonaContacto(models.Model):
    TIPO_PERSONA = (
        ('F', 'Familiar'),
        ('C', 'Colega'),
        ('P', 'Pasajero'),
        ('D', 'Conductor'),
        ('E', 'Desconocido'),
        ('A', 'Asistente')
    ) 
    nombre = models.CharField(max_length=80, blank=True, null=True)
    paterno = models.CharField(max_length=80, blank=True, null=True)
    materno = models.CharField(max_length=80, blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    referencia_ubicacion = models.CharField(max_length=500, blank=True, null=True)
    contacto = models.ForeignKey(Contacto, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'PersonaContacto'
        verbose_name_plural = '9 Personas Contacto'

    def __str__(self):
        return "{} {}".format(self.id, self.nombre, self.paterno)

    def __unicode__(self):
        return "{} {}".format(self.id, self.nombre, self.paterno)

