---
kind: claim
claim_id: type-I-normal-even-source-ratio-two-pair
title: Type I 偶源桥的比二普通除子对等价
statement: 在Type I正规形偶源反向选择器中，置L=2K。存在偶桥因子E当且仅当存在互素普通除子a,b|L，使a=2b mod R，重构E=La/b为偶数且E<=2L-2R。此时E|4K^2和E=4K mod R自动成立，源为n=(2L-E)/R。故平方桥选择精确化为L的有界普通除子比值命中2 mod R的问题。
claim_status: established
topics:
- type-I
- normal-form
- descent
- reverse-lift
- divisor-residues
- factorization
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

# Type I 偶源桥的比二普通除子对等价

在[偶源反向选择器](type-I-normal-even-source-selector.md)中，令

$$
L=2K.
$$

由于 $E\mid4K^2=L^2$，把分数 $E/L$ 既约化为

$$
\frac EL=\frac ab,\qquad(a,b)=1. \tag{1}
$$

## 定理

存在偶源严格反向边，当且仅当存在正整数 $a,b$ 满足

$$
a\mid L,\qquad b\mid L,\qquad(a,b)=1,\qquad a\equiv2b\pmod R, \tag{2}
$$

并且由

$$
E=\frac{La}{b} \tag{3}
$$

重构的整数满足

$$
2\mid E,\qquad E\le2L-2R. \tag{4}
$$

此时

$$
n=\frac{2L-E}{R},\qquad
\frac4n=\frac1{nK/E}+\frac1{ABC}+\frac1{ACH}. \tag{5}
$$

## 证明

若给定偶桥 $E$，令 $g=(E,L)$、$a=E/g$、$b=L/g$。由 $E\mid L^2$，逐素因子指数
可知 $a,b\mid L$；定义保证二者互素，且 $E/L=a/b$。又 $L$ 在模 $R$ 下可逆，因为
$4K=pR+1$，所以

$$
E\equiv2L\pmod R
\quad\Longleftrightarrow\quad
\frac ab\equiv2\pmod R
\quad\Longleftrightarrow\quad
a\equiv2b\pmod R. \tag{6}
$$

这给出 (2)--(4)。

反过来，设 (2)--(4) 成立。由 $b\mid L$，$E=La/b$ 为整数；又 $a\mid L$，故

$$
\frac{L^2}{E}=\frac{Lb}{a}
$$

为整数，即 $E\mid L^2=4K^2$。由 (6) 得 $E\equiv2L=4Kpmod R$，再应用偶源选择器
即可恢复 (5)。

## 含义

此等价把“从 $K^2$ 选平方因子”改写为 $L=2K$ 的两个**普通除子**之间的有界比值问题。
若

$$
\Delta_R(L)=\left\{a/b\pmod R:a,b\mid L\right\},
$$

则内部同余目标就是 $2\in\Delta_R(L)$，同时保留 (4) 的偶性和大小预算。它与平移平方尾的
反向普通除子对判据具有相同的积集结构，为后续使用子群、角色或有符号指数盒工具提供正确
的状态空间；但没有保证任意 $L,R$ 都命中残数 $2$。

五亿偶源闭合的全部 $1{,}717$ 条边均已按此普通除子对重构。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_even_source_ratio_pair_audit.py
python3 -m unittest tests/test_type_i_tail_reverse_even_source_ratio_pair_audit.py -q
~~~
