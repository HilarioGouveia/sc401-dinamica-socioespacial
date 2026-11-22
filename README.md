# Dinâmica socioespacial e acessibilidade no corredor da SC-401: integração de dados públicos e análise exploratória do ecossistema tecnológico

Projeto estruturado em fases para integração auditável de fontes públicas geoespaciais, demográficas, trabalhistas (setor de TI / CNAE 62) e de mobilidade urbana no eixo da rodovia SC-401 (Norte da Ilha de Florianópolis, SC — município `4205407`).

## Fase 1 — Escopo e Princípios
1. **Auditoria prévia de fontes (`audit`)**: inspeção de schema, códigos, valores nulos, geometrias e limites de uso antes de assumir cobertura ou granularidade.
2. **Ingestão bruta rastreável (`ingest`)**: armazenamento imutável em `data/raw/`, cálculo de hash SHA-256 e registro em `raw_data.ingestion_manifest`.
3. **Camada espacial padronizada (`build-core`)**: padronização para `SIRGAS 2000 / UTM zone 22S` (`EPSG:31982`) e carga em `geo_core` / `analytics_eda`.

> Nota metodológica: microdados públicos de RAIS/Novo CAGED são desidentificados (sem CNPJ completo ou endereço exato do estabelecimento), e arquivos GTFS descrevem a oferta programada de transporte público, não tráfego observado em tempo real.
