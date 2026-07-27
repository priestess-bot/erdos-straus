---
kind: claim
claim_id: type-I-pminusone-b12-divisor-residue-selector
title: Type I的p减一B一二除子剩余类选择器
statement: 设p=1 mod4、E是4的倍数、R=E-1、K=(pR+1)/4，并假定E|(p-1)^2/4。对源n=p-1，B=1的Type I正规形最大尾反向边存在，当且仅当K有除子C满足4C=-1 modR；B=2的边存在，当且仅当存在2C|K满足16C=-1 modR且K/(2C)为奇数。两种情形均由H=K/(BC)、A=(H+B)/R和m=(4B^2C+1)/R显式恢复。
claim_status: established
topics:
- type-I
- normal-form
- descent
- even-source
- factorization
- source-state
- selector
- residue-class
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# Type I 的 \(p-1\)、\(B=1,2\) 除子剩余类选择器

设

\[
p\equiv1\pmod4,\qquad 4\mid E,\qquad R=E-1,
\qquad K=\frac{pR+1}{4},
\]

并假定

\[
E\mid\frac{(p-1)^2}{4}. \tag{1}
\]

这里 \(R\) 为奇数，且 \(4K\equiv1\pmod R\)。取源 \(n=p-1\) 时，
[源状态实现判据](type-I-normal-source-state-realization.md) 可以压缩为以下两个除子剩余类问题。

## \(B=1\)

存在所需边，当且仅当 \(K\) 有正除子 \(C\) 使

\[
4C\equiv-1\pmod R. \tag{2}
\]

确实，令 \(H=K/C\)。由 \(4K\equiv1\) 及 (2)，有 \(H\equiv-1\pmod R\)，故

\[
A=\frac{H+1}{R},\qquad m=\frac{4C+1}{R} \tag{3}
\]

均为整数，且 \(\gcd(A,1)=1\)。反向则是正规形条件 \(R\mid4C+1\) 本身。

## \(B=2\)

存在所需边，当且仅当存在正整数 \(C\) 满足

\[
2C\mid K,\qquad16C\equiv-1\pmod R,
\qquad \frac K{2C}\ \text{为奇数}. \tag{4}
\]

此时令 \(H=K/(2C)\)。前两个条件给出 \(H\equiv-2\pmod R\)，于是

\[
A=\frac{H+2}{R},\qquad m=\frac{16C+1}{R}. \tag{5}
\]

由于 \(R\) 为奇数，\(A\) 为奇数当且仅当 \(H\) 为奇数；这正是 (4) 的第三项，也是
\(\gcd(A,2)=1\) 的完整条件。反向同样直接来自源状态实现判据。

对核心素数 \(p\equiv1\pmod{24}\)，(2) 或 (4) 所给的正规形自动具有自然缺口。对 \(B=1\)，
若 \(C=K\)，则 \(4C\equiv1\pmod R\) 与 (2) 矛盾；故 \(m<p\)。对 \(B=2\)，当 \(E=4\)
时 \(K\) 为奇数而无候选；当 \(E>4\) 时 \(H\equiv-2\pmod R\) 且 \(H\) 为奇数，因而 \(H\ge3\)，
也给出 \(m<p\)。由于 \(m\equiv3\pmod4\)，它确为自然 Type I 缺口。这不是仅在形式整数环中
成立的重参数化，而是核心范围内的实际短证书选择器。

这一步把 \(B=1\) 的搜索完全变为“\(K\) 是否含有一个指定剩余类的因子”，把 \(B=2\) 变为同一
问题加一个二进奇偶条件。它没有证明这种除子在一般 \(K\) 中总会存在；这正是可用解析数论、筛法或
代数构造推进的核心障碍。

对十万前缀二幂残余的 93 个 \(p-1\) 回归点，这两个选择器的分布为

\[
B=1:81,\qquad B=2:12,
\]

且所用 \(E\) 仅为

\[
12,20,24,28,40,48,56,72,100,112,120,136.
\]

可复现命令：

~~~bash
python3 reproductions/type_i_pminusone_b12_residue_selector.py
python3 -m unittest tests/test_type_i_pminusone_b12_residue_selector.py -q
~~~
