import geopandas as gpd


def normalize_to_srid(gdf: gpd.GeoDataFrame, target_srid: int = 31982, fallback_epsg: int = 4326) -> gpd.GeoDataFrame:
    if gdf.crs is None:
        gdf = gdf.set_crs(epsg=fallback_epsg)
    cleaned = gdf[gdf.geometry.notna() & gdf.geometry.is_valid].copy()
    return cleaned.to_crs(epsg=target_srid)


def compute_area_km2(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    result = gdf.copy()
    result["area_km2"] = (result.geometry.area / 1_000_000.0).round(6)
    return result
