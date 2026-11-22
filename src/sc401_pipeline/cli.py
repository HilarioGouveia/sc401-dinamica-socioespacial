from pathlib import Path
import typer
from sc401_pipeline.config import settings
from sc401_pipeline.use_cases.audit_sources import audit_file
from sc401_pipeline.use_cases.ingest_raw import register_raw_file

app = typer.Typer(help="CLI da Fase 1 — Dinâmica socioespacial e acessibilidade no corredor da SC-401")


@app.command()
def audit(source_name: str, file_path: Path) -> None:
    """Audita um arquivo de amostra e salva relatório JSON em data/audit."""
    report = audit_file(source_name=source_name, file_path=file_path, audit_dir=settings.data_audit_dir)
    typer.echo(report.model_dump_json(indent=2))


@app.command()
def ingest(
    source_name: str,
    vintage: str,
    file_path: Path,
    notes: str | None = None,
) -> None:
    """Calcula hash SHA-256 do arquivo bruto e registra o lote no PostGIS."""
    record = register_raw_file(
        database_url=settings.database_url,
        source_name=source_name,
        vintage=vintage,
        file_path=file_path,
        notes=notes,
    )
    typer.echo(record.model_dump_json(indent=2))


if __name__ == "__main__":
    app()
