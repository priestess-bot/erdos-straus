---
kind: claim
claim_id: five-branch-sieve-residual
title: 五条显式因子证书分支的共同残余有 7/2 维筛界
statement: 令 R_5(X) 为 p<=X、p=1 mod24 的素数中同时未被 m=3、(p+1)/2 的 3 mod4 因子、p+4 的 3 mod4 因子、4p+1 的 3 mod4 因子和 (3p+1)/4 的 2 mod3 因子这五条显式分支覆盖的数量，则 R_5(X)=O(X/(log X)^(7/2))。该共同残余非空，例如 p=2521；故筛界不能代替逐点短证书或递降选择器。
claim_status: established
topics:
- sieve
- density
- certificate
- residual-set
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Appendix A, shifted-prime additive functions and sieve estimates"
  role: methodological-foundation
- paper: bradford2024
  locator: "Propositions 1--4"
  role: certificate-branches
visibility: public
last_checked: '2026-07-23'
---

# 五条显式因子证书分支的共同残余有 \(7/2\) 维筛界

对 \(p=24t+1\)，考虑下列五条已证的直接分支：

\[
\begin{array}{c|c|c}
\text{分支} & \text{移位整数} & \text{要求的素因子}\\
\hline
m=3 & 6t+1=(p+3)/4 & 2\pmod3\\
(p+1)/2 & 12t+1 & 3\pmod4\\
p+4 & 24t+5 & 3\pmod4\\
4p+1 & 96t+5 & 3\pmod4\\
(3p+1)/4 & 18t+1 & 2\pmod3
\end{array}
\]

前四条分别见 `gap-three-criterion`、`p-plus-one-sqrt-certificate`、
`p-plus-four-sqrt-certificate` 和 `four-p-plus-one-type-ii-certificate`；第五条见
`three-p-plus-one-descent-certificate`。

令 \(R_5(X)\) 是 \(p\le X\) 的核心素数中这五条分支均失败的数量。则

\[
R_5(X)\ll\frac{X}{(\log X)^{7/2}}. \tag{1}
\]

## 筛法证明

对每个素数 \(\ell>3\)，同时筛去 \(24t+1\equiv0\pmod\ell\)，以及上表中
对应 \(\ell\) 所属同余类的移位整数为零的剩余类。除有限例外 \(\ell=5,11\) 外，
这些线性同余类两两不同：两个类相同只会要求它们的线性系数和常数项的行列式被
\(\ell\) 整除，而所有非零行列式的素因子都在 \(\{2,3,5,11\}\) 中。

故对充分大的 \(\ell\)，局部禁类数 \(\nu(\ell)\) 由 \(\ell\pmod{12}\) 给出：

\[
\begin{array}{c|cccc}
\ell\pmod{12} & 1 & 5 & 7 & 11\\
\hline
\nu(\ell) & 1 & 3 & 4 & 6
\end{array}
\]

其中恒有的一个禁类来自 \(24t+1\) 必为素数；\(2\pmod3\) 的两个移位在
\(5,11\pmod{12}\) 类中各增加一个，\(3\pmod4\) 的三个移位在
\(7,11\pmod{12}\) 类中各增加一个。于是筛积满足

\[
\begin{aligned}
V_5(z)
&=\prod_{\ell\le z}\left(1-\frac{\nu(\ell)}\ell\right)\\
&\asymp
(\log z)^{-\frac14(1+3+4+6)}
=(\log z)^{-7/2}. \tag{2}
\end{aligned}
\]

这里使用了算术级数中的 Mertens 定理；有限个例外素数只改变常数。标准 Selberg
上界筛对 \(t\le X/24\) 给出

\[
S_5(X,z)\ll XV_5(z)+z^2(\log z)^{O(1)}.
\]

取 \(z=X^{1/4}\) 即得到 (1)。同样地，对平方自由模数 \(d\)，禁类交集的计数为
\(X\omega(d)/(24d)+O(\omega(d))\)，满足此上界筛的余项估计。

## 不能推出的结论

这个共同残余不是空的：\(p=2521\) 时，上表的五个整数分别为

\[
631,\quad1261,\quad2525,\quad10085,\quad1891,
\]

均不含相应要求同余类的素因子。因此 (1) 只是把逐点目标压缩到一个更薄的集合；它没有
为该集合构造有界证书，也没有构造到较小实例的可闭合提升边。
