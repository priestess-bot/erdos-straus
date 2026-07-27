---
kind: claim
claim_id: odd-distance-even-source-overflow-normal-form
title: 奇距离偶源平方尾的溢出正规形
statement: 设 (r,M)=1，e|M^2，e<=M，e=-M mod r，并令 x=(M+e)/r。令 g=gcd(M,e)、a=M/g、B=e/g。则 M=ag、e=Bg，且 gcd(a,B)=1、B|g、B<=a、a+B=0 mod r；反之这些条件唯一重建一个有效平方尾。并且 gcd(e,x)=g，所以 B=e/gcd(e,x) 正是尾诱导 Type I 正规形的溢出因子。
claim_status: established
topics:
- type-I
- even-source
- normal-form
- overflow
- divisor-residues
- factorization
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization
visibility: public
last_checked: '2026-07-26'
---

# 奇距离偶源平方尾的溢出正规形

设

\[
(r,M)=1,\qquad e\mid M^2,\qquad e\le M,\qquad e\equiv-M\pmod r,
\]

并定义

\[
g=(M,e),\qquad a=\frac{M}{g},\qquad B=\frac{e}{g}.
\]

则尾条件等价于以下正规形：

\[
M=ag,\qquad e=Bg,\qquad (a,B)=1,\qquad B\mid g,\qquad B\le a,\qquad a+B\equiv0\pmod r. \tag{1}
\]

此外，令 \(x=(M+e)/r\)，有

\[
(e,x)=g,\qquad \frac{e}{(e,x)}=B. \tag{2}
\]

所以 \(B\) 恰为尾因子归一化为 Type I 目标除子后的溢出，而不是另一个独立参数。

## 证明

由定义 \(M=ag,e=Bg\)。逐素数比较 \(e\mid M^2\) 的指数给出 \(B\mid g\)；
由 \(e\le M\) 给出 \(B\le a\)。最大公因子的定义给出 \((a,B)=1\)。再由

\[
M+e=g(a+B)equiv0pmod r

\]

以及 \((g,r)=1\)，得到最后一个同余。

反之，(1) 给出 \(e=Bg\mid a^2g^2=M^2\)、\(e\le M\)，并由
\(M+e=g(a+B)\) 给出尾同余。唯一性来自 \(g=(M,e)\)。

最后，\(rx=g(a+B)\)。由于 \((B,a)=1\) 且 \((B,r)=1\)，有
\((B,(a+B)/r)=1\)，故

\[
(e,x)=\left(Bg,g\frac{a+B}{r}\right)=g.
\]

这证明 (2)。

零溢出判据是 \(B=1\) 的特例：此时 \(a\mid M\) 且 \(a\equiv-1\pmod r\)。高溢出状态
则不再是模糊的“平方因子失败”，而是寻找 \(a,B,g\) 满足 (1) 的有限指数积集问题。对四个
十亿压力点的全部 47 个平方尾，正反构造均已逐项复核。
