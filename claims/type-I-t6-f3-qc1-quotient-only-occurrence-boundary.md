---
kind: claim
claim_id: type-I-t6-f3-qc1-quotient-only-occurrence-boundary
title: F3 R3/R5 quotient-only 的规范 ideal factor 与整数 occurrence 边界
statement: >-
  对每个 R3/R5 域中的 actual persistent low proper-height stutter state，
  q_perp=min{q prime:q|k,q not divide h} 在全域存在且满足 7<=q_perp<p/4。
  在 Z[omega] 中，beta=a-b omega 被唯一的有向 norm-q_perp 素理想
  (q_perp,omega-lambda) 整除，其中 lambda=a*b^{-1} mod q_perp；共轭理想不整除
  beta，且该 ideal multiplicity 恰为 v_q_perp(k)。这把裸 q_perp|k 加强为绑定
  actual stutter arithmetic receipt 的内容寻址 algebraic factor，但仍不是整数 raw
  complete-excess side occurrence，不能支付 E1 或 support charge conservation。
  条件于未来证明一份 path-bound integer occurrence 可合法把 charged support A 更新为
  A*q_perp，规范 target 公式 L=A*q_perp、c=-q_perp^{-1} mod p、K_T=Lc、
  R_T=(4K_T-1)/p 给出唯一 high-support overflow shape，局部 N7 容量从 p-1 降至
  c<=p-2，并在 shape control 中唯一匹配 type_i_a_gt_one_overflow_residual。
  但当前没有真实 runtime source replay、共同 terminal dispatch、共享 producer rule、
  ROOT_SOL/scope propagation 或 common admission，因此 R3、R5、QC1、F3 与 T6 保持 OPEN。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t6-f3-proper-root-routing-with-explicit-residuals
  - type-I-root-capacity-stutter-common-divisor-alignment
  - type-I-root-capacity-stutter-primitive-quotient-normalization
  - type-I-root-capacity-stutter-eisenstein-support
  - type-I-root-capacity-stutter-complementary-eisenstein-coordinate-gap
  - t6-persistent-selector-state-v1
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - type-I
  - t6-f3
  - proper-root
  - quotient-only
  - qc1
  - eisenstein-factor
  - occurrence-boundary
  - proof-boundary
sources:
  - concept: t6-f3-proper-root-domain-v1
    role: R3/R5 quantifier and terminal precedence
  - claim: type-I-root-capacity-stutter-common-divisor-alignment
    role: quotient-only factor is disjoint from shared coordinate content
  - claim: type-I-root-capacity-stutter-complementary-eisenstein-coordinate-gap
    role: quotient size and factor-level normal-form obstruction
  - reproduction: reproductions/type_i_t6_f3_qc1_quotient_only_physical_transition.py
    role: algebraic factor, conditional target shape, fail-closed and common-kernel shape controls
visibility: public
last_checked: '2026-08-24'
---

# F3 R3/R5 quotient-only occurrence boundary

## 1. Quantifier

Let S be an `ACTUAL_PERSISTENT`, terminal-first-surviving proper-root state
whose admitted source and maximal stutter receipts give

\[
2\le h<p,\qquad k>1,\qquad
k_\perp=\prod_{q\mid k,\ q\nmid h}q^{v_q(k)}>1.
\tag{1}
\]

The state is in exactly one owned residual:

\[
\begin{aligned}
R3 &: m=3,\quad 5\nmid D_*,\quad k_\perp>1,\\
R5 &: m>3,\quad k_\perp>1.
\end{aligned}
\tag{2}
\]

The dedicated m=3, q=5 route and the h-supported cases are excluded.

## 2. Canonical algebraic carrier

Define

\[
\boxed{q_\perp=\min\{q:q\text{ prime},\ q\mid k,\ q\nmid h\}.}
\tag{3}
\]

Existence follows immediately from \(k_\perp>1\). The Eisenstein support
theorem and \(3\mid h\) imply

\[
q_\perp\equiv1\pmod3,\qquad q_\perp\ge7.
\tag{4}
\]

The proper-root inequalities give \(N<e^2\) and \(e(m-1)<h\), where

\[
N=a^2-ab+b^2=hk,\qquad b=e-1.
\]

Since \(m\ge3\),

\[
k=\frac Nh<\frac{e^2}{h}<\frac h4<\frac p4,
\qquad q_\perp<p/4.
\tag{5}
\]

Thus the carrier choice is total, deterministic and bounded across both R3
and R5. This is still an arithmetic carrier statement.

## 3. What the oriented ideal proves

Work in

\[
\mathbb E=\mathbb Z[\omega],\qquad \omega^2-\omega+1=0,
\]

and set

\[
\beta=a-b\omega,\qquad N(\beta)=hk.
\tag{6}
\]

The prime \(q_\perp\) divides neither \(a\) nor \(b\). If it divided one,
(6) would force it to divide both; the common-divisor alignment theorem
would then imply \(q_\perp\mid h\), contradicting (3).

Hence \(b\) is invertible modulo \(q_\perp\). Put

\[
\lambda\equiv ab^{-1}\pmod {q_\perp}.
\tag{7}
\]

