---
kind: claim
claim_id: type-I-raw-infinite-p-parent-ancestry-no-go
title: Primitive raw 节点的无穷 p-反向祖先与有限来源条件无效性
statement: 设 p 为奇素数，pR+1=4K，R>=3 且 p 不整除 R。每个正 primitive formal raw node P=(A,B,m) 都有显式无穷实际 p-反向祖先链 P_0=P，P_{j+1}=(p A_j^2,p A_j B_j-R,p A_j m_j-1)，并且每步以 q=p、shift=1、gcd reduction=A_j 恰回放到 P_j。因此，仅以“存在长度 L 的 actual primitive p-raw 前驱词”为条件、且不指定独立左端 root 的任意有限来源规则对全部 primitive node 都成立，不能承担 E1 source provenance。该结论特别排除把 c=9 的 m>1 dyadic 前驱或其 p-parent 延长为有限 raw word 后直接登记为 root。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-raw-universal-p-parent-root-policy-boundary
  - type-I-g-anchor-c9-dyadic-high-layer-predecessor
  - denominator-escape-state-contract
topics:
  - type-I
  - raw-path
  - p-parent
  - source-provenance
  - c9
  - E1
  - root-policy
  - proof-boundary
sources:
  - claim: type-I-raw-universal-p-parent-root-policy-boundary
    role: one-step-adjustable-p-parent
  - claim: type-I-g-anchor-c9-dyadic-high-layer-predecessor
    role: c9-dyadic-raw-predecessor-family
  - concept: denominator-escape-state-contract
    role: E1-root-scope-requirement
  - reproduction: reproductions/type_i_raw_infinite_p_parent_ancestry.py
    role: generic-and-c9-ancestry-replay-controls
visibility: public
last_checked: '2026-08-12'
---

# Primitive raw 节点的无穷 \(p\)-反向祖先

## 1. 设置与一步公式

固定

\[
p\ge5\text{ 为素数},
\qquad
pR+1=4K,
\qquad
R\ge3,
\qquad
p\nmid R.
\tag{1}
\]

令

\[
P=(A,B,m),
\qquad
A,B,m>0,
\qquad
A+B=Rm,
\qquad
(A,B)=1
\tag{2}
\]

为一个有序 primitive formal raw node。定义其定向 \(p\)-父节点为

\[
\boxed{
\operatorname{Par}_p(P)=
\left(pA^2,\ pAB-R,\ pAm-1\right).}
\tag{3}
\]

这是可调 \(p\)-parent 定理中，先交换目标坐标、再取 \(g=A\) 的特例；下文给出
直接验证，以保留迭代所需的精确方向和 gcd 回执。

## 2. 无穷祖先定理

**定理。** \(\operatorname{Par}_p(P)\) 仍是正 primitive formal raw node，并且有一条
实际 raw 边

\[
\boxed{
\operatorname{Par}_p(P)
\xrightarrow[q=p,\ \mathrm{shift}=1,
\ \gcd\ \mathrm{reduction}=A]{}
P.}
\tag{4}
\]

所以递归定义

\[
P_0=P,
\qquad
P_{j+1}=\operatorname{Par}_p(P_j)
\quad(j\ge0)
\tag{5}
\]

给出任意指定长度的 actual primitive \(p\)-raw 前驱词，进而给出无穷反向祖先链。

**证明。** 由 (2) 和 \((A,B)=1\)，有

\[
(A,R)=1,
\tag{6}
\]

因为 \(d\mid A,R\) 蕴含 \(d\mid A,Rm-A=B\)。又

\[
pA^2+(pAB-R)=pA(A+B)-R=R(pAm-1),
\tag{7}
\]

故 (3) 保持 formal invariant。正性由

\[
AB\ge Rm-1\ge R-1,
\qquad pAB>R
\tag{8}
\]

得到。primitive 性则是

\[
\gcd(pA^2,pAB-R)=1:
\tag{9}
\]

任一共同素因子若整除 \(A\)，由第二项模 \(A\) 等于 \(-R\) 和 (6) 矛盾；若是
\(p\)，则由 \(pAB-R\equiv-R\not\equiv0\pmod p\) 矛盾。

对 (3) 的第一坐标以 \(q=p\) 作 raw transition。其层数

\[
pAm-1\equiv-1\pmod p
\tag{10}
\]

强制 shift 为 \(1\)，且第二坐标模 \(p\) 是 \(-R\)，所以 unit 条件成立。又
\(p\nmid K\)，故第一坐标中的 \(p\) 是有效的超容量标签。未约分的像精确为

\[
\left(A^2,AB,Am\right).
\tag{11}
\]

它的三坐标 gcd 恰为 \(A\)，因为 \((A,B)=1\)。同时除以 \(A\) 后就是
\((A,B,m)\)，证明 (4)。由于 (3) 对每个 primitive node 都成立，归纳即得 (5)。
证毕。

## 3. E1 的有限祖先 no-go

固定任何 \(L\ge1\)。令一个“有限 raw 来源条件”只断言：给定节点存在一条长度至少
\(L\) 的反向词，词中每个节点均为正 primitive formal node，且每条边满足 actual
\(q=p\) raw transition 的容量、shift、unit 与 gcd-reduction 条件。定理把 (5) 的前
\(L\) 步作为该词，因此这个条件对 (1)--(2) 的**每一个**节点成立。

所以此类条件不能区分任何目标节点，特别不能支付状态合同的 E1：

\[
\boxed{
\text{有限长度 actual raw ancestry，若没有独立指定的左端 root，
不是 source provenance。}}
\tag{12}
\]

该结论的范围是精确的。它不排除一个在选择目标前独立定义、并带有内容摘要、scope、
normal-form adapter 和解提升的 root policy；它只排除用 (5) 的存在性补造这种 policy。

## 4. 对 \(c=9\) 的后果

在 \(c=9\) 图表中，每一个已知 dyadic 高层前驱

\[
P_\gamma=(2\gamma x,\ 2\gamma y-R,\ 2\gamma-1)
\tag{13}
\]

满足 (2)，并且该域有 \(2p<R<3p\)，故 \(p\nmid R\)。因此 (5) 直接给出

\[
\cdots\longrightarrow
\operatorname{Par}_p^2(P_\gamma)
\longrightarrow
\operatorname{Par}_p(P_\gamma)
\longrightarrow
P_\gamma
\xrightarrow[q=2]{}(x,y,1).
\tag{14}
\]

这说明把已有 \(S_1\) 或 \(S_B\) source 向左延长任意有限步，绝不会把它变成
target-independent 的 root-entry。c9 若要进入 verified edge，仍须提供有限 raw 图外的
E1 root policy，以及单独的 E3 adapter、E4 lift 与 E5 支付。

## 5. 定向控制

复现器重放以下两条无限链的有限前缀：

* \(p=73,R=71,K=1296\) 的 anchor \((1,70,1)\)；
* \(p=193,R=511,K=24656\) 的 c9 dyadic node \((736,797,3)\)。

每一步重算 formal invariant、primitive 性、\(p\)-容量、shift、unit 条件和实际
gcd reduction；它不做素数扫描或覆盖率声明。

```bash
python3 reproductions/type_i_raw_infinite_p_parent_ancestry.py --verify
```
