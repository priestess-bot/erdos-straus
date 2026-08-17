#!/usr/bin/env python3
"""Checks the machine-readable T5 transition taxonomy for contract-surface completeness."""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[1]

def verify():
    reg=json.loads((ROOT/'data/t5-full-phase-registry-v2.json').read_text())
    tax=json.loads((ROOT/'data/t5-full-transition-taxonomy-v2.json').read_text())
    contract=(ROOT/'concepts/denominator-escape-state-contract.md').read_text(encoding='utf-8')
    assert reg['registry_id']=='t5_full_phase_registry_v2'
    assert tax['taxonomy_id']=='t5_full_transition_surface_v2'
    outputs={x['kind'] for x in tax['selector_outputs']}
    assert outputs=={
        'type_I_hit','type_II_hit','support_switch','q_adic_lift','generalized_dyadic_terminal'
    }
    tickets=set(reg['admission_tickets'])
    assert tickets=={'OUTER_RANK_DROP','PHASE_DROP','LOCAL_DROP'}
    assert '选择器只能返回下列五种带类型回执。' in contract
    for heading in (
        '### 4.1 type_I_hit',
        '### 4.2 type_II_hit',
        '### 4.3 support_switch',
        '### 4.4 q_adic_lift',
        '### 4.5 generalized_dyadic_terminal',
    ):
        assert heading in contract
    assert '只有 E1--E5 全部通过后，状态才可标记为 verified_edge。' in contract
    assert '### 6.9 T5 完整全局良基合同（2026-08-17）' in contract
    document_ids=set()
    for directory, field in ((ROOT/'claims', 'claim_id'), (ROOT/'concepts', 'concept_id')):
        for path in directory.glob('*.md'):
            match=re.search(rf'^{field}:\s*(\S+)\s*$', path.read_text(encoding='utf-8'), re.MULTILINE)
            if match:
                document_ids.add(match.group(1))
    # Every contract edge family must name a present claim/concept and a T5 rank ticket.
    for row in tax['current_verified_edge_families']:
        assert row['rank_ticket'] and row['reference'] in document_ids
    # The three known cycle mechanisms must all be explicitly covered.
    names={x['name'] for x in tax['cycle_obstructions_resolved_by_phase_contract']}
    assert 'PRE/algebraic-inverse two-cycle' in names
    assert 'm=1 terminal-free formal self-loop' in names
    assert 'legacy reset re-entry carrier cycle' in names
    print('T5 FULL transition-surface taxonomy audit passed')

if __name__=='__main__':
    verify()
