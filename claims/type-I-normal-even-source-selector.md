---
kind: claim
claim_id: type-I-normal-even-source-selector
title: Type I 正规形最大尾的偶源反向选择器
statement: 在Type I正规形最大尾反向选择器中，R必为奇数。若E|4K^2且R|(4K-E)，则E|nK自动等价于E|4K^2，且n=(4K-E)/R的奇偶性等于E的奇偶性。因此偶源严格边恰由偶因子E|4K^2、E=4K mod R、E<=4K-2R给出；源项为a=nK/E。这将终止于偶数的条件完全下推为目标正规形因子E的奇偶性。
claim_status: established
topics:
- type-I
- normal-form
- descent
- reverse-lift
- even-source
- selector
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: divisor-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-27'
---

# Type I 正规形最大尾的偶源反向选择器

沿用[最大尾反向二尾选择器](type-I-normal-reverse-two-tail-selector.md)的记号：

$$
R=\frac{4B^2C+1}{m},\qquad H=AR-B,\qquad K=BCH,
\qquad4K=pR+1. \tag{1}
$$

## 引理

存在保持前两项的偶源严格反向边，当且仅当存在正整数 $E$ 满足

$$
E\mid4K^2,\qquad E\equiv4K\pmod R,\qquad E\equiv0\pmod2,
\qquad E\le4K-2R. \tag{2}
$$

此时

$$
n=\frac{4K-E}{R},\qquad a=\frac{nK}{E},\qquad
\frac4n=\frac1a+\frac1{ABC}+\frac1{ACH}, \tag{3}
$$

并且 $2\mid n$、$2\le n<p$。

## 证明

由 (1) 有

$$
pR=4K-1,
$$

右端为奇数，故 $R$ 为奇数。若 $R\mid4K-E$，则

$$
\gcd(E,R)=\gcd(4K,R)=1. \tag{4}
$$

再令 $n=(4K-E)/R$。模 $E$ 有

$$
nR\equiv4K\pmod E.
$$

结合 (4)，得到

$$
E\mid nK\quad\Longleftrightarrow\quad E\mid4K^2. \tag{5}
$$

所以先前选择器中看似额外的源端整除条件完全由目标端的 $E\mid4K^2$ 表达。又因 $R$ 为
奇数、$4K$ 为偶数，

$$
n\equiv E\pmod2. \tag{6}
$$

因此 $n$ 偶当且仅当 $E$ 偶。条件 $E\le4K-2R$ 正好等价于 $n\ge2$；而 $E\ge2$ 与
$pR=4K-1$ 一起给出 $n<p$。式 (3) 由 (5) 及原选择器恢复。

## 含义

这个引理没有解决正规形 $(A,B,C,m)$ 的全称选择问题，但它消除了一个逻辑层：为得到可终止的
偶源，不必先构造源、再分解源，只需在目标端寻找满足 (2) 的**偶**桥因子。五亿偶源闭合的
全部 $1{,}717$ 条记录均已按 (2) 重建核验。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_even_source_divisor_audit.py
python3 -m unittest tests/test_type_i_tail_reverse_even_source_divisor_audit.py -q
~~~
