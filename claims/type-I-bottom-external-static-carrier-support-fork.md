---
kind: claim
claim_id: type-I-bottom-external-static-carrier-support-fork
title: 底层外部静态载体的来源三分与吸收边界
statement: 在合法核心图表 4K=pR+1 的完整 raw bottom Reach 中，取本原节点 X+Y=R 和外部素数 q 不整除 K；若 q^e 恰为 X 的完整 q 部分、X=q^e a，则 q 不整除 aY，并且恰有两种支持情形：aY|K 时该节点是 clean single-external q^e-slab，其规范图表 R_Q 不等于 R，R_Q<R 给出现有合同下的 E1--E5 absorption，R_Q>R 则 Q>R/4 且 a 属于 {1,2,3}；aY 不整除 K 时，必有 r 不等于 q 在同一节点超过 K 的 r 进容量并产生竞争 raw 边。若一条 q 边直接进入完整且 q-free 的 sink-SCC，则源精确写成 (qA,B)->(A,R-A)，并有 q 不整除 AB(R-A)，所以 Q=q 且上述三分可直接回溯。该回溯只适用于 path-carried static 素数，并不把 MISS_STATIC 自动升级为终端或全局单 q 收费；p=107722177,R=207 给出 q=103 四通道静态、与指定 q=103 slab 关联的 gap/collision/node-anchor/new-chart-centered 菜单全 miss 且 R_103>R 的精确 large-slab 边界，而原 p=2017 的同一 103 前缀实际有 R_103=115<R 的合法 absorption。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-formal-external-slab-collision-absorption-rechart
  - type-I-bottom-word-lattice-pareto-cycle-capacity-selector
  - type-I-target-fiber-joint-capacity-signed-carrier-dictionary
  - denominator-escape-state-contract
topics:
  - type-I
  - formal-target-pair
  - bottom-SCC
  - external-slab
  - static-carrier
  - q-adic-capacity
  - support-fork
  - absorption
  - large-slab
  - proof-boundary
sources:
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: complete-raw-transition-interface
  - claim: type-I-formal-external-slab-collision-absorption-rechart
    role: verified-single-slab-absorption-contract
  - claim: type-I-bottom-word-lattice-pareto-cycle-capacity-selector
    role: path-static-and-sink-SCC-receipt
visibility: public
last_checked: '2026-08-01'
---

# 底层外部静态载体的来源三分与吸收边界

## 1. 完整外部素数部分的支持分叉

固定核心素数和合法图表

\[
p\equiv1\pmod {24},
\qquad
3\le R\le p-2,
\qquad
4K=pR+1.
\tag{1}
\]

取完整、未剪枝 raw formal Reach 的一个底层本原节点

\[
X+Y=R,
\qquad
(X,Y)=1.
\tag{2}
\]

设外部素数 \(q\nmid K\) 整除 \(X\)，并取它在 \(X\) 中的完整幂

\[
e=v_q(X),
\qquad
Q=q^e,
\qquad
X=Qa.
\tag{3}
\]

由 \(e\) 的定义和 (2)，立即有

\[
q\nmid aY.
\tag{4}
\]

现在恰有以下两个支持情形。

### 1.1 clean single-external slab

若

\[
aY\mid K,
\tag{5}
\]

则 (2)--(5) 正是 single-external slab

\[
(X,Y)=(Qa,Y),
\qquad aY\mid K,
\qquad (Q,aY)=1,
\qquad m=1.
\tag{6}
\]

因为 \(X<R<p\)，有 \(q\ne p\)。所以可定义唯一规范图表

\[
1\le R_Q<4Q,
\qquad
pR_Q\equiv-1\pmod {4Q},
\qquad
K_Q=\frac{pR_Q+1}{4}.
\tag{7}
\]

若 \(R_Q=R\)，则 \(Q\mid K\)，与 \(q\nmid K\) 矛盾。因此 \(R_Q\ne R\)，并有精确
二分：

\[
\boxed{
R_Q<R
\quad\lor\quad
R_Q>R.
}
\tag{8}
\]

第一支在隔离的 \(\texttt{external\_capacity\_absorption}\) 阶段中是已有 E1--E5
合同下的 verified support switch；这里升级的是 slab 宏边，不是 raw formal 边。
第二支满足

\[
R<R_Q<4Q,
\qquad
Q>\frac R4.
\tag{9}
\]

再由 \(Qa<R\) 得

\[
\boxed{a\in\{1,2,3\}.}
\tag{10}
\]

所以 clean 分支不是“吸收或未知”，而是精确落入

\[
\boxed{
\text{verified absorption}
\quad\lor\quad
\text{large-slab }a=1,2,3.
}
\tag{11}
\]

两类 slab collision 或新图表中心命中可以在 (11) 之前直接终端，但并非 (11) 的必要
条件。

### 1.2 竞争超额分支

若 \(aY\nmid K\)，则存在素数 \(r\) 满足

