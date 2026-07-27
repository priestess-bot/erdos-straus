---
kind: claim
claim_id: type-I-normal-source-square-bridge-equivalence
title: Type I正规形桥因子的归一化源平方等价
statement: 在Type I正规形最大尾的偶源反向边中，令s=p-n、E=4K-nR=sR+1，并令d=gcd(E,4)。则E|4K^2当且仅当E|n^2/d。特别地E|n^2；桥因子条件可精确地从目标K平方改写为源分母的归一化平方整除。
claim_status: established
topics:
- type-I
- normal-form
- descent
- reverse-lift
- factorization
- source-state
- two-adic
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# Type I 正规形桥因子的归一化源平方等价

沿用 [Type I 正规形最大尾的偶源反向选择器](type-I-normal-even-source-selector.md) 的记号：

$$
4K=pR+1,\qquad E=4K-nR,\qquad 2\le n<p,\qquad 2\mid n.
$$

令 $s=p-n$，并置 $d=\gcd(E,4)$。则

$$
E=sR+1,\qquad \gcd(s,E)=1,\qquad 4sK\equiv-n\pmod E. \tag{1}
$$

## 定理

桥因子条件有精确的源侧表达：

$$
E\mid4K^2
\quad\Longleftrightarrow\quad
E\mid\frac{n^2}{\gcd(E,4)}. \tag{2}
$$

右端是整数，因为 $E$ 偶、$n$ 偶。它特别推出 $E\mid n^2$。

## 证明

写 $E=2^e u$，其中 $u$ 为奇数、$e\ge1$。由 (1)，$4s$ 在模 $u$ 下可逆，故

$$
u\mid K^2\quad\Longleftrightarrow\quad u\mid n^2. \tag{3}
$$

余下只须比较二进赋值。令 $j=v_2(K)$、$t=v_2(n)$。左端在2-进部分为

$$
e\le2+2j. \tag{4}
$$

若 $e=1$，(4) 自动成立；又 $t\ge1$，恰与 $2\mid n^2/2$ 对应。

现设 $e\ge2$。由 (1) 可写 $n=-4sK+Ew$。若 $e\le j+2$，则 $t\ge e$，所以
$e\le2t-2$。若 $e>j+2$，两项的2-进赋值不同，故 $t=j+2$，此时 (4) 正好成为

$$
e\le2t-2. \tag{5}
$$

反向同理：若 (4) 失败，则必有 $e>j+2$，从而 $t=j+2$ 并使 (5) 失败。于是对
$e\ge2$，(4) 等价于 $2^e\mid n^2/4$。结合 (3) 及
$d=2$（$e=1$）或 $d=4$（$e\ge2$），即得 (2)。

## 含义

这把 [偶源反向选择器](type-I-normal-even-source-selector.md) 中的 $E\mid4K^2$ 精确转换为
近目标源 $n=p-s$ 的平方因子条件。仍须同时满足 $E=sR+1$ 以及正规形的其余整性条件，
所以它不是独立的全称选择器；但它把低支撑桥和非标准源状态置于同一可分解对象上。

`type_i_h19_p25_residue_boundary_source_profile.py` 对28个外部纯剩余障碍逐条核验 (2) 及
源、目标的完整有理数恒等式；独立 H19 偶桥档案的664条记录也全部满足该等价。
