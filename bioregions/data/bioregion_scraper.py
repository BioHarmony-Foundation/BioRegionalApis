import csv
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

from bs4 import BeautifulSoup
from requests import get
from shapely import MultiPolygon

root_url = "https://www.oneearth.org"

realms_json = get(f'{root_url}/api/realms.json').json()


with open(f'{dir_path}/bioregions.csv', 'w', newline='') as bioregion_csv_file:
    bio_region_writer = csv.writer(bioregion_csv_file, delimiter='|')

    bio_region_writer.writerow(['REALM', 'SUB_REALM', 'BIO_REGION', 'BIO_REGION_ID', 'BIO_REGION_WKT'])

    for realm in realms_json['items']:
        realm_title = realm['title']
        print('Realm: ' + realm_title)

        for sub_realm in realm['subrealms']:
            sub_realm_title = sub_realm['title']
            print('SubRealm: ' + sub_realm_title)

            for bioregion in sub_realm['bioregionSet']['items']:
                bioregion_title = bioregion['title'].rsplit(maxsplit=1)[0]
                bioregion_id = bioregion['regionId']
                print('BioRegion: ' + bioregion_title)

                bioregion_geometry_response = get(f'{root_url}/geoData/bioregions/{bioregion_id}.kml')
                bioregion_geometry_soup = BeautifulSoup(bioregion_geometry_response.content)
                coordinates = bioregion_geometry_soup.find_all('coordinates')[0]
                coord_pairs = coordinates.string.split()
                coord_pair_tuples = [tuple(pair.split(',')) for pair in coord_pairs]
                coord_pair_float_tuples = [(float(pair[0]), float(pair[1]),) for pair in coord_pair_tuples]
                bioregion_polygon = MultiPolygon([[coord_pair_float_tuples]])

                bio_region_writer.writerow([
                    realm_title,
                    sub_realm_title,
                    bioregion_title,
                    bioregion_id,
                    bioregion_polygon.wkt
                ])


with open(f'{dir_path}/bioregions.csv', 'r', newline='') as bioregion_csv_file:

    bioregion_reader = csv.DictReader(bioregion_csv_file, delimiter='|')

    with open(f'{dir_path}/ecoregions.csv', 'w', newline='') as eco_regions_csvfile:

        eco_region_writer = csv.writer(eco_regions_csvfile, delimiter='|')

        eco_region_writer.writerow(['BIO_REGION_ID', 'ECO_REGION', 'ECO_REGION_DESCRIPTION', 'ECO_REGION_ID'])

        for bioregion in bioregion_reader:

            bioregion_id = bioregion['BIO_REGION_ID']

            ecoregion_json = get(f'{root_url}/api/bioregion/{bioregion_id.lower()}/data.json').json()

            for ecoregion in ecoregion_json['ecoregionSet']['items']:
                ecoregion_title = ecoregion['title'].strip()
                ecoregion_id = ecoregion['regionId']
                ecoregion_description = ecoregion['dek']
                print('EcoRegion: ' + ecoregion_title)

                eco_region_writer.writerow([
                    bioregion_id,
                    ecoregion_title,
                    ecoregion_description,
                    ecoregion_id
                ])

