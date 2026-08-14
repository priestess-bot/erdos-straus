---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-p-anchor-capacity-expansion
title: q=1 高 C=2 的 19 相位 p-anchor 完整超额容量扩张
statement: >-
  令 p=912u+769 是 q=1 full-carrier d=1 容量二刚性进入的核心素数。其 high C=2
  target 的 support、residual 和 cofactor 为
  M=(p-1)(2p+1)(2p^2-3p-1)/8、R=4p^3-8p^2-p+4、K=2M。
  有 gcd(R-1,K)=2、v_2(R-1)=1<v_2(K)，故 p-source anchor 的唯一完整超额块为
  Q=(R-1)/2、beta=2，且 gcd(Q,M)=1、p 不整除 Q。因而 canonical p-source bundle
  的 support 严格扩张为 MQ，其下一个 canonical cofactor 精确为
  c_1=(2p+4)/3>2。这个 action 具有 chart-local raw p-source 和 p-free bundle
  receipt，但容量从 2 严格上升到 c_1，不能充当本相位的严格容量递降。该结论不排除
  terminal-first 的独立 Type I/II 证书、其它 raw/bottom anchor，或跨图表下降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-d-one-capacity-two-rigidity
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - high-support
  - nineteen-phase
  - p-anchor
  - complete-excess
  - capacity-map
  - strict-counterexample
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-d-one-capacity-two-rigidity
    role: high-c-two-phase-input-and-closed-form-support
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: chart-local-p-source-to-anchor-contract
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: canonical-carry-capacity-formula
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_p_anchor_capacity_expansion.py
    role: exact-polynomial-and-capacity-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的 p-anchor 容量扩张

## 1. The high \(C=2\) chart

On the q=1 capacity-two entrance, put

\[
p=912u+769,
\qquad
M=\frac{(p-1)(2p+1)(2p^2-3p-1)}8.
\tag{1}
\]

The preceding rigidity result gives the canonical high-support chart

\[
K=2M,
\qquad
R=\frac{8M-1}{p}=4p^3-8p^2-p+4.
\tag{2}
\]

In particular, \(R\equiv4\pmod p\), so the universal \(p\)-source is
primitive and reaches the usual anchor \((1,R-1,1)\).  This section concerns
the deterministic complete-excess block at that particular anchor.

## 2. The complete-excess block is forced

Write

\[
F=2p^2-3p-1,
\qquad
K=\frac{(p-1)(2p+1)F}{4}.
\tag{3}
\]

The following three identities control every odd common divisor of \(R-1\)
and \(K\):

\[
R-1\equiv-2\pmod {p-1},
\tag{4}
\]

\[
R-1=(2p+1)(2p^2-5p+2)+1,
\tag{5}
\]

\[
R-1=(2p-1)F-2(p-1).
\tag{6}
\]

If an odd prime divides both \(F\) and \(R-1\), (6) makes it divide
\(p-1\); but then \(F\equiv-2\pmod {p-1}\), a contradiction.  Equations
(4)--(6) therefore exclude every odd common prime factor of \(R-1\) and
\(K\).

Since \(p\equiv1\pmod4\),

\[
R-1\equiv2\pmod4,
\qquad
v_2(K)\ge2.
\tag{7}
\]

Consequently

\[
\boxed{\gcd(R-1,K)=2.}
\tag{8}

The factor 2 is not excess, while every odd prime block of \(R-1\) is fully
excess.  Thus the complete-excess data at the p-anchor is exactly

\[
\boxed{Q=\frac{R-1}{2},\qquad \beta=2.}
\tag{9}

Because \(Q\) is odd, (8) also yields

\[
\boxed{(Q,M)=1.}
\tag{10}

Finally \(R-1\equiv3\pmod p\), so \(p\nmid Q\).  The p-source and p-free
gates therefore both pass without a repair.

## 3. The canonical target expands capacity

By (10), the bundle support is

\[
M_1=\operatorname{lcm}(M,Q)=MQ.
\tag{11}

Let \(c_1\in\{1,\ldots,p-1\}\) be its canonical cofactor.  From the
source chart, \(4M\cdot2\equiv1\pmod p\); hence

\[
c_1\equiv2Q^{-1}\pmod p.
\tag{12}

Using \(Q\equiv(R-1)/2\equiv3/2\pmod p\), this becomes

\[
c_1\equiv\frac43\pmod p.
\tag{13}

As \(p\equiv1\pmod3\), the standard representative is

\[
\boxed{c_1=\frac{2p+4}{3}.}
\tag{14}

For every core prime here, \(2<c_1<p\).  Therefore the deterministic
p-anchor action has the strict capacity direction

\[
\boxed{2\longmapsto\frac{2p+4}{3}>2.}
\tag{15}

It is an exact capacity map and a valid chart-local raw/bundle receipt, but
not a strict capacity descent.  No conclusion is drawn about a different
terminal certificate, a different bottom-node bundle, or a cross-chart
operation.

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_p_anchor_capacity_expansion.py --verify
```
