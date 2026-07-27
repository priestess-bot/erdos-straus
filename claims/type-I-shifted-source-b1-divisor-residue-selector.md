---
kind: claim
claim_id: type-I-shifted-source-b1-divisor-residue-selector
title: Type I移位偶源的B一除子剩余类选择器
statement: 设p=1 mod4，n=p-s为严格更小偶数，R为不小于3的奇数且K=(pR+1)/4为整数，E=sR+1，并假定E|n^2/gcd(E,4)。则存在自然Type I正规形最大尾反向边，其源为n且B=1，当且仅当K有除子C满足R|4C+1；令H=K/C、A=(H+1)/R、m=(4C+1)/R即可显式恢复该边。百万前缀最终三条短外源边分别由(s,R)=(25,19)一次和(9,31)两次实现。
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
- shifted-source
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# Type I 移位偶源的 \(B=1\) 除子剩余类选择器

设

\[
p\equiv1\pmod4,\qquad n=p-s,\qquad 2\le n<p,\qquad 2\mid n,
\]

并取奇数 \(R\ge3\)，使

\[
K=\frac{pR+1}{4}\in\mathbb Z,\qquad E=sR+1,
\qquad E\mid\frac{n^2}{\gcd(E,4)}. \tag{1}
\]

则 \(E=4K-nR\)，故 (1) 由[归一化源平方等价](type-I-normal-source-square-bridge-equivalence.md)
等价于最大尾桥的条件 \(E\mid4K^2\)。

## 定理

存在源为 \(n\)、\(B=1\) 的自然 Type I 正规形最大尾反向边，当且仅当 \(K\) 有正除子 \(C\)
满足

\[
R\mid4C+1. \tag{2}
\]

此时令

\[
H=\frac KC,\qquad A=\frac{H+1}{R},\qquad m=\frac{4C+1}{R}. \tag{3}
\]

便有

\[
p=4AC-m,
\qquad
\frac4p=\frac1{AC}+\frac1{ACH}+\frac1{pK},
\qquad
\frac4n=\frac1{nK/E}+\frac1{AC}+\frac1{ACH}. \tag{4}
\]

## 证明

若边已存在，\(B=1\) 时正规形条件正是 (2)，且 \(K=CH\)。反之，
\(4K\equiv1\pmod R\) 与 \(4C\equiv-1\pmod R\) 给出

\[
H=K/C\equiv-1\pmod R,
\]

所以 (3) 的 \(A\) 为整数，且 \(\gcd(A,1)=1\)。由 (3) 直接计算

\[
4AC-m=\frac{4CH-1}{R}=\frac{4K-1}{R}=p.
\]

又因 \(R\ge3\)，不可能有 \(H=1\)（否则 \(H\equiv-1\pmod R\)）。故 \(m<p\)；
由 \(p\equiv1\pmod4\) 及 \(4K=pR+1\) 可知 \(m\equiv3\pmod4\)，所以 \(m\) 是自然缺口。
最后由 (1) 和源状态实现判据得到 (4)。

## 百万残余的含义

[百万多层闭合](type-I-multitier-short-source-closure-1m.md)的最终三点全都落在这个单除子选择器中：

\[
(p,s,R,E)=(297049,25,19,476),
\]

以及

\[
(p,s,R,E)=(513529,9,31,280),\quad(710089,9,31,280).
\]

因此它们并非必须切换到不同坐标或 Type II；它们只是不在 \(s=1\) 面上。真正的后续问题是能否证明：
有限或自适应的小 \((s,R)\) 菜单，总能使 \(K\) 出现 (2) 所要求的除子。这一命题目前仍未证明。

可复现命令：

~~~bash
python3 reproductions/type_i_shifted_source_b1_selector_1m.py
python3 -m unittest tests/test_type_i_shifted_source_b1_selector_1m.py -q
~~~
