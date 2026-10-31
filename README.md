# Auditoria cidadã de logs de urnas — 2º turno presidencial de 2026

Material educativo e técnico, apartidário. **Pacote preparado localmente; não publicado.**

## O que foi analisado
Relatórios derivados de arquivos de log e Boletins de Urna (BU) para as 27 UFs, votação de 25/10/2026. Foram observados 127.854.309 eventos individuais de 'voto computado' e 127.854.631 comparecimentos nos BUs. A conciliação por UF foi exata em 21 UFs e teve ressalvas em BA, MA, PB, PI, RS e SP (322 eventos de diferença no conjunto).

## Recorte temporal dos eventos observados
- Antes de 17h, horário de Brasília: 127.819.979.
- A partir de 17h, inclusive: 34.330.
- A classificação considera os fusos locais registrados nas análises estaduais.

**Não é possível descobrir a escolha de um eleitor pelo horário do evento.** Os totais por candidato vêm de BUs agregados, nunca de logs individuais. O total de 322 eventos não conciliados não equivale a 322 votos comprovadamente perdidos, nem comprova fraude.

## Como reproduzir este consolidado
1. Obtenha os arquivos originais em fontes oficiais e guarde seus hashes; não altere os ZIPs.
2. Execute e revise os processadores sobre cópias de trabalho, mantendo os registros de contingência e os fusos.
3. Gere os 27 JSONs estaduais no formato de 'auditoria_por_uf/<UF>.json'.
4. Execute: `python validar_resultados_publicos.py --origem CAMINHO_DA_AUDITORIA`.
5. Compare os totais, os hashes e as ressalvas com o relatório publicado.

**Limite de reprodutibilidade:** este kit contém o validador do consolidado e os relatórios, mas não inclui os ZIPs originais nem todo o pipeline de extração. A reprodução completa a partir de arquivos brutos exige publicar e revisar separadamente o pipeline de processamento, suas dependências e os identificadores de origem. Não apresente este kit como reprodução integral já demonstrada.

## Segurança e transparência
Não inclui credenciais, tokens, dados pessoais ou ZIPs originais. Antes de publicar, revise o histórico Git, licenças, direitos de redistribuição dos arquivos, URLs de origem, versões das ferramentas e hashes oficiais. Registre toda divergência sem preenchimento artificial.
