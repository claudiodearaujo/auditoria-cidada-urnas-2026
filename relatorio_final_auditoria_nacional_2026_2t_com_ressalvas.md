# Relatorio final da auditoria nacional dos logs individuais — 2o turno 2026

**Classificacao:** PROCESSAMENTO CONCLUIDO COM RESSALVAS DOCUMENTAIS.

**Escopo:** arquivos locais do segundo turno presidencial de 25/10/2026, 27 UFs. Este documento nao constitui certificacao oficial dos resultados eleitorais.

## Sintese

- Comparecimentos informados nos BUs: **127,854,631**.
- Eventos individuais de voto computado encontrados: **127,854,309**.
- Antes de 17h de Brasilia: **127,819,979**.
- A partir de 17h de Brasilia (inclusive): **34,330**.
- 21 UFs conciliadas; 6 UFs com ressalvas, 7 secoes afetadas e 322 eventos nao conciliados.

## Votos por candidato (somente agregados dos BUs)

| Categoria | Votos |
|---|---:|
| Lula | 64,056,078 |
| Flavio Bolsonaro | 59,654,544 |
| Branco | 1,425,821 |
| Nulo | 2,718,188 |

Margem agregada entre candidatos: **4,401,534** votos. Os logs individuais nao identificam o candidato votado.

## Quadro completo das 27 UFs

| UF | Comparecimento BU | Eventos observados | Antes 17h | Desde 17h | Diferenca | Estado |
|---|---:|---:|---:|---:|---:|---|
| AC | 453,654 | 453,654 | 453,496 | 158 | +0 | CONCILIADO |
| AL | 1,951,632 | 1,951,632 | 1,950,986 | 646 | +0 | CONCILIADO |
| AM | 2,192,059 | 2,192,059 | 2,191,055 | 1,004 | +0 | CONCILIADO |
| AP | 429,975 | 429,975 | 429,833 | 142 | +0 | CONCILIADO |
| BA | 9,422,047 | 9,422,033 | 9,417,843 | 4,190 | -14 | RESSALVA |
| CE | 6,024,843 | 6,024,843 | 6,023,769 | 1,074 | +0 | CONCILIADO |
| DF | 1,868,280 | 1,868,280 | 1,867,300 | 980 | +0 | CONCILIADO |
| ES | 2,409,214 | 2,409,214 | 2,408,920 | 294 | +0 | CONCILIADO |
| GO | 4,047,280 | 4,047,280 | 4,046,546 | 734 | +0 | CONCILIADO |
| MA | 4,127,771 | 4,127,735 | 4,126,814 | 921 | -36 | RESSALVA |
| MG | 13,044,203 | 13,044,203 | 13,041,950 | 2,253 | +0 | CONCILIADO |
| MS | 1,594,460 | 1,594,460 | 1,594,038 | 422 | +0 | CONCILIADO |
| MT | 2,085,334 | 2,085,334 | 2,084,425 | 909 | +0 | CONCILIADO |
| PA | 4,989,573 | 4,989,573 | 4,988,265 | 1,308 | +0 | CONCILIADO |
| PB | 2,743,560 | 2,743,559 | 2,743,088 | 471 | -1 | RESSALVA |
| PE | 6,126,467 | 6,126,467 | 6,124,831 | 1,636 | +0 | CONCILIADO |
| PI | 2,239,830 | 2,239,829 | 2,239,492 | 337 | -1 | RESSALVA |
| PR | 7,059,339 | 7,059,339 | 7,058,413 | 926 | +0 | CONCILIADO |
| RJ | 10,077,449 | 10,077,449 | 10,073,299 | 4,150 | +0 | CONCILIADO |
| RN | 2,232,823 | 2,232,823 | 2,232,410 | 413 | +0 | CONCILIADO |
| RO | 988,489 | 988,489 | 987,934 | 555 | +0 | CONCILIADO |
| RR | 308,597 | 308,597 | 308,452 | 145 | +0 | CONCILIADO |
| RS | 6,889,638 | 6,889,636 | 6,888,807 | 829 | -2 | RESSALVA |
| SC | 4,762,303 | 4,762,303 | 4,761,840 | 463 | +0 | CONCILIADO |
| SE | 1,466,659 | 1,466,659 | 1,466,372 | 287 | +0 | CONCILIADO |
| SP | 27,364,389 | 27,364,121 | 27,355,261 | 8,860 | -268 | RESSALVA |
| TO | 954,763 | 954,763 | 954,540 | 223 | +0 | CONCILIADO |
| **TOTAL** | **127,854,631** | **127,854,309** | **127,819,979** | **34,330** | **-322** | **COM RESSALVAS** |

## Ressalvas e limites

- BA: 14 eventos nao conciliados em duas secoes.
- MA: 36 eventos nao conciliados em uma secao.
- PB: 1 evento nao conciliado em uma secao; confirmacoes de voto presentes.
- PI: 1 evento nao conciliado em uma secao; confirmacoes de voto presentes.
- RS: 2 eventos nao conciliados em uma secao; contingencia entre duas urnas.
- SP: 268 eventos sem log disponivel na secao 64777/0395/0298; arquivo o03221sp6477703950298-log.jez ausente no pacote analisado.

Os 322 eventos nao foram atribuidos artificialmente a horario nem candidato. A pequena dimensao numerica da divergencia nao demonstra integridade documental integral e nao constitui, isoladamente, prova de irregularidade.

## Metodologia e preservacao

- Corte de horario em Brasilia, com os ajustes de fuso registrados nos JSONs estaduais, incluindo as excecoes de AM e Fernando de Noronha/PE.
- Deduplicacao de eventos identicos de contingencia documentada; separacao de urnas fisicas conforme evidencias.
- Os arquivos originais ZIP, JSONs estaduais, scripts e evidencias permanecem preservados. Nenhuma exclusao foi executada por este gerador.
- Validacao: 27 UFs, somas por horario, totais de BUs e diferenca de 322 eventos.
- Verificacao criptografica integral de todos os ZIPs nao foi refeita nesta etapa.

## Fontes locais

- auditoria_por_uf/*.json
- auditoria_nacional_final_com_ressalvas_2026_2t.json
- diagnostico_global_pendencias_2026_2t.json
- validacao_independente_invariantes_2026_2t.json
- divergencias_identificadas_2026_2t.md
- solicitacao_tecnica_complementacao_logs_2026_2t.md (preparada, nao enviada)

Gerado em UTC: 2026-10-31T00:44:38.444595+00:00
