---
kind: claim
claim_id: type-II-canonical-critical-fan-escape-trichotomy
title: 规范 Type II 扇不能长期全为一孔临界失败
statement: 令 p=1 mod24 为素数，取 H 满足 4H<p 且 4 乘以不大于 H 的全部素数之积大于 p-1。则前 H 条平方自由规范 Type II 射线中，必有一条成功，或至少一条失败射线不是一孔支撑临界型。后一种失败精确地分为目标残数在素因子支撑外，或目标在支撑内但除子残数缺失集至少有两个元素。由素数定理，充分大的 p 可取 H=(1+epsilon)log p。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-II
- canonicalization
- critical-sequence
- subgroup-structure
- trichotomy
- deterministic-reduction
- proof-program
sources:
- reproduction: reproductions/type_ii_canonical_fan_escape_trichotomy.py
  role: exact canonical-fan factor, subgroup, and quadratic-separator replay
- result: reproductions/type-ii-canonical-fan-escape-trichotomy-results.json
  role: focused typed fan escape profiles
- paper: montgomery_vaughan2007
  locator: Chapter 11, fixed-modulus prime-number-theorem context
  role: primorial-growth-consequence
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-08-04'
---

# 规范 Type II 扇不能长期全为一孔临界失败

## 定理

对每个 \(s\ge1\)，唯一写作

\[
s=a_s^2c_s,\qquad c_s\ \text{平方自由},
\]

并令其规范 Type II 射线的模数和移位数为

\[
M_s=4a_sc_s,\qquad N_s=p+4s=p+a_sM_s. \tag{1}
\]

对 \(N_s\) 的素因子残数序列，记

\[
\Pi_s=\{\text{所有子序列乘积}\}\subset U(M_s),\qquad
K_s=\langle\text{该素因子残数序列}\rangle. \tag{2}
\]

设

\[
\mathfrak P(H)=\prod_{\substack{\ell\le H\\\ell\ {\rm prime}}}\ell. \tag{3}
\]

若核心素数 \(p\) 和整数 \(H\) 满足

\[
4H<p,\qquad 4\mathfrak P(H)>p-1, \tag{4}
\]

则前 \(H\) 条规范射线至少发生下列三件事之一：

1. 存在 \(s\le H\) 成功，即 \(N_s\) 有因子 \(h>1\) 满足
   \(h\equiv-1\pmod {M_s}\)，从而给出 Type II 证书；
2. 存在失败的 \(s\le H\)，但 \(-1\notin K_s\)；
3. 存在失败的 \(s\le H\)，且 \(-1\in K_s\) 但

\[
\lvert K_s\setminus\Pi_s\rvert\ge2. \tag{5}
\]

换言之，在 (4) 的扇宽内，不可能每条规范射线都失败且都满足一孔临界等式

\[
\Pi_s=K_s\setminus\{-1\}. \tag{6}
\]

这里第一项是直接终端；后两项分别是支撑外失败与非一孔支撑内失败。这不是对后两项的
排除定理，只是把不能长期维持的一孔临界主型从逐点选择器的剩余状态中严格剥离。

## 证明

假设前三项都不发生。于是每个 \(1\le s\le H\) 的射线失败，且都满足 (6)。
由 \(M_s\mid4s\) 和 \(4s\le4H<p\)，有 \(\gcd(p,M_s)=1\)。因此
`type-II-support-critical-congruence-trap` 可逐条应用，给出

\[
p\equiv1\pmod {M_s}\qquad(1\le s\le H). \tag{7}
\]

令

\[
Q_H=\operatorname{lcm}\bigl(24,M_1,\ldots,M_H\bigr). \tag{8}
\]

由 (7)，\(Q_H\mid p-1\)。但每个不大于 \(H\) 的素数 \(\ell\) 对应规范表示

\[
\ell=1^2\ell,\qquad M_\ell=4\ell.
\]

所以

\[
4\mathfrak P(H)\mid Q_H\mid p-1, \tag{9}
\]

这与 (4) 矛盾。故至少有一项发生。

若没有成功射线，所有 \(-1\notin K_s\) 的失败属于第二项。其余失败都有
\(-1\in K_s\)，又因射线失败而 \(-1\notin\Pi_s\)。不是 (6) 就等价于
\(\lvert K_s\setminus\Pi_s\rvert\ge2\)，即第三项。由此也验证该三分没有遗漏。

## 扇宽尺度

条件 (4) 是完全可计算的，不需任何渐近估计。作为尺度说明，令
\(\vartheta(H)=\log\mathfrak P(H)\)。由素数定理
\(\vartheta(H)=(1+o(1))H\)，所以任取固定 \(\epsilon>0\)，对充分大的 \(p\) 可取

\[
H=\left\lceil(1+\epsilon)\log p\right\rceil. \tag{10}
\]

此时第二个条件在 (4) 中成立，而 \(4H<p\) 也自动成立。因此这是一条
\(O(\log p)\) 宽度的确定性状态约化，而不是固定宽度射线饱和证明。

例如，\(p=73\) 时取 \(H=5\)：\(4\mathfrak P(5)=120>72\)，且 \(20<73\)。
所以前五条规范射线不可能全部是一孔临界失败。这个数值例子只说明判据的精确形式，
不作为一般证明的替代。

## 与当前路线的关系

`type-II-ac-rays-superlog-residual` 和
`type-II-growing-canonical-fan-superlog-tail` 控制的是大量素数上同时失败的密度；
本定理则对单个 \(p\) 排除一种会妨碍结构分类的失败组合。它与筛法不相替代：
在已有有限审计中，绝大多数失败本来就属于第二项的支撑外型，故该三分法没有把剩余
自动变成证书。

现已将该三分接入表示--对偶--容量选择器。支撑外行由商群
`U(4*a_s*c_s)/K_s` 的二次角色给出精确分离回执；支撑内多孔行保存
`K_s minus Pi_s` 作为目标纤维缺陷。统一状态仍标为
`certificate_type=type_ii_canonical_fan_escape_trichotomy`、
`selector_status=analysis_evidence`，因为这两类回执尚未给出跨状态载体映射或完整解提升。
七个聚焦核心素数的可重放结果位于
[Type II 扇逃逸三分结果](../reproductions/type-ii-canonical-fan-escape-trichotomy-results.json)。

下一步若要把这里推进为逐点结论，必须针对第二项或第三项建立跨移位不相容性、可提升的
递降，或新的因子选择定理。仅继续强化一孔临界的同余陷阱不会覆盖主导残余。
