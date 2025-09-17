# users/serializers.py
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Aeropuertos, GuiasPescas, DestPesca, TipoPesca, RegionesPesca, \
    Destinos, Marinas, LanchasRegion, LugaresHoteles, TiposHabitaciones, Regimen, \
    Municipios, RentRoom, Nacionalidades, OrigReservas, TiposCarros, VuelosDomesticos

class AeropuertosSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Aeropuertos
        fields = ('id','aaerodescripcion','alugar','asiglas','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class GuiasPescasSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = GuiasPescas
        fields = ('id','GNOMBREDELGUIA','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class DestPescaSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    regionestext = serializers.ReadOnlyField(source='REGIONES.REGIONES')
    LANCHAS = serializers.CharField(
            required=False, allow_null=True, allow_blank=True)
    def validate_LANCHAS(self, value):
        if not value:
            return 0
        try:
            return int(value)
        except ValueError:
            raise serializers.ValidationError('You must supply an integer')

    class Meta:
        model = DestPesca
        fields = ('id','DESTINO','REGIONES','LANCHAS','regionestext','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}, 'LANCHAS': {'required': False, 'allow_null': True}}
class TipoPescaSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = TipoPesca
        fields = ('id','MPESCA','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class RegionesPescaSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = RegionesPesca
        fields = ('id','REGIONES','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class DestinosSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Destinos
        fields = ('id','DESTINO','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class MarinasSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Marinas
        fields = ('id','Lmarina','Nmarina','NoficialMarina','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class LanchasRegionSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    regionestext = serializers.ReadOnlyField(source='REGIONES.REGIONES')

    class Meta:
        model = LanchasRegion
        fields = ('id','REGIONES','SumaDeLANCHAS','slug','regionestext')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class LugaresHotelesSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    polotext = serializers.ReadOnlyField(source='Polo.DESTINO')

    class Meta:
        model = LugaresHoteles
        fields = ('id','Polo','LugarHotel','Direccion','Telefono','slug','polotext')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class TiposHabitacionesSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = TiposHabitaciones
        fields = ('id','THABITACION','TCANTC','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}, 'TCANTC': {'required': False, 'allow_null': True}}
class RegimenSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Regimen
        fields = ('id','TPLANALIM','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class MunicipiosSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    polotext = serializers.ReadOnlyField(source='polo.DESTINO')

    class Meta:
        model = Municipios
        fields = ('id','municipio','polo','polotext','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class RentRoomSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    polotext = serializers.ReadOnlyField(source='polocasa.DESTINO')
    municipiotext = serializers.ReadOnlyField(source='municipcasa.municipio')
    class Meta:
        model = RentRoom
        fields = ('id','polocasa','polotext','municipiotext','Direccioncasa','telefonocasa','contactocasa','descripcion','municipcasa','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}, 'telefonocasa': {'required': False, 'allow_null': True}, 'contactocasa': {'required': False, 'allow_null': True}, 'descripcion': {'required': False, 'allow_null': True}}
class NacionalidadesSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Nacionalidades
        fields = ('id','descripcion','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class OrigReservasSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = OrigReservas
        fields = ('id','ONOMBRE','OCORREO','Onreservai','onreservaf','ONINICIOCOD','temporada','codini','codfin','sweetin','automaticfilemaker','automaticexcel','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}, 'OCORREO': {'required': False, 'allow_null': True}, 'temporada': {'required': False, 'allow_null': True},
                        'codini': {'required': False, 'allow_null': True}, 'codfin': {'required': False, 'allow_null': True}}
class TiposCarrosSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = TiposCarros
        fields = ('id','desctipocarro','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
class VuelosDomesticosSerializer(serializers.ModelSerializer):
    vdpolotext = serializers.ReadOnlyField(source='vdpolo.DESTINO')
    vddestinotext = serializers.ReadOnlyField(source='vddestino.aaerodescripcion')
    vdterminaltext = serializers.ReadOnlyField(source='vdterminal.aaerodescripcion')
    vdlugardesalidatext = serializers.ReadOnlyField(source='vdlugardesalida.DESTINO')
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = VuelosDomesticos
        fields = ('id','vdnvuelo','vdfvueloi','vdfvuelor','vddiasemana','vdpolo',
                  'vdpolotext','vddestino','vddestinotext','vdterminal',
                  'vdterminaltext','vdlugardesalida','vdlugardesalidatext',
                  'vdhsalida','vdhllegada','vdcapacasignadai', 'vdpnrasignadoi',
                  'vdcapacasignadar','vdpnrasignador','slug')
        extra_kwargs = {'url': {'lookup_field': 'slug'}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            
            if not user:
                raise serializers.ValidationError('Credenciales inválidas')
            
            if not user.is_active:
                raise serializers.ValidationError('Usuario inactivo')
            
            refresh = RefreshToken.for_user(user)
            
            data['user'] = user
            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)
            
        return data
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user

