CREATE TABLE IF NOT EXISTS raw_data.ingestion_manifest (
    batch_id         BIGSERIAL PRIMARY KEY,
    source_name      VARCHAR(80)  NOT NULL,
    vintage          VARCHAR(40)  NOT NULL,
    file_name        TEXT         NOT NULL,
    sha256_hash      CHAR(64)     NOT NULL,
    record_count     INTEGER      NOT NULL CHECK (record_count >= 0),
    ingested_at      TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    notes            TEXT
);

CREATE TABLE IF NOT EXISTS geo_core.census_tracts_2022 (
    cd_setor         VARCHAR(20)  PRIMARY KEY,
    cd_mun           VARCHAR(7)   NOT NULL,
    nm_bairro        VARCHAR(120),
    pop_total        INTEGER,
    dom_part_ocup    INTEGER,
    area_km2         NUMERIC(12, 6),
    geom             GEOMETRY(MultiPolygon, 31982) NOT NULL
);

CREATE TABLE IF NOT EXISTS geo_core.sc401_corridor_zones (
    zone_id          SERIAL PRIMARY KEY,
    zone_name        VARCHAR(120) NOT NULL,
    corridor_role    VARCHAR(50)  NOT NULL,
    geom             GEOMETRY(MultiPolygon, 31982) NOT NULL
);

CREATE TABLE IF NOT EXISTS geo_core.transit_stops_gtfs (
    stop_id          VARCHAR(64)  PRIMARY KEY,
    stop_name        VARCHAR(200),
    feed_version     VARCHAR(64)  NOT NULL,
    scheduled_trips_weekday INTEGER CHECK (scheduled_trips_weekday >= 0),
    geom             GEOMETRY(Point, 31982) NOT NULL
);

CREATE TABLE IF NOT EXISTS geo_core.ti_employment_series (
    series_id        BIGSERIAL PRIMARY KEY,
    source_type      VARCHAR(20)  NOT NULL CHECK (source_type IN ('RAIS', 'NOVO_CAGED')),
    cd_mun           VARCHAR(7)   NOT NULL,
    ref_period       VARCHAR(10)  NOT NULL,
    cnae_subclasse   VARCHAR(10)  NOT NULL,
    active_links     INTEGER,
    admissions       INTEGER,
    separations      INTEGER,
    avg_wage_brl     NUMERIC(12, 2),
    is_identified    BOOLEAN      NOT NULL DEFAULT FALSE,
    UNIQUE (source_type, cd_mun, ref_period, cnae_subclasse)
);

CREATE TABLE IF NOT EXISTS analytics_eda.tract_accessibility_summary (
    cd_setor             VARCHAR(20) PRIMARY KEY REFERENCES geo_core.census_tracts_2022(cd_setor),
    dist_sc401_m         NUMERIC(12, 2),
    stops_within_500m    INTEGER DEFAULT 0,
    trips_within_500m    INTEGER DEFAULT 0,
    pop_density_km2      NUMERIC(12, 2),
    updated_at           TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
