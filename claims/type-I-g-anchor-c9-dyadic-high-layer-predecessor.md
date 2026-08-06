---
kind: claim
claim_id: type-I-g-anchor-c9-dyadic-high-layer-predecessor
title: c=9 补余 seed 的二进高层 raw 前驱与 provenance 边界
statement: 设 p=24h+1 为核心素数且 h=2 (mod 3)，令 c=9 full-Q 补余 seed 的 target raw node 为 T={x,R-x}，其中 x=p-9。所有以 q=2、m>1 进入 T 的 primitive formal raw 前驱均可由一个方向 X 属于 {x,R-x} 和整数 gamma 精确参数化；其合法性等价于正性、互素性和 v_2(2 gamma X)>v_2(K) 四项条件。特别地，x 侧存在无穷多条 dyadic 前驱：对无穷多个指数 a，(2^a x,2^a(R-x)-R,2^a-1) 经 q=2 与 gcd reduction 2^(a-1) 落到 T。该结果只建立局部 analysis-evidence raw transition；它不提供 source/path provenance、overflow bundle receipt、E3 verifier、Sol(p) lift 或 E5，故不能把 c=9 seed 或 R=11 dual-RESET 登记为 verified_edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-even-tail-complement-source-switch
  - type-I-g-anchor-complement-seed-m1-interface-rigidity
  - type-I-g-anchor-full-q-complement-r11-reset-boundary
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-g-anchor-marked-raw-peeling-calculus
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - complement-torsor
  - c9
  - raw-path
  - m-greater-than-one
  - dyadic
  - source-provenance
  - proof-boundary
sources:
  - claim: type-I-g-anchor-even-tail-complement-source-switch
    role: c9-complement-seed-and-m1-boundary
  - claim: type-I-g-anchor-complement-seed-m1-interface-rigidity
    role: m1-inbound-no-go
  - claim: type-I-g-anchor-full-q-complement-r11-reset-boundary
    role: conditional-dual-reset
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: raw-transition-and-source-semantics
  - concept: denominator-escape-state-contract
    role: E1-E5-admission-boundary
visibility: public
last_checked: '2026-08-06'
---

# \(c=9\) 补余 seed 的二进高层 raw 前驱与 provenance 边界

## 1. \(c=9\) target 图表与记号

固定核心素数

\[
p=24h+1,
\qquad
h=3k+2.
\tag{1}
\]

full-\(Q\) 补余的 \(c=9\) seed 给出

\[
\begin{aligned}
x&=p-9=72k+40, & M&=50k+34,\\
R&=4M-25=200k+111, & y&=R-x=128k+71,\\
K&=Mx.
\end{aligned}
\tag{2}
\]

因而

\[
pR+1=4K,
\qquad
x+y=R,
\qquad
(x,y)=1,
\qquad
2x<R<3x.
\tag{3}
\]

这里 \(x\) 为偶数，而 \(y,R\) 为奇数。记

\[
\lambda=v_2(x),
\qquad
\nu=v_2(M),
\qquad
v_2(K)=\lambda+\nu.
\tag{4}
\]

由 \(x=8(9k+5)\)、\(M=2(25k+17)\)，有

\[
\lambda\ge3,
\qquad
\nu\ge1.
\tag{5}
\]

令

\[
T=\operatorname{can}(x,y,1)
\tag{6}
\]

为 seed 的 canonical formal node，其中

\[
\operatorname{can}(A,B,m)=(\min\{A,B\},\max\{A,B\},m).
\tag{7}
\]

已知 \(T\) 在整个 \(m=1\) raw 图中没有入边；原因是唯一的几何候选
\(q=2\) 不满足 \(v_2(2x)>v_2(K)\)。本卡说明：这并不排除来自 \(m>1\)
层的实际 formal raw 入边。

## 2. 所有 \(q=2,m>1\) 入边的精确参数化

取一个方向

\[
X\in\{x,y\},
\qquad
Y=R-X,
\tag{8}
\]

并对 \(\gamma\ge2\) 定义带有指定被除坐标的候选

\[
P_{X,\gamma}
=\operatorname{can}\bigl(2\gamma X,\,2\gamma Y-R,\,2\gamma-1\bigr).
\tag{9}
\]

