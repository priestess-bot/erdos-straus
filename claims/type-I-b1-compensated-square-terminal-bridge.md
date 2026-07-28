---
kind: claim
claim_id: type-I-b1-compensated-square-terminal-bridge
title: B 等于一正规形的补偿平方终端桥
statement: 设核心素数 p 具有 B=1 Type I 正规形 mR=4C+1、p=4AC-m、H=AR-1、K=CH。若 T|H^2、T=4 mod R，且 q=(H-CT)/R 为正整数并满足 T|qH，则 E=4C^2T 是满足 E|4K^2、E=1 mod R、E<=4K-2R 的偶终端因子，源为 n=4Cq。T=4 是此前自平方桥，R=3、T=1 给出奇 H 的补偿例。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- b1
- terminal-bridge
- compensated-square
- square-divisor
- even-source
- normal-form
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# \(B=1\) 正规形的补偿平方终端桥

设 \(p\equiv1\pmod {24}\) 是核心素数，且已有 \(B=1\) Type I 正规形

\[
mR=4C+1,
\qquad p=4AC-m,
\qquad H=AR-1,
\qquad K=CH. \tag{1}
\]

于是 \(R\ge3\) 为奇数，\(4K=pR+1\)，并且

\[
4C\equiv-1\pmod R. \tag{2}
\]

**定理。** 令 \(T\) 为满足

\[
T\mid H^2,
\qquad T\equiv4\pmod R, \tag{3}
\]

的正整数。再令

\[
q=\frac{H-CT}{R}. \tag{4}
\]

若 \(q>0\) 且 \(T\mid qH\)，则

\[
E=4C^2T,
\qquad n=4Cq \tag{5}
\]

给出一张 Type I 偶源终端桥：

\[
E\mid4K^2,
\qquad E\equiv1\pmod R,
\qquad E\le4K-2R,
\qquad 2\le n<p, \tag{6}
\]

且精确有

\[
\frac4n=\frac1{qH/T}+\frac1{AC}+\frac1{ACH}. \tag{7}
\]

**证明。** 由 (2)、(3) 得

\[
E=4C^2T\equiv4C^2\cdot4=16C^2\equiv1pmod R. \tag{8}
\]

又 \(K=CH\) 且 \(T\mid H^2\)，故

\[
\frac{4K^2}{E}=\frac{H^2}{T}\in\mathbb Z. \tag{9}
\]

由 (4) 有

\[
4K-E=4CH-4C^2T=4CRq,
\]

因而 \(n=(4K-E)/R=4Cq\) 是偶数。这里 \(C\ge2\)，故 \(4K-E=4CRq\ge2R\)，给出
(6) 的范围界；\(E>1\) 还推出 \(n<p\)。条件 \(T\mid qH\) 正是第一源分母 \(qH/T\)
为整数所需的条件。最后，利用 \(Rq=H-CT\) 和 \(H+1=AR\)，有

\[
\frac1{qH/T}+\frac1{AC}+\frac1{ACH}
=\frac T{qH}+\frac R{CH}
=\frac{CT+Rq}{CqH}
=\frac1{Cq}=\frac4n.
\]

证毕。

## 两个边界实例

- 若 \(T=4\)，则 (3) 要求 \(H\) 为偶数，且 (5) 退化为 \(E=16C^2\)。这正是
  [自平方终端桥](type-I-b1-self-square-terminal-bridge.md)。
- 若 \(R=3\)，则 \(T=1\) 自动满足 \(T\equiv4\pmod R\)。例如
  \((p,A,C,m,R,H,K)=(73,4,5,7,3,11,55)\) 给出
  \((T,E,q,n,qH/T)=(1,100,2,40,22)\)。这里 \(H\) 为奇数，故这不是 \(T=4\)
  自平方桥能处理的情形。

定理只提供已有正规形与一个补因子平方除子后的充分条件，不声称这类 \(T\) 对每个核心素数、
每个 \(B=1\) 形式或无界缺口都存在。

~~~bash
python3 -m unittest tests.test_type_i_b1_compensated_square_profile_600m -q
~~~
