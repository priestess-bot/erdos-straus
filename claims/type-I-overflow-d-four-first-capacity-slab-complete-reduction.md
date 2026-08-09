---
kind: claim
claim_id: type-I-overflow-d-four-first-capacity-slab-complete-reduction
title: 高载体 d=4 首容量层的双模 fixed-s 组合闭合
statement: >-
  设 p≡1 (mod 24) 为素数，verified overflow 满足 pn=16M+1、d=4、4p−7≤n≤8p−17，
  且携带 A|M、1≤A≤B_p=(p−1)^2/4 及既有 source/path、Sol(p)、E1--E5 合同。
  令 r=M mod p、s=(16r+1)/p、P=4r、c=(p−1)/4。则 p≡1 (mod 16) 时 (s,P)=(1,c)，
  p≡9 (mod 16) 时 (s,P)=(9,(9p−1)/4)，统一满足 c≤P≤B_p。若 A<c，取 L=P
  给出完整 fixed-s 严格外层秩递降；若 A≥c，则 B_p<M<2B_p 且 4^2<p，直接接入既有
  small-d 容量层完整递降。故该 d=4 首容量层的每个状态都有严格可提升后继。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-high-carrier-height-staircase
  - type-I-overflow-fixed-s-bounded-divisor-saturation
  - type-I-overflow-small-d-capacity-complete-reduction
topics:
  - type-I
  - overflow
  - high-carrier
  - d-four
  - capacity-window
  - fixed-s
  - dual-remainder
  - small-d-composition
  - well-founded-descent
  - selector
sources:
  - claim: type-I-overflow-high-carrier-height-staircase
    role: d-four-height-entry
  - claim: type-I-overflow-fixed-s-bounded-divisor-saturation
    role: fixed-s-E1-E5-contract
  - claim: type-I-overflow-small-d-capacity-complete-reduction
    role: A-at-least-c-composition
  - reproduction: reproductions/type_i_overflow_d_four_first_capacity_slab_complete_reduction.py
    role: two-modulus-fixed-s-and-small-d-receipt
visibility: public
last_checked: '2026-08-09'
---

# 高载体 \(d=4\) 首容量层的双模 fixed-\(s\) 组合闭合

## 定理

令 \(p\equiv1\pmod {24}\) 为核心素数，并设一个已有 source/path/node 回执的
verified overflow 满足

\[
pn=16M+1,
\qquad d=4,
\qquad 4p-7\le n\le8p-17,
\tag{1}
\]

以及 \(A\mid M\)、\(1\le A\le B_p\)，其中

\[
B_p=\frac{(p-1)^2}{4},
\qquad c=\frac{p-1}{4}.
\tag{2}
\]

把 \(r=M\bmod p\) 取为 \(1\le r<p\) 的规范代表，并置

\[
s=\frac{16r+1}{p},
\qquad P=4r.
\tag{3}
\]

则 \(s\) 为正整数，且有精确的模 16 二分

\[
\begin{array}{c|c|c}
p\bmod16&s&r\text{ 与 }P\\ \hline
1&1&r=(p-1)/16,\quad P=c\\
9&9&r=(9p-1)/16,\quad P=(9p-1)/4.
\end{array}
\tag{4}
\]

两种情形统一满足

\[
c\le P\le B_p.
\tag{5}
\]

因此每个状态按 \(A\) 分流：

\[
\begin{array}{c|c|c}
\text{条件}&\text{后继}&\text{严格付款}\\ \hline
A<c&L=P\mid rd&\text{fixed-}s\text{，第一坐标严格下降}\\
A\ge c&\text{small-}d\text{ 容量层的因子/交换/商折叠}&
\left(\lfloor B_p/A\rfloor,M\right)\text{ 字典序严格下降}.
\end{array}
\tag{6}
\]

在既有恒等解提升和 E1--E5 合同下，(1) 的整个 \(d=4\)、\(B_p<M<2B_p\) 首容量层
不留 overflow 余项。

## 容量界

由 (1) 的下界，

\[
16M=pn-1\ge p(4p-7)-1
>4(p-1)^2=16B_p,
\tag{7}
\]

其中最后一个严格不等式等价于 \(p>5\)。由上界，

\[
16M=pn-1\le p(8p-17)-1
<8(p-1)^2=32B_p,
\tag{8}
\]

因为右侧减左侧为 \(p+9\)。所以

\[
\boxed{B_p<M<2B_p.}
\tag{9}
\]

核心素数 \(p\equiv1\pmod {24}\) 必有 \(p\ge73\)，故

\[
d^2=16<p.
\tag{10}
\]

这正是既有 small-\(d\) 容量层定理在 \(A\ge c\) 分支所需的全部数值门。

## 双模 fixed-\(s\) 分支

