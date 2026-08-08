---
kind: claim
claim_id: type-I-overflow-negative-fixed-n-reentry-reset
title: overflow 负固定-n 重入的支持重置递降
statement: 设核心素数 p=1 (mod 24) 的 verified overflow 满足 pn=4Md+1、S=Md，并携带 1<=A<=B_p=(p-1)^2/4 的 charged support。若某个 L|S 满足 A<L<=B_p、floor(B_p/L)<floor(B_p/A)，且 D=S/L-p 满足 1<=D<p，则令 u=n-4L。恒等式 pu=4LD+1 给出正整数 u，并使 (M_T,d_T,n_T;A_T)=(L,D,u;L) 成为合法 canonical overflow/marked 状态；它以 Sol(p) 恒等提升并通过完整 E1--E5，其中 outer support rank 严格下降。该卡是商模 p 折叠在 h=1 的特例；D>=p 的长余量也由后续的完整商折叠处理，不能再作为最终残余。
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
因此本卡单独闭合 \(Ad<2p\) 的短余量。若 \(Ad\ge2p\)，则 \(D\ge p\)，它不再
满足本卡的 \(h=1\) 门；但这不是最终残余，因为
[固定-\(n\) 商模 \(p\) 折叠的完整外层秩递降](type-I-overflow-fixed-n-quotient-fold-descent.md)
会把 \(D\) 继续约化到其非零模 \(p\) 余数。结合该一般引理后，整个小-\(d\) 容量层
由[完整余因子递降](type-I-overflow-small-d-capacity-complete-reduction.md)闭合。

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

有 \(D=103\ge p\)，所以不满足本卡的 \(h=1\) 门；完整商折叠则取
\(103\equiv6\pmod {97}\)，把它送到 \((101,6,25;101)\)。因此它是这个特例的边界，
而不是完整选择器的边界。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_negative_fixed_n_reentry_reset.py --verify
```

四条精确回执覆盖一个 \(L\nmid M\) 的一般除子、保留旧 support 的重入、素大余因子
reset，以及 \(D\ge p\) 的严格不适用边界；不做历史范围扫描。
