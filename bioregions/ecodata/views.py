from django.contrib.gis.geos import Point

from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from .models import Biome, BioRegion, EcoRegion, Realm, SubRealm
from .serializers import (BiomeSerializer, BioRegionSerializer, EcoRegionSerializer, 
                            EcoRegionDetailSerializer, RealmSerializer, SubRealmSerializer)


class BiomeViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Biome.objects.all()
    serializer_class = BiomeSerializer


class BioRegionViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = BioRegion.objects.all()
    serializer_class = BioRegionSerializer


class EcoRegionViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = EcoRegion.objects.all()
    serializer_class = EcoRegionSerializer


class RealmViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Realm.objects.all()
    serializer_class = RealmSerializer


class SubRealmViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = SubRealm.objects.all()
    serializer_class = SubRealmSerializer


@api_view(['GET'])
def get_ecoregion_from_coordinates(request, latitude, longitude):
    lat = float(latitude)
    lng = float(longitude)
    point = Point(lat, lng)
    eco_regions = EcoRegion.objects.filter(geometry__intersects=point)

    if not eco_regions:
        return Response(None, HTTP_404_NOT_FOUND)

    return Response(EcoRegionDetailSerializer(eco_regions[0]).data)

