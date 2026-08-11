---
kind: claim
claim_id: type-II-odd-kernel-overflow-natural-tail-relation-graph
title: Type II 奇核盒外关系的 px 自然尾容量与 kappa=1 周期归约
statement: >-
  固定素数 p=1 mod 4、合法缺口 m 与 x=(p+m)/4。任一互素目标关系
  A+B=m*kappa 都满足 gcd(AB,m*kappa)=1；因此关系商 kappa 对 A、B 的
  每个活跃素数都没有同坐标支付能力。恒等式
  4/p=1/x+A/(px*kappa)+B/(px*kappa) 的两个自然尾为整数当且仅当
  AB|px：p 不整除 AB 时得到 Type II，p 整除 AB 时恰使用唯一 p 槽并得到
  Type I。对每个超过 px 指数容量的素数 ell，规范换源保持互素目标关系，且
  kappa>1 时严格降低 kappa；完整可达图因而必到直接证书，或进入有限的
  kappa=1 周期图。该图是内部 certificate search，不是 E1--E5 递归边。
  p=67369 的 q=21、42 两条物理权最小关系分别沿显式路径暴露 gap 31 的
  Type I 与 gap 151 的 Type II 终端，关闭了这两个中性载体压力点；一般
  kappa=1 SCC 的全称终端或可提升转交仍未证明。p=1153,q=16 进一步给出
  标签终端为空的二周期，否定“每个底层 SCC 自含短证书标签”；但它的两个
  物理最小关系在入周期前分别由 kappa 的 gap 23 Type II 与 divisor 3 Type I
  终端抢占，证明 fresh-quotient terminal 必须先于 SCC adapter。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-coprime-factor-normal-form
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-II-p-minus-one-jacobi-odd-kernel-affine-box-relay
  - type-II-p-minus-one-jacobi-weighted-minimum-overflow-neutral-carrier-no-go
  - denominator-escape-state-contract
topics:
  - type-II
  - type-I
  - odd-kernel
  - empty-box
  - natural-tail
  - physical-capacity
  - relation-quotient
  - support-switch
  - cycle-or-terminal
  - neutral-carrier
  - proof-program
sources:
  - claim: type-II-coprime-factor-normal-form
    role: within-capacity-Type-II-normal-form
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: analogous-formal-transition-algebra-and-cycle-boundary
  - claim: type-II-p-minus-one-jacobi-weighted-minimum-overflow-neutral-carrier-no-go
    role: minimum-overflow-input-relations
  - claim: denominator-escape-state-contract
    role: E1-E5-recursive-edge-boundary
  - reproduction: reproductions/type_ii_odd_kernel_overflow_natural_tail_relation_graph.py
    role: exact-capacity-transition-path-SCC-and-terminal-verifier
visibility: public
last_checked: '2026-08-11'
---

# Type II 奇核盒外关系的 \(px\) 自然尾容量与 \(\kappa=1\) 周期归约

## 1. 从盒外指数到互素目标关系

令

\[
p\equiv1\pmod4,\qquad
m\equiv3\pmod4,\qquad
3\le m\le p-2,\qquad
x=\frac{p+m}{4}.
\tag{1}
\]

给定互素正整数 \(A,B\) 满足

\[
A+B=m\kappa,\qquad \kappa\in\mathbb N.
\tag{2}
\]

这包括奇核空盒外的整数目标表示。若

\[
x=\prod_i\ell_i^{e_i},\qquad
\prod_i\ell_i^{z_i}=\frac AB,\quad (A,B)=1,\qquad
\prod_i\ell_i^{z_i}\equiv-1\pmod m,
\tag{3}
\]

则 \(m\mid A+B\)，故得到 (2)。

关系商与模数具有完全新鲜性：

\[
\boxed{\gcd(AB,m\kappa)=1.}
\tag{4}
\]

事实上，若素数 \(r\mid A\) 且 \(r\mid m\kappa\)，由
\(B=m\kappa-A\) 得 \(r\mid B\)，与 \((A,B)=1\) 矛盾；对 \(B\) 同理。
特别地，

