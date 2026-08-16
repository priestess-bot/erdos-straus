---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-reentry-rho-one-p-primary-exclusion
title: H4 q0=1 第二 re-entry 的 rho=1 p-primary 排除
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 clean
  q bridge 的 q0=1 second-stutter unitary transduction 中，若 rho=gcd(q,2T/q)=1
  且 second top-capacity target 留在 a2=1，则 qhat=q 并有 attached primitive raw
  re-entry (xi,zeta)=(x2/q,R4-x2/q)。两个 endpoint 都 p-free。事实上 actual H4
  carry 给 h=2d、p=2qd-1；若 p divides zeta，则
  p divides q^3-q^2+1-2d。乘以 q 后得到 p divides
  (q-1)(q+1)(q^2-q+1)。因为 p>q+1 且 p=-1 (mod q)，必有
  q^2-q+1=(q-1)p，进而 q=2d(q-1)，这与 q>=3、d>=1 矛盾。
  该结论不处理 rho>1 unitary allocation、第三 q carrier、p-free payload 的 typed/
  terminal/serializer guards 或其容量门。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-p-primary-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - a-one
  - q0-one
  - double-q-carrier
  - raw-path
  - p-primary
  - p-free
  - complete-excess-bundle
  - unitary-divisor
  - capacity-map
  - solution-lift
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
    role: rho-one-raw-reentry-and-second-stutter-contract
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
    role: actual-p-free-second-endpoint-and-double-q-geometry
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-p-primary-exclusion
    role: actual-H4-carry-h-equals-two-d
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: clean-q-primitive-word-convention
  - concept: denominator-escape-state-contract
    role: guarded-p-free-dispatch-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_second_stutter_unitary_transduction.py
    role: rho-one-p-primary-factorization-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0=1\) 第二 re-entry 的 \(\rho=1\) p-primary 排除

## 1. 范围

保留 actual H4 proper-overlap top-capacity \(a_{\rm alt}=1\) clean \(q\)-bridge 的
\(q_0=1\) double-\(q\) endpoint。写

\[
w=\frac{p+1}{2}=qd,
\qquad
h=2d,
\qquad
p=2qd-1.
\tag{1}
\]

这里 \(h=2d\) 是 actual H4 carry 与 clean-\(q\) 的结论。设 second capacity
stutter 已落在 \(a_2=1\)，并使用其 unitary carrier 记号

\[
\rho=\left(q,\frac{2T}{q}\right),
\qquad
\widehat q=\frac q\rho.
\tag{2}
\]

本卡只处理

\[
\boxed{\rho=1.}
\tag{3}
\]

于是 \(\widehat q=q\)。既有 second-stutter transduction 给 \(q\mid x_2\)，并把同一
actual H4 prefix 实际延伸为 primitive raw word

\[
\boxed{
\{x_2,y_2\}
\rightsquigarrow
\{\xi,\zeta\}:=
\left\{\frac{x_2}{q},R_4-\frac{x_2}{q}\right\}.
}
\tag{4}
\]

此前已知 \(p\nmid x_2y_2\)，而 \(q<p\)，故

\[
p\nmid\xi.
\tag{5}
\]

下面只排除另一坐标 \(\zeta\) 的 \(p\)-block；它不把 (4) 自动登记为 persistent
macro。

## 2. p-primary 会强制一个固定因子式

double-\(q\) endpoint 满足

\[
q^2y_2=R_4-h,
\qquad
x_2+y_2=R_4.
\tag{6}
\]

再用 \(x_2=q\xi\)，得到 exact re-entry identity

\[
\boxed{(q^2-1)R_4=q^3\xi-h.}
\tag{7}
\]

若反设 \(p\mid\zeta\)，则 \(R_4\equiv1\pmod p\) 给 \(\xi\equiv1\pmod p\)。将其
代入 (7)，再使用 (1)，得到必要条件

\[
\boxed{p\mid N:=q^3-q^2+1-2d.}
\tag{8}
\]

这个条件已经与任何 complete-excess support 的选择无关。把 (8) 乘以 \(q\)，并用
\(2qd=p+1\)，有精确恒等式

\[
\begin{aligned}
qN
&=q^4-q^3+q-p-1\\
&=\underbrace{(q-1)(q^3+1)}_{=(q-1)(q+1)(q^2-q+1)}-p.
\end{aligned}
\tag{9}
\]

故 (8) 强制

\[
p\mid(q-1)(q+1)(q^2-q+1).
\tag{10}
\]

但 \(q\ge3\)、\(d\ge1\) 给

\[
p=2qd-1>q+1,
\tag{11}
\]

所以 \(p\) 不能整除前两个因子。因此

\[
q^2-q+1=mp
\tag{12}
\]

对某个正整数 \(m\)。又 \(p>q\) 使 \(0<m<q\)，而 \(p\equiv-1\pmod q\)，所以

\[
1\equiv q^2-q+1\equiv mp\equiv-m\pmod q.
\tag{13}
\]

唯一可能是 \(m=q-1\)。代回 (12) 和 (1)，得到

\[
q^2-q+1=(q-1)(2qd-1)
\quad\Longrightarrow\quad
q=2d(q-1),
\tag{14}
\]

但右端至少为 \(2(q-1)>q\)。矛盾。

## 3. 后果与边界

故 (8) 不可能，结合 (5) 得

\[
\boxed{p\nmid\xi\zeta.}
\tag{15}
\]

所以 \(\rho=1\) 的 second-stutter \(a_2=1\) actual re-entry 不会重新打开
\(p\)-primary residual；它只剩 Type I terminal、p-free single-side/atomic payload、
容量以及语义 guards 的分派。

本证明没有使用有限 phase factor screen，也没有处理 \(\rho>1\) 的 proper-unitary
allocation；后者仍可能有不同的 \(p\)-primary 几何。它同样不证明 p-free payload 已通过
terminal-first、typed、source/path、serializer 或 persistent contract。

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_second_stutter_unitary_transduction.py --verify
```

回执只核对 (9) 的因式式与两个小数值控制；全称排除由第 2 节的整数反证完成，不依赖
prime-range、denominator 或 Reach 扫描。
