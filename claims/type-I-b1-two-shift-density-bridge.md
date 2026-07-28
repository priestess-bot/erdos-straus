---
kind: claim
claim_id: type-I-b1-two-shift-density-bridge
title: 两条移位因子分支的B等于一上半区桥有二维筛残余
statement: 令T(X)计数p<=X、p=1 mod24的素数，要求(p+1)/2没有3 mod4素因子且(3p+1)/4没有2 mod3素因子。则T(X)=O(X/(log X)^2)。因此来自这两个移位因子分支的显式B=1上半区偶桥覆盖相对密度一的核心素数，且未覆盖集的筛界比任一单分支的O(X/(log X)^(3/2))更薄。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
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
- paper: elsholtz_tao2013
  locator: Appendix A
  role: upper-bound-sieve-methodology
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
&\ell\nmid(p+1)/2\quad\text{对每个 }\ell\equiv3\pmod4,\\
&q\nmid(3p+1)/4\quad\text{对每个 }q\equiv2\pmod3\}.
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

对每个素数 \(\ell>3\)，筛去 \(24t+1\equiv0\pmod\ell\) 的一个根。若
\(\ell\equiv3\pmod4\)，再筛去 \(12t+1\equiv0\pmod\ell\) 的一个根；若
\(\ell\equiv2\pmod3\)，再筛去 \(18t+1\equiv0\pmod\ell\) 的一个根。

三个根在 \(\ell>3\) 时两两不同：任意两条线性式的行列式绝对值属于
\(\{6,12\}\)。因此，按 \(\ell\pmod {12}\) 分类，局部禁根数为

\[
\begin{array}{c|cccc}
\ell\pmod {12} & 1&5&7&11\\
\hline
\nu(\ell) & 1&2&2&3.
\end{array}
\tag{4}
\]

算术级数中的 Mertens 定理遂给出

\[
\begin{aligned}
V(z)
&=\prod_{\ell\le z}\left(1-\frac{\nu(\ell)}{\ell}\right)\\
&\asymp
(\log z)^{-(1+2+2+3)/4}
=(\log z)^{-2}.
\end{aligned}
\tag{5}
\]

标准 Selberg 上界筛应用于 \(t\le X/24\) 给出

\[
S(X,z)\ll XV(z)+z^2(\log z)^{O(1)}.
\tag{6}
\]

取 \(z=X^{1/4}\)。被 (1) 计数的充分大素数没有任何被筛去的小素因子，故属于该筛余集；
至多 \(p\le z\) 的有限前缀贡献 \(O(z)\)。结合 (5)--(6) 即得 (2)。

具体地，对任意平方自由模数 \(d\)，所列禁根交集在 \(t\le X/24\) 中的计数为
\[
\frac{X}{24d}\prod_{\ell\mid d}\nu(\ell)
+O\!\left(\prod_{\ell\mid d}\nu(\ell)\right).
\]
因此该线性筛系统满足上述 Selberg 上界筛所需的余项估计；\(\ell=2,3\) 及根碰撞的
有限例外只改变隐含常数。

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
