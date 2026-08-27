---
kind: claim
claim_id: type-I-root-capacity-stutter-m-three-natural-fan-small-cofactor-clearance
title: proper-root m=3 natural-fan fan-miss 的小 cofactor 清除
statement: >-
  在 actual proper-root m=3,d=13,s_d=3 core 中，若 natural fan miss，
  则 C>=223。证明从既有 C>=40、C=1 mod6 和 C 的每个素因子=1 mod3 开始，
  穷尽 40<=C<223 的22个候选。18个候选使 p=52C-3 合数；余下
  C=61,73,91 的 fixed-C divisor fiber 没有位于必要区间的 F|N_C，C=157
  的唯一区间 F 违反 A=52t-1 合同。这只是 actual Diophantine/core pruning，
  不证明一般 fan hit、terminal、E1--E5 或 T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-m-three-natural-fan-cofactor-support-separation
  - type-I-root-capacity-stutter-m-three-natural-fan-fixed-cofactor-second-norm-gate
topics:
  - type-I
  - f3
  - proper-root
  - m-three
  - natural-fan
  - fixed-cofactor
  - small-cofactor
  - family-empty
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-m-three-natural-fan-cofactor-support-separation
    role: fan-miss cofactor domain and exact fixed-C fiber
  - claim: type-I-root-capacity-stutter-m-three-natural-fan-fixed-cofactor-second-norm-gate
    role: fixed-fiber necessary conditions
visibility: public
last_checked: '2026-08-27'
---

# proper-root m=3 natural-fan fan-miss 的小 cofactor 清除

## 1. Domain

For an actual `m=3`, \(d=13\), \(s_d=3\) core packet, the natural fan
miss condition gives

\[
C\ge40,\qquad C\equiv1\pmod6,\qquad
q\mid C\Longrightarrow q\equiv1\pmod3.
\tag{1}
\]

The fixed-fiber relations are

\[
p=52C-3,\qquad
F\mid N_C:=8112C^2-884C+25,
\tag{2}
\]

\[
104C-5<F<156C-8,\qquad F\equiv1\pmod3,
\tag{3}
\]

\[
3H+F+20\equiv0\pmod{156},\qquad H=N_C/F.
\tag{4}
\]

Only these necessary conditions are needed for the small-cofactor clearance.

## 2. Complete finite list below 223

The integers satisfying (1) with \(40\le C<223\) are exactly

\[
\begin{aligned}
&43,49,61,67,73,79,91,97,103,109,127,133,139,151,\\
&157,163,169,181,193,199,211,217.
\end{aligned}
\tag{5}

\]

For all but four entries, \(p=52C-3\) is visibly composite. A nontrivial
factor is displayed in the following table:

\[
\begin{array}{c|rrrrrrrrrrrrrrrrrr}
C&43&49&67&79&97&103&109&127&133&139&151&163&169&181&193&199&211&217\\
\hline
q\mid(52C-3)&7&5&59&5&71&53&5&7&31&5&47&37&5&97&79&5&7&29
\end{array}
\tag{6}

\]

The remaining prime values are \(C=61,73,91,157\). Their exact fiber data
are

\[
\begin{array}{c|c|c|c}
C&p&N_C&\text{fiber outcome}\\
\hline
61&3169&31\cdot823\cdot1181&\text{no divisor in (3)}\\
73&3793&11\cdot59\cdot66509&\text{no divisor in (3)}\\
91&4729&89\cdot191\cdot3947&\text{no divisor in (3)}\\
157&8161&5^2\cdot709\cdot11273&F=17725\text{ is the only candidate}
\end{array}
\tag{7}

\]

For \(C=157\), the sole candidate has \(H=11273\), but

\[
3H+F+20=51564\equiv84\pmod{156},
\]

contradicting (4). Thus none of the entries in (5) can be an actual
fan-miss core packet.

## 3. Consequence and boundary

\[
\boxed{
\text{actual }m=3,d=13,s_d=3\text{ natural-fan miss}
\Longrightarrow C\ge223.}
\tag{8}
\]

This is a finite exact factor/divisor proof, not a heuristic search. It does
not say that a fan-miss packet with \(C\ge223\) exists or survives the
second-norm and primitive gates. It does not produce a terminal, actual
source-path, E1--E5 successor, or any global T6 conclusion.
