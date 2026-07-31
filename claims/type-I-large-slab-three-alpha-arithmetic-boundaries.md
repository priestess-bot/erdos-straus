---
kind: claim
claim_id: type-I-large-slab-three-alpha-arithmetic-boundaries
title: large-slab 三个内部系数的算术出口与提升边界
statement: 对核心线性图表 4K=pR+1 的初始 clean large-slab R=alpha Q+beta、K=alpha beta c、alpha属于{1,2,3}、Q=q^e、q不整除K，三个 alpha 分支可无样本地进一步压缩。alpha=1 时 beta(4c-p)=pQ+1，并有一个 gap 3 的 Type II 命中或规范容量超额二分；alpha=2 时 R_Q>R 等价于规范 tau 不超过 (4Q-R-1)/4，并使局部补量 4Q-R 严格减少 4tau，但该量尚不是状态势；alpha=3 时 R_Q>R 规范地产生 b'=beta+4delta<Q 与 n_*=(pb'+1)/Q<p，满足 n_*Q-pb'=1 及 p(Q-b')-Q(p-n_*)=1，但尚无从 n_* 到 p 的全域解提升。因此三分已经给出明确的下一接口，却没有闭合 overflow 或全称选择器。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-large-slab-factor-pair-layer-capacity
  - type-I-marked-support-accumulation-rechart-saturation
  - type-I-general-dyadic-terminal-transfer
  - type-I-generalized-dyadic-natural-lift-equivalence
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - large-slab
  - factor-pair
  - gap-3
  - capacity-overflow
  - generalized-dyadic
  - marked-lift
  - rechart
  - determinant
  - solution-lift
  - proof-boundary
sources:
  - claim: type-I-large-slab-factor-pair-layer-capacity
    role: three-alpha-factor-pair-normal-form
  - claim: type-I-marked-support-accumulation-rechart-saturation
    role: marked-descent-and-overflow-reclassification
  - claim: type-I-general-dyadic-terminal-transfer
    role: generalized-dyadic-arithmetic-candidate
  - claim: type-I-generalized-dyadic-natural-lift-equivalence
    role: natural-marker-emptiness-boundary
  - claim: denominator-escape-state-contract
    role: arithmetic-candidate-versus-verified-edge-boundary
visibility: public
last_checked: '2026-08-01'
---

# large-slab 三个内部系数的算术出口与提升边界

## 1. 共同设置

固定核心素数和初始线性图表

\[
p\equiv1\pmod {24},
\qquad
4K=pR+1,
\qquad
3\le R\le p-2.
\tag{1}
\]

设一条完整 clean large-slab 写成

\[
R=\alpha Q+\beta,
\qquad
K=\alpha\beta c,
\qquad
Q=q^e>\frac R4,
\qquad
q\nmid K,
\qquad
\alpha\in\{1,2,3\}.
\tag{2}
\]

这里 \(\beta>0\)、\((\alpha Q,\beta)=1\)。本卡研究旧分类中的上升分支
\(R_Q>R\)。按累积支撑定理，若 \(R_Q<p\)，它已经是合法 marked descent；只有
\(R_Q>p\) 才属于当前 overflow。不过，下列恒等式对两种上升情形都成立，因而可以作为
overflow 的进一步输入。

## 2. \(\alpha=1\)：双因子正规形与 gap 3 二分

写

\[
R=Q+\beta,
\qquad
K=\beta c,
\qquad
H=4c-p,
\qquad
d=H-c=3c-p,
\qquad
W=4Q-R=3Q-\beta.
\tag{3}
\]

将 (1)--(3) 展开，得到两个精确因子式

\[
\boxed{\beta H=pQ+1},
\qquad
\boxed{\beta d=\frac{pW+3}{4}}.
\tag{4}
\]

又因 \((c,p)=1\)，数 \(H,c,d\) 两两互素。因此尾因子可以从两个仿射量中无歧义恢复：

\[
\boxed{
\beta=
\gcd\left(pQ+1,\frac{pW+3}{4}\right).}
\tag{5}
\]

large-slab 条件 \(\beta<3Q\) 给出

\[
H>\frac p3,
\qquad
H\equiv3\pmod4,
\qquad
d\equiv2\pmod3.
\tag{6}
\]

并且有精确的 balanced/dominant 二分

