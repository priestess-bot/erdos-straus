# T6 F2/F3 Gate Audit

> Date: 2026-08-25
>
> Result: Gate 0 has a clean current checkout and the local runtime protocol is
> now source-audited. Gate 1 is only a local protocol freeze, Gate 2 remains a
> type-space freeze, and Gate 3 is not satisfied. F1, F2, F3 and T6 remain
> open.

## F1 Runtime Boundary

The shared PersistentSelectorRuntimeV1 has one concrete queue mutation:
PersistentSelectorRuntimeV1._enqueue_admitted_target_v1:self._queue.append.
Both bootstrap and successor paths reach it only after the common admission
gate. The constructor inventory audit now recognizes this anchor without
mistaking ordinary BFS list appends for selector queues.

This is not a global runtime result. The only instantiated runtime registers
two q=1 routes and ends at a declared DEAD_END. Its terminal schedules are
named local predicates, not a complete p-level terminal oracle. The exact
gap-11 terminal at

\[
p=241441,\qquad x=60363,\qquad d=1083
\tag{1}
\]

lies outside that local schedule. Therefore a local runtime MISS cannot
provide the complete terminal-first receipt required by C8, H4, F2 or F3.
The inventory retains four genuine F1 unknown items; nine source signals are
now explicitly classified as nonruntime controls and must be reopened if a
future producer integrates them.

## F2 High-Support Repair

The prior C=1/C>1 matrix silently assumed a canonical support chart. For a
general high-support header \(K=AC\), the exact split is

\[
C=c+pt,\qquad c=\langle(4A)^{-1}\rangle_p.
\tag{2}
\]

Only \(t=0\), equivalently \(R<4A\) and \(1\le C<p\), may enter the existing
determinant-dual C=1/C>1 theorems. The noncanonical branch \(t>0\) has a
strict total-cofactor normalizer with E2/E4/E5 arithmetic, but requires its
own E1/E3/re-entry package.

The formal chart

\[
(p,R,K;A)=(73,5551,101306;1369)
\tag{3}
\]

shows why the distinction is necessary: it passes the current generic state
schema with \(C=74\ge p\), but \(d=p-C\) is not a legal determinant-dual
parameter. It also has a post-hoc determinant identity, which is explicitly
an E1 negative control rather than a source receipt.

## F3 Interface Corrections

QC1 has two noninterchangeable target shapes:

\[
\begin{array}{c|c|c}
\text{norm-ideal proposal}&Aq_\perp&\langle-q_\perp^{-1}\rangle_p\\
\text{endpoint-excess deflation}&AE/q_\perp^\mu&\langle-q_\perp^\mu\rangle_p
\end{array}
\tag{4}
\]

The second needs its own projector and validator after a genuine source-bound
\(q_\perp\mid E\) occurrence. An ideal factor does not supply that occurrence.

For TR1, the R4 dyadic-fresh subleaf is empty because \(m=3\) makes \(D\)
odd. The R6 dyadic first child remains conditionally p-free, and the
R6-specific full-capacity theorem excludes the bad companion residue, reducing
the final arithmetic endpoint to terminal-or-single-side. Canonical rank,
source receipts and admission remain open. The short multi-step raw-word policy
belongs to the separate m=3,q=5 lineage and is not imported into R6.

For m=3,q=5, the existing source-bound macro accepts arbitrary state IDs and
scopes as digest inputs; it is not an admitted-source proof. The next actual
F3 activation remains the versioned endpoint-path receipt plus a registered
source owner and independent validator.

The F2 R=3 hard-core \(D=2p-3\) contact has now been parameterized exactly:
the prime-\(D\) stratum is family-empty, while composite \(D\) requires the
full quotient cofactor/order/gcd gate and has positive arithmetic controls.
This is a terminal-search reduction, not a global terminal theorem.

The R6 dyadic companion congruence has also been reduced: the full-capacity
\(W_y\) word cannot equal the bad residue \((h+1)/2\), so after source-bound
prefix replay the arithmetic endpoint is p-free and terminal-or-single-side.
Its canonical final rank and common admission are still open.

## Current Gate Status

| Gate | Status | Blocking fact |
|---|---|---|
| Gate 0 baseline | Current checkout audited | Historical workpack remains historical; current sources are separately audited. |
| Gate 1 runtime protocol | Local only | Two q=1 routes, partial terminal scope, no all-constructor coverage. |
| Gate 2 target grammar | Type-space only | No F2/F3 producer has passed complete E1-E5 admission. |
| Gate 3 F1 grammar | Open | Four inventory unknowns, no all-constructor re-entry theorem, and unresolved global queue coverage. |
| Gate 4 track admission | Open | Every F2/F3 nonterminal result still lacks at least E1, E3 or re-entry. |

The next proof-producing work must attach an actual source, complete terminal
priority and a common projector to one narrow residual branch. Adding another
chart identity, local rank inequality or fixture does not advance a Gate 4
admission.
