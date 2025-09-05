# users/urls.py
from django.urls import path, include
from . import views
from .views import AeropuertosViewSet,GuiasPescasViewSet,DestPescaViewSet, TipoPescaViewSet, RegionesPescaViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('airports', AeropuertosViewSet)
router.register('guiaspesca', GuiasPescasViewSet)
router.register('destpesca', DestPescaViewSet)
router.register('tipopesca', TipoPescaViewSet)
router.register('regionespesca', RegionesPescaViewSet)

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
