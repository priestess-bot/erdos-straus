# Agent 7 F3 m=3,q=5,p2 Wave-2 handoff: genuine two-sided residual

## Baseline and ownership

- Branch: `sol/f3-m3-q5-p2`
- Baseline: `da550fe949fee70a853b094295f69959e3f7c4e5`
- Parent track: `R1_M3_Q5_PATH_UNBOUND` / `R2_M3_Q5_PATH_BOUND_NO_SERIALIZER`
- Focused leaf: `R2_M3_Q5_P2_TWO_SIDED`
- Shared files deliberately untouched: `README.md`, `index/**`, frontier/ledger,
  persistent runtime, common grammar and producer registry.

The mandatory scope freeze, residual matrix and target-shape proposal are:

```text
data/t6-wave1/f3-m3-q5-p2-two-sided-scope-freeze-v1.json
data/t6-wave1/f3-m3-q5-p2-two-sided-residual-matrix-v1.json
data/interface-requests/f3-m3-q5-p2-two-sided-target-shapes-v1.json
```

## Exact result

The existing source-bound macro is sufficient for the following sequence only:

```text
actual parent
  -> replayable root/path receipt
  -> terminal-first priority misses
  -> p-free endpoint
  -> original-K complete-excess recanonicalization
```

At the endpoint, if

\[
u=E_uD_u,\qquad v=E_vD_v,
\qquad E_u,E_v>1,
\qquad E_uE_v=1+p^2\chi,
\]

then the direct canonical target has

\[
c_T=p-1,
\qquad K_T=K(1+p^2\chi).
\]

It is an increasing reparameterization of the same \(a=1,d=1\) root chart:

\[
T=p^2\varrho-(p+1)/2,
\qquad
\varrho' = \varrho+\chi T,
\qquad
T'=T(1+p^2\chi).
\]

Thus the direct image is not a strict T5 edge. It is a nonpersistent checkpoint and
does not establish E3 or recursive re-entry.

## Why the current macro cannot close it

| Gate | Finding |
|---|---|
| E1 | The path receipt ends at the p-free endpoint. The canonical rechart supplies no new source-forward occurrence. |
| E2 | The endpoint normal form gives a deterministic (E_u,E_v,D_u,D_v) and canonical image. |
| E3 | No active serializer/owner/admission binds the p2 rechart as a recursive state. |
| E4 | The (\operatorname{Sol}(p)) identity lift is conditional after target validation. |
| E5 | (c_T=p-1) leaves the fixed charged local rank unchanged; no strict ticket is available. |
| Re-entry | Open until a later source-forward suffix or terminal is proved. |

The smallest valid closure theorem is therefore one of:

1. a full actual family-empty proof;
2. a terminal-first certificate; or
3. a new source-forward final atomic macro with complete E1--E5 and active re-entry.

The two-sided normal form, a higher (p)-adic congruence, or a finite arithmetic control
does not satisfy this disjunction.

## Independent negative controls

`reproductions/type_i_t6_f3_m3_q5_p2_two_sided_boundary.py` independently reconstructs
the arithmetic control used by the existing p2 verifier. It checks:

- (p=73, \varrho=57), (T=303716), (A=11237492), (K=809099424),
  (R=44334215);
- a primitive p-free two-sided endpoint
  ((u,v)=(43726898,607317));
- (E_u=21863449), (E_v=202439),
  (E_uE_v=4426014752111=1+73^2\cdot830552590);
- canonical cofactor (c_T=72=p-1), and the exact increasing rechart identity;
- a same-chart endpoint with multiplier noncongruent to (1\pmod p), showing that
  the p2 congruence is not chart-wide;
- rejection of a nonprimitive/non-p-free endpoint.

This is deliberately an arithmetic control, not an actual (m=3,5\mid D_*\) witness.
It proves consistency of the residual normal form and the absence of a direct E5 ticket;
it does not prove the residual is nonempty.

## Current disposition

```text
R1 source-path coverage                 OPEN (coordinator integration)
R2 strict endpoint branches              conditional arithmetic closure
R2 genuine two-sided p2                 OPEN_MINIMAL_RESIDUAL
F3 proper-root physicalization           OPEN
T6 selector totality                     OPEN
```

No family or atomic arm is requested. The proposed final target, if a future theorem finds
one, should project to the existing high-support `type_i_a_gt_one_overflow_residual` family
only after synchronous normalization and a parent-to-final strict ticket.
