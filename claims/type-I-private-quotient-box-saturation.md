---
kind: claim
claim_id: type-I-private-quotient-box-saturation
title: Type I 多私有因子商群指数盒的饱和判据
statement: 设 x=E 乘积 r_i^{b_i}，其中 r_i 为互异私有素数且 gcd(E,乘积 r_i)=1。若固定因子的平方除子残数 J=Pi_m(E^2) 已是子群，令 H=<J,r_1,...,r_k>、Q=H/J，并令 S_i={r_i^j J:0<=j<=2b_i}。则 x^2 的除子残数在 Q 中恰为 S_1...S_k；若该乘积集等于 Q 且目标 t=-1/4 属于 H，则必有 Type I 目标证书。更一般地，令 T 为乘积集稳定子群，Kneser 不等式 sum_i |S_iT|-(k-1)|T| >= |Q| 是饱和的充分条件；在中心化盒中，命中条件可精确降到 Q/T，且 T 非平凡时严格降低有限群阶。该判据严格推广一私有因子的三余类饱和，不证明全称混合终端选择器。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- divisor-residues
- private-factors
- quotient-box
- finite-exponent
- Kneser-theorem
- saturation
- obstruction
- mixed-selector
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: product-set-growth-context
visibility: public
last_checked: '2026-07-29'
---

# Type I 多私有因子商群指数盒的饱和判据

## 设置

令 \(m\equiv3\pmod4\) 为合法缺口，取

$$
x=E\prod_{i=1}^{k}r_i^{b_i},
\qquad
\gcd\left(E,\prod_i r_i\right)=1, \tag{1}
$$

其中 \(r_i\) 是互异素数，且所有数都与 \(m\) 互素。对正整数 \(N\) 写

$$
\Pi_m(N)=\{d\bmod m:d\mid N\}. \tag{2}
$$

假设固定因子的平方除子谱

$$
J=\Pi_m(E^2) \tag{3}
$$

已经是 \((\mathbb Z/m\mathbb Z)^\times\) 的子群。令

$$
H=\langle J,r_1,\ldots,r_k\rangle,
\qquad
Q=H/J, \tag{4}
$$

并记 \(\bar r_i=r_iJ\in Q\)。

对每个私有方向定义有限指数段

$$
S_i=\{\bar r_i^{\,j}:0\le j\le2b_i\}\subseteq Q,
\qquad
B=S_1S_2\cdots S_k. \tag{5}
$$

这里 \(B\) 是商群中的私有指数盒投影；它不要求各 \(S_i\) 或各 \(r_i\) 互素。

## 精确饱和定理

有精确的商群投影恒等式

$$
\boxed{
\Pi_m(x^2)\text{ 在 }Q\text{ 中的像}=B.
} \tag{6}
$$

特别地，若

$$
B=Q \tag{7}
$$

且目标残数

$$
t=-4^{-1}\pmod m
$$

属于 \(H\)，则

$$
t\in\Pi_m(x^2), \tag{8}
$$

从而存在 Type I 目标平方除子。目标除子取互补因子后可按标准正规化恢复
\(x=ABC\)、\(d=B^2C\) 的 Type I 证书。

因此，任意 Type I 状态的未命中必须满足至少一个精确缺口：

$$
t\notin H
\quad\text{或}\quad
\bar t\notin B,\qquad
\Delta_Q=|Q|-|B|>0. \tag{9}
$$

其中 \(\Delta_Q\) 是私有指数盒在稳定固定层之后的商群缺陷。

## Kneser 饱和充分条件

令

$$
T=\operatorname{Stab}_Q(B).
$$

多项积集 Kneser 不等式给出

$$
|B|
\ge
\sum_{i=1}^{k}|S_iT|-(k-1)|T|. \tag{10}
$$

所以可检验的饱和条件是

$$
\boxed{
\sum_{i=1}^{k}|S_iT|-(k-1)|T|
\ge |Q|
\Longrightarrow B=Q.
} \tag{11}
$$

在 \(T=\{1\}\) 的非周期情形，这简化为

$$
\sum_{i=1}^{k}|S_i|\ge |Q|+k-1. \tag{12}
$$

每个方向的大小可直接由商阶计算：

$$
|S_i|=\min\{2b_i+1,\operatorname{ord}_Q(\bar r_i)\}. \tag{13}
$$

因此 (11)--(13) 把“多个私有因子是否足以填满缺口”转化为有限的阶和预算，而不是
枚举所有 \(x^2\) 除子。

## 已有三余类判据的恢复

