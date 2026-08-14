---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-fixed-template-obstruction
title: q=1 高 C=2 的 19 相位固定 Type I/II 模板阻碍
statement: >-
  令 p_u=912u+769。q=1 full-carrier d=1 容量二刚性所给的每个核心素数
  p=p_u 都满足 p=9 (mod 19)。因此不存在以 h=19=4ACK-1 为 defining factor 的
  Type II AC raw ray h|Kp+A：ACK=5 的三种可能 (A,C,K) 都使 Kp+A 非零模 19。
  更强地，在整个仿射 progression p_u 上不存在固定 Type I normal-form template
  (A,B,m)（C_u 随 u 变化）或固定 Type II AC-ray template (A,C,K)（B_u 随 u
  变化），其整除条件对每个 u 恒成立。前者由 m 只能为 3 或 19 后与
  AB|gcd(228,(769+m)/4)=1 矛盾；后者由 h=4ACK-1 必整除 912，故 h 只能为 3 或 19，
  而 base point p_0=769 排除两者。此外，若固定 Type II gap m 与因子对 (A,B) 并只令
  C_u 变化，要求标准两尾 lift 对每个 u 都有 n<p 会强制 m+1|48；六个可能 gap 的
  common support g_m 都满足 g_m+1<m，故 m 不能整除 A+B。该结果只排除参数无关的
  整条同余类恒等式与固定 gap 的统一严格 lift，不排除随 p 选择的 Type I/II 证书、有限菜单
  按更细 residue 分派，或严格可提升递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-d-one-capacity-two-rigidity
  - type-I-coprime-factor-normal-form
  - type-II-coprime-factor-normal-form
  - type-II-factor-pair-carrier-strict-descent
  - type-II-raw-ray-certificate
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - high-support
  - nineteen-phase
  - fixed-template
  - ac-ray
  - terminal
  - strict-no-go
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-d-one-capacity-two-rigidity
    role: p-equals-912u-plus-769-high-c-two-phase-input
  - claim: type-I-coprime-factor-normal-form
    role: fixed-type-i-template-normal-form
  - claim: type-II-coprime-factor-normal-form
    role: fixed-type-ii-ac-ray-normal-form
  - claim: type-II-factor-pair-carrier-strict-descent
    role: aligned-fixed-gap-type-ii-lift-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_fixed_template_obstruction.py
    role: exact-finite-divisor-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的固定模板阻碍

## 1. The residual progression

The capacity-two rigidity theorem puts the only q=1 immediate \(d=1\)
entrance into the progression

\[
p_u=912u+769,\qquad p_u\equiv9\pmod {19}.
\tag{1}
\]

This card asks a deliberately narrower question than a global terminal
selector: can a single normal-form certificate identity close every member of
this progression?  The answer is no for both Type I and Type II templates.
The distinction matters: the result does **not** say that a particular prime
\(p_u\) lacks a certificate.

## 2. The phase prime 19 cannot be a Type II ray factor

In the AC-ray normal form, a Type II ray with defining factor \(h\) has

\[
h=4ACK-1,
\qquad h\mid Kp+A.
\tag{2}
\]

Suppose \(h=19\).  Then \(ACK=5\), so the only positive triples
\((A,C,K)\) are

\[
(1,1,5),\qquad(1,5,1),\qquad(5,1,1).
\tag{3}
\]

For \(p\equiv9\pmod {19}\), their three ray residues are respectively

\[
5p+1\equiv8,\qquad p+1\equiv10,\qquad p+5\equiv14\pmod {19}.
\tag{4}
\]

None is zero.  Hence:

\[
\boxed{\text{No }p\equiv9\pmod {19}\text{ has a Type II AC ray whose
defining factor is }19.}
\tag{5}
\]

In particular, the forced \(q_\star=19\) of the q=1 high \(C=2\) macro
cannot simply be recycled as the direct Type II ray factor.  Other factors
\(h\), and all Type I certificates, remain possible.

## 3. No uniform Type II AC ray on the progression

Fix positive \(A,C,K\), write

\[
h=4ACK-1,
\tag{6}
\]

and suppose the AC divisibility condition in (2) holds for every integer
\(u\ge0\).  Comparing adjacent values of \(u\) gives

\[
h\mid912K.
\tag{7}
\]

