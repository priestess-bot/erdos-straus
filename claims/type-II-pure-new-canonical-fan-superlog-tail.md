---
kind: claim
claim_id: type-II-pure-new-canonical-fan-superlog-tail
title: 任意固定对数对数幂规范移位扇的纯新失败集具有超对数稀薄尾部
statement: 对任意固定 alpha>0，令 L=log log X、H=floor(L^alpha)。对每个 20<=s<=H 写 s=a_s^2 c_s，其中 c_s 平方自由。满足 p<=X、p=1 mod24 且对所有这些 s 都不存在 H19 新素数 ell 使 ell|p+4s、ell=-1 mod4a_sc_s 的素数数目为 O_alpha(X exp[-c_alpha L log L])。因此相对密度一的核心素数具有纯新单素因子 Type II 证书，其规范移位不超过 (log log X)^alpha。常数和起始阈值依赖固定的 alpha；本结论不对 alpha 趋于零一致，也不排除无限例外。
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
topics:
- type-II
- canonicalization
- sieve
- density
- pure-new-factor
- growing-family
- short-certificate
- proof-program
sources:
- paper: montgomery_vaughan2007
  locator: Chapter 11, Corollaries 11.19 and 11.21 (published chapter pp. 381--382)
  role: uniform-Siegel-Walfisz-input
- paper: shute2022
  locator: Section 5.5, Lemma 5.5.1 (printed p. 57)
  role: explicit-growing-dimension-fundamental-lemma
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 任意固定对数对数幂规范移位扇的纯新失败集具有超对数稀薄尾部

## 定理

令

\[
L=\log\log X.
\]

固定任意 \(\alpha>0\)，并取

\[
H=\left\lfloor L^\alpha\right\rfloor. \tag{1}
\]

对每个 \(20\le s\le H\)，唯一写成

\[
s=a_s^2c_s,\qquad c_s\text{ 平方自由},\qquad M_s=4a_sc_s. \tag{2}
\]

令

\[
\mathcal O_p=\bigcup_{1\le t\le19}\operatorname{Supp}(p+4t).
\]

记 \(E_{\mathrm{can,new}}(X,H)\) 为满足 \(p\le X\)、
\(p\equiv1\pmod{24}\) 的素数 \(p\) 中，对所有 \(20\le s\le H\) 都不存在
素数 \(\ell\) 使

\[
\ell\mid p+4s,\qquad
\ell\equiv-1\pmod{M_s},\qquad
\ell\notin\mathcal O_p. \tag{3}
\]

则存在 \(c_\alpha>0\)，使对充分大的 \(X\)，

\[
E_{\mathrm{can,new}}(X,H)
\ll_\alpha X\exp\bigl(-c_\alpha L\log L\bigr). \tag{4}
\]

常数 \(c_\alpha\)、隐常数和 \(X\) 的起始阈值允许依赖固定的 \(\alpha\)。式 (4)
不是对 \(\alpha\to0\) 的一致估计。

## 证书翻译与新性

对非例外点取满足 (3) 的 \(s,\ell\)，并令

\[
K=\frac{\ell+1}{M_s},\qquad h=\ell.
\]

于是

\[
h=4a_sc_sK-1,\qquad h\mid Kp+a_s. \tag{5}
\]

第二个整除关系来自 \(h\mid p+4a_s^2c_s\) 以及
\(4a_sc_sK\equiv1\pmod h\)；这里
\(\gcd(4a_sc_s,h)=1\)，因为 \(h\equiv-1\pmod{4a_sc_s}\)。若 \(p>4H\)，则
\(p>4a_s^2c_s\)，所以 Type II 射线的序条件自动成立。由
[Type II 原始射线证书](type-II-raw-ray-certificate.md)，(5) 恢复一张合法 Type II
证书。

下面只筛大于

\[
Y=\exp(H^2) \tag{6}
\]

的素数。充分大的 \(H\) 下有 \(Y>4H\)。若 \(\ell>Y\) 同时整除
\(p+4s\) 与某个 \(p+4t\)，其中 \(1\le t\le19\)，则

\[
\ell\mid4(s-t),\qquad 0<|4(s-t)|<4H<\ell,
\]

