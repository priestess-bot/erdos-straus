---
kind: claim
claim_id: type-I-overflow-negative-fixed-n-reentry-reset
title: overflow 负固定-n 重入的支持重置递降
statement: 设核心素数 p=1 (mod 24) 的 verified overflow 满足 pn=4Md+1、S=Md，并携带 1<=A<=B_p=(p-1)^2/4 的 charged support。若某个 L|S 满足 A<L<=B_p、floor(B_p/L)<floor(B_p/A)，且 D=S/L-p 满足 1<=D<p，则令 u=n-4L。恒等式 pu=4LD+1 给出正整数 u，并使 (M_T,d_T,n_T;A_T)=(L,D,u;L) 成为合法 canonical overflow/marked 状态；它以 Sol(p) 恒等提升并通过完整 E1--E5，其中 outer support rank 严格下降。对小-d 容量层的素大余因子残余，取 L=b=M/A 时 D=Ad-p；故 Ad<2p 的全部残余都被该边闭合，真正余项必有 Ad>=2p（从而 d>=5）。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-small-d-capacity-prime-residual-dichotomy
topics:
  - type-I
  - overflow
  - fixed-n
  - negative-chart
  - reentry
  - support-reset
  - denominator-descent
  - well-founded-descent
  - selector
sources:
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: shared-support-rank-and-identity-lift-contract
  - claim: type-I-overflow-small-d-capacity-prime-residual-dichotomy
    role: prime-large-residual-specialization
  - reproduction: reproductions/type_i_overflow_negative_fixed_n_reentry_reset.py
    role: focused-four-route-receipt
visibility: public
last_checked: '2026-08-08'
---

# overflow 负固定-\(n\) 重入的支持重置递降

## 定理

设 \(p\equiv1\pmod {24}\) 为素数，且一个已有 source/path/node 回执的 verified
overflow 满足

\[
pn=4Md+1,
\qquad S=Md,
\qquad 1\le d<p.
\tag{1}
\]

令当前 charged support 满足 \(1\le A\le B_p:=(p-1)^2/4\)。若存在一个除子
\(L\mid S\) 满足

\[
A<L\le B_p,
\qquad
\left\lfloor\frac{B_p}{L}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor,
\tag{2}
\]

并且其“负固定-\(n\)”余量

\[
D:=\frac SL-p
\tag{3}
\]

满足 \(1\le D<p\)，则定义

\[
u:=n-4L,
\qquad
M_T=L,
\qquad d_T=D,
\qquad A_T=L.
\tag{4}
\]

这给出一条完整的
`overflow_negative_fixed_n_reentry_reset_v1` 边：目标满足

\[
pu=4M_Td_T+1,
\tag{5}
\]

并且其 canonical chart 为

\[
R_T=4L-u>0,
\qquad K_T=L(p-D)>0,
\qquad pR_T+1=4K_T,
\qquad L\mid K_T.
\tag{6}
\]

它以 \(W_T=W_S=\operatorname{Sol}(p)\) 的恒等映射提升全部标记解，并以
\(\lfloor B_p/L\rfloor<\lfloor B_p/A\rfloor\) 支付 support reset 的严格外层秩。
因此这是一个真正的 E1--E5 递降，而不是把负的 \(4L-n\) 当作未解释的候选。

## 证明

由 (1) 和 (3)，

\[
\begin{aligned}
p(n-4L)
&=pn-4pL\\
&=4S+1-4pL\\
&=4L\left(\frac SL-p\right)+1
=4LD+1.
\end{aligned}
\tag{7}
\]

所以 \(u\) 是正整数。事实上 \(D>0\) 时 (7) 的右端为正；而 \(D<p\) 时

\[
pu=4LD+1<4Lp,
\qquad 0<u<4L.
\tag{8}
\]

由于 \(p\equiv1\pmod4\)，(7) 还给出 \(u\equiv1\pmod4\)。于是
\(R_T=4L-u\) 是正的 \(3\pmod4\) canonical 代表。由 (5) 直接计算

\[
pR_T+1
=4pL-pu+1
=4L(p-D)=4K_T.
\tag{9}
\]

\(D<p\) 保证 \(K_T>0\)，而 \(L\mid K_T\) 显然。因此 (4)--(6) 给出合法的
determinant normal form；\(R_T<p\) 时它是 marked absorb，\(R_T>p\) 时它仍是
overflow，二者均合法。

E1 继承输入的 source/path/node 回执；E2--E3 是 (5)--(9) 的整数恒等式和 normal
form；E4 使用图表无关的 \(\operatorname{Sol}(p)\) 恒等提升；E5 正是 (2)。目标
charged support 设为 \(A_T=L\)，故 \(A\nmid L\) 时的支撑更换由同一个严格 outer
rank 显式支付。这完成证明。

## 小-\(d\) 素大余因子残余的收缩

在[高载体小 \(d\) 容量层的素大余因子残余二分](type-I-overflow-small-d-capacity-prime-residual-dichotomy.md)
的残余中，取 \(L=b=M/A\)。此时

\[
\frac SL=\frac{M d}{b}=Ad,
\qquad D=Ad-p,
\qquad u=n-4b.
\tag{10}
\]

该残余已经有 \(4b\le n\)，而 \(D=0\) 会使 (7) 给出 \(pu=1\)，不可能；所以
\(D\ge1\)。若 \(Ad<2p\)，则 \(D<p\)，本定理立即给出完整 reentry-reset 边。
因此三类旧规则加上本卡后，真正的素大余因子余项必须满足

\[
b\text{ 为素数},
\qquad p<b<2(p-1),
\qquad Ad\ge2p.
\tag{11}
\]

此前已证明这类容量层有 \(A<p/2\)，所以 (11) 强制 \(d>4\)，即 \(d\ge5\)。

短余量例

\[
(p,d,n,M,A,b)=(73,4,329,1501,19,79)
\]

有 \(D=3\)、\(u=13\)，故本卡将其送到

\[
(M_T,d_T,n_T;A_T)=(79,3,13;79),
\]

并严格降低 \(\lfloor1296/A\rfloor\) 从 \(68\) 到 \(16\)。相反，

\[
(p,d,n,M,A,b)=(97,5,833,4040,40,101)
\]

有 \(D=103\ge p\)，所以不满足本定理的 \(d_T<p\) 门；这只是新门的精确边界，
不表示其它终端或 alternate 不存在。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_negative_fixed_n_reentry_reset.py --verify
```

四条精确回执覆盖一个 \(L\nmid M\) 的一般除子、保留旧 support 的重入、素大余因子
reset，以及 \(D\ge p\) 的严格不适用边界；不做历史范围扫描。
