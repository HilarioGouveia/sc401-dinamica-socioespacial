# Inventário Verificável de Fontes (Fase 1)

| Fonte | Órgão / Gestor | Escopo na Fase 1 | Limitações e Verificação Obrigatória |
| :--- | :--- | :--- | :--- |
| **GeoPortal PMF** | PMF / IPUF | Camadas territoriais, viário, uso do solo | Conferir data de atualização, SRID e disponibilidade de séries históricas |
| **Censo Demográfico 2022** | IBGE | Setores censitários (`4205407`), população e domicílios | Usar dicionário oficial de cada produto/edição; evitar tratar agregados como microdados individuais |
| **RAIS / Novo CAGED** | MTE (PDET) | Vínculos, admissões, desligamentos e salários em CNAE grupo 62 | Bases públicas são não identificadas; não presumir geocodificação por lote/CNPJ sem ACT |
| **GTFS Transporte** | Consórcio Fênix / PMF | Paradas, rotas, viagens e frequências programadas | Mede oferta programada (`feed_version`), não velocidade média ou tráfego observado |
