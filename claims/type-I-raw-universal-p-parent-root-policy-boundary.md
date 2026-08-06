---
kind: claim
claim_id: type-I-raw-universal-p-parent-root-policy-boundary
title: 任意 primitive raw node 的 p-parent 反向提升与 root-policy 边界
statement: 设 p 为奇素数、pR+1=4K、R>=3 且 p 不整除 R。对任意正 primitive formal raw node P=(A,B,m) 与任意 g>0，若 pgA>R，则显式 triple S_g=(pgB,pgA-R,pgm-1) 在且仅在 (g,R)=1、(B,pgm-1)=1 时是正 primitive formal node；它有一条实际 q=p raw 边以 shift=1、gcd reduction=g 送到 P（至多交换坐标）。特别地 g=B 总可用，故“某节点有可回放的 p-raw 父节点”是普遍形式事实，不能单独充当 E1 source provenance；g=1 的无约分版本则有额外、可研究的互素门。任何新增 root-entry 仍须由 target-independent 的具名 policy、scope、E2/E3 normal form、全域 E4 lift 与 E5 另行准入。该构造对 c=9 dyadic high-layer nodes 和 c=3 complement seed 都适用，但不把它们自动升级为 verified edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-g-anchor-c9-dyadic-high-layer-predecessor
  - type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - raw-path
  - p-parent
  - source-provenance
  - root-policy
  - c3
  - c9
  - E1
  - proof-boundary
sources:
  - claim: type-I-g-anchor-marked-raw-peeling-calculus
    role: formal-raw-transition-semantics
  - claim: type-I-g-anchor-c9-dyadic-high-layer-predecessor
    role: dyadic-target-instances
  - claim: type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
    role: root-entry-admission-requirements
  - concept: denominator-escape-state-contract
    role: E1-to-E5-root-scope-contract
visibility: public
last_checked: '2026-08-06'
---

# 任意 primitive raw node 的 \(p\)-parent 反向提升与 root-policy 边界

本卡给出 raw 图中的一个普遍反向构造。它是 formal raw source 的算术事实，
**不是**新建递归根或解提升的许可。

## 1. 可调 \(g\) 的 \(p\)-parent 定理

固定

\[
p\ge5\ \text{为素数},
\qquad
pR+1=4K,
\qquad
R\ge3,
\qquad
p\nmid R.
\tag{1}
\]

令一个有序 primitive formal raw node 为

\[
P=(A,B,m),
\qquad
A,B,m>0,
\qquad
A+B=Rm,
\qquad
(A,B)=1.
\tag{2}
\]

由 (2) 自动有

\[
(B,R)=1.
\tag{3}
\]

取 \(g\in\mathbb Z_{>0}\)，并令

\[
\boxed{
N=pgm-1,
\qquad
S_g=\left(pgB,\ pgA-R,\ N\right).
}
\tag{4}
\]

**定理。** 若

\[
pgA>R,
\qquad
(g,R)=1,
\qquad
(B,N)=1,
\tag{5}
\]

则 \(S_g\) 是正 primitive formal raw node，且以第一坐标为被除坐标的
\(q=p\) raw transition 满足

\[
S_g\xrightarrow[\gcd\ \mathrm{reduction}=g]{q=p} (B,A,m),
\tag{6}
\]

所以 canonicalize 后恰为 \(P\)。反过来，在 \(pgA>R\) 下，\(S_g\) 的
primitive 性恰等价于 (5) 的后两项。

**证明。** 由 (2) 有

\[
 (B,R)=1.
\tag{7}
\]

又由 (5) 有 \(pgA-R>0\)，并且

\[
pgB+(pgA-R)=pg(A+B)-R=RN.
\tag{8}
\]

所以 (4) 的坐标和满足 formal invariant。由于 \(p\nmid R\) 且 \(N\equiv-1\pmod p\)，
有 \((p,RN)=1\)。又 \((g,R)=1\) 蕴含 \((g,N)=1\)，故 (7) 给出精确恒等式

\[
\begin{aligned}
\gcd(pgB,pgA-R)
&=\gcd(pgB,RN)\\
&=\gcd(B,N).
\end{aligned}
\tag{9}
\]

若 \((g,R)>1\)，该公因子直接同时整除 \(S_g\) 的两个坐标；因此 (9) 也证明了所述
primitive 性的充要性。由 (1) 有 \(p\nmid K\)，而 \(v_p(pgB)>0=v_p(K)\)，
故 \(p\) 是有效 raw 超容量标签。source 层数为 \(N\)，所以其 shift 是 \(1\)；同时

