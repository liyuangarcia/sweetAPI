from django.db import models
import uuid

#Aeropuertos
class Aeropuertos(models.Model):
     aaerodescripcion = models.CharField(max_length=20)
     alugar = models.CharField(max_length=50)
     asiglas = models.CharField(max_length=3)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(Aeropuertos, self).save(*args, **kwargs)

     def __str__(self):
         return self.aaerodescripcion
#Guias
class GuiasPescas(models.Model):
     GNOMBREDELGUIA = models.CharField(max_length=20)

     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(GuiasPescas, self).save(*args, **kwargs)

     def __str__(self):
         return self.GNOMBREDELGUIA
#POSIBLES ACTIVIDADES EN EL POLO
class TipoPesca(models.Model):
     MPESCA = models.CharField(max_length=10)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(TipoPesca, self).save(*args, **kwargs)

     def __str__(self):
         return self.MPESCA
#Regiones de pesca
class RegionesPesca(models.Model):
     REGIONES = models.CharField(max_length=20)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(RegionesPesca, self).save(*args, **kwargs)

     def __str__(self):
         return self.REGIONES
#Asignacion de lanchas a los polos de pescas
class DestPesca(models.Model):
     DESTINO = models.CharField(max_length=20)
     REGIONES = models.ForeignKey(
        RegionesPesca,
        null=True,                  # Permite valores NULL en la base de datos
        blank=True,
        on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
     )
     LANCHAS = models.IntegerField(blank=True, null=True, default=None)

     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(DestPesca, self).save(*args, **kwargs)

     def __str__(self):
         return self.DESTINO
#Destinos o polos turisticos
class Destinos(models.Model):
     DESTINO = models.CharField(max_length=20)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(Destinos, self).save(*args, **kwargs)

     def __str__(self):
         return self.DESTINO
#Marinas
class Marinas(models.Model):
     Lmarina = models.CharField(max_length=20)
     Nmarina = models.CharField(max_length=50)
     NoficialMarina = models.CharField(max_length=50)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(Marinas, self).save(*args, **kwargs)

     def __str__(self):
         return self.Nmarina
#Lanchas por Region
class LanchasRegion(models.Model):
     REGIONES = models.ForeignKey(
        RegionesPesca,
        null=True,                  # Permite valores NULL en la base de datos
        blank=True,
        on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
     )
     SumaDeLANCHAS = models.IntegerField()
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(LanchasRegion, self).save(*args, **kwargs)

     def __str__(self):
         return self.REGION
#Municipios
class Municipios(models.Model):
     polo = models.ForeignKey(
        Destinos,
        null=True,                  # Permite valores NULL en la base de datos
        blank=True,
        on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
     )
     municipio = models.CharField(max_length=50)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(Municipios, self).save(*args, **kwargs)

     def __str__(self):
         return self.municipio
#Hoteles
class LugaresHoteles(models.Model):
     Polo = models.ForeignKey(
        Destinos,
        null=True,                  # Permite valores NULL en la base de datos
        blank=True,
        on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
     )
     LugarHotel = models.CharField(max_length=20)
     Direccion = models.CharField(max_length=250)
     Telefono = models.CharField(max_length=20)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(LugaresHoteles, self).save(*args, **kwargs)

     def __str__(self):
         return self.LugarHotel
#Tipos de Habitaciones
class TiposHabitaciones(models.Model):
     THABITACION = models.CharField(max_length=10)
     TCANTC = models.IntegerField(blank=True, null=True, default=None)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(TiposHabitaciones, self).save(*args, **kwargs)

     def __str__(self):
         return self.THABITACION
#Regimenes
class Regimen(models.Model):
     TPLANALIM = models.CharField(max_length=3)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(Regimen, self).save(*args, **kwargs)

     def __str__(self):
         return self.TPLANALIM
#Casas con rentas de habitaciones
class RentRoom(models.Model):
     polocasa = models.ForeignKey(
        Destinos,
        null=True,                  # Permite valores NULL en la base de datos
        blank=True,
        on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
     )
     Direccioncasa = models.CharField(max_length=70)
     telefonocasa = models.CharField(max_length=10,blank=True, null=True)
     contactocasa = models.CharField(max_length=30, blank=True, null=True)
     descripcion = models.CharField(max_length=50, blank=True, null=True)
     municipcasa = models.ForeignKey(
        Municipios,
        null=True,                  # Permite valores NULL en la base de datos
        blank=True,
        on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
     )
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(RentRoom, self).save(*args, **kwargs)

     def __str__(self):
         return self.Direccioncasa
