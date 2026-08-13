---
kind: claim
claim_id: type-I-s-zero-rechart-standalone-potential-no-go
title: s=0 重图表的半群压缩与单坐标势 no-go
statement: >-
  在 a=1,d=1 正规形上，形式 s=0 更新 Phi_t 精确满足
  Phi_u o Phi_t=Phi_{t+u+p^2tu}，任意有限更新词均压成一次，且 A/T、K/T、K/A
  与全部相对赋值不变。p=73 给出形式根高度 1->2->1、容量始终 (2,3) 的两步控制，
  同一终态也可一步到达。更强地，既有 p=97 chart-local actual raw endpoint receipt
  族含一个无限子族：其源端根容量为 (2,3)，关联的 conditional s=0 arithmetic target
  根容量同时饱和到 (9410,9507)。因此来源深度、比例、根高度、根容量或有限素数支撑
  均不能单独成为所有形式 s=0 边上的严格良基势；该结论没有构造 admitted cycle，
  也不排除依赖 terminal priority、typed admission 与 persistent lineage 的复合势。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-endpoint-s-zero-p-free-return
  - type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
  - type-I-overflow-full-product-d-one-a-one-all-core-dual-saturation-s-zero-tree-no-go
topics:
  - type-I
  - overflow
  - s-zero
  - rechart
  - semigroup
  - potential-function
  - root-height
  - capacity-reset
  - finite-support
  - lineage
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-endpoint-s-zero-p-free-return
    role: actual-source-side-endpoint-receipt-family
  - claim: type-I-overflow-full-product-d-one-a-one-regeneration-return-digit-normal-form
    role: exact-a-one-s-zero-normal-form
  - reproduction: reproductions/type_i_s_zero_rechart_standalone_potential_no_go.py
    role: formal-height-compression-and-conditional-capacity-reset-controls
visibility: public
last_checked: '2026-08-13'
---

# \(s=0\) 重图表的半群压缩与单坐标势 no-go

## 1. 形式 \(s=0\) 更新是可压缩半群

固定核心素数 \(p\)，写