当 \(k=1\)、\(b_1=1\) 时，

$$
S_1=\{1,\bar r,\bar r^2\}.
$$

若 \(\operatorname{ord}_Q(\bar r)\le3\)，则 \(S_1=Q\)，(7)--(8) 恢复已有的
一私有因子三余类饱和判据。若固定层未饱和，则本定理不适用，正好保留此前的
“碰撞因子指数不足”分支。

## 线性源的中心化版本

对线性状态的目标 \(K=(pR+1)/4\)，把一个固定层与若干互异私有素因子写成

$$
K=N\prod_{i=1}^{k}q_i^{b_i},
\qquad
\gcd\left(N,\prod_iq_i\right)=1,
\qquad (K,R)=1,
\qquad
J=\mathcal C_R(N),\qquad
H=\langle J,q_1,\ldots,q_k\rangle. \tag{20}
$$

假设 \(J\) 是 \(H\) 的子群，并令 \(Q=H/J\)。定义中心化私有盒

$$
S_i^{\pm}
=\{(q_iJ)^z:-b_i\le z\le b_i\},
\qquad
B^{\pm}=S_1^{\pm}\cdots S_k^{\pm}. \tag{21}
$$

令 \(\pi_Q:H\to Q\) 为自然投影。则有精确恒等式

$$
\boxed{
\pi_Q\bigl(\mathcal C_R(K)\bigr)=B^{\pm}.
} \tag{22}
$$

这是前述中心化平方谱恒等式在分层分解下的直接投影：固定层的所有中心化指数落在
\(J\)，而每个 \(q_i\) 的中心化指数区间投影为 \(S_i^{\pm}\)。由于 \(J\) 是子群，
固定层的乘法不会再引入额外的商群缺口。

因此，只要

$$
-1\in H,\qquad B^{\pm}=Q, \tag{23}
$$

就得到

$$
-1\in\mathcal C_R(K). \tag{24}
$$

令 \(T^{\pm}=\operatorname{Stab}_Q(B^{\pm})\)，Kneser 给出

$$
|B^{\pm}|
\ge
\sum_i|S_i^{\pm}T^{\pm}|-(k-1)|T^{\pm}|. \tag{25}
$$

故右端至少为 \(|Q|\) 时，(23) 自动成立。命中后取互补因子可令
\(d\le K\)、\(d\equiv-K\pmod R\)；在线性源中同时取
\(E_0=sR+1\)，便得到原混合终端选择器所需的偶因子条件。

这个中心化版本与前面的目标侧版本互补：前者处理 \(d\mid K^2\) 的对称指数预算，
后者处理 \(e\mid x^2\) 的 Type I 目标除子。两者共同保留了“固定层缺陷”和“私有盒缺陷”
这两个可递降的状态量。

## 稳定子群商的精确递降

对中心化私有盒 \(B^{\pm}\) 令

$$
T^{\pm}=\operatorname{Stab}_Q(B^{\pm}),
\qquad
\pi:Q\longrightarrow Q/T^{\pm}. \tag{26}
$$

由于 \(1\in B^{\pm}\)，有

$$
T^{\pm}\subseteq B^{\pm},
\qquad
B^{\pm}T^{\pm}=B^{\pm}. \tag{27}
$$

从而对任意 \(y\in Q\) 有精确等价

$$
\boxed{
y\in B^{\pm}
\quad\Longleftrightarrow\quad
\pi(y)\in\pi(B^{\pm}).
} \tag{28}
$$

并且

$$
\pi(B^{\pm})=\pi(S_1^{\pm})\cdots\pi(S_k^{\pm}),
\qquad
\operatorname{Stab}_{Q/T^{\pm}}\bigl(\pi(B^{\pm})\bigr)=\{1\}. \tag{29}
$$

因此 \(-1\) 是否命中在商群中完全保真：

$$
-1\in B^{\pm}
\quad\Longleftrightarrow\quad
-T^{\pm}\in\pi(B^{\pm}). \tag{30}
$$

若 \(T^{\pm}\ne\{1\}\)，(26)--(30) 给出严格更小的有限群子问题；若
\(T^{\pm}=\{1\}\)，则原盒已经是无周期的，Kneser 的无周期增长界可直接施加。
这是一种商群层面的严格递降，不等同于把素数 \(p\) 或模数 \(R\) 变小；要完成全称
混合终端引理，还需证明该商群递降能够被提升为另一条可用的线性源状态，或排除所有
无周期缺陷盒。

## 素数阶无周期商的显式预算

若稳定子群商 Q/T^± 为奇素数阶循环群 C_ell，令

