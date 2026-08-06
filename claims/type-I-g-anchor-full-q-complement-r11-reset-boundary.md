---
kind: claim
claim_id: type-I-g-anchor-full-q-complement-r11-reset-boundary
title: full-Q 补余 seed 的 R=11 条件性 RESET 与标准 lift 边界
statement: 设 p=24h+1 是核心素数。full-Q 行的补余 torsor 产生两类 A=1 的真实 overflow determinant seed：h 不等于 2 (mod 3) 时 (M,d,n)=(26h+1,3,13)，h 等于 2 (mod 3) 时 (M,d,n)=((50h+2)/3,9,25)。两类 seed 的 d-dual 都精确落在同一低图表 (R_d,K_d)=(11,3(22h+1))。因此，只要 seed 另有 verified source/path/node receipt，现有 A=1 dual-RESET 定理就给出一条完整 E1--E5、恒等 Sol(p) lift 的 marked_absorb 边，支撑分别为 3 或 9。另一方面，pn=4Md+1 只给出带负尾的恒等式，n=13,25 不能充当 Bradford gap；两类 seed 上所有保留两分母的一项替换 lift 和同二尾一坐标缩放 lift 均为空。故 R=11 是一个强的条件性汇合点，而不是从旧 G raw path 已登记的递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-fixed-chart-affine-complement-overflow-torsor
  - type-I-overflow-a-one-dual-outer-rank-reset
  - type-I-overflow-fixed-n-bounded-divisor-saturation
  - two-denominator-lift-d-only-marked-normal-form
  - scaled-source-descent-rigidity
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - full-Q
  - complement-torsor
  - overflow
  - R-11
  - dual-reset
  - fixed-n
  - solution-lift
  - proof-boundary
sources:
  - claim: type-I-g-anchor-fixed-chart-affine-complement-overflow-torsor
    role: full-Q-complement-determinant-seeds
  - claim: type-I-overflow-a-one-dual-outer-rank-reset
    role: conditional-E1-E5-dual-edge
  - claim: two-denominator-lift-d-only-marked-normal-form
    role: complete-two-tail-lift-parameterization
  - claim: scaled-source-descent-rigidity
    role: same-tail-scaling-rigidity
visibility: public
last_checked: '2026-08-06'
---

# full-\(Q\) 补余 seed 的 \(R=11\) 条件性 RESET 与标准 lift 边界

## 1. 两族真实 overflow determinant seed

固定核心素数

\[
p=24h+1.
\tag{1}
\]

full-\(Q\) 行的补余 torsor 给出下列两族。这里 \(d\) 是新 determinant 行中的缺量，
\(C=p-d\) 是余因子，并且

\[
pn=4Md+1,
\qquad
R=4M-n,
\qquad
K=MC=M(p-d).
\tag{2}
\]

\[
\begin{array}{c|c|c|c|c|c}
\epsilon & \text{条件} & M & d & n & R \\ \hline
3 & h\not\equiv2\pmod3 & 26h+1 & 3 & 13 & 104h-9 \\
9 & h\equiv2\pmod3 & (50h+2)/3 & 9 & 25 & (200h-67)/3
\end{array}
\tag{3}
\]

第 (3) 中的每一行，直接代入即有

\[
pR+1=4K,
\qquad
R>p.
\tag{4}
\]

所以它们是实际的 overflow determinant chart。但它们此时只是算术
seed；是否能作为递归状态，仍取决于 source/path/node receipt。

## 2. 两族都压缩到 \(R=11\)

将 \(M=kp+r\) 写成 \(1\le r<p\)，并定义

\[
s=\frac{4rd+1}{p}.
\tag{5}
\]

对称 \(d\)-dual 图表为

\[
(R_d,K_d)=(4d-s,\ d(p-r)).
\tag{6}
\]

两支的参数完全显式：

\[
\begin{array}{c|c|c|c}
\epsilon&r&s&(R_d,K_d)\\ \hline
3&2h&1&(11,\ 3(22h+1))\\
9&M&25&(11,\ 3(22h+1))
\end{array}
\tag{7}
\]

例如第一支有 \(M=p+2h\)，而第二支 \(M<p\)，故 (7) 从
(5)--(6) 立即得到。尤其

\[
p\cdot11+1=4\cdot3(22h+1).
\tag{8}
\]

如果 (3) 的 seed **已经**具有 verified \(A=1\) overflow 的完整
source/path/node receipt，则现有 \(A=1\) dual-RESET 引理可以直接应用：

\[
A'=d\in\{3,9\},
\qquad
A'\mid K_d,
\qquad
R_d=11<p,
\tag{9}
\]

且

