---
kind: claim
claim_id: cyclic-reciprocal-transport-obstruction
title: 最小循环倒数耦合提升对核心素数的整性障碍
statement: 对任意核心素数 p=1 mod24、任意 2<=n<p 及任意正整数源解 4/n=1/a+1/b+1/c，循环倒数耦合式 1/A=n(1/a+1/b)/(2p)、1/B=n(1/b+1/c)/(2p)、1/C=n(1/c+1/a)/(2p) 虽恒满足 1/A+1/B+1/C=4/p，却不可能同时令 A,B,C 为正整数。因此最小的零偏移、两稀疏循环三坐标耦合不能提供带标记严格递降边。
claim_status: established
topics:
- descent
- solution-lift
- obstruction
- integrality
- unit-fractions
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: Section 2
  role: Egyptian-fraction equation context
visibility: public
last_checked: '2026-07-25'
---

# 最小循环倒数耦合提升对核心素数的整性障碍

## 候选耦合式

设

\[
\frac4n=\frac1a+\frac1b+\frac1c,\qquad 2\le n<p,
\]

并定义三个目标倒数

\[
\begin{aligned}
\frac1A&=\frac n{2p}\left(\frac1a+\frac1b\right),\\
\frac1B&=\frac n{2p}\left(\frac1b+\frac1c\right),\\
\frac1C&=\frac n{2p}\left(\frac1c+\frac1a\right). \tag{1}
\end{aligned}
\]

每一个源坐标恰出现两次，故无须任何因子条件便有实数恒等式

\[
\frac1A+\frac1B+\frac1C
=\frac np\left(\frac1a+\frac1b+\frac1c\right)
=\frac4p. \tag{2}
\]

这是一种改变全部三个坐标的零偏移循环耦合，不属于保留一项或两项的提升模板。
其唯一问题是三个倒数能否同时是单位分数。

## 定理

若 \(p\equiv1\pmod {24}\) 为素数，则 (1) 的 \(A,B,C\) 不可能同时为正整数。

换言之，按循环记号，三个整性条件

\[
n(a+b)\mid2pab,\quad
n(b+c)\mid2pbc,\quad
n(c+a)\mid2pca \tag{3}
\]

不能与源方程同时成立。

## 证明

对一对 \((a,b)\)，记

\[
q_{ab}=\frac{n(a+b)}{\gcd(n(a+b),2ab)}. \tag{4}
\]

由 (3) 可知 \(q_{ab}\mid p\)，所以 \(q_{ab}\in\{1,p\}\)。
若 \(q_{ab}=p\)，由于 \(p\nmid n\)，便有

\[
p\mid a+b. \tag{5}
\]

另一方面，源方程给出

\[
\frac{2ab}{n(a+b)}
=\frac{2c}{4c-n}. \tag{6}
\]

因此 \(q_{ab}=1\) 当且仅当右式为正整数。若设其等于 \(k\)，并写
\(r=2k-1\)，则

\[
c=\frac{kn}{2(2k-1)},\qquad
4c-n=\frac nr. \tag{7}
\]

特别地 \(r\mid n\)。

三个 \(q\) 中至多有一个等于 \(1\)。事实上，若例如
\(q_{bc}=q_{ca}=1\)，则由 (6) 的循环版本可取正整数 \(u,v\)，使

\[
a=\frac{un}{4u-2},\qquad
b=\frac{vn}{4v-2}.
\]

代回源方程得到

\[
\frac1c=\frac{2/u+2/v-4}{n}\le0,
\]

矛盾。若三个 \(q\) 都等于 \(p\)，则 (5) 对三对成立；由于 \(p\) 是奇数，
\(p\mid a,b,c\)。把源方程同除以 \(p\) 后会给出

\[
\frac{4p}{n}=\frac1{a/p}+\frac1{b/p}+\frac1{c/p}\le3,
\]

但 \(p>n\)，矛盾。故恰有两个 \(q\) 等于 \(p\)，另一个等于 \(1\)。

不妨设

