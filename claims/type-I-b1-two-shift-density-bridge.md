---
kind: claim
claim_id: type-I-b1-two-shift-density-bridge
title: 两条移位因子分支的B等于一上半区桥有二维筛残余
statement: 令T(X)计数p<=X、p=1 mod24的素数，要求(p+1)/2没有3 mod4素因子且(3p+1)/4没有2 mod3素因子。则T(X)=O(X/(log X)^2)。因此来自这两个移位因子分支的显式B=1上半区偶桥覆盖相对密度一的核心素数，且未覆盖集的筛界比任一单分支的O(X/(log X)^(3/2))更薄。
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
topics:
- type-I
- b1
- terminal-bridge
- upper-half-source
- sieve
- density
- p-plus-one
- three-p-plus-one
- proof-program
sources:
- paper: shute2022
  locator: Sections 5.2--5.5, especially equations (5.3.5)--(5.3.6) and Lemma 5.5.1 (printed p. 57)
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

# 两条移位因子分支的 \(B=1\) 二维筛残余

## 定理

令

\[
\begin{aligned}
T(X)=\#\{p\le X:\ &p\equiv1\pmod {24},\ p\text{ 为素数},\\
&\ell\nmid(p+1)/2\quad\text{对每个素数 }\ell\equiv3\pmod4,\\
&q\nmid(3p+1)/4\quad\text{对每个素数 }q\equiv2\pmod3\}.
\end{aligned}
\tag{1}
\]

则

\[
T(X)\ll\frac{X}{(\log X)^2}.
\tag{2}
\]

每个不被 \(T(X)\) 计数的核心素数均有一张严格上半区的 \(B=1\) Type I 偶终端桥：

- 第一行因子条件命中时，使用[来自 \(p+1\) 的桥](type-I-p-plus-one-b1-upper-bridge.md)；
- 第二行因子条件命中时，使用[来自 \((3p+1)/4\) 的桥](type-I-three-p-plus-one-b1-upper-bridge.md)。

所以这两条显式桥分支的共同残余是相对密度零，并有 (2) 的更强绝对上界。

## 筛法证明

写 \(p=24t+1\)。三个相关线性整数是

\[
24t+1,\qquad
\frac{p+1}{2}=12t+1,\qquad
\frac{3p+1}{4}=18t+1.
\tag{3}
\]

对每个素数 \(\ell>3\)，把局部禁根集写成

\[
\begin{aligned}
E_\ell^{(0)}
&=\{t\bmod\ell:24t+1\equiv0\pmod\ell\},\\
E_\ell^{(1)}
&=\begin{cases}
\{t\bmod\ell:12t+1\equiv0\pmod\ell\},&\ell\equiv3\pmod4,\\
\varnothing,&\ell\equiv1\pmod4,
\end{cases}\\
E_\ell^{(2)}
&=\begin{cases}
\{t\bmod\ell:18t+1\equiv0\pmod\ell\},&\ell\equiv2\pmod3,\\
\varnothing,&\ell\equiv1\pmod3,
\end{cases}\\
E_\ell&=E_\ell^{(0)}\cup E_\ell^{(1)}\cup E_\ell^{(2)}.
\end{aligned}
\]

三个根在 \(\ell>3\) 时两两不同：任意两条线性式的行列式绝对值属于
\(\{6,12\}\)。因此，令 \(\nu(\ell)=|E_\ell|\)，按 \(\ell\pmod {12}\)
分类的局部禁根数为

\[
\begin{array}{c|cccc}
\ell\pmod {12} & 1&5&7&11\\
\hline
\nu(\ell) & 1&2&2&3.
\end{array}
\tag{4}
\]

令

\[
\mathcal A_X=\{t\in\mathbb Z_{\ge0}:24t+1\le X\},
\qquad N_X=|\mathcal A_X|=\frac X{24}+O(1).
\tag{5}
\]

对仅含素因子 \(\ell>3\) 的平方自由数 \(d\)，令 Shute 筛模型中的乘法密度为

\[
\nu(d)=\prod_{\ell\mid d}\nu(\ell),\qquad
g(\ell)=\frac{\nu(\ell)}\ell,\qquad
g(d)=\prod_{\ell\mid d}g(\ell)=\frac{\nu(d)}d.
\tag{6}
\]

由 (4)，对每个筛素数都有 \(0\le g(\ell)\le3/\ell<1\)。定义

\[
\mathcal A_{X,d}
=\{t\in\mathcal A_X:t\bmod\ell\in E_\ell\text{ 对每个 }\ell\mid d\}.
\]

把每个 \(\ell\mid d\) 处的全部禁根作组合，中国剩余定理给出模 \(d\) 的精确
\(\nu(d)\) 个根。因此

\[
|\mathcal A_{X,d}|
=N_Xg(d)+r_d=N_X\frac{\nu(d)}d+r_d,
\qquad |r_d|\le\nu(d).
\tag{7}
\]

