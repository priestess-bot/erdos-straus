---
kind: claim
claim_id: type-I-f2-high-support-r-three-raw-menu-and-external-rechart-boundary
title: F2 high-support R=3 raw-menu obstruction and C>1 external-rechart lock
statement: >-
  In the C=1 R=3 hard core, the universal raw source has a complete non-p
  first-label menu indexed by the prime divisors of D=2p-3. A non-anchor
  first step exists exactly when D is composite; the core prime p=2521 has
  D=5039 prime, so hard-core arithmetic cannot supply a universal non-anchor
  raw exit. Separately, for an actual high-support C>1 chart, every current
  full-excess external rechart M=lcm(A,Q)>A remains TYPEI/CHARGED overflow;
  on the empty-improvement leaf its cofactor cannot give LOCAL_DROP. Neither
  result constructs E1 for the original parent, an admitted successor, or a
  terminal certificate.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f2-high-support-c1-r-three-anchor-no-reentry
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-raw-universal-p-parent-root-policy-boundary
  - type-I-high-support-rank-aware-sink-bundle-selector
topics:
  - type-I
  - F2
  - high-support
  - C-one
  - C-greater-than-one
  - R-three
  - raw-source
  - complete-excess
  - overflow
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_f2_high_support_r_three_raw_menu_boundary.py
    role: exact hard-core prime and composite-D menu controls
  - claim: type-I-f2-high-support-c1-r-three-anchor-no-reentry
    role: canonical-anchor re-entry exclusion
  - claim: type-I-high-support-rank-aware-sink-bundle-selector
    role: empty-improvement rank comparison
visibility: public
last_checked: '2026-08-25'
---

# F2 high-support R=3 raw-menu obstruction and C>1 external-rechart lock

## 1. R=3 hard core has no universal non-anchor first edge

Let \(p\equiv1\pmod {24}\) be a core prime in the remaining \(C=1\) hard
core, put

\[
P=p+4,\qquad N=\frac{3p+1}{4},\qquad D=2p-3,
\tag{1}
\]

and assume

\[
q\mid P\Longrightarrow q\equiv1\pmod4,
\qquad
q\mid N\Longrightarrow q\equiv1\pmod3.
\tag{2}
\]

The associated low chart is \((p,3,N;N)\), and its universal raw source is

\[
S=(p,D,p-1).
\tag{3}
\]

First,

\[
8N-3D=11.
\tag{4}
\]

Thus any common divisor of \(D\) and \(N\) divides \(11\). If \(11\mid D\),
then \(p\equiv7\pmod {11}\), hence \(11\mid P\), contradicting (2) because
\(11\equiv3\pmod4\). Therefore

\[
\boxed{(D,N)=1.}
\tag{5}
\]

The current universal-source raw rule consequently has precisely the following
non-\(p\) first labels: every prime \(q\mid D\). Writing \(a=D/q\), its exact
raw image is

\[
(p,D,p-1)
\xrightarrow q
\left(a,\frac{a+3}{2},\frac{a+1}{2}\right).
\tag{6}
\]

There is no gcd reduction: \(q\ne3\), \(3\nmid D\), and
\(\gcd(a,(a+3)/2)=1\). The image is the canonical anchor exactly when \(q=D\).
Hence a non-anchor first step exists if and only if \(D\) is composite.

The control

\[
p=2521,\quad P=5^2\cdot101,\quad N=31\cdot61,\quad D=5039
\tag{7}
\]

satisfies (2), while \(D\) is prime. Its only non-\(p\) step is
\((1,2,1)\), the canonical anchor. Thus the proposed universal implication

```text
R=3 hard core -> universal source has a non-anchor first raw edge
```

is false. This is deliberately only a raw-menu control, not a claim that the
control survives terminal-first or witnesses any conjectural failure. It rules
out this particular proof strategy. A different inherited source, a Type-II
terminal, or a new non-bottom projection is not excluded.

## 2. Current C>1 external rechart cannot become a phase or rank exit

Let an actual high-support Type-I/CHARGED chart satisfy

\[
K=AC,\qquad A>B_p:=\frac{(p-1)^2}{4},\qquad C>1,
\tag{8}
\]

and let a current full-excess receipt have

\[
M=\operatorname{lcm}(A,Q)>A,
\qquad K_M=Mc_M,
\qquad R_M=\frac{4K_M-1}{p}.
\tag{9}
\]

If \(R_M<p\), then \(R_M\equiv3\pmod4\) gives \(R_M\le p-2\), so

\[
K_M=\frac{pR_M+1}{4}\le B_p.
\tag{10}
\]

But \(K_M\ge M>A>B_p\), a contradiction. Therefore

\[
\boxed{R_M>p.}
\tag{11}
\]

The rechart remains a `TYPEI/CHARGED` overflow rather than an ABSORB phase
drop. On the empty-improvement leaf the rank-aware selector has \(c_M\ge C\).
With the unchanged \(\eta_p\) payload, the relevant charged tuple cannot
strictly decrease:

\[
(p,2,4,0,c_M,\eta_p,0)
\not<
(p,2,4,0,C,\eta_p,0).
\tag{12}
\]

Hence this rechart has no `LOCAL_DROP` ticket except when a terminal rule
preempts it. The result does not exclude a new Type-II terminal, direct
cofactor route, non-bundle raw carrier, or a separately proved protocol/E5
producer.
