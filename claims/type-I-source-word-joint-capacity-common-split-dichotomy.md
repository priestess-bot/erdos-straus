---
kind: claim
claim_id: type-I-source-word-joint-capacity-common-split-dichotomy
title: 来源交叉表示的联合容量共同过载—分裂交换二分
statement: 对核心图表 4K=pR+1 和 x_R=(p+R)/4，令 g=gcd(K,x_R)、kappa=K/g、xi=x_R/g。任一目标乘积 L 相对 K 与 x_R 的缺陷 e_K=L/gcd(L,K)、e_x=L/gcd(L,x_R) 满足 gcd(e_K,e_x)=L/gcd(L,lcm(K,x_R))、lcm(e_K,e_x)=L/gcd(L,g)。因此双容量 miss 精确二分为：存在同一素数同时超过两种容量；或 L 整除联合容量且两个缺陷互素，分别整除 xi、kappa，并满足一条精确容量交换恒等式。来源路径字产生的两个交叉目标乘积逐一适用该二分；至少一个乘积共同过载和两个乘积共享同一过载素数分别由 lcm、gcd 的整除失败精确刻画。分裂交换恒等式本身没有构造标记状态、解提升或 E4，也不强制任何有界深度的同图表 external Reach 终端；p=2017,R=207 是后一个窄命题的精确反例，但它已有 ordinary gap 15 和前缀 q=103 absorption，不能作为 terminal-first 或 terminal-or-descent 反例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-source-word-bottom-projection-dual-capacity
  - type-I-psi-one-source-word-large-slab-constraint
  - type-I-formal-full-excess-cycle-or-hit-reduction
  - type-II-coprime-factor-normal-form
topics:
  - type-I
  - type-II
  - formal-target-pair
  - path-word
  - q-adic-capacity
  - common-overload
  - split-capacity
  - external-slab
  - proof-boundary
sources:
  - claim: type-I-source-word-bottom-projection-dual-capacity
    role: source-word-cross-target-pairs
  - claim: type-I-psi-one-source-word-large-slab-constraint
    role: nonnegative-path-word-transport
  - claim: type-I-formal-full-excess-cycle-or-hit-reduction
    role: target-product-to-Type-I-interface
  - claim: type-II-coprime-factor-normal-form
    role: target-product-to-gap-R-Type-II-interface
visibility: public
last_checked: '2026-08-01'
---

# 来源交叉表示的联合容量共同过载—分裂交换二分

## 1. 两种容量的公共轴与独占轴

固定核心素数与合法图表

\[
p\equiv1\pmod {24},
\qquad
3\le R\le p-2,
\qquad
R\equiv3\pmod4,
\qquad
4K=pR+1,
\tag{1}
\]

并记

\[
x=x_R=\frac{p+R}{4},
\qquad
\Delta=\frac{R^2-1}{4}.
\tag{2}
\]

直接相减得到两条基本恒等式

\[
Rx-K=\Delta,
\qquad
px-K=\frac{p^2-1}{4}.
\tag{3}
\]

令

\[
g=(K,x),
\qquad
\kappa=\frac Kg,
\qquad
\xi=\frac xg,
\qquad
\delta=\frac\Delta g.
\tag{4}
\]

由 \(R<p\)、\(p\) 为素数可知 \((p,R)=1\)。将 (1)--(2) 模 \(R\) 化简，还得到

\[
(K,R)=(x,R)=1.
\]

由欧几里得算法，

\[
\boxed{
g=\left(x,\frac{R^2-1}{4}\right)
=\frac{(p+R,R^2-1)}4
=\frac{(p+R,p^2-1)}4.
}
\tag{5}
\]

而且

\[
(\kappa,\xi)=1,
\qquad
\boxed{
\operatorname{lcm}(K,x)=g\kappa\xi=\frac{Kx}{g}.
}
\tag{6}
\]

所以 \(g\) 是两种容量的公共轴，\(\kappa\)、\(\xi\) 是互素的独占轴。

## 2. 任意目标乘积的两个精确缺陷因子

对任意正整数 \(L\)，定义

\[
e_K(L)=\frac{L}{(L,K)},
\qquad
e_x(L)=\frac{L}{(L,x)}.
\tag{7}
\]

