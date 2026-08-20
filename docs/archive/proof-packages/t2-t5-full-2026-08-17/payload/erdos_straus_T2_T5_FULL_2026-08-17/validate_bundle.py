#!/usr/bin/env python3
from pathlib import Path
import json, subprocess, yaml
ROOT=Path(__file__).resolve().parent
CLAIM_REQUIRED={'kind','claim_id','title','statement','claim_status','topics','sources','visibility','last_checked'}
CONCEPT_REQUIRED={'kind','concept_id','title','summary','topics','sources','visibility','last_checked'}

def frontmatter(path):
    text=path.read_text(encoding='utf-8')
    assert text.startswith('---\n'), path
    return yaml.safe_load(text.split('---',2)[1])

def main():
    for p in ROOT.rglob('claims/*.md'):
        d=frontmatter(p); assert CLAIM_REQUIRED<=set(d), (p,CLAIM_REQUIRED-set(d)); assert d['kind']=='claim'
    for p in ROOT.rglob('concepts/*.md'):
        d=frontmatter(p); assert CONCEPT_REQUIRED<=set(d), (p,CONCEPT_REQUIRED-set(d)); assert d['kind']=='concept'
    reg=json.loads((ROOT/'T5_global_well_foundedness_full/data/t5-full-phase-registry-v2.json').read_text())
    tax=json.loads((ROOT/'T5_global_well_foundedness_full/data/t5-full-transition-taxonomy-v2.json').read_text())
    assert set(reg['admission_tickets'])=={'OUTER_RANK_DROP','PHASE_DROP','LOCAL_DROP'}
    assert {x['kind'] for x in tax['selector_outputs']}=={'type_I_hit','type_II_hit','support_switch','q_adic_lift','generalized_dyadic_terminal'}
    subprocess.run([str(ROOT/'run_focused_verifiers.sh')],check=True)
    generated_roots=[ROOT/'T2_atomic_admission_v1', ROOT/'T5_global_well_foundedness_full']
    for base in generated_roots:
        for p in base.rglob('*'):
            if p.is_file() and p.suffix in {'.md','.py','.json','.sh','.csv'} and 'patches' not in p.parts:
                txt=p.read_text(encoding='utf-8')
                for i,line in enumerate(txt.splitlines(),1):
                    assert line==line.rstrip(), f'trailing whitespace {p}:{i}'
    print('T2 + T5 FULL bundle validation passed')
if __name__=='__main__': main()
