# T6 F2 & F3 High-Concurrency Execution Plan

**Repository:** `priestess-bot/erdos-straus`

**Purpose:** Close all currently identified F2 and F3 obligations as quickly as possible under an 8-thread / 7-subagent execution model, without weakening theorem quantifiers or bypassing F1 admission requirements.

**Primary consumers:** Codex coordinator + sol-ultra subagents

**Execution mode:** 1 coordinator thread + up to 7 concurrent subagents
**Status discipline:** No theorem-status upgrade until all quantified leaves satisfy the exact acceptance contract below.

---

## 1. Mission

The objective of this wave is to complete the whole currently identified F2 and F3 surface required for T6.

The target closure condition is:

```text
T6-F2-NONPROPER-DISPATCH-TOTALITY
AND
T6-F3-PROPER-ROOT-PHYSICALIZATION
```

For every actual terminal-first surviving state in the combined F2/F3 domain, the implementation and proof package must deterministically establish exactly one of:

```text
FAMILY_EMPTY
TERMINAL
VERIFIED_SUCCESSOR(E1-E5)
```

The following statuses are explicitly insufficient for closure:

```text
ARITHMETIC_ONLY
CANDIDATE_TRANSITION
CONDITIONAL_ADAPTER
LOCAL_EDGE_ONLY
BLOCKED_BY_GRAMMAR
FINITE_CONTROL_PASSED
OPEN_MINIMAL_RESIDUAL
```

The final output of this wave is a frozen, auditable F2/F3 edge surface ready to be handed to F4 selector assembly.

---

## 2. Required Integration Baseline

Do not start new work from `main`, from only the F1 branch, or from only the F3 branch.

Create one integration baseline containing both post-`c851bd2` lines of work.

Recommended procedure:

```bash
git fetch --all --prune

git switch -c integration/t6-f2-f3-wave1 \
  c851bd213936b3bc8b3103b469292c139d229e97

git cherry-pick 1b66fd6
git cherry-pick c676ddd
```

If generated KB files conflict, do not manually merge theorem-ledger semantics. Finish the cherry-picks, then regenerate generated artifacts from the source claims:

```bash
python scripts/kb.py validate
python scripts/kb.py build
```

Then run the complete baseline audit:

```bash
python reproductions/pre_t6_contract_kernel_audit.py --root . --require-full-tree
python -m unittest tests.test_pre_t6_contract_kernel_audit -v
python -m unittest discover -s tests -p 'test_*.py'
python scripts/audit_t6_constructor_inventory_v1.py
git diff --check
```

Record the resulting full SHA in:

```text
data/t6-f2-f3-wave1-workpack.json
```

Every subagent branch and worktree must start from this exact SHA.

---

## 3. Execution Architecture

Use all available concurrency, but divide work by mutually exclusive mathematical quantifier domains rather than by files or proof techniques.

| Thread | Suggested branch | Exclusive responsibility |
|---|---|---|
| Coordinator | `integration/t6-f2-f3-wave1` | Integration, F1 admission/runtime substrate, shared grammar, merging, final status control |
| Agent 1 | `sol/f2-post-g-h4-totality` | post-G Type-I continuation + C2/H4 full branch totality |
| Agent 2 | `sol/f2-overflow-high-support-totality` | all A>1 overflow + high-support empty-improvement |
| Agent 3 | `sol/f2-c8-atomic-closure` | c8 outgoing totality + recursive closure of H4/c8 atomic targets |
| Agent 4 | `sol/f3-high-endpoint` | all actual proper-factor high endpoints h>p |
| Agent 5 | `sol/f3-qc1-quotient-only` | R3/R5 quotient-only QC1 physicalization |
| Agent 6 | `sol/f3-h-supported-tr1` | R4/R6 h-supported / transverse TR1 physicalization |
| Agent 7 | `sol/f3-m3-q5-p2` | R1/R2 m=3,q=5 source path, serializer, second child, p^2 gate |

Recommended worktrees:

```bash
git worktree add ../wt-f2-post-g -b sol/f2-post-g-h4-totality <INTEGRATION_SHA>
git worktree add ../wt-f2-overflow -b sol/f2-overflow-high-support-totality <INTEGRATION_SHA>
git worktree add ../wt-f2-atomic -b sol/f2-c8-atomic-closure <INTEGRATION_SHA>
git worktree add ../wt-f3-high -b sol/f3-high-endpoint <INTEGRATION_SHA>
git worktree add ../wt-f3-qc1 -b sol/f3-qc1-quotient-only <INTEGRATION_SHA>
git worktree add ../wt-f3-tr1 -b sol/f3-h-supported-tr1 <INTEGRATION_SHA>
git worktree add ../wt-f3-p2 -b sol/f3-m3-q5-p2 <INTEGRATION_SHA>
```

---

## 4. Global Closure Contract

Every track must satisfy the same closure contract.

For every state in the track's exact quantified domain, prove a mutually exclusive and exhaustive guard partition whose every leaf is exactly one of:

```text
FAMILY_EMPTY
TERMINAL
VERIFIED_SUCCESSOR
```

A `VERIFIED_SUCCESSOR` is valid only when all of E1-E5 are present.

### E1 — Actual source receipt

Must bind the successor to an actual source occurrence and actual path.

Required properties:

- parent/source identity;
- source occurrence provenance;
- terminal-first miss receipt;
- branch-precedence receipt;
- replayable path digest;
- no actualness inferred from a fixture or boolean eligibility field.

### E2 — Deterministic target

The successor target must be uniquely recomputable.

Required properties:

- deterministic constructor;
- fixed tie-breaks;
- no oracle choice;
- no manual prime/factor selection;
- no hidden dependence on test fixtures.

### E3 — Persistent-state admission

Required properties:

- canonical target schema;
- normal form;
- family predicate classification;
- owner and precedence;
- owner/family digest;
- passage through the common admission gate;
- no caller-supplied family or owner authority.

### E4 — Universal lift

The lift must hold for the whole quantified branch, not only for sampled instances.

### E5 — Fixed T5 descent

The final persistent target must strictly decrease the same frozen global T5 potential in `N^7`.

A local checkpoint decrease is not enough. The relevant comparison is parent to final admitted target.

---

## 5. Coordinator Critical Path

The coordinator owns all shared interfaces and must actively remove the common bottleneck preventing F2/F3 results from entering the active graph.

### 5.1 Complete `PRODUCER_PROJECTION_AND_EXCLUSIVE_ADMISSION_V1`

Required outcome:

- every non-false recursive source signal is classified as a registered producer or explicit nonrecursive control;
- every producer has a complete terminal/reject/nonterminal guard partition;
- every nonterminal target is projected to `PersistentSelectorStateV1`;
- every target passes extractor, family classification, owner validation, and admission;
- initializer and every successor queue mutation pass one and only one common admission gate.

### 5.2 Establish the minimal shared runtime

Implement one deterministic replay runtime, conceptually:

```text
PersistentSelectorRuntimeV1
    ├── verify_source_state
    ├── dispatch_terminal_first
    ├── call_registered_producer
    ├── project_target_to_PersistentSelectorStateV1
    ├── reject_before_persistent_queue_v1
    └── enqueue_admitted_target
```

Recommended producer interface:

```python
def produce_transition_v1(
    *,
    producer_id: str,
    branch_id: str,
    source_state: PersistentSelectorStateV1,
    source_receipt: dict,
) -> TerminalResult | RejectedResult | CandidateTransition:
    ...
```

Recommended admission interface:

```python
def admit_candidate_transition_v1(
    candidate: CandidateTransition,
) -> VerifiedSuccessor | RejectedResult:
    ...
```

### 5.3 Remove forbidden admission patterns

The following must not independently grant recursive authority:

```text
recursive_edge_eligible=True
persistent_queue=True
family_id supplied by caller
owner supplied by caller
normal_form supplied from unverified cache
parent reconstructed from a bare prime
registry name treated as an executable producer
```

### 5.4 Two-stage freeze

#### Freeze A — runtime protocol

Freeze early:

```text
PersistentSelectorStateV1 envelope
producer rule schema
source receipt schema
terminal result schema
candidate transition schema
admission result schema
T5 ticket API
```

#### Freeze B — final grammar

Collect all seven agents' target-shape proposals first, then freeze:

```text
family predicates
precedence
allowed overlaps
producer-declared target sets
atomic arms
mark behavior
grammar hash
producer registry hash
```

This prevents late E3 rework.

### 5.5 Coordinator acceptance

Before F1 grammar freeze:

- unresolved producer/source-signal count = 0;
- initializer and every active producer have one disposition;
- root -> full-carrier -> first Type-I step -> second-anchor consumes serialized predecessors continuously;
- no producer reconstructs its parent from a prime or fixture;
- every target uses the same extractor;
- every queue mutation uses the same gate;
- zero-family, illegal-overlap, unknown-producer, unknown-branch cases fail closed;
- new F2/F3 producers use the same registration protocol;
- actual trace induction replays from initializer through all admitted successors.

---

## 6. Agent 1 — F2 post-G, C2 and H4 Totality

### Quantified domain

Own all actual terminal-first-surviving states arising from:

- ordinary q=1 G endpoints;
- positive-q G endpoints;
- full-carrier Type-I roots;
- first Type-I successors;
- second-anchor descendants;
- d=1 relay descendants;
- high-C=2 19-phase descendants;
- every H4 selector branch;
- nonterminal F/G descendants emitted by H4.

### Objectives

1. Actualize all G handoffs.
   - q=1 G;
   - positive-q G;
   - c=3 source-lineage G.
   - Each must bind a real source receipt and produce the common persistent schema.
   - If a conditional source is unreachable, prove it unreachable instead of registering it.

2. Close the continuous post-G chain:

```text
G endpoint
  -> full-carrier root
  -> first Type-I child
  -> second-anchor
  -> postmacro receiver
```

3. Lift d=1 relay from fixture-level control to its full actual domain.

4. Upgrade C2 19-phase arithmetic summaries to actual target-producing transitions.

5. Build an exhaustive H4 guard DAG including at minimum:
   - terminal-first branches;
   - proper/non-proper overlap;
   - top/non-top capacity;
   - a_alt=1 / a_alt>1;
   - clean-q / non-clean-q;
   - F/G/atomic/other descendants.

6. Route atomic outputs through Agent 3's common atomic target contract.

### Acceptance

- no post-G `later dispatch open` remains;
- positive-q is either actualized or proven unreachable;
- H4 guard partition is symbolic, exhaustive and mutually exclusive;
- C2 no longer terminates at arithmetic-only summary;
- every nonterminal result is an admitted active-family successor;
- every successor has E1-E5;
- close `GAP-O1-POST-G-TYPE-I`;
- close `GAP-O1-H4-OTHER-BRANCHES`.

---

## 7. Agent 2 — F2 A>1 Overflow and High-Support Totality

### Quantified domain

Own every actual terminal-first-surviving:

- `A>1` overflow state;
- high-support F/G sink state with `A > B_p = (p-1)^2/4`.

### Objectives

1. Build a complete `A>1` partition under fixed precedence:

```text
terminal
same-chart support promotion
joined-support outer reset
bounded-divisor fixed-n descent
M complete-excess transition
total-cofactor transition
high-support routing
explicit residual
```

The final explicit residual must be proven empty or given a paid successor.

2. Actualize the M complete-excess adapter.
   - add target normal form;
   - typed owner;
   - serializer;
   - terminal-first precedence;
   - recursive re-entry;
   - surface admission.
   - If its source family is unreachable, prove that instead.

3. Resolve the known p=409 anomaly rather than trusting self-reported eligibility.

4. Lift high-support nonempty improvement from focused controls to a full-domain deterministic selector.

5. Close empty-improvement separately for:
   - C=1;
   - C>1.

For C=1, do not reuse the already-known non-decreasing same-protocol complete-excess route. Closure must be family-empty, terminal, outer-rank/lower-protocol descent, or another full E1-E5 reset.

### Acceptance

- every actual `A>1` state has exactly one exit;
- M is either a real producer or proven unreachable;
- no fixture-manufactured actualness remains;
- the p=409 anomaly is explicitly classified;
- high-support nonempty improvement is universally proved;
- C=1 and C>1 empty-improvement are both closed;
- all targets enter the common grammar;
- close `GAP-O1-A-GT-ONE-OVERFLOW`;
- close `GAP-O1-HIGH-SUPPORT-ROOT-CAPACITY`.