\[
p\mid a+b,\qquad p\mid b+c,\qquad q_{ca}=1. \tag{8}
\]

在源方程

\[
4abc=n(ab+bc+ca) \tag{9}
\]

中模 \(p\) 计算。由 \(a\equiv c\equiv-b\pmod p\)，并且 \(p\nmid b\)
（否则三项都被 \(p\) 整除，已排除），得

\[
4b\equiv-n\pmod p. \tag{10}
\]

而 \(q_{ca}=1\) 对应 (7) 中的互补坐标 \(b\)。所以

\[
4b-n=\frac nr,\qquad r\mid n,\qquad r=2k-1\ \text{为奇数}. \tag{11}
\]

将 (10) 与 (11) 合并，得到

\[
p\mid4b+n=\frac{n(2r+1)}r. \tag{12}
\]

因 \(r\mid n<p\)，可在模 \(p\) 下消去 \(nr^{-1}\)，从而
\(p\mid2r+1\)。又 \(0<2r+1<2p+1\) 且 \(2r+1\) 为奇数，故

\[
2r+1=p. \tag{13}
\]

但是 \(p\equiv1\pmod {24}\) 蕴含

\[
r=\frac{p-1}{2}\equiv0\pmod {12},
\]

这与 (11) 的 \(r\) 为奇数矛盾。定理得证。

## 矩阵化推论

令源倒数向量为

\[
t=(1/a,1/b,1/c)^{\mathsf T},\qquad \boldsymbol1^{\mathsf T}t=\frac4n.
\]