**定理（高层二进前驱的充要参数化）。** 式 (9) 是一个以 \(2\gamma X\)
为被 \(q=2\) 除去坐标、并且终点为 \(T\) 的 primitive \(m>1\) raw 前驱，当且仅当

\[
\boxed{
\begin{aligned}
2\gamma Y&>R,\\
(\gamma,R)&=1,\\
(X,2\gamma-1)&=1,\\
v_2(2\gamma X)&>\lambda+\nu.
\end{aligned}}
\tag{10}
\]

在这些条件下，其 raw transition 具有精确的未约分与约分形式

\[
\begin{aligned}
&(2\gamma X,\,2\gamma Y-R,\,2\gamma-1)\\
&\quad\xrightarrow[\text{shift}=1]{q=2}
(\gamma X,\gamma Y,\gamma)
\xrightarrow[\text{gcd reduction}=\gamma]{}
(X,Y,1),
\end{aligned}
\tag{11}
\]

后者 canonicalize 后正是 \(T\)。

**证明。** \(m=2\gamma-1\) 为奇数，故 \(q=2\) 的唯一 raw shift 是 \(1\)。
式 (11) 由 raw transition 的定义直接给出。又 \(2\gamma Y-R\) 为奇数，且

\[
\gcd\bigl(2\gamma X,2\gamma Y-R\bigr)=1
\Longleftrightarrow
(\gamma,R)=1\ \text{且}\ (X,2\gamma-1)=1.
\tag{12}
\]

事实上，一个奇素数若同时整除 \(\gamma\) 和第二坐标，就整除 \(R\)；若同时整除
\(X\) 和第二坐标，则由 \((X,Y)=1\) 恰整除 \(2\gamma-1\)。这证明了
primitive 条件的充要性。最后一条正是 \(q=2\) 的超容量条件。此时
\(R,m,2\gamma Y-R\) 都为奇数，故 \(q=2\) 的 unit-shift 条件自动成立。

反过来，设一个 \(q=2\) 的 \(m>1\) raw 边落到 \(T\)。其源层数必须为奇数，写作
\(m=2\gamma-1\)。未约分后层数为 \(\gamma\)；终点层数为 \(1\)，故 gcd reduction
恰为 \(\gamma\)。将终点两坐标按被除坐标的方向记为 \((X,Y)\)，便强制得到 (9) 与
(11)。其余 raw 和 primitive 条件恰为 (10)。证毕。

## 3. 两个方向的显式条件

若 \(X=x\)、\(Y=y\)，因 \(y>R/2\)，正性自动成立。式 (10) 化为

\[
\boxed{
2^\nu\mid\gamma,
\qquad
(\gamma,R)=1,
\qquad
(x,2\gamma-1)=1.
}
\tag{13}
\]

这里第一项来自

\[
v_2(2\gamma x)>v_2(x)+\nu
\Longleftrightarrow
v_2(\gamma)\ge\nu.
\tag{14}
\]

若 \(X=y\)、\(Y=x\)，容量条件化为

\[
2^{\lambda+\nu}\mid\gamma.
\tag{15}
\]

它强制 \(\gamma\ge16\)，而 \(2x<R<3x\)，故这时正性也自动成立。第二个方向的完整条件是

\[
\boxed{
2^{\lambda+\nu}\mid\gamma,
\qquad
(\gamma,R)=1,
\qquad
(y,2\gamma-1)=1.
}
\tag{16}
\]

因此 \(m=1\) 入边的缺失只是最低层的容量阻塞，并不是整个 formal raw 图的入边
缺失。

## 4. 无穷 dyadic 前驱族

考虑 \(X=x\) 的方向。令 \(a\) 是一个素数，满足

\[
a>
\max\left\{
\nu,\ \,\operatorname{ord}_r(2):
r\mid x,\ r\ \text{为奇素数}
\right\}.
\tag{17}
\]

取 \(\gamma=2^{a-1}\)。则 \((\gamma,R)=1\)，且若某个奇素数
\(r\mid x\) 还整除 \(2^a-1\)，便有 \(\operatorname{ord}_r(2)\mid a\)。
对奇素数 \(r\)，有 \(\operatorname{ord}_r(2)>1\)；而 \(a\) 为比所有这些阶都大的
素数，所以该阶既不能等于 \(1\) 也不能等于 \(a\)，不可能整除 \(a\)。因此 (13) 成立，得到

