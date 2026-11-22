from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "sc401_geo"
    postgres_user: str = "sc401_user"
    postgres_password: str = "change_me_local_dev"
    data_raw_dir: Path = Path("data/raw")
    data_audit_dir: Path = Path("data/audit")
    target_srid: int = 31982
    municipality_code: str = "4205407"

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


settings = Settings()
