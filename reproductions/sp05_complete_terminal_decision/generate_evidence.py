#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import sp05_contract as C
import sp05_constructor as P
import sp05_independent_replayer as R

ROOT = Path(__file__).resolve().parent
EVIDENCE = ROOT / "evidence"
EVIDENCE.mkdir(exist_ok=True)


def dump(name: str, value) -> None:
    (EVIDENCE / name).write_text(
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


p = 21169
source = C.make_reference_root_state(p)
source_decision = P.complete_source_terminal_decision(source)
projection = C.phase_projection(p)
projection_wire = P.projection_mapping(projection)
target_decision = P.complete_target_terminal_decision(source, projection)
source_replay = R.replay_source_decision(source, source_decision)
target_replay = R.replay_target_decision(source, projection_wire, target_decision)

dump(
    "p21169-terminal-replay.json",
    {
        "head_sha": C.PINNED_HEAD_SHA,
        "authority_boundary": "REFERENCE_SOURCE_SHAPE_ONLY_NOT_REPOSITORY_ACTUALNESS",
        "source_state": source,
        "source_terminal_decision": source_decision,
        "source_independent_replay": source_replay,
        "target_projection": projection_wire,
        "target_terminal_decision": target_decision,
        "target_independent_replay": target_replay,
        "conclusion": "TERMINAL_PREEMPTS_SUCCESSOR",
    },
)

controls = {}
for control_p in (73, 241441, 2689, 12721, 1201, 2521, 21169):
    result = P.bradford_m23_prefix(control_p)
    controls[str(control_p)] = result
controls["21169_gap31_typeII_d1"] = P._bradford_certificate(21169, 31, 1, "TYPEII")
dump("m23-and-gap31-controls.json", controls)

projection_evidence = {}
for control_p in (1201, 2521, 21169):
    projection = C.phase_projection(control_p)
    projection_evidence[str(control_p)] = {
        "projection": P.projection_mapping(projection),
        "projection_equation": 4 * projection.K == control_p * projection.R + 1,
        "anchor_gcd": __import__("math").gcd(projection.R - 1, projection.K),
        "source_potential": list(C.source_potential(control_p)),
        "target_potential": list(C.target_potential(control_p)),
        "ticket": C.PHASE_DROP,
        "strict_lex_drop": C.target_potential(control_p) < C.source_potential(control_p),
    }
dump("projection-anchor-t5.json", projection_evidence)

dump(
    "status-boundary.json",
    {
        "head_sha": C.PINNED_HEAD_SHA,
        "proved": [
            "finite complete terminal decision for each fixed p",
            "M23 prefix preemption",
            "global sorted factor-pair coverage",
            "unique phase-root projection",
            "canonical anchor miss",
            "identity solution lift",
            "frozen T5 PHASE_DROP",
            "conditional target owner and reentry shape",
            "nonterminal-edge/counterexample equivalence",
        ],
        "not_issued": [
            "exact-HEAD source actualness receipt for a complete-miss source",
            "production complete-schedule registry authority",
            "current-repository PersistentSelectorState successor admission",
            "queue mutation",
            "concrete nonterminal edge witness",
        ],
        "status": "OPEN_PROPOSITION_FOR_FIRST_ACTUAL_NONTERMINAL_EDGE",
        "reason": "A concrete complete-miss source is exactly an Erdos-Straus counterexample in the ordinary q=1 G domain.",
    },
)

print("evidence generated")
