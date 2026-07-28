---
kind: claim
claim_id: type-I-b1-three-factor-sieve-bridge
title: 三条移位因子 B 等于一桥的六分之十三维筛残余
statement: 令 T7(X) 计数 p<=X、p=1 mod24 的素数，要求 (p+1)/2 无三模四素因子、(3p+1)/4 无二模三素因子且 (7p+1)/4 无五模七素因子。则 T7(X)=O(X/(log X)^(13/6))。三种任一因子条件命中时均有显式 B=1 上半区偶终端桥，故共同未覆盖集相对核心素数密度为零。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- b1
- terminal-bridge
- sieve
- density
- p-plus-one
- three-p-plus-one
- seven-p-plus-one
sources:
- paper: shute2022
  locator: Sections 5.2--5.5, especially equations (5.3.5)--(5.3.6) and Lemma 5.5.1
  role: explicit-fixed-dimension-upper-bound-sieve
- paper: montgomery_vaughan2007
  locator: Chapter 11, Corollaries 11.19/11.21
  role: fixed-modulus-PNT-in-arithmetic-progressions
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 三条移位因子 (B=1) 桥的 (13/6) 维筛残余

令 (T_7(X)) 计数满足下列条件的核心素数 (p\le X)：

\[
\begin{aligned}
&\ell\nmid\frac{p+1}{2}
&&\text{对每个 }\ell\equiv3\pmod4,\\
&q\nmid\frac{3p+1}{4}
&&\text{对每个 }q\equiv2\pmod3,\\
&r\nmid\frac{7p+1}{4}
&&\text{对每个 }r\equiv5\pmod7.
\end{aligned} \tag{1}
\]

则

\[
T_7(X)\ll\frac{X}{(\log X)^{13/6}}. \tag{2}
\]

前两条因子条件分别由[\(p+1\) 桥](type-I-p-plus-one-b1-upper-bridge.md)和
[\((3p+1)/4\) 桥](type-I-three-p-plus-one-b1-upper-bridge.md)终端化；第三条的补集由
[\(R=7\) 桥](type-I-seven-p-plus-one-r7-b1-upper-bridge.md)终端化。因此三条桥的共同未覆盖集
不仅相对密度为零，而且满足 (2)。

## 筛维计算

写 (p=24t+1)。除去不影响渐近的素数 (2,3,7)，四个线性式是

\[
L_0=24t+1,
\qquad L_1=12t+1,
\qquad L_2=18t+1,
\qquad L_3=21t+1. \tag{3}
\]

这里 ((7p+1)/4=2L_3)，所以第三条中的奇素因子条件恰是 (L_3) 的条件。对每个
\(\ell>7\)，这四个式的根两两不同：任意两条的系数行列式绝对值属于

\[
\{3,6,9,12\}. \tag{4}
\]

令 \(\nu(\ell)\) 是素性和三条禁止因子条件共同排除的根数，则

\[
\nu(\ell)=1+mathbf1_{\ell\equiv3\ (4)}
 +\mathbf1_{\ell\equiv2\ (3)}
 +\mathbf1_{\ell\equiv5\ (7)}. \tag{5}
\]

固定模数 (84) 的 PNT-AP 与分部求和给出

\[
\sum_{\ell<v}\frac{\nu(\ell)}\ell
=\left(1+\frac12+\frac12+\frac16\right)\log\log v+O(1)
=\frac{13}{6}\log\log v+O(1). \tag{6}
\]

因此

\[
V(v)=\prod_{7<\ell<v}\left(1-\frac{\nu(\ell)}\ell\right)
\asymp(\log v)^{-13/6}. \tag{7}
\]

其余步骤与[两因子二维筛](type-I-b1-two-shift-density-bridge.md)相同：对平方自由 (d)，
CRT 精确给出 \(\nu(d)\) 个根，取 (D=X^{1/3})，并取固定的
\(b\ge9\cdot(13/6)+1\)、\(z=D^{1/b}\)。上界基本筛引理适用。这里

\[
\nu(d)\le4^{\omega(d)}\le\tau_4(d),
\qquad
\sum_{d\le D}\tau_4(d)\ll D(1+\log D)^3, \tag{8}
\]

故余项为 \(O(X^{1/3}(\log X)^3)\)，被 (2) 吸收。避开 (1) 的素数必落在该筛余集，
从而得到 (2)。

由于核心素数个数为 \(\asymp X/\log X\)，共同残余相对于核心素数的比例为
\(O((\log X)^{-7/6})\)。这仍不是全称证明：筛余可能无限，且 (2) 不能构造每个残余的
替代桥。但它把已知显式 (B=1) 分支的绝对筛指数由 (2) 提升到 (13/6)。

~~~bash
python3 -m unittest tests.test_type_i_seven_p_plus_one_r7_b1_upper_bridge -q
~~~
