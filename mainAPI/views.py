# users/views.py
from rest_framework import status, generics, viewsets, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer, \
    AeropuertosSerializer, GuiasPescasSerializer, DestPescaSerializer, TipoPescaSerializer,\
    RegionesPescaSerializer, DestinosSerializer, MarinasSerializer, LanchasRegionSerializer,\
    LugaresHotelesSerializer, TiposHabitacionesSerializer, RegimenSerializer, MunicipiosSerializer, \
    RentRoomSerializer, NacionalidadesSerializer, OrigReservasSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Aeropuertos,GuiasPescas, DestPesca,TipoPesca, RegionesPesca, \
    Destinos, Marinas, LanchasRegion, LugaresHoteles, TiposHabitaciones, Regimen, \
    Municipios, RentRoom, Nacionalidades, OrigReservas

#@permission_classes([IsAuthenticated])
class AeropuertosViewSet(viewsets.ModelViewSet):
    queryset = Aeropuertos.objects.all().order_by('aaerodescripcion')
    serializer_class = AeropuertosSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['aaerodescripcion', 'alugar', 'asiglas']
    lookup_field = 'slug'
#@permission_classes([IsAuthenticated])
class GuiasPescasViewSet(viewsets.ModelViewSet):
    queryset = GuiasPescas.objects.all().order_by('GNOMBREDELGUIA')
    serializer_class = GuiasPescasSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['GNOMBREDELGUIA']
    lookup_field = 'slug'
#@permission_classes([IsAuthenticated])
class DestPescaViewSet(viewsets.ModelViewSet):
    queryset = DestPesca.objects.all().order_by('DESTINO')
    serializer_class = DestPescaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['DESTINO','LANCHAS', 'REGIONES__REGIONES']
    lookup_field = 'slug'
#@permission_classes([IsAuthenticated])
class TipoPescaViewSet(viewsets.ModelViewSet):
    queryset = TipoPesca.objects.all().order_by('MPESCA')
    serializer_class = TipoPescaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['MPESCA']
    lookup_field = 'slug'
#@permission_classes([IsAuthenticated])
class RegionesPescaViewSet(viewsets.ModelViewSet):
    queryset = RegionesPesca.objects.all().order_by('REGIONES')
    serializer_class = RegionesPescaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['REGIONES']
    lookup_field = 'slug'
class DestinosViewSet(viewsets.ModelViewSet):
    queryset = Destinos.objects.all().order_by('DESTINO')
    serializer_class = DestinosSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['DESTINO']
    lookup_field = 'slug'
class MarinasViewSet(viewsets.ModelViewSet):
    queryset = Marinas.objects.all().order_by('Nmarina')
    serializer_class = MarinasSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Lmarina','Nmarina','NoficialMarina']
    lookup_field = 'slug'
class LanchasRegionViewSet(viewsets.ModelViewSet):
    queryset = LanchasRegion.objects.all().order_by('REGIONES__REGIONES')
    serializer_class = LanchasRegionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['REGIONES__REGIONES']
    lookup_field = 'slug'
class LugaresHotelesViewSet(viewsets.ModelViewSet):
    queryset = LugaresHoteles.objects.all().order_by('LugarHotel')
    serializer_class = LugaresHotelesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['Polo__DESTINO','LugarHotel','Direccion','Telefono']
    lookup_field = 'slug'
class TiposHabitacionesViewSet(viewsets.ModelViewSet):
    queryset = TiposHabitaciones.objects.all().order_by('THABITACION')
    serializer_class = TiposHabitacionesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['THABITACION','TCANTC']
    lookup_field = 'slug'
class RegimenViewSet(viewsets.ModelViewSet):
    queryset = Regimen.objects.all().order_by('TPLANALIM')
    serializer_class = RegimenSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['TPLANALIM']
    lookup_field = 'slug'
class MunicipiosViewSet(viewsets.ModelViewSet):
    queryset = Municipios.objects.all().order_by('municipio')
    serializer_class = MunicipiosSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['municipio','polo__DESTINO']
    lookup_field = 'slug'
class RentRoomViewSet(viewsets.ModelViewSet):
    queryset = RentRoom.objects.all().order_by('Direccioncasa')
    serializer_class = RentRoomSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['polocasa__DESTINO','Direccioncasa','telefonocasa','contactocasa','descripcion','municipcasa__municipio']
    lookup_field = 'slug'
class NacionalidadesViewSet(viewsets.ModelViewSet):
    queryset = Nacionalidades.objects.all().order_by('descripcion')
    serializer_class = NacionalidadesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['descripcion']
    lookup_field = 'slug'
class OrigReservasViewSet(viewsets.ModelViewSet):
    queryset = OrigReservas.objects.all().order_by('ONOMBRE')
    serializer_class = OrigReservasSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['ONOMBRE','OCORREO','Onreservai','onreservaf','temporada','codini','codfin']
    lookup_field = 'slug'

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.validated_data['user']
        user_data = UserSerializer(user).data
        
        return Response({
            'user': user_data,
            'refresh': serializer.validated_data['refresh'],
            'access': serializer.validated_data['access']
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        user_data = UserSerializer(user).data
        
        return Response({
            'user': user_data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    # Con SimpleJWT, el logout es del lado del cliente
    return Response({"message": "Logout exitoso"}, status=status.HTTP_200_OK)