逐素数比较赋值立刻得到

\[
\boxed{
(e_K(L),e_x(L))
=\frac{L}{(L,\operatorname{lcm}(K,x))},
}
\tag{8}
\]

以及

\[
\boxed{
\operatorname{lcm}(e_K(L),e_x(L))
=\frac{L}{(L,g)}.
}
\tag{9}
\]

确切地说，若

\[
\ell=v_q(L),
\qquad
k=v_q(K),
\qquad
y=v_q(x),
\]

则 (8) 两边的 \(q\)-进指数都是

\[
\max\{0,\ell-\max(k,y)\},
\]

而 (9) 两边的指数都是

\[
\max\{0,\ell-\min(k,y)\}.
\]

因此定义规范共同过载因子

\[
\boxed{
C(L)=\frac{L}{(L,\operatorname{lcm}(K,x))}
=(e_K(L),e_x(L)).
}
\tag{10}
\]

其素因子恰好是满足

\[
v_q(L)>v_q(K)
\quad\text{且}\quad
v_q(L)>v_q(x)
\tag{11}
\]

的共同过载素数；\(C(L)\) 还保留超过联合容量的精确指数。

## 3. 共同过载—分裂交换二分

假设 \(L\) 同时 miss 两种容量，即

\[
L\nmid K,
\qquad
L\nmid x,
\tag{12}
\]

等价地 \(e_K(L)>1\)、\(e_x(L)>1\)。则恰有以下一支发生。

### 3.1 共同过载支

若

\[
C(L)>1,
\tag{13}
\]

则每个 \(q\mid C(L)\) 都同时满足 (11)。等价地，

\[
\boxed{
C(L)>1
\iff
L\nmid\operatorname{lcm}(K,x).
}
\tag{14}
\]

这给出可直接送入跨状态 \(q\)-进容量账本的规范载体，但单个状态上的共同过载还不是
容量矛盾。

### 3.2 分裂交换支

若

\[
C(L)=1,
\tag{15}
\]

则 \(L\mid\operatorname{lcm}(K,x)\)，并且

\[
\boxed{
e_K(L)\mid\xi,
\qquad
e_x(L)\mid\kappa,
\qquad
(e_K(L),e_x(L))=1.
}
\tag{16}
\]

所以 \(K\) 所缺的部分完全由 \(x\) 的独占容量供应，\(x\) 所缺的部分完全由 \(K\)
的独占容量供应。由 (9) 还有

\[
\boxed{
e_K(L)e_x(L)=\frac{L}{(L,g)}.
}
\tag{17}
\]

这不只是一种支持分拆。两个交换因子还避开 (3) 的剩余量：

\[
\boxed{
(e_K(L)e_x(L),\delta)=1.
}
\tag{18}
\]

证明 (18) 时，以 \(q\mid e_K(L)\) 为例。由 (16) 必有
\(v_q(x)>v_q(K)\)。又因 \((K,R)=(x,R)=1\)，所以 \(q\nmid R\)；在
\(Rx-K=\Delta\) 中两项赋值不等，故

\[
v_q(\Delta)=v_q(K)=v_q(g),
\]

即 \(q\nmid\delta\)。另一交换因子完全对称。

进一步有

\[
4ge_K(L)\mid p+R,
\qquad
4ge_x(L)\mid pR+1.
\tag{19}
\]

置

\[
a=\frac{x}{ge_K(L)},
\qquad
b=\frac{K}{ge_x(L)},
\tag{20}
\]

则 (3) 精确化为

\[
\boxed{
R e_K(L)a-e_x(L)b=\delta.
}
\tag{21}
\]

式 (16)--(21) 称为**分裂容量交换证书**。它是一个完全显式的短算术证书，但没有自动
给出目标平方除子、标记解集或良基下降。

## 4. 两个交叉表示之间的联合判据

对两个目标乘积 \(L_1,L_2\)，记 \(C_i=C(L_i)\)。由逐素数赋值还有两条精确判据：

\[
\boxed{
C_1>1\ \text{或}\ C_2>1
\iff
\operatorname{lcm}(L_1,L_2)
\nmid\operatorname{lcm}(K,x),
}
\tag{22}
\]

以及

