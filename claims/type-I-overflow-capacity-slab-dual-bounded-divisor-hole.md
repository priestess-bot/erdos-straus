---
kind: claim
claim_id: type-I-overflow-capacity-slab-dual-bounded-divisor-hole
title: 高载体因子阈值残余的双有界除子空图谱
statement: 在高载体容量层因子阈值残余中，算术行 (p,d,n,M,A,b)=(73,13,1461,2051,293,7) 同时满足 pn=4Md+1、B_p<M<2B_p、c<=A<=B_p、A|M、1<b<=d 及 d*spf(b)>=p；但 S=Md=26663 的任意除子都不落在 A<L<=B_p，且 rd=91<A。因此固定-n 商模 p 折叠的全部有界除子候选与 fixed-s 的全部有界除子候选均为空。故因子阈值残余不能仅靠扩大两张有界除子 atlas 而全称闭合；该行只是算术边界，不带可达性或猜想反例断言。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-capacity-slab-factor-threshold-residual
  - type-I-overflow-fixed-n-quotient-fold-descent
  - type-I-overflow-fixed-s-bounded-divisor-saturation
topics:
  - type-I
  - overflow
  - high-carrier
  - capacity-window
  - factor-threshold
  - fixed-n
  - fixed-s
  - bounded-divisor
  - proof-boundary
  - selector
sources:
  - claim: type-I-overflow-capacity-slab-factor-threshold-residual
    role: residual-gate
  - claim: type-I-overflow-fixed-n-quotient-fold-descent
    role: complete-fixed-n-divisor-interface
  - claim: type-I-overflow-fixed-s-bounded-divisor-saturation
    role: fixed-s-divisor-interface
  - reproduction: reproductions/type_i_overflow_capacity_slab_dual_bounded_divisor_hole.py
    role: focused-single-row-receipt
visibility: public
last_checked: '2026-08-08'
---

# 高载体因子阈值残余的双有界除子空图谱

## 定理

令

\[
(p,d,n,M,A,b)=(73,13,1461,2051,293,7).
\tag{1}
\]

这是一条满足高载体容量层因子阈值残余全部算术门的行：若

\[
B_p=\frac{(p-1)^2}{4}=1296,
\qquad c=\frac{p-1}{4}=18,
\tag{2}
\]

则

\[
pn=4Md+1,
\qquad B_p<M<2B_p,
\qquad c\le A\le B_p,
\qquad A\mid M,
\tag{3}
\]

并且

\[
1<b=7\le13=d,
\qquad d\operatorname{spf}(b)=13\cdot7=91\ge73=p.
\tag{4}
\]

然而，固定-\(n\) 的完整商折叠所需的有界除子集

\[
\mathcal D_n=
\left\{L:L\mid Md,\ A<L\le B_p,
\left\lfloor\frac{B_p}{L}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor\right\}
\tag{5}
\]

为空；对偶 fixed-\(s\) 的候选集

\[
\mathcal D_s=
\left\{L:L\mid rd,\ A<L\le B_p,\ 4L>s,
\left\lfloor\frac{B_p}{L}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor\right\}
\tag{6}
\]

也为空，其中 \(r=M\bmod p\) 且 \(s=(4rd+1)/p\)。

所以，不能把“因子阈值残余总可由某个 fixed-\(n\) 或 fixed-\(s\) 有界除子闭合”
作为下一步命题。本结论是一个严格的算术反例，不声称 (1) 有递归来源回执，也不构成
Erdos--Straus 猜想的反例。

## 精确分解

由 (1)，

\[
2051=7\cdot293,
\qquad Md=26663=7\cdot13\cdot293.
\tag{7}
\]

因而

\[
\operatorname{Div}(Md)=
\{1,7,13,91,293,2051,3809,26663\}.
\tag{8}
\]

其中不小于 \(A=293\) 的下一项已经是 \(2051>B_p\)，而 \(L=293\) 又没有严格超过
\(A\)。故甚至不施加势条件，(5) 的区间门已经为空。固定-\(n\) 商模 \(p\) 折叠因此
没有任何可调用的除子；这包括普通 fixed-\(n\) 图表与其负图表折叠两侧。

另一方面，

\[
r=2051\bmod73=7,
\qquad rd=91,
\qquad s=\frac{4\cdot91+1}{73}=5.
\tag{9}
\]

而 \(\operatorname{Div}(rd)=\{1,7,13,91\}\) 的每一项都小于 \(A\)，所以 (6) 也在
carrier 门之前为空。

这条行还准确处于因子阈值菜单的未分流处：唯一非平凡余因子因子 \(g=7\) 满足

\[
dg=91\not<p,
\tag{10}
\]

余因子交换要求 \(d<b\) 而这里 \(13>7\)，并且 \(L=b=7<A\) 不能作 support-reset
折叠。于是它不是遗漏某个同一菜单的候选，而是两张完整有界除子 atlas 共同的明确空洞。

## 研究含义

这个边界排除了一个看似自然但错误的全称路线：只要把 \(L=b\) 扩大到所有
\(L\mid Md\)，再加上所有 \(L\mid rd\)，就能消除因子阈值残余。下一选择器必须加入
不同类型的出口，例如可验证的直接 Type I/II 终端、非有界除子的构造性变换，或带来源
标签的跨状态容量；不能将继续枚举这两张 atlas 误记为证明进展。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_capacity_slab_dual_bounded_divisor_hole.py --verify
```

该回执只重算 (1)--(10) 的单条精确算术行，不做历史范围扫描。
