---
kind: claim
claim_id: type-II-pure-new-square-ray-superlog-tail
title: 增长平方移位上的纯新单素因子 Type II 射线具有超对数稀薄尾部
statement: 存在绝对常数 c>0。令 L=log log X、R=floor(sqrt(L))，并令 E(X) 计数 p<=X、p=1 mod24 的素数，使得对每个 5<=r<=R 都不存在素数 q 满足 q|p+4r^2、q=-1 mod4r，且 q 不整除任一 p+4t (1<=t<=19)。则对充分大 X，有 E(X)<<X exp(-c L log L)。每个非例外 p 因而有一张除子 r^2<=log log X 的纯新单素因子 Type II 证书。这不排除无限例外。
claim_status: established
topics:
- type-II
- sieve
- density
- pure-new-factor
- canonicalization
- growing-family
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: Appendix A, shifted-prime sieve methodology
  role: upper-bound-sieve-methodology
- paper: shute2022
  locator: Section 5.5, Lemma 5.5.1
  role: uniform-fundamental-lemma
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-27'
---

# 增长平方移位上的纯新单素因子 Type II 射线具有超对数稀薄尾部

## 定理

记 H19 的旧因子集合为

\[
\mathcal O_p=\bigcup_{1\le t\le19}\operatorname{Supp}(p+4t).
\]

令

\[
L=\log\log X,\qquad R=\lfloor\sqrt L\rfloor.
\]

令 \(E_{\mathrm{sq,new}}(X)\) 计数满足 \(p\le X\)、\(p\equiv1\pmod{24}\) 且对每个
\(5\le r\le R\) 都不存在素数 \(q\) 使

\[
q\mid p+4r^2,\qquad q\equiv-1\pmod{4r},\qquad q\notin\mathcal O_p. \tag{1}
\]

则存在绝对常数 \(c>0\)，使对充分大的 \(X\)，

\[
E_{\mathrm{sq,new}}(X)\ll X\exp\bigl(-cL\log L\bigr). \tag{2}
\]

故除去相对密度为零的核心素数后，总有 \(s=r^2\le R^2\le\log\log X\) 满足 (1)。
对其中 \(p>4R^2\) 的点，取 \(A=r,C=1,h=q\)，便得到一张纯新单素因子 Type II
证书；余下的 \(p\le4R^2\) 只有 \(O(R^2)\) 个，已被渐近例外项吸收。

## 证书与新性

由 \(q\equiv-1\pmod{4r}\)，令

\[
K=\frac{q+1}{4r},\qquad h=q=4rK-1. \tag{3}
\]

又 \(q\mid p+4r^2\) 等价于 \(h\mid Kp+r\)。只要 \(p\ge4r^2\)，Type II 正规形的
序条件自动成立，故 (3) 恢复一张除子 \(d=r^2\) 的合法证书。

若 \(q>4R^2\) 同时整除 \(p+4r^2\) 与某个 \(p+4t\)（\(1\le t\le19\)），则

\[
q\mid4(r^2-t).
\]

这里 \(r\ge5\)，所以 \(r^2-t\ne0\)，且 \(0<|4(r^2-t)|<4R^2<q\)，矛盾。
因此筛法中大于 \(4R^2\) 的候选素数自动是相对 H19 的新因子。

## 无碰撞筛根

写 \(p=24u+1\)。对每个素数 \(\ell>4R^2\)，定义

\[
\nu_R(\ell)
=1+\#\{5\le r\le R:\ell\equiv-1\pmod{4r}\}. \tag{4}
\]

第一项对应 \(p\equiv0\pmod\ell\)。为上界 (1) 的失败集，只筛满足
\(\ell>4R^2\) 的候选素数已足够：这类候选由上一节自动是新因子，故 (1) 的失败
必然避开它们。于是对 (4) 中每个 \(r\) 还必须避开

\[
p\equiv-4r^2\pmod\ell. \tag{5}
\]

这些根精确地两两不同：两个平方根重合会迫使
\(\ell\mid4(r^2-s^2)\)，而其非零绝对值小于 \(4R^2\)；它们也不可能与零根重合。
因此 \(\nu_R(\ell)\) 是禁根的精确数目。

令

\[
A_R=\sum_{r=5}^{R}\frac1{\varphi(4r)}.
\]

有初等界

\[
\frac14\sum_{r=5}^{R}\frac1r\le A_R\ll\log R. \tag{6}
\]

所有模数 \(4r\) 都是 \(O(\sqrt{\log\log X})\)。一致的算术级数 Mertens 估计给出

\[
\sum_{4R^2<\ell\le z}\frac{\nu_R(\ell)}{\ell}
=(1+A_R)\log\log z+O(R\log R). \tag{7}
\]

又 \(\nu_R(\ell)\le R+1<\ell\)，且二次对数项有界。因此相应筛积满足

\[
V_R(z)\ll\exp(CR\log R)(\log z)^{-1-A_R}. \tag{8}
\]

这里没有一般因子射线的横截面熵：每条平方射线始终只筛指定的
\(-1\pmod{4r}\) 素数类。

## 有参数上界筛

对仅含 \(4R^2\) 以上素因子的平方自由 \(d\)，中国剩余定理给出

\[
\#\{u\le X/24:u\text{ 落在 }d\text{ 的禁根}\}
=\frac X{24}\frac{\nu_R(d)}d+O(\nu_R(d)), \tag{9}
\]

其中 \(\nu_R(d)=\prod_{\ell\mid d}\nu_R(\ell)\)。由 (7)--(8)，基本上界筛的筛维为
\(\kappa_R=1+A_R=O(\log R)\)，正则性成本满足
\(\log K_R=O(R\log R)\)。这里零根排除了 \(p\) 自身的素因子；因而只对 \(p>z\)
直接得到筛包含，\(p\le z\) 的点在最后单独以 \(O(z)\) 计入。

取

\[
D=X^{1/3},\qquad s\asymp R\log R,\qquad z=D^{1/s}.
\]

有参数的上界筛及 \(\nu_R(d)\le(R+1)^{\omega(d)}\) 给出

\[
\begin{aligned}
E_{\mathrm{sq,new}}(X)\ll{}&
X\exp(CR\log R)
\left(\frac{R\log R}{\log X}\right)^{1+A_R}\\
&+X^{1/3}\exp\bigl(O(R\log\log X+R\log R)\bigr). \tag{10}
\end{aligned}
\]

严格地说，(10) 的右侧还应加 \(O(z+R^2)\)。前者来自上段的 \(p\le z\)，后者来自
序条件尚未自动成立的小点。代入 \(R=\lfloor\sqrt L\rfloor\)，并用 (6)，第一项的
对数主项为 \(-\Omega(L\log L)\)，第二项、\(z\) 与 \(R^2\) 都更小，遂得 (2)。

## 边界

这是密度定理，不是逐点选择器。它允许极稀薄但可能无限的例外集，也没有给出对单个
例外素数的递降边。移位族随 \(X\) 增长，因此固定有限扇的条件性逃逸边界并不矛盾。

下列脚本逐项核验新性守卫、禁根公式与禁根互异性：

~~~bash
python3 reproductions/type_ii_pure_new_square_ray_sieve.py \
  --bounds 10 20 50 \
  --prime-bound 100000 \
  --output reproductions/type-ii-pure-new-square-ray-sieve-results.json
python3 -m unittest tests/test_type_ii_pure_new_square_ray_sieve.py -q
~~~
