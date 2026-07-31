---
kind: claim
claim_id: type-I-bottom-word-lattice-pareto-cycle-capacity-selector
title: 底层路径字的格正规形、有限 Pareto 前沿与周期容量选择器
statement: 底层 formal 边在祖先定向的缩放坐标上由两个三角整数矩阵作用，任意完整定向路径字唯一压成 M(Q,A,B)=((A+1,A),(B,B+1))，其中 A+B=Q-1，并满足 QX'=X+AR、QY'=Y+BR、SNF(M)=diag(1,Q)。固定路径字的根位于指标 Q 的格；同向闭环进一步满足 Q=1 mod R 和 M=I+((Q-1)/R)(X,Y)^T(1,1)。沿闭环重复时，每个来源交叉乘积的赋值向量恰为 |d-nv(Q)|，故命中 K 或 x_R 等价于一维整数区间交，miss 有静态素数或区间分离证书。对任意有限 ancestry-lifted Reach，固定首后继和定向终点后的全部路径四通道容量 Pareto 前沿有限，且每个极小签名及任一直接容量命中都有显式有限长度见证。线性 F strong miss (p,R)=(57073,23) 反驳“必有最短来源字使 slab-q 进入至少一个共同过载因子”；(2017,207) 的底部二循环确有静态 103 分离，但其路径前缀已有 R_103=115 的合法 absorption，且 p 本身已有 gap 15 终端，所以它不是 terminal-first 或 terminal-or-descent 反例。路径字还给出端点差的闭式，但闭合词只恢复节点自身的 affine gap，不能由周期积自动产生新终端。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-I-psi-one-source-word-large-slab-constraint
  - type-I-source-word-joint-capacity-common-split-dichotomy
  - type-I-target-fiber-joint-capacity-signed-carrier-dictionary
  - type-I-formal-external-slab-collision-absorption-rechart
  - denominator-escape-state-contract
topics:
  - type-I
  - formal-target-pair
  - path-word
  - bottom-SCC
  - representation-lattice
  - Smith-normal-form
  - Pareto
  - q-adic-capacity
  - support-switch
  - selector
  - counterexample-boundary
sources:
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: finite-Reach-and-bottom-cycle-reduction
  - claim: type-I-psi-one-source-word-large-slab-constraint
    role: ancestry-oriented-path-word
  - claim: type-I-source-word-joint-capacity-common-split-dichotomy
    role: four-channel-joint-capacity
  - claim: type-I-formal-external-slab-collision-absorption-rechart
    role: resource-anchored-absorption-state-contract
visibility: public
last_checked: '2026-08-01'
---

# 底层路径字的格正规形、有限 Pareto 前沿与周期容量选择器

## 1. 底层边的两个生成矩阵

固定合法核心图表

\[
p\equiv1\pmod {24},
\qquad
3\le R\le p-2,
\qquad
4K=pR+1.
\tag{1}
\]

在 \(m=1\) 层按 ancestry 定向节点为

\[
X+Y=R,
\qquad (X,Y)=1.
\tag{2}
\]

若当前累计路径字为 \(\Theta\)，定义缩放坐标

\[
S_X=\Theta X,
\qquad
S_Y=\Theta Y.
\tag{3}
\]

底层边没有额外正规公因子。若选择 \(q\mid X\)，则

\[
(X,Y,\Theta)\longmapsto
\left(\frac Xq,R-\frac Xq,q\Theta\right),
\]

所以

\[
\binom{S_X'}{S_Y'}
=
M_X(q)\binom{S_X}{S_Y},
\qquad
M_X(q)=
\begin{pmatrix}
1&0\\
q-1&q
\end{pmatrix}.
\tag{4}
\]

若选择 \(q\mid Y\)，保持 ancestry 标签后的对称式为