素数 \(2,3\) 不用放入筛素数集：(3) 中三个整数在模 \(2\) 时都为 \(1\)，在模
\(3\) 时也都为 \(1\)。现定义

\[
V(v)=\prod_{\substack{3<\ell<v\\ \ell\text{ 为素数}}}
\left(1-\frac{\nu(\ell)}\ell\right).
\tag{8}
\]

Montgomery--Vaughan 的 Corollary 11.21 对固定模数 \(12\) 给出 PNT-AP。
对其 \(\pi(x;12,a)\) 估计作分部求和，则每个
\(a\in\{1,5,7,11\}\) 都满足

\[
\sum_{\substack{\ell\le v\\ \ell\equiv a\pmod {12}}}\frac1\ell
=\frac14\log\log v+C_a+o(1)
=\frac14\log\log v+O(1).
\]

结合 (4)，得到

\[
\sum_{3<\ell<v}\frac{\nu(\ell)}\ell
=\frac{1+2+2+3}{4}\log\log v+O(1)
=2\log\log v+O(1),
\]

其中各处的 \(\ell\) 都只取素数。又因
\(\sum_\ell g(\ell)^2\le9\sum_\ell\ell^{-2}<\infty\)，对 (8) 取对数可得

\[
\log V(v)
=\sum_{3<\ell<v}\log(1-g(\ell))
=-2\log\log v+O(1),
\qquad
V(v)\asymp(\log v)^{-2}.
\tag{9}
\]

两侧比较并扩大一个固定常数 \(K\ge1\) 后，对所有 \(2\le w\le v\) 都有

\[
\frac{V(w)}{V(v)}
\le K\left(\frac{\log v}{\log w}\right)^2.
\tag{10}
\]

这正是 Shute 的 Lemma 5.5.1 所需的筛维 \(\kappa=2\) 正则性。取

\[
D=X^{1/3},\qquad
b=\left\lceil18+10\log K+2\right\rceil,
\qquad z=D^{1/b}.
\tag{11}
\]

这里 \(b\) 是与 \(X\) 无关的固定常数，引理中的参数为
\(\log D/\log z=b\ge9\kappa+1=19\)，而且

\[
e^{9\kappa-b}K^{10}=e^{18-b}K^{10}\le e^{-2}.
\tag{12}
\]

设 \(P(z)=\prod_{3<\ell<z}\ell\)，其中乘积只取素数，并令 \(S(X,z)\) 为
\(\mathcal A_X\) 中避开所有 \(3<\ell<z\) 禁根的整数数目。Shute 的上界基本筛引理
及其余项定义给出

\[
S(X,z)
\le N_XV(z)\left(1+e^{18-b}K^{10}\right)+R^+(D,z).
\tag{13}
\]

组合筛系数的绝对值不超过 \(1\)。由 (7) 及 \(\nu(\ell)\le3\)，

\[
\begin{aligned}
|R^+(D,z)|
&\le
\sum_{\substack{d\le D\\d\mid P(z)}}|r_d|\\
&\le \sum_{d\le D}\tau_3(d)
\le D(1+\log D)^2.
\end{aligned}
\tag{14}
\]

第二个不等式使用：对平方自由 \(d\)，
\(\nu(d)\le3^{\omega(d)}=\tau_3(d)\)；最后一个不等式可由对三元组
\(d_1d_2d_3\le D\) 逐层调和求和得到。因为 \(b\) 固定，有

\[
N_XV(z)\ll\frac{X}{(\log X)^2},
\qquad
R^+(D,z)\ll X^{1/3}(\log X)^2.
\tag{15}
\]

最后，若 (1) 中被计数的素数 \(p>z\)，则它的素性使 \(24t+1=p\)
避开第一个禁根，而 (1) 中两个全称条件使另两个线性式也避开所有筛根。
因而

\[
T(X)\le S(X,z)+O(z)
\ll\frac{X}{(\log X)^2},
\tag{16}
\]

因为 \(z=X^{1/(3b)}\) 和 (15) 中的余项都被右端吸收。最后仍用
Montgomery--Vaughan 的 Corollary 11.21，但这次取固定模数 \(24\)，得到

\[
\pi(X;24,1)\sim\frac{\operatorname{Li}(X)}{\varphi(24)}
=\frac{\operatorname{Li}(X)}8
\asymp\frac X{\log X}.
\]

与 (16) 相除，即得相对密度零的结论。

## 对全称目标的含义

该结论没有证明所有核心素数都命中两条桥中的一条。它只把当前精确 \(B=1\) 终端选择问题的
剩余集压缩为一个 \(O(X/\log^2X)\) 的可能无限集合。下一步必须利用这个残余的**共同因子限制**，
或者构造第三条不与前两条仅作有限并的自适应桥；单纯重复密度论证不能排除无限例外。

可复现检查：

~~~bash
python3 -m unittest \
  tests/test_type_i_p_plus_one_b1_upper_bridge.py \
  tests/test_type_i_three_p_plus_one_b1_upper_bridge.py -q
~~~
