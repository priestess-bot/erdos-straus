---
kind: claim
claim_id: type-I-overflow-high-carrier-fixed-n-R-descent
title: 高载体 overflow 固定 n 有界除子的 R 严格递降
statement: 设 verified overflow 满足 pn=4Md+1、S=Md、A≤B_p=(p-1)^2/4，且 M>B_p。若存在被有界固定-n 选择器接受的 L|S，满足 A<L≤B_p、4L>n 和 floor(B_p/L)<floor(B_p/A)，则 L<M，因而 R_L=4L-n<R_M=4M-n；结合固定-n 行列式恒等式、Sol(p) 恒等提升和吸收支撑势下降，该边同时携带一个严格 canonical-R 次级秩下降。该引理是条件性的：它不证明这样的 L 必然存在，也不把高载体残余改写成已闭合分支。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - type-I-overflow-same-chart-support-promotion
  - denominator-escape-state-contract
topics:
- type-I
- overflow
- high-carrier
- fixed-n
- bounded-divisor
- canonical-R
- outer-rank
- well-founded-descent
- typed-receipt
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: high-carrier R descent field and verifier
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused high-carrier replay
visibility: public
last_checked: '2026-08-03'
---

# 高载体 overflow 固定 \(n\) 有界除子的 \(R\) 严格递降

## 1. 条件性引理

设一个已验证 overflow 状态满足

\[
pn=4Md+1,
\qquad
S=Md=\frac{pn-1}{4},
\qquad
A\le B_p:=\frac{(p-1)^2}{4},
\qquad
M>B_p.
\tag{1}
\]

若固定-\(n\) 有界除子选择器接受某个 \(L\mid S\)，则它已经验证

\[
A<L\le B_p,
\qquad
4L>n,
\qquad
\left\lfloor\frac{B_p}{L}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{2}
\]

由 (1)--(2) 立即得到

\[
L\le B_p<M.
\tag{3}
\]

来源和后继的 canonical 模数分别为

\[
R_M=4M-n,
\qquad
R_L=4L-n.
\]

因此

\[
R_M-R_L=4(M-L)>0,
\qquad
R_L<R_M.
\tag{4}
\]

这不是“载体较小所以秩下降”的启发式，而是同一固定-\(n\) 图表恒等式中的精确
差值。\(R_L\) 可以仍大于 \(p\)，此时后继仍是 overflow；(4) 只说明它在
canonical-\(R\) 次级秩上严格下降。

## 2. 与完整边的组合

由于 \(L\mid S\) 且 \(4L>n\)，有 \(S/L<p\)，从而

\[
K_L=L\left(p-\frac SL\right)>0,
\qquad
4K_L=pR_L+1,
\qquad
L\mid K_L.
\]

固定-\(n\) 有界除子主张已经给出：

1. canonical chart 的合法性和 \(R_L\equiv3\pmod4\)；
2. 以图表无关的 \(\operatorname{Sol}(p)\) 作恒等解提升；
3. \(\lfloor B_p/L\rfloor<\lfloor B_p/A\rfloor\) 的 absorbed-support 外层势下降；
4. \(A\nmid L\) 时显式支付 support reset，而不是声称支撑保持。

所以高载体接受边同时拥有完整 E1--E5，并额外记录 (4) 的 canonical-\(R\) 下降。
这个 \(R\) 字段应被理解为高载体出口的次级秩：若后续允许重新进入高载体阶段，仍需
给出更外层的相位排序或证明组合势下降；不能只凭 (4) 宣称整个 overflow 图无环。

## 3. 高载体残余的精确边界

若不存在满足 (2) 的 \(L\)，本引理不产生后继。结合同图表支撑升级的余项计算，
高载体来源还满足 \(n\ge p+4\)；因此剩余问题应转向：

- 找到一个满足 (2) 的固定-\(n\) 除子；
- 证明固定-\(s\) 或 source/path/node alternate 的可提升边；
- 或构造直接 Type I/II 终端、容量矛盾或另一个良基外层秩。

特别是，\(M>B_p\) 本身并不反驳 Erdos--Straus 猜想，也不意味着没有其它出口。

## 4. 聚焦回放

统一选择器对 12 个固定-\(n\) 有界除子回执逐行重算高载体字段。只有一条来源进入
\(M>B_p\) 域，并且得到严格下降：

\[
(p,M,A,n,L)=(73,1518,66,379,1288),
\]

\[
B_{73}=1296,
\qquad
R_M=3743,
\qquad
R_L=2823,
\qquad
R_M-R_L=920.
\]

因此回放计数为

\[
\texttt{high\_carrier\_verified\_edge\_count}=1,
\qquad
\texttt{high\_carrier\_R\_descent\_count}=1.
\]

这是选择器合同的有限回放，不是对所有高载体 overflow 的存在性扫描。

复现命令：

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
