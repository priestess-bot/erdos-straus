---
kind: claim
claim_id: t6-q-one-phase-root-target-terminal-transport-anchor-miss-v1
title: q=1 phase-root 的有限 terminal predicate transport 与 anchor-sink 恒 MISS
statement: >-
  Let p=24t+1 be a core prime with an ordinary q=1 G root surviving the
  registered Bradford terminal prefix at gaps 3, 7 and 11. For the canonical
  full-carrier phase root R=16t+3, K=(6t+1)(16t+1), the same p-only Bradford
  candidate sets at gaps 3, 7 and 11 are empty in any target representation,
  while gcd(R-1,K)=1. Hence the finite target schedule consisting exactly of
  that transported prefix followed by the R-1 divides K anchor-sink predicate
  has a scope-bound MISS. This is a mathematical transport theorem only: it
  does not issue a target terminal receipt, E2, E3, E4, E5, producer,
  admission, queue or global-exhaustion authority.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - q-one
  - phase-root
  - terminal-first
  - finite-scope
  - anchor-sink
  - proof-boundary
sources:
  - claim: t6-q-one-production-terminal-issuer-v1
    role: exact registered-prefix MISS input contract
  - claim: t6-coordinator-q1-root-prefix-scoped-e1-authority-v4
    role: ordinary q=1 G root and phase-root occurrence contract
  - claim: type-II-q-one-full-carrier-phase-root-entry
    role: canonical full-carrier root formula and fresh source
  - reproduction: scripts/t6_q_one_phase_root_independent_math_replay_v1.py
    role: independent replay of R, K, full-carrier projection and phase-drop evidence
  - reproduction: scripts/t6_q_one_root_v1_base_admission_verifier_v1.py
    role: complete divisor enumeration convention for the registered prefix
visibility: public
last_checked: '2026-08-27'
---

# Target Terminal Transport

## Scope

Fix an ordinary q=1 G root for a core prime

\[
p=24t+1,
\qquad X=\frac{p+3}{4}=6t+1.
\]

The canonical phase-root chart is

\[
R=16t+3,
\qquad K=X(16t+1),
\qquad A=1,
\qquad 4K=pR+1.
\tag{1}
\]

This claim assumes only the already registered finite terminal prefix is a
MISS. It does not assert a complete terminal universe.

For an odd gap \(m\), let \(x_m=(p+m)/4\). Define the finite frozen Bradford
candidate predicate by iterating every \(d\mid x_m^2\), in increasing divisor
order, and then Type I before Type II. The Type-I family contains precisely
the \(d\) satisfying

\[
d\mid x_m^2,
\qquad m\mid px_m+d,
\qquad m\mid p\left(x_m+p\frac{x_m^2}{d}\right),
\tag{2I-guard}
\]

and has the candidate form

\[
\left(x_m,\frac{px_m+d}{m},\frac{p(x_m+p x_m^2/d)}{m}\right)
\tag{2I}
\]

The Type-II family contains precisely the \(d\) satisfying

\[
d\mid x_m^2,
\qquad d\le x_m,
\qquad m\mid x_m+d,
\qquad m\mid p(x_m+d),
\qquad m\mid p\left(x_m+\frac{x_m^2}{d}\right),
\tag{2II-guard}
\]

and has the candidate form

\[
\left(x_m,\frac{p(x_m+d)}{m},\frac{p(x_m+x_m^2/d)}{m}\right),
\tag{2II}
\]

The reciprocal identity is checked for every guard-satisfying candidate. This
definition reads only \(p,m,d\), not a source state, target state, chart or
unknown solution.

### Odd-gap residue normalization

The displayed guards have a useful exact normalization. Suppose more
generally that \(p\) is prime, \(3\le m\le p-2\),
\(m\equiv3\pmod4\), \(x=(p+m)/4\), and \(de=x^2\). Then

\[
(p,m)=(x,m)=1,
\qquad p\equiv4x\pmod m.
\tag{2N}
\]

Indeed, any common divisor of \(x\) and \(m\) divides
\(4x-m=p\), and it is smaller than \(p\). Thus all four quantities
\(p,x,d,e\) are units modulo \(m\). Consequently the two Type-I
integrality conditions are each equivalent to