\[
N\equiv-1\pmod p,
\qquad
pgA-R\equiv-R\not\equiv0\pmod p,
\tag{10}
\]

给出 unit 条件。raw 除法未约分时精确为

\[
(pgB,pgA-R,N)
\longmapsto
(gB,gA,gm).
\tag{11}
\]

因为 \((A,B)=1\)，右端前两坐标的 gcd 恰为 \(g\)，并且 \(g\mid gm\)。约分后得到
(6)。证毕。

两个特别情形说明这一定理的强弱不同：

\[
\begin{aligned}
g=1:&\quad
S_1=(pB,pA-R,pm-1),
&&\text{当且仅当 }(B,pm-1)=1;\\
g=B:&\quad
S_B=(pB^2,pAB-R,pBm-1),
&&\text{总是成立，因为 }pBm-1\equiv-1\pmod B.
\end{aligned}
\tag{12}
\]

这里 \(g=B\) 的正性也自动成立：由 \(AB\ge Rm-1\ge R-1\) 与
\(p\ge5\)，有 \(pAB>R\)。因此每个满足 (1)--(2) 的 target 至少有这个
二次 formal \(p\)-parent。

取 canonical anchor \(P=(R-1,1,1)\) 时，\(B=g=m=1\)，式 (4) 专门化为

\[
S_1=(p,p(R-1)-R,p-1)=(p,R(p-1)-p,p-1),
\tag{13}
\]

这正是既有的 `universal_p_source_v1`（至多差有序坐标约定）。因此本定理不是另造一条
特殊技巧，而是把 universal \(p\)-source 反向推广到每个 primitive raw node。

## 2. 这条构造为什么不能自动成为 E1

定理对 (1)--(2) 的每一个 node 都给出 formal \(p\)-parent。于是以下推理没有信息量：

```text
目标 node 有一个 p-raw 父节点
=> 目标 node 有 source provenance
=> 可建立递归状态
```

第一行普遍为真，后两行并不随之成立。若允许在发现目标 node 后把 (4) 临时宣布为 root，
则任意 raw node 都能获得同样的“来源”，E1 的 root 条件会退化为 tautology。

因此一个可接受的 root-entry 至少仍须额外给出：

1. 在选择目标之前定义的具名、target-independent root family；
2. 不可由 charged history 创建的 `fresh_source_tree_only` scope；
3. 从 source word 到 typed determinant state 的 E2/E3 verifier；
4. 全域带标记解集 lift 和不可重置的 E5 支付。

这些要求正是现有状态合同把 `analysis_evidence_not_verified_edge` 与
`verified_edge` 分开的原因。

## 3. 两个当前接口的含义

对 \(c=9\) complement seed 的任一合法 dyadic high-layer node

\[
P_{x,\gamma}=(2\gamma x,2\gamma y-R,2\gamma-1),
\tag{14}
\]

已有前驱卡的 primitive、容量和正性条件使其满足 (2)。并且核心 \(c=9\) 域有

\[
2p<R<3p,
\tag{15}
\]

故 \(p\nmid R\)，定理自动给出它的实际 formal \(p\)-parent。特别地，\(\gamma=2\)
时两个控制点都可直接回放：

\[
\begin{array}{c|c|c}
p&P_{x,2}&S_{B}(P_{x,2})\\ \hline
193&(736,797,3)&(193\cdot797^2,\ 193\cdot736\cdot797-511,\ 193\cdot797\cdot3-1)\\
337&(1312,1421,3)&(337\cdot1421^2,\ 337\cdot1312\cdot1421-911,\ 337\cdot1421\cdot3-1)
\end{array}
\tag{16}
\]

对 \(c=3\) 的 even-tail seed \(P=(x,R-x,1)\)，也同样存在 (12) 的 \(g=B\)
parent。它不能替代
[fresh root-entry 准入边界](type-I-g-anchor-c3-even-tail-root-entry-admission-boundary.md)
所要求的独立有序 raw receipt；恰恰相反，(4) 说明为何不能以“存在一个 raw 父节点”
代替该 receipt。

## 4. 研究后果

这条定理给出了一个可重用的 source-policy no-go：以后任何利用形式 raw source 的
selector 分支，都必须标明其 root 不是由目标 node 反向构造得到。对 \(c=9\)，可以研究
是否有一个事先定义的 \(\gamma\)-family 及独立状态语义，使 (12) 成为合法 root-entry；
在此以前，它只是一条可回放 raw path，不能提供 E1--E5 或 Erdős--Straus 的全称结论。
