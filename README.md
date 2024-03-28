# BioRegionalAPIs

A new era of Regenerative Software solutions are being built. We have the chance to re-frame how we organize ourselves and how we think about our place in this world. These APIs are built to enable the organization of people, organizations, solutions, villages, networks, etc -- into their respective BioRegions, EcoRegions, Biomes, and Nature Conservation Status.

Imagine a user-signup form where you use either their device location data, a provided address, or provided latitude/longitude coordinates to attach tag, category, or group assignments based on BioRegional data.

We can group Regenerative solutions to anything from housing to growing plants -- by the EcoRegion, BioRegion, or Biomes in which they are effective.

We can group Natural Building, Permaculture, Indigenous Wisdom, or any sort of workshop leader or educator by the EcoRegions or Biomes they know how to serve.

The possibilities are many, and I invite you to consider how your Regenerative Software project can help raise BioRegional awareness.

For more details, check out the project's [documentation](http://BioHarmony-Foundation.github.io/BioRegionAPIs/).


# Development

## Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)

## Stack

* Docker
* Postgres (+GIS)
* Python
* Django
* Django Rest Framework

## Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Load up the data:

```bash
docker-compose run --rm web "python manage.py load_data"
```


# Acknowledgements

[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

This API is loaded up with data from the [RESOLVE EcoRegions 2017 Dataset](https://developers.google.com/earth-engine/datasets/catalog/RESOLVE_ECOREGIONS_2017) from [Resolve](https://www.resolve.ngo/).

The EcoRegion data is supplemented with BioRegion data from the [One Earth Navigator](https://www.oneearth.org/navigator/) from [OneEarth](https://www.oneearth.org/).
