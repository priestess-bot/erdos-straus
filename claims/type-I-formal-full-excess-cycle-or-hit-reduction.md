---
kind: claim
claim_id: type-I-formal-full-excess-cycle-or-hit-reduction
title: 完整超高形式图的 Type I 或一层周期归约
statement: 固定核心素数 p、R>=3 与 4K=pR+1，在互素正形式对 A+B=Rm 上允许每个满足 v_q(AB)>v_q(K) 的素数作正规形式迁移。固定起点的可达图有限；m>1 的每条边严格降低 m；节点无出边当且仅当 AB|K，并在此时直接产生同状态 Type I 证书。因此中心谱 miss 时任意持续选择的轨道最终进入 m=1 有向周期。m=1 的每条非自环边恰降低 min(A,B) 或 max(A,B) 之一，唯一可能的自环参数为 (R,q,{A,B})=(3,2,{1,2})；该自环可在中心谱 miss 的核心状态中真实出现。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-ranked-pruning-and-external-gap-selector
  - type-I-general-b-centered-square-spectrum
  - type-I-coprime-factor-normal-form
topics:
  - type-I
  - formal-target-pair
  - q-adic
  - full-excess-graph
  - cycle-or-hit
  - support-switch
  - well-founded-pruning
  - proof-boundary
sources:
  - claim: type-I-formal-ranked-pruning-and-external-gap-selector
    role: general-formal-transition
  - claim: type-I-general-b-centered-square-spectrum
    role: centered-terminal
  - claim: type-I-coprime-factor-normal-form
    role: direct-Type-I-reconstruction
visibility: public
last_checked: '2026-07-31'
---

# 完整超高形式图的 Type I 或一层周期归约

## 1. 完整超高图

固定核心素数与状态参数

\[
p\equiv1\pmod {24},
\qquad R\ge3,
\qquad 4K=pR+1.
\tag{1}
\]

于是 \(R\equiv3\pmod4\) 且 \((R,K)=1\)。节点是无序形式对

\[
S=(\{A,B\},m),
\qquad A,B,m>0,
\qquad (A,B)=1,
\qquad A+B=Rm.
\tag{2}
\]

对每个素数统一约定 \(\nu_q=v_q(K)\)，包括 \(q\nmid K\) 时 \(\nu_q=0\)。若

\[
v_q(AB)>\nu_q,
\tag{3}
\]

则 \(q\) 只整除 \(A,B\) 中的一侧。把该侧记为 \(C\)，另一侧记为 \(D\)。由
互素性与 (2) 得 \(q\nmid RmD\)，故存在唯一的

\[
1\le t<q,
\qquad t\equiv-m\pmod q.
\tag{4}
\]

定义

\[
(\widetilde C,\widetilde D,\widetilde m)
=
\left(
\frac Cq,
\frac{D+Rt}{q},
\frac{m+t}{q}
\right),
\tag{5}
\]

再令 \(g=(\widetilde C,\widetilde D)\)。一般形式迁移定理给出
\(g\mid\widetilde m\)，所以正规后继为

\[
T_q(S)=
\left(
\left\{\frac{\widetilde C}{g},\frac{\widetilde D}{g}\right\},
\frac{\widetilde m}{g}
\right).
\tag{6}
\]

这里的边集必须遍历 (3) 的**全部**素数。若只允许 \(q\mid K\)，下面的汇点刻画不成立。

## 2. 有限性与严格降层

若起点的第三坐标为 \(m_0\)，则任一可达节点都满足

\[
1\le m\le m_0,
\qquad A+B=Rm\le Rm_0.
\tag{7}
\]

所以固定起点的可达节点只有有限多个。若 \(m>1\)，由 \(1\le t<q\) 和 (6) 得

\[
m'
\le \frac{m+t}{q}
\le \left\lceil\frac mq\right\rceil
<m.
\tag{8}
\]

因此所有周期都只能位于 \(m=1\) 层。

## 3. 汇点精确等价于同状态 Type I

由完整边条件 (3)，节点无出边当且仅当

\[
v_q(AB)\le v_q(K)\quad\text{对每个素数 }q,
\tag{9}
\]

也就是

\[
\boxed{AB\mid K.}
\tag{10}
\]

在 (10) 下交换两侧后设 \(A<B\)，并写

\[
K=ABC.
\tag{11}
\]

中心除子

\[
d=A^2C=\frac{KA}{B}
\tag{12}
\]

满足

\[
d<K,
\qquad d\mid K^2,
\qquad d\equiv-K\pmod R.
\tag{13}
\]

最后一个同余来自 \(A+B=Rm\) 和 \((B,R)=1\)。这不只是抽象的中心谱命中。令

\[
h=\frac{4A^2C+1}{R}.
\tag{14}
\]

则

\[
(\alpha,\beta,\gamma)=(m,A,C)
\tag{15}
\]

满足 Type I 互素正规形

\[
p=4\alpha\beta\gamma-h,
\qquad (\alpha,\beta)=1,
\qquad h\mid\beta p+\alpha.
\tag{16}
\]

其中 \((m,A)=1\) 由 \((A,R)=(A,B)=1\) 与 \(A+B=Rm\) 得出。又因

\[
R(p-h)=4AC(B-A)-2>0,
\tag{17}
\]

