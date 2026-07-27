---
kind: claim
claim_id: shifted-quadratic-tail-opposite-divisor-pair
title: 缩放平方尾的反向普通除子对判据
statement: 在平移平方外源正规形中，gcd(L,t)=1。存在平方尾 f|L^2 使 f=-L mod t，当且仅当存在普通除子 a,b|L 使 a=-b mod t。故内层选择等价于普通除子残数集 Pi_t(L) 与其负集相交。
claim_status: established
topics:
- type-I
- descent
- external-source
- divisor-residues
- factorization
- parametrization
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 缩放平方尾的反向普通除子对判据

在[缩放平方尾正规形](shifted-quadratic-tail-normalization.md)中，内层尾存在当且仅当

$$
f\mid L^2,\qquad f\equiv-L\pmod t,
$$

其中 $\gcd(L,t)=1$。这个条件等价于

$$
\exists a,b\mid L\quad\text{使}\quad a\equiv-b\pmod t. \tag{1}
$$

换言之，若

$$
\Pi_t(L)=\{d\bmod t:d\mid L\},
$$

则完整平方尾的精确判据是

$$
\Pi_t(L)\cap(-\Pi_t(L))\ne\varnothing. \tag{2}
$$

## 证明

若 $f\mid L^2$ 且 $f\equiv-L\pmod t$，令 $g=\gcd(f,L)$，并设

$$
a=\frac{f}{g},\qquad b=\frac{L}{g}.
$$

由 $f\mid L^2$ 可知 $a,b\mid L$。又 $f/L=a/b$ 在模 $t$ 下有定义，故
$f\equiv-L$ 等价于 $a\equiv-b$。

反之，若 $a,b\mid L$ 且 $a\equiv-b\pmod t$，令

$$
f=\frac{La}{b}.
$$

因为 $b\mid L$，$f$ 为整数；逐素因子指数可见 $f\mid L^2$。在模 $t$ 下，
$fb=La\equiv-Lb$，再由 $b$ 为单位得到 $f\equiv-L$。这与平方尾正规形完全等价。

该重写没有降低一般性：两亿压力集中的25条平方必要状态仍需要其普通除子残数集与负集的
非平凡交点。但它把“平方因子指数”转化为一对普通除子的差集问题，使 Kneser、加法组合和
乘法子群的交集工具可以直接作用于内层选择器。

## 有界有符号指数盒形式

更具体地，若

$$
L=\prod_{i=1}^r \ell_i^{e_i},
$$

定义其有符号除子商盒为

$$
\Delta_t(L)=
\left\{\prod_{i=1}^r\ell_i^{z_i}\bmod t:-e_i\le z_i\le e_i\right\}.
\tag{3}
$$

则 (1)--(2) 还等价于

$$
-1\in\Delta_t(L). \tag{4}
$$

事实上，对任意坐标向量 $z$，取

$$
a=\prod_{z_i>0}\ell_i^{z_i},\qquad
b=\prod_{z_i<0}\ell_i^{-z_i}.
$$

则 $a,b\mid L$ 且 $a/b=\prod_i\ell_i^{z_i}$。反过来，约去任意一对普通除子
$a,b$ 的公因子后，其指数差自然落在区间 $[-e_i,e_i]$。所以 (4) 是精确而非仅充分的
重写。

这给出一个与“平方尾”无关的内层目标：不是证明整个由素因子生成的子群含有 $-1$，而是
证明 $-1$ 落入各生成元只有有限指数预算的对称乘积盒。特别地，支持度为 $h$ 的证书正是
只有 $h$ 个坐标 $z_i$ 非零的 (4) 中表示；该量可用于严格检验任何低支持度选择器。

## 半密度充分条件

还存在一个不依赖素因子个数的直接充分条件。令

$$
D=\Pi_t(L)\subseteq(\mathbb Z/t\mathbb Z)^\times.
$$

若

$$
|D|>\frac{\varphi(t)}2, \tag{5}
$$

则完整平方尾必存在。确实，若 $D\cap(-D)$ 为空，则这两个同样大小的集合在单位群中不交，
从而 $2|D|\le\varphi(t)$，与 (5) 矛盾。由 (2) 即得结论。

条件 (5) 只是充分而非必要：低密度的 $D$ 仍可能恰含一对相反除子。因此它适合作为分层
选择器的第一层，失败时才需要分析有符号指数盒的精细结构。

## 对称盒饱和充分条件

令

$$
H_t(L)=\langle\ell_1,\ldots,\ell_r\rangle
\le(\mathbb Z/t\mathbb Z)^\times.
$$

若

$$
-1\in H_t(L),\qquad \Delta_t(L)=H_t(L), \tag{6}
$$

则完整平方尾必存在。第一条件把目标置于实际生成的子群中，第二条件说明每个该子群元素
都已由预算 $[-e_i,e_i]$ 的有符号指数表示；因此特别有 $-1\in\Delta_t(L)$，再由 (4)
即得尾证书。

这比半密度条件强：它允许 $\Pi_t(L)$ 和 $-\Pi_t(L)$ 都远小于单位群的一半，只要求其
对称商集已经填满相关子群。它仍只是充分条件；若 (6) 失败，不能推出 $-1$ 不在
$\Delta_t(L)$。

## 源因子完成充分条件

在平移平方外源正规形中写

$$
N=dt+1,\qquad L=kN,\qquad 4k\equiv1\pmod t.
$$

若存在正整数分解

$$
N=uvw
$$

使

$$
u^2v+4\equiv0pmod t, \tag{7}
$$

则完整平方尾必存在。事实上，取

$$
a=uk,\qquad b=w.
$$

两者均整除 $L$。由 $N\equiv1$ 和 $4k\equiv1\pmod t$，有

$$
4uv(a+b)=4u^2vk+4uvw\equiv u^2v+4\equiv0pmod t.
$$

故 $a\equiv-b\pmod t$，再由 (1) 得到尾证书。

条件 (7) 是一个可直接从归一化源 $N$ 的因子分解验证的三块完成规则。它既不要求
$\Delta_t(L)$ 填满子群，也不要求补集奇偶性，因此为上述两层失败时提供了不同的结构入口。

## 双侧有界接口完成条件

更一般地，设

$$
k=\alpha r\beta,\qquad N=\gamma z\delta,
$$

其中各块为正整数。若

$$
4rz(\beta\delta)^2+1\equiv0pmod t, \tag{8}
$$

则取

$$
a=\alpha\gamma,\qquad b=\beta\delta
$$

便得到反向普通除子对。因为 $kN=abrz\equiv1/4pmod t$，从而

$$
4brz(a+b)=4abrz+4b^2rz
\equiv1+4rz(\beta\delta)^2\equiv0pmod t.
$$

在实际选择器中可额外限制 $\beta$ 与 $\delta$ 分别为 $1$ 或单个素数幂；这使 $b$ 最多
跨越 $k,N$ 两侧的两个素数幂接口，仍保留 (8) 的完整证明。该限制不把一般反向对问题
自动化，而是一个可检验的受限双侧完成族。
