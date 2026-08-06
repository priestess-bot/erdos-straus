---
kind: claim
claim_id: type-I-g-anchor-c3-two-intermediate-target-source-template
title: c=3 补余 seed 的双中间节点 target-source raw 模板
statement: 在 c=3 补余 target chart 中，若存在两个中间节点参数 a,b，使 R-1=b alpha、R-b=a beta、R-a=8 gamma，且 alpha、beta、gamma 为素数并满足一组逐边可检验的充分单位与容量排除条件，则 target universal p-source 有一条实际 m=1 raw 路径经 N_R(b)、N_R(a)、N_R(4) 和 t=4 节点 N_R(4x) 到达 complement seed N_R(x)。该路径的 anchor-to-N_R(4) 相位 P=2 alpha beta gamma 满足 4P=-1 (mod R)，而到 t=4 节点的相位 W=13P=-M (mod R)，完整词为 -13 (mod R)。固定 a,b 时，三个整除和所选 prime-label 专门化中的奇偶要求化为带 gcd 可解性门的 CRT 系统，从而产生可枚举的 affine-prime 条件族。文中给出三个新族和覆盖 c=3 全部四个允许 h (mod 6) 类的四个控制点；这些只给出条件性 fresh target-source raw provenance，不构成 verified_edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-complement-seed-m1-interface-rigidity
  - type-I-g-anchor-even-tail-complement-source-switch
  - type-I-g-anchor-c3-affine-prime-target-source-template
  - type-I-g-anchor-full-q-complement-r11-reset-boundary
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-overflow-cofactor-r-chart-support
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - complement-torsor
  - c3
  - target-source
  - raw-path
  - affine-prime
  - CRT
  - phase
  - even-tail
  - proof-boundary
sources:
  - claim: type-I-g-anchor-complement-seed-m1-interface-rigidity
    role: endpoint-phase-gate-and-exact-even-tail
  - claim: type-I-g-anchor-even-tail-complement-source-switch
    role: c3-complement-seed-and-even-side-encoding
  - claim: type-I-g-anchor-c3-affine-prime-target-source-template
    role: original-a7-b2-specialization
  - claim: type-I-g-anchor-marked-raw-peeling-calculus
    role: raw-transition-semantics
  - claim: type-I-overflow-cofactor-r-chart-support
    role: high-R-universal-p-source-lemma
  - concept: denominator-escape-state-contract
    role: E1-E5-admission-boundary
visibility: public
last_checked: '2026-08-06'
---

# \(c=3\) 补余 seed 的双中间节点 target-source raw 模板

## 1. 固定 target chart 与目标

令

\[
h\ge3,
\qquad
p=24h+1\ \text{为素数},
\qquad
h\not\equiv2\pmod3,
\qquad
h\not\equiv12\pmod{13}.
\tag{1}
\]

这是 full-\(Q\) 补余构造的 \(c=3\) 分支。写

\[
R=104h-9,
\qquad
M=26h+1,
\qquad
x=24h-2,
\qquad
K=Mx.
\tag{2}
\]

则

\[
4K=pR+1,
\qquad
R=4M-13,
\qquad
13x=3R+1.
\tag{3}
\]

补余 seed 是 \(N_R(x)=\{x,R-x\}\)。它的偶侧编码为 \(t=1\)，而

\[
N_R(4x)=\{4x,R-4x\}=\{4x,8h-1\}
\tag{4}
\]

是相同 physical 行的精确 \(t=4\) even-tail 节点。

本卡给出 target 图表自身的 raw source path。它不是 old G 图表的 transport，也不把
even-tail projection 伪称为既有 marked edge。

## 2. 双中间节点充分条件

取正整数 \(a,b\)，并定义

\[
\alpha=\frac{R-1}{b},
\qquad
\beta=\frac{R-b}{a},
\qquad
\gamma=\frac{R-a}{8}.
\tag{5}
\]

假设

\[
(a,b)=1,
\qquad
a\equiv7\pmod8,
\tag{6}
\]