\[
\boxed{
\exists q:q\mid C_1\ \text{且}\ q\mid C_2
\iff
(L_1,L_2)\nmid\operatorname{lcm}(K,x).
}
\tag{23}
\]

因此不能用乘积 \(L_1L_2\) 代替联合需求：同一素数在两个表示中的重复会被错误地重复
计价。判断“至少一边过载”应使用 lcm；判断“同一 \(q\) 同时服务两边”应使用 gcd。

## 5. 接回来源路径字

设首后继为

\[
U+V=Rm_0,
\tag{24}
\]

一条正规路径以路径字 \(\Theta\) 到达按祖先定向的底层终点

\[
X+Y=R,
\qquad
\Theta X=U+Ru,
\qquad
\Theta Y=V+Rv,
\tag{25}
\]

其中 \(u,v\ge0\)。定义

\[
d_U=(U,\Theta Y),
\qquad
d_V=(V,\Theta X),
\tag{26}
\]

以及两个交叉目标乘积

\[
L_U=\frac{U\Theta Y}{d_U^2},
\qquad
L_V=\frac{V\Theta X}{d_V^2}.
\tag{27}
\]

已有来源交叉表示定理说明：\(L_i\mid K\) 给出直接 Type I，\(L_i\mid x\) 给出 gap
\(R\) 的直接 Type II。因此，在这两个直接出口均已排除时，每个 \(L_i\) 都满足
(12)，从而**逐一**进入共同过载支或分裂交换支。

这比只记录四个非空缺陷向量更精确，但仍没有证明：

- 两个 \(L_i\) 必须落在同一支；
- 两个共同过载集合必有公共素数；
- 共同过载在不同状态间必重复；
- 分裂交换必产生内部终端或合法 E4。

## 6. 分裂交换不能直接终端化

### 6.1 最小核心上的环境形式边

取

\[
(p,R,K,x)=(73,23,420,24).
\]

环境形式边

\[
(1,45,2)\xrightarrow{q=3}(8,15,1)
\]

在空后缀下给出 \(L_U=L_V=120\)。此时

\[
g=12,
\qquad
e_K=2,
\qquad
e_x=5,
\qquad
C=1,
\]

所以它是严格分裂交换。这个状态不是 F 状态，因而只用于否定纯代数层面的“所有双 miss
都有共同 \(q\)”命题。

### 6.2 非空 formal 路径可使两边同时分裂

取

\[
(p,R,K,x)=(1297,47,15240,336),
\]

以及

\[
(U,V)=(12,35)
\xrightarrow{q=7}
(X,Y)=(42,5),
\qquad
\Theta=7.
\]

两个乘积为

\[
L_U=420,
\qquad
L_V=210,
\]

且两者都有

\[
e_K=7,
\qquad
e_x=5,
\qquad
C=1.
\]

所以“两个交叉表示不可能同时分裂”在一般 formal 路径上也为假；这个例子不满足更窄的
来源锚定 F 前提。

### 6.3 F 状态中的 split 可被 terminal-first 提前删除

冻结状态

\[
(p,R)=(68822329,14231)
\]

含有来源边

\[
(207,3870625,272)
\xrightarrow{q=5,\ g=55}
(156,14075,1).
\]

空后缀给出

\[
L_U=L_V=2195700,
\qquad
e_K=13,
\qquad
e_x=2815=5\cdot563,
\qquad
C=1.
\]

但同一状态已经在内部 gap \(191\) 有 Type I 证书。因此这个 split 不属于
internal-terminal-first 的剩余域。

### 6.4 单边 split 不强制内部终端

冻结来源锚定状态

\[
(p,R,K,x)=(122014489,471,14367206080,30503740)
\]

有路径

\[
(16,80525,171)
\xrightarrow{q=5,\ g=5}
(76,3221,7)
\xrightarrow{q=19}
(4,467,1).
\]

按 \(U=3221,V=76,X=467,Y=4,\Theta=19\) 定向，得到

\[
L_U=244796,
\qquad
(e_K(L_U),e_x(L_U))=(19,3221),
\qquad
C(L_U)=1,
\]

而

\[
L_V=1868,
\qquad
e_K(L_V)=e_x(L_V)=C(L_V)=467.
\]

