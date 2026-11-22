CREATE INDEX IF NOT EXISTS idx_census_tracts_geom
    ON geo_core.census_tracts_2022 USING GIST (geom);

CREATE INDEX IF NOT EXISTS idx_corridor_zones_geom
    ON geo_core.sc401_corridor_zones USING GIST (geom);

CREATE INDEX IF NOT EXISTS idx_transit_stops_geom
    ON geo_core.transit_stops_gtfs USING GIST (geom);

CREATE INDEX IF NOT EXISTS idx_ti_employment_period_cnae
    ON geo_core.ti_employment_series (cd_mun, ref_period, cnae_subclasse);
