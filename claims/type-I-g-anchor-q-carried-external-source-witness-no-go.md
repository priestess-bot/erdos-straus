---
kind: claim
claim_id: type-I-g-anchor-q-carried-external-source-witness-no-go
title: G-anchor Q-carried 因子不能充当 external-source witness
statement: >-
  令 p 为核心素数且 p=1 (mod 24)、R=p-2、Q=(p-3)/2。若正整数 k|(p-1)/4、
  q=4k-1 且 q|Q，令
  n=(qp+1)/(q+1)、M=kn。则 q>=7 且 q 是 G-anchor Jacobi-odd 的 actual raw label，
  并有精确恒等式 gcd(Q,M)=gcd(Q,3q+1)。因此不存在正整数 g 同时满足
  g|Q、g|M 和 g=-1 (mod q)。所以 mixed-factor external-source 及其 adaptive
  子族不能把来自同一 actual Q raw carrier 的因子当作 q-外部源 witness；任何该类
  marked n<p 递降必须使用不整除 Q 的独立因子。该结论不排除其它 k、非 Q-carried
  witness、平方因子外部源的更宽 e-机制、直接 Type I/II 证书或其它 G exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-jacobi-odd-complete-excess-source-menu
  - mixed-factor-external-source-descent
  - adaptive-external-source-descent
topics:
  - type-I
  - G-state
  - G-anchor
  - complete-excess-bundle
  - raw-path
  - external-source
  - marked-descent
  - gcd-intersection
  - no-go
  - proof-boundary
sources:
  - claim: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
    role: actual-Q-carrier-and-Jacobi-odd-raw-label
  - claim: mixed-factor-external-source-descent
    role: mixed-external-witness-and-global-lift-contract
  - claim: adaptive-external-source-descent
    role: adaptive-external-subfamily
  - reproduction: reproductions/type_i_g_anchor_q_carried_external_source_witness_no_go.py
    role: focused-coprime-and-nontrivial-intersection-controls
visibility: public
last_checked: '2026-08-16'
---

# G-anchor \(Q\)-carried 因子不能充当 external-source witness

## 1. 一个真正可达的 raw label 与 external-source 参数相遇

固定核心素数

\[
p\equiv1\pmod {24},\qquad
R=p-2,\qquad
Q=\frac{p-3}{2}.
\tag{1}
\]

考虑一个 ordinary external-source 参数

\[
k\ge1,\qquad k\mid\frac{p-1}{4},\qquad q=4k-1,\qquad q\mid Q,
\tag{2}

\]

以及它的严格较小分母和被保留分母

\[
n=\frac{qp+1}{q+1},\qquad M=kn.
\tag{3}
\]

条件 \(q\mid Q\) 不是抽象的因子碰撞。首先 \(q=3\) 不可能，因为
\(Q\equiv2\pmod3\)，所以 \(q\ge7\)。又

\[
R=p-2\equiv1\pmod q,
\qquad R\equiv q\equiv3\pmod4.
\tag{4}
\]

Jacobi 互反律给出

\[
\chi_R(q)=\left(\frac qR\right)
=(-1)^{((q-1)/2)((R-1)/2)}\left(\frac Rq\right)
=-1.
\tag{5}
\]

所以 \(q\in\mathcal D_p^-\)：它确实是 G-anchor 的 actual Jacobi-odd raw label，
而不是事后添加的外部素因子。问题是：这个 raw carrier 是否能直接提供 external-source
的 witness？

## 2. \(Q\) 与 external source 的精确公共载体

令

\[
a=\frac{p-1}{q+1}.
\tag{6}
\]

由 (2) \(q+1=4k\) 整除 \(p-1\)，故 \(a\) 为正整数，且

\[
p=(q+1)a+1,\qquad n=qa+1,\qquad Q=2ka-1.
\tag{7}
\]

特别地

\[
(Q,k)=1,\qquad (Q,q+1)=1.
\tag{8}
\]

后一个等式只用 \(Q\) 为奇数及 \((Q,k)=1\)。从 (3) 和 (7) 有

\[
(q+1)n=qp+1=2qQ+3q+1.
\tag{9}
\]

因此

\[
\begin{aligned}
(Q,M)
&=(Q,kn)\\
&=(Q,n)\\
&=(Q,(q+1)n)\\
&=\boxed{(Q,3q+1)}.
\end{aligned}
\tag{10}
\]

这里第二、三行分别使用 (8)，最后一行使用 (9)。这不是渐近上界，而是给定
G-anchor raw label 和 external-source 参数后的 exact gcd identity。

## 3. \(-1\) witness 不可能来自 \(Q\)

**定理。** 在 (1)--(3) 的域内，不存在正整数 \(g\) 满足

\[
g\mid Q,\qquad g\mid M,\qquad g\equiv-1\pmod q.
\tag{11}
\]

**证明。** 若 (11) 成立，(10) 给出 \(g\mid3q+1\)。又 \(g\equiv-1\pmod q\)、
\(g>0\)，可写

\[
g=jq-1\qquad(j\ge1).
\tag{12}
\]

由 \(g\le3q+1\) 和 \(q\ge7\)，只可能 \(j=1,2,3\)。

当 \(j=1\) 时，\(q-1\mid3q+1=3(q-1)+4\)，从而 \(q-1\mid4\)，矛盾。
当 \(j=2\) 时，

\[
0<q+2=(3q+1)-(2q-1)<2q-1,
\]

故 \(2q-1\nmid3q+1\)。当 \(j=3\) 时同理

\[
0<2=(3q+1)-(3q-1)<3q-1.
\]

三种情形均矛盾，故 (11) 不可能。\(\square\)

## 4. 对可提升 external-source 分支的准确影响

mixed-factor external-source 的全域 lift 要求

\[
g\mid M=kn,\qquad g\equiv-1\pmod q.
\tag{13}
\]

若该 witness 是 G-anchor raw carrier 的一部分，即再有 \(g\mid Q\)，定理立即否定
(13)。adaptive external-source 的 witness \(f\mid n\) 是 (13) 的更窄特例，因而也
不能由 \(Q\)-carried 因子提供。

这给全局 G/Type I 选择器一条明确的 stop route：当它把 (2) 中这个 actual raw label
选作 external-source 参数时，不能再把同一 \(Q\)-word 的任何因子重复登记为标记
\(n<p\) 解的 external witness。若要使用该外部源，必须发现一个不整除 \(Q\) 的因子；
若要使用 raw carrier，则必须走 Type I/II terminal、其它 source-switch 或新的 lift。

本卡不声称 external-source family 为空。它也不处理完整平方因子机制中的一般
\(e\mid M^2\)，因为 \(e\) 可以不是 \(Q\) 的因子；将该更宽分支也归入本 no-go 会越过
(11) 的精确假设。

## 5. 定向回执

```bash
python3 reproductions/type_i_g_anchor_q_carried_external_source_witness_no_go.py --verify
```

回执只检查两个固定 core controls：\(p=73,q=7\) 给出互素交集；
\(p=1873,q=11\) 给出非平凡的 \((Q,M)=17=(Q,3q+1)\)，但其仅有非平凡公共因子
\(17\equiv6\pmod{11}\)，不是 \(-1\)。两个控制都重算 Jacobi-odd raw-label 条件，
不扫描素数范围、分母或 Reach history。
