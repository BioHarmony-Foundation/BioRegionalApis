from rest_framework import serializers
from .models import Realm, SubRealm, Biome, BioRegion, ConservationStatus, EcoRegion


class RealmSerializer(serializers.ModelSerializer):

    class Meta:
        model = Realm
        fields = ('id', 'name',)


class SubRealmSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubRealm
        fields = ('id', 'name', 'realm',)


class SubRealmDetailSerializer(serializers.ModelSerializer):
    
    realm = RealmSerializer()

    class Meta:
        model = SubRealm
        fields = ('id', 'name', 'realm',)


class BioRegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BioRegion
        fields = ('id', 'name', 'sub_realm',)


class BioRegionDetailSerializer(serializers.ModelSerializer):

    sub_realm = SubRealmDetailSerializer()

    class Meta:
        model = BioRegion
        fields = ('id', 'name', 'sub_realm',)


class BiomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Biome
        fields = ('id', 'name', 'color',)


class ConservationStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = ConservationStatus
        fields = ('id', 'name', 'code', 'color',)


class EcoRegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = EcoRegion
        fields = ('id', 'name', 'area', 'color', 'description', 'biome', 'bio_region', 'conservation_status',)


class EcoRegionDetailSerializer(serializers.ModelSerializer):

    biome = BiomeSerializer()
    bio_region = BioRegionDetailSerializer()
    conservation_status = ConservationStatusSerializer()

    class Meta:
        model = EcoRegion
        fields = ('id', 'name', 'area', 'color', 'description', 'biome', 'bio_region', 'conservation_status',)