且 (5) 中三个数都是素数，并满足下面一组逐边充分排除条件：

\[
\alpha\nmid14,
\qquad
\beta\nmid b(b+13)(3b+1),
\qquad
\gamma\nmid a(a+13)(3a+1).
\tag{7}
\]

原先使用的数值界只是容易检查的充分条件：

\[
\alpha>14,
\qquad
\beta>\max\{b+13,3b+1\},
\qquad
\gamma>\max\{a+13,3a+1\}
\Longrightarrow\text{(7)}.
\tag{7a}
\]

这里 (5) 的整数性就是三条因子等式

\[
R-1=b\alpha,
\qquad
R-b=a\beta,
\qquad
R-a=8\gamma.
\tag{8}
\]

**定理（双中间节点 raw 路径）。** 在 (1)--(8) 下，target universal source

\[
\mathsf S_T=
\bigl(p,R(p-1)-p,p-1\bigr)
\tag{9}
\]

有一条实际 \(m=1\) raw 路径

\[
\begin{aligned}
\mathsf S_T
&\xrightarrow{p}N_R(1)
\xrightarrow{\alpha}N_R(b)
\xrightarrow{\beta}N_R(a)
\xrightarrow{2}N_R(4\gamma)\\
&\xrightarrow{\gamma}N_R(4)
\xrightarrow{13}N_R(8h-1)=N_R(4x)
\xrightarrow{2}N_R(2x)
\xrightarrow{2}N_R(x).
\end{aligned}
\tag{10}
\]

特别地，(10) 给出 complement seed 的条件性 fresh target-source raw provenance。

### 2.1 逐步坐标公式

从 \(N_R(1)\) 开始，依次选择补余坐标，可把 (10) 写成有序形式

\[
\begin{aligned}
(R-1,1,1)
&\xrightarrow{\alpha}(b,R-b,1)\\
&\xrightarrow{\beta}(a,R-a,1)\\
&\xrightarrow{2}(4\gamma,R-4\gamma,1)\\
&\xrightarrow{\gamma}(4,R-4,1)\\
&\xrightarrow{13}(8h-1,4x,1)\\
&\xrightarrow{2}(2x,R-2x,1)
\xrightarrow{2}(x,R-x,1).
\end{aligned}
\tag{11}
\]

例如第一步使用 \(R-1=b\alpha\)。在 \(m=1\) 层，shift 为
\(\alpha-1\)，所以另一个输出坐标正好是 \(R-b\)。其余各步同理；
\((a,b)=1\) 确保 \(N_R(a)\) primitive，因为 \((a,R)=(a,b)=1\)。

## 3. 容量、单位与 primitive 检查

先看 source 的 \(p\)-边。由

\[
M=p+2h,
\qquad
x=p-3,
\qquad
R-4p=8h-13,
\tag{12}
\]

因为 \(p<M<2p\) 且 \(x=p-3\)，可知 \(p\nmid K\)。又对 \(h\ge3\) 有
\(0<8h-13<p\)，从而 \(p\nmid R\)。再由

\[
R(p-1)-p\equiv-R\not\equiv0\pmod p
\tag{12a}
\]

可知 source 是 primitive，且 \(p\) 与 \(R\)、\(p-1\) 及另一 source 坐标都互素；
这正是首条 raw 边的 unit 条件。故 \(p\) 是 source 第一坐标的有效外部超容量素数；
其 shift 为 \(1\)，无 gcd 约分，并给出 (10) 的首边。

对三个随 \(h\) 变化的标签，(3) 和 (8) 给出

\[
\begin{array}{c|cc}
q & \text{若 }q\mid M\text{ 所迫使的常数} &
    \text{若 }q\mid x\text{ 所迫使的常数}\\ \hline
\alpha & 14 & 4\\
\beta & b+13 & 3b+1\\
\gamma & a+13 & 3a+1
\end{array}
\tag{13}
\]

具体地，三行分别来自

