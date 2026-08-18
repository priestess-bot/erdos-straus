# T6 selector obligation ledger

> Status: `T6_GLOBAL_SELECTOR_TOTALITY = OPEN`.
>
> This is a machine-checked inventory of the current transition surface. It is
> deliberately not a global selector claim, a reachable-state exhaustion proof,
> or evidence that the Erdős--Straus conjecture is closed.

## Purpose

[`t6-selector-obligation-ledger-v1.json`](../data/t6-selector-obligation-ledger-v1.json)
records the distinction that the T6 program must preserve:

- a claim can give E1--E5 under its written receipt guard;
- that does not prove the guard occurs for every actual reachable state;
- a strict T5 ticket does not prove that any candidate exists; and
- a finite control remains `analysis_only` unless a universal proof closes its
  quantified family.

The ledger contains all 14 concrete edge claims currently listed by the T5
transition taxonomy, while excluding the generic legal-marked-state contract:
the latter is an admission schema, not a constructor.  Every source and target
is assigned to a named state family.  Each `OPEN` family is required to name a
`MINIMAL_SELECTOR_GAP`; the verifier rejects an inventory that silently drops
one.

## Current frontier

| Minimal gap | Exact missing statement | Why existing work does not close it |
|---|---|---|
| `GAP-O1-INITIAL-ROOT` | Every core root has a canonical legal serializer and first non-circular selector classification. | The contract specifies root fields, not a total dispatch. |
| `GAP-O1-GLOBAL-EXHAUSTION` | Every actual nonterminal reachable state belongs to a family with a total exit. | The registered-edge taxonomy is not an independent construction of the reachable set. |
| `GAP-O1-POST-G-TYPE-I` | Every nonterminal state after a q=1 or positive-q G handoff has a total Type I continuation. | The full-carrier handoff proves a root and first strict segment only. |
| `GAP-O1-A-GT-ONE-OVERFLOW` | Every actual residual `A>1` overflow is terminal or has E1--E5. | Current resets and bounded-divisor constructions are guarded. |
| `GAP-O1-HIGH-SUPPORT-ROOT-CAPACITY` | Every high-support/root-capacity state has a strict exit or is empty. | Sink-bundle selection only works when its improvement set is nonempty. |
| `GAP-O2-PROPER-ROOT-K-GT-ONE` | QC1 or TR1 physicalizes every actual proper-root `k>1` residual. | A formal quotient chart has neither E1 provenance nor an E4 lift. |
| `GAP-O3-C8-OUTGOING` | Every terminal-first-surviving c=8 parent has terminal, double-low receipt, or another verified edge. | The c=8 macro is conditional on the qualifying receipt. |
| `GAP-O4-NEW-ATOMIC-OR-MARKED-FAMILY` | Any future atomic or marked generator closes its T2/T3 obligations before admission. | Current named-graph unreachability says nothing about future constructors. |

The full JSON additionally names H4 non-v1 branches and nonterminal current
atomic targets, which are intentionally kept separate from c=8 existence.

## Interpretation rules

`CLOSED_BY_UNIVERSAL_SUCCESSOR` is local to the source guard written in the
underlying claim. It means the claim supplies a terminal or verified successor
for that declared source class, not that all reachable states enter the class.
`RELATIVE_EDGE_ONLY` means a handoff is valid only under an explicit source
hypothesis. `LOCAL_EDGE_ONLY` means a guarded construction exists but its
failure branch remains part of a global gap.

Only three closure modes are permitted for an open family:

1. a universal family-empty proof;
2. a universal terminal; or
3. a universal verified successor with E1--E5 and a strict T5 ticket.

Neither a no-go for one candidate action nor a finite scan is a fourth mode.

## Reproduction

```bash
python3 reproductions/type_i_t6_selector_obligation_ledger.py --verify
python3 -m unittest tests/test_type_i_t6_selector_obligation_ledger.py
```

The verifier cross-checks the ledger against the T5 taxonomy, every referenced
claim card and focused verifier, the current two-arm atomic surface, all
required O1--O4 entries, every open family, and the acceptance-gate status. A
passing result explicitly retains `T6_GLOBAL_SELECTOR_TOTALITY = OPEN`.