矛盾。因此筛出的 \(\ell\) 自动不属于 \(\mathcal O_p\)。同一个 \(\ell>Y\)
对应的不同移位根也两两不同；零根与移位根若重合，则
\(\ell\mid4s\)，同样与 \(0<4s\le4H<\ell\) 矛盾。

## 筛维与一致素数倒数和

写 \(p=24u+1\)，并精确定义筛序列

\[
\mathcal A_X=\{u\in\mathbb Z:0\le u<X/24\},\qquad
N=\lvert\mathcal A_X\rvert\asymp X. \tag{7}
\]

对每个 \(\ell>Y\)，定义禁根数

\[
\nu_H(\ell)
=1+\#\{20\le s\le H:\ell\equiv-1\pmod{M_s}\}. \tag{8}
\]

第一项对应 \(p\equiv0\pmod\ell\)，其余各项对应
\(p\equiv-4s\pmod\ell\)。上一节说明这些根精确地互不相同。

令

\[
A_H=\sum_{s=20}^{H}\frac1{\varphi(M_s)},\qquad
\kappa_H=1+A_H. \tag{9}
\]

因为 \(M_s=4s/a_s\le4s\)，有初等下界

\[
A_H\ge\frac14\sum_{s=20}^{H}\frac1s
\ge\frac14\log H-O(1), \tag{10}
\]

同时粗界 \(\kappa_H\le H\) 足够用于下面的参数选择。

对任意 \(v\ge Y\)，有 \(M_s\le4H\le\log v\)。固定 Siegel--Walfisz 中的
指数参数 \(A=1\)，其 \(\pi(t;M_s,-1)\) 版本便对所有 \(t\ge Y\) 和相关模数一致
成立。对素数计数作分部求和时，直接误差为
\(O(H e^{-c_1H})\)；缩小绝对常数 \(c>0\) 后，得到

\[
\sum_{\substack{Y<\ell\le v\\
\ell\equiv-1\pmod{M_s}}}\frac1\ell
=\frac1{\varphi(M_s)}
\log\frac{\log v}{\log Y}+O(e^{-cH}), \tag{11}
\]

其中误差对 \(20\le s\le H\) 一致。把 (11) 对 \(s\) 求和并加上普通素数
倒数和，再次缩小 \(c\) 以吸收外层的 \(H\)，便有

\[
\sum_{Y<\ell\le v}\frac{\nu_H(\ell)}\ell
=\kappa_H\log\frac{\log v}{\log Y}+O(1). \tag{12}
\]

这里的误差常数是绝对的。另由 \(\nu_H(\ell)\le H\)，

\[
\sum_{\ell>Y}\frac{\nu_H(\ell)^2}{\ell^2}
\ll\frac{H^2}{Y}=o(1). \tag{13}
\]

令

\[
\mathcal P_Y=\{\ell:\ell\text{ 为素数且 }\ell>Y\},\qquad
g(\ell)=\frac{\nu_H(\ell)}{\ell}.
\]

于是 \(0\le g(\ell)<1\)。这正是 Shute 基本引理允许的任意筛素数集；截去
\(\ell\le Y\) 不改变引理的形式。定义

\[
V_H(v)=\prod_{Y<\ell<v}\left(1-\frac{\nu_H(\ell)}\ell\right),
\]

并在 \(v\le Y\) 时令 \(V_H(v)=1\)。由 (12)、(13) 展开对数可得

\[
\log V_H(v)
=-\kappa_H\log\frac{\log v}{\log Y}+O(1),
\]

其中误差是绝对的，因而有双边估计

\[
V_H(v)\asymp
\left(\frac{\log Y}{\log v}\right)^{\kappa_H}
\quad(v\ge Y). \tag{14}
\]

其中比较常数是绝对的。特别地，对所有 \(2\le w\le v\)，

\[
\frac{V_H(w)}{V_H(v)}
\le K_0\left(\frac{\log v}{\log w}\right)^{\kappa_H}. \tag{15}
\]

这里 \(K_0\ge1\) 是绝对常数。若 \(w\ge Y\)，式 (15) 直接来自 (14)；若
\(w<Y\)，则使用 \(V_H(w)=1\) 以及
\(\log w\lelog Y\)。这一步给出了增长筛维基本引理所需的全部区间正则性，而不只是
终点处的单边筛积估计。