该状态的七个合法内部 gap 全部 Type I/II miss，所以它精确否定

\[
\text{“任一交叉乘积 split”}
\Longrightarrow
\text{“同状态内部终端”}.
\]

不过完整冻结记录在可达 external gap \(35\) 有 Type I 证书。这个例子本身仍未排除
有界深度候选，但下面的 \(p=2017\) 反例会把该候选完整否定。

### 6.5 坐标差与共同载体也不自动出现

对

\[
(p,R)=(97,47),
\qquad
(X,Y)=(2,45),
\]

有 \(L=90\)、\(e_K=3\)、\(e_x=5\)，仍为分裂交换；但坐标差 \(43\) 的完整
Type I/II 平方除子谱为空。交换因子或坐标差都不是自动终端。

另一方面，在来源残余

\[
(p,R)=(37793809,12423)
\]

的一条路径中，两个共同过载因子分别为

\[
C(L_U)=1549,
\qquad
C(L_V)=6211,
\qquad
(1549,6211)=1.
\]

所以即使两个交叉表示都处于共同过载支，也不能假定存在同一个载体素数；(23) 是必须
实际检查的额外条件。

### 6.6 strict split 不强制同图表 external Reach 终端

取核心素数

\[
(p,R,K,x)=(2017,207,104380,556).
\tag{31}
\]

存在真正的 \(\Psi_0=1\) 来源边

\[
(1156,1535,13)
\xrightarrow{q=17,\ g=1}
(68,139,1).
\tag{32}
\]

这里 \(1535\mid K\)，且

\[
1156=17\cdot68,
\qquad
1535\cdot68=K,
\]

所以它具有规范的一层超额来源结构。空后缀 \(\Theta=1\) 的两个交叉乘积相同：

\[
L_U=L_V=68\cdot139=9452.
\tag{33}
\]

其联合容量数据为

\[
(e_K,e_x,C)=(139,17,1),
\tag{34}
\]

故这是 strict split。又有 \(g=(K,x)=4\)，以及精确交换式

\[
207\cdot139-17\cdot1535
=2678
=\frac{207^2-1}{4g}.
\tag{35}
\]

中心 \(K\) 盒为空，全部 \(K\)-内部合法 gap 只有 \(307,1535\)，两者的完整
Type I/II 平方除子谱都 miss。因此它在 \(R=207\) 的局部菜单中是 F 且
internal-free。这个限定不能改写成 terminal-first：原素数已有 ordinary gap \(15\)
的 Type I 和 Type II 证书。

从终点出发的完整 formal Reach 恰为

\[
(68,139)
\xrightarrow{139}(1,206)
\xrightarrow{103}(2,205)
\xrightarrow{41}(5,202)
\xrightarrow{101}(2,205).
\tag{36}
\]

即 4 个节点、4 条边。全图的 external gap 候选只有 \(139,103\)，两者也都完整
Type I/II miss。加入同一状态的第二个真实首后继 \((85,122,1)\) 后，状态级完整
post-first Reach 只有 5 个节点、5 条边，候选集合仍不变且全部 miss。

同一条路径在进入二循环前还经过 clean slab

\[
(1,206)=(1,103\cdot2),
\qquad 2\mid K,
\]

并满足

\[
R_{103}=115<207.
\tag{36a}
\]

所以现有 absorption 合同已经给出 E1--E5 verified rechart。循环节点的
\(101\)-slab 还满足 \(R_{101}=135<207\)，且新图表立即中心 Type I 命中。
这些事实不改变 external gap 集合的 miss，却说明本例不反驳 E4、absorption 或
terminal-or-descent。

特别地，交换余量 \(2678=2\cdot13\cdot103\) 的素因子 \(103\) 已在一步后作为
\(103\mid R-1\) 被显式暴露，仍不产生同图表 external 终端。因此以下窄命题为假：

\[
\text{strict split}
\Longrightarrow
\text{深度 }d\text{ 内有 external 终端}
\tag{37}
\]

对任意固定 \(d\)，甚至把右侧换成“完整 formal Reach 中有 external 终端”仍为假。
这里不能删除 external，也不能把右侧换成“直接终端或合法递降”。

### 6.7 一表示不变、另一表示仿射更新

