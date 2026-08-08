---
kind: claim
claim_id: type-I-overflow-small-d-capacity-complete-reduction
title: 高载体小 d 容量层的完整余因子递降
statement: 设核心素数 p=1 (mod 24) 的 verified overflow 满足 pn=4Md+1、B_p=(p-1)^2/4<M<2B_p、1<=d<p，且 charged support 满足 c=(p-1)/4<=A<=B_p、A|M、d^2<p。则必有完整 E1--E5 严格递降：写 b=M/A；b<=d 时用最小素因子转移，b<p 且 b>d 时用余因子交换，b>p 时 L=b 满足完整 outer-rank 条件并由固定-n 商模 p 折叠给出后继。b=p 不可能。故这个小 d 高载体容量层不留未分流的 overflow。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-factor-exchange-carrier-descent
  - type-I-overflow-fixed-n-quotient-fold-descent
  - type-I-overflow-capacity-slab-factor-threshold-residual
topics:
  - type-I
  - overflow
  - high-carrier
  - small-d
  - capacity-window
  - cofactor
  - quotient-fold
  - support-reset
  - well-founded-descent
  - selector
sources:
  - claim: type-I-overflow-cofactor-factor-exchange-carrier-descent
    role: composite-and-small-prime-transfers
  - claim: type-I-overflow-fixed-n-quotient-fold-descent
    role: large-cofactor-folded-reset
  - claim: type-I-overflow-capacity-slab-factor-threshold-residual
    role: sharp-capacity-slab-residual-and-square-threshold
  - reproduction: reproductions/type_i_overflow_small_d_capacity_complete_reduction.py
    role: focused-five-route-receipt
visibility: public
last_checked: '2026-08-08'
---

# 高载体小 \(d\) 容量层的完整余因子递降

## 定理

设 \(p\equiv1\pmod {24}\) 为素数，并令

\[
B_p=\frac{(p-1)^2}{4},
\qquad c=\frac{p-1}{4}.
\tag{1}
\]

设一个已有 source/path/node 回执的 verified overflow 满足

\[
pn=4Md+1,
\qquad B_p<M<2B_p,
\qquad 1\le d<p,
\tag{2}
\]

且 charged support 满足

\[
c\le A\le B_p,
\qquad A\mid M,
\qquad d^2<p.
\tag{3}
\]

写 \(b=M/A\)。则该状态必有一条完整 E1--E5 的严格递降。更精确地：

\[
\begin{array}{c|c|c}
\text{条件}&\text{规范构造}&\text{严格势}\\ \hline
b\le d&g=\operatorname{spf}(b)\text{ 的因子转移}&\left(\lfloor B_p/A\rfloor,M\right)\\
b<p,\ b>d&(M,d)\mapsto(Ad,b)&\left(\lfloor B_p/A\rfloor,M\right)\\
b>p&L=b\text{ 的商模 }p\text{ 折叠}&\left\lfloor B_p/A\right\rfloor
\end{array}
\tag{4}
\]

特别地，该 \(A\ge c\) 的小 \(d\) 高载体容量层不再留下素大余因子残余。

## 余因子范围

由 (2)--(3)，

\[
1<b=\frac MA\le\frac Mc<\frac{2B_p}{c}=2(p-1).
\tag{5}
\]

又 \(p\nmid M\)，所以当 \(b\) 是素数时 \(b\ne p\)。这穷尽了 (4) 的三类
余因子。

## 小余因子

先设 \(b\le d\)，并令 \(g=\operatorname{spf}(b)\)。由于
\(g\le b\le d\)，(3) 给出

\[
dg\le d^2<p.
\]

所以 \(g\) 可移，余因子因子转移引理给出保持 \(A\) 的严格载体递降。这里不要求
\(b\) 为素数或合数。

再设 \(b<p\) 而 \(b>d\)。直接使用余因子交换
\((M,d)=(Ab,d)\mapsto(Ad,b)\)。它同样由
\(\left(\lfloor B_p/A\rfloor,M\right)\) 的字典序严格下降。

## 大余因子的商折叠

最后设 \(b>p\)。此时

\[
A=\frac Mb<\frac{2B_p}{p}=\frac{(p-1)^2}{2p}<\frac p2<b,
\tag{6}
\]

因而 \(b>2A\)。又由 (5) 及 \(p\ge73\)，

\[
A<b<2(p-1)<B_p,
\qquad
\left\lfloor\frac{B_p}{b}\right\rfloor
\le\left\lfloor\frac{B_p}{2A}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{7}
\]

取 \(L=b\mid M\mid Md\)。它满足完整 fixed-\(n\) 外层秩的除子条件。令

\[
\frac{Md}{b}=ph+\delta,
\qquad 1\le\delta<p,
\qquad n_T=n-4bh.
\tag{8}
\]

商模 \(p\) 折叠引理给出

\[
pn_T=4b\delta+1,
\]

并把 support 重置到 \(b\)，严格降低 (7) 的第一坐标。这一构造同时覆盖
\(4b>n\) 的普通正 fixed-\(n\) 情形与 \(4b\le n\) 的负图表重入；后者不再是
未闭合残余。

E1--E5 分别由两个所引的转移合同提供，故 (4) 完成所有情况。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_small_d_capacity_complete_reduction.py --verify
```

五条精确回执覆盖 \(b\le d\) 的因子转移、\(b<p,b>d\) 的交换、大余因子的普通
fixed-\(n\) 商，以及大余因子的长商折叠；不做历史范围扫描。
