from django.db import models
import uuid

Week = (
    (1, 'Domingo'),
    (2, 'Lunes'),
    (3, 'Martes'),
    (4, 'Miercoles'),
    (5, 'Jueves'),
    (6, 'Viernes'),
    (7, 'Sábado'),
)

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
     temporada = models.CharField(max_length=50, blank=True, null=True)
     codini = models.CharField(max_length=50, blank=True, null=True)
     codfin = models.CharField(max_length=50, blank=True, null=True)
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
#Medios de transfer
class TiposCarros(models.Model):
     desctipocarro = models.CharField(max_length=20)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(TiposCarros, self).save(*args, **kwargs)

     def __str__(self):
         return self.desctipocarro
#Medios de transfer
class VuelosDomesticos(models.Model):
      vdnvuelo = models.CharField(max_length=50)
      vdfvueloi = models.DateField()
      vdfvuelor = models.DateField(null=True, blank=True)
      vddiasemana = models.CharField(max_length=2, choices=Week,null=True, blank=True)
      vdpolo = models.ForeignKey(
         Destinos,
         null=True,                  # Permite valores NULL en la base de datos
         blank=True,
         related_name='vuelos_polo',
         on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
      )
      vddestino = models.ForeignKey(
         Aeropuertos,
         null=True,                  # Permite valores NULL en la base de datos
         blank=True,
         related_name='vuelos_destino',
         on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
      )
      vdterminal = models.ForeignKey(
         Aeropuertos,
         null=True,                  # Permite valores NULL en la base de datos
         blank=True,
         related_name='vuelos_terminal',
         on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
      )
      vdlugardesalida = models.ForeignKey(
         Destinos,
         null=True,                  # Permite valores NULL en la base de datos
         blank=True,
         related_name='vuelos_lugar_salida',
         on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
      )
      vdhsalida =  models.TimeField()
      vdhllegada =  models.TimeField()
      vdcapacasignadai = models.IntegerField(blank=True, null=True, default=0)
      vdpnrasignadoi = models.CharField(max_length=10,null=True, blank=True)
      vdcapacasignadar = models.IntegerField()
      vdpnrasignador = models.CharField(max_length=10,null=True, blank=True)
      slug = models.SlugField(unique=True)

      def save(self, *args, **kwargs):
          self.slug = '%s' % (
              uuid.uuid1()
          )
          super(VuelosDomesticos, self).save(*args, **kwargs)

      def __str__(self):
          return self.vdnvuelo
#Operadores
class Operadores(models.Model):
     OPERADOR = models.CharField(max_length=20)
     IOPERADOR = models.CharField(max_length=20,null=True, blank=True)
     ioperador2 = models.CharField(max_length=20,null=True, blank=True)
     OSEGUIMIENTO = models.BooleanField()
     ocodigo = models.BooleanField()
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(Operadores, self).save(*args, **kwargs)

     def __str__(self):
         return self.OPERADOR
#Agencias
class Agencias(models.Model):
     AGENCIA = models.CharField(max_length=20)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(Agencias, self).save(*args, **kwargs)

     def __str__(self):
         return self.AGENCIA

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

class DatGenerales(models.Model):
     NRESERVA = models.CharField(max_length=10, null=True, blank=True)
     NIZQUIERDA = models.CharField(max_length=2, null=True, blank=True)
     NDERECHA = models.CharField(max_length=6, null=True, blank=True)
     RCSOLICITUD = models.IntegerField(null=True, blank=True)
     NDERECHA = models.CharField(max_length=6, null=True, blank=True)
     RORIGENDELARESERVA = models.ForeignKey(
         OrigReservas,
         null=True,                  # Permite valores NULL en la base de datos
         blank=True,
         related_name='orige_reserva',
         on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
      )
     RCORIGENDELARESERVA = models.IntegerField(null=True, blank=True)
     RCARPETA = models.IntegerField(null=True, blank=True)
     RISERVICIO = models.DateField(null=True, blank=True)
     RFSERVICIO = models.DateField(null=True, blank=True)
     RCUBATUR = models.CharField(max_length=10, null=True, blank=True)
     RHOTEL = models.CharField(max_length=4, null=True, blank=True)
     RNOMBRE = models.CharField(max_length=50)
     RAGENCIA = models.ForeignKey(
         Agencias,
         null=True,                  # Permite valores NULL en la base de datos
         blank=True,
         related_name='agencias_reserva',
         on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
      )
     ROPERADOR = models.ForeignKey(
         Operadores,
         null=True,                  # Permite valores NULL en la base de datos
         blank=True,
         related_name='operador_reserva',
         on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
      )
     RCANTPAX = models.IntegerField(null=True, blank=True)
     RCANTPAXPREV = models.IntegerField()
     RESTADODELARESERVA = models.CharField(max_length=1, null=True, blank=True)
     RCOMENTARIO = models.CharField(max_length=100, null=True, blank=True)
     RRECOGIDA = models.CharField(max_length=20, null=True, blank=True)
     RALOJAMIENTO = models.CharField(max_length=2, null=True, blank=True)
     RTIPODEPESCA = models.CharField(max_length=1, null=True, blank=True)
     RIN = models.DateField(null=True, blank=True)
     ROUT = models.DateField(null=True, blank=True)
     RDESTINO = models.ForeignKey(
         DestPesca,
         null=True,                  # Permite valores NULL en la base de datos
         blank=True,
         related_name='destino_reserva',
         on_delete=models.PROTECT,  # Previene eliminar categor�as usadas
      )
     RCPAXDESTINO = models.IntegerField(null=True, blank=True)
     RCPAXDESTINOPREV = models.IntegerField(null=True, blank=True)
     RFSOLICITUD = models.DateField(null=True, blank=True)
     REXCLUSIVA = models.BooleanField()
     rinicial = models.IntegerField(null=True, blank=True)
     RULTIMOCLIEN = models.IntegerField(null=True, blank=True)
     dias = models.IntegerField(null=True, blank=True)
     bloqueada = models.BooleanField()
     RCDADOXOPERADOR = models.CharField(max_length=50, null=True, blank=True)
     temporada = models.CharField(max_length=11, null=True, blank=True)
     solicitante = models.CharField(max_length=2, null=True, blank=True)
     modreserva = models.IntegerField(null=True, blank=True)
     modaloj = models.IntegerField(null=True, blank=True)
     modtransf = models.IntegerField(null=True, blank=True)
     modclient = models.IntegerField(null=True, blank=True)
     modocausas = models.IntegerField(null=True, blank=True)
     rcerrada = models.BooleanField()
     rPROTEGIDA = models.BooleanField()
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(DatGenerales, self).save(*args, **kwargs)

     def __str__(self):
         return self.RNOMBRE