任何零偏移线性倒数传输 \(t'=Mt\)，若要对这个实数解平面上的全部 \(t\) 都满足
\(\boldsymbol1^{\mathsf T}t'=4/p\)，当且仅当

\[
\boldsymbol1^{\mathsf T}M=\frac np\boldsymbol1^{\mathsf T}. \tag{14}
\]

这是因为左侧在仿射平面 \(\boldsymbol1^{\mathsf T}t=4/n\) 上恒定，当且仅当其
线性系数向量与 \(\boldsymbol1\) 平行；代入总和即得比例 \(n/p\)。

特别地，若 \(M\) 是每行、每列均恰有两个非零元且所有非零元同为
\(n/(2p)\) 的正矩阵，则其零一支撑是一个 \(3\) 阶二正则二分图，必为
\(J-P\)，其中 \(P\) 是置换矩阵。重排源、目标坐标后它就是 (1) 的循环矩阵
\(J-I\)。故上述定理同时排除了整个**平衡二稀疏零偏移**族，而非仅排除某个坐标次序。

## 任意非均匀权重的偶数标准源障碍

上述对称权重并不是唯一可能的循环传输。令 \(0<r<s\)、\(\gcd(r,s)=1\)，并改用

\[
\begin{aligned}
\frac1A&=\frac n{ps}\left(\frac r a+\frac{s-r}b\right),\\
\frac1B&=\frac n{ps}\left(\frac r b+\frac{s-r}c\right),\\
\frac1C&=\frac n{ps}\left(\frac r c+\frac{s-r}a\right). \tag{15}
\end{aligned}
\]

每个输入倒数的总系数仍为 \(r+(s-r)=s\)，所以 (15) 对任意实数源解仍满足
\(1/A+1/B+1/C=4/p\)。但它不能从最简单、无条件可解的偶数标准源

\[
\frac4n=\frac1{n/2}+\frac1n+\frac1n,\qquad 2\mid n,\quad n<p \tag{16}
\]

产生核心目标的整数解。事实上，代入 \((a,b,c)=(n/2,n,n)\) 后三项被强制为

\[
A=\frac{ps}{s+r},\qquad B=p,\qquad C=\frac{ps}{2s-r}. \tag{17}
\]

若 \(A,C\) 都是整数，则

\[
s+r\mid ps,\qquad 2s-r\mid ps. \tag{18}
\]

既约性给出

\[
\gcd(s+r,s)=\gcd(2s-r,s)=1.
\]

又两个左侧因子都大于 \(1\)，所以当 \(p\) 是素数时 (18) 迫使

\[
s+r=p,\qquad2s-r=p.
\]

于是 \(s=2r\) 且 \(p=3r\)，与核心素数 \(p\equiv1\pmod {24}\) 矛盾。
这个结论没有对 \(r,s\) 施加大小上界。

因此，在全部零偏移循环权重中，任何可能的正向路线都不能只调用偶数标准源；
它必须使用非标准源解的额外因子结构，或离开循环传输族。

同样的结论适用于另一条无条件标准源。若 \(3\mid n<p\)，取

\[
\frac4n=\frac1{n/3}+\frac1{2n}+\frac1{2n}. \tag{19}
\]

把它代入 (15)，得到

\[
A=\frac{2ps}{s+5r},\qquad B=2p,\qquad
C=\frac{2ps}{6s-5r}. \tag{20}
\]

记 \(g=\gcd(s,5)\)。由 \(\gcd(r,s)=1\)，两个分母因子分别与 \(s\) 的最大公因数
都恰为 \(g\)。若 (20) 的 \(A,C\) 为整数，令

\[
u=\frac{s+5r}{g},\qquad v=\frac{6s-5r}{g},
\]

则

\[
u,v\mid2p,\qquad
7s=g(u+v),\qquad
r=\frac{g(6u-v)}{35}. \tag{21}
\]

正性 \(0<r<s\) 给出 \(v<6u\) 与 \(u<6v\)。核心素数满足 \(p\ge73\)，而
\(u,v\) 只能属于 \(\{1,2,p,2p\}\)。因此它们不能一个来自 \(\{1,2\}\)、另一个来自
\(\{p,2p\}\)，否则比值至少为 \(p/2>6\)。若两者都小，则 \(u+v\in\{2,3,4\}\)；
若两者都含 \(p\)，则 \(u+v\in\{2p,3p,4p\}\)。但由 (21) 和
\(\gcd(g,7)=1\)，两种情形都必须有 \(7\mid u+v\)，前者不可能，后者迫使 \(p=7\)。
故 (19) 也没有核心目标的整数加权循环提升。

这把循环传输的可用源进一步压到真正非标准、带因子标记的解；它不能从两条最常见的
无条件标准分解中获得归纳起点。

这不是说加权循环恒空。例如

\[
\frac4{15}=\frac14+\frac1{120}+\frac1{120}
\]

在 \(p=31\)、\(r/s=1/2\) 时由 (15) 送到

\[
\frac4{31}=\frac1{16}+\frac1{248}+\frac1{16}. \tag{22}
\]

这个正例的源解是非标准的，而 \(31\not\equiv1\pmod {24}\)。它说明新的障碍精确针对
本问题的核心同余类及无条件标准源；因此下一项有信息量的研究是为核心 \(p\) 寻找具有
可递归因子描述的非标准标记源解，而不是继续变换标准三元组。

## 可复现的独立核对

脚本枚举每个 \(n<p\) 的全部排序源解，并以精确有理数检验 (1)：

    python3 reproductions/cyclic_reciprocal_lift.py \
      --limit 200 \
      --output reproductions/cyclic-reciprocal-lift-core-200-results.json

该范围含 \(73,97,193\) 三个核心素数，并逐一检查 31,921 个源解；输出没有整数循环提升。
这只是对实现和符号的有限交叉核对，不是定理证明所依赖的外推。

## 对下一轮搜索的约束

(1) 是最小的零偏移、每行恰读取两项的正循环倒数传输。它已经同时满足：

1. 在实数解曲面上对所有源解成立；
2. 改变全部三项，而非保留一个目标坐标；
3. 对带标记源解可直接检验整性。

定理表明这些优点仍不足以给出核心类递降。因此下一个候选至少必须放宽其中一项：
使用非均匀的耦合权重或三稀疏矩阵、加入不与直接证书等价的偏移，或让耦合系数依赖于
源解的额外因子标记。无论采用哪种方案，都仍须按 marked-solution-descent-closure
的要求证明标记源状态可递归闭合。