## 显式增长维数上界筛

对仅含 \((Y,z)\) 中素因子的平方自由 \(d\)，令
\(\mathcal A_d\subseteq\mathcal A_X\) 为落在对应禁根中的元素。中国剩余定理给出

\[
\lvert\mathcal A_d\rvert
=N\frac{\nu_H(d)}d+r_d,\qquad |r_d|\le\nu_H(d), \tag{16}
\]

其中 \(\nu_H(d)=\prod_{\ell\mid d}\nu_H(\ell)\)。取

\[
D=X^{1/3},\qquad
b=\left\lceil9\kappa_H+10\log K_0+2\right\rceil,\qquad
z=D^{1/b}. \tag{17}
\]

由 \(b=O(\kappa_H)\)、\(\kappa_H\le H\)，对 (1) 中每个固定的
\(\alpha>0\) 都有 \(H^3=o(\log X)\)，因而充分大的 \(X\) 下 \(z>Y\)。
Shute 的显式基本筛引理中，主项相对误差为

\[
e^{9\kappa_H-b}K_0^{10}\le e^{-2}. \tag{18}
\]

此外 \(\nu_H(d)\le H^{\omega(d)}\le\tau_H(d)\)，逐层调和求和给出

\[
\sum_{d\le D}\nu_H(d)
\le D(1+\log D)^H. \tag{19}
\]

将 Shute 引理用于质量为 \(N\) 的序列 \(\mathcal A_X\)。由 (14)--(19)，再用
\(N\asymp X\)，并把被零根误删的 \(Y<p=\ell<z\) 单独计入，得到

\[
E_{\mathrm{can,new}}(X,H)
\ll X\left(\frac{C\kappa_HH^2}{\log X}\right)^{\kappa_H}
+D(1+\log D)^H+O(z). \tag{20}
\]

## 渐近收口

由 (1)、(10) 及 \(\kappa_H\le H\)，

\[
\log\left(\frac{C\kappa_HH^2}{\log X}\right)
\le-L+O_\alpha(\log L),
\]

而

\[
\kappa_H\ge\frac{\alpha}{4}\log L-O(1).
\]

所以 (20) 的第一项至多为

\[
X\exp\bigl(-c_\alpha L\log L\bigr)
\]

且 \(c_\alpha>0\)。另一方面，

\[
\log\bigl(D(1+\log D)^H\bigr)
\le\frac13\log X+O(HL),
\]

其中 \(HL=o(\log X)\)；同时 \(z\le X^{1/3}\)。这两项都严格小于所需上界，
从而证明 (4)。对证书结论还需补计 \(p\le4H\) 的 \(O(H)\) 个小点，这同样被
(4) 吸收。

## 推进边界

旧版本只取 \(H=\lfloor\delta L\rfloor\)，还从 \(4H\) 起直接套用算术级数
Mertens 估计，并只写出了筛积的终点上界。改从 \(Y=\exp(H^2)\) 起筛后，
Siegel--Walfisz 的模数范围、双边筛积估计和全部 \(w\)-区间正则性同时闭合；因此
\(\delta\) 无需充分小，并可强化为任意固定 \(\alpha>0\) 的 (1)。

这是密度定理，不是逐点选择器或严格递降引理。它允许极稀薄但可能无限的例外集合，
也不提供对单个例外素数选取 \(s\) 的统一规则。全称证明仍需处理真实
\(E_{\mathrm{can,new}}(X,H)\) 中的每个点。

独立复核核对了 (11) 的一致模数范围、(15) 的低端分支、Shute 引理中的
\(e^{9\kappa-b}K^{10}\) 依赖以及 (19) 的余项。现有复现程序只检查规范分解、
新性守卫、禁根互异性和倒数质量；它不以有限测试替代上述解析证明。

## 有限复现

~~~bash
python3 reproductions/type_ii_pure_new_canonical_fan_sieve.py \
  --bounds 50 100 1008 \
  --prime-bound 100000 \
  --output reproductions/type-ii-pure-new-canonical-fan-sieve-results.json
python3 -m unittest tests/test_type_ii_pure_new_canonical_fan_sieve.py -q
~~~
