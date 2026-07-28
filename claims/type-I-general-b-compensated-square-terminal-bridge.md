---
kind: claim
claim_id: type-I-general-b-compensated-square-terminal-bridge
title: 一般 B 正规形的补偿平方终端桥
statement: 设核心素数 p 具有 Type I 正规形 p=4ABC-m、mR=4B^2C+1、H=AR-B、K=BCH。若 T|H^2、T=4B^2 mod R，且 q=(H-BCT)/R 为正整数并满足 T|qH，则 E=4B^2C^2T 是满足 E|4K^2、E=1 mod R、E<=4K-2R 的偶终端因子，源为 n=4BCq。B=1 时退化为补偿平方桥。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- general-b
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

# 一般 \(B\) 正规形的补偿平方终端桥

令 \(p\equiv1\pmod {24}\) 的 Type I 正规形为

\[
p=4ABC-m,
\qquad mR=4B^2C+1,
\qquad H=AR-B,
\qquad K=BCH, \tag{1}
\]

其中 \((A,B)=1\)。则 \(4K=pR+1\)，且

\[
4B^2C\equiv-1pmod R. \tag{2}
\]

**定理。** 若正整数 \(T\) 满足

\[
T\mid H^2,
\qquad T\equiv4B^2pmod R, \tag{3}
\]

并且

\[
q=\frac{H-BCT}{R}>0,
\qquad Tmid qH, \tag{4}
\]

则令

\[
E=4B^2C^2T,
\qquad n=4BCq, \tag{5}
\]

给出合法的 Type I 偶源终端桥：

\[
E\mid4K^2,
\qquad E\equiv1pmod R,
\qquad E\le4K-2R,
\qquad 2\le n<p, \tag{6}
\]

且

\[
\frac4n=\frac1{qH/T}+\frac1{ABC}+\frac1{ACH}. \tag{7}
\]

**证明。** 由 (2)、(3)，有

\[
E=4B^2C^2T\equiv-C\cdot4B^2\equiv1pmod R. \tag{8}
\]

又 \(K=BCH\)，故

\[
\frac{4K^2}{E}=\frac{H^2}{T}\in\mathbb Z. \tag{9}
\]

由 (4) 得

\[
4K-E=4BCH-4B^2C^2T=4BCRq,
\]

所以 \(n=(4K-E)/R=4BCq\) 为偶数。右边至少为 \(4R\)，因而给出 \(E\le4K-2R\)；
\(E>1\) 给出 \(n<p\)。条件 \(T\mid qH\) 保证首项 \(qH/T\) 整数。最后，利用
\(H+B=AR\) 与 \(Rq=H-BCT\)，有

\[
\frac1{qH/T}+\frac1{ABC}+\frac1{ACH}
=\frac T{qH}+\frac{H+B}{ABCH}
=\frac T{qH}+\frac R{BCH}
=\frac{BCT+Rq}{BCqH}
=\frac1{BCq}=\frac4n.
\]

这证明 (6)--(7)。

当 \(B=1\) 时，(3)--(5) 正是 [\(B=1\) 补偿平方桥](type-I-b1-compensated-square-terminal-bridge.md)。
特别地，\(T=4B^2\) 给出此前的“自然自平方”候选；
[自然自平方刚性](type-I-general-b-self-square-rigidity.md)说明该特例在 \(B>1\) 时必失败，
而本定理允许不同 \(T\) 来补偿这个障碍。

例如 \(p=30{,}997{,}849\) 有 \((A,B,C,m,R,H)=(33989,3,76,119,23,781744)\)。
取 \(T=128\)，则 \(T\equiv4B^2\pmod {23}\)、\(q=32720\)，并给出

\[
(E,n,qH/T)=(26{,}615{,}808,29{,}840{,}640,199{,}833{,}310).
\]

这不是自然 \(T=36\) 自平方候选，且其源处于上半区。

~~~bash
python3 -m unittest tests.test_type_i_general_b_compensated_square_residual_profile_600m -q
~~~