---

## 8. Agent 3 — F2 c8 Outgoing and Atomic Recursive Closure

### Quantified domain

Own:

- every actual q=1 full-carrier d=1 parent reaching c8 after terminal-first;
- every nonterminal H4 atomic output;
- every nonterminal c8 atomic output.

### Objectives

1. Prove the c8 total exit trichotomy:

```text
TERMINAL
DOUBLE_LOW_VERIFIED_SUCCESSOR
OTHER_VERIFIED_SUCCESSOR
```

2. Build one shared atomic target serializer for H4 and c8, conceptually:

```text
AtomicPendingTargetV1
    source_parent_id
    source_macro_id
    source_path_digest
    terminal_first_digest
    atomic_grammar_arm
    canonical payload
    chart facts
    F/G/hit classification
    scope
    T5 ticket candidate
```

3. Project atomic targets into `PersistentSelectorStateV1` through the common admission gate.

4. Close downstream F/G routing rather than leaving `pending_suffix`, `pending_dispatch` or `later selector` markers.

5. If a new atomic shape exceeds T2v1/T3v1:
   - emit a precise family/arm request;
   - expand T2 grammar;
   - update T3 if nontrivial marks become reachable;
   - keep the transition unregistered until the firewall passes.

### Acceptance

- c8 trichotomy holds for the full actual domain;
- every c8 actual parent exits;
- H4 and c8 use the same atomic serializer;
- no pending atomic target remains active;
- every atomic F/G target has recursive re-entry;
- all new grammar arms pass T2/T3 admission;
- close `GAP-O3-C8-OUTGOING`;
- close `GAP-O1-ATOMIC-TARGET-CLOSURE`.

---

## 9. Agent 4 — F3 Proper-Root High Endpoint

### Quantified domain

Own exactly:

```text
ACTUAL_PERSISTENT
AND PROPER_FACTOR_ROOT
AND h > p
AND terminal_first_miss
```

Do not import low-height-only fields or theorems such as `N=hk`, `k>=1`, `D_star>1`, or QC1/TR1 low-height routing unless separately re-proved in this domain.

### Objectives

1. Rebuild the high-endpoint normal form only from valid high-height hypotheses.

2. Prove one of the following for the whole domain:
   - family empty;
   - all states terminal;
   - deterministic physical successor.

3. If producing a successor, supply:
   - actual root occurrence;
   - deterministic carrier and tie-break;
   - target normal form;
   - universal lift;
   - parent-to-target T5 ticket;
   - admitted recursive re-entry.

### Acceptance

- proof statement preserves the exact `PROPER_FACTOR_ROOT` high-height quantifier;
- no actualness is inferred from arithmetic controls;
- no low-height-only field is read without proof;
- whole domain closes by empty/terminal/E1-E5 successor;
- `OPEN_HIGH_ENDPOINT_TOTAL_EXIT` disappears.

---

## 10. Agent 5 — F3 R3/R5 Quotient-Only QC1

### Quantified domain

Own:

```text
R3_M3_NONQ5_QUOTIENT_ONLY
R5_MGT3_QUOTIENT_ONLY
```

with:

```text
2 <= h < p
k > 1
k_perp > 1
```

excluding the dedicated `m=3, 5 | D_star` route.

### Objectives

1. Establish the canonical quotient-only carrier:

```text
q_perp = min { q : q | k and q does not divide h }
```

2. Prove `q_perp` exists across the whole R3/R5 domain and bind it to an actual source occurrence.

3. Implement one shared `QC1PhysicalTransitionV1` that provides E1-E5.

4. Use fixed tie-breaks only; no human-selected factors.

5. Eliminate every quotient-only residual. If the route changes family, prove the new family predicate rather than relabeling it.

### Acceptance

- R3 and R5 are universally covered;
- active QC1 serializer is nonempty;
- carrier is an actual occurrence, not only a divisibility fact;
- deterministic target and E1-E5 are present;
- all targets pass common admission;
- close `OPEN_QC1_PHYSICAL_SERIALIZER` on the quotient-only domain.

---

## 11. Agent 6 — F3 R4/R6 H-Supported / TR1