\[
\gcd(\kappa,A)=\gcd(\kappa,B)=1.
\tag{5}
\]

所以 \(\kappa\) 的素因子都不在当前活跃支撑 \(AB\) 上。它可以提供新的
alternate-gap 候选，却不能支付 \(A\) 或 \(B\) 的任何现有指数缺口。
更精确地，对每个

\[
h\mid\kappa,\qquad
h\equiv3\pmod4,\qquad
3\le h\le p-2,
\tag{5a}
\]

选择器可以独立运行 gap-\(h\) 短证书 verifier。命中时这是直接 alternate
terminal；未命中时，\(h\) 的新鲜性本身不产生解。

## 2. 精确的 \(px\) 自然尾容量

由 \(4x=p+m\) 和 (2) 得

\[
\boxed{
\frac4p
=\frac1x
+\frac{A}{px\kappa}
+\frac{B}{px\kappa}.}
\tag{6}
\]

对应的形式自然尾为

\[
Y=\frac{px\kappa}{A},\qquad
Z=\frac{px\kappa}{B}.
\tag{7}
\]

因为 \((A,B)=1\) 且 (5) 成立，

\[
Y,Z\in\mathbb N
\iff AB\mid px\kappa
\iff
\boxed{AB\mid px.}
\tag{8}
\]

因此自然尾的完整物理支付池不是 \(x\)，而是

\[
\boxed{\mathcal C_{\rm nat}=px.}
\tag{9}
\]

其中 \(x\) 的素因子 occurrence 是 Type II 容量，额外的一层 \(p\) 是 Type I
容量。由于 \(x<p\)，有 \(p\nmid x\)。式 (8) 只有两种情形：

1. 若 \(p\nmid AB\)，则 \(AB\mid x\)。交换两侧使 \(A\le B\)，写
   \(x=ABC\)，则 \(d=A^2C=xA/B\le x\) 给出 Type II 证书。
2. 若 \(p\mid AB\)，则 \(v_p(AB)=1\)，且 \(p\) 只整除一侧。写
   \(A=pA_0\)、\(A_0B\mid x\)，则 \(d=xB/A_0\mid x^2\) 给出 Type I
   证书；自然尾 \(px\kappa/A=x\kappa/A_0\) 不被 \(p\) 整除，另一尾被
   \(p\) 整除。

所以

\[
\boxed{
AB\mid px
\iff
\text{关系 (2) 的自然尾直接给出 Type I 或 Type II 短证书}.}
\tag{10}
\]

定义两侧缺口和总缺口

\[
\Omega_A=\frac{A}{(A,px)},\qquad
\Omega_B=\frac{B}{(B,px)},\qquad
\Omega=\frac{AB}{(AB,px)}.
\tag{11}
\]

互素性给出

\[
\boxed{\Omega=\Omega_A\Omega_B},\qquad
\Omega=1\iff\text{直接终端}.
\tag{12}
\]

若 \(A/B\) 来自 (3)，则 \(p\nmid AB\) 且
\(AB=\prod_i\ell_i^{|z_i|}\)，所以

\[
\boxed{
\Omega
=\frac{AB}{(AB,x)}
=\prod_i\ell_i^{(|z_i|-e_i)_+}
=W(z).}
\tag{13}
\]

这把奇核盒、指数预算与 Type I/II 自然尾整除统一成整数容量证书；
\(\kappa\) 由 (5) 严格贡献零同坐标容量。

## 3. 完整超容量关系迁移

若当前不是终端，则 \(AB\nmid px\)，故存在素数 \(\ell\) 满足

\[
v_\ell(AB)>v_\ell(px).
\tag{14}
\]

交换两侧后设 \(\ell\mid A\)。由 (4) 有
\(\ell\nmid m\kappa B\)，所以存在唯一

\[
1\le t<\ell,\qquad
t\equiv-\kappa\pmod\ell.
\tag{15}
\]

定义 raw 迁移

\[
A_0=\frac A\ell,\qquad
B_0=\frac{B+mt}{\ell},\qquad
\kappa_0=\frac{\kappa+t}{\ell}.
\tag{16}
\]

