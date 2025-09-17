# users/urls.py
from django.urls import path, include
from . import views
from .views import AeropuertosViewSet,GuiasPescasViewSet,DestPescaViewSet, TipoPescaViewSet, \
    RegionesPescaViewSet, DestinosViewSet, MarinasViewSet, LanchasRegionViewSet,LugaresHotelesViewSet, \
    TiposHabitacionesViewSet, RegimenViewSet, MunicipiosViewSet,RentRoomViewSet, NacionalidadesViewSet, \
    OrigReservasViewSet, TiposCarrosViewSet, VuelosDomesticosViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('airports', AeropuertosViewSet)
router.register('guiaspesca', GuiasPescasViewSet)
router.register('destpesca', DestPescaViewSet)
router.register('tipopesca', TipoPescaViewSet)
router.register('regionespesca', RegionesPescaViewSet)
router.register('destinos', DestinosViewSet)
router.register('marinas', MarinasViewSet)
router.register('lanchasregion', LanchasRegionViewSet)
router.register('lugareshoteles', LugaresHotelesViewSet)
router.register('tiposhabitaciones', TiposHabitacionesViewSet)
router.register('regimenes', RegimenViewSet)
router.register('municipios', MunicipiosViewSet)
router.register('rentroom', RentRoomViewSet)
router.register('nacionalidades', NacionalidadesViewSet)
router.register('origenreservas', OrigReservasViewSet)
router.register('tiposcarros', TiposCarrosViewSet)
router.register('vuelosdomesticos', VuelosDomesticosViewSet)

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