\[
g=\frac{p+1}{2},
\qquad
C=\frac{p^2-1}{2},
\qquad
T=p^2r-g,
\tag{1}

\[
A=gT,
\qquad
K=CT.
\tag{2}

endpoint multiplier 为 \(1+p^2t\) 的形式 \(s=0\) 更新精确为

\[
\Phi_t(r,T,A,K)=
\bigl(r+tT,(1+p^2t)T,(1+p^2t)A,(1+p^2t)K\bigr),
\qquad t\ge1.
\tag{3}

令

\[
v=t+u+p^2tu.
\tag{4}

则

\[
(1+p^2u)(1+p^2t)=1+p^2v,
\tag{5}

直接代入给出

\[
\boxed{\Phi_u\circ\Phi_t=\Phi_v.}
\tag{6}

所以任意有限更新词都压成一次更新，其总 multiplier 为

\[
\prod_j(1+p^2t_j)=1+p^2v.
\tag{7}

因此，不携带不可压缩 lineage token 的 arithmetic state 无法恢复实际更新次数或
分解。与此同时，以下量沿每条形式边完全不变：

\[
\boxed{
\frac AT=g,
\qquad
\frac KT=C,
\qquad
\frac KA=p-1,}
\tag{8}

以及对每个素数 \(q\)，

\[
\boxed{
\nu_q(K)-\nu_q(T)=\nu_q(C).}
\tag{9}

特别地，反复使用 \(\Phi_1\) 已构成一条无限形式链，所以不存在一个在全部
unrestricted formal \(s=0\) 边上严格下降的良基势。这个陈述只针对形式边图，不能
外推为 admitted selector graph 的非终止性。

## 2. 根高度可先升后降

根锚 departure 可写成

\[
R(r)-(p+1)=pJ(r),
\qquad
J(r)=2(p^2-1)r-p-2.
\tag{10}

因为 \(p\nmid T\)，从 (3) 得

\[
\boxed{J(r+tT)\equiv J(r)+t\pmod p.}
\tag{11}

所以形式更新既能增加也能消去额外的 \(p\)-进层。

固定 \(p=73\)，从 \(r_0=1\) 出发：

\[
(r_0,T_0)=(1,5292)
\xrightarrow{\Phi_4}
(21169,112809564)
\xrightarrow{\Phi_2}
(225640297,1202437142676).
\tag{12}

三态的根 departure 高度为

\[
1\longrightarrow2\longrightarrow1,
\tag{13}

而两侧根容量始终为 \((2,3)\)。此外

\[
21317\cdot10659
=227217903
=1+73^2\cdot42638,
\tag{14}

所以两步终态也等于单步 \(\Phi_{42638}\) 的终态。由此，未保护的来源深度不是状态
函数；根高度或容量对单独作为每条形式边的严格势也分别失败。式 (12) 的两条箭头
都是 normal-form formal actions，不是已获 receipt 或 admission 的 selector 边。

## 3. 有限支撑也不是可耗尽资源

沿 (3)，令 \(L=1+p^2t\)，则

\[
\operatorname{supp}(K')
=\operatorname{supp}(K)\cup\operatorname{supp}(L).
\tag{15}

任给有限的 \(p\)-free 整数 \(Q\)，CRT 可解

\[
t\equiv-p^{-2}\pmod {q^e}
\tag{16}

对 \(Q=\prod q^e\) 的全部素数幂条件，从而一次令 \(Q\mid L\)。这只能保证注入
指定支撑，不能禁止 \(L\) 还有其它素因子。另一方面，固定一次 \(t\) 后连续两次使用
同一 \(\Phi_t\)，第二步的支撑集合已经不再变化，而状态仍变化。因此有限支撑集合
既不能在每条形式边上严格变化，也不存在一个预先固定、最终必被耗尽的有限支撑宇宙。
这不排除把带 multiplicity、priority 或 lineage 的支撑数据纳入更丰富的复合势。

## 4. 实际源端 receipt 关联的条件容量重置

既有 \(p=97,h=58\) 参数族给出从 canonical anchor 可逐边重放的 chart-local actual
raw endpoint receipt：

\[
r(k)=66988440+
4243815461730835674059638914706837844637k,
\tag{17}

\[
E(k)=369377901007+
23400629237489299674263740436419983401253504k.
\tag{18}

对每个 \(k\ge0\)，既有证明给出

\[
R(k)-58=331E(k),
\quad 58\cdot331\mid K(k),
\quad (E(k),A(k))=(E(k),K(k))=1,
\quad E(k)\equiv1\pmod {97^2}.
\tag{19}

这里“actual”只修饰源端 raw path 可重放；persistent source lineage 仍是条件性的。

令

\[
U=\frac{97^2+1}{2}=4705,
\qquad
V=\frac{97^2+97+1}{3}=3169,
\qquad
D_0=UV=14910145,
\tag{20}

并限制到

\[
\boxed{k=14392062+D_0j,\qquad j\ge0.}
\tag{21}

因为 (17)--(18) 在 \(k\) 中仿射，(21) 使下列模 \(U,V\) 的数据对所有 \(j\)
保持固定。源参数满足

\[
(r+49,U)=1,
\qquad
(2r+1,V)=1,
\tag{22}

故两侧根容量是 \((2,3)\)。同时

\[
D_0\mid E,
\qquad
(T,D_0)=1.
\tag{23}

写

\[
t=\frac{E-1}{97^2},
\qquad
r'=r+tT.
\tag{24}

在 \(j=0\) 的固定剩余上，

\[
\begin{array}{c|cc}
 &\bmod U&\bmod V\\ \hline
r+49\ \text{或}\ 2r+1&2583&1849\\
T&2122&1300\\
t&1&3072
\end{array}
\tag{25}

所以

\[
r'+49\equiv2583+2122\equiv0\pmod U,
\tag{26}

\[
2r'+1\equiv1849+2\cdot3072\cdot1300\equiv0\pmod V.
\tag{27}

一般根容量公式于是给出关联 conditional arithmetic target 的两侧满容量

\[
\boxed{
2(r'+49,U)=9410,
\qquad
3(2r'+1,V)=9507.}
\tag{28}

代表 \(j=0\) 为

\[
\begin{aligned}
r={}&61077255241788814332878114958073522084029059934,\\
E={}&336783306824958725248583556712863459150180685186255,\\
t={}&35793740761500555345794830132093044866636272206.
\end{aligned}
\tag{29}

式 (19)--(29) 证明：即使 source-side endpoint analysis receipt 是实际可重放的，
其关联 \(s=0\) 形式 target 仍可把最小根容量同时重置到满容量。它不声称该 target
已通过 typed validation 或 E1--E5，更不是 admitted successor。事实上

\[
\frac4{97}=\frac1{28}+\frac1{194}+\frac1{2716}
\tag{30}

会被 terminal-first 更早抢占。

## 5. 精确 no-go 与下一种势

本卡严格排除以下对象单独充当每条形式 \(s=0\) 边的严格良基势：

1. 未保护的 arithmetic ancestry length；
2. \(A/T,K/T,K/A\) 或相对赋值；
3. 根 departure 高度；
4. 两侧根容量对或其“距满容量”缺陷；
5. 有限素数支撑集合。

它没有构造 admitted nonterminal cycle，也不排除只定义在 admitted nonterminal graph
上的复合势。下一种可信候选必须显式依赖 terminal priority 与 typed admission，并携带
在 split/rechart 后仍不可丢弃、不可由 (6) 压缩的 persistent lineage 资源。

## 6. 聚焦回执

```bash
python3 reproductions/type_i_s_zero_rechart_standalone_potential_no_go.py --verify
```

脚本只核对 (12)--(14)、一个有限支撑控制及 (21)--(30) 的 \(j=0,1\) 固定实例；
它不运行历史测试，不扫描素数、分母、selector history 或一般参数范围。