\[
v_r(aY)>v_r(K).
\tag{12}
\]

由 (4) 可知 \(r\ne q\)，并且

\[
v_r(XY)=v_r(QaY)=v_r(aY)>v_r(K).
\tag{13}
\]

所以同一节点存在一条标号 \(r\) 的 raw bottom transition。于是得到无条件的局部三分

\[
\boxed{
\text{ABSORB}(Q)
\quad\lor\quad
\text{LARGE}(Q,a)
\quad\lor\quad
\text{COMPETING\_EXCESS}(r).
}
\tag{14}
\]

第三支只是完整 Reach 中的竞争分析分支；它没有自动的标记状态、解提升或良基势，不能
登记为 E4。

## 2. q-free sink-SCC 的入口强化

设一条标号 \(q\nmid K\) 的底层边直接进入完整 raw Reach 的 sink-SCC：

\[
S=(qA,B,1)
\xrightarrow q
T=(A,R-A,1).
\tag{15}
\]

再假设该 sink-SCC 的全部边标号都不含 \(q\)。这里必须量化整个 SCC，而不是只要求某
一条选定周期的词积不含 \(q\)。

若 \(q\mid A\) 或 \(q\mid R-A\)，因为 \(v_q(K)=0\)，节点 \(T\) 就有 raw \(q\)
出边。sink 性会迫使该边仍在 SCC 内，矛盾。源节点本原又给 \(q\nmid B\)。因此

\[
\boxed{q\nmid AB(R-A).}
\tag{16}
\]

特别地，(15) 中的 \(q\) 恰为源坐标的完整 \(q\) 部分，故第 1 节可取

\[
Q=q,
\qquad a=A,
\qquad Y=B.
\tag{17}
\]

还有一个精确的出边判据：

\[
\boxed{
\operatorname{OutLabels}(S)=\{q\}
\iff AB\mid K.
}
\tag{18}
\]

若 \(AB\nmid K\)，(12)--(13) 给出竞争标号 \(r\ne q\)。该竞争边可进入另一个 SCC；
除非源 \(S\) 本身已在 sink-SCC 内，否则不能声称它仍在同一 SCC。

## 3. MISS_STATIC 的来源回溯

对来源路径和底层端点，写

\[
\begin{aligned}
d_{U,\ell}
&=v_\ell(U)-v_\ell(\Theta Y),\\
d_{V,\ell}
&=v_\ell(V)-v_\ell(\Theta X).
\end{aligned}
\tag{19}
\]

相对容量 \(D\in\{K,x_R\}\)，若周期词在 \(\ell\) 上的移动高度为零，而

\[
|d_{i,\ell}|>v_\ell(D),
\tag{20}
\]

则得到 \(\texttt{MISS\_STATIC}(\ell)\)。式 (19) 表明静态素数可以来自四类位置：
\(U,V\)、入口词 \(\Theta\) 或交叉端点 \(X,Y\)。所以静态 receipt 本身没有自动的
raw 边来源。

一般来源词的 \(\Theta\) 可能同时含边标号和高层 gcd reduction，所以仅知
\(q\mid\Theta\) 仍不够。若 receipt 额外记录 \(q\) 确实是某条 bottom raw 边的标号
（特别地，所量化的是纯 bottom word，此时 \(q\mid\Theta\) 就有该含义），才可回溯到
该边的源节点并应用 (14)。这给出规范的
\(\texttt{PATH\_STATIC\_PROVENANCE}\)：

\[
\boxed{
\text{clean ABSORB}
\quad\lor\quad
\text{clean LARGE}
\quad\lor\quad
\text{另一 raw 超额分支}.
}
\tag{21}
\]

式 (21) 是候选选择器的正向桥，但还不是 sink-SCC 的全称逃逸：第三支可能继续循环，
第二支正是尚未闭合的 large-slab；若静态素数只来自 \(U,V,X,Y\)，还不能调用它。

## 4. 原 p=2017 的静态 receipt 实际先有 absorption

取

\[
(p,R,K,x_R)=(2017,207,104380,556).
\tag{22}
\]

来源路径的 ancestry 定向前缀是

\[
(68_U,139_V;\Theta=1)
\xrightarrow{139}
(206_U,1_V;\Theta=139)
\xrightarrow{103}
(2_U,205_V;\Theta=139\cdot103).
\tag{23}
\]

中间节点满足

\[
206=103\cdot2,
\qquad
2\mid K.
\tag{24}
\]

所以它是 clean slab \((Q,a,Y)=(103,2,1)\)。其 direct/cross collision、节点/锚点
external gap 都 miss，但

\[
\boxed{
R_{103}=115<207,
\qquad
K_{103}=57989=103\cdot563.
}
\tag{25}
\]

因此这是 verified absorption，而不是 terminal-or-descent 的反例。进入二循环后

\[
(2,205)\xrightarrow{41}(5,202)\xrightarrow{101}(2,205)
\tag{26}
\]

