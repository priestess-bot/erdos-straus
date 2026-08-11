---
kind: claim
claim_id: type-I-type-II-double-g-external-source-preemption
title: 模三双 G 的完整零平移外部源失败与 gap-11 终端优先截断
statement: >-
  核心素数 p=5209 是模三双 G： (p+3)/4=1303 与
  (3p+1)/4=3907 的所有素因子均为 1 (mod 3)。对全部
  k | (p-1)/4=1302，完整零平移 quadratic external-source 二尾族的
  因子菜单 e | (k n_k)^2、e<=k n_k、e=-k n_k (mod 4k-1) 均为空；
  因而该完整外部源族不能作为双 G 的全局出口。可是 p=5209 同时有
  gap-11 Type II 因子对 (A,B,C,K)=(1,87,15,8)，并以
  n=(p+11)/12=435 给出显式的两尾严格递降。因此这不是 terminal-first
  后的未决 G/Type I 状态，而是完整外部源失败必须先由 Type II terminal 截断的严格控制。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-type-II-mod-three-double-g-exit-obstruction
  - quadratic-factor-external-source-descent
  - type-II-factor-pair-carrier-strict-descent
  - type-II-c3-q-complementary-divisor-r7mod11-descent
topics:
  - Erdos-Straus
  - type-I
  - type-II
  - double-G
  - external-source
  - terminal-first
  - strict-descent
  - counterexample
  - proof-program
sources:
  - claim: quadratic-factor-external-source-descent
    role: complete-zero-shift-external-source-parameterization
  - claim: type-II-factor-pair-carrier-strict-descent
    role: gap-eleven-terminal-and-two-tail-lift
  - reproduction: reproductions/type_i_type_ii_double_g_external_source_preemption.py
    role: exact-p5209-finite-menu-and-terminal-control
visibility: public
last_checked: '2026-08-12'
---

# 模三双 G 的完整零平移外部源失败与 gap-11 终端优先截断

## 1. 要排除的完整外部源族

对核心素数 \(p\)，令

\[
k\mid\frac{p-1}{4},\qquad Q_k=4k-1,
\qquad n_k=\frac{Q_kp+1}{Q_k+1},\qquad M_k=kn_k.
\tag{1}
\]

定义完整零平移平方因子菜单

\[
\mathcal E_0(p)=
\left\{(k,e):
\begin{array}{l}
k\mid(p-1)/4,\\
e\mid M_k^2,\quad e\le M_k,\\
e\equiv-M_k\pmod {Q_k}
\end{array}
\right\}.
\tag{2}
\]

平方因子外部源定理说明，\(\mathcal E_0(p)\) 非空当且仅当某个
允许 \(k\) 的、保持第一分母 \(M_k\) 的完整二尾可给出

\[
\frac4{n_k}=\frac1{M_k}+\frac1u+\frac1v
\longmapsto
\frac4p=\frac1{pM_k}+\frac1u+\frac1v.
\tag{3}
\]

因此 (2) 不是一个只搜索外部源子族的近似筛，而是这一零平移、固定保留分母
机制的完整因子判据。

## 2. 一个双 G 的完整外部源反例

取

\[
p=5209,\qquad
\frac{p+3}{4}=1303,\qquad
\frac{3p+1}{4}=3907.
\tag{4}
\]

三个数 \(5209,1303,3907\) 都是素数，且后两个均为 \(1\pmod3\)。所以
\(p\) 是模三双 G 控制；特别地，gap \(3\) 的 Type II \(q=1\) 出口和
\(R=3\) Type I 伴随出口同时为 G。

这里

\[
\frac{p-1}{4}=1302=2\cdot3\cdot7\cdot31,
\tag{5}
\]

故 (2) 只须检查 16 个 \(k\) 值。对每个 \(k\)，精确分解 \(M_k\)，枚举
\(M_k^2\) 的全部正因子，并检验 (2) 的其余两行，得到

\[
\boxed{\mathcal E_0(5209)=\varnothing.}
\tag{6}
\]

所以完整 quadratic external-source family 不仅漏掉某个预先指定的 \(k\)，而是
在该双 G 点的所有允许外部源上均没有 marked two-tail lift。它当然也包含普通及
mixed-factor external-source 子族，故这些更窄分支同样不能关闭这个点。

## 3. terminal-first 的正确截断

式 (6) 不是 Erdős--Straus 的反例，也不是合法的 terminal-first residual。写

\[
h=217,\qquad q=2h+1=435,\qquad
r=29\equiv7\pmod{11}.
\tag{7}
\]

令

\[
d=\frac qr=15,\qquad c=\frac{3r+1}{11}=8,
\qquad x=3q=1305.
\tag{8}
\]

则 \(x+d=1320=11cd\)，并且这正是 gap \(11\) 的 Type II 互素因子正规形

\[
(A,B,C,K)=(1,87,15,8),\qquad A+B=88=11K.
\tag{9}
\]

它给出直接 terminal

\[
\frac4{5209}
=\frac1{1305}+\frac1{625080}+\frac1{54381960},
\tag{10}
\]

同时给出严格较小分母 \(n=q=(p+11)/12=435\) 的标记两尾解

\[
\frac4{435}
=\frac1{1305}+\frac1{120}+\frac1{10440}
\longmapsto
\frac4{5209}
=\frac1{1305}+\frac1{5209\cdot120}+\frac1{5209\cdot10440}.
\tag{11}
\]

所以在全局选择器中，\(p=5209\) 必须在 direct Type II terminal-first 分支停止，
而不能因 (6) 被送入 G/Type I 的 source-contract 队列。

## 4. 结论边界

这个控制严格排除的是下列错误全称：

\[
\text{“每个模三双 G 点都由完整零平移 external-source family 关闭”。}
\]

它不排除非零平移 external source、even-split 等其它提升，也不提供一个
terminal-first 后仍未决的 G/Type I 状态。其正面意义是调度性的：外部源菜单的空性
必须在所有直接 Type II terminal 之后解释；否则会把一个已关闭的点错误地当成
全局 source-contract 反例。

## 聚焦复现

~~~bash
python3 reproductions/type_i_type_ii_double_g_external_source_preemption.py --verify
~~~
