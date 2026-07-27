---
kind: claim
claim_id: type-II-growing-canonical-fan-superlog-tail
title: 对数对数增长的规范 Type II 扇具有超对数稀薄尾部
statement: 存在绝对常数 delta,c>0，使 H(X)=floor(delta log log X) 时，满足 p<=X、p=1 mod24 且前 H(X) 条平方自由规范 Type II 射线均失败的素数数目至多为 X exp(-c(log log X)^2)。因此存在一个明确增长的规范移位上界 H(X)=Theta(log log X)，在相对密度一意义下捕获核心素数，且失败集比任意固定对数幂更稀薄。该结论不排除无限个例外，也不提供逐点选择器。
claim_status: established
topics:
- type-II
- canonicalization
- sieve
- density
- growing-family
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: Appendix A, shifted-prime sieve methodology
  role: upper-bound-sieve-methodology
- paper: shute2022
  locator: Section 5.5, Lemma 5.5.1
  role: uniform-fundamental-lemma
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 对数对数增长的规范 Type II 扇具有超对数稀薄尾部

## 定理

对 $s\ge1$，写 $s=a_s^2c_s$，其中 $c_s$ 平方自由，并令

\[
M_s=4a_sc_s.
\]

令 $T_H(X)$ 计数满足 $p\le X$、$p\equiv1\pmod {24}$ 且前 $H$ 条规范移位
$s=1,\ldots,H$ 全部失败的素数。存在绝对常数 $\delta,c>0$，使

\[
H=\left\lfloor\delta\log\log X\right\rfloor
\quad\Longrightarrow\quad
T_H(X)\ll X\exp\left(-c(\log\log X)^2\right). \tag{1}
\]

特别地，这个失败集是 $O_A(X/(\log X)^A)$，其中 $A>0$ 任意但固定。除以核心
素数数目 $\asymp X/\log X$ 后，前 $H(X)$ 条规范射线覆盖相对密度一的核心素数。

## 失败的筛表述

固定 $s$。如果该射线失败，则 $p+4s$ 的所有素因子残数落入
$U(M_s)$ 的一个半大小横截面 $T_s$。由
`type-II-ac-rays-superlog-residual` 的对合论证，$T_s$ 的选择数至多为

\[
2^{\varphi(M_s)/2}. \tag{2}
\]

对 $1\le s\le H$ 取并，`type-II-canonical-fan-uniform-sieve-interface` 给出

\[
\#\{(T_1,\ldots,T_H)\}\le \exp(C_0H^2) \tag{3}
\]

以及 $M_s\mid4s$。故只需对一个固定横截面系统作上界筛，再乘以 (3)。

写 $p=24t+1$。对不整除 $24\prod_{s<t}(s-t)$ 的素数 $\ell>4H$，要保留这个
横截面系统，必须避开：

1. 一个根 $24t+1\equiv0\pmod\ell$；
2. 对每个 $s$，当 $\ell\bmod M_s\notin T_s$ 时的一个根
   $24t+1+4s\equiv0\pmod\ell$。

这些根互异。令 $\nu(\ell)$ 为禁根数。因为每个横截面的补集在 $U(M_s)$ 中占一半，
而 $M_s\le4H$，Siegel--Walfisz 范围内的算术级数 Mertens 估计一致给出

\[
\sum_{\ell\le z}\frac{\nu(\ell)}{\ell}
=\left(1+\frac H2\right)\log\log z
+O(H^2+H\log H), \tag{4}
\]

只要 $H\ll\log\log z$。对数展开中的二次项满足

\[
\sum_{\ell>4H}\frac{\nu(\ell)^2}{\ell^2}=O(H^2). \tag{5}
\]

因而相应筛积满足

\[
V(z)\ll
\exp(C_1H^2+C_1H\log H)(\log z)^{-1-H/2}. \tag{6}
\]

这里的常数绝对，不依赖横截面系统。

## 有参数的统一上界筛