\[
\begin{aligned}
b\alpha&=4M-14, & 13x&=3b\alpha+4,\\
a\beta&=4M-13-b, & 13x&=3a\beta+3b+1,\\
8\gamma&=4M-13-a, & 13x&=24\gamma+3a+1.
\end{aligned}
\tag{14}
\]

因此 (7) 蕴含

\[
\alpha\nmid K,
\qquad
\beta\nmid K,
\qquad
\gamma\nmid K.
\tag{15}
\]

又 \(b\mid R-1\) 给出 \((b,R)=1\)，而 \(a\mid R-b\) 与 \((a,b)=1\)
给出 \((a,R)=1\)。式 (7) 还分别排除了 \(\beta\mid b\) 与
\(\gamma\mid a\)。故每个奇标签都与相应的另一坐标、层数和 \(R\) 互素；
这给出所有奇素数边的 unit 条件。

又 \(M\) 为奇数、\(x=2(12h-1)\)，所以

\[
v_2(K)=1.
\tag{16}
\]

因为 \(a\equiv7\pmod8\) 且 \(R\equiv7\pmod8\)，有 \(R-a=8\gamma\)。
故第一条 \(2\)-边的所选坐标有二进高度至少 \(3\)；末端两条 \(2\)-边分别在
\(4x\) 和 \(2x\) 上有高度 \(3,2\)，均严格大于 (16)。

最后 \(M\equiv1\pmod{13}\)，而

\[
x\equiv11h-2\pmod{13}.
\tag{17}
\]

所以 (1) 的 \(h\not\equiv12\pmod{13}\) 恰好保证 \(13\nmid K\)。这验证
\(N_R(4)\xrightarrow{13}N_R(4x)\) 的容量条件。至此 (10) 的每一步都是实际 raw
transition，而非只在 \(U(R)\) 中的模同余连线。

## 4. 两个相位层级与 endpoint gate

这里必须区分到 \(N_R(4)\) 与到 exact \(t=4\) 节点 \(N_R(4x)\) 的标签积。定义

\[
P=2\alpha\beta\gamma,
\qquad
W=13P.
\tag{18}
\]

其中 \(P\) 是从 canonical anchor 到 \(N_R(4)\) 的相位；\(W\) 才是从 anchor 到
\(N_R(4x)\) 的相位。由 (8)，模 \(R\) 有

\[
\alpha b\equiv-1,
\qquad
\beta a\equiv-b,
\qquad
8\gamma\equiv-a.
\tag{19}
\]

于是

\[
4P
=8\alpha\beta\gamma
\equiv-\alpha\beta a
\equiv\alpha b
\equiv-1
\pmod R.
\tag{20}
\]

结合 \(4M\equiv13\pmod R\)，得到

\[
\boxed{
P\equiv-4^{-1}\pmod R,
\qquad
W=13P\equiv-M\pmod R.
}
\tag{21}
\]

最后两个 \(2\)-边把 \(W\) 乘以 \(4\)，故完整 anchor-to-seed 标签积为

\[
\boxed{4W\equiv-13\pmod R.}
\tag{22}
\]

这严格经过既有的 determinant--raw endpoint gate：到 \(N_R(4x)\) 的相位为所需的
\(-M\)，到 seed \(N_R(x)\) 的完整词为所需的 \(-13\)。

## 5. 固定 \(a,b\) 时的 CRT 生成器

对固定 \((a,b)\)，(8) 的整数性，以及本 prime-label 专门化为使
\(\gamma\) 成为奇素数而采用的奇偶条件，给出如下系统：

\[
\begin{cases}
104h\equiv10\pmod b,\\
104h\equiv9+b\pmod a,\\
h\equiv(a+9)/8+1\pmod2.
\end{cases}
\tag{23}
\]

不能把其中任一条单独视为充分条件。前两条各自可解的必要且充分 gcd 门分别是

\[
\gcd(104,b)\mid10,
\qquad
\gcd(104,a)\mid(9+b).
\tag{24}
\]

即使 (24) 成立，也还必须检查两条线性同余解类与第三条奇偶同余在公共 gcd 上相容。
本卡的 CRT 假设是完整系统 (23) 可解。

