import os 

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry, Polygon, MultiPolygon

import geopandas as gpd
import pandas as pd

from bioregions.ecodata.models import Realm, SubRealm, Biome, BioRegion, ConservationStatus, EcoRegion

dir_path = os.path.dirname(os.path.realpath(__file__))


class Command(BaseCommand):
    help = "Loads EcoRegions2017 and BioRegion data into the database"

    def handle(self, *args, **options):

        bio_regions = pd.read_csv(f'{dir_path}/../../../data/bioregions.csv', delimiter='|')
        bio_regions['geometry'] = gpd.GeoSeries.from_wkt(bio_regions['BIO_REGION_WKT'])

        bio_region_map = {}

        for index, row in bio_regions.iterrows():
            realm, realm_created = Realm.objects.get_or_create(name=row['REALM'])
            sub_realm, sub_realm_created = SubRealm.objects.get_or_create(name=row['SUB_REALM'], realm=realm)
            bio_region, bio_region_created = BioRegion.objects.get_or_create(
                name=row['BIO_REGION'],
                sub_realm=sub_realm,
                defaults={
                    "geometry": GEOSGeometry(str(row['geometry']))
                }
            )
            bio_region_map[row['BIO_REGION_ID']] = bio_region

        eco_regions = pd.read_csv(f'{dir_path}/../../../data/ecoregions.csv', delimiter='|')
        eco_regions_2017 = gpd.read_file(f'{dir_path}/../../../data/Ecoregions2017.shp')

        merged_eco_regions = eco_regions_2017.merge(eco_regions, left_on='ECO_ID', right_on='ECO_REGION_ID')
        multiple_bio_regions = merged_eco_regions[merged_eco_regions.duplicated(subset=['ECO_ID'])]

        for index, row in merged_eco_regions.iterrows():
            biome, biome_created = Biome.objects.get_or_create(name=row['BIOME_NAME'], color=row['COLOR_BIO'])
            conservation_status, conservation_status_created = ConservationStatus.objects.get_or_create(name=row['NNH_NAME'], code=row['NNH'], color=row['COLOR_NNH'])

            geometry = GEOSGeometry(str(row['geometry']))
            
            bio_region = bio_region_map[row['BIO_REGION_ID']]

            in_multiple_bio_regions = multiple_bio_regions[multiple_bio_regions['ECO_ID'] == row['ECO_ID']]

            if not in_multiple_bio_regions.empty:
                print('Splitting EcoRegion into BioRegional Parts: ' + row['ECO_REGION'])
                try:
                    # Some EcoRegions span multiple BioRegions
                    # This is attempting to create multiple EcoRegions where each has
                    # a subset of the total EcoRegion's geometry based on the containing BioRegion
                    resulting_geometry = geometry.intersection(bio_region.geometry)
                except Exception:
                    print('Could not intersect geometry for: ' + row['ECO_REGION'])
                    resulting_geometry = geometry
            else:
                resulting_geometry = geometry

            if isinstance(resulting_geometry, Polygon):
                resulting_geometry = MultiPolygon(resulting_geometry)

            eco_region, eco_region_createad = EcoRegion.objects.get_or_create(
                name=row['ECO_REGION'],
                bio_region=bio_region,
                defaults={
                    "geometry": resulting_geometry,
                    "area": row['SHAPE_AREA'],
                    "color": row['COLOR'],
                    "description": row['ECO_REGION_DESCRIPTION'],
                    "biome": biome,
                    "conservation_status": conservation_status,
                }
            )
            
            if eco_region_createad:
                print('Created EcoRegion: ' + row['ECO_REGION'])