\[
e\equiv-4^{-1}\pmod m,
\tag{2I-res}
\]

and the Type-II conditions apart from \(d\le x\) are equivalent to

\[
d\equiv-x\pmod m.
\tag{2II-res}
\]

For Type I, \(m\mid px+d\) is equivalent to
\(d(4e+1)\equiv0\pmod m\), while
\(m\mid x+pe\) is equivalent to \(x(1+4e)\equiv0\pmod m\).
For Type II, \(d\equiv-x\pmod m\) gives
\(de=x^2\equiv-xe\pmod m\), hence also \(e\equiv-x\pmod m\).
This proves that the frozen predicate is exactly a divisor-residue predicate,
including when \(m\) is composite. It is the elementary normal-form
corollary of short-certificate-equivalence; it neither enlarges the
registered schedule nor supplies global terminal coverage.

## Prefix Transport

Let

\[
\mathcal P(p)=\mathcal C_3(p)\cup\mathcal C_7(p)\cup\mathcal C_{11}(p).
\]

The V3 registered-prefix MISS hypothesis is exactly that all three ordered
candidate sets are empty. Since their defining integer data are p-only,

\[
\mathcal P(p)=\varnothing
\tag{3}
\]

is unchanged between the Type-II q=1 root and any target projection of the
same \(4/p\), ROOT_SOL interface that explicitly registers this identical
p-only Bradford predicate. Thus a future target scheduler may prove the same
finite MISS after it binds its own target projection.

Equation (3) is a mathematical transport, not an object conversion. A V3
receipt is bound to a source state and cannot itself be renamed as a
target-projection receipt. The target scheduler must independently bind its
projection ID/digest, replay \(\mathcal P(p)\), and retain

```text
ordered_gaps       = [3, 7, 11]
next_unchecked_gap = 15
global_exhaustion  = false
```

## Anchor-Sink Miss

The target-local anchor-sink family is available only if

\[
R-1\mid K.
\tag{4}
\]

Set \(M=R-1=16t+2\). Then \(16t+1=M-1\), hence

\[
K=X(M-1)\equiv-X\equiv 10t+1\pmod M.
\tag{5}
\]

Because \(0<10t+1<M\), equation (5) already proves \(M\nmid K\). In fact
the stronger statement holds:

\[
\gcd(M,16t+1)=1,
\]

and every common divisor of \(M\) and \(X\) divides

\[
3M-8X=-2.
\]

Since \(X\) is odd, \(\gcd(M,X)=1\), so

\[
\boxed{\gcd(R-1,K)=1.}
\tag{6}
\]

Consequently the anchor-sink certificate

\[
\left(\frac{K}{R-1},K,pK\right)
\]

does not exist for any canonical ordinary q=1 full-carrier phase root. This
is a MISS only for this named anchor-sink family; it says nothing about other
Type-I or Type-II terminal families.

## Consequence

For the finite target schedule

```text
transported Bradford gaps 3, 7, 11
then target-local anchor-sink R-1 | K
```

the registered-prefix MISS premise implies a scope-bound target MISS. The
conclusion has no terminal-leaf authority and cannot act as `MISS_COMPLETE`.
It is a necessary input for a later target-bound terminal receipt after an E2
projection exists, not permission to issue E2 or a successor.

## Controls

For the existing prefix-MISS controls:

| \(p\) | \((R,K)\) | target anchor result | unregistered gap 23 |
|---:|---:|---|---|
| 1201 | \((803,241101)\) | MISS, \(\gcd(802,241101)=1\) | Type I \(d=34\) |
| 2521 | \((1683,1060711)\) | MISS, \(\gcd(1682,1060711)=1\) | Type II \(d=8\) |

The gap-23 certificates are outside the registered scope. Therefore an
extension of the schedule through gap 23 would terminal-first preempt these
two controls; neither can be treated as evidence that gap 23 is universally
empty or universally nonempty.

## Non-Claims

This theorem does not establish a target receipt, target state ID, target
owner, E2--E5, standard E1, producer, branch, persistent admission, queue,
re-entry, complete terminal coverage, F1/F2/F3 closure, T6 totality or the
Erdos-Straus conjecture.
