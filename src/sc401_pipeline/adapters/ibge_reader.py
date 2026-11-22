from pathlib import Path
import geopandas as gpd
import pandas as pd


def read_census_tracts(vector_path: Path, municipality_code: str = "4205407") -> gpd.GeoDataFrame:
    gdf = gpd.read_file(vector_path)
    mun_col = next((c for c in ["CD_MUN", "cd_mun", "COD_MUN"] if c in gdf.columns), None)
    if mun_col:
        gdf = gdf[gdf[mun_col].astype(str).str.startswith(municipality_code)].copy()
    return gdf


def read_census_attributes(table_path: Path, sep: str = ";") -> pd.DataFrame:
    return pd.read_csv(table_path, sep=sep, dtype=str, low_memory=False)
