from django.db import models
from django.contrib.gis.db.models import MultiPolygonField

from bioregions.config.models import NamedModel


class Realm(NamedModel):
    pass


class SubRealm(NamedModel):
    realm = models.ForeignKey(Realm, on_delete=models.DO_NOTHING, related_name="subrealms")


class BioRegion(NamedModel):
    sub_realm = models.ForeignKey(SubRealm, on_delete=models.DO_NOTHING, related_name="bioregions")
    geometry = MultiPolygonField(geography=True)


class Biome(NamedModel):
    color = models.CharField(max_length=7)


class ConservationStatus(NamedModel):
    code = models.SmallIntegerField()
    color = models.CharField(max_length=7)


class EcoRegion(models.Model):
    name = models.CharField(max_length=255)
    area = models.DecimalField(decimal_places=6, max_digits=10)
    geometry = MultiPolygonField(geography=True)
    color = models.CharField(max_length=7)
    description = models.TextField()
    bio_region = models.ForeignKey(BioRegion, on_delete=models.DO_NOTHING, related_name="ecoregions")
    biome = models.ForeignKey(Biome, on_delete=models.DO_NOTHING, related_name="ecoregions")
    conservation_status = models.ForeignKey(ConservationStatus, on_delete=models.DO_NOTHING, related_name="ecoregions")

    def __str__(self):
        return self.name