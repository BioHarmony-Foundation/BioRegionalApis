from django.contrib.gis import admin as gis_admin
from django.contrib import admin

from .models import BioRegion, EcoRegion, Biome, ConservationStatus, Realm, SubRealm


@admin.register(EcoRegion)
class EcoRegionAdmin(gis_admin.OSMGeoAdmin):
    list_display = ['name', 'bio_region']


@admin.register(BioRegion)
class BioRegionAdmin(gis_admin.OSMGeoAdmin):
    list_display = ['name', 'sub_realm']


admin.site.register(Biome)
admin.site.register(ConservationStatus)
admin.site.register(Realm)
admin.site.register(SubRealm)

