---
kind: claim
claim_id: type-I-t6-f3-tr1-fresh-dstar-endpoint-split
title: TR1 D-star factors split exactly into fresh raw factors and capacity-saturated factors
statement: >-
  For an actual low proper-root stutter endpoint with z=ED in canonical
  maximal complete-excess form, every prime factor of D_star is either absent
  from E and capacity-saturated, or belongs to E and yields a deterministic
  source-bound primitive raw deflation. Thus gcd(D_star,E) is the exact
  fresh-factor discriminator. If 2 divides that gcd, the raw child is also
  p-free. This is a relative E1 arithmetic bridge requiring an independently
  verified endpoint transcript and terminal prefix; it supplies neither child
  recanonicalization, E2--E5, common admission nor TR1 closure.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-strict-carry-universal-raw-word-policy-boundary
  - type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
topics:
  - type-I
  - F3
  - TR1
  - proper-root
  - stutter
  - D-star
  - complete-excess
  - raw-deflation
  - p-free
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: primewise canonical maximality formulas
  - claim: type-I-root-capacity-strict-carry-universal-raw-word-policy-boundary
    role: primitive source-forward raw move
  - claim: type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
    role: pure-T-side valuation specialization
visibility: public
last_checked: '2026-08-25'
---

# TR1 fresh D-star factors versus capacity-saturated factors

## 1. Exact valuation dichotomy

Let an actual low proper-root stutter receipt satisfy

\[
2\le h<p,\qquad z=R-h=ED,
\tag{1}
\]

where \(E,D\) are obtained from the canonical maximal complete-excess
normalization relative to \(K=A(p-1)\). Put

\[
D_* = \frac{D}{(D,h^2-1)}.
\tag{2}
\]

For a prime \(q\mid D_*\), write

\[
a=v_q(A),\qquad k=v_q(K),\qquad b=v_q(z).
\tag{3}
\]

The primewise maximality formulas give

\[
v_q(D)=
\begin{cases}
b,&b\le k,\\
a,&b>k,
\end{cases}
\qquad
v_q(E)=
\begin{cases}
0,&b\le k,\\
b-a,&b>k.
\end{cases}
\tag{4}
\]

Therefore

\[
\boxed{q\nmid E\Longleftrightarrow b=v_q(D)\le k,}
\tag{5}
\]

and

\[
\boxed{q\mid E\Longleftrightarrow b>k,quad v_q(D)=a,quad q\in Q_K(z).}
\tag{6}
\]

Define the fresh set

\[
\mathcal F_{\rm fresh}(S)=
\{q\text{ prime}:q\mid(D_*,E)\}.
\tag{7}
\]

If this set is empty, no \(D_*\)-prime is an endpoint complete-excess factor;
the existing bundle/atomic grammar has no paid factor at that coordinate. If it
is nonempty, take its least prime \(q\).

## 2. Conditional source-forward raw suffix

Assume in addition that a persistent source has already supplied a replayable
path to the actual primitive endpoint \((z,h,1)\), and that all prior
\(Q\mid u\) terminal checks return MISS. By (6),
\(v_q(z)>v_q(K)\), so the raw rule gives

\[
(z,h,1)\longmapsto
\left(\frac zq,R-\frac zq,1\right).
\tag{8}
\]

Since \(q\mid D_*\), it divides neither \(p\) nor \(h\); moreover
\((z,R)=(z,h)=1\). Thus the step has shift \(q-1\), no gcd reduction, and
remains primitive. It is a relative E1 bridge only: the endpoint word
constructed backward from a desired root cannot replace the assumed source
path.

## 3. Dyadic fresh factor

If \(2\mid(D_*,E)\), write

\[
x=\frac z2,\qquad y=R-\frac z2.
\tag{9}
\]

The child is automatically \(p\)-free. Indeed \(p\nmid x\) because
\(z\equiv1-h\pmod p\) and \(2\le h<p\). If \(p\mid y\), then
\(z\equiv2\pmod p\), hence \(h=p-1\). But \(h\mid p^2+p+1\) and
\(p\equiv1\pmod h\) would give \(h\mid3\), forcing \(p=4\), impossible
for a core prime. Hence \(p\nmid xy\).

The remaining obligations are deliberately unchanged: a child terminal prefix,
complete-excess/atomic split, target normal form, E2--E5, common admission and
re-entry still require a new source-bound receipt interface. In particular,
terminal misses of the \(Q\mid u\) menu do not imply
\((D_*,E)>1\).