But \(h\equiv-1\pmod K\), hence \((h,K)=1\), and therefore

\[
h\mid912=2^4\cdot3\cdot19.
\tag{8}
\]

Since \(h\equiv3\pmod4\), its only possible values are

\[
h\in\{3,19\}.
\tag{9}
\]

For \(h=3\), necessarily \(A=C=K=1\), but

\[
Kp_0+A=770\not\equiv0\pmod3.
\tag{10}
\]

For \(h=19\), (4) gives the contradiction.  Thus no fixed \((A,C,K)\)
AC ray is valid identically on (1).  In particular, no such ray can provide a
uniform direct Type II terminal or an aligned \(n<p\) Type II lift for this
whole progression.

## 4. No uniform Type I normal-form template

Fix a Type I normal-form template \((A,B,m)\), with \((A,B)=1\), while
allowing only

\[
C_u=\frac{p_u+m}{4AB}
\tag{11}
\]

to vary.  For it to be a legal Type I certificate identity on all \(u\), its
normal-form conditions are

\[
4AB\mid p_u+m,
\qquad m\mid Bp_u+A,
\qquad m\equiv3\pmod4.
\tag{12}
\]

Adjacent \(u\)'s imply

\[
AB\mid228,
\qquad m\mid912B.
\tag{13}
\]

The gap \(m\) is odd.  If either \(3\) or \(19\) divides \(B\), it cannot
divide \(Bp_0+A\), by \((A,B)=1\).  As the odd part of \(912\) is
\(3\cdot19\), (13) therefore forces

\[
m\mid57,\qquad m\equiv3\pmod4,
\qquad\text{so }m\in\{3,19\}.
\tag{14}
\]

If \(m=3\), then (12) at \(u=0\) gives

\[
AB\mid\frac{769+3}{4}=193.
\tag{15}
\]

Together with \(AB\mid228\), this gives \(AB=1\), but then

\[
3\nmid Bp_0+A=770.
\tag{16}
\]

If \(m=19\), the same argument uses

\[
AB\mid\frac{769+19}{4}=197,
\tag{17}
\]

again forcing \(AB=1\), while \(19\nmid770\).  This proves that no fixed
Type I normal-form template is an identity on the whole progression.

## 5. No uniform aligned fixed-gap Type II descent template

There is another apparently simple terminal route not covered by a fixed AC
ray: keep a Type II gap \(m\) and factor pair \((A,B)\) fixed, and allow only
the remaining factor \(C_u\) of

\[
x_u=\frac{p_u+m}{4}=ABC_u
\tag{18}
\]

to vary.  If this template is to give the standard strict two-tail lift for
every \(u\), then \(m+1\mid p_u-1\) identically.  Hence

\[
m+1\mid\gcd(768,912)=48.
\tag{19}
\]

The legal positive gaps are exactly

\[
m\in\{3,7,11,15,23,47\}.
\tag{20}
\]

For a fixed factor pair, \(AB\) divides every \(x_u\), so it divides

\[
g_m:=\gcd\!\left(228,\frac{769+m}{4}\right).
\tag{21}
\]

The six exact values are

\[
\begin{array}{c|rrrrrr}
m&3&7&11&15&23&47\\ \hline
g_m&1&2&3&4&6&12.
\end{array}
\tag{22}
\]

For positive \(A,B\), \(A+B\le AB+1\).  Thus (21)--(22) give

\[
0<A+B\le g_m+1<m.
\tag{23}
\]

But a Type II normal form requires \(m\mid A+B\), a contradiction.  Hence
there is no fixed \((m,A,B)\) factor-pair template that supplies an aligned
strict \(n<p\) Type II descent throughout (1).  As before, this does not
exclude a parameter-dependent gap or factor pair.

## 6. Exact scope

The argument intentionally uses adjacent *integer* parameters in the ambient
affine progression.  It therefore rules out a parameter-independent congruence
identity, not a selector that chooses different data at different prime
parameters.  It also does not rule out a finite menu that is dispatched by a
strictly finer residue condition.  The remaining meaningful routes for the
high \(C=2\) phase are consequently a genuinely parameter-dependent
certificate/terminal construction or a strict lift-preserving descent.

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_fixed_template_obstruction.py --verify
```