上述反例的机制来自一条一般恒等式。设底层节点 \(X+Y=R\)，路径字为 \(\Theta\)，
且下一步选中 \(q\mid X\)。底层迁移无需额外正规约分，并且

\[
(X,Y,\Theta)
\longmapsto
\left(\frac Xq,R-\frac Xq,q\Theta\right).
\tag{38}
\]

若记

\[
S_X=\Theta X,
\qquad
S_Y=\Theta Y,
\]

则更新精确为

\[
\boxed{
(S_X,S_Y)
\longmapsto
\left(S_X,qS_Y+(q-1)S_X\right).
}
\tag{39}
\]

所以使用 \(S_X\) 的那一个交叉约分对完全不变，使用 \(S_Y\) 的另一个才作仿射更新；
选中 \(Y\) 时完全对称。由此，split 缺陷和交换恒等式可以沿 formal 边原封不动地保留，
它们本身不是下降量。

这关闭了“继续增加 depth 菜单”的方向。split 支若要进入递归证明，状态至少必须同时
记录两个交叉表示、split/common 分支和底层 SCC 信息，再证明新的容量下降或合法 E4；
不能再把 formal Reach 深度当作势函数。

## 7. 冻结 residual 的探索性剖面

对已有 70 条 `basic-local miss` 且完整 formal 后继图没有 good single slab 的冻结记录，
按词典序多源最短路径重建来源字后，得到以下只读探索性结果：

| 口径 | 记录 | 交叉乘积 | \(C(L)>1\) | 两边共享某个共同载体 |
|---|---:|---:|---:|---:|
| 全部 residual | 70 | 140 | 140 | 55 |
| 其中 `strong_miss` | 59 | 118 | 118 | 47 |
| 再排除同状态内部终端 | 34 | 68 | 68 | 27 |

最后一行只表示来源状态的 `internal.hit=false`，不是完整 terminal-first。其 181 个共同
过载素因子支持出现中，166 个完全位于 \(Kx\) 的支撑之外；slab 外素数在 34/34 条记录
中落入 \(C(L_U)\cup C(L_V)\)，而首缺陷素数只命中 2/34。59 个不同载体素数中只有
16 个跨状态复用；固定 \(q\le31\) 仍漏掉 24 个状态中的 3 个。

这些数字是研究方向证据，不参与本主张的一般证明。聚焦复现验证本节之前的代数恒等式、
七条代表路径和 \(p=2017\) 的 5 节点完整反例，没有重跑 1412 条 slab 的历史普查。

## 8. 当前推进意义

这个二分排除了一个错误希望：双容量 miss 不必产生共同素数，分裂交换也不自动产生
Type I/II、D-only 或 E4。它同时把下一步缩成两个具体任务：

1. 对共同过载支，将 \(C(L)\) 的外部 slab / suffix 载体映到不同状态间可比较的同余链，
   使用向量容量而不是假设两边共享单个 \(q\)；
2. 对分裂交换支，把两个交叉表示、split/common 分支和 bottom SCC 一起纳入状态，
   再证明新的容量下降，或把 \((e_K,e_x,\delta)\) 映入一个真正非空、可提升且良基
   下降的标记状态；不能继续假设有界 Reach 自动终端。

有限 residual 中每个交叉乘积都有共同过载，是强正信号，但在证明来源锚定全称命题前，
它只能作为待证明的候选规律，不能替代量词。

## 9. 复现

- 脚本：
  `reproductions/type_i_source_word_joint_capacity_dichotomy.py`
- 结果：
  `reproductions/type-i-source-word-joint-capacity-dichotomy-results.json`
- 输入：
  `reproductions/type-i-psi-one-full-spectrum-terminal-descent-audit-results.json`
- formal 边实现：
  `reproductions/type_i_f_psi_one_formal_transition_closure.py`

聚焦复现逐式检查 (3)、(5)--(10)、分裂支 (16)--(21)、七条 formal 路径、\(p=97\)
坐标差完整 miss、\(p=2017\) 的 complete-Reach split 反例，以及
\(p=68822329\)、\(p=122014489\) 的冻结终端边界。其语义是
`algebraic theorem plus focused analysis evidence`，不是 formal 边到合法递降边的升级。
