# users/views.py
from rest_framework import status, generics, viewsets, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer, AeropuertosSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Aeropuertos

#@permission_classes([IsAuthenticated])
class AeropuertosViewSet(viewsets.ModelViewSet):
    queryset = Aeropuertos.objects.all().order_by('aaerodescripcion')
    serializer_class = AeropuertosSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['aaerodescripcion', 'alugar', 'asiglas']
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