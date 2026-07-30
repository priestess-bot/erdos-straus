---
kind: claim
claim_id: type-I-f-overflow-repair-transition-potential-boundary
title: R 因子修复转移图的良基势函数边界
statement: 对同一 K 支撑的目标纤维，若 t 是 R 的真因子，则单位权溢出价格满足 Omega_1(t)<=Omega_1(R)，故 (Omega_1(t),t) 按词典序严格小于 (Omega_1(R),R)。冻结的 48 条平衡商边中 Omega_1 严降 22 条、相等 26 条；有限 Cayley 图多源 BFS 还精确求出全部 42 个 F-box miss 的 Omega_1，范围为 1--18。这个势函数只作用于 t=1 (mod 4) 的商表示，不是合法 Type I 状态递降：149 条一级合法修复边全部满足 R'>R、K'>K，151 个派生合法状态无一重入冻结见证域。冻结已知边图虽有 319 个节点、203 条边且无环，但仍有 45 个商状态没有已证明终端，因此当前的 R、支撑逃逸、Omega 与因子高度不能组成一个已经闭合且解可提升的统一良基势函数。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f-overflow-r-modulus-repair
  - type-I-f-overflow-balanced-endpoint-descent
  - type-I-f-overflow-lower-modulus-weighted-cost-interface
  - type-I-f-overflow-lower-modulus-shared-gap-type-II-lift
  - marked-solution-descent-closure
topics:
- type-I
- F-state
- descent
- well-founded-potential
- transition-graph
- finite-box
- overflow
- solution-lift
- finite-audit
- proof-program
sources:
- claim: type-I-f-overflow-r-modulus-repair
  role: legal-repair-input
- claim: type-I-f-overflow-balanced-endpoint-descent
  role: quotient-reduction-input
- claim: type-I-f-overflow-lower-modulus-weighted-cost-interface
  role: omega-definition
- claim: type-I-f-overflow-lower-modulus-shared-gap-type-II-lift
  role: proved-terminal-edges
- claim: marked-solution-descent-closure
  role: liftability-criterion
visibility: public
last_checked: '2026-07-30'
---

# $R$ 因子修复转移图的良基势函数边界

## 两类转移必须分型

沿用 $R$-因子修复的记号：

\[
4K=pR+1,\qquad R=mt,\qquad A=mu-1,\qquad B=mv+1.
\]

当前构造同时产生两种性质不同的落点。

