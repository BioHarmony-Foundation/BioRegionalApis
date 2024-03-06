from django.conf import settings
from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .ecodata.views import BiomeViewSet, BioRegionViewSet, EcoRegionViewSet, RealmViewSet, SubRealmViewSet, get_ecoregion_from_coordinates

router = DefaultRouter()
router.register(r'biomes', BiomeViewSet)
router.register(r'bioregions', BioRegionViewSet)
router.register(r'ecoregions', EcoRegionViewSet)
router.register(r'realms', RealmViewSet)
router.register(r'subrealms', SubRealmViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/ecoregion_from_coordinates/<str:latitude>/<str:longitude>/', get_ecoregion_from_coordinates),
    path('api-token-auth/', views.obtain_auth_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # the 'api-root' from django rest-frameworks default router
    # http://www.django-rest-framework.org/api-guide/routers/#defaultrouter
    re_path(r'^$', RedirectView.as_view(url=reverse_lazy('api-root'), permanent=False)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
