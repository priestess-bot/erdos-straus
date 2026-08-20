#!/usr/bin/env python3
"""Checks the machine-readable T5 transition taxonomy for contract-surface completeness."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]

def verify():
    reg=json.loads((ROOT/'data/t5-full-phase-registry-v2.json').read_text())
    tax=json.loads((ROOT/'data/t5-full-transition-taxonomy-v2.json').read_text())
    assert reg['registry_id']=='t5_full_phase_registry_v2'
    assert tax['taxonomy_id']=='t5_full_transition_surface_v2'
    outputs={x['kind'] for x in tax['selector_outputs']}
    assert outputs=={
        'type_I_hit','type_II_hit','support_switch','q_adic_lift','generalized_dyadic_terminal'
    }
    tickets=set(reg['admission_tickets'])
    assert tickets=={'OUTER_RANK_DROP','PHASE_DROP','LOCAL_DROP'}
    # All current recursive families must name a T5 rank ticket.
    for row in tax['current_verified_edge_families']:
        assert row['rank_ticket'] and row['reference']
    # The three known cycle mechanisms must all be explicitly covered.
    names={x['name'] for x in tax['cycle_obstructions_resolved_by_phase_contract']}
    assert 'PRE/algebraic-inverse two-cycle' in names
    assert 'm=1 terminal-free formal self-loop' in names
    assert 'legacy reset re-entry carrier cycle' in names
    print('T5 FULL transition-surface taxonomy audit passed')

if __name__=='__main__':
    verify()