\[
\binom{S_X'}{S_Y'}
=
M_Y(q)\binom{S_X}{S_Y},
\qquad
M_Y(q)=
\begin{pmatrix}
q&q-1\\
0&1
\end{pmatrix}.
\tag{5}
\]

式 (4)--(5) 把“一个交叉表示不变、另一个仿射更新”提升成完整的整数矩阵作用。

## 2. 任意底层词的唯一半群正规形

对 \(Q\ge1\)、\(A,B\ge0\) 且 \(A+B=Q-1\)，记

\[
M(Q,A,B)=
\begin{pmatrix}
A+1&A\\
B&B+1
\end{pmatrix}.
\tag{6}
\]

两个生成元分别是

\[
M_X(q)=M(q,0,q-1),
\qquad
M_Y(q)=M(q,q-1,0).
\tag{7}
\]

直接相乘得到组合律

\[
\boxed{
M(Q_2,A_2,B_2)M(Q_1,A_1,B_1)
=M(Q_1Q_2,A_1+Q_1A_2,B_1+Q_1B_2).
}
\tag{8}
\]

因此任意完整的定向底层路径字 \(w\)，其边标号乘积

\[
Q(w)=\prod_{e\in w}q_e
\tag{9}
\]

连同每一步的 \(X/Y\) 分支方向，唯一决定一个矩阵

\[
\boxed{
M(w)=M(Q,A,B),
\qquad A+B=Q-1.
}
\tag{10}
\]

若路径从 \((X,Y)\) 到按 ancestry 定向的 \((X',Y')\)，则

\[
\boxed{
QX'=X+AR,
\qquad
QY'=Y+BR.
}
\tag{11}
\]

唯一性来自矩阵的两个非对角元就是 \(A,B\)。必须保留完整定向字：标签积 \(Q\) 单独
并不决定 \(A,B\)，最短的反例就是 \(M_X(q)\ne M_Y(q)\)。

### 格与 Smith 正规形

矩阵满足

\[
M(Q,A,B)\binom1{-1}=\binom1{-1},
\qquad
(1,1)M(Q,A,B)=Q(1,1).
\tag{12}
\]

所以它固定差分子格 \(\mathbb Z(1,-1)\)，并在和坐标商格上乘以 \(Q\)。又因矩阵条目
的最大公因子为 1、行列式为 \(Q\)，有

\[
\boxed{\operatorname{SNF}(M)=\operatorname{diag}(1,Q).}
\tag{13}
\]

固定词 \((Q,A)\) 能作用于一个定向根 \((X,R)\) 的必要整数条件为

\[
\boxed{X+AR\equiv0\pmod Q.}
\tag{14}
\]

这是 \(\mathbb Z^2\) 中指标恰为 \(Q\) 的格。固定 \(R\) 时，区间
\(1\le X\le R-1\) 内同一词的可能定向根数至多

\[
\boxed{\left\lceil\frac{R-1}{Q}\right\rceil.}
\tag{15}
\]

特别地，\(Q\ge R\) 时至多一个。式 (15) 是第一个不依赖扫描的路径字复用容量；它只
是必要根容量，中间每条 formal 边的合法性仍须逐边核验。

## 3. 同向与换向闭环

若非空路径字回到同一个定向节点 \((X,Y)\)，由 (11) 得

\[
(Q-1)X=AR,
\qquad
(Q-1)Y=BR.
\]

因 \((X,R)=(Y,R)=1\)，所以

\[
\boxed{
Q\equiv1\pmod R,
\qquad
c=\frac{Q-1}{R}\in\mathbb N,
\qquad
A=cX,\quad B=cY.
}
\tag{16}
\]

闭环矩阵因而具有秩一更新正规形

\[
\boxed{
M=I+c\binom XY(1,1).
}
\tag{17}
\]

若一次闭环把 ancestry 两侧交换，则相同计算给出 \(Q\equiv-1\pmod R\)；把该词平方
后得到同向闭环，并可调用 (16)--(17)。

## 4. 路径字 rechart 的合同边界

