---
kind: claim
claim_id: type-I-overflow-smooth23-low-k-fixed-n-cofactor
title: 2,3-光滑二维 overflow 的低 k fixed-n cofactor 递降
statement: 设 P=2^a 3^b、p=4P+1 为素数，r=2、d=P/2、M=kp+2、A=M。令 q=2 当 2|d，否则令 q=3。若 1<=k<=floor((B_p-2q)/(q p))，则 fixed-n 行列式取 L=qM=S/(d/q)，其中 S=Md，给出正的 canonical chart、恒等解提升和严格的 floor(B_p/A) 外层势下降。该结论条件于状态已有合法来源回执，不证明参数状态从原始图表可达；超过阈值的高 k 行保留为分析残余。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-smooth23-k-one-fixed-n-saturation
sources:
  - claim: type-I-overflow-fixed-n-bounded-divisor-saturation
    role: fixed-n bounded-divisor E1--E5 lemma
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: exact low-k cofactor receipts
topics:
  - type-I
  - overflow
  - fixed-n
  - cofactor
  - smooth-support
  - outer-rank
  - recursive-descent
  - typed-receipt
visibility: public
last_checked: '2026-08-04'
---

# 2,3-光滑二维 overflow 的低 \(k\) fixed-n cofactor 递降

## 1. 参数与候选

令

\[
P=2^a3^b,\qquad a,b\ge1,\qquad p=4P+1\ \text{为素数},
\]

并取

\[
r=2,\qquad d=P/2,\qquad M=kp+2,\qquad A=M.
\]

由于 \(P=6\) 时 \(p=25\) 非素数，若 \(d\) 为奇数则 \(d=3^b\) 且 \(b\ge2\)；
因此下面的选择总是合法：

\[
q=
\begin{cases}
2,&2\mid d,\\
3,&2\nmid d.
\end{cases}
\qquad q\mid d,\quad q\ge2.
\]

由固定-\(n\) 行列式，

\[
n=4kd+1,\qquad pn=4Md+1,\qquad S=Md.
\]

令

\[
h=d/q,\qquad L=qM=M d/h=S/h.
\]

于是 \(L\mid S\)、\(L\ge2A\)，并且 \(L>A\)。

## 2. 容量与正性

状态参数范围 \(M\le B_p\) 等价于

\[
1\le k\le \left\lfloor\frac{B_p-2}{p}\right\rfloor.
\]

候选 \(L=qM\) 落入容量盒的充分且精确条件为

\[
qM\le B_p
\iff
1\le k\le \left\lfloor\frac{B_p-2q}{qp}\right\rfloor.
\]

对该范围内的 \(k\)，

\[
4L-n
=4q(kp+2)-4kd-1
=(16q-2)kP+4qk+8q-1>0.
\]

固定-\(n\) 目标图表定义为

\[
R_L=4L-n,\qquad K_L=L\left(p-\frac{S}{L}\right)
=qM(p-h).
\]

直接消元得到

\[
pR_L+1=4K_L,\qquad L\mid K_L,
\]

所以 \((p,R_L,K_L;L)\) 是合法 canonical chart。又因为 \(L\ge2A\)，

\[
\left\lfloor\frac{B_p}{L}\right\rfloor
\le
\left\lfloor\frac{B_p}{2A}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\]

固定-\(n\) 行列式的图表无关标记集给出恒等 E4，故该边满足完整 E1--E5，目标状态
仍可继续作为 overflow 递归节点。

## 3. 对保持 \(M\) 倍性的 fixed-\(n\) 子图的完备性

若限制候选保持旧支撑并写成

\[
L=Mu,\qquad u\mid d,\qquad u>1,
\]

则 \(u\) 的最小可能值就是 \(q=\operatorname{spf}(d)\)。因此在这个子图中：

\[
qM\le B_p
\quad\Longleftrightarrow\quad
\text{存在有界的 multiple-}M\text{ 候选},
\]

而

\[
qM>B_p
\quad\Longrightarrow\quad
\text{所有 }L=Mu,\ u\mid d,\ u>1\text{ 都越出容量盒}.
\]

这不是整个 fixed-\(n\) 因子图谱的完备性结论；仍可能存在
\(L\mid Md\) 但 \(M\nmid L\) 的支撑重置候选，必须单独枚举并支付外层势。

## 4. 覆盖范围与剩余边界

该引理覆盖每个合法种子从 \(k=1\) 到

\[
k_{\mathrm{cof}}=
\left\lfloor\frac{B_p-2q}{qp}\right\rfloor.
\]

当前五个种子的阈值为

\[
(p,q,k_{\mathrm{cof}})
=(73,3,5),(97,2,11),(193,2,23),(433,2,53),(1297,2,161).
\]

当 \(k>k_{\mathrm{cof}}\) 时，最小的这种 \(qM\) 已超过 \(B_p\)；这只排除了本条
规范 cofactor 候选，不能推出 fixed-\(n\) 因子图谱为空。剩余行应继续检查其它
\(L\mid Md\)，或转交 Type II、alternate carrier 与 q-进容量分支。

## 5. 逻辑边界与回执

该结论是“若状态可达，则有严格后继”的参数性引理；它不证明
\(P=2^a3^b\) 产生的形式状态实际出现在原始 F/G Reach 中，也不关闭高-\(k\) 残余。

统一选择器对五个种子分别重算 \(M,d,n,S,q,L,R_L,K_L\)、canonical chart、恒等
解提升和外层势，生成 smooth23_low_k_fixed_n_cofactor 回执。回执把
source_reach_status 保持为 unproved，并把高-\(k\) 部分保留为 analysis_evidence。

重放命令：

python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