\[
\boxed{
P_a=
\operatorname{can}\bigl(2^a x,\,2^a y-R,\,2^a-1\bigr)
\xrightarrow{q=2}T.
}
\tag{18}
\]

其精确回放为

\[
(2^a x,2^a y-R,2^a-1)
\longmapsto
(2^{a-1}x,2^{a-1}y,2^{a-1})
\longmapsto
(x,y,1),
\tag{19}
\]

第二箭头的 gcd reduction 为 \(2^{a-1}\)。由素数有无穷多个，满足 (17) 的 \(a\)
也有无穷多个；于是 (18) 给出无穷多个两两不同的高层 primitive formal 前驱。

这族的标签固定为 \(2\)，但层数 \(m=2^a-1\) 和坐标尺度不受界。它不能被误读为
“一个有界 \(m=1\) raw word 已经到达 seed”。

## 5. 两个聚焦控制

\[
\begin{array}{c|c|c|c|c|c|c}
p & h & (R,x,y) & M & K & v_2(K) & P_{x,2^{a-1}}\\ \hline
193 & 8 & (511,184,327) & 134 & 24656 & 4 & (736,797,3)\\
337 & 14 & (911,328,583) & 234 & 76752 & 4 & (1312,1421,3)
\end{array}
\tag{20}
\]

两行都可取 \(a=2\)，此时 \(\nu=1\) 且 \((x,3)=1\)。raw 回放分别为

\[
(736,797,3)
\longmapsto(368,654,2)
\longmapsto(184,327,1),
\tag{21}
\]

以及

\[
(1312,1421,3)
\longmapsto(656,1166,2)
\longmapsto(328,583,1).
\tag{22}
\]

这两个控制也说明本卡与 \(m=1\) 无入边结论完全相容：两条边的源层数都是 \(3\)，
而非 \(1\)。特别地，\(p=337\) 旧 G universal-source Reach 不含其偶侧
source-switch 所需的 \(\{7,328\}\)，并不妨碍 target 图表在更高 formal 层拥有
(22) 这样的局部前驱。

## 6. provenance 与 E1--E5 的严格边界

式 (11)、(18)、(21)、(22) 的正确类型是
`analysis_evidence_not_verified_edge`。它们只证明一个既已给定的高层 primitive
formal node 可以经真实 raw 规则落到 seed，不能提供该高层 node 的来源。具体地：

| 项 | 本卡给出的内容 | 尚未给出的内容 |
|---|---|---|
| E1 | 一条局部 raw transition 的整数回放 | 从具名 universal source 或另一合法 root 到 \(P_{X,\gamma}\) 的 source/path/node receipt 与 scope |
| E2 | seed 的既有 determinant 算术 | 产生该 seed 的 complete-excess 或 overflow-determinant bundle receipt |
| E3 | primitive 性、shift、容量与 gcd 的局部检查 | 将 \(m>1\) triple 接入偶侧 mark、typed classification 和 source-switch 的正规形 verifier |
| E4 | 无 | 对带标记解集的全域 \(\operatorname{Sol}(p)\) lift |
| E5 | formal 层数从 \(2\gamma-1\) 降至 \(1\) | 一条已准入状态边的良基势支付与 terminal-first 调度 |

因此，已有的 \(R=11\) d-dual RESET 仍只能在 seed **另有**完整 verified receipt 时
使用；本卡的高层前驱本身不能补足该前提。它也不产生直接 Type I/II certificate，
不构成 `verified_edge`，更不声称 Erdos--Straus 猜想已被解决。

后续若要把这条接口变成真正候选宏，最小工作是构造一个可重放的高层 source tree，
定义其到偶侧 \(t=1\) mark 的 E3 适配器，并独立证明 E4 与 E5。此前，应优先保留
[\(n-2\) direct terminal 筛](type-I-g-anchor-complement-seed-n-minus-two-terminal-sieves.md)
和 [\(m=1\) 接口刚性边界](type-I-g-anchor-complement-seed-m1-interface-rigidity.md)
作为不依赖该高层接口的分支。

