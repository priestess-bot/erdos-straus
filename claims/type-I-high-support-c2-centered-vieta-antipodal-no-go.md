---
kind: claim
claim_id: type-I-high-support-c2-centered-vieta-antipodal-no-go
title: 最小 C=2 图表的反足 Vieta 全称 no-go
statement: >-
  对每个正整数 U，令 R=8U-1、K=U(8U+1)。则 R/K 不可能写成两个
  正单位分数；等价地，K^2 没有除子 d 满足 d=-K (mod R)，也不存在互素
  a,b 满足 ab|K、R|a+b。证明把假想反足对化为
  (a+b+h)(a+b+2h)=8abch^2，并对 b 作 Vieta 跳跃；除唯一判别式为负的
  边界外，另一正整数根严格小于 a，与最小反例矛盾。取
  U=(p-1)/4 后得到：每个核心素数的最小高支撑 C=2 图表
  (R_2,K_2)=(2p-3,(p-1)(2p-1)/4) 都 centered Type I miss，
  所以关系点 E=2(p-1)、n=p-1 的自然标记源对所有 p 都为空，而不只是
  在已经分类为 F/G 的控制上为空。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-support-c2-boundary-carry-dyadic-capacity-transduction
  - type-I-generalized-dyadic-natural-lift-equivalence
  - type-I-general-b-centered-square-spectrum
topics:
  - type-I
  - high-support
  - c2-boundary
  - centered-spectrum
  - antipodal-divisor
  - unit-fraction
  - vieta-jumping
  - strict-no-go
  - marked-solution
sources:
  - reproduction: reproductions/type_i_high_support_c2_centered_vieta_no_go.py
    role: symbolic-identity-and-focused-antipodal-control-verifier
visibility: public
last_checked: '2026-08-11'
---

# 最小 \(C=2\) 图表的反足 Vieta 全称 no-go

## 1. 全称定理

对任意正整数 \(U\)，令

\[
R=8U-1,
\qquad
V=8U+1=R+2,
\qquad
K=UV.
\tag{1}
\]

则

\[
\boxed{
\frac RK\ne\frac1x+\frac1y
\quad\text{对所有 }x,y\in\mathbb N.}
\tag{2}
\]

等价地，

\[
\boxed{
\nexists d\mid K^2:\quad d\equiv-K\pmod R.}
\tag{3}
\]

这个结论不需要 \(4U+1\) 为素数，也不依赖有限指数盒的大小估计。

## 2. 从二单位分数到互素反足对

标准因子化给出

\[
\frac RK=\frac1x+\frac1y
\iff
(Rx-K)(Ry-K)=K^2.
\tag{4}
\]

反向恢复也没有隐藏整除条件：若 \(d\mid K^2\) 且
\(d\equiv-K\pmod R\)，则 \((R,K)=1\) 给出 \((R,d)=1\)，并有

\[
x=\frac{K+d}{R},
\qquad
y=\frac{K+K^2/d}{R}\in\mathbb N.
\]

其中第二个分子的整除性来自
\(K^2/d\equiv-K\pmod R\)，两个分母也显然为正。把 \(d\) 换成互补因子
\(K^2/d\) 只交换 \(x,y\)；又因 \(d=K\) 会迫使 \(R\mid2K\)，与
\((R,K)=1\)、\(R\ge7\) 矛盾，所以可规范为 \(0<d<K\)。因此 (2) 与 (3)
确实等价。

下面把 (3) 改写成更适合下降的反足形式。

任取 \(d\mid K^2\)。逐素因子把 \(d/K\) 约成最简分数

\[
\frac dK=\frac ab,
\qquad
(a,b)=1,
\qquad
a\mid K,\quad b\mid K,\quad ab\mid K.
\tag{5}
\]

因为 \((R,K)=1\)，同余 \(d\equiv-K\pmod R\) 等价于

\[
a\equiv-b\pmod R.
\tag{6}
\]

反过来，任意满足 (5)--(6) 的 \(a,b\) 都给出

\[
d=\frac{Ka}{b}\mid K^2,
\qquad d\equiv-K\pmod R.
\]

所以只需排除

\[
\boxed{
(a,b)=1,\quad ab\mid K,\quad R\mid a+b.}
\tag{7}
\]

## 3. 必要的 Vieta 方程

假设 (7) 成立，定义

\[
h=\frac{a+b}{R},
\qquad
c=\frac{K}{ab}.
\tag{8}
\]

四个量 \(a,b,h,c\) 都是正整数。由

\[
8K=(R+1)(R+2)
\tag{9}
\]

以及 \(R=(a+b)/h\)，得到必要方程

\[
\boxed{
(a+b+h)(a+b+2h)=8abch^2.}
\tag{10}
\]

下面证明 (10) 根本没有正整数解；这比只排除带额外互素条件的 (7) 更强。

## 4. Vieta 递降

反设 (10) 有正整数解，取使

\[
\max(a,b)
\]

最小的一组，并利用 (10) 的对称性令 \(a\le b\)。把 (10) 视为关于 \(b\)
的二次方程：

