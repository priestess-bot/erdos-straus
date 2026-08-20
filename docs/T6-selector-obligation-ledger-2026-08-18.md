# T6 selector obligation ledger

> Status: `T6_GLOBAL_SELECTOR_TOTALITY = OPEN`.
>
> 2026-08-20 disposition: v1 remains the historical detailed ledger. The
> canonical frozen boundary is now `data/t6-proof-frontier-v2.json`; it retains
> all eight active mathematical gaps, closes O4 only as a frozen-v1 admission
> firewall, and groups the remaining work into F1--F5.
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

The ledger contains all 15 concrete edge claims currently listed by the T5
transition taxonomy, while excluding the generic legal-marked-state contract:
the latter is an admission schema, not a constructor.  Every source and target
is assigned to a named state family.  Each `OPEN` family is required to name a
`MINIMAL_SELECTOR_GAP`; the verifier rejects an inventory that silently drops
one.

## Current frontier

The earlier prose table omitted two gaps that were already present in the v1
JSON: non-v1 H4 branches and recursive closure of current atomic targets. That
presentation defect is repaired here. The complete active mathematical set is:

| Minimal gap | Exact missing statement | Why existing work does not close it |
|---|---|---|
| `GAP-O1-GLOBAL-EXHAUSTION` | Every actual nonterminal reachable state belongs to a family with a total exit. | The registered-edge taxonomy is not an independent construction of the reachable set. |
| `GAP-O1-H4-OTHER-BRANCHES` | Every actual H4 branch and every nonterminal descendant has a terminal or verified successor. | T1v1 covers only the actual `a=1` clean-q arm under its written guard. |
| `GAP-O1-POST-G-TYPE-I` | Every nonterminal state after a q=1 or positive-q G handoff has a total Type I continuation. | The full-carrier handoff proves a root and first strict segment only. |
| `GAP-O1-A-GT-ONE-OVERFLOW` | Every actual residual `A>1` overflow is terminal or has E1--E5. | The relative total-cofactor adapter retypes a supplied registered source, but no universal theorem supplies that registration for every residual. |
| `GAP-O1-HIGH-SUPPORT-ROOT-CAPACITY` | Every high-support/root-capacity state has a strict exit or is empty. | Sink-bundle selection only works when its improvement set is nonempty. |
| `GAP-O1-ATOMIC-TARGET-CLOSURE` | Every nonterminal target emitted by the current H4/c=8 atomic macros is recursively classified and dispatched. | Atomic admission and one strict macro step do not prove later totality. |
| `GAP-O2-PROPER-ROOT-K-GT-ONE` | QC1 or TR1 physicalizes every actual proper-root `k>1` residual. | A formal quotient chart and the current m=3,q=5 arithmetic policy have neither continuous E1 provenance nor a complete E4 lift. |
| `GAP-O3-C8-OUTGOING` | Every terminal-first-surviving c=8 parent has terminal, double-low receipt, or another verified edge. | The c=8 macro is conditional on the qualifying receipt. |

`GAP-O1-INITIAL-ROOT` is discharged. The p-only initializer fixes `q=1`,
`m=3`, and \(X=(p+3)/4\): a least factor of \(X\) congruent to
\(2\pmod 3\) gives a direct Type II root terminal, while its absence is the
ordinary q=1 G certificate consumed by the established full-carrier handoff
under its declared endpoint-local terminal prefix. This closes only the frozen
root construction; it does not imply that the Type I target, or every later
reachable state, has a total exit.

`GAP-O4-NEW-ATOMIC-OR-MARKED-FAMILY` is no longer left as an open process
promise for the frozen graph. The v2 admission firewall rejects any new atomic
or nontrivial marked target unless the change registers the family, extends
T2/T3, supplies serializer and lift, assigns a T6 owner, and passes the audit.
Its status is therefore `CLOSED_FOR_FROZEN_V1_BY_ADMISSION_FIREWALL`; any such
new constructor automatically reopens it.

The eight mathematical gaps are assigned exactly once: global exhaustion to
T6-F1, the six non-proper gaps to T6-F2, and proper-root `k>1` to T6-F3.
Selector assembly/lifts and independent closure are F4 and F5. See
[`T6-proof-boundary-2026-08-20.md`](T6-proof-boundary-2026-08-20.md).

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

The current `k=3` Vieta-companion obstruction is such a no-go: it removes the
same-`M` rechart attempt before a target exists, but does not alter the O2
quantifier or its `OPEN` status. The later primitive quotient normalization
is also structural only: it isolates all quotient-only factors in
\(\kappa=k/\gcd(a,e-1)\) and gives a generic actual-root cyclotomic saturation
identity. For a quotient-only prime \(q\), it further splits
\(q\mid(p^2+p+1)/h\) exactly by \(q\mid e\) or
\(B\equiv(p+1)A\pmod q\),
but creates no E1 provenance or E4 lift.

The latest \(m=3,q=5\) policy adds a stronger arithmetic reduction: after
p-free canonicalization, the repeated hard channel is isolated by
\(L_\omega\equiv1\pmod{p^2}\). This is recorded as
`ESTABLISHED_ARITHMETIC_ONLY`; it does not close O2 until the gate is proved
empty, terminal, or equipped with a complete paid successor and recursive
closure.

## Reproduction

```bash
python3 reproductions/type_ii_initial_q_one_root_dispatch.py --verify
python3 -m unittest tests/test_type_ii_initial_q_one_root_dispatch.py
python3 reproductions/type_i_t6_selector_obligation_ledger.py --verify
python3 -m unittest tests/test_type_i_t6_selector_obligation_ledger.py
python3 reproductions/pre_t6_contract_kernel_audit.py --root .
python3 -m unittest tests.test_pre_t6_contract_kernel_audit -v
```

The v1 verifier cross-checks the detailed ledger against the T5 taxonomy, every referenced
claim card and focused verifier, the current two-arm atomic surface, all
required O1--O4 entries, every open family, and the acceptance-gate status. A
passing result explicitly retains `T6_GLOBAL_SELECTOR_TOTALITY = OPEN`.

The v2 audit additionally freezes the 16-family/15-edge surface, checks the
closed-world mark invariant, rejects silent loss of any active mathematical
gap, and forbids promotion of the p-squared arithmetic reduction to a verified
edge. On a complete checkout it also compares v2 directly with the v1 JSON.