## 7. 两个 \(\gamma=2\) 控制点的 source 边界

本节只讨论 \(p=193,337\) 的 \(\gamma=2\) 高层前驱，不能外推为全部 \(c=9\)
source tree 的分类。令

\[
P=(A,B,3)=(4x,4y-R,3),
\qquad
A=96h-32,
\qquad
B=104h-35.
\tag{23}
\]

### target universal source 不可达 \(P\)

target 的 universal source 为

\[
\mathsf S=(p,R(p-1)-p,p-1).
\tag{24}
\]

在两个控制点，其第二坐标均为素数：

\[
\begin{array}{c|c|c|c}
p&R&K&R(p-1)-p\\ \hline
193&511&24656&97919\\
337&911&76752&305759
\end{array}
\tag{25}
\]

所以 \(\mathsf S\) 只有标签 \(p\) 与该第二坐标两条 raw 出边，二者都直接到达
\((1,R-1,1)\)。后一标签的 shift 是 \(R(p-1)-p-(p-1)\)。由于任意 \(m>1\)
raw 边严格降低 \(m\)，而 \(m=1\) 边保持该层，\(\mathsf S\) 的所有非平凡后代均在
底层，不能命中层数为 \(3\) 的 \(P\)。这给出两个 strict local no-go，而不是一般的
source 不存在结论。

### 一步 \(m=p-1\) parent 的限定性分类

设一个 primitive 层数 \(L=p-1\) node 一步进入 \(P\)，标签为 \(q\)、gcd reduction
为 \(g\)，并令 \(C=qg\)。若最终被除方向是 \(X\in\{A,B\}\)，则存在
\(1\le t<q\) 使

\[
L+t=3C,
\qquad
\text{source coordinates}=\{CX,RL-CX\}.
\tag{26}
\]

故 primitive 性必要要求

\[
(CX,RL)=1,
\qquad\text{特别地}\qquad (X,RL)=1.
\tag{27}
\]

对 \(p=337\)，有

\[
(A,RL)=16,
\qquad
(B,RL)=7,
\tag{28}
\]

所以所有 \(q,g,t\) 的一步 \(m=336\) primitive parent 都被排除。对 \(p=193\)，
只有 \(X=B\) 通过 (27) 的必要条件；有限枚举给出五个 formal parent：

\[
\begin{array}{c|c}
\text{parent}&(q,t,g)\\ \hline
(46307,51805,192)&(5,3,13)\ \text{或}\ (13,3,5)\\
(41525,56587,192)&(71,21,1)\\
(35149,62963,192)&(79,45,1)\\
(31961,66151,192)&(83,57,1)\\
(27179,70933,192)&(89,75,1)
\end{array}
\tag{29}
\]

它们均不含坐标 \(p=193\)，因此不是 `universal_p_source_v1`；仍只是无根 formal
parents。

### 旧仿射 source-switch 也不能命中 \(P\)

对已有的 \(c=9\) 仿射候选

\[
\Phi_\Delta(U,V,m)=(U,V+\Delta m,m),
\qquad
\Delta=\frac{128h-64}{3},
\tag{30}
\]

有

\[
3\Delta=128h-64>A,B
\tag{31}
\]

（核心 \(c=9\) 域从 \(h=8\) 开始）。所以无论全局坐标方向如何，\(P\) 的
\(\Phi_\Delta\) 逆像都有一个负坐标。旧 G 图表的这个特定 affine adapter 因而不能把
任何旧 \(m=3\) node 送到 \(P\)。这不排除非线性、多图表或新 root-entry 宏。

最后，两个控制点确有无根的二进逆塔：在 primitive 与容量条件成立的层上，

\[
H_j=\operatorname{can}\left(2^jA,
R+2^j(B-R),2^{j+1}+1\right),
\qquad
H_{j+1}\xrightarrow{q=2}H_j,
\qquad H_0=P.
\tag{32}
\]

其层数分别延伸为

\[
193:\ 3,5,9,17,33,65,129;
\qquad
337:\ 3,5,9,17,33,65,129,257.
\tag{33}
\]

它们全为奇数，不能与层数 \(p-1\) 为偶数的 universal source 直接接合。该塔强调的是
formal 局部丰富性，不能代替 E1 provenance。