\[
Q<\beta\Longleftrightarrow H<p,
\qquad
Q>\beta\Longleftrightarrow H>p.
\tag{7}
\]

等号因 \((Q,\beta)=1\) 且 \(Q>1\) 不可能。balanced 支的 \(H\) 是合法 gap，
其保留首分母 \(c=(p+H)/4\) 的完整因子谱就是

\[
u\mid c^2,\qquad
\begin{array}{c|c}
i&u\pmod H\\ \hline
0&-pc\\
1&-c\\
2&-p^{-1}c
\end{array}
\tag{8}
\]

其中完整因子为 \(p^iu\mid(pc)^2\)。任一命中都是 gap \(H\) 的直接 Type I/II
终端；全 miss 不是递降。

即使 (8) 失败，\(d\) 仍给出一个规范的 gap 3 二分。令

\[
x_3=\frac{p+3}{4},
\qquad
g=(d,x_3^2).
\tag{9}
\]

由 \(x_3\equiv1\pmod3\)、\(d\equiv2\pmod3\)，恰有

\[
\boxed{
g\equiv2\pmod3
\Longrightarrow
\min\left(g,\frac{x_3^2}{g}\right)
\text{ 是 gap }3\text{ 的 Type II 除子},}
\tag{10}
\]

或者

\[
\boxed{
e_3=\frac dg>1,
\qquad
e_3\equiv2\pmod3.}
\tag{11}
\]

在第二支，至少存在一个素数 \(\ell\equiv2\pmod3\) 满足

\[
v_\ell(d)>2v_\ell(x_3).
\tag{12}
\]

所以 \(\alpha=1\) 不只是“命中或 miss”：它给出直接 gap 3 终端，或一个规范的
gap3_capacity_overflow receipt。后者仍须注入其它状态的真实 \(\ell\)-进容量，不能
单独登记为 E4。

### 2.1 一个无限二进算术候选族及其提升缺口

令 \(k\in\mathbb Z_{\ge0}\)，并置

\[
u=101+132k,
\qquad
p=196u+5=19801+25872k
\tag{13}
\]

并只取其中为素数的项。因
\((19801,25872)=1\)，Dirichlet 定理保证这样的素数有无穷多个；它们都满足
\(p\equiv1\pmod {24}\)。取

\[
R=39,\qquad Q=11,\qquad\beta=28,\qquad
C=\frac{39u+1}{4},\qquad K=196C.
\tag{14}
\]

直接重算有

\[
4K=pR+1,\qquad 28\mid K,\qquad K\equiv10\pmod {11}.
\]

故 \((Q,\beta)=(11,28)\) 是一条 \(\alpha=1\) clean large-slab。对
\(L=2K\) 取广义二进数据

\[
(a,b,j)=(1,C,2).
\tag{15}
\]

由于 \(4C\equiv1\pmod {39}\)，有 \(a\equiv2^jb\pmod R\)，并且

\[
E=2^{1-j}L\frac ab=196,
\qquad
n=\frac{2L-E}{R}=196u=p-5.
\tag{16}
\]

所以 (13) 给出无穷多个严格更小偶数 \(n\) 的 generalized-dyadic arithmetic
candidate。但这还不是当前合同中的终端或 E4：自然标记分母为

\[
\eta=\frac{nK}{E}=uK,
\tag{17}
\]

而自然标记集非空当且仅当原 \((R,K)\) 中心 Type I 已经命中；标准偶数解
\((n/2,n,n)\) 也不含 \(\eta\)。例如

\[
(k,u,p,K)=(96,12773,2503513,24409252)
\tag{18}
\]

的中心状态是 F miss，因此 (17) 的自然标记集严格为空。故这个无限族否定了
“合法广义 \(2^2\) 算术数据自动给出可提升终端”，同时留下一个精确正向问题：为
(16) 构造不同于自然标记的非空源，或证明其它载体直接终端。

这里的 F 分类也可不用黑箱复核。式 (18) 中

\[
K=2^2\cdot7^3\cdot17791,
\qquad
17791\equiv7\pmod {39}.
\]

所以有限盒中的有效指数满足
\(i\in[-2,2]\)、\(j\in[-4,4]\)，目标方程为
\(2^i7^j\equiv-1\pmod {39}\)。关系

\[
7^2\equiv2^{10},
\qquad
7^5\equiv-2
\pmod {39}
\]