Then

\[
\lambda^2-\lambda+1\equiv0\pmod {q_\perp}.
\tag{8}
\]

The two roots \(\lambda\) and \(1-\lambda\) are distinct because
\(q_\perp\ne3\). Therefore the oriented prime ideal

\[
\mathfrak q_S=(q_\perp,\omega-\lambda)
\tag{9}
\]

satisfies

\[
\boxed{\mathfrak q_S\mid\beta,
\qquad \bar{\mathfrak q}_S\nmid\beta.}
\tag{10}
\]

Since \(q_\perp\nmid h\), its multiplicity in (10) is exactly
\(v_{q_\perp}(k)\). For a genuinely replayed source, this construction can be
content-addressed by the source state, producer, admission, source-path,
terminal-first and maximal-receipt digests. This is stronger than storing only
`q_perp divides k`. The current reproducer deliberately does not authenticate
those runtime objects: it rejects every `ACTUAL_PERSISTENT` label and exercises
only an explicit non-actual shape control.

It is nevertheless not E1. Equation (10) locates a prime ideal in an
Eisenstein norm. It does not locate an integer \(q_\perp\)-power on a
specific raw source side with valuation exceeding the current K-capacity,
does not replay a raw transition which consumes it, and does not prove that
one occurrence may be charged into `absorbed_support`. In particular,

\[
\boxed{\mathfrak q_S\mid\beta
\not\Longrightarrow
\text{path-bound integer complete-excess occurrence}.}
\tag{11}
\]

The gap in (11) is exactly the divisor-as-occurrence error prohibited by the
wave plan.

## 4. Conditional target formula

The existing root chart has charged support \(\mathcal A\) and

\[
K_S=\mathcal A(p-1),\qquad
\mathcal A>B_p=\frac{(p-1)^2}{4}.
\tag{12}
\]

Suppose a future theorem strengthens (10) to a path-bound integer occurrence
with a valid one-use owner and proves the support conservation rule

\[
\mathcal A_T=\mathcal A q_\perp.
\tag{13}
\]

Then define

\[
L=\mathcal A q_\perp,\qquad
c=\langle-q_\perp^{-1}\rangle_p,
\tag{14}
\]

\[
K_T=Lc,\qquad R_T=\frac{4K_T-1}{p}.
\tag{15}
\]

Because \(4\mathcal A\equiv-1\pmod p\), the target is integral and

\[
pR_T+1=4K_T,\qquad L\mid K_T,\qquad R_T\equiv3\pmod4.
\tag{16}
\]

The bounds \(1<q_\perp<p/4\) exclude \(c=p-1\), so

\[
1\le c\le p-2.
\tag{17}
\]

Moreover \(R_T>p\), because \(\mathcal A>B_p\), \(q_\perp\ge7\), and

\[
4K_T\ge4\mathcal A q_\perp>7(p-1)^2>p^2+1.
\tag{18}
\]

Thus (15) is a deterministic high-support overflow shape. Direct evaluation
of the frozen family predicates, without constructing any state or rule, gives
exactly one current family match:

```text
type_i_a_gt_one_overflow_residual
```

and its formal N7 ranks would be

\[
\Pi(S)=(p,2,4,0,p-1,0,0),
\qquad
\Pi(T)=(p,2,4,0,c,0,0).
\tag{19}
\]

Hence (17) supplies a conditional `LOCAL_DROP`. This does not become an E5
ticket until E1-E4, target terminal priority and final common admission are
actually established.

## 5. Minimal residual

The original R3/R5 residual is reduced, but not closed. Every actual input
has a canonical q_perp and oriented ideal factor. To obtain a physical edge,
one must still prove:

1. an integer source-side occurrence theorem identifying side, node, path,
   exponent and current K-capacity for this same q_perp;
2. a one-use owner and charge-conservation theorem justifying (13), including
   the case \(q_\perp\mid\mathcal A\);
3. replay of the real upstream source state, mark and scope rather than a
   self-declared evidence string;
4. the coordinator-owned target terminal dispatch;
5. registration of the real producer rule and replay through the shared
   admission runtime.

The reproducer only classifies the proposed target facts. It creates no
producer rule, terminal receipt, persistent state or admission evidence. The
accurate statuses are:

```text
Q_PERP_EXISTENCE = ESTABLISHED
ORIENTED_EISENSTEIN_IDEAL_FACTOR = ESTABLISHED
INTEGER_RAW_OCCURRENCE_AND_CONSERVATION = OPEN
QC1PhysicalTransitionV1 = OPEN_MINIMAL_RESIDUAL
R3 = OPEN_MINIMAL_RESIDUAL
R5 = OPEN_MINIMAL_RESIDUAL
F3 = OPEN
T6 = OPEN
```

Focused checks:

```bash
python3 reproductions/type_i_t6_f3_qc1_quotient_only_physical_transition.py --verify
python3 -m unittest tests.test_type_i_t6_f3_qc1_quotient_only_physical_transition -v
```

The numeric control is explicitly core-congruent but nonprime. It checks
algebra, target shape and fail-closed behavior; it is not an actual witness or
the universal proof.
