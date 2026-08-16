---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-third-q-d-one-p-primary-exclusion
title: H4 q0=1 第三 q carrier 的 d=1 p-primary 排除
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 clean
  q bridge 的 q0=1 second-stutter transduction 中，若 rho=q（等价于 qhat=1），则
  q^3 divides Q_K4(z) divides z，故有第三条 actual primitive q raw word
  (x3,y3)=(R4-z/q^3,z/q^3)。若 d=gcd((p+1)/2,M4)=1，则 h=2、p=2q-1；
  该第三 endpoint 全部 p-free。因为 p divides x3 会强制
  p divides q^3+1=(q+1)(q^2-q+1)，而 p>q+1、p=-1 (mod q) 迫使
  q^2-q+1=(q-1)p，继而 q=2(q-1)，与 q>=3 矛盾。该结论不处理 d>1 的
  third carrier，也不自动支付 terminal/typed/payload/serializer guards。
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
  - triple-q-carrier
  - raw-path
  - p-primary
  - p-free
  - complete-excess-bundle
  - capacity-map
  - solution-lift
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-second-stutter-unitary-transduction
    role: rho-equals-q-third-carrier-existence
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q0-one-double-q-bridge
    role: double-q-geometry-and-original-p-free-bundle
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-q0-reentry-p-primary-exclusion
    role: actual-H4-carry-h-equals-two-d
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: clean-q-primitive-word-convention
  - concept: denominator-escape-state-contract
    role: guarded-p-free-dispatch-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_second_stutter_unitary_transduction.py
    role: third-carrier-d-one-factorization-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q_0=1\) 第三 \(q\) carrier 的 \(d=1\) p-primary 排除

## 1. 第三 actual raw word

保留 actual H4 \(q_0=1\) second-stutter transduction，并设

\[
\rho=q,
\qquad
\widehat q=1.
\tag{1}
\]

既有 unitary carrier 结论给

\[
q^3\mid Q_{K_4}(z)\mid z.
\tag{2}
\]

所以在原 H4 prefix 上有第三条实际 primitive \(q\)-word

\[
\boxed{
\{h,z\}
\rightsquigarrow
\{x_1,y_1\}
\rightsquigarrow
\{x_2,y_2\}
\rightsquigarrow
\{x_3,y_3\}
:=
\left\{R_4-\frac z{q^3},\frac z{q^3}\right\}.
}
\tag{3}
\]

原 p-free bundle 给 \(p\nmid z\)，而 \(q<p\)，故

\[
p\nmid y_3.
\tag{4}
\]

本卡排除 \(x_3\) 的 \(p\)-block，只处理 \(d=1\) 的 actual H4 子支：

\[
d=\left(\frac{p+1}{2},M_4\right)=1,
\qquad
h=2,
\qquad
p=2q-1.
\tag{5}
\]

## 2. 第三 endpoint 的因式矛盾

由 (3)，

\[
q^3x_3=q^3R_4-z=(q^3-1)R_4+h.
\tag{6}
\]

若反设 \(p\mid x_3\)，在 (6) 中使用 \(R_4\equiv1\pmod p\) 和 (5)，得到

\[
\boxed{p\mid q^3+1.}
\tag{7}
\]

分解右端：

\[
q^3+1=(q+1)(q^2-q+1).
\tag{8}
\]

由于 \(q\ge3\)，(5) 给 \(p=2q-1>q+1\)，故 \(p\) 不能整除首因子。于是存在正整数
\(m\) 使

\[
q^2-q+1=mp.
\tag{9}
\]

又 \(p>q\)，所以 \(0<m<q\)。模 \(q\) 约化 (9)：

\[
1\equiv mp\equiv-m\pmod q.
\tag{10}
\]

故 \(m=q-1\)。将其代入 (9) 和 (5)，有

\[
q^2-q+1=(q-1)(2q-1)
\quad\Longrightarrow\quad
q=2(q-1),
\tag{11}
\]

这与 \(q\ge3\) 矛盾。因此 \(p\nmid x_3\)。结合 (4)，得到

\[
\boxed{p\nmid x_3y_3.}
\tag{12}
\]

## 3. 后果与边界

所以 \(d=1\)、\(\widehat q=1\) 的 third-carrier branch 不会重新制造
\(p\)-primary residual；后续只须按 Type I terminal、p-free payload、容量和语义 guards
分派。后继的
[p-free 容量图与 source \(D\)-gate](type-II-q-one-c-two-19-phase-h4-a-one-q0-one-third-q-d-one-pfree-capacity-map.md)
已把这里的 capacity stutter 收缩为 \(D\equiv72\pmod p\) 与
\(D\mid q^3-4q+1\)，但不把这条必要 sieve 误写成全称排除。它不处理 \(d>1\) 的
同一几何。

更上游的 [original q-bridge source \(D\)-gate](type-II-q-one-c-two-19-phase-h4-a-one-d-one-q-bridge-stutter-source-d-gate-closure.md)
现已排除 actual \(d_4=1\) 的 first stutter，故本卡 \(d=1\) third-carrier 的
antecedent 在实际 H4 域为空；本卡的因式结论仍作为条件性 local lemma 保留。

\`\`\`bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q0_one_second_stutter_unitary_transduction.py --verify
\`\`\`

回执只核对 (6)--(8) 的固定因式控制；全称排除来自第 2 节，不扫描素数范围、denominator
或 Reach history。