且 \(h\equiv3\pmod4\)，故 \(3\le h\le p-2\)。所以 (14)--(16) 给出原素数
\(p\) 的合法直接 Type I 终端。交换 \(A,B\) 得到互补中心因子 \(K^2/d\)。

## 4. Cycle-or-hit 定理

若状态级中心平方除子谱 miss，则第 3 节说明完整超高图没有汇点。从任一给定起点开始，
每一步任取一条出边便得到无限游走。第 2 节的可达图有限，所以游走在有限步内必重复一个
节点，并在两次出现之间形成有向周期；(8) 又排除 \(m>1\) 周期。因此

\[
\boxed{
\text{中心 Type I 命中}
\quad\lor\quad
\text{任意持续的完整超高游走都在有限步内形成 }m=1\text{ 有向周期}.}
\tag{18}
\]

若后继选择只依赖当前节点，则有限确定性轨道最终周期化；对允许同一节点多次选择不同
后继的一般游走，(18) 只断言它必包含一个周期段，不声称此后永远留在该周期。它把形式图
的最终障碍精确压到 \(m=1\)，但形式边仍只是
`analysis_evidence`，尚未提供合法状态、解提升和 E1--E5 回执。

## 5. 一层边的双秩几何

在 \(m=1\) 层令

\[
x=\min(A,B),
\qquad y=R-x,
\qquad 1\le x<R/2.
\tag{19}
\]

此时 (5) 中 \(t=q-1\)、\(g=1\)。若选中坐标为 \(C\)，后继规范小坐标为

\[
x'=\frac Cq,
\qquad y'=R-x'.
\tag{20}
\]

若选中小侧 \(C=x\)，则 \(x'<x\) 而 \(y'>y\)。若选中大侧 \(C=y\)，则

\[
x'<x\iff R<(q+1)x,
\qquad
y'<y\iff R>(q+1)x.
\tag{21}
\]

所以每条非自环边恰好严格降低 `min` 或 `max` 之一。这解释了两个独立秩

\[
\rho_{\min}=(m,\min(A,B)),
\qquad
\rho_{\max}=(m,\max(A,B))
\tag{22}
\]

为何各自产生 DAG，也解释了为何把两个边集合并后会重新允许周期。

等号 \(R=(q+1)x\) 给出自环。由 \((x,R)=1\) 得 \(x=1\)、\(R=q+1\)；再由
\(R\equiv3\pmod4\) 和 \(q\) 为素数，唯一可能是

\[
\boxed{(R,q,x)=(3,2,1).}
\tag{23}
\]

## 6. 自环不能由中心硬门自动删除

取

\[
p=1009,
\qquad R=3,
\qquad K=757.
\tag{24}
\]

这里 \(p\equiv1\pmod {24}\) 为素数，\(K=757\) 也是素数且 \(757\equiv1\pmod3\)。
所以 \(K^2\) 的所有因子模 3 都为 1，中心目标 \(-K\equiv2\pmod3\) miss。另一方面，
一层节点 \(\{1,2\}\) 的大坐标含外部素数 \(q=2\)，而

\[
\{1,2\}\longmapsto\{2/2,3-2/2\}=\{1,2\}.
\tag{25}
\]

所以 (23) 在真正中心 miss 的核心状态中会发生。任何全称外部周期逃逸引理都必须单列
这个二进自环，或提供覆盖它的其它 Type I/II、偶终端或合法 support switch；不能把它
并入要求 \(Q\equiv3\pmod4\) 的普通外部缺口菜单。该整数边界由
`reproductions/type_i_formal_cycle_multiplier_boundary.py` 再次独立核验。

## 7. 外部二进周期不是例外而是普遍子图

固定任意奇数 \(R\)。一层无序互素节点可识别为

\[
(\mathbb Z/R\mathbb Z)^\times/\{\pm1\}.
\tag{26}
\]

每对 \(\{x,R-x\}\) 恰有一个偶坐标。总选择该偶坐标并除以 2，在 (26) 上正是置换

\[
[x]\longmapsto[2^{-1}x].
\tag{27}
\]

所以这些二进边把全部一层节点分解成若干有向周期。对核心状态
\(R\equiv3\pmod8\)，有

\[
K=\frac{pR+1}{4}\equiv1\pmod2.
\tag{28}
\]

因此每个偶坐标都满足 \(v_2(AB)>v_2(K)=0\)，(27) 的全部边都是真实外部超高边。
式 (23) 只是这组置换周期在 \(R=3\) 时的一节点特例。

这证明“完整超高图含外部周期”在一半核心模数中是必然现象，而不是接近 Type I/II
终端的充分信号。任何有用的外部周期引理必须加入全局终端优先、源可达性、指数消元或
合法 support switch 等周期外信息。

## 8. 对下一步的精确收缩

式 (18) 把完整形式闭包的开放部分收缩为一层周期的二分：

1. 周期全部坐标由 \(K\) 支撑时，需要证明周期支撑强制同状态中心命中；
2. 周期含 \(K\) 外素数时，需要利用多节点表示格消去外部指数并得到直接证书，或把它
   升级为满足完整 E1--E5 与解提升的合法换支撑边；纯粹存在外部周期不够；
3. \(R=3,q=2\) 的自环必须作为独立二进边界处理。

“被单步秩拒绝的后继只做直接终端前瞻”是当前选择器的合同，不是一般数学不可能性；若
未来构造出带整体下降证明的宏边，仍可合法跨越多个形式节点。
