import hashlib
from pathlib import Path
import pandas as pd
from sc401_pipeline.adapters.postgis_repo import append_manifest, get_engine
from sc401_pipeline.domain.schemas import IngestionBatchRecord


def compute_sha256(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def register_raw_file(
    database_url: str,
    source_name: str,
    vintage: str,
    file_path: Path,
    record_count: int | None = None,
    notes: str | None = None,
) -> IngestionBatchRecord:
    sha256_hash = compute_sha256(file_path)
    if record_count is None:
        if file_path.suffix.lower() in {".csv", ".txt"}:
            record_count = len(pd.read_csv(file_path, sep=None, engine="python", dtype=str))
        else:
            record_count = 0

    record = IngestionBatchRecord(
        source_name=source_name,
        vintage=vintage,
        file_path=file_path,
        sha256_hash=sha256_hash,
        record_count=record_count,
        notes=notes,
    )
    engine = get_engine(database_url)
    append_manifest(
        engine,
        {
            "source_name": record.source_name,
            "vintage": record.vintage,
            "file_name": record.file_path.name,
            "sha256_hash": record.sha256_hash,
            "record_count": record.record_count,
            "notes": record.notes,
        },
    )
    return record
