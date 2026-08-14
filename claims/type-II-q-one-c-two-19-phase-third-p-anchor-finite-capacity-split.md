---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-third-p-anchor-finite-capacity-split
title: q=1 高 C=2 的 19 相位第三 p-anchor 有限容量分裂
statement: >-
  令 p=912u+769 是 q=1 full-carrier d=1 容量二刚性进入的核心素数，并连续执行前两条
  canonical p-anchor complete-excess action。第二个 target 的 residual R_2 与 carrier
  K_2 满足 gcd(R_2-1,K_2)=2、v_2(R_2-1)=1、p 不整除 (R_2-1)/2，故第三条
  p-anchor 仍有唯一完整超额块 Q_2=(R_2-1)/2。其 canonical capacity 为
  c_3=(1536+a(p)p)/2261，其中 a(p) 是 1,...,2260 中满足
  a(p)p=-1536 (mod 2261) 的唯一整数。对所有可为素数的 u (mod 119)，
  a(p)=13+19k，0<=k<=118，且 k 不等于 3 (mod 7)、2 (mod 17)。该有限 selector
  有 96 个允许类；恰有 64 类满足 c_3<c_2，另 32 类满足 c_3>c_2。因而第三条
  p-anchor 既不是全称扩张，也不是全称严格递降；它提供一个精确、可检索的参数依赖
  容量分裂。该结论仍不构成 global solution lift 或全局良基势。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-second-p-anchor-capacity-expansion
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
  - finite-selector
  - congruence-split
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-second-p-anchor-capacity-expansion
    role: first-two-p-anchor-charts-and-capacities
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: chart-local-p-source-to-anchor-contract
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: canonical-carry-capacity-formula
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_third_p_anchor_finite_capacity_split.py
    role: exact-polynomial-gcd-and-finite-selector-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的第三 p-anchor 有限容量分裂

## 1. Third-anchor carrier

Continue the notation of the preceding two p-anchor actions.  Thus

\[
p=912u+769,
\qquad
F=2p^2-3p-1,
\qquad
H=R_0-1=4p^3-8p^2-p+3,
\tag{1}
\]

and set

\[
N_1=6(R_1-1).
\tag{2}
\]

After the second complete-excess action, the carrier and residual are

\[
K_2=M_2c_2
=\frac{(p-1)(2p+1)(13p+16)FHN_1}{3648},
\qquad
R_2=\frac{4K_2-1}{p}.
\tag{3}
\]

The source is again primitive and the next block is p-free, because direct
reduction gives

\[
R_2\equiv\frac{3173}{912}\pmod p,
\qquad
R_2-1\equiv\frac{2261}{912}\pmod p,
\tag{4}
\]

where

\[
3173=19\cdot167,
\qquad
2261=7\cdot17\cdot19.
\tag{5}
\]

None of these odd factors can equal a core prime in (1).

## 2. The third complete-excess block is forced

Put \(N_2=912(R_2-1)\) and

\[
U=16p^6-32p^5-72p^4+156p^3+37p^2-117p-38.
\tag{6}
\]

Exact polynomial division gives

\[
\begin{aligned}
N_2&\equiv-1824 &&\pmod {p-1},\\
N_2&\equiv 912 &&\pmod {2p+1},\\
N_2&\equiv-171 &&\pmod {13p+16},\\
N_2&\equiv-1824(p-1) &&\pmod F,\\
N_2&\equiv1216(p^2-2p-1) &&\pmod H,\\
N_2&\equiv48U &&\pmod {N_1}.
\end{aligned}
\tag{7}
\]

The two earlier elimination identities remain available,

\[
F\equiv-2\pmod {p-1},
\tag{8}
\]

\[
-(p-3)H+(4p^2-12p+3)(p^2-2p-1)=6,
\tag{9}
\]

while the final degree-seven factor has the short relation

\[
N_1=pU+19(p+1),
\qquad
N_1\equiv64\pmod {p+1}.
\tag{10}
\]

Let \(\ell\) be an odd common prime divisor of \(R_2-1\) and \(K_2\).
For \(\ell\notin\{3,19\}\), the denominator in (3) is harmless, and
(7) sends \(\ell\) into one of the six displayed factors.  The three
linear remainders exclude it.  The \(F\) and \(H\) cases reduce using
(8)--(9), exactly as in the second-anchor proof.  In the \(N_1\) case,
(7) gives \(\ell\mid U\); then (10) gives \(\ell\mid p+1\), and its
second identity forces \(\ell\mid64\), a contradiction.

The two deferred primes are excluded uniformly by the phase congruences

\[
R_2\equiv-1\pmod {24},
\qquad
R_2\equiv2\pmod {19}.
\tag{11}
\]

Both follow by substituting \(p=912u+769\) into (3) after cancellation.
Hence \(R_2-1\) is neither divisible by \(3\) nor by \(19\), has exact
2-adic valuation one, and \(K_2\) is even.  Therefore

\[
\boxed{\gcd(R_2-1,K_2)=2.}
\tag{12}
\]

The third p-anchor has the unique complete-excess data

\[
\boxed{Q_2=\frac{R_2-1}{2},\qquad \beta_2=2,\qquad (Q_2,M_2)=1,
\qquad p\nmid Q_2.}
\tag{13}
\]

## 3. An exact finite selector for the third capacity

The preceding capacity is

\[
c_2=\frac{13p+16}{19}\equiv\frac{16}{19}\pmod p.
\tag{14}
\]

Together with (4), it yields

\[
c_3\equiv c_2Q_2^{-1}
\equiv\frac{16}{19}\frac{1824}{2261}
=\frac{1536}{2261}\pmod p.
\tag{15}
\]

For a phase prime, \((p,2261)=1\).  Define \(a(p)\) as the unique integer
in \(\{1,\ldots,2260\}\) satisfying

\[
a(p)p\equiv-1536\pmod {2261}.
\tag{16}
\]

Then the standard canonical representative is

\[
\boxed{c_3=\frac{1536+a(p)p}{2261}.}
\tag{17}
\]

It is indeed between \(1\) and \(p-1\).  To make (17) searchable without
large integer factorization, write \(a(p)=13+19k\).  As \(u\) varies
modulo \(119=7\cdot17\), a phase prime must avoid

\[
u\equiv4\pmod7,
\qquad
u\equiv12\pmod {17},
\tag{18}
\]

because those are exactly the classes for which \(p\) is divisible by
\(7\) or \(17\).  The remaining classes map bijectively under (16) to

\[
\boxed{
0\le k\le118,
\qquad
k\not\equiv3\pmod7,
\qquad
k\not\equiv2\pmod {17}.
}
\tag{19}
\]

There are \(119-17-7+1=96\) such classes.  The capacity direction is

\[
c_2-c_3=\frac{(1547-a(p))p+368}{2261}.
\tag{20}
\]

Thus \(c_3<c_2\) exactly when \(a(p)\le1547\), equivalently \(k\le80\).
Among \(k=0,\ldots,80\), the exclusions in (19) remove 12 and 5 values
with no overlap, leaving 64.  The remaining 32 permitted classes have
\(c_3>c_2\).  There is no equality case.

For a concrete descent-side control, \(p=15361\) has \(u=16\),
\(a(p)=13\), and

\[
(c_1,c_2,c_3)=(10242,10511,89).
\tag{21}
\]

This is a strict chart-local capacity drop, not yet a global descent: the
support has grown through all three complete-excess blocks, and no solution
lift or global well-founded potential has been proved.

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_third_p_anchor_finite_capacity_split.py --verify
```
