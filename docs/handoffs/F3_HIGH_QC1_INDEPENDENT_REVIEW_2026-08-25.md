# F3 high endpoint / QC1 independent review

Date: 2026-08-25

This is an independent Agent 4/5 review. It does not modify the shared
frontier, README, theorem ledger, selector grammar, or active producer
registry. Machine-readable scope, matrix, and target proposals are stored in:

- `data/t6-wave1/f3-high-qc1-narrow-scope-freeze-v1.json`
- `data/t6-wave1/f3-high-qc1-narrow-residual-matrix-v1.json`
- `data/interface-requests/f3-high-qc1-narrow-target-shapes-v1.json`

## Verdict

No `FAMILY_EMPTY`, terminal, or active `VERIFIED_SUCCESSOR` was proved.

Established arithmetic boundaries are:

1. High strict carry has a deterministic overflow-shaped target and a
   conditional local rank drop.
2. High stutter splits into a `k=1` Pell surface and an odd `k>=3` surface.
3. Quotient-only QC1 has a deterministic `q_perp` and an oriented Eisenstein
   ideal factor.
4. If `q_perp|E` and a source-forward integer path is independently verified,
   valuation recomputation gives a strict raw-deflation cofactor.

None of these supplies the missing source occurrence, common admission,
universal lift, or final T5 ticket over the original quantifier.

## High endpoint scope

The exact high domain is:

```text
ACTUAL_PERSISTENT AND PROPER_FACTOR_ROOT AND h>p AND terminal_first_miss
```

The input must retain an active producer, admission, replayable source path,
and maximal-receipt envelope. An arithmetic tuple with matching `p,h,r,D`
fields is not an actual input.

For high stutter, the valid relations include:

```text
D=(m-1)*p-(h-p-1)
e=(p*h+1)/D
a=e*m-h > e
N=a^2-a*(e-1)+(e-1)^2 = h*k
```

The inequality is `a>e`, opposite to the low-height `a<e` inequality.

## High k=1 Pell residual

For `k=1`, primitive square-factor normalization gives:

```text
e=d*x^2, a=d*x*y-1, gcd(x,y)=1, y>x
d=2 (mod 3), 3 does not divide x, 3 divides y
y^2+x*y-x^2 = c*(d*x*y-1), c=1 (mod 3)
```

Let `T=d*x^2` and `a=d*x*y-1`. The candidate numerator for `p` obeys the
exact identity:

```text
d^3*x^4*(x^2-x*y+y^2)-d^2*x^3*(x+y)+1
  = a*d^2*x^3*(y-x) + (T-1)*(T^2-T-1)
```

Thus candidate integrality requires the extra gate:

```text
a divides (T-1)*(T^2-T-1)
```

If `q=(T^2-T-1)/a`, the same identity gives:

```text
p=d^2*x^3*(y-x)+(T-1)*q
```

This is a genuine narrowing lemma, not an emptiness proof. It must still be
intersected with core primality, `p=1 (mod 24)`, proper root divisibility,
canonical `D`, terminal-first miss, and actual admission.

## Why low k=1 descent does not transfer

As a quadratic in `y`, the high Pell equation has the other root:

```text
y_sharp=(c*d-1)*x-y
```

Because `d=2 (mod 3)`, `c=1 (mod 3)`, `3|y`, and `3 does not divide x`,
`y_sharp = x (mod 3)`, so it leaves the high parameter domain even if it is
positive. As a quadratic in `x`, the other root is
`x_sharp=-(c*d-1)*y-x<0`.

Therefore the low-height Vieta descent, which relies on `a<e` and `y<=x`,
cannot close this high surface. The root-lift saturation result also gives an
infinite formal subprogression preserving fixed `(p,h,u,D)` divisor gates and
Theta-only terminal predicates. This blocks a proof based only on those static
valuation gates; it does not assert that an actual persistent high state exists.

The core curve control `p=115815206209,d=11,x=101,y=1020` is not a closure
witness: a gap-3 terminal fires before proper-root routing.

