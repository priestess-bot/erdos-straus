---
kind: claim
claim_id: type-I-general-b-self-square-rigidity
title: 一般 B 正规形的自然自平方补因子刚性
statement: 对任意 Type I 正规形 p=4ABC-m、mR=4B^2C+1、H=AR-B、K=BCH，自然满足 E_square=(4B^2C)^2=1 mod R 的自平方补因子整除4K^2，当且仅当 B=1且H为偶数。因而 B>1 时该特定自平方机制必不能成为终端因子；这不排除其他一般B因子或终端桥。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- general-b
- self-square
- terminal-bridge
- rigidity
- normal-form
- obstruction
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 一般 \(B\) 正规形的自然自平方补因子刚性

令一张 Type I 正规形写为

\[
p=4ABC-m,
\qquad
mR=4B^2C+1,
\qquad
H=AR-B,
\qquad
K=BCH, \tag{1}
\]

其中 \((A,B)=1\)。由 (1) 有 \(4K=pR+1\)，并且

\[
4B^2C\equiv-1\pmod R. \tag{2}
\]

看似是 \(B=1\) 自平方桥的直接一般化的因子为

\[
E_{\square}=(4B^2C)^2=16B^4C^2. \tag{3}
\]

它确实自动满足 \(E_{\square}\equiv1pmod R\)。但它在 \(B>1\) 时不能通过目标侧的平方整除条件。

**定理。**

\[
E_{\square}\mid4K^2
\quad\Longleftrightarrow\quad
B=1\ \text{且}\ 2\mid H. \tag{4}
\]

**证明。** 由 \(K=BCH\)，有

\[
\frac{4K^2}{E_{\square}}=\frac{H^2}{4B^2}. \tag{5}
\]

所以 (4) 左侧等价于 \(2B\mid H\)。另一方面，\((B,R)=1\)，因为任意 \(B,R\) 的公因子也会
整除 \(mR-4B^2C=1\)。若 \(B\mid H=AR-B\)，则 \(B\mid AR\)；再由
\((A,B)=(B,R)=1\)，得到 \(B=1\)。反向在 \(B=1\) 时，(5) 正好等价于 \(2\mid H\)。证毕。

因此 [\(B=1\) 自平方终端桥](type-I-b1-self-square-terminal-bridge.md) 的 \(E=16C^2\) 不是一个
可以仅靠把 \(C\) 替换成 \(B^2C\) 而推广的公式。这个刚性结果只否定自然候选 (3)：
[一般 \(B\) 补偿平方桥](type-I-general-b-compensated-square-terminal-bridge.md) 允许不同的 \(T\)
补偿该障碍；其他一般 \(B\)、线性源或 Type II 机制也仍然可能闭合。

例如 \(p=67{,}369\) 的一般 \(B\) 线性证书有

\[
(A,B,C,m,R,H,K)=(74,3,76,119,23,1699,387372).
\]

此时 \(E_{\square}=16\cdot3^4\cdot76^2\equiv1\pmod {23}\)，但 \(2B=6\nmid1699\)，故
\(E_{\square}\nmid4K^2\)。

~~~bash
python3 -m unittest tests.test_type_i_general_b_self_square_rigidity -q
~~~
