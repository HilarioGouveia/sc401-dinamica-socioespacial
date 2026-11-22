from pathlib import Path
import pandas as pd

TI_CNAE_PREFIXES = ("6201", "6202", "6203", "6209")


def read_mte_table(file_path: Path, sep: str = ";", encoding: str = "latin1") -> pd.DataFrame:
    return pd.read_csv(file_path, sep=sep, encoding=encoding, dtype=str, low_memory=False)


def filter_ti_cnae(df: pd.DataFrame, cnae_col: str = "cnae_2_subclasse") -> pd.DataFrame:
    if cnae_col not in df.columns:
        raise KeyError(f"Coluna CNAE '{cnae_col}' não encontrada nas colunas: {list(df.columns)}")
    cleaned = df[cnae_col].astype(str).str.replace(r"\D", "", regex=True)
    return df[cleaned.str.startswith(TI_CNAE_PREFIXES)].copy()