底层每个边素数都小于 \(R<p\)，所以 \((p,Q(w))=1\)。对任意非空底层词可以定义

\[
1\le R_Q<4Q,
\qquad
pR_Q\equiv-1\pmod {4Q},
\qquad
K_Q=\frac{pR_Q+1}{4}.
\tag{18}
\]

于是

\[
R_Q\equiv3\pmod4,
\qquad
\boxed{Q\mid K_Q.}
\tag{19}
\]

若新图表中心命中，它直接恢复原 \(p\) 的 Type I 终端，不需要把中间 formal 边升级
为递降边。但仅有

\[
R_Q<R
\tag{20}
\]

并不足以把任意路径词登记为 E4：状态合同还要求该 \(Q\) 来自规范的带符号缺陷或已有
slab 容量接口。对 single-external slab 的完整外幂 \(Q=q^e\)，已有 absorption 定理
提供 E1--E5；对任意合数路径词，若没有 \(Q\mid M\mid L\) 或等价的载体锚定，(18)--(20)
只能登记为 candidate rechart。这个限制阻止“任取一个模数重编码同一方程”被误报为
猜想下降。

## 5. 同向周期是一条精确容量射线

固定一条到达底层节点 \((X,Y)\) 的来源路径，路径字为 \(\Theta\)，首后继 ancestry
坐标为 \(U,V\)。两个交叉乘积是

\[
L_U=\frac{U\Theta Y}{(U,\Theta Y)^2},
\qquad
L_V=\frac{V\Theta X}{(V,\Theta X)^2}.
\tag{21}
\]

设该节点有同向闭环，词积为 \(Q\)。绕环 \(n\ge0\) 次后，终点和 ancestry 不变，
路径字变成 \(\Theta Q^n\)。对任意素数 \(\ell\)，令

\[
\begin{aligned}
d_{U,\ell}&=v_\ell(U)-v_\ell(\Theta Y),\\
d_{V,\ell}&=v_\ell(V)-v_\ell(\Theta X),\\
w_\ell&=v_\ell(Q).
\end{aligned}
\tag{22}
\]

使用 \(v_\ell(AB/(A,B)^2)=|v_\ell(A)-v_\ell(B)|\)，得到

\[
\boxed{
v_\ell(L_U(n))=|d_{U,\ell}-nw_\ell|,
\qquad
v_\ell(L_V(n))=|d_{V,\ell}-nw_\ell|.
}
\tag{23}
\]

所以对 \(D\in\{K,x_R\}\) 和 \(i\in\{U,V\}\)，命中 \(L_i(n)\mid D\) 精确等价于

\[
|d_{i,\ell}-nw_\ell|\le v_\ell(D)
\qquad\text{对所有 }\ell.
\tag{24}
\]

当 \(w_\ell=0\) 时，若

\[
|d_{i,\ell}|>v_\ell(D),
\tag{25}
\]

则 \(\ell\) 是 MISS_STATIC 证书。当 \(w_\ell>0\) 时，(24) 给出整数区间

\[
\left\lceil
\frac{d_{i,\ell}-v_\ell(D)}{w_\ell}
\right\rceil
\le n\le
\left\lfloor
\frac{d_{i,\ell}+v_\ell(D)}{w_\ell}
\right\rfloor.
\tag{26}
\]

把全部区间与 \(n\ge0\) 相交：

- 交集含整数时为 CYCLE_RAY_HIT，并由 (21) 恢复 Type I 或 gap-\(R\) Type II；
- 有 (25) 时为 MISS_STATIC；
- 没有静态障碍但区间交为空时为 MISS_INTERVAL，最大下界与最小上界就是两坐标短
  对偶分离证书。

因此无限次绕环不是无限搜索问题，而是四个一维整数区间系统。

## 6. 所有路径的规范有限 Pareto 前沿

