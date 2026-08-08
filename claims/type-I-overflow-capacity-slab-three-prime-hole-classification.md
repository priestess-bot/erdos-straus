---
kind: claim
claim_id: type-I-overflow-capacity-slab-three-prime-hole-classification
title: 高载体三素因子残差的双图谱空洞分类
statement: 对一个 verified overflow，若 M=Ab 且 A、b、d 为满足支撑大小条件的三枚两两不同素数，并且 Md=A*b*d 的四个可能的严格超 A 除子全部被容量边界排除；若 r=M mod p 与 d 也是两枚不超过 A 的不同素数，且 rd 同样跨过 (A,B_p]，则 fixed-n 与 fixed-s 的完整有界除子 atlas 同时为空。该引理解释 p=73 与 p=673 的两个精确残差行，但不声称来源可达性、递归不可达性或 Erdos--Straus 反例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-capacity-slab-factor-threshold-residual
  - type-I-overflow-capacity-slab-dual-bounded-divisor-hole
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
  - arithmetic-hole
  - proof-boundary
sources:
  - claim: type-I-overflow-capacity-slab-factor-threshold-residual
    role: residual-gate
  - claim: type-I-overflow-capacity-slab-dual-bounded-divisor-hole
    role: exact-control-rows
  - claim: type-I-overflow-fixed-n-quotient-fold-descent
    role: fixed-n-selector-interface
  - claim: type-I-overflow-fixed-s-bounded-divisor-saturation
    role: fixed-s-selector-interface
  - reproduction: reproductions/type_i_overflow_capacity_slab_three_prime_hole.py
    role: structural-two-row-receipt
visibility: public
last_checked: '2026-08-09'
---

# 高载体三素因子残差的双图谱空洞分类

## 引理

令 \(p\equiv1\pmod {24}\) 为素数，并令

\[
B_p=\frac{(p-1)^2}{4},
\qquad
c=\frac{p-1}{4}.
\]

设一个已有 source/path/node 回执的 verified overflow 满足

\[
pn=4Md+1,
\qquad
B_p<M<2B_p,
\qquad
c\le A\le B_p,
\qquad
M=Ab,
\qquad
1<b\le d,
\qquad
db\ge p.
\tag{1}
\]

再假设 \(A,b,d\) 是两两不同的素数，\(b,d\le A\)，并且

\[
Ab>B_p,
\qquad
Ad>B_p,
\qquad
bd\le A\quad\text{或}\quad bd>B_p.
\tag{2}
\]

令 \(r\) 是 \(M\bmod p\) 的代表，且令 \(s=(4rd+1)/p\)。若 \(r,d\) 是不超过
\(A\) 的不同素数，并且

\[
rd\le A\quad\text{或}\quad rd>B_p,
\tag{3}
\]

则固定-\(n\) 和 fixed-\(s\) 的有界除子集合都为空：

\[
\begin{aligned}
\mathcal D_n&=\{L:L\mid Md, A<L\le B_p\}=\varnothing,\\
\mathcal D_s&=\{L:L\mid rd, A<L\le B_p\}=\varnothing.
\end{aligned}
\tag{4}
\]

因此，加入原有的外层秩条件
\(\lfloor B_p/L\rfloor<\lfloor B_p/A\rfloor\)、fixed-\(s\) 的
\(4L>s\) 或任何其它正性条件，也不能从这两张 atlas 产生递降边。

这里的结论只是在明确的三素因子边界内分类算术空洞；它不排除直接 Type I/II
证书、其它 carrier、Fourier/格证书或带来源标签的跨状态递降。

## 证明

由 \(A,b,d\) 两两不同且为素数，

\[
Md=Abd
\]

是平方自由的，所有除子恰为

\[
1, A, b, d, Ab, Ad, bd, Abd.
\tag{5}
\]

其中 \(b,d\le A\)，所以单素因子不落在严格区间 \((A,B_p]\)；\(Ab=M>B_p\)，
\(Ad>B_p\)，且 \(Abd>B_p\)。最后，(2) 已排除唯一剩余候选 \(bd\) 落在
\((A,B_p]\)。这证明了 \(\mathcal D_n=\varnothing\)。

同理，(r,d) 是不同素数，故

\[
\operatorname{Div}(rd)=\{1,r,d,rd\}.
\tag{6}
\]

前两个非平凡除子不超过 \(A\)，而 (3) 排除 \(rd\) 落在严格区间，故
\(\mathcal D_s=\varnothing\)。由 \(pn=4Md+1\) 及 \(M\equiv r\pmod p\)，还自动有
\(p\mid4rd+1\)，所以 \(s\) 的定义与 fixed-\(s\) 图表一致。证毕。

## 两个精确控制

### \(p=73\)

取

\[
(d,n,M,A,b,r,s)=(13,1461,2051,293,7,7,5),
\qquad B_{73}=1296.
\]

这里 \(M=7\cdot293\)、\(Md=7\cdot13\cdot293\)，且

\[
bd=91\le A,
\qquad
Ad=3809>B_{73},
\qquad
rd=91\le A.
\]

所以引理给出两张 atlas 的空洞。该素数另有独立的 gap-7 终端

\[
\frac4{73}=\frac1{20}+\frac1{219}+\frac1{4380},
\tag{7}
\]

故这里不是猜想反例，而是“有界除子菜单并不自动闭合”的正控制。

### \(p=673\)

取

\[
(d,n,M,A,b,r,s)=(647,830325,215923,821,263,563,2165),
\qquad B_{673}=112896.
\]

这里 \(M=263\cdot821\)，并且

\[
bd=170161>B_{673},
\qquad
Ad=531187>B_{673},
\qquad
rd=364261>B_{673}.
\]

所以同样得到双 atlas 空洞；但该素数有独立的 gap-7 Type I 终端

\[
\frac4{673}=\frac1{170}+\frac1{16345}+\frac1{374006290}.
\tag{8}
\]

这条加强控制说明：即使 clean external slab 的整数输入已经完整满足，仍不能把
“双 atlas 空洞”升级为 source/path 层面的未解状态。

## 研究边界

该引理把两个孤立的双空洞例子提升为可检查的结构性子类，但它只消解“继续枚举
\(L\mid Md\) 或 \(L\mid rd\) 必然找到有界除子”的错误假设。要推进统一选择器，下一
步仍需把这些算术行与真实 source/path 标签连接，并证明它们必然触发直接终端、跨状态
容量证书、其它非平方自由 carrier，或严格良基递降中的一个。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_capacity_slab_three_prime_hole.py --verify
```

该回执只验证引理假设、完整除子枚举、两个空洞及两个终端恒等式，不做历史范围扫描。