令

\[
g_b=\gcd(104,b),
\qquad
g_a=\gcd(104,a),
\qquad
L=\operatorname{lcm}\left(\frac b{g_b},\frac a{g_a},2\right).
\tag{25}
\]

若 (23) 可解，则其解是某个 \(h_0\pmod L\)。沿

\[
h=h_0+Lu
\tag{26}
\]

三个数 \(p,\alpha,\beta,\gamma\) 都是 \(u\) 的整数仿射函数。再筛去

\[
h\equiv2\pmod3,
\qquad
h\equiv12\pmod{13},
\tag{27}
\]

并要求四个仿射数实际为素数，就得到定理的可枚举条件族。这里没有声称任一这样的
四元仿射素数系统有无穷多个参数值。

## 6. 三个新的 affine-prime 条件族

本节所有参数均取 \(u\in\mathbb N_0\)。这些是保留原始表述的 affine-prime
子族；每个控制点的三个中间标签都已核验为素数并满足 (7)。更一般的 factor-block
版本不要求三个标签为素数，但须逐个素因子按端点预留容量判定，不能把 (7) 误作其必要条件。

### 6.1 \((a,b)=(7,46)\)：引入 \(h\equiv1\pmod6\) 控制点

系统 (23) 化为

\[
h=43+322u.
\tag{28}
\]

其四个仿射数为

\[
\begin{aligned}
p&=1033+7728u, & \alpha&=97+728u,\\
\beta&=631+4784u, & \gamma&=557+4186u.
\end{aligned}
\tag{29}
\]

为留在 \(c=3\) 分支并保持 \(13\)-边容量，需要

\[
u\not\equiv1\pmod3,
\qquad
u\not\equiv6\pmod{13}.
\tag{30}
\]

在这些条件、\(p\) 为素数及 (7) 成立时，(10) 的 anchor 后标签为

\[
97+728u,
\quad
631+4784u,
\quad
2,
\quad
557+4186u,
\quad
13,
\quad
2,
\quad
2.
\tag{31}
\]

\(u=0\) 是控制点，给出 \(h=43\)、\(p=1033\) 以及标签
\((97,631,2,557,13,2,2)\)。

### 6.2 \((a,b)=(15,2)\)：\(h\equiv4\pmod6\) 的新族

系统 (23) 给出

\[
h=4+30u,
\tag{32}
\]

且

\[
\begin{aligned}
p&=97+720u, & \alpha&=203+1560u,\\
\beta&=27+208u, & \gamma&=49+390u.
\end{aligned}
\tag{33}
\]

此时自动有 \(h\equiv1\pmod3\)；\(13\)-边只排除

\[
u\equiv2\pmod{13}.
\tag{34}
\]

在 \(p\) 为素数、(7) 与 (34) 成立时，(10) 给出 raw 路径。取 \(u=37\)，得到

\[
h=1114,
\qquad
p=26737,
\qquad
(\alpha,\beta,\gamma)=(57923,7723,14479).
\tag{35}
\]

### 6.3 \((a,b)=(79,202)\)：\(h\equiv0\pmod6\) 的新族

这里

\[
\gcd(104,202)=2\mid10,
\qquad
\gcd(104,79)=1\mid211,
\tag{36}
\]

且完整 CRT 系统的解为

\[
h=138+15958u.
\tag{37}
\]

四个仿射数是

\[
\begin{aligned}
p&=3313+382992u, & \alpha&=71+8216u,\\
\beta&=179+21008u, & \gamma&=1783+207454u.
\end{aligned}
\tag{38}
\]

分支和 \(13\)-容量条件分别是

\[
u\not\equiv2\pmod3,
\qquad
u\not\equiv8\pmod{13}.
\tag{39}
\]

取 \(u=0\) 时四个数均为素数，且满足 (7)：

\[
(p,\alpha,\beta,\gamma)=(3313,71,179,1783).
\tag{40}
\]

## 7. 四个逐边 raw 控制点