最短图路径不是容量选择不变量：不同等长路径可以产生不同 \(\Theta\)，绕环也能任意
放大它。正确对象是全部路径容量签名的 Pareto 前沿。本节证明它仍有显式有限见证界。

取任意有限 formal Reach，并把每个无序节点提升为“节点 + ancestry 方向”，得到有限
有向图 \(\widetilde G\)，记顶点数为 \(N\)。每条边保留完整整数标签 \(h_e=q_eg_e\)；
在底层 \(g_e=1\)。固定首后继 \(U,V\)、起点和一个 ancestry 定向的 \(m=1\) 终点
\((X,Y)\)，并令路径 \(w\) 的标签赋值向量为

\[
t(w)_\ell=v_\ell\left(\prod_{e\in w}h_e\right).
\tag{27}
\]

置

\[
a_\ell=v_\ell(U)-v_\ell(Y),
\qquad
b_\ell=v_\ell(V)-v_\ell(X).
\tag{28}
\]

再记

\[
\nu_\ell=v_\ell(K),
\qquad
\sigma_\ell=v_\ell(x_R).
\]

由 (21) 的同一赋值计算，四通道容量签名为

\[
\Sigma(w)=
\left(
(|a-t|-\nu)_+,
(|a-t|-\sigma)_+,
(|b-t|-\nu)_+,
(|b-t|-\sigma)_+
\right).
\tag{29}
\]

其中绝对值、正部和减法都逐坐标作用。对有限多个允许终点分别应用以下定理，再取有限
并，仍得到完整有限前沿。

偏序取所有坐标逐一比较。令 \(\mathcal P_{\rm move}\) 为边标签中实际出现的有限素数集，
并定义

\[
m_\ell=\max(0,a_\ell,b_\ell)
\qquad(\ell\in\mathcal P_{\rm move}),
\tag{30}
\]

以及截断计数

\[
\widehat t_\ell=\min(t_\ell,m_\ell).
\tag{31}
\]

则有显式界

\[
\boxed{
B=N\prod_{\ell\in\mathcal P_{\rm move}}(m_\ell+1).
}
\tag{32}
\]

**有限前沿定理。**

1. 每个 Pareto 极小容量签名都有一条长度 \(<B\) 的实现路径；
2. 若任意路径使 \(L_U\) 或 \(L_V\) 整除 \(K\) 或 \(x_R\)，则也存在一条长度
   \(<B\) 的命中路径；
3. 因而完整无限路径集的直接容量命中与 Pareto 前沿可由一个有限、路径选择无关的
   搜索判定。

### 证明

对一个 Pareto 极小签名选取最短实现路径。若其长度至少为 \(B\)，则按鸽巢原理存在两个
路径前缀，它们到达相同 lifted vertex，并具有相同截断向量 \(\widehat t\)。删除两前缀
之间的闭合子路，终点和 ancestry 不变。

若该子路在素数 \(\ell\) 上增加了正赋值，则两个截断值相同迫使删除点之前已经有
\(t_\ell\ge m_\ell\)。删除后最终赋值仍至少为 \(m_\ell\)。而 (29) 中关于
\(t_\ell\) 的四个函数，在

\[
t_\ell\ge\max(0,a_\ell,b_\ell)=m_\ell
\]

以后都单调不减。因此删环不会增大任何容量坐标。若有坐标严格减小，原签名不极小；
若全部相同，原实现路径不是最短。两者都矛盾，故第一项成立。

若存在命中路径，取其签名之下的 Pareto 极小签名。被命中的整块缺陷坐标全为零，支配
它的签名在该块仍只能为零，所以相应极小路径仍命中。结合第一项即得第二项，第三项随之
成立。证毕。

这一定理用完整 Pareto 前沿替代了任意 lex tie-break，也严格解释了为何可以有限检查
SCC，而无需假设“图最短路径”就是容量最优路径。

## 7. 两个反例边界

