# Using Coordinates to get BioRegional Data


### Request

`GET` `/api/v1/ecoregion_from_coordinates/[latitude]/[longitude]/`


### Response

```json
{
    "id": int,  # EcoRegion ID
    "name": str,
    "area": decimal,  # EcoRegion Area in square degrees
    "color": str,  # EcoRegion Hexidecimal Color
    "description": str,
    "biome": {
        "id": int,  # Biome ID
        "name": str,
        "color": str  # Biome Hexidecimal Color
    },
    "bio_region": {
        "id": int,  # BioRegion ID
        "name": str,
        "sub_realm": {
            "id": int,  # SubRealm ID
            "name": str,
            "realm": {
                "id": int,  # Realm ID
                "name": str
            }
        }
    },
    "conservation_status": {
        "id": int,  # Conservation Status ID
        "name": str,  # Half Protected, Nature Could Reach Half, Nature Could Recover, or Nature Imperiled
        "code": int,  # 1-4 
        "color": str  # Conservation Status Hexidecimal Color
    }
}
```

Example:

GET `/api/v1/ecoregion_from_coordinates/-122.464444/37.786389/`

```json
{
    "id": 92,
    "name": "California Interior Chaparral and Woodlands",
    "area": 7.330978,
    "color": "#FFA77F",
    "description": "This ecoregion wraps around California’s Central Valley, extending from Shasta Lake in the north to the vicinity of Wheeler Ridge in the south.",
    "biome": {
        "id": 3,
        "name": "Mediterranean Forests, Woodlands & Scrub",
        "color": "#FE0000"
    },
    "bio_region": {
        "id": 103,
        "name": "Greater California",
        "sub_realm": {
            "id": 28,
            "name": "North Pacific Coast",
            "realm": {
                "id": 8,
                "name": "Northern America"
            }
        }
    },
    "conservation_status": {
        "id": 4,
        "name": "Nature Could Recover",
        "code": 3,
        "color": "#F9A91B"
    }
}
```

