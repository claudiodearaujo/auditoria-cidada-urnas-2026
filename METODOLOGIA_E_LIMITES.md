# Metodologia e limites de interpretação

**BU**: resumo agregado da votação de uma seção; informa totais, mas não revela horários individuais de escolha.
**Log**: sequência técnica de eventos da urna. A expressão 'O voto do eleitor foi computado' é um marcador técnico; sua contagem não é automaticamente equivalente à quantidade de votos válidos para presidente.
**Fusos**: o corte 17h é aplicado em horário de Brasília, não simplesmente na hora exibida pelo log. Verificar exceções territoriais.
**Contingência**: logs de urnas substituídas podem coexistir; deduplicar apenas eventos comprovadamente repetidos e preservar a trilha.
**Ressalvas**: BA -14, MA -36, PB -1, PI -1, RS -2, SP -268. Em PB e PI existem outros marcadores de confirmação compatíveis com os comparecimentos. Em SP faltou o arquivo o03221sp6477703950298-log.jez no ZIP analisado.
**Limites**: não inferir candidato, identidade, voto secreto ou fraude a partir de um evento. O processamento não certifica a completude de todas as fontes. Os 322 eventos não recebem horário imputado.
**Verificabilidade**: hashes confirmam integridade dos bytes de uma cópia conhecida, não por si sós autenticidade, completude ou ausência de adulteração na origem.
