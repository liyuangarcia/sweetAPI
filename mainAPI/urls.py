# users/urls.py
from django.urls import path, include
from . import views
from .views import AeropuertosViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('airports', AeropuertosViewSet)
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    #path('airports/',AeropuertosViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update','delete': 'destroy'}))
]
