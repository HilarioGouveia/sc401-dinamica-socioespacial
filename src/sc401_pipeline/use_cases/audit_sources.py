import json
from pathlib import Path
import geopandas as gpd
import pandas as pd
from sc401_pipeline.domain.schemas import AuditReport

VECTOR_SUFFIXES = {".shp", ".geojson", ".json", ".gpkg"}


def audit_file(source_name: str, file_path: Path, audit_dir: Path) -> AuditReport:
    audit_dir.mkdir(parents=True, exist_ok=True)
    warnings: list[str] = []

    if file_path.suffix.lower() in VECTOR_SUFFIXES:
        gdf = gpd.read_file(file_path)
        null_ratios = {col: round(float(gdf[col].isna().mean()), 4) for col in gdf.columns if col != "geometry"}
        valid_geoms = int(gdf.geometry.notna().sum() & gdf.geometry.is_valid.sum())
        if gdf.crs is None:
            warnings.append("CRS/SRID ausente no arquivo vetorial.")
        if valid_geoms < len(gdf):
            warnings.append(f"{len(gdf) - valid_geoms} geometrias inválidas ou nulas encontradas.")
        report = AuditReport(
            source_name=source_name,
            file_path=str(file_path),
            row_count=len(gdf),
            columns=[str(c) for c in gdf.columns if c != "geometry"],
            null_ratios=null_ratios,
            crs_detected=str(gdf.crs) if gdf.crs else None,
            valid_geometries=valid_geoms,
            warnings=warnings,
        )
    else:
        sep = ";" if file_path.suffix.lower() == ".csv" else ","
        df = pd.read_csv(file_path, sep=sep, dtype=str, low_memory=False)
        null_ratios = {str(col): round(float(df[col].isna().mean()), 4) for col in df.columns}
        report = AuditReport(
            source_name=source_name,
            file_path=str(file_path),
            row_count=len(df),
            columns=[str(c) for c in df.columns],
            null_ratios=null_ratios,
            warnings=warnings,
        )

    out_file = audit_dir / f"{source_name}_{file_path.stem}_audit.json"
    out_file.write_text(report.model_dump_json(indent=2), encoding="utf-8")
    return report


def dump_audit_summary(reports: list[AuditReport], out_path: Path) -> Path:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = [json.loads(r.model_dump_json()) for r in reports]
    out_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    return out_path
