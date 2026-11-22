from pathlib import Path
import geopandas as gpd


def load_geoportal_layer(layer_path: Path, default_epsg: int = 4326) -> gpd.GeoDataFrame:
    gdf = gpd.read_file(layer_path)
    if gdf.crs is None:
        gdf = gdf.set_crs(epsg=default_epsg)
    return gdf
