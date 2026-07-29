---
kind: claim
claim_id: type-I-normal-ratio-two-nondegenerate-terminal-or-descent
title: Type I 比二命中的非退化偶终端或奇源递降二分
statement: 设 Type I 正规形满足 4K=pR+1，令 L=2K。若存在互素除子 a,b|L，使 a≡2b mod R、(a,b)≠(1,L) 且 a<2b，则 E=La/b 满足 1<E≤2L−2R、E|4K²、E≡1 mod R。令 n=(2L−E)/R，则 2≤n<p、E|nK；若 E 偶则得到偶源终端桥，若 E 奇则得到严格更小的奇源带标记递降边。相反，未排除退化对 (1,L) 时，比二残数碰撞只能给出 E=1、n=p；对 (2,1) 型碰撞则给出 E=2L、n=0，二者都不是目标引理所需的出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- normal-form
- terminal-bridge
- descent
- reverse-lift
- ratio-two
- nondegenerate
- parity
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-terminal-selector-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-29'
---

# Type I 比二命中的非退化偶终端或奇源递降二分

## 设置

沿用 Type I 正规形最大尾选择器的记号。固定一个正规形，使

$$
4K=pR+1,
\qquad L=2K,
\qquad R\text{ 为奇数}. \tag{1}
$$

考虑 $L$ 的互素除子对

$$
a,b\mid L,
\qquad (a,b)=1,
\qquad a\equiv2b\pmod R. \tag{2}
$$

令

$$
E=L\frac ab. \tag{3}
$$

这里的“非退化小侧命中”是指

$$
(a,b)\ne(1,L),
\qquad a<2b. \tag{4}
$$

第一条排除 $E=1$ 的原地命中，第二条排除 $E=2L$ 的零源边界。

## 二分引理

在 (1)--(4) 下，$E$ 为整数并满足

$$
1<E\le2L-2R,
\qquad E\mid L^2=4K^2,
\qquad E\equiv2L\equiv1\pmod R. \tag{5}
$$

置

$$
n=\frac{2L-E}{R}=\frac{4K-E}{R}. \tag{6}
$$

则

$$
2\le n<p,
\qquad E\mid nK, \tag{7}
$$

并且对原正规形的前两项，令 $\alpha=nK/E$，有严格源身份

$$
\frac4n
=\frac1\alpha+\frac1{ABC}+\frac1{ACH}. \tag{8}
$$

此外 $R$ 为奇数，故

$$
n\equiv E\pmod2. \tag{9}
$$

因此得到精确的析取：

* $E$ 偶时，(5) 是所需的偶因子终端证书；
* $E$ 奇时，(6)--(8) 是一个严格更小的奇源带标记递降边。

第二项应理解为**带标记**递降：它保留了两个正规形分母 $ABC,ACH$，所以在这条标记源态
上有明确的提升坐标；它不声称任意无标记的 $n$ 三项解都能提升回 $p$。

## 证明

由 $a,b\mid L$ 且 $(a,b)=1$，$E=La/b$ 为整数，并且

$$
\frac{L^2}{E}=\frac{Lb}{a}\in\mathbb Z,
$$

所以 $E\mid L^2=4K^2$。由 (2) 和 $(L,R)=1$，

$$
E\equiv L\,a\,b^{-1}\equiv2L\pmod R.
$$

再由 (1) 得 $2L=4K\equiv1\pmod R$。

因为 $(a,b)\ne(1,L)$ 且 $a,b\mid L$、$(a,b)=1$，有 $b<L$；$b$ 是 $L$ 的真除子，
故 $b\le L/2$。条件 $a<2b$ 给出正整数 $q$ 使

$$
2b-a=qR,
\qquad q\ge1.
$$

于是

$$
2L-E=L\frac{2b-a}{b}=L\frac{qR}{b}
\ge2R,
$$

得到 (5) 的上界。又 $E>1$ 且 $4K-1=pR$，所以

$$
0<4K-E<4K-1=pR,
$$

从而 (6) 给出 $2\le n<p$。

由 $E\equiv1\pmod R$ 可知 $(E,R)=1$。模 $E$ 有

$$
nR=4K-E\equiv4K\pmod E.
$$

乘以 $K$ 并使用 $E\mid4K^2$，得到 $E\mid nRK$；再约去与 $E$ 互素的 $R$，得
$E\mid nK$。代入 $\alpha=nK/E$ 即得 (8)。最后因 $R$ 奇、$2L$ 偶，(6) 两边模 $2$ 化简为
$n\equiv E\pmod2$，证毕。

## 退化边界及对密度路线的修正

在 Type I 情形，两个端点本来就总是满足残数命中：

$$
(a,b)=(1,L):
\quad E=1,\quad n=p,
$$

因为 $2L=4K\equiv1\pmod R$；以及

$$
(a,b)=(2,1):
\quad E=2L,\quad n=0.
$$

所以仅证明

$$
\mathcal D_R(L)\cap2\mathcal D_R(L)\ne\varnothing
$$

并不能给出终端或递降；它可能只重新发现上述端点。此前的普通半密度判据和本引理组合时，
必须把“非退化”与“小侧”作为独立目标。二进截断半密度判据由于排除了最高二进层的
$b=L$，会自动排除 $E=1$，但仍需检查 $a<2b$ 以排除大侧/零源边界。

该修正把当前可证明的局部路线写成

$$
\text{非退化小侧比二命中}
\Longrightarrow
\text{偶终端或奇源严格递降},
$$

而不是把残数碰撞本身误记为完整的混合终端选择器。全称难点仍是：对每个未被普通
Type II 覆盖的核心素数，选择一个正规形和一个满足 (4) 的非退化碰撞，或给出另一个
带严格势函数的递降出口。
