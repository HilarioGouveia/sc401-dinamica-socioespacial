from pathlib import Path
import pandas as pd
from sc401_pipeline.use_cases.audit_sources import audit_file


def test_audit_csv_sample(tmp_path: Path) -> None:
    sample_csv = tmp_path / "amostra_cnae.csv"
    pd.DataFrame({"cd_mun": ["4205407", "4205407"], "cnae": ["6201101", None]}).to_csv(
        sample_csv, sep=";", index=False
    )
    report = audit_file(source_name="mte_amostra", file_path=sample_csv, audit_dir=tmp_path / "audit")
    assert report.row_count == 2
    assert report.null_ratios["cnae"] == 0.5
