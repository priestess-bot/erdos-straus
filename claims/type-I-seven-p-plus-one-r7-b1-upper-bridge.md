---
kind: claim
claim_id: type-I-seven-p-plus-one-r7-b1-upper-bridge
title: 来自七 p 加一五模七因子的 R 等于七 B 等于一上半区桥
statement: 对核心素数 p，若奇素数 q=5 mod7 整除 K=(7p+1)/4，则令 C=q、H=K/q、A=(H+1)/7、m=(4q+1)/7；这给出 B=1 的 Type I 正规形。再取 E=8、n=p-1，得到严格上半区偶源终端桥。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- b1
- p-minus-one
- terminal-bridge
- seven-p-plus-one
- factorization
- sieve
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 来自 \((7p+1)/4\) 五模七因子的 \(R=7\) (B=1) 上半区桥

令 (p\equiv1\pmod {24}) 为核心素数，写

\[
K=\frac{7p+1}{4}.
\]

假设奇素数 (q) 满足

\[
q\mid K,
\qquad q\equiv5\pmod7. \tag{1}
\]

取

\[
C=q,
\qquad H=\frac Kq,
\qquad A=\frac{H+1}{7},
\qquad m=\frac{4q+1}{7}. \tag{2}
\]

由于 (K\equiv2\pmod7) 且 (q^{-1}\equiv3\pmod7)，有 (H\equiv6\equiv-1\pmod7)，
所以 (2) 中的 (A,m) 都是正整数。并且

\[
7m=4C+1,
\qquad K=CH,
\qquad
p=4AC-m. \tag{3}
\]

因此 ((A,1,C)) 是一张 Type I 正规形，且

\[
\frac4p=\frac1{AC}+\frac1{ACH}+\frac1{pK}. \tag{4}
\]

现在令

\[
R=7,
\qquad E=8,
\qquad n=p-1. \tag{5}
\]

写 (p=24t+1)，则 (K=42t+2) 为偶数，故 (8\mid4K^2)。又

\[
E\equiv1\pmod R,
\qquad
\frac{4K-E}{R}=\frac{7p+1-8}{7}=p-1=n. \tag{6}
\]

此外 (E<2K)，而 (n) 是满足 (n\ge(p+1)/2) 的偶数。因此最大尾可反向提升，给出

\[
\frac4n=\frac1{nK/E}+\frac1{AC}+\frac1{ACH}. \tag{7}
\]

这正是[九条固定 (p-1) 射线](type-I-fixed-universal-pminusone-b1-rays.md)中 (E=8,R=7)
射线的一条单素因子充分条件。它与 (p\equiv25\pmod{48}) 上的
[模七混合因子边界](type-I-k2-mod7-even-source-factor.md)不同：这里不限制该附加同余类，且直接
给出 (p-1) 的 (B=1) 桥。

~~~bash
python3 -m unittest tests.test_type_i_seven_p_plus_one_r7_b1_upper_bridge -q
~~~