由 \(pn=16M+1\) 和 \(M=kp+r\)，有

\[
16r+1=sp,
\qquad 1\le s\le15.
\tag{11}
\]

又 \(p\equiv1\pmod {24}\) 蕴含 \(p\equiv1\) 或 \(9\pmod {16}\)。若 \(p\equiv1\pmod {16}\)，
则 \(s\equiv1\pmod {16}\)，结合 (11) 得 \(s=1\)，从而

\[
r=\frac{p-1}{16},\qquad P=4r=c.
\tag{12}
\]

若 \(p\equiv9\pmod {16}\)，则 \(s\equiv9\pmod {16}\)，故 \(s=9\)，并且

\[
r=\frac{9p-1}{16},\qquad P=\frac{9p-1}{4}.
\tag{13}
\]

在第二行，\(P\le B_p\) 等价于

\[
p^2-11p+2\ge0,
\tag{14}
\]

对 \(p\ge73\) 成立；第一行显然成立。两行均有 \(P\ge c\)。

现在假设 \(A<c\)。由 (5) 有 \(A<P\le B_p\)，且 \(P=rd\) 因为 \(d=4\)。此外

\[
4P>s,
\tag{15}
\]

在第一行是 \(p-1>1\)，在第二行是 \(9p-1>9\)。固定-\(s\) 的严格外层势条件也自动
成立，因为

\[
\frac{B_p}{P}\le\frac{B_p}{c}=p-1,
\qquad
\frac{B_p}{A}>\frac{B_p}{c}=p-1,
\tag{16}
\]

从而

\[
\left\lfloor\frac{B_p}{P}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{17}
\]

取 \(L=P\) 代入既有 fixed-\(s\) 有界除子合同。其 canonical 后继的两个整数为

\[
R_P=4P-s,
\qquad K_P=P(p-1),
\tag{18}
\]

并满足

\[
pR_P+1=4K_P,
\qquad R_P\equiv3\pmod4,
\qquad R_P>0,
\qquad K_P>0.
\tag{19}
\]

因此这是完整 E1--E5 的 fixed-\(s\) 严格边；若 \(A\nmid P\)，其支撑重置由既有外层
势明确支付，而非声称 support-preserving。

## \(A\ge c\) 的组合闭合

若 \(A\ge c\)，(9)--(10) 逐项满足既有“高载体小 \(d\) 容量层的完整余因子递降”
定理的假设：\(B_p<M<2B_p\)、\(c\le A\le B_p\)、\(A\mid M\) 以及 \(d^2<p\)。
该定理已经给出穷尽的三类后继：

1. \(b=M/A\le d\) 时的最小素因子转移；
2. \(b<p\) 且 \(b>d\) 时的余因子交换；
3. \(b>p\) 时的固定-\(n\) 商模 \(p\) 折叠。

每一类都保持或显式重置 support，并严格降低

\[
\Lambda_p(M,d;A)=
\left(\left\lfloor\frac{B_p}{A}\right\rfloor,M\right).
\tag{20}
\]

所以 \(A\ge c\) 不再需要另建 d=4 专门的素因子菜单。

## 穷尽性与边界

输入的 \(A\) 必满足 \(A<c\) 或 \(A\ge c\)，两分支互斥且穷尽。前者由 (12)--(19)
给出新的双模 fixed-\(s\) 边，后者由既有 small-\(d\) 定理闭合。故本卡证明的是

\[
\boxed{4p-7\le n\le8p-17,\quad d=4}
\]

这一首容量层的完整选择器入口，而不是全体 \(d\ge4\) 或全体 \(n\ge8p-16\) 的结论。
source/path/node 可达性、图表无关的 \(\operatorname{Sol}(p)\) 恒等提升仍沿用依赖卡片的假设。

## 控制实例与复现

\[
\begin{array}{c|r|r|r|r|r|l}
p&n&M&r&s&A&\text{分支}\\ \hline
73&297&1355&41&9&5&\text{dual fixed-}s\\
97&385&2334&6&1&6&\text{dual fixed-}s\\
73&313&1428&41&9&714&\text{small-}d\text{ factor}\\
73&361&1647&41&9&549&\text{small-}d\text{ factor}\\
73&329&1501&41&9&19&\text{small-}d\text{ quotient fold}
\end{array}
\]

精确复现命令：

    python3 reproductions/type_i_overflow_d_four_first_capacity_slab_complete_reduction.py --verify

本卡的明确边界是 \(d=4,\ M\ge2B_p,\ A\ge c\) 的更高容量层；其中 \(A<c\)
已由通用 dual 饱和引理覆盖。\(d^2\ge p\) 或其它 source/path 未闭合部分仍需
generalized \(2^j\)、q-adic capacity 或其它 Type I/II 证书。
