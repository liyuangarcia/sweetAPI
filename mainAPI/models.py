from django.db import models
import uuid


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
     GNGUIA = models.CharField(max_length=2)
     GNOMBREDELGUIA = models.CharField(max_length=20)

     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(GuiasPescas, self).save(*args, **kwargs)

     def __str__(self):
         return self.GNOMBREDELGUIA

#Asignacion de lanchas a los polos de pescas
class DestPesca(models.Model):
     NDESTINO = models.CharField(max_length=2)
     DESTINO = models.CharField(max_length=20)
     REGION = models.CharField(max_length=2)
     LANCHAS = models.IntegerField()

     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(DestPesca, self).save(*args, **kwargs)

     def __str__(self):
         return self.DESTINO

#POSIBLES ACTIVIDADES EN EL POLO
class TipoPesca(models.Model):
     MTIPODEPESCA = models.CharField(max_length=1)
     MPESCA = models.CharField(max_length=1)
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(TipoPesca, self).save(*args, **kwargs)

     def __str__(self):
         return self.MPESCA

#Lanchas por Region
class LanchasRegion(models.Model):
     REGION = models.CharField(max_length=2)
     SumaDeLANCHAS = models.IntegerField()
     slug = models.SlugField(unique=True)

     def save(self, *args, **kwargs):
         self.slug = '%s' % (
             uuid.uuid1()
         )
         super(LanchasRegion, self).save(*args, **kwargs)

     def __str__(self):
         return self.REGION

# class OrigReservas(models.Model):
#     ONO = models.CharField(max_length=2)
#     ONOMBRE = models.CharField(max_length=50)
#     OCORREO = models.CharField(max_length=80)
#     Onreservai = models.CharField(max_length=2)
#     onreservaf = models.CharField(max_length=2)
#     ONINICIOCOD = models.IntegerField()
#     temporada = models.CharField(max_length=50)
#     codini = models.CharField(max_length=50)
#     codfin = models.CharField(max_length=50)
#     sweetin = models.BooleanField()
#     automaticfilemaker = models.BooleanField()
#     automaticexcel = models.BooleanField()
#     slug = models.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = '%s' % (
#             uuid.uuid1()
#         )
#         super(OrigReservas, self).save(*args, **kwargs)
#
#     def __str__(self):
#         return self.ONOMBRE
#
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

