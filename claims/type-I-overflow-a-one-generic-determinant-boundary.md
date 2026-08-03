---
kind: claim
claim_id: type-I-overflow-a-one-generic-determinant-boundary
title: A=1 overflow 的小载体假设边界
statement: 旧的“所有 A=1 overflow 取 L=d”结论需要额外假设 M<p。若 verified overflow 满足 pn=4Md+1、R_M=4M-n>p 且 M<p，则 d≥2、L=d 给出合法固定-n identity-lift 边；不加 M<p 时该结论为假，(p,M,d,n)=(73,1297,29,2061) 满足行列式 overflow 但 L=d 的图表为负，且 B_p 以下没有正候选除子。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-fixed-n-bounded-divisor-saturation
topics:
- type-I
- overflow
- determinant
- fixed-n
- A-one
- small-carrier
- negative-boundary
- proof-audit
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: exact arithmetic negative-boundary receipt and verifier
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: replayable A=1 boundary data
visibility: public
last_checked: '2026-08-03'
---

# A=1 overflow 的小载体假设边界

## 1. 正确的受限引理

设

\[
pn=4Md+1,\qquad R_M=4M-n>p,\qquad M<p.
\tag{1}
\]

因为 \(p\equiv1\pmod4\)，所以 \(n\equiv1\pmod4\)。若 \(d=1\)，则

\[
n=\frac{4M+1}{p}<4+\frac1p,
\]

从而 \(n=1\)，进而 \(M=(p-1)/4\) 且

\[
R_M=4M-1=p-2<p,
\]

与 overflow 矛盾。因此 \(d\ge2\)。取 \(L=d\)，则

\[
R_d=4d-n,\qquad K_d=d(p-M)>0.
\]

并且

\[
pR_d+1=4d(p-M).
\]

因此 \(R_d>0\)：否则左端不可能等于正的四的倍数。另一方面，overflow 给出
\(4M>p+n\)，而 (1) 给出

\[
4d=\frac{pn-1}{M}
<\frac{4pn}{p+n}
\le p+n.
\]

所以 \(0<R_d<p\)，且 \(d\mid K_d\)。当旧 support 为 \(A=1\) 时，这条边支付
\(\lfloor B_p/d\rfloor<B_p\) 的外层势下降，正是旧 claim 中 \(L=d\) 论证成立的范围。

## 2. 不加 \(M<p\) 的严格负边界

取

\[
(p,M,d,n)=(73,1297,29,2061).
\]

直接计算

\[
4Md+1=150453=73\cdot2061,\qquad
R_M=4M-n=3127>73,
\]

所以这是满足 determinant overflow 恒等式的 \(A=1\) 算术状态。令

\[
S=Md=37613=29\cdot1297,\qquad
B_p=\frac{(73-1)^2}{4}=1296.
\]

其不超过 \(B_p\) 的全部除子只有 \(1,29\)。但

\[
4\cdot1-n=-2057<0,\qquad
4\cdot29-n=-1945<0.
\]

所以没有满足 \(4L>n\) 的有界固定-\(n\) 除子；特别地，\(L=d\) 不是合法图表。该
回执还记录 \(K_M=M(73-29)=57068\) 及
\(73R_M+1=4K_M\)，因此负边界不是行列式算术错误。

## 3. 逻辑范围

该 tuple 没有 raw Reach、source/path/node 或 complete-excess provenance，不能作为
Erdős--Straus 猜想的反例；它只反驳“任意 determinant overflow 且 \(A=1\) 都有
\(L=d\)”这一过强的中间命题。统一选择器将其标成 analysis_evidence、
recursive_edge_eligible=false，并把当前全称目标修正为：

1. 小载体子族 \(M<p\) 的 \(A=1\) 边已闭合；
2. 一般 \(A=1\) 的固定-\(n\) 除子可能为空，但对偶 \(d/r\) RESET 已给出独立的
   E1--E5 算术出口；
3. 递归可达 \(A>1\) 的外层秩存在性仍未证明。

重放命令：

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
