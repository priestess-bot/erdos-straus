---
kind: claim
claim_id: type-I-overflow-fixed-n-quotient-fold-descent
title: overflow 固定-n 商模 p 折叠的完整外层秩递降
statement: 设核心素数 p=1 (mod 24) 的 verified overflow 满足 pn=4Md+1、S=Md，并携带 1<=A<=B_p=(p-1)^2/4 的 charged support。若存在 L|S 满足 A<L<=B_p 且 floor(B_p/L)<floor(B_p/A)，令 q=S/L=ph+delta，其中 h>=0、1<=delta<p；则 n_T=n-4Lh 是正整数，且 (M_T,d_T,n_T;A_T)=(L,delta,n_T;L) 是完整 E1--E5 的递降后继。q<p 时 h=0，恢复既有正 fixed-n 边；q>p 时 h>=1，给出折叠的负 fixed-n 重入。因而固定-n 有界除子边不需要另行假设 4L>n：严格外层秩的有界除子本身已经足以给出后继。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-n-bounded-divisor-saturation
topics:
  - type-I
  - overflow
  - fixed-n
  - quotient-fold
  - reentry
  - support-reset
  - well-founded-descent
  - selector
sources:
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: original-positive-fixed-n-branch-and-shared-rank-contract
  - reproduction: reproductions/type_i_overflow_fixed_n_quotient_fold_descent.py
    role: focused-four-route-receipt
visibility: public
last_checked: '2026-08-08'
---

# overflow 固定-\(n\) 商模 \(p\) 折叠的完整外层秩递降

## 定理

设 \(p\equiv1\pmod {24}\) 为素数，一个已有 source/path/node 回执的 verified
overflow 满足

\[
pn=4Md+1,
\qquad S=Md,
\qquad 1\le d<p,
\tag{1}
\]

并携带 charged support \(1\le A\le B_p:=(p-1)^2/4\)。若某个除子 \(L\mid S\)
满足

\[
A<L\le B_p,
\qquad
\left\lfloor\frac{B_p}{L}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor,
\tag{2}
\]

写其商的 Euclidean 分解为

\[
q:=\frac SL=ph+\delta,
\qquad h\ge0,
\qquad 1\le\delta<p.
\tag{3}
\]

则

\[
n_T:=n-4Lh,
\qquad M_T:=L,
\qquad d_T:=\delta,
\qquad A_T:=L
\tag{4}
\]

定义一条完整的
`overflow_fixed_n_quotient_fold_outer_rank_v1` 边。精确地，

\[
pn_T=4M_Td_T+1,
\tag{5}
\]

且 canonical 坐标

\[
R_T=4L-n_T>0,
\qquad K_T=L(p-\delta)>0,
\qquad pR_T+1=4K_T,
\qquad L\mid K_T.
\tag{6}
\]

这条边以 \(\operatorname{Sol}(p)\) 恒等提升，并以 (2) 的严格外层秩下降支付
support reset。特别地，存在满足 (2) 的 \(L\) 已足以构造后继；不需要额外假设
\(4L>n\)。

## 商折叠恒等式

先注意 \(p\nmid q\)：否则 \(p\mid S=Lq\)，与
\(4S=pn-1\equiv-1\pmod p\) 矛盾。因此 (3) 中的 \(\delta\) 确实属于
\(\{1,\ldots,p-1\}\)。由 (1) 和 (3)，

\[
\begin{aligned}
p(n-4Lh)
&=pn-4Lph\\
&=4Lq+1-4Lph\\
&=4L\delta+1.
\end{aligned}
\tag{7}
\]

右端为正，故 \(n_T>0\)。又 \(\delta<p\) 和 \(L\ge2\) 给出

\[
pn_T=4L\delta+1\le4L(p-1)+1<4Lp,
\qquad 0<n_T<4L.
\tag{8}
\]

因为 \(p\equiv1\pmod4\)，(7) 蕴含 \(n_T\equiv1\pmod4\)。所以
\(R_T=4L-n_T\) 是正的 \(3\pmod4\) canonical 代表。再由 (7)，

\[
pR_T+1
=4pL-pn_T+1
=4L(p-\delta)=4K_T,
\tag{9}
\]

从而得到 (5)--(6)。

## E1--E5 与两侧统一

E1 继承输入的 source/path/node 回执；E2--E3 是 (5)--(9) 的整数恒等式及 target
normal form；E4 取 \(W_T=W_S=\operatorname{Sol}(p)\) 和恒等映射；E5 正是 (2)。
目标 support 设为 \(A_T=L\)，若 \(A\nmid L\) 则由同一严格外层势显式支付重置。

当 \(q<p\) 时 \(h=0\)、\(n_T=n\)、\(\delta=q\)，这就是已有的正 fixed-\(n\)
有界除子边，且 (8) 等价于 \(4L>n\)。当 \(q>p\) 时 \(h\ge1\)，(4) 把原来
负的 \(4L-n\) 重入为新的正 determinant 坐标。旧的 \(D<p\) 负重入正是
\(q=p+D\) 且 \(h=1\) 的特例；若 \(D\ge p\)，本折叠仍然有效，不应把它误记为
递归边的边界。

## 聚焦复现

```bash
python3 reproductions/type_i_overflow_fixed_n_quotient_fold_descent.py --verify
```

四条精确回执覆盖普通 \(q<p\) 固定-\(n\) 边、\(h=1\) 且 \(L\nmid M\) 的折叠、
support-preserving 折叠与 \(h=2\) 的长商折叠；不做历史范围扫描。