## QC1 occurrence boundary

For the low R3/R5 domain:

```text
q_perp=min{q prime: q|k and q does not divide h}
```

exists with `q_perp>=7` and `q_perp<p/4`. The oriented ideal
`(q_perp,omega-lambda)` divides `a-b*omega` with multiplicity
`v_q_perp(k)`. This is an algebraic norm occurrence, not an integer raw
source occurrence.

The focused nonactual control `p=54481, h=12063, k=q_perp=61` has
`v_61(R-h)=v_61(D)=v_61(E)=v_61(K)=0`. Its non-primality is intentional: it
shows that the present norm and ideal data do not imply `q_perp|E` or locate an
integer occurrence on the stutter side.

If `q_perp|E` and a replayable source-forward path is independently supplied,
the valuation theorem gives:

```text
M_child=A*E/q^mu
c_child=<-q^mu>_p < p-1
```

with `mu=1` or `v_q(p-1)+1` at the capacity boundary. This is only a
conditional raw suffix. It does not supply E1 when the root word is only
analysis metadata, nor E3, E4, re-entry, or a parent-to-final E5 ticket. The
atomic rank-stutter leaf has a deterministic second raw suffix, but the same
provenance and admission gaps remain.

## Quantifier vulnerabilities

1. **Arithmetic tuple versus actual source.** High Pell points and QC1
   controls do not carry active producer/admission/path receipts.
2. **Low theorem versus high domain.** Using `a<e`, `m<1+sqrt(h)`, `D_star>1`,
   or low QC1/TR1 routing in `h>p` silently shrinks the domain.
3. **Ideal factor versus integer occurrence.** Ideal divisibility does not
   identify a raw node, side, exponent above current capacity, or one-use
   support owner.
4. **Quotient factor versus endpoint excess.** `q_perp|k` does not imply
   `q_perp|E`; `A*q_perp` and `A*E/q^mu` are different target formulas.
5. **Local rank versus T5 ticket.** A formal cofactor drop is not the fixed
   parent-to-final-target `N^7` descent until common admission succeeds.
6. **Self-sealed replay.** A track-local digest or shape classification cannot
   authorize producer, terminal MISS, source mark, or recursive queue entry.

## Acceptance table

| obligation | result |
|---|---|
| high-domain scope freeze | established |
| high strict-carry arithmetic target | conditional shape only |
| high `k=1` Pell parameterization | established residual |
| high `k=1` FAMILY_EMPTY/terminal | not proved |
| high odd `k>=3` closure | not proved |
| QC1 `q_perp` existence/orientation | established arithmetic |
| QC1 integer occurrence | open |
| QC1 `q_perp|E` coverage | open; nonimplication control exists |
| QC1 endpoint strict raw suffix | conditional |
| QC1 E1/E3/E4/E5/re-entry | open |
| F3/T6 | open |

## Recommended next theorem

Do not add another static congruence audit. The smallest useful theorem is one
of the following, with the original quantifier preserved:

1. Prove a source-path lemma that forces a specified `q_perp` valuation above
   current `K` capacity (or proves an alternate terminal) for every R3/R5
   source.
2. Prove a high-domain theorem intersecting (H3) with canonical maximality and
   the complete terminal-first schedule, yielding FAMILY_EMPTY, terminal, or a
   paid successor.
3. If neither is available, retain the exact residual leaves and keep them
   nonrecursive.

## Focused verification

The following focused checks passed on the observed checkout:

```text
python3 reproductions/type_i_t6_f3_high_endpoint_k_one_pell.py --verify
python3 reproductions/type_i_t6_f3_high_endpoint_root_lift_saturation.py --verify
python3 reproductions/type_i_t6_f3_qc1_endpoint_excess_deflation.py --verify
python3 reproductions/type_i_t6_f3_qc1_quotient_only_physical_transition.py --verify
```

No broad range scan was used as proof, and no shared frontier or global status
was changed by this review.
