# Decisões Metodológicas — Fase 1

1. **Sistema de Referência Espacial (`EPSG:31982`)**: todas as camadas vetoriais e pontuais são convertidas para `SIRGAS 2000 / UTM zone 22S` para cálculos de distância e proximidade em metros.
2. **Associação vs. Causalidade**: a Fase 1 foca em integração, estatística descritiva e análise exploratória espacial, sem afirmar causalidade direta da expansão tecnológica sobre preços imobiliários ou saturação viária.
3. **Resolução de Dados Trabalhistas**: vínculos e movimentações em TI (CNAE 6201-1, 6202-0, 6203-8, 6209-1) são tratados no nível de agregação disponível na base auditada, registrando `is_identified=FALSE` para microdados públicos anonimizados.
