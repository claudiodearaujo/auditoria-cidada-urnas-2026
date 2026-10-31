import argparse, json, pathlib, sys
p=argparse.ArgumentParser()
p.add_argument('--origem',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parent)
a=p.parse_args()
root=a.origem
f=root/'auditoria_nacional_final_com_ressalvas_2026_2t.json'
if not f.exists(): sys.exit('Arquivo nacional nao encontrado: '+str(f))
d=json.loads(f.read_text(encoding='utf-8'))
rows=d['ufs']
assert len(rows)==27 and len(set(r['uf'] for r in rows))==27
t=d['totais']
for k in ['comparecimento_bu','eventos_observados','antes_17h_brasilia','desde_17h_brasilia_inclusive','diferenca']:
 assert t[k]==sum(r[k] for r in rows),(k,t[k])
assert t['eventos_observados']==t['antes_17h_brasilia']+t['desde_17h_brasilia_inclusive']
assert t['comparecimento_bu']-t['eventos_observados']==322
assert sum(r['status']=='RESSALVA' for r in rows)==6
print('VALIDADO: 27 UFs; eventos',t['eventos_observados'],'antes',t['antes_17h_brasilia'],'desde',t['desde_17h_brasilia_inclusive'],'diferenca',t['diferenca'])