表明目标在无限生成群中可达，例如 \((i,j)=(-1,5)\)。但盒内 \(j\) 必为奇数；对
\(j=-3,-1,1,3\)，所需 \(i\pmod {12}\) 依次为 \(3,5,7,9\)，均不在
\([-2,2]\)。因此它确为 F，而不是 G 或 hit。

## 3. \(\alpha=2\)：规范图表步严格减少局部补量

写

\[
R=2Q+\beta,
\qquad
K=2\beta c,
\qquad
d=2Q-\beta=4Q-R.
\tag{19}
\]

由 (1) 得

\[
\boxed{\beta(8c-p)=2pQ+1},
\qquad
R\equiv7\pmod8,
\qquad
d\equiv5\pmod8.
\tag{20}
\]

特别地 \(d=4h+1\) 且 \(h\) 为正奇数；边界 \(\beta=2Q-1\) 因会给出 \(d=1\)
而不可能。

令唯一的 \(1\le\tau<Q\) 满足

\[
K+p\tau\equiv0\pmod Q.
\tag{21}
\]

规范图表代表精确为

\[
R_Q=
\begin{cases}
R+4\tau,&\tau\le h,\\
R+4\tau-4Q,&\tau\ge h+1.
\end{cases}
\tag{22}
\]

因此

\[
\boxed{R_Q>R\Longleftrightarrow\tau\le h.}
\tag{23}
\]

在该支，新图表相对于 \(4Q\) 的补量为

\[
4Q-R_Q=d-4\tau<d.
\tag{24}
\]

式 (24) 是真正的严格整数下降，但目前只在固定 \(Q\) 的算术图表内定义。换载体后
\(d\) 可以重置，而且当 \(R_Q>p\) 时该图表不是合法后继。因此 (24) 只能登记为
local_complement_drop，不能替代状态合同的 E4、E5。

## 4. \(\alpha=3\)：行列式为一的较小秩候选

写

\[
R=3Q+\beta,
\qquad
K=3\beta c.
\tag{25}
\]

large-slab 条件给出 \(0<\beta<Q\)，并且

\[
\boxed{\beta(12c-p)=3pQ+1.}
\tag{26}
\]

所以自然尾缺口 \(12c-p>3p\)，永远不是合法短 gap。

令

\[
p\rho\equiv K\pmod Q,
\qquad
1\le\rho<Q,
\qquad
\delta=Q-\rho.
\tag{27}
\]

若 \(R_Q>R\)，规范代表必须满足

\[
R_Q=R+4\delta,
\qquad
0<4\delta<Q-\beta.
\tag{28}
\]

置

\[
\beta'=\beta+4\delta,
\qquad
n_*=\frac{p\beta'+1}{Q}.
\tag{29}
\]

式 (27) 与 \(4K\equiv p\beta+1\pmod Q\) 给出 \(Q\mid p\beta'+1\)；由
\(0<\beta'<Q\) 又有 \(0<n_*<p\)。更精确地，

\[
\boxed{n_*Q-p\beta'=1},
\qquad
\boxed{p(Q-\beta')-Q(p-n_*)=1.}
\tag{30}
\]

这是一对互补的 Farey 邻接行列式，也是 \(\alpha=3\) 最自然的严格较小 equation-rank
候选。但 (30) 只给出算术邻接；目前没有定义一个非空标记集
\(W(p,n_*,\ldots)\)，也没有 \(W_{n_*}\to\operatorname{Sol}(p)\) 的全域提升。因此
\(n_*<p\) 不能写成已经证明的递降边。

## 5. 对下一阶段的约束

三个分支现在给出不同而明确的接口：

1. \(\alpha=1\)：证明 (11)--(12) 的容量超额必被另一图表吸收，或为 (16) 构造不同于
   自然好尾的可提升标记源；
2. \(\alpha=2\)：把局部补量下降 (24) 嵌入不会因换 \(Q\) 重置的全局势，或在 overflow
   前直接产生终端；
3. \(\alpha=3\)：为 determinant pair (30) 构造规范标记纤维和全域解提升，或证明失败
   强制某个外层 gap 命中。

这些结论排除了把模 \(3\)、模 \(8\) 或单个 endpoint gap 当成自动闭合机制。它们也
没有证明 overflow 必停；在进入本卡之前仍应先应用累积支撑分流
\(R_{AQ}<p\) 的 marked descent 与 \(R_{AQ}>p\) 的 overflow。