\[
\left\lfloor\frac{B_p}{A'}\right\rfloor
<
\left\lfloor\frac{B_p}{1}\right\rfloor,
\qquad
B_p=\frac{(p-1)^2}{4}.
\tag{10}
\]

因而这时存在一条完整的 E1--E5 边：解集取图表无关的
\(\operatorname{Sol}(p)\)，E4 是恒等提升，且目标 \(R_d<p\) 是
`marked_absorb`。

重要的量词是“如果已经具有 receipt”。现有 full-\(Q\) 补余
torsor 只构造了 (2) 的算术行，不能倒推 E1 的来源或 E3 的带标记
转移。

## 3. fixed-\(n\) 对照

令 \(S=Md=(pn-1)/4\)。两支的完全饱和选择 \(L=S\) 为

\[
S=
\begin{cases}
78h+3=(13p-1)/4,&\epsilon=3,\\
150h+6=(25p-1)/4,&\epsilon=9.
\end{cases}
\tag{11}
\]

它们均满足 \(S\le B_p\)。在同样的 verified-overflow 前提下，固定
\(n\) 引理因而可给出

\[
(R_S,K_S)=((p-1)n-1,\ S(p-1)).
\tag{12}
\]

但 \(n\in\{13,25\}\) 使 \(R_S>p\)，所以这是高 \(R\) overflow，而不是 (7) 的低图表吸收。

第二支还有一个特殊一致性：\(L=d=9\) 满足固定-\(n\) 窗口的
条件，并且给出同一张 \(R=11\) 图表：

\[
R_L=4\cdot9-25=11,
\qquad
K_L=9(p-M)=3(22h+1).
\tag{13}
\]

第一支不能如此写，因为 \(4d=12<n=13\)。它正是需要 (6) 的
dual 通道才到达 \(R=11\) 的原因。

## 4. determinant 永远不等于直接证书

核心行列式的正确变形是

\[
\boxed{
\frac4p=\frac{n}{Md}-\frac1{pMd}.
}
\tag{14}
\]

负号至关重要：即使 \(n/(Md)\) 能拆成两个正单位分数，(14) 也不给出
三项正 Egyptian 分解。而且 \(13,25\equiv1\pmod4\)，它们不能作为 Bradford
正规形的 gap \(m\equiv3\pmod4\)。

还可以看到，即使固定这一图表并要求含有分母 \(pK\) 的三项分解，也需要额外的
因子条件

\[
e\mid K^2,
\qquad
e\equiv-K\pmod R.
\tag{15}
\]

在 (15) 成立时才有

\[
u=\frac{K+e}{R},
\qquad
v=\frac{K+K^2/e}{R},
\qquad
\frac4p=\frac1u+\frac1v+\frac1{pK}.
\tag{16}
\]

这个条件不是 (2) 的推论。例如 \(p,h,\epsilon=(193,8,9)\) 时，

\[
(R,K)=(511,24656),
\qquad
K=2^4\cdot23\cdot67.
\tag{17}
\]
因 \(7\mid511\)，任意 \(e\mid K^2\) 模 \(7\) 都属于
\(\langle2\rangle=\{1,2,4\}\)，而 \(-K\equiv5\pmod7\)，故 (15) 失败。

## 5. 现有标准 lift 的精确排除

对“保留两个源分母、仅替换一项”的完整 D-only 正规形，因
\(n\equiv1\pmod4\)，其因子参数满足

\[
D\le n(n+3)-3p.
\tag{18}
\]

第一支中 \(p\ge73\)，所以

\[
D\le208-3p<0.
\tag{19}
\]

第二支除 \(p=193\) 外有 \(p\ge337\)，因而

\[
D\le700-3p<0.
\tag{20}
\]

在剩下的 \((p,n)=(193,25)\) 情形，\(0<D<625\) 且

\[
D\equiv np=4825\equiv121\pmod{672}.
\tag{21}
\]

只可能 \(D=121\)，但 \(121\nmid4825^2\)。所以两族在这个完整两尾
lift 模板上都没有 E4。

对同一二尾、只缩放被替换分母的模板，必要恒等式为

\[
4A(p-n)=n(p-d).
\tag{22}
\]

因 \((p,n)=1\) 且 \(n\) 为奇数，\(n\mid A\)。写 \(A=na\) 后有

\[
d=4an-(4a-1)p>0
\quad\Longrightarrow\quad
p<\frac{4an}{4a-1}\le\frac{4n}{3},
\tag{23}
\]

这与两族的 \(p\ge73\) 和 \(p\ge193\) 矛盾。因此这个 scaling 模板也不能
把常数 \(n\) seed 变成递归入口。

## 6. 余下缺口

本卡给出的 \(R=11\) 通道有两重作用：它把两个看似不同的
full-\(Q\) 补余族合并成一个低图表目标，并且一旦来源合法就有现成的
严格 E1--E5 计费。它没有解决的唯一关键步骤是：

\[
\text{old G raw source/path}
\longrightarrow
\text{full-\(Q\) complement seed}
\tag{24}
\]

的 action-preserving marked adapter。目标图表当然可拥有自己的 universal
source，但那是一棵独立的 fresh source tree，不会反向补全 (24) 的 E1/E3。

以上排除了已知的两尾、同尾 scaling 和常数源模板；它不排除新的三坐标非线性
lift、另一个 \(N<p\) 源，或独立的 \(p\)-依赖 Type I/II 终端。
