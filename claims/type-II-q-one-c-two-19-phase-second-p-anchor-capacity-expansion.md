---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-second-p-anchor-capacity-expansion
title: q=1 高 C=2 的 19 相位连续双 p-anchor 容量扩张
statement: >-
  令 p=912u+769 是 q=1 full-carrier d=1 容量二刚性进入的核心素数。记第一条
  p-anchor 完整超额 action 的 support、capacity 为 M_1=M_0Q_0、
  c_1=(2p+4)/3，且 K_1=M_1c_1、R_1=(4K_1-1)/p。则
  gcd(R_1-1,K_1)=2、v_2(R_1-1)=1，故第二个 p-anchor 的唯一完整超额块为
  Q_1=(R_1-1)/2，且 gcd(Q_1,M_1)=1、p 不整除 Q_1。它给出的 canonical
  capacity 精确为 c_2=(13p+16)/19，并严格满足
  2<c_1<c_2<p。因此该 19 相位的确定性连续双 p-anchor complete-excess 路径在
  前两步均严格扩张容量，不能提供 strict capacity descent。此结论不排除独立
  Type I/II terminal certificate、其它 anchor 或跨图表 action。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-p-anchor-capacity-expansion
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
  - claim: type-II-q-one-c-two-19-phase-p-anchor-capacity-expansion
    role: first-p-anchor-support-capacity-and-complete-excess-receipt
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: chart-local-p-source-to-anchor-contract
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: canonical-carry-capacity-formula
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_second_p_anchor_capacity_expansion.py
    role: exact-polynomial-gcd-and-double-capacity-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的连续双 p-anchor 容量扩张

## 1. Input and the second anchor chart

Fix the high \(C=2\) entrance

\[
p=912u+769,
\qquad
F=2p^2-3p-1,
\qquad
M_0=\frac{(p-1)(2p+1)F}{8}.
\tag{1}
\]

The first p-anchor result supplies

\[
R_0=4p^3-8p^2-p+4,
\qquad
Q_0=\frac{R_0-1}{2},
\tag{2}
\]

and its canonical target is

\[
M_1=M_0Q_0,
\qquad
c_1=\frac{2p+4}{3},
\qquad
K_1=M_1c_1,
\qquad
R_1=\frac{4K_1-1}{p}.
\tag{3}
\]

Here the quantities in (3) are integral.  Eliminating the intermediate
support gives the useful closed forms

\[
K_1=
\frac{(p-1)(p+2)(2p+1)F(R_0-1)}{24},
\tag{4}
\]

\[
R_1=
\frac{16p^7-32p^6-72p^5+156p^4+37p^3-117p^2-19p+25}{6}.
\tag{5}
\]

In particular,

\[
R_1\equiv\frac{25}{6}\pmod p,
\qquad
R_1-1\equiv\frac{19}{6}\pmod p.
\tag{6}
\]

The latter residue is nonzero because the present primes are not \(19\).
Thus the second p-anchor candidate is again p-free; this is not inferred from
a finite sample.

## 2. The second complete-excess block is again forced

Put

\[
N=6(R_1-1),
\qquad
H=R_0-1.
\tag{7}
\]

Direct polynomial division from (5) gives

\[
\begin{aligned}
N&\equiv-12 &&\pmod {p-1},\\
N&\equiv 6 &&\pmod {2p+1},\\
N&\equiv-12(p-1) &&\pmod F,\\
N&\equiv8(p^2-2p-1) &&\pmod H,\\
N&\equiv-3 &&\pmod {p+2}.
\end{aligned}
\tag{8}
\]

For the two non-linear factors, the needed elimination identities are

\[
F\equiv-2\pmod {p-1},
\tag{9}
\]

\[
-(p-3)H+(4p^2-12p+3)(p^2-2p-1)=6.
\tag{10}
\]

Let \(\ell\) be an odd common prime divisor of \(R_1-1\) and \(K_1\).
If \(\ell\ne3\), then \(\ell\mid N\), and (4), (8) force it through one
of the five factors in (4).  The linear-factor remainders exclude it
immediately.  If it enters through \(F\), then (8) first forces
\(\ell\mid p-1\), contradicting (9).  If it enters through \(H\), then
(8) forces \(\ell\mid p^2-2p-1\), and (10) gives \(\ell\mid6\), again a
contradiction.  Hence only \(\ell=3\) remains as a formal possibility.

Write \(p=1+24v\).  Substitution into (5) has the form

\[
R_1=-1+24T(v),\qquad T(v)\in\mathbb Z[v].
\tag{11}
\]

Therefore \(R_1-1\equiv-2\pmod {24}\): it has 2-adic valuation exactly
one and is not divisible by \(3\).  Since \(p\equiv1\pmod8\), the factor
\(F\) has 2-adic valuation one, so \(M_0\), hence \(M_1\), is even; also
\(c_1=2(p+2)/3\) is even.  Thus \(K_1\) is even.  We obtain the exact identity

\[
\boxed{\gcd(R_1-1,K_1)=2.}
\tag{12}
\]

Consequently the second anchor has one deterministic complete-excess block,

\[
\boxed{Q_1=\frac{R_1-1}{2},\qquad \beta_1=2,\qquad (Q_1,M_1)=1,
\qquad p\nmid Q_1.}
\tag{13}
\]

## 3. The second canonical target expands again

Equation (13) gives \(M_2=M_1Q_1\).  Modulo \(p\), equations (3) and (6)
give

\[
c_1\equiv\frac43,
\qquad
Q_1\equiv\frac{19}{12}.
\tag{14}
\]

Thus its canonical cofactor obeys

\[
c_2\equiv c_1Q_1^{-1}\equiv\frac{16}{19}\pmod p.
\tag{15}
\]

Because \(p\equiv9\pmod {19}\), the representative in
\(\{1,\ldots,p-1\}\) is

\[
\boxed{c_2=\frac{13p+16}{19}.}
\tag{16}
\]

It lies above the first capacity by the exact amount

\[
c_2-c_1=\frac{p-28}{57}>0,
\tag{17}
\]

and \(c_2<p\).  The deterministic two-action chart-local path is therefore

\[
\boxed{
2\ \longmapsto\ \frac{2p+4}{3}
\ \longmapsto\ \frac{13p+16}{19},
}
\tag{18}
\]

with strict increase at both arrows.  This closes the two consecutive
canonical p-anchor complete-excess actions as candidates for the required
strict capacity descent.  It does not establish that no other terminal or
cross-chart route exists.

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_second_p_anchor_capacity_expansion.py --verify
```