$$
\overline S_i=\pi(S_i^{\pm}),
\qquad
\overline B=\pi(B^{\pm}),
\qquad
\ell=|Q/T^{\pm}|. \tag{31}
$$

则素数阶循环群中的 Kneser（等价于 Cauchy--Davenport）给出

$$
|\overline B|
\ge
\min\left\{\ell,\sum_i|\overline S_i|-(k-1)\right\},
\qquad
|\overline S_i|=\min\{2b_i+1,\operatorname{ord}(\pi(q_iJ))\}. \tag{32}
$$

所以

$$
\sum_i|\overline S_i|\ge\ell+k-1
\quad\Longrightarrow\quad
\overline B=Q/T^{\pm}. \tag{33}
$$

特别地，在所有非平凡方向都未绕满 C_ell 时，若记
\(I=\{i:\pi(q_iJ)\ne1\}\)，则

$$
2\sum_{i\in I}b_i\ge\ell-1
\quad\Longrightarrow\quad
\overline B=Q/T^{\pm};
\qquad
\text{F 型未命中}\Longrightarrow 2\sum_{i\in I}b_i\le\ell-2. \tag{34}
$$

这给出了无周期商中的显式总指数预算；它仍是单状态条件，不自动产生跨模数的源下降。

## 证明

任意 \(d\mid x^2\) 可唯一写成

$$
d=d_E\prod_{i=1}^{k}r_i^{j_i},
\qquad
d_E\mid E^2,\quad0\le j_i\le2b_i. \tag{14}
$$

将 (14) 对 \(m\) 取残数并投影到 \(Q\)。固定部分 \(d_E\) 的残数属于 \(J\)，
而私有部分的所有可能残数恰为各 \(S_i\) 的乘积，故像包含于 \(B\)。
反向地，对任意 \(j_i\) 和任意 \(d_E\mid E^2\)，式 (14) 本身就是 \(x^2\) 的除子，
所以每个 \(B\) 中的类都被实现，得到 (6)。

若 \(B=Q\)，则 \(t\in H\) 的商类 \(\bar t\) 属于 \(B\)，与某个固定层残数相乘
即可得到 \(t\in\Pi_m(x^2)\)，证明 (8)。Kneser 的多因子形式直接应用于
\(S_1,\ldots,S_k\) 得到 (10)；若右端达到 \(|Q|\)，而 \(B\subseteq Q\)，则
必有 \(B=Q\)。式 (12)--(13) 是相应的无周期化简和循环子群指数段大小公式。证毕。

素数阶商中的多项积集不等式给出 (32)；每个方向的阶在 C_ell 中只能是 1 或 ell，
所以 (32) 的大小公式成立。若某个方向已经绕满，盒立即等于整个商群；否则对
I 中的每个方向有 |overline S_i|=2b_i+1，而其余方向贡献 1。代入 (33) 得到 (34)；
F 型未命中取其逆否命题即可。

**商群递降证明。** 对 (26)--(30)，盒 B^± 包含单位元且 T^± 稳定盒，所以得到 (27)。若某个元素的
商类属于 π(B^±)，可写成 y=bt，其中 b∈B^±、t∈T^±；由 (27) 即有
y∈B^±，故 (28) 成立。积集投影给出 (29) 的第一式。若商群中某个商类稳定
π(B^±)，则 B^±uT^±=B^±；两边基数相同且 B^±u⊆B^±，故 B^±u=B^±，
即 u∈T^±，得到 (29) 的平凡稳定子群。最后令 y=-1 即得 (30)。

## 对混合终端目标的作用

这张卡把 Type I 有限指数分支拆成两个可分别证明的对象：

1. **支撑逃逸**：证明 \(t=-1/4\) 属于固定层与私有方向生成的 \(H\)；
2. **商群饱和**：证明私有指数盒 \(B\) 填满目标所在的商群，或至少包含 \(\bar t\)。

在线性源的混合终端问题中，支撑逃逸可由二残数注入、二次互反拉回或高阶角色分析提供；
一旦同一正规形的目标侧满足 (8)，再结合已有的偶终端桥判据即可检查
\(E\equiv1\pmod R\)、\(E\le4K-2R\) 和偶性。因而后续真正的全称缺口被压缩为：
沿可达线性源状态，固定碰撞层是否最终饱和，或私有指数盒缺陷是否能转成严格递降。

本卡不声称 \(\Delta_Q\) 必为零，也不构造跨 \(R\) 的下降势函数；它是多私有因子有限指数
分支的精确结构定理。