四个 \(K/x_R\) 容量通道仍确有 \(\texttt{MISS\_STATIC}(103)\)；正确解释是该 ray
无法修复容量，但 SCC 压缩前的路径前缀已经提供合法出口。

事实上循环节点 \((5,202)=(5,101\cdot2)\) 还有 clean \(101\)-slab，满足

\[
R_{101}=135<207,
\tag{27}
\]

且新图表中心除子 \(101\) 直接给出 gap \(3\) 的 Type I 证书。另需更正全局语义：
\(p=2017\) 本身已有 gap \(15\) 的 Type I 和 Type II 证书，所以它不是
\(\texttt{terminal\mbox{-}first\ unresolved}\)；F、internal-free 只描述 \(R=207\)
的局部菜单。

## 5. static 素数不强制吸收：精确 large-slab 边界

同一个 \(R=207\) 骨架可取

\[
p=107722177,
\qquad
K=5574622660
=2^2\cdot5\cdot17\cdot307\cdot53407,
\tag{28}
\]

其中 \(p\) 和 \(53407\) 都是素数，且 \(53407\equiv1\pmod {207}\)。新增生成元在模
\(207\) 下为单位元，所以 centered \(-1\) 谱仍为 F；(23)、(26) 的全部 raw 边也保持。
此时

\[
x_R=26930596=2^2\cdot7^2\cdot11\cdot12491.
\tag{29}
\]

在循环基点对 \(\ell=103\) 仍有

\[
d_{U,103}=d_{V,103}=-1,
\qquad
v_{103}(K)=v_{103}(x_R)=v_{103}(41\cdot101)=0.
\tag{30}
\]

所以四通道均为 \(\texttt{MISS\_STATIC}(103)\)。出生节点仍是 clean
\((Q,a,Y)=(103,2,1)\)，但现在

\[
\boxed{R_{103}=375>207.}
\tag{31}
\]

gap \(103\) 的完整 Type I/II 平方除子谱、\(T\mid207\) 的两类 collision、节点和
锚点 external-affine 菜单全部 miss。因此 (31) 精确否定

\[
\text{four-channel path static }q
\Longrightarrow
\text{同一 }q\text{ 给 external terminal 或 ABSORB}.
\tag{32}
\]

它只把该 receipt 送入 large-slab \(a=2\) 分支。

必须紧邻保留全局边界：这个新素数也不是统一选择器反例。循环节点
\((2,205)=(2,41\cdot5)\) 给出

\[
R_{41}=35<207
\tag{33}
\]

的 clean absorption，且新图表立即中心命中。另一 \(101\)-slab 虽有
\(R_{101}=327>207\)，其新图表也中心命中。式 (31) 只关闭“指定静态素数局部强制
出口”，不关闭完整 SCC 的其它载体选择。

## 6. 竞争超额支确实必要

取

\[
(p,R,K)=(5596369,35,48968229),
\qquad
K=3\cdot79\cdot107\cdot1931.
\tag{34}
\]

底层节点 \((8,27)\) 对外部素数 \(q=2\) 有

\[
Q=2^3=8,
\qquad
a=1,
\qquad
aY=27\nmid K.
\tag{35}
\]

这里 \(v_3(27)=3>v_3(K)=1\)，所以同一节点除 \(q=2\) 边外还有竞争 \(r=3\) 边：

\[
(8,27)\xrightarrow2(4,31),
\qquad
(8,27)\xrightarrow3(9,26).
\tag{36}
\]

这说明不能在未检查 \(aY\mid K\) 时把路径中出现的外部 \(q\) 直接登记为 single-slab。

## 7. 对统一选择器的净推进

路径静态 receipt 现在可以携带一个可复核来源字段，而不再只是无方向的缺陷素数：

\[
\texttt{PATH\_STATIC}(q)
\mapsto
\begin{cases}
\texttt{VERIFIED\_ABSORB}(Q),\\
\texttt{LARGE\_SLAB}(Q,a),\\
\texttt{COMPETING\_RAW}(r).
\end{cases}
\tag{37}
\]

这已经把原 \(p=2017\) 的静态 receipt 正确拉回合法递降，并把更强错误命题压到一个
真实 large-slab 反例。尚未解决的是：

1. large-slab \(a=1,2,3\) 的全称出口；
2. 竞争超额分支在完整 SCC/Pareto 前沿中为何最终出现 clean slab 或直接终端；
3. 不是 path-carried 的源/端点 static 如何映到外部载体；
4. 多坐标 Pareto 价格如何注入跨状态的真实有限容量。

聚焦复现为

~~~bash
python3 reproductions/type_i_bottom_external_static_carrier_support_fork.py
python3 reproductions/type_i_bottom_external_static_carrier_support_fork.py --verify
~~~

它只核对 (22)--(36) 的代表性整数、raw 边、中心/缺口谱和静态赋值，不重跑历史普查。