1. 一级修复产生合法 Type I 状态
   \[
   R'={4KA+1\over m},\qquad K'={pR'+1\over4}.
   \]
2. 端点平衡产生同一 $K$ 支撑上的商表示模数
   \[
   t=R/m.
   \]

第一类保留 $R'\equiv3\pmod4$，却不降低状态高度；第二类严格降低模数，却有
$t\equiv1\pmod4$，因而不是合法 Type I 缺口状态。把这两类节点都简称为“更小
状态”会掩盖良基证明中最关键的类型差异。

## 合法修复边严格增高

由 $4K=pmt+1$ 与 $A+1=mu$，有

\[
R'={ (pmt+1)A+1\over m}=ptA+u.
\tag{1}
\]

合法缺口满足 $m\le p-2$，且 $A\ge1$、$u\ge1$，所以

\[
R'-R=t(pA-m)+u>0.
\tag{2}
\]

同一 $p$ 下 $K=(pR+1)/4$，故 (2) 还推出 $K'>K$。因此任何以通常升序
$R$ 或 $K$ 为首坐标的词典序势函数，在一级合法修复边上都朝错误方向移动。
反向排列 $R$ 也不能单独给出良基序，因为正整数上的严格增长可以无限持续；除非另有
一个取值于良基集合且先严格下降的坐标，而当前构造尚未提供这样的坐标。

## 商表示上的精确 $\Omega_1$ 势函数

令 $K=\prod_iq_i^{\nu_i}$，并令

\[
\phi_s(z)=\prod_iq_i^{z_i}\pmod s,
\qquad
\mathcal C_s=\phi_s\left(\prod_i[-\nu_i,\nu_i]\right).
\]

在以 $q_i^{\pm1}$ 为生成边的有限 Cayley 图中，从集合 $\mathcal C_s$ 到
$-1\bmod s$ 的最短距离恰为

\[
\Omega_1(s)=
\min_{\phi_s(z)=-1}\sum_i(|z_i|-\nu_i)_+.
\tag{3}
\]

证明如下。给定目标向量 $z$，逐坐标把它截断到盒内向量 $b$，则从
$\phi_s(b)$ 到 $\phi_s(z)$ 有一条长度等于 (3) 中费用的路径，所以图距离不大于
$\Omega_1(s)$。反之，任意从盒像出发、长度为 $L$ 的生成元路径给出
$z=b+d$，且其盒外费用不大于 $\lVert d\rVert_1\le L$。故
$\Omega_1(s)$ 不大于图距离，两者相等。

若 $t\mid R$，模 $R$ 的每个目标向量约化后仍是模 $t$ 的目标向量，因此

\[
\Omega_1(t)\le\Omega_1(R).
\tag{4}
\]

再结合 $t<R$，得到严格词典序下降

\[
\boxed{(\Omega_1(t),t)<_{\mathrm{lex}}(\Omega_1(R),R).}
\tag{5}
\]

所以 (5) 是一条真正的良基势函数引理，但其定义域是“固定 $K$ 支撑的商表示”，
不是带解提升的合法 Type I 状态图。

## 冻结精确审计

复现脚本和结果为：

~~~text
reproductions/type_i_f_overflow_repair_transition_potential.py
reproductions/type-i-f-overflow-repair-transition-potential-results.json
~~~

结果文件 SHA-256：

~~~text
c5aa5e5f39cfa33d62471ad32657fea73c3ef905882d77787dc26989f79a2110
~~~

48 条严格平衡商边全部满足 (5)：

~~~text
strict_quotient_count: 48
quotient_omega_strict_decrease_count: 22
quotient_omega_equal_count: 26
quotient_omega_increase_count: 0
quotient_omega_R_lexicographic_strict_decrease_count: 48
quotient_legal_type_I_modulus_count: 0
~~~

多源 BFS 精确求出全部 42 个 F-box miss 的 $\Omega_1$，从而关闭此前有限壳层
$L\le9$ 留下的 6 个未解析点：

~~~text
Omega_1 histogram:
1:12, 2:8, 3:2, 4:4, 5:2, 6:2, 7:2,
8:3, 9:1, 10:1, 11:1, 12:2, 15:1, 18:1
minimum: 1
maximum: 18
~~~

先前壳层算法得到的 36 个精确值与本次有限图算法全部一致；另外 6 个值也都满足先前
记录的下界 $\Omega_1\ge10$。

| $p$ | lower $t$ | 方向 | 精确 $\Omega_1$ |
|---:|---:|:---:|---:|
| 62704849 | 649 | forward | 12 |
| 75056809 | 21113 | reverse | 11 |
| 310002289 | 107977 | reverse | 18 |
| 312918169 | 16649 | forward | 10 |
| 366108649 | 11057 | forward | 12 |
| 373561609 | 208577 | forward | 15 |

商边的其它坐标呈现明确冲突：模数的素因子重数高度在 48/48 条边上严格下降，
但原 $K$-支撑端点的逃逸数从 0 增至 1 或 2：

~~~text
one escaped endpoint: 7
two escaped endpoints: 41
escape residual product bit length: 12--230
~~~

因此以升序“支撑逃逸数”为首坐标的词典序在 48/48 条商边上失败；以 $R$ 或
$(\Omega_1,R)$ 为首坐标则全部下降。把“剩余未逃逸端点数”反向计数虽可人为制造
一次下降，但该坐标在最多两层后耗尽，而且没有证明外部素因子在后续修复中不能被重新
吸收，故它不是递归不变量。

一级合法修复的方向完全相反：

~~~text
primary_legal_repair_count: 149
primary_modulus_increase_count: 149
primary_K_increase_count: 149
primary_direct_terminal_count: 0
modulus bit-length growth: 29--252
~~~

二级修复只产生两个合法小模数落点：

~~~text
(p,R,R_second)=(51029449,16371,7)
(p,R,R_second)=(534844249,11011,3)
~~~

二者均没有直接平方命中，也没有继承新 $K$ 的 F/G 见证，因此不能继续应用同一
选择规则。

## 冻结图与“无环”的边界

把当前仓库中已经证明的边全部建图，得到：

~~~text
nodes: 319
edges: 203
source F nodes: 116
primary legal repair nodes: 149
lower quotient nodes: 48
second legal repair nodes: 2
Type II terminal nodes: 4
directed cycles: 0
maximum known path length: 2
~~~

四个 Type II 终端来自三个 lower-hit 状态；其余 45 个商状态没有已证明的共享缺口
Type II 终端，其中包括全部 42 个 F-box miss 和三个未提升的 F-box hit。

这个有限图无环不是全局良基性的证据。151 个派生合法状态无一与冻结源状态的
$(p,R)$ 重合，48 个商模数也无一重入源域；换言之，图在所有关键落点处停止，是因为
尚未定义下一条边，而不是因为已经证明必须终止。任意有限无环图当然都有人工拓扑秩，
但该秩没有给出对新状态可重复计算的算术势函数。

## 缺失的提升条件

要把 (5) 升级为目标所需的“严格且解可提升的递降”，至少还缺少以下一项统一桥接：

1. 从 $t\equiv1\pmod4$ 的目标关系构造合法 $h\equiv3\pmod4$，并证明对应
   Type I 平方除子或 Type II 因子条件，而不只是共享缺口候选；
2. 给出真实源分母 $n<p$、非空的标记解集 $W_{n,\theta}$，以及
   $W_{n,\theta}\to\operatorname{Sol}(p)$ 的显式提升；模数 $t$ 本身不是这样的
   源分母；
3. 对每个一级或二级合法修复状态 $(p,R',K')$，规范地产生新的 F/G 见证，使选择器
   在同一状态类型上闭合，并证明某个良基坐标严格下降；
4. 证明支撑逃逸残差必进入一个 Type II 端点或同一条可比较的 $q$-进载体；
5. 把 $\Omega_1$ 的每个正层映射为可收费的共同容量。仅有 (4) 不够，因为 26 条
   商边的 $\Omega_1$ 完全不变。

因此当前能严格声称的是：商表示层已经有规范良基势函数；合法状态层仍没有闭合的
势函数与提升映射。不存在数据支持把二者合并成已经完成的递降定理。

## 复现

~~~bash
python3 reproductions/type_i_f_overflow_repair_transition_potential.py
~~~