\[
F(X)
=X^2+(2a+3h-8ach^2)X+(a+h)(a+2h).
\tag{11}
\]

于是 \(F(b)=0\)，另一根为

\[
\boxed{
b'=\frac{(a+h)(a+2h)}{b}.}
\tag{12}
\]

因为 \(F\) 是首一整系数多项式且 \(b\) 是整数根，\(b'\) 也是整数；根的乘积
为正，所以 \(b'>0\)。

现在计算

\[
F(0)=(a+h)(a+2h)>0,
\tag{13}
\]

\[
F(a)
=(4-8ch^2)a^2+6ah+2h^2.
\tag{14}
\]

若 \(h\ge2\)，由 \(c\ge1\) 有

\[
F(a)
\le
(4-8h^2)a^2+6ah+2h^2.
\tag{15}
\]

记 (15) 右侧为 \(G_h(a)\)。它在 \(a\ge1\) 上严格递减，因为

\[
G_h(a+1)-G_h(a)
=(4-8h^2)(2a+1)+6h<0
\qquad(h\ge2,a\ge1),
\]

而 \(a=1\) 时

\[
4+6h-6h^2<0.
\tag{16}
\]

若 \(h=1,a\ge2\)，则

\[
F(a)\le-4a^2+6a+2<0.
\tag{17}
\]

若 \(h=a=1,c\ge2\)，则

\[
F(a)=12-8c<0.
\tag{18}
\]

只剩 \((a,h,c)=(1,1,1)\)。这时

\[
F(X)=X^2-3X+6
\tag{19}
\]

的判别式为 \(-15\)，没有整数根，所以也不可能来自 (10)。

因此每个假想正整数解都满足

\[
F(0)>0,\qquad F(a)<0.
\tag{20}
\]

一个根严格位于 \((0,a)\)。另一方面 \(b\ge a\)，而 \(F(a)<0\) 又排除
\(b=a\)，所以 \(b>a\) 是较大根；由 (12) 得

\[
0<b'<a.
\tag{21}
\]

把 \(b\) 替换为 \(b'\) 仍满足同一个方程 (10)，但

\[
\max(a,b')=a<b=\max(a,b),
\]

与最小性矛盾。故 (10) 无正整数解，(7)、(3)、(2) 全部不可能。

## 5. 对最小高支撑 \(C=2\) 图表的推论

对任意核心素数 \(p\equiv1\pmod {24}\)，取

\[
U=\frac{p-1}{4}.
\tag{22}
\]

则

\[
R_2=2p-3=8U-1,
\qquad
K_2=\frac{(p-1)(2p-1)}4=U(8U+1).
\tag{23}
\]

由 (2)--(3) 得

\[
\boxed{
\text{每个 }H_2(p)\text{ 都 centered Type I miss}.}
\tag{24}
\]

因此 \(H_2(p)\) 无需先由有限盒计算分类成 F 或 G，便已经知道中心目标纤维为空。
F/G 只继续区分目标是否落在支撑生成子群中。

短关系容量定理给出的偶前驱与自然标记为

\[
E=2(p-1),
\qquad
n=p-1,
\qquad
\alpha=A_2=\frac{(p-1)(2p-1)}8.
\tag{25}
\]

又有

\[
\frac4n-\frac1\alpha
=\frac{R_2}{K_2}
=\frac4p-\frac1{pK_2}.
\tag{26}
\]

自然标记源非空当且仅当 \(R_2/K_2\) 可分成两个正单位分数。由 (2)，得到无条件
结论

\[
\boxed{
W_{\rm natural}(p-1,A_2)=\varnothing
\quad\text{对每个核心素数 }p.}
\tag{27}
\]

这严格加强了此前的条件句“若图表已经是 F/G miss，则自然标记源为空”。

## 6. 容量解释与边界

内部关系

\[
V=8U+1\equiv2\pmod{8U-1}
\tag{28}
\]

确实是一条短的同号差关系 \(V-2=R\)。但 centered Type I 需要的是两个
\(K=UV\) 支撑比值的反足和关系。式 (10)--(21) 证明，允许 \(U\) 与 \(V\)
的全部真因子后，这个符号缺口仍不能被吸收。

所以 \(C=2\) 边界现在同时具有：

1. complete-excess 候选全部严格上升；
2. 同图表唯一内部支撑位不能被 full-block 语法读取；
3. 内部关系确实产生 \(p-1\) 偶前驱；
4. 该关系的自然 marked source 全称为空。

本定理不排除其它 \(p-1\) 图表直接命中，也不排除改变标记、保留尾或正规形的
跨图表终端。后续的 rank-one 穷尽定理进一步证明：双尾保持 \(D\)-only 候选要么
重索引成另一张 centered Type I 终端，要么标记纤维严格为空。

聚焦验证：

~~~bash
python3 reproductions/type_i_high_support_c2_centered_vieta_no_go.py --verify
~~~

验证器核对 Vieta 多项式恒等式、少量 \(U\) 的反足/中心谱控制以及
\(p=73,97,193\) 的图表嵌入；有限控制只用于防止公式回归，不替代上述证明。