### Quantified domain

Own:

```text
R4_M3_NONQ5_H_SUPPORTED
R6_MGT3_H_SUPPORTED
```

with:

```text
2 <= h < p
k > 1
k_perp = 1
```

excluding `m=3, 5 | D_star`.

### Objectives

1. Build an exhaustive h-supported partition:

```text
terminal
QC1 via genuinely admissible h-supported carrier
TR1 via D_star/transverse carrier
family-empty
explicit residual
```

The final explicit residual must disappear.

2. Bind TR1 to an actual parent, source path, actual factor occurrence, terminal-first misses and deterministic factor selection.

3. Implement `TR1PhysicalTransitionV1` with E1-E5.

4. If R4 and R6 require distinct arithmetic payloads, keep one common envelope and admission protocol.

### Acceptance

- R4 and R6 are universally covered;
- `k_perp=1` is never treated as quotient-only;
- active TR1 serializer exists;
- the no-transverse case is empty, terminal or paid;
- all targets pass common F1 admission;
- close `OPEN_TR1_PHYSICAL_SERIALIZER` outside the m=3,q=5 domain.

---

## 12. Agent 7 — F3 m=3, q=5 and the p^2 Gate

### Quantified domain

Own exactly:

```text
R1_M3_Q5_PATH_UNBOUND
R2_M3_Q5_PATH_BOUND_NO_SERIALIZER
```

with actual persistent proper-root input and:

```text
m = 3
5 | D_star
```

### Objectives

1. Close source-path coverage for R1.
   - every actual state has a canonical replayable raw path;
   - priority misses are explicit;
   - the q=5 occurrence is actual;
   - path/policy word is source-bound.

2. Implement the R2 endpoint serializer, including:
   - first child;
   - deterministic omega_pf suffix;
   - policy endpoint;
   - complete-excess recomputation;
   - one-sided/two-sided classification;
   - target owner;
   - recursive admission.

3. Preserve the distinction between:

```text
L1 = (E/l) F_y
L_omega = E_u E_v
```

No theorem for L1 may be silently applied to L_omega.

4. Close the complete p^2 gate:

```text
E_u E_v = 1 + p^2 chi
```

Handle all three structural cases:

- pure-dyadic;
- full-capacity one-sided;
- genuine two-sided atomic.

Each must close as empty, terminal, or E1-E5 paid successor.

5. Close the second-child problem.
   - prove existence or family-empty;
   - deterministic tie-break;
   - no return to parent;
   - target typing;
   - parent-to-final-target T5 ticket.

### Acceptance

- R1 path coverage is total;
- R2 has an active serializer;
- pure-dyadic closes;
- one-sided closes;
- genuine two-sided closes;
- second child has full E5;
- no use of `L1 = L_omega`;
- higher p-adic congruences alone are not counted as closure;
- close `OPEN_M3_Q5_SOURCE_PATH_COVERAGE`;
- close `OPEN_M3_Q5_TARGET_AND_SECOND_CHILD`;
- close `OPEN_M3_Q5_P2_GATE`.

---

## 13. File Ownership Rules

High concurrency must not create constant merge conflicts in shared frontier and runtime files.

### Coordinator-only files

Only the coordinator may directly modify:

```text
README.md
index/theorem-ledger.md
index/catalog.json
data/t6-proof-frontier-v2.json
data/t6-selector-obligation-ledger-v1.json
data/t5-full-transition-taxonomy-v2.json
data/t6-constructor-inventory-v1.json
concepts/t6-persistent-selector-state-v1.md
scripts/t6_persistent_selector_state_v1.py
shared selector runtime
shared producer registry
shared family grammar
```

### Subagent-owned outputs

Subagents should add track-specific files under:

```text
claims/
data/
docs/
reproductions/
tests/
```

Use track-prefixed names to avoid collisions.

### Shared-interface requests

If a subagent needs a new family, owner, atomic arm, mark or shared grammar change, it should not directly edit the coordinator-owned grammar. Instead emit:

```text
data/interface-requests/<track-id>-family-request-v1.json
```

The coordinator owns the final decision and implementation.

### Generated index files