### 7.1 线性源也不能救回 shortest slab-\(q\) 候选

取

\[
(p,R,K,x_R)=(57073,23,328170,14274).
\tag{33}
\]

它有真正线性源

\[
(a,s)=(2378,1),
\qquad
p=a+s+asR,
\qquad
(aR+1)(sR+1)=4K.
\tag{34}
\]

中心完整平方除子盒含 81 点且目标 \(-1\) 零命中，所以状态为 F。一层正壳边

\[
(20,3,1)\xrightarrow{q_*=2,\ g=1}(10,13,1)
\tag{35}
\]

只有一层 \(2\)-进超额。首后继本身就是 large slab

\[
(Q,\alpha,\beta)=(13,1,10).
\tag{36}
\]

因此从 post-first anchor 到该 slab 的最短后缀是唯一空路。定向只能取

\[
U=10\mid K,
\qquad
V=13,
\qquad
\Theta=1.
\]

两个交叉乘积相同：

\[
L_U=L_V=130,
\qquad
C(L_U)=C(L_V)=1,
\tag{37}
\]

因为 \(13\mid x_R\) 恰一层。与此同时，该 slab 的 direct/cross collision 命中集、
节点和 anchor external-affine 命中集均为空，且

\[
R_{13}=43>23.
\tag{38}
\]

所以它确为 linear-source、F、\(\Psi_0=1\) 的 strong large-slab miss，却没有任何
最短路径使 slab 素数 \(13\) 进入共同过载。旧的最短路径载体候选即使补上“线性源”
仍为假。

该状态已有内部 gap \(15\) 的 Type I，完整 Reach 也有 external gap \(7\) 的 Type I。
所以 (33) 只关闭按现有 strong-miss 定义写出的载体量词；它不否定同时加入完整
terminal-first unresolved 前提的更窄命题，更不是 Erdős--Straus 反例。

### 7.2 局部 internal-free 的底部静态分离

取

\[
(p,R,K,x_R)=(2017,207,104380,556).
\tag{39}
\]

真实来源边

\[
(1156,1535,13)\xrightarrow{17}(68,139,1)
\tag{40}
\]

直接到达另一个 strong slab \((Q,\alpha,\beta)=(139,1,68)\)。这里也是
\(C(68\cdot139)=1\)，且 \(R_{139}=231>207\)；状态还同时为 F、internal-free，
但不来自线性源。

从该 slab 依次走标签 \(139,103\) 到达 \((2,205)\)，累计字
\(\Theta=139\cdot103\)。其底部二循环为

\[
(2,205)\xrightarrow{41}(5,202)\xrightarrow{101}(2,205).
\tag{41}
\]

按 ancestry 定向，循环矩阵是

\[
\boxed{
Q=41\cdot101=4141=1+20R,
\qquad
M=
\begin{pmatrix}
41&40\\
4100&4101
\end{pmatrix}
=I+20\binom2{205}(1,1).
}
\tag{42}
\]

对两个交叉表示，素数 \(103\) 都满足 \(w_{103}=0\)、\(|d_{103}|=1\)，而
\(103\nmid Kx_R\)。所以四个容量通道均有 MISS_STATIC(103)；无限重复 (41) 只改变
\(41,101\) 的赋值，永远不能修复该容量盒。

这个结论只描述进入二循环后的受限 path language。它不能被写成完整选择器反例：
路径前缀中的中间节点

\[
(1,206)=(1,103\cdot2)
\]

是 clean single-external slab，并满足

\[
R_{103}=115<207,
\qquad
K_{103}=57989=103\cdot563.
\tag{42a}
\]

所以 SCC 压缩前已经存在现有 E1--E5 合同下的 verified absorption。循环节点
\((5,202)=(5,101\cdot2)\) 还给出 \(R_{101}=135<207\)，新图表中心除子 \(101\)
直接产生 gap \(3\) 的 Type I 证书。更早的 terminal-first 又会发现原素数 gap \(15\)
同时有 Type I 和 Type II 证书。因此 (39) 只反驳“沿指定 cycle ray 重复必修复四通道
容量”，不反驳终端、absorption 或递降。

