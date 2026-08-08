---
kind: claim
claim_id: type-I-overflow-capacity-slab-dual-bounded-divisor-hole
title: 高载体因子阈值残余的双有界除子空图谱
statement: 在高载体容量层因子阈值残余中，算术行 (p,d,n,M,A,b)=(73,13,1461,2051,293,7) 同时满足 pn=4Md+1、B_p<M<2B_p、c<=A<=B_p、A|M、1<b<=d 及 d*spf(b)>=p；但 S=Md=26663 的任意除子都不落在 A<L<=B_p，且 rd=91<A，因此固定-n 商模 p 折叠与 fixed-s 的全部有界除子候选均为空。更强地，(p,d,n,M,A,b)=(673,647,830325,215923,821,263) 从 canonical 父态 (R,K;A)=(527,88668;821) 的 clean external slab (Q,alpha,beta)=(263,2,1) 满足全部整数来源门后得到，仍有两张 atlas 同时为空；但该 p 有独立 gap-7 Type I 终端。故仅扩大有界除子 atlas 或只使用 clean-slab 算术都不能全称闭合残余；这两行均不带完整 source/path 可达性或猜想反例断言。
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
    role: focused-two-row-receipt
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

## clean-slab 加强边界

上面的最小行只使用 determinant 算术。下列第二行表明，即使补上
`marked_external_accumulation` 的 clean external slab **整数接口**，仍不能从该接口本身
推出两张有界除子 atlas 的出口。

令

\[
p=673,
\qquad (R_0,K_0;A)=(527,88668;821).
\tag{11}
\]

则

\[
4K_0=pR_0+1,
\qquad 3\le R_0\le p-2,
\qquad R_0\equiv3\pmod4,
\qquad A\mid K_0,
\qquad A\le K_0\le B_{673},
\qquad K_0/A=108.
\tag{12}
\]

取

\[
Q=263,
\qquad \alpha=2,
\qquad \beta=1.
\tag{13}
\]

其中 \(Q\) 是素数、\(Q\nmid K_0\)，而

\[
Q\alpha+\beta=526+1=R_0,
\qquad (Q\alpha,\beta)=1,
\qquad \alpha\beta=2\mid K_0.
\tag{14}
\]

所以 (12)--(14) 是 clean slab 的全部整数输入条件。将其累积到

\[
M=AQ=215923
\tag{15}
\]

后，规范重图表给出

\[
R_M=33367>p,
\qquad K_M=5613998=M\cdot26,
\tag{16}
\]

从而

\[
(d,n)=(p-26,4M-R_M)=(647,830325),
\qquad pn=4Md+1.
\tag{17}

\]

这里 \(B_{673}=112896\)，故

\[
B_{673}<M<2B_{673},
\qquad 168=c\le821=A\le B_{673},
\qquad b=M/A=263\le d.
\tag{18}
\]

并且 \(d\operatorname{spf}(b)=647\cdot263\ge673\)，所以这仍是因子阈值残余。
然而

\[
Md=821\cdot263\cdot647,
\tag{19}
\]

其严格大于 \(A=821\) 的最小非平凡除子已经是

\[
263\cdot647=170161>B_{673}
\quad\text{或}\quad
821\cdot263=M>B_{673}.
\tag{20}

因此 \(\mathcal D_n=\varnothing\)。同时

\[
r=M\bmod p=563,
\qquad rd=563\cdot647,
\qquad s=2165,
\tag{21}

\]

而 \(563,647<A\)、\(563\cdot647>B_{673}\)，故 \(\mathcal D_s=\varnothing\)。

这里必须保留一个关键限定：\(p=673\) 自身有独立的 gap-7 Type I 终端

\[
x=170,
\qquad d_{\mathrm{cert}}=5,
\qquad
\frac4{673}=\frac1{170}+\frac1{16345}+\frac1{374006290}.
\tag{22}

\]

所以完整 selector 的 terminal-first 规则会先截断这条算术构造。它不是未解决核心的
source/path 反例；它严格排除的只是“clean slab 的整数合同自动制造有界除子出口”这一
错误推论。

## 研究含义

这个边界排除了一个看似自然但错误的全称路线：只要把 \(L=b\) 扩大到所有
\(L\mid Md\)，再加上所有 \(L\mid rd\)，就能消除因子阈值残余。加强行还排除了把
clean external slab 的整数等式单独升级为这种闭合定理。下一选择器必须将可验证的直接
Type I/II 终端、完整 source/path/F--G 数据或带来源标签的跨状态容量作为独立输入；不能将
继续枚举这两张 atlas 或重排 clean slab 因子误记为证明进展。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_capacity_slab_dual_bounded_divisor_hole.py --verify
```

该回执重算基本空洞及 clean-slab 加强空洞的两条精确算术行，不做历史范围扫描。