#Nacionalidades
class Nacionalidades(models.Model):
     descripcion = models.CharField(max_length=20)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(Nacionalidades, self).save(*args, **kwargs)

     def __str__(self):
         return self.descripcion
#Origenes de la reserva
class OrigReservas(models.Model):
     ONOMBRE = models.CharField(max_length=50)
     OCORREO = models.CharField(max_length=80, blank=True, null=True)
     Onreservai = models.CharField(max_length=2)
     onreservaf = models.CharField(max_length=2)
     ONINICIOCOD = models.IntegerField()
     temporada = models.CharField(max_length=50)
     codini = models.CharField(max_length=50)
     codfin = models.CharField(max_length=50)
     sweetin = models.BooleanField()
     automaticfilemaker = models.BooleanField()
     automaticexcel = models.BooleanField()
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(OrigReservas, self).save(*args, **kwargs)

     def __str__(self):
         return self.ONOMBRE

# class Regiones(models.Model):
#     NNREGION = models.CharField(max_length=2)
#     NDREGION = models.CharField(max_length=20)
#     slug = models.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = '%s' % (
#             uuid.uuid1()
#         )
#         super(Regiones, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.NDREGION
#
# class DestPesca(models.Model):
#     NDESTINO = models.CharField(max_length=2)
#     DESTINO = models.CharField(max_length=20)
#     REGION = models.CharField(max_length=2)
#     LANCHAS = models.IntegerField()
#     slug = models.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = '%s' % (
#             uuid.uuid1()
#         )
#         super(DestPesca, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.DESTINO
#
# class Agencias(models.Model):
#     NAGENCIAS = models.CharField(max_length=3)
#     AGENCIA = models.CharField(max_length=20)
#     slug = models.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = '%s' % (
#             uuid.uuid1()
#         )
#         super(Agencias, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.AGENCIA
#
# class DatGenerales(models.Model):
#     NRESERVA = models.CharField(max_length=10)
#     NIZQUIERDA = models.CharField(max_length=2)
#     NDERECHA = models.CharField(max_length=6)
#     RCSOLICITUD = models.IntegerField()
#     NDERECHA = models.CharField(max_length=6)
#     RORIGENDELARESERVA = models.CharField(max_length=2)
#     RCORIGENDELARESERVA = models.IntegerField()
#     RCARPETA = models.IntegerField()
#     RISERVICIO = models.DateField()
#     RFSERVICIO = models.DateField()
#     RCUBATUR = models.CharField(max_length=10)
#     RHOTEL = models.CharField(max_length=4)
#     RNOMBRE = models.CharField(max_length=50)
#     RAGENCIA = models.CharField(max_length=3)
#     ROPERADOR = models.CharField(max_length=3)
#     RCANTPAX = models.IntegerField()
#     RCANTPAXPREV = models.IntegerField()
#     RESTADODELARESERVA = models.CharField(max_length=1)
#     RCOMENTARIO = models.CharField(max_length=100)
#     RRECOGIDA = models.CharField(max_length=20)
#     RALOJAMIENTO = models.CharField(max_length=2)
#     RTIPODEPESCA = models.CharField(max_length=1)
#     RIN = models.DateField()
#     ROUT = models.DateField()
#     RDESTINO = models.CharField(max_length=2)
#     RCPAXDESTINO = models.IntegerField()
#     RCPAXDESTINOPREV = models.IntegerField()
#     RFSOLICITUD = models.DateField()
#     REXCLUSIVA = models.BooleanField()
#     rinicial = models.IntegerField()
#     RULTIMOCLIEN = models.IntegerField()
#     dias = models.IntegerField()
#     bloqueada = models.BooleanField()
#     RCDADOXOPERADOR = models.CharField(max_length=50)
#     temporada = models.CharField(max_length=11)
#     solicitante = models.CharField(max_length=2)
#     modreserva = models.IntegerField()
#     modaloj = models.IntegerField()
#     modtransf = models.IntegerField()
#     modclient = models.IntegerField()
#     modocausas = models.IntegerField()
#     rcerrada = models.BooleanField()
#     rPROTEGIDA = models.BooleanField()
#     slug = models.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = '%s' % (
#             uuid.uuid1()
#         )
#         super(DatGenerales, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.RNOMBRE

