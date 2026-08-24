# Agent 5 handoff: F3 R3/R5 quotient-only QC1

## Baseline

- Base: `9215f8c92c53c0eb1081849b0a03e5cb922facad`
- Branch: `sol/f3-qc1-quotient-only`
- Owned residuals: `R3_M3_NONQ5_QUOTIENT_ONLY`, `R5_MGT3_QUOTIENT_ONLY`

## Established result

Every actual R3/R5 state has the deterministic arithmetic carrier

\[
q_\perp=\min\{q:q\mid k,\ q\nmid h\},
\qquad 7\le q_\perp<p/4.
\]

For the actual stutter Eisenstein element (\beta=a-b\omega), the root
(\lambda=ab^{-1}\pmod {q_\perp}) determines one oriented prime ideal

\[
(q_\perp,\omega-\lambda)\mid\beta,
\]

while its conjugate does not divide (\beta). Its multiplicity is exactly
(v_{q_\perp}(k)). This is a source-bound algebraic factor, stronger than a bare
`q_perp|k` flag.

## Refuted transition attempt

The ideal factor is not an integer raw complete-excess occurrence. It does not identify
a raw side or node, does not compare its exponent with the current K capacity, and does
not justify charging one rational (q_\perp) factor into `absorbed_support`.
Consequently the attempted inference

```text
oriented ideal factor -> A_target=A*q_perp -> verified edge
```

is invalid. The reproducer now records E1 as incomplete and rejects every actual call
before transition construction.

The formulas

\[
L=\mathcal A q_\perp,
\quad c=\langle-q_\perp^{-1}\rangle_p,
\quad (R_T,K_T)=((4Lc-1)/p,Lc)
\]

remain a conditional target-shape theorem: if an independent integer occurrence and
charge-conservation theorem justifies (L), the target is high-support overflow,
(c\le p-2), and direct evaluation of the frozen family predicates uniquely matches
`type_i_a_gt_one_overflow_residual`. The control creates no producer rule, terminal
receipt, persistent state or runtime admission evidence.

## Evidence

- Claim: `claims/type-I-t6-f3-qc1-quotient-only-occurrence-boundary.md`
- Minimal residual: `data/t6-wave1/f3-qc1-minimal-residual-v1.json`
- Scope and matrix: `data/t6-wave1/f3-qc1-*.json`
- Candidate/negative controls:
  `reproductions/type_i_t6_f3_qc1_quotient_only_physical_transition.py`
- Tests: `tests/test_type_i_t6_f3_qc1_quotient_only_physical_transition.py`
- Interface request: `data/interface-requests/f3-qc1-target-shapes-v1.json`

## Smallest next theorem

For every actual R3/R5 input, prove that this same canonical (q_\perp) occurs on a
specific integer raw side/node/path with exponent above current K capacity, and prove a
one-use charge-conservation rule. Then replay the real source state/ROOT_SOL/scope, target
terminal dispatcher, shared producer registry and common admission.

## Status

```text
Q_PERP_EXISTENCE = ESTABLISHED
ORIENTED_IDEAL_FACTOR = ESTABLISHED
INTEGER_OCCURRENCE_AND_CONSERVATION = OPEN
R3 = OPEN_MINIMAL_RESIDUAL
R5 = OPEN_MINIMAL_RESIDUAL
OPEN_QC1_PHYSICAL_SERIALIZER = OPEN
F3 = OPEN
T6 = OPEN
```
