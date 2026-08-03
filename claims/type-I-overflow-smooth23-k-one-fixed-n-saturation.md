---
kind: claim
claim_id: type-I-overflow-smooth23-k-one-fixed-n-saturation
title: 2,3-光滑二维 fixed-s overflow 的 k=1 fixed-n 饱和递降
statement: 设 P=2^a 3^b、p=4P+1 为素数，取 r=2、d=P/2、M=p+2、A=M，并令 n=2P+1。则 pn=4Md+1、R_M>p，且 S=Md 满足 A<S<=B_p=(p-1)^2/4。取 fixed-n 候选 L=S，得到 R_L=4S-n=(p-1)n-1、K_L=S(p-1)，恒等解提升和严格的 floor(B_p/A) 外层势下降。因此任何已证明可达的该 k=1 状态都有 verified fixed-n overflow 递降边；该结论不证明状态来源可达。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-fixed-s-23-smooth-residual
sources:
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: fixed-n bounded-divisor saturation theorem
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: exact k=1 smooth-family selector receipt
topics:
  - type-I
  - overflow
  - fixed-n
  - fixed-s
  - smooth-support
  - outer-rank
  - recursive-descent
  - typed-receipt
visibility: public
last_checked: '2026-08-04'
---

# 2,3-光滑二维 fixed-s overflow 的 (k=1) fixed-n 饱和递降

## 1. 参数族

令

\[
P=2^a3^b,\qquad a,b\ge1,
\qquad p=4P+1\ \text{为素数},
\]

并取

\[
r=2,\qquad d=P/2,\qquad M=p+2,\qquad A=M.
\]

由 (p=4P+1) 有

\[
n=4M-R_M=2P+1,
\qquad pn=4Md+1.
\]

因为 (P\ge18)（(P=6) 时 (4P+1=25) 不是素数），所以 (d\ge9)，从而

\[
S:=Md>A,
\qquad
R_M=4M-n=14P+7>p.
\]

这正是前一份 2,3-光滑 fixed-s residual 中参数 (k=1) 的二维 overflow。

## 2. fixed-n 饱和边

记

\[
B_p=\frac{(p-1)^2}{4}=4P^2.
\]

由于 (n=2P+1\le p-2=4P-1)，有

\[
S=\frac{pn-1}{4}\le B_p.
\]

因此 (L=S) 是 fixed-n 行列式的有界除子。它满足 (A<L\)、(4L>n)，且

\[
R_L=4L-n=(p-1)n-1,
\qquad
K_L=L\left(p-\frac{S}{L}\right)=S(p-1).
\]

直接计算得到

\[
pR_L+1=4K_L,
\qquad L\mid K_L.
\]

又 (L=S\ge2A)，故

\[
\left\lfloor\frac{B_p}{L}\right\rfloor
\le
\left\lfloor\frac{B_p}{2A}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

所以这是一个完整的 E1--E5 fixed-n 恒等提升边。由于 (R_L>p)，目标仍标记为
overflow，但 absorbed-support 外层势严格下降。

## 3. 逻辑边界

该引理是条件性递降结论：它假设参数状态已经有合法的 source/path/node provenance，
不从 (p=4P+1) 自动推出该状态在原始图表中可达。它覆盖参数族的全部 (k=1) 行；
(k\ge2) 时 (n\ge p)，低 (n) 饱和条件失效，仍需固定-n 的其它 2,3-光滑除子、
alternate carrier、Type II 或 q-进容量分支。

## 4. 聚焦回执

统一选择器在种子

\[
(a,b,p)\in\{(1,2,73),(3,1,97),(4,1,193),(2,3,433),(2,4,1297)\}
\]

上逐项重算 (M,d,n,S,R_L,K_L)、canonical chart、恒等解提升和外层势，生成
`smooth23_k_one_fixed_n_saturation` 回执。回执将 `source_reach_status` 保持为
`unproved`，因此不会把算术条件误写成来源可达性或全称证明。

重放命令：

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```