## 8. 路径字对端点差的闭式与证书边界

固定 canonical 节点

\[
N_r=\{r,R-r\},
\qquad
N_s=\{s,R-s\},
\qquad
1\le r,s<\frac R2.
\tag{42b}
\]

设路径字 \(M(Q,A,B)\) 从定向 \((r,R-r)\) 出发，ancestry 终点第一坐标为

\[
t=\frac{r+AR}{Q}.
\tag{42c}
\]

于是无序终点为 \(N_s\) 当且仅当 \(t=s\) 或 \(t=R-s\)。定义

\[
\begin{aligned}
D_0&=A(R-r)-Br=Q(t-r),\\
D_1&=(B+1)R-(Q+1)r=Q((R-r)-t),
\end{aligned}
\tag{42d}
\]

以及

\[
\begin{aligned}
g_\parallel
&=(r,R-s)(s,R-r),\\
g_\times
&=(r,s)(R-r,R-s).
\end{aligned}
\tag{42e}
\]

把两节点的 parallel/cross 乘积对约到互素后，其 \(R\)-倍差值为

\[
\begin{array}{c|cc}
&h_\parallel&h_\times\\ \hline
t=s&
\dfrac{D_1}{Qg_\parallel}&
\dfrac{|D_0|}{Qg_\times}\\[2mm]
t=R-s&
\dfrac{D_0}{Qg_\parallel}&
\dfrac{|D_1|}{Qg_\times}.
\end{array}
\tag{42f}
\]

这把端点差变成路径字的精确有界候选；但它不是路径矩阵自身的新 primitive 关系。若约分
后的端点差对为

\[
(u,v)=1,
\qquad
v-u=Rh,
\tag{42g}
\]

则对合法奇数 \(h>1\)，这对 \((u,v)\) 本身严格不可能充当 gap \(h\) 的 Type II
正规形：条件 \(h\mid u+v\) 会与 \(v\equiv u\pmod h\)、\((u,h)=1\) 一起推出
\(h\mid2\)。它自身充当 Type I 正规形当且仅当

\[
\boxed{
uv\mid\frac{p+h}{4},
\qquad
h\mid p+1.
}
\tag{42h}
\]

同一 gap 仍可由另一组平方除子命中，所以 (42h) 是 native-pair 判据，不是 gap 的完整
miss 判据。

若路径闭合回 \(N_r\)，则端点差退化为

\[
\boxed{
h_\times=0,
\qquad
h_\parallel=R-2r.
}
\tag{42i}
\]

右侧完全不含 \(Q,A,B\)。因此闭环端点差只恢复节点自身已在仿射菜单中的 gap；周期积
\(Q\) 的新增信息只存在于容量射线或载体锚定 rechart 中。

两个冻结例的归因据此精确化：

1. \(p=5596369,R=35\) 的两步词 \((2,19)\) 从 \(N_3\) 到 \(N_1\)，给
   \((h_\parallel,h_\times)=(31,1)\)；gap \(31\) 的实际证书使用另一正规形，而
   \(Q=38\) 选择 \(R_{38}=23\) 是独立 candidate rechart。
2. \(p=212973049,R=215\) 的 gap \(35\) 来自单边
   \(N_2\xrightarrow{71}N_3\)。三步词 \((107,71,53)\) 的首尾
   \(N_1\to N_4\) 只给 \((105,3)\)；完整闭环在 \(N_4\) 给出的 \(207\) 只是
   \(R-2\cdot4\)，不是周期积产生的新 gap。

最小核心例 \(p=73,R=11\) 的真实边
\(N_4\xrightarrow7N_1\) 两种端点差都给合法 gap \(3\)，但完整 Type I/II 平方除子谱
仍 miss。因此“任意真实路径端点必有一个差值终端”也是错误的。