下表中的每一行都以 (11) 的有序坐标逐步回放，检查了 source 的 \(p\)-边、所有
shift、gcd reduction、每个 \(q\)-进容量以及 (21)--(22) 的相位。它们只是明确控制，
不是对所有 \((a,b)\) 的穷尽搜索。

\[
\begin{array}{c|c|c|c|c}
h\bmod6 & (a,b) & h & p & (\alpha,\beta,\gamma)\\ \hline
3 & (7,2) & 3 & 73 & (151,43,37)\\
1 & (7,46) & 43 & 1033 & (97,631,557)\\
0 & (79,202) & 138 & 3313 & (71,179,1783)\\
4 & (15,2) & 1114 & 26737 & (57923,7723,14479)
\end{array}
\tag{41}
\]

因此，\(c=3\) 分支的四个允许余类

\[
h\bmod6\in\{0,1,3,4\}
\tag{42}
\]

都已有这一个双中间节点 skeleton 的实际控制点。特别地，原先的
\(h=3+42u\) 不是 endpoint phase 或 target source 的全局同余障碍。

## 8. 原 \((7,2)\) prime-label 模板为何恰为 \(h=3+42u\)

取 \((a,b)=(7,2)\)。前两条整除和 prime-label 专门化所用的
\(\gamma\) 为奇数条件先给

\[
h=3+14t.
\tag{43}
\]

这时

\[
\beta=43+208t.
\tag{44}
\]

若 \(t\equiv1\pmod3\)，则 \(h\equiv2\pmod3\)，不属于 \(c=3\) 分支；若
\(t\equiv2\pmod3\)，则

\[
\beta\equiv1+t\equiv0\pmod3,
\tag{45}
\]

此时 \(3\mid\beta\) 且 \(3\mid M\)，故违反 (7) 的严格容量条件。因此只剩
\(t\equiv0\pmod3\)，也就是

\[
h=3+42u.
\tag{46}
\]

这说明旧 prime-label 卡的参数限制来自该特定 \(1\to2\to7\to4\) 路径下的局部
容量筛；它不是该拓扑全部 factor-block 路径的必要条件。特别地，\(\gamma\) 为偶数时，
末端 \(4\) 的二进预留容量仍可能允许拆分后的 \(2\)-因子通过。第 6 节表明更换中间
节点后可进入其他 \(h\) 余类。

## 9. 反例、限制与合同边界

不能任意选择 \(a\equiv7\pmod8\)。例如 \((a,b)=(23,2)\) 时，第二条整除要求

\[
23\mid R-2=104h-11
\tag{47}

\]

强制

\[
h\equiv22\pmod{23}.
\tag{48}
\]

但 \(24\equiv1\pmod{23}\)，所以

\[
p=24h+1\equiv h+1\equiv0\pmod{23}.
\tag{49}
\]

对正整数 \(h\)，这里不可能有 \(p=23\)，故该表面上相同形状的候选族完全不能产生
目标素数。这是 CRT 可解之外仍需做局部素性筛的具体反例。

更一般地，固定 \((a,b)\) 后仍须要求 \(p\) 为素数并验证 (7)；本卡不声称有限个
\((a,b)\) 能覆盖全部核心素数。这里的 prime-label 专门化具有固定标签词；允许将
复合标签拆为素因子词的更强版本另见后续的 factor-block 结果，其词长不再有界。

最后，(10) 是 target chart 内的 raw/source provenance 结论。它在素数条件成立时可作为
E1 的 raw receipt，并与既有 complement seed 算术相容；但 even-tail direction 的 E3
verifier、全域 \(\operatorname{Sol}(p)\) lift 的 E4、以及宏级 E5 支付尚未定义。本卡
不构成 `verified_edge`，更不声称 Erdos--Straus 猜想已被解决。现有接口为何不能直接
接纳这类 receipt、以及 root-only entry 的最小字段，见
[偶侧 seed 的 fresh root-entry 准入边界](type-I-g-anchor-c3-even-tail-root-entry-admission-boundary.md)。
