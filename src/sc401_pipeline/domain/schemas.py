from datetime import datetime
from pathlib import Path
from pydantic import BaseModel, Field


class AuditReport(BaseModel):
    source_name: str
    file_path: str
    row_count: int = Field(ge=0)
    columns: list[str]
    null_ratios: dict[str, float]
    crs_detected: str | None = None
    valid_geometries: int | None = None
    warnings: list[str] = Field(default_factory=list)
    audited_at: datetime = Field(default_factory=datetime.utcnow)


class IngestionBatchRecord(BaseModel):
    source_name: str
    vintage: str
    file_path: Path
    sha256_hash: str
    record_count: int = Field(ge=0)
    notes: str | None = None