Subagents may run KB build locally but should not commit conflicting generated `index/` files. The coordinator regenerates them after cherry-picking source claims.

---

## 14. Mandatory First Deliverables for Every Subagent

Before attempting a long final proof, every subagent must first publish three small machine-auditable artifacts.

### 14.1 Scope freeze

Example:

```json
{
  "track_id": "F3-QC1",
  "base_sha": "<integration-sha>",
  "quantifier": "...",
  "excluded_domains": ["..."],
  "existing_established_lemmas": ["..."],
  "forbidden_inferences": ["..."]
}
```

### 14.2 Residual matrix

Every leaf should expose:

```json
{
  "leaf_id": "...",
  "predicate": "...",
  "mutually_exclusive_with": ["..."],
  "coverage_proof": "...",
  "planned_closure": "EMPTY|TERMINAL|VERIFIED_SUCCESSOR",
  "target_shape": "...",
  "current_blocker": "..."
}
```

### 14.3 Target-shape proposal

List every target shape the track may produce, including:

```text
existing family match
new family required
atomic arm required
mark behavior
T5 ticket type
owner precedence request
```

The coordinator should use these seven proposals to freeze the final grammar before the proofs are integrated.

---

## 15. Definition of Done for Every Track

| ID | Requirement | Acceptance condition |
|---|---|---|
| D1 | Exact quantifier | Actual state, terminal-first assumptions, and all guards are explicit |
| D2 | Exhaustive partition | Leaves are mutually exclusive and union to the whole input domain |
| D3 | E1 | Source occurrence, path, provenance and precedence are replayable |
| D4 | E2 | Target is unique and deterministic, with fixed tie-breaks |
| D5 | E3 | Schema, normal form, owner, digest and common admission all pass |
| D6 | E4 | Universal lift holds over the full quantified branch |
| D7 | E5 | Final admitted target strictly decreases the fixed T5 `N^7` potential |
| D8 | Re-entry | Target re-enters the active selector domain |
| D9 | Negative controls | malformed/unknown/overlap/priority-drift cases fail closed |
| D10 | Independent replay | Independent auditor does not call the selector logic being audited |

No track is closed unless D1-D10 all pass.

---

## 16. Cross-Audit Pairing

The proof author must not be the sole authority that upgrades its own track.

Use these pairings:

```text
Agent 1 <-> Agent 3
post-G/H4 vs atomic/c8

Agent 5 <-> Agent 6
QC1 vs TR1

Agent 4 <-> Agent 7
high endpoint vs m=3,q=5

Agent 2
coordinator review + independent review from the first available F2 agent
```

Every cross-audit must explicitly search for:

- quantifier shrinkage;
- fixture-as-actual errors;
- divisor-as-occurrence errors;
- arithmetic-child-as-persistent-successor errors;
- missing terminal precedence;
- family label used as E3;
- local potential used as T5;
- finite search used as family-empty;
- unregistered constructors;
- unreviewed T2/T3 grammar expansion.

---

## 17. Work Stealing / Dynamic Reallocation

If one subagent finishes early or becomes genuinely blocked on a shared interface, reallocate it rather than leaving it idle.

Priority order for assistance:

1. Agent 7 genuine two-sided p^2 residual;
2. Agent 2 high-support C>1 empty-improvement;
3. Agent 4 high endpoint;
4. Agent 1 H4 other branches;
5. Agent 6 no-transverse h-supported residual;
6. independent mutation tests and replay verifiers.

Assistants must work on separate branches:

```text
assist/<target-track>/<subproblem>
```

They should contribute independent derivations, counterexample searches, symbolic verifiers, mutation controls or review notes. The original track owner decides whether a proof is adopted; the coordinator decides whether code is cherry-picked.

---

## 18. Research Stop-Loss Rules

A new arithmetic lemma counts as progress only if it does at least one of:

- strictly shrinks a registered residual quantifier domain;
- proves a family empty;
- proves a branch terminal;
- directly constructs a deterministic paid successor;
- eliminates a complete guard leaf.

The following are not sufficient on their own:

```text
higher-order congruence
more divisibility conditions
stronger lower bound
smaller finite search range
more computational examples
```

### Forbidden inference patterns

Do not:

```text
use registry count as constructor exhaustion
infer actualness from recursive_edge_eligible=True
infer admission from persistent_queue=True
infer E3 from a family label
infer E5 from a local checkpoint drop
reconstruct the parent from a bare prime
register a conditional adapter as an actual edge
use finite search as family-empty proof
transfer an L1 p^2 theorem to L_omega without a bridge
use low-height k/D_star theorems in the high-endpoint domain
```

---

## 19. Merge Gates

### Gate 0 — Integration baseline

Integrate the existing F1 and F3 branches. Run all validation.

### Gate 1 — Runtime protocol freeze

Freeze:

```text
state envelope
producer rule
source receipt
terminal result
candidate transition
admission result
T5 ticket API
```

### Gate 2 — Target-shape freeze

Collect all seven target-shape proposals and freeze:

```text
family predicates
new atomic arms
new marks
precedence
allowed overlaps
producer target sets
```

### Gate 3 — F1 grammar freeze

All existing and newly proposed producers must have:

- complete partition;
- common serializer;
- common gate;
- actual re-entry;
- no bypass path.

Only after Gate 3 may a candidate transition become an active verified successor.

### Gate 4 — Track admission

Recommended integration order:

1. Agent 3 atomic serializer;
2. Agent 5 QC1 common serializer;
3. Agent 6 TR1 common serializer;
4. Agent 1 post-G/H4;
5. Agent 2 overflow/high-support;
6. Agent 4 high endpoint;
7. Agent 7 m=3,q=5 p^2.

### Gate 5 — Combined F2/F3 closure receipt

Coordinator generates:

```text
data/t6-f2-nonproper-totality-v1.json
data/t6-f3-proper-root-physicalization-v2.json
data/t6-f2-f3-combined-closure-receipt-v1.json
```

Required summary counters:

```text
F2 residual leaves = 0
F3 residual leaves = 0
unknown producers = 0
unadmitted targets = 0
pending dispatch/targets = 0
conditional actual edges = 0
T5 ticket failures = 0
```

### Gate 6 — Status update

Only after all gates pass may the coordinator update:

```text
T6-F1-REACHABLE-STATE-EXHAUSTION = CLOSED
T6-F2-NONPROPER-DISPATCH-TOTALITY = CLOSED
T6-F3-PROPER-ROOT-PHYSICALIZATION = CLOSED
```

Do not close T6 itself yet. After F1-F3, the remaining work is F4 selector assembly followed by F5 independent audit.

---

## 20. Validation Commands

Every subagent branch must run at least:

```bash
python scripts/kb.py validate
python scripts/kb.py build
python reproductions/pre_t6_contract_kernel_audit.py --root . --require-full-tree
python -m unittest tests.test_pre_t6_contract_kernel_audit -v
python -m unittest discover -s tests -p 'test_*.py'
python scripts/audit_t6_constructor_inventory_v1.py
git diff --check
```

For modified Python files:

```bash
python -m py_compile <all-modified-python-files>
```

The coordinator reruns the full suite after every batch of cherry-picks and regenerates generated KB artifacts before evaluating theorem status.

---

## 21. Final Wave Acceptance

This F2/F3 wave is complete only when all of the following are simultaneously true:

```text
F1 unresolved producer/source-signal count = 0
F2 open family leaves = 0
F3 residual families = 0
unknown or conditional actual producers = 0
pending dispatch/target states = 0
all nonterminal successors pass the common admission gate
all nonterminal successors have strict tickets in the fixed T5 N^7 potential
all negative controls fail closed as intended
independent replay passes
full KB validation passes
full-tree audit passes
all unit tests pass
```

Only then may the frozen F2/F3 edge set be handed to F4.

---

## 22. Expected Final Handoff to F4

The coordinator should end the wave with a compact handoff stating:

```text
1. frozen integration SHA
2. frozen grammar hash
3. frozen producer registry hash
4. complete F2 family table and receipts
5. complete F3 family table and receipts
6. exact T5 ticket taxonomy used by every edge
7. independent replay command set
8. zero residual counters
9. explicit statement that T6 remains open only for F4 + F5
```

F4 must then build one deterministic terminal-first selector over this frozen edge set. F5 must audit that selector from a clean checkout using an independent verifier.
