---
kind: claim
claim_id: type-I-large-slab-factor-pair-layer-capacity
title: large-slab 的受限因子对正规形与跨指数层支撑容量
statement: 对 m=1 单外部 large-slab X=q^e alpha、Y=beta、K=alpha beta c，其中 alpha属于{1,2,3}且q不整除alpha，令 N_{alpha,e}=alpha p q^e+1、H=4 alpha c-p，则 beta H=N_{alpha,e}；反之，满足 H=N/beta、H同余-p模4alpha、q不整除(H+p)/(4alpha)及 beta<(4-alpha)q^e 的每个除子 beta，都唯一恢复一个算术 large-slab。对 f>=e 还有精确公式 gcd(N_{alpha,e},N_{alpha',f})=gcd(N_{alpha,e},alpha' q^{f-e}-alpha)，故固定 alpha 的尾素数只出现在一个指数剩余类中。对来源路径字的两个交叉乘积，slab 素数进入共同过载因子的指数又由 v_q(Theta)、v_q(V)、e、v_q(x_R) 精确决定。这给出无扫描上界的因子层和路径层容量接口，但不自动产生 Type I/II 或合法 E4。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-formal-linear-chart-p-transience-large-slab-anchor
  - type-I-psi-one-source-word-large-slab-constraint
  - type-I-source-word-joint-capacity-common-split-dichotomy
topics:
  - type-I
  - formal-target-pair
  - external-slab
  - large-slab
  - factor-pair
  - cross-state
  - q-adic-capacity
  - divisor-capacity
  - proof-boundary
sources:
  - claim: type-I-formal-linear-chart-p-transience-large-slab-anchor
    role: large-slab-three-anchor-reduction
  - claim: type-I-psi-one-source-word-large-slab-constraint
    role: source-word-slab-arithmetic-identity
  - claim: type-I-source-word-joint-capacity-common-split-dichotomy
    role: cross-product-common-overload-factor
visibility: public
last_checked: '2026-08-01'
---

# large-slab 的受限因子对正规形与跨指数层支撑容量

## 1. 精确因子对正规形

固定奇数 \(p\)、素数 \(q\) 和 \(e\ge1\)，记

\[
Q=q^e.
\tag{1}
\]

考虑一个 \(m=1\) 单外部 large-slab

\[
X=Q\alpha,
\qquad
Y=\beta,
\qquad
X+Y=R,
\tag{2}
\]

满足

\[
(X,Y)=1,
\qquad
K=\alpha\beta c,
\qquad
q\nmid K,
\qquad
4K=pR+1,
\qquad
Q>\frac R4.
\tag{3}
\]

已有三锚点压缩给出

\[
\alpha\in\{1,2,3\}.
\tag{4}
\]

定义

\[
N_{\alpha,e}=\alpha p q^e+1,
\qquad
H=4\alpha c-p.
\tag{5}
\]

将 \(R=\alpha q^e+\beta\) 代入 \(4\alpha\beta c=pR+1\)，得到

\[
\boxed{\beta H=N_{\alpha,e}.}
\tag{6}
\]

这不只是必要整除条件，而是一个双向参数化。固定 \(p,q,e,\alpha\)，并假设
\(q\nmid\alpha\)。对任意正除子

\[
\beta\mid N_{\alpha,e},
\qquad
H=\frac{N_{\alpha,e}}\beta,
\tag{7}
\]

若满足

\[
H\equiv-p\pmod {4\alpha},
\qquad
q\nmid\frac{H+p}{4\alpha},
\qquad
\beta<(4-\alpha)q^e,
\tag{8}
\]

则令

\[
c=\frac{H+p}{4\alpha},
\qquad
R=\alpha q^e+\beta,
\qquad
K=\alpha\beta c
\tag{9}
\]

便唯一恢复一个满足 (2)--(3) 的算术 large-slab。

事实上，\(N_{\alpha,e}\equiv1\pmod {q\alpha}\)，所以

\[
(q\alpha,\beta H)=1.
\tag{10}
\]

这自动给出 \((q^e\alpha,\beta)=1\)；(8) 的第二项再给出 \(q\nmid c\)，故
\(q\nmid K\)。同时

\[
4K=\beta(H+p)=\alpha p q^e+p\beta+1=pR+1.
\tag{11}
\]

最后，(8) 的严格大小条件等价于

\[
4q^e>\alpha q^e+\beta=R.
\tag{12}
\]

所以正向构造和反向恢复互为逆映射。这里的“算术 slab”只断言 (2)--(3)；是否来自
某个指定线性源的 formal Reach，仍是额外限制。

## 2. 三分支的大小刚性

由 (6) 和 (12)，

\[
\boxed{
\beta<(4-\alpha)q^e,
\qquad
H>\frac{\alpha p}{4-\alpha}.
}
\tag{13}
\]

三个分支分别为

| \(\alpha\) | 小因子范围 | 互补因子范围 |
|---:|---:|---:|
| 1 | \(\beta<3q^e\) | \(H>p/3\) |
| 2 | \(\beta<2q^e\) | \(H>p\) |
| 3 | \(\beta<q^e\) | \(H>3p\) |

因此报告中提出的 \(\alpha=1,2,3\) 分类可以精确改写为三个受限因子对问题，而不是
无界搜索 \(R,K\)。特别是 \(\alpha=3\) 支的互补因子必严格大于 \(3p\)。

## 3. 固定参数的精确除子容量

对整数区间 \(I\)，定义 admissible divisor set

\[
\begin{aligned}
\mathcal D_{p,q,\alpha,e}(I)=\{\,\beta>0:\;&
\beta\mid N_{\alpha,e},\quad H=N_{\alpha,e}/\beta,\\
&H\equiv-p\pmod {4\alpha},\quad
q\nmid(H+p)/(4\alpha),\\
&\beta<(4-\alpha)q^e,\quad
\alpha q^e+\beta\in I\,\}.
\end{aligned}
\tag{14}
\]

在 \(q\nmid\alpha\) 下，固定 \((p,q,\alpha,e)\)、且 \(R\in I\) 的全部算术
large-slab 与 \(\mathcal D_{p,q,\alpha,e}(I)\) 双射。因此它们的数目精确为

\[
\boxed{\#\mathcal D_{p,q,\alpha,e}(I).}
\tag{15}
\]

若只考虑真正线性图表的必要区间 \(3\le R\le p-2\)，则固定 \((p,q)\) 的全部可达
large-slab 数目至多为

\[
\boxed{
\sum_{\substack{\alpha\in\{1,2,3\}\\q\nmid\alpha}}
\ \sum_{\substack{e\ge1\\\alpha q^e<p-2}}
\#\mathcal D_{p,q,\alpha,e}([3,p-2]).
}
\tag{16}
\]

若按外部高度收费，总高度相应至多为把 (16) 中每项乘以 \(e\) 后的和。这个上界不含
素数扫描截断；实际 source/reach 条件只会继续删除 (14) 中的候选。

## 4. 不同 \((\alpha,e)\) 层的精确 gcd

现在固定 \(p,q\)，但允许 \(\alpha,e\) 改变。若 \(f\ge e\)，则

\[
\boxed{
\gcd(N_{\alpha,e},N_{\alpha',f})
=
\gcd\left(N_{\alpha,e},\alpha' q^{f-e}-\alpha\right).
}
\tag{17}
\]

证明只用恒等式

\[
\alpha N_{\alpha',f}
-\alpha'q^{f-e}N_{\alpha,e}
=\alpha-\alpha'q^{f-e}.
\tag{18}
\]

左侧两个 \(N\) 的公因子显然整除右侧。反过来，若

\[
d\mid N_{\alpha,e},
\qquad
d\mid\alpha'q^{f-e}-\alpha,
\]

则 (18) 给出 \(d\mid\alpha N_{\alpha',f}\)。又因
\((N_{\alpha,e},\alpha)=1\)，所以 \((d,\alpha)=1\)，从而
\(d\mid N_{\alpha',f}\)。这证明 (17)。

逐素数地，任意素数 \(\ell\) 都满足

\[
\min\{v_\ell(N_{\alpha,e}),v_\ell(N_{\alpha',f})\}
\le
v_\ell(\alpha'q^{f-e}-\alpha).
\tag{19}
\]

同一结论自动传给任意尾因子 \(T\mid N_{\alpha,e}\)、
\(T'\mid N_{\alpha',f}\)。因此不论某个素因子被分配给 \(\beta\) 还是 \(H\)，它在
两层间的最大共同可复用指数都由 (19) 的小差值支付。

## 5. 固定 \(\alpha\) 的周期容量

取 \(\alpha'=\alpha\)。因 \((N_{\alpha,e},\alpha)=1\)，(17) 化为精确公式

\[
\boxed{
\gcd(N_{\alpha,e},N_{\alpha,f})
=\gcd(N_{\alpha,e},q^{f-e}-1).
}
\tag{20}
\]

更一般地，设 \(E\) 是至少含两个指数的有限集合，\(e_0=\min E\)，并令

\[
d_E=\gcd\{e-e_0:e\in E,\ e>e_0\}.
\tag{21}
\]

利用 \(\gcd(q^a-1,q^b-1)=q^{\gcd(a,b)}-1\)，得到

\[
\boxed{
\gcd_{e\in E}N_{\alpha,e}
=\gcd(N_{\alpha,e_0},q^{d_E}-1).
}
\tag{22}
\]

特别地，若素数 \(\ell\) 在某一层 \(e_0\) 满足
\(\ell\mid N_{\alpha,e_0}\)，则 \(\ell\nmid q\)，而且

\[
\boxed{
\ell\mid N_{\alpha,e}
\iff
e\equiv e_0\pmod {\operatorname{ord}_\ell(q)}.
}
\tag{23}
\]

所以在任意整数指数区间 \([E_0,E_1]\) 内，同一尾素数至多出现

\[
\boxed{
\left\lfloor
\frac{E_1-E_0}{\operatorname{ord}_\ell(q)}
\right\rfloor+1
}
\tag{24}
\]

次。这是一个真正的跨层支撑容量：高阶素数不能在相邻指数层任意重复，出现位置被限制
在唯一的乘法阶剩余类中。

## 6. 同一指数的 admissible 分支几乎正交

令 \(f=e\)。式 (17) 给出

\[
\gcd(N_{\alpha,e},N_{\alpha',e})
=\gcd(N_{\alpha,e},\alpha'-\alpha).
\tag{25}
\]

对 \(\alpha,\alpha'\in\{1,2,3\}\)：

- \(|\alpha'-\alpha|=1\) 时，两层互素；
- \(\{\alpha,\alpha'\}=\{1,3\}\) 时，公因子至多为 \(2\)；
- 若 \(q\) 为奇数，则后一公因子精确为 \(2\)；
- 若 \(q=2\)，则两个 \(N\) 都为奇数，后一公因子也是 \(1\)。

因此同一 \((p,q,e)\) 下，所有 admissible \(\alpha\) 分支不可能共享任何奇尾素数。
奇 \(q\) 时 \(\alpha=1,3\) 之间唯一的公共载体只是普适奇偶因子 \(2\)；还要保留
\(q\nmid\alpha\) 对可用分支的删除。

## 7. 来源交叉表示中的 slab-\(q\) 精确载体判据

因子对容量控制 \(\beta,H\) 的支撑复用；还需要判断 external slab 素数 \(q\) 本身
何时进入来源交叉表示的共同过载因子。设首后继按内部坐标定向为

\[
U+V=Rm_0,
\qquad
U\mid K,
\tag{26}
\]

并由路径字 \(\Theta\) 到达按祖先定向的底层节点

\[
X_U+X_V=R.
\tag{27}
\]

设其中一个终点坐标含有唯一外部幂 \(q^e\)，另一个不含 \(q\)，并记

\[
a=v_q(\Theta),
\qquad
b=v_q(V),
\qquad
s=v_q(x_R),
\qquad
x_R=\frac{p+R}{4},
\tag{28}
\]

\[
e_U=v_q(X_U),
\qquad
e_V=v_q(X_V),
\qquad
\{e_U,e_V\}=\{e,0\}.
\tag{29}
\]

两个来源交叉乘积为

\[
L_U=\frac{U\Theta X_V}{(U,\Theta X_V)^2},
\qquad
L_V=\frac{V\Theta X_U}{(V,\Theta X_U)^2}.
\tag{30}
\]

因为 \(q\nmid K\) 且 \(U\mid K\)，有 \(q\nmid U\)，于是

\[
v_q(L_U)=a+e_V,
\qquad
v_q(L_V)=|b-a-e_U|.
\tag{31}
\]

令

\[
C(L)=\frac{L}{(L,\operatorname{lcm}(K,x_R))}
\tag{32}
\]

为联合容量的共同过载因子。由于 \(v_q(K)=0\)，(31) 精确给出

\[
\boxed{
v_q(C(L_U))=(a+e_V-s)_+,
\qquad
v_q(C(L_V))=(|b-a-e_U|-s)_+.
}
\tag{33}
\]

这里 \((t)_+=\max(t,0)\)。证明只需注意
\(v_q(U,\Theta X_V)=0\)，而

\[
v_q(V,\Theta X_U)=\min\{b,a+e_U\}.
\]

所以 (31) 的第二式是
\(b+a+e_U-2\min\{b,a+e_U\}=|b-a-e_U|\)。

式 (33) 立即给出两个完整的 miss 条件：

- 外部坐标是 \(U\) 的后代，即 \((e_U,e_V)=(e,0)\) 时，
  \[
  q\nmid C(L_U)C(L_V)
  \iff
  a\le s\ \text{且}\ |b-a-e|\le s;
  \tag{34}
  \]
- 外部坐标是 \(V\) 的后代，即 \((e_U,e_V)=(0,e)\) 时，
  \[
  q\nmid C(L_U)C(L_V)
  \iff
  a+e\le s\ \text{且}\ |b-a|\le s.
  \tag{35}
  \]

因此“slab \(q\) 是共同载体”不再只是有限样本字段，而是一个精确赋值判据。尤其
\(a>s\) 时无论后代方向如何都有 \(q\mid C(L_U)\)；但 (34)--(35) 也保留了明确的
逃逸窗口，所以不能把 residual 中的正信号直接升级为全称命题。

### 7.1 非继承出生支的刚化

若

\[
b=v_q(V)=0,
\tag{36}
\]

则两个 ancestry 方向的最大需求都精确等于 \(a+e\)，因而

\[
\boxed{
q\mid C(L_U)C(L_V)
\iff
a+e>s.
}
\tag{37}
\]

所以这一支若 miss，必有

\[
q^{a+e}\mid x_R,
\qquad
Q=q^e\mid x_R.
\tag{38}
\]

在真正线性图表中 \(Q<R<p\)，故 \(q\ne p\)。又因 \(q\nmid R\) 且 \(R\) 为奇数，
\(p,R\) 在模 \(4Q\) 下都可逆。由 \(4x_R=p+R\) 及规范吸收图表

\[
pR_Q\equiv-1\pmod {4Q}
\tag{39}
\]

进一步得到

\[
p\equiv-R\pmod {4Q},
\qquad
\boxed{R_Q\equiv R^{-1}\pmod {4Q}.}
\tag{40}
\]

若规范代表 \(R_Q<R\)，这就进入已有 ABSORB 候选；但下降不是纯同余自动结果。例如

\[
(p,R,Q,\alpha,\beta)=(409,47,19,2,9)
\tag{41}
\]

满足 \(Q\mid x_R\)，却有 \(R_Q=55>47\)。

二进支还会完全刚化。若 \(q=2\)，由 \(K\) 奇、\(p\equiv1\pmod8\) 得
\(R\equiv3\pmod8\)，故 \(s=v_2(x_R)=0\)。于是 (34)--(35) 的 miss 精确等价于

\[
X_U\text{ 是外部坐标},
\qquad
a=0,
\qquad
b=e.
\tag{42}
\]

也就是说，二进 external carrier 只有在“路径字不含 2、\(V\) 含恰好 \(2^e\)，且
endpoint 外部幂位于 \(U\)-ancestry”这一交叉匹配中，才能同时避开两个共同过载因子。

### 7.2 source-anchored 反例与 shortest-carrier 候选的否定

slab \(q\) 的 union 命中即使在来源锚定 F 状态中也不是无条件全称。一条冻结来源锚定
反例为

\[
(p,R,K,x_R)=(10170169,127,322902866,2542574),
\tag{43}
\]

其首后继与底层 ancestry 数据为

\[
U=1,
\quad V=5079,
\quad\Theta=210,
\quad X_U=101,
\quad X_V=26.
\tag{44}
\]

这里 \(q=101,e=1\)，并且

\[
(a,b,s,e_U,e_V)=(0,0,1,1,0).
\tag{45}
\]

两个交叉乘积满足

\[
L_U=5460,
\quad C(L_U)=210,
\qquad
L_V=11969510,
\quad C(L_V)=59255,
\tag{46}
\]

所以 \(101\nmid C(L_U)C(L_V)\)。这正是 (37) 的边界等号
\(a+e=s=1\)，不是公式失败。该记录也不是 strong miss：锚点 gap \(63\) 已有 Type I，
且 \(R_{101}=35<R\)。

事实上，加入 strong miss 甚至 linear-source 都不能救回最短路径候选。先记录一个精确的
零距离引理：若 post-first anchor 本身就是

\[
U=\beta,
\qquad
V=Q\alpha,
\qquad
Q=q^e
\]

的 single-external slab，则唯一空后缀满足

\[
\boxed{
L_U=L_V=Q\alpha\beta,
\qquad
v_qC(L_U)=v_qC(L_V)=\bigl(e-v_q(x_R)\bigr)_+.
}
\tag{47}
\]

这是因为 \((Q\alpha,\beta)=1\)、\(q\nmid K\)，且空路有 \(\Theta=1\)，直接代入
(29)--(32) 即得。

现在取

\[
(p,R,K,x_R)=(57073,23,328170,14274).
\tag{48}
\]

它有线性源

\[
(a_0,s_0)=(2378,1),
\qquad
p=a_0+s_0+a_0s_0R,
\qquad
(a_0R+1)(s_0R+1)=4K.
\tag{49}
\]

中心平方除子盒含 81 点且零命中。一条真实首边为

\[
(20,3,1)\xrightarrow{q_*=2,\ g=1}(10,13,1),
\tag{50}
\]

而首后继自身就是

\[
(Q,\alpha,\beta)=(13,1,10)
\tag{51}
\]

的 strong large-slab miss：direct/cross 命中集、节点/锚点 external-affine 命中集均空，
且 \(R_{13}=43>23\)。由 (47)，唯一最短后缀给出

\[
L_U=L_V=130,
\qquad
C(L_U)=C(L_V)=1,
\tag{52}
\]

因为 \(v_{13}(x_R)=1\)。所以旧候选

\[
\text{strong miss}
\Longrightarrow
\exists w\in\mathcal W_{\min}(S):
q\mid C(L_U(w))C(L_V(w))
\]

为假，即使补上 linear-source 也仍为假。该例已有内部 gap \(15\) 的 Type I，完整 Reach
也有 external gap \(7\) 的 Type I，因此它不否定再附加 terminal-first unresolved 的
更窄量词；但目前没有理由把该窄量词提升为新候选。正确的选择不变量应是固定支撑上的
完整 Pareto 容量前沿，并在 bottom SCC 内使用周期射线的命中或静态/区间 miss 证书，
而不是任意最短图路径。

## 8. 与统一选择器的接口及边界

本定理完成了报告所要求的 large-slab 三分参数压缩中的一个算术层：

1. 每个候选由 \(N_{\alpha,e}\) 的一个受限因子对唯一编码；
2. 固定外部 \(q\) 的高度层数和候选数有精确有限容量；
3. 尾素数跨层复用由 (17)、(22)、(24) 控制；
4. 同一指数的所有 admissible \(\alpha\) 分支在奇支撑上完全分离；
5. slab 素数进入来源共同过载因子的条件由 (33)--(35) 精确判定。

它仍没有证明以下任何一项：

- admissible divisor 必给出 Type I/II；
- 一个算术 slab 必在指定源的 formal Reach 中出现；
- external slab 素数 \(q\) 对每条来源路径都必是共同过载素数；
- 因子对 miss 必产生非空 D-only 状态或满足 E1--E4 的合法递降。

此外，“strong miss 必存在最短来源路径字使 slab \(q\) 进入共同过载”不是尚待证明的
开放项，而是已由 (48)--(52) 否定。

所以 (14)--(47) 是后续 slab/suffix 向量容量的严格输入，不是 large-slab 三分逃逸定理
本身。下一步应把完整路径 Pareto 前沿的共同过载因子映入这些 \(N_{\alpha,e}\) 尾坐标，
或从不满足该映射的 split/SCC miss 支构造改变根尾数据的合法后继。完整路径的有限性与
周期证书见[底层路径字的格正规形、有限 Pareto 前沿与周期容量选择器](type-I-bottom-word-lattice-pareto-cycle-capacity-selector.md)。

## 9. 聚焦复现

~~~bash
python3 reproductions/type_i_large_slab_factor_pair_layer_capacity.py
python3 reproductions/type_i_large_slab_factor_pair_layer_capacity.py --verify
~~~

结果文件：

~~~text
reproductions/type-i-large-slab-factor-pair-layer-capacity-results.json
~~~
