---
kind: claim
claim_id: type-I-source-square-congruence-modulus
title: Type I源平方桥条件的精确同余模数
statement: 对任意偶数E，写E=2^a乘以奇数部分u，并定义Lambda(E)=2^{ceil((a+min(a,2))/2)}乘以所有奇素数q的q^{ceil(v_q(E)/2)}之积。对任意偶数n，E整除n^2/gcd(E,4)当且仅当Lambda(E)整除n。因此在移位源n=p-s中，源平方桥条件等价于p同余s模Lambda(E)；再加上s整除E-1，候选源状态可完全表示为桥因子及一个线性同余，而不必先枚举n的全部平方因子。
claim_status: established
topics:
- type-I
- normal-form
- descent
- source-state
- bridge
- congruence
- factorization
- two-adic
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# Type I 源平方桥条件的精确同余模数

令 \(E\) 为偶数，写

\[
E=2^a\prod_{q\ \mathrm{odd}}q^{e_q},\qquad a\ge1,
\]

并定义

\[
\Lambda(E)=
2^{\left\lceil(a+\min(a,2))/2\right\rceil}
\prod_{q\ \mathrm{odd}}q^{\lceil e_q/2\rceil}. \tag{1}
\]

## 定理

对任何偶数 \(n\)，有精确等价

\[
E\mid\frac{n^2}{\gcd(E,4)}
\quad\Longleftrightarrow\quad
\Lambda(E)\mid n. \tag{2}
\]

因而，对于移位源 \(n=p-s\)，(2) 等价于

\[
p\equiv s\pmod{\Lambda(E)}. \tag{3}
\]

若还要求 \(E=sR+1\)，则只需附加 \(s\mid E-1\)（以及 \(R=(E-1)/s\) 的正性和正规形的因子对条件）。
这把候选 Type I 源状态的桥兼容性严格压缩为 \((E,s)\) 的整除和同余条件。

## 证明

对每个奇素数 \(q\)，(2) 左侧的 \(q\)-进条件是

\[
e_q\le2v_q(n),
\]

即 \(v_q(n)\ge\lceil e_q/2\rceil\)。在 \(q=2\) 处，令
\(\delta=\min(a,2)=v_2(\gcd(E,4))\)。条件为

\[
a\le2v_2(n)-\delta,
\]

即 \(v_2(n)\ge\lceil(a+\delta)/2\rceil\)。逐素数合并正是 (1) 中
\(\Lambda(E)\mid n\)。反向逐素数读取即可，证明 (2)；代入 \(n=p-s\) 即得 (3)。

## 研究作用与边界

[归一化源平方等价](type-I-normal-source-square-bridge-equivalence.md) 将桥条件转到源侧；本引理进一步给出源侧条件的最小整除模数。故可扩展的选择律应尝试从低复杂度 \(E\) 出发，选择

\[
s\mid E-1,\qquad p\equiv s\pmod{\Lambda(E)}, \tag{4}
\]

随后才处理 \(K=(p(E-1)/s+1)/4\) 上的因子对残数。这避免把“存在合适源平方因子”误当成独立的启发式搜索步骤。

但 (4) **不**保证 \(BC\mid K\) 且 \(4B^2C\equiv-1\pmod R\)，所以它不是 Erdős--Straus 猜想的证明，也尚未给出全称移位界。脚本在 \(E,n\le2000\) 的一百万个偶数对上逐项核对 (2)，并在五千万前缀最终 35 条动态移位见证上验证 (3)。

可复现命令：

~~~bash
python3 reproductions/type_i_source_square_modulus.py
python3 -m unittest tests/test_type_i_source_square_modulus.py -q
~~~