这里必须处理筛维随 $H$ 变化的常数，不能直接引用固定维数的上界筛。对一个固定
横截面系统，令 $\mathcal A=\{1\le t\le X/24\}$，并令 $E_\ell$ 是上文列出的
$\nu(\ell)$ 个禁余类。对平方自由 $d$（其素因子均大于 $4H$）有精确计数

\[
\#\{t\in\mathcal A:t\in E_d\}
=\frac{X}{24}\frac{\nu(d)}d+r_d,\qquad |r_d|\le\nu(d), \tag{7}
\]

其中 $\nu(d)=\prod_{\ell\mid d}\nu(\ell)$。因此局部密度
$g(d)=\nu(d)/d$ 是乘性的。

由 (4)--(6)，令 $\kappa=1+H/2$，任意 $2\le w\le z$ 都有

\[
\frac{V(w)}{V(z)}
\le K_H\left(\frac{\log z}{\log w}\right)^\kappa,
\qquad
\log K_H\ll H^2+H\log H. \tag{8}
\]

这是基本筛引理的正则性假设。注意 (8) 的 $K_H$ 不必有界；它的明确大小正是
统一化所需保留的成本。

取

\[
D=X^{1/3},\qquad
s=\left\lceil 9\kappa+10\log K_H+2\right\rceil,\qquad
z=D^{1/s}. \tag{9}
\]

则 $s\ll H^2+H\log H$。`shute2022` 的 Lemma 5.5.1 给出上界筛系数，
其主项乘子至多 $2$；该结论只要求 $s\ge9\kappa+1$，而 (9) 还使
$e^{9\kappa-s}K_H^{10}\le e^{-2}$。

余项也可直接一致估计。该基本筛的组合系数绝对值至多一，且

\[
\nu(d)\le(H+1)^{\omega(d)}\le\tau_{H+1}(d).
\]

由 $H+1$ 重除数函数的逐层双曲线求和，

\[
\sum_{d\le D}\tau_{H+1}(d)
\le D(1+\log D)^H. \tag{10}
\]

所以单个横截面系统的筛余数至多

\[
\ll X\exp(C_2H^2+C_2H\log H)
\left(\frac{H^2}{\log X}\right)^{1+H/2}
+X^{1/3}\exp\bigl(H\log\log X+O(H^2+H\log H)\bigr). \tag{11}
\]

这里用到了 $\log z=(\log X)/O(H^2+H\log H)$；把多出的
$H\log H$ 吸收到指数成本中即可。乘以 (3)，得到

\[
\begin{aligned}
T_H(X)\ll{}&
X\exp(C_3H^2+C_3H\log H)
\left(\frac{H^2}{\log X}\right)^{1+H/2}\\
&+X^{1/3}\exp\bigl(H\log\log X+C_3H^2+C_3H\log H\bigr).
\end{aligned} \tag{12}
\]

令 $L=\log\log X$、$H=\lfloor\delta L\rfloor$。式 (12) 第一项的指数主项为

\[
C_3\delta^2L^2-\frac{\delta}{2}L^2+O(L\log L).
\]

选取充分小的绝对 $\delta>0$，即得到 (1)。第二项相对于
$X\exp(-cL^2)$ 额外含有 $X^{-2/3}$，所以在此范围内更小。

## 范围检查

式 (4) 所需的模数只有 $M_s\le4H=O(\log\log X)$，因此远在
Siegel--Walfisz 的多对数模数范围内。`type-II-canonical-fan-uniform-sieve-interface`
中的总模数和横截面熵界保证了 (3) 的组合成本；筛法本身只按每个单独 $M_s$ 的
素数残数类使用 (4)，不需要把所有模数相乘后再对那个巨模数调用素数定理。式
(7)--(12) 还检查了此前缺失的筛维、正则性常数和截断余项依赖。

## 边界

这是密度结果，不是 Erdős--Straus 猜想的证明。它允许一个极稀薄但无限的例外集；
也没有给出对给定 $p$ 如何确定一个成功 $s$ 的算法性证明。

固定十四移位扇的条件性逃逸边界不与本定理冲突：这里 $H(X)$ 无界增长。
仍需进一步的因子选择、递降或新的结构定理，才能把 (1) 升级为逐点覆盖。