## 9. 短路径确实可以生成合法直接终端

上述反例否定特定载体规则，不否定把路径作为候选生成器。

### 8.1 \(p=5596369,R=35\)

残余节点 \(\{3,32\}\) 沿三条 \(q=2\) 边到达

\[
\{3,32\}\to\{16,19\}\to\{8,27\}\to\{4,31\}.
\tag{43}
\]

前三个暴露 gap \(3,19,27\) 的完整谱均 miss；末节点的 external gap \(31\) 则有
Type I 除子 \(d=85\)，恢复

\[
\frac4{5596369}
=\frac1{1399100}
+\frac1{252576769935}
+\frac1{23266420776626664606900}.
\tag{44}
\]

另一条两边词 \(w=(2,19)\) 从 \(\{3,32\}\) 到 \(\{1,34\}\)，其 \(Q=38\) 给出

\[
R_{38}=23<35,
\qquad
K_{38}=32179122.
\tag{45}
\]

新图表中心除子 \(684\) 命中并产生 gap \(119\)，所以路径选图后可独立恢复直接终端。
但 \(38\) 不满足唯一 single-slab 的 \(32\mid M\mid96\)，故 (45) 不是现有
absorption E1 下的 verified E4。

### 8.2 \(p=212973049,R=215\)

large slab \(\{2,213\}\) 一步 \(71\)-peeling 后到达

\[
\{3,212\}=\{3,53\cdot4\}.
\]

这里 \(3\cdot4\mid K\)，所以暴露的 single-external \(Q=53\) 满足已有 absorption
接口。其规范图表为

\[
R_{53}=171<215,
\qquad
K_{53}=9104597845,
\tag{46}
\]

并且中心除子 \(1325\) 产生 gap \(31\) 和直接解

\[
\frac4{212973049}
=\frac1{53243270}
+\frac1{365855517964342}
+\frac1{1939033962968479405}.
\tag{47}
\]

从 \(\{3,212\}\) 到 \(R_{53}\) 的 absorption 宏边通过现有 E1--E5；到达
\(\{3,212\}\) 的前导 \(71\)-formal 边仍只是候选生成步骤。由于新图表已经直接命中，
本例最终不需要递归使用那条 formal 边。

## 10. 良基边界与下一接口

任何只依赖当前 bottom 节点的势函数都不可能沿完整边集严格下降，因为 (41) 一类有向环
真实存在。对固定权赋值势

\[
\Phi(\text{node})+\sum_\ell c_\ell v_\ell(\Theta)
\tag{48}
\]

也一样：绕一圈的总增量若非负，就不可能每边严格下降；若为负，重复闭环使 (48) 无下界，
因而不是良基自然数势。

正确调度是：

1. 把 SCC 凝聚图作为有限分析 DAG；
2. 在 SCC 内输出 CYCLE_RAY_HIT、MISS_STATIC、MISS_INTERVAL 或完整有限 Pareto 前沿；
3. 只有直接终端或满足完整载体合同的 rechart 宏边进入证明图。

凝聚 DAG 的下降只是分析调度，不是 E4。当前仍需证明：每个 sink-SCC 的规范 miss
证书如何强制新的 Type I/II、改变根尾数据的标记状态，或另一条严格可提升递降。

## 11. 聚焦复现

聚焦脚本只验证 (4)--(17)、两个反例、两个短路径终端和相应 unit-fraction 恒等式；它
不重跑 483 态或 1412 slabs 的历史普查：

~~~bash
python3 reproductions/type_i_bottom_word_lattice_pareto_cycle_capacity.py
python3 reproductions/type_i_bottom_word_lattice_pareto_cycle_capacity.py --verify
~~~

结果文件为

~~~text
reproductions/type-i-bottom-word-lattice-pareto-cycle-capacity-results.json
~~~
