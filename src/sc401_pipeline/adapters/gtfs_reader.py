from pathlib import Path
import geopandas as gpd
import pandas as pd


def load_gtfs_stops(gtfs_dir: Path, feed_version: str) -> gpd.GeoDataFrame:
    stops_path = gtfs_dir / "stops.txt"
    stops = pd.read_csv(stops_path, dtype={"stop_id": str})
    gdf = gpd.GeoDataFrame(
        stops,
        geometry=gpd.points_from_xy(stops["stop_lon"], stops["stop_lat"]),
        crs="EPSG:4326",
    )
    gdf["feed_version"] = feed_version
    return gdf
