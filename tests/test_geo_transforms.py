import geopandas as gpd
from shapely.geometry import Polygon
from sc401_pipeline.use_cases.build_geo_core import compute_area_km2, normalize_to_srid


def test_normalize_and_area() -> None:
    poly = Polygon([
        (-48.52, -27.54),
        (-48.51, -27.54),
        (-48.51, -27.53),
        (-48.52, -27.53),
    ])
    gdf = gpd.GeoDataFrame({"id": [1]}, geometry=[poly], crs="EPSG:4326")
    projected = normalize_to_srid(gdf, target_srid=31982)
    with_area = compute_area_km2(projected)
    assert projected.crs.to_epsg() == 31982
    assert with_area["area_km2"].iloc[0] > 0
