import geopandas as gpd
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine


def get_engine(database_url: str) -> Engine:
    return create_engine(database_url, future=True)


def append_manifest(engine: Engine, record: dict) -> None:
    sql = text(
        """
        INSERT INTO raw_data.ingestion_manifest (
            source_name, vintage, file_name, sha256_hash, record_count, notes
        ) VALUES (
            :source_name, :vintage, :file_name, :sha256_hash, :record_count, :notes
        )
        """
    )
    with engine.begin() as conn:
        conn.execute(sql, record)


def replace_geodataframe(engine: Engine, gdf: gpd.GeoDataFrame, schema: str, table_name: str) -> None:
    gdf.to_postgis(name=table_name, con=engine, schema=schema, if_exists="replace", index=False)


def upsert_tabular(engine: Engine, df: pd.DataFrame, schema: str, table_name: str) -> None:
    df.to_sql(name=table_name, con=engine, schema=schema, if_exists="append", index=False)