三者都是正整数，且

\[
A_0+B_0=m\kappa_0.
\tag{17}
\]

令 \(g=(A_0,B_0)\)。因为 \((A_0,m)=(B_0,m)=1\)，有
\((g,m)=1\)；由 (17) 得 \(g\mid\kappa_0\)。于是规范后继

\[
A'=\frac{A_0}{g},\qquad
B'=\frac{B_0}{g},\qquad
\kappa'=\frac{\kappa_0}{g}
\tag{18}
\]

满足

\[
(A',B')=1,\qquad
A'+B'=m\kappa',\qquad
\gcd(A'B',m\kappa')=1.
\tag{19}
\]

若 \(\kappa>1\)，则

\[
\kappa'
\le\frac{\kappa+t}{\ell}
\le\frac{\kappa+\ell-1}{\ell}
<\kappa.
\tag{20}
\]

这是关系层的真实良基下降，而不是启发式尺寸变化。

## 4. 直接证书或 \(\kappa=1\) 周期归约

固定起始关系 \((\{A,B\},\kappa)\)，对每个满足 (14) 的素数加入 (18) 的边。
每个节点先检查 (10) 和 (5a)，每条边在跟随前再把合法载体 \(\ell\) 当作
alternate gap 检查。由于 \(\kappa\) 不增且

\[
A+B=m\kappa\le m\kappa_{\rm start},
\tag{21}
\]

可达关系图有限。无出边当且仅当不存在 (14)，也就是

\[
AB\mid px,
\tag{22}
\]

此时由 (10) 直接终止。若没有到达终端，(20) 迫使每条持续路径进入
\(\kappa=1\) 层，有限性再迫使其出现有向周期。因此

\[
\boxed{
\text{直接 Type I/II 自然尾终端}
\quad\lor\quad
\text{有限 }\kappa=1\text{ 周期障碍}.}
\tag{23}
\]

在底层有 \(A+B=m\)。式 (15) 给出 \(t=\ell-1\)，且 \(g=1\)，所以

\[
\boxed{
\{C,m-C\}
\longmapsto
\left\{\frac C\ell,m-\frac C\ell\right\}.}
\tag{24}
\]

每个 \(C\) 都是模 \(m\) 的单位；无序底层节点可嵌入
\(U(m)/\{\pm1\}\)，而 (24) 是允许坐标上的乘法

\[
[C]\longmapsto[\ell^{-1}C].
\tag{25}
\]

又因 \(A,B<m<p\)，底层不可能使用 \(p\) 槽，所以直接终端条件退化为
\(AB\mid x\)，即原 Type II 指数盒命中。空盒情形没有底层汇点，真正剩余对象
正是 (24) 的 SCC，而不是尚未分析的无限盒外空间。

## 5. \(p=67369\) 的两个中性载体压力点得到新终端

### 5.1 \(q=21\)

物理权最小关系为

\[
\frac AB=\frac7{657},\qquad
A+B=83\cdot8,\qquad
\Omega=3.
\tag{26}
\]

完整迁移给出

\[
\begin{aligned}
(\{7,657\},8)
&\xrightarrow{3}(\{10,73\},1)
\xrightarrow{2}(\{5,78\},1)\\
&\xrightarrow{5}(\{1,82\},1)
\xrightarrow{2}(\{41,42\},1)
\xrightarrow{2}(\{21,62\},1).
\end{aligned}
\tag{27}
\]

首边的 raw 三元组为 \((219,30,3)\)，规范化因子为 \(3\)，故直接落到
\(\kappa=1\)。在最后节点，素数 \(31\mid62\) 是超过 \(px\) 容量的合法边标签。
terminal-first 在跟随该边前检查 gap \(31\)，得到 Type I 证书

\[
(x_{31},d,y,z)
=(16850,3370,36618420,12334731684900).
\tag{28}
\]

相应恒等式为

\[
\frac4{67369}
=\frac1{16850}
+\frac1{36618420}
+\frac1{12334731684900}.
\tag{29}
\]

从 \(\{10,73\}\) 可达的整个底层图有 \(41\) 个节点，并构成一个 SCC；所以
(28) 是周期内部暴露的 alternate terminal，不是自然尾汇点。

### 5.2 \(q=42\)

物理权最小关系为

\[
\frac AB=\frac{1809}{28},\qquad
A+B=167\cdot11,\qquad
\Omega=3.
\tag{30}
\]

一条显式可达路径是

\[
\begin{aligned}
(\{28,1809\},11)
&\xrightarrow{3}(\{65,603\},4)
\xrightarrow{5}(\{13,154\},1)
\xrightarrow{13}(\{1,166\},1)\\
&\xrightarrow{83}(\{2,165\},1)
\xrightarrow{11}(\{15,152\},1)
\xrightarrow{2}(\{76,91\},1)\\
&\xrightarrow{13}(\{7,160\},1)
\xrightarrow{2}(\{80,87\},1)
\xrightarrow{5}(\{16,151\},1).
\end{aligned}
\tag{31}
\]

素数 \(151\) 是最后节点的超容量边标签，也是合法缺口。它给出新的 Type II 证书

\[
(x_{151},d,y,z)
=(16880,32,7545328,3980160520),
\tag{32}
\]

即

\[
\frac4{67369}
=\frac1{16880}
+\frac1{7545328}
+\frac1{3980160520}.
\tag{33}
\]

从 \(\{13,154\}\) 可达 \(21\) 个底层节点，其中唯一循环 SCC 有 \(19\) 个节点。
这证明“最小关系的局部共享缺口没有终端”不等于“该关系的完整迁移闭包没有终端”。

### 5.3 fresh quotient 分支真实但不全称

\(q=42\) 的另一个单位计数最小轨道

\[
\frac{A}{B}=\frac{9849}{4},\qquad
A+B=167\cdot59,\qquad
\Omega=7
\tag{34}
\]

具有新鲜关系商 \(\kappa=59\)。式 (5a) 直接调用 gap \(59\)，得到 Type I 证书

\[
(x_{59},d,y,z)
=(16857,151713,19250694,144100000454).
\tag{35}
\]

相反，\(q=21\) 的最小关系商 \(8\) 没有合法 \(3\bmod4\) 因子；\(q=42\) 的
物理最小关系商 \(11\) 虽合法，但 gap \(11\) 没有 Type I/II 证书。因此 quotient
菜单是真实终端来源，却不是单独的全称闭包。

### 5.4 \(p=1153\)：底层标签完备性的严格反例

取

\[
p=1153,\qquad q=16,\qquad m=63,\qquad x=304=2^4\cdot19.
\tag{36}
\]

这是端点允许状态；目标位于源生成子群，但 signed box 为空。完整检查
\(W\le19^2\) 得到且只得到

\[
(z_2,z_{19})\in
\{(-3,-3),(-3,3),(3,-3),(3,3)\},
\qquad W=19^2=361.
\tag{37}
\]

忽略 terminal-first 时，完整底层图含二周期

\[
\boxed{
\{1,62\}\xrightarrow{31}\{2,61\}
\xrightarrow{61}\{1,62\}.}
\tag{38}
\]

其内部标签只有 \(31,61\)。其中 \(61\equiv1\pmod4\)，唯一合法 gap \(31\)
没有 Type I/II 证书；原 gap \(63\) 也没有证书。因此

\[
\boxed{\text{“每个 }\kappa=1\text{ SCC 自含短证书边标签”是假的}.}
\tag{39}
\]

不过 (37) 的两个反足轨道都在进入该 SCC 前被 fresh quotient 抢占。代表
\[
\frac1{54872},\quad \kappa=871
\]
沿载体 \(19\) 到达

\[
(\{5,1444\},23),
\]

其中 quotient gap \(23\) 给出 Type II 证书

\[
(x_{23},d,y,z)=(294,28,16142,169491).
\tag{40}
\]

另一个代表

\[
\frac{6859}{8},\quad \kappa=109
\]
沿载体 \(19\) 到达 \((\{17,361\},6)\)，其 quotient divisor \(3\) 给出 Type I
证书

\[
(x_3,d,y,z)=(289,17,111078,2177239878).
\tag{41}
\]

所以 (36) 不是组合菜单反例，而是严格的调度定理：fresh-quotient terminal 必须在
底层 SCC 标签适配器之前运行；只检查 SCC 内标签会错误报告未闭合。
此外 \(p=1153\) 在更外层的全局 terminal-first 中已经由 gap \(3\) Type I 预占；
本例的作用只是否定 SCC 内部标签完备性，不是制造新的未解决核心素数。

## 6. 与 E1--E5 的准确边界

关系迁移 (16)--(20) 具有确定的整数前提、构造和严格 \(\kappa\) 降层，但它仍不是
状态合同中的递归边：

1. 后继只是 \((A',B',\kappa')\)，没有构造完整的 equation target、
   marked solution set、模数上下文和合法正规形，故不满足 E2；
2. 非终端节点的自然尾至少有一个非整数，没有给出
   \(W_T\to W_S\) 的全域解提升，故不满足 E4；
3. \(\kappa\) 只在内部搜索的上层严格下降，底层存在真实周期，所以它不是跨合法状态
   的全域 E5 势；
4. (16) 会引入 \(B+mt\) 的新素因子，不能假定后继仍在原奇核源列或原指数盒内。

因此规范类型是

~~~text
certificate_type = type_ii_natural_tail_relation_graph
selector_status = analysis_evidence
recursive_edge_eligible = false
~~~

只有三类输出可以升级：

1. \(AB\mid px\) 时，按 (10) 直接输出 Type I/II terminal；
2. \(\kappa\) 的合法因子通过短证书 verifier 时，输出 fresh-quotient terminal；
3. 关系节点或边标签产生其它合法缺口并通过完整短证书 verifier 时，输出
   alternate Type I/II terminal。

若完整可达图没有这两类终端，应输出
KAPPA_ONE_RELATION_SCC，并把该 SCC 交给新的 source-switch 或 E1--E5
适配器；不能把图内的 \(\kappa\) 降层冒充递归证明。

## 7. 一般有限阿贝尔源群接口与剩余缺口

式 (2)--(25) 不使用循环离散对数，只使用一个真实整数指数原像 \(z\) 及目标
\(-1\) 的同余。因此对任意有限阿贝尔源群，只要二阶目标位于源像中，任取一个完整
整数原像并按正负部分形成 \(A/B\)，同样得到物理缺口 (13)、\(px\) 容量和完整关系图。
循环假设只负责把原有限盒写成单个奇模仿射方程，不负责本定理的关系迁移。

这已经把一般空盒的待证对象收缩为：证明至少一个规范整数原像的可达关系图出现自然尾、
fresh-quotient 或 edge-label terminal，或者把每个剩余 KAPPA_ONE_RELATION_SCC 转成满足
E1--E5 的严格可提升后继。当前定理关闭了 \(p=67369\) 的两个最小中性载体压力点，
而 \(p=1153\) 证明一般 SCC 不必自含可证书边标签；全称空盒转交目标因此仍须一个
跨 SCC 的真实适配器。

后续的真因子端点定理已经构造出一个这样的条件性适配器：若 terminal-first 后的
source-reachable 底层节点含较小坐标 \(a\mid q\)、\(a<q\)，则以
\(q'=a\) 重建合法 \(p-1\) Type II 端点；命中时直接终止，否则以
\(\operatorname{Sol}(p)\) 恒等提升和势 \(q'<q\) 得到完整 E1--E5 边。因此本节所留的
全称缺口进一步缩为这个真因子坐标的存在性，而不是 E2/E4/E5 的构造。见
[Type II 关系图可达底层的真因子端点递降](type-II-relation-reach-proper-endpoint-descent.md)。

聚焦验证：

~~~bash
python3 reproductions/type_ii_odd_kernel_overflow_natural_tail_relation_graph.py --verify
~~~

验证器只检查本定理的容量恒等式、规范迁移、两条显式路径、底层 SCC 规模和 gap
\(31,151\) 证书，不运行历史范围测试。
