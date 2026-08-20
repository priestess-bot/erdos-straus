# Erdős–Straus T2 + T5 FULL integration bundle — 2026-08-17

## Status

```text
T2_ATOMIC_ADMISSION_V1
    = PHASE_LOCAL_GRAMMAR_CLOSED

T5_GLOBAL_WELL_FOUNDEDNESS
    = CONTRACT_LEVEL_WELL_FOUNDEDNESS_CLOSED

T6_GLOBAL_SELECTOR_TOTALITY
    = OPEN
```

The T5 status is intentionally stronger than the earlier `REGISTERED_EDGE_SCHEDULE_CLOSED` milestone.
FULL T5 no longer derives well-foundedness from a hand-maintained edge allowlist.  Instead it makes a
single canonical rank admission rule part of the state contract: every persistent successor must pass
E1--E4 and one of exactly three T5 tickets (`OUTER_RANK_DROP`, `PHASE_DROP`, `LOCAL_DROP`).

## Full T5 rank

For every persistent recursive state:

\[
\Pi_{T5}(S)=(\rho,\Phi,\Psi,r_1,r_2,r_3,r_4)\in\mathbb N^7
\]

with lexicographic order.

Major phases:

```text
TYPEII_REL          = 4
TYPEII_G_HANDOFF    = 3
TYPEI               = 2
GENERIC_MARKED      = 1
```

Type-I protocols:

```text
CHARGED = 4
PRE     = 3
ABSORB  = 2
RESET   = 1
```

Canonical local ranks:

- Type-II relation: `q`;
- Type-I CHARGED: `(floor(B_p/A), K/A, eta_p)`;
- PRE: `a`;
- ABSORB: `(R,m,r_epsilon)`;
- RESET: carrier `M`.

Same-rank upward phase/protocol re-entry is forbidden.  A smaller induction rank may reset everything.

## Why this is a complete T5 and not T5-v1

The contract-level theorem explicitly handles:

- Type-II F/G endpoint descent;
- any G->Type-I handoff once E1--E4 exists, not just a hard-coded q=1 allowlist;
- charged-support accumulation and overflow resets;
- high-support capacity macros and T2 atomic edges;
- immediate d=1 regeneration;
- PRE/ABSORB phase scheduling;
- legacy support-losing RESET and its known re-entry cycle;
- smaller marked/equation ranks;
- future q-adic/support-switch candidates through the same three admission tickets.

Terminal leaves, analysis evidence, pending normalization and macro internal checkpoints do not create
recursive successors and therefore do not require E5.

## What remains open

Only selector/existence questions, principally T6.  Examples: a positive-q G state may have no known
handoff, a high-support state may have no known improving candidate, or marked-terminal membership may
be unknown.  Such a state is a T6 dead-end; it does not invalidate T5 and does not require adding a new
T5 rank coordinate.

## Contents

- `T2_atomic_admission_v1/` — T2 finite atomic grammar and focused verifier.
- `T5_global_well_foundedness_full/` — complete contract-level T5 theorem, phase registry, transition
  taxonomy, state-contract patch and focused verifiers.
- `source_snapshots/` — exact public state-contract/theorem-ledger snapshots used for the audit.
- `run_focused_verifiers.sh` — contract-level controls.
- `validate_bundle.py` — frontmatter/JSON/taxonomy/whitespace checks.
- `PATCH-MANIFEST.md` — proposed repository destinations and merge discipline.
- `SHA256SUMS.txt` — artifact hashes.
