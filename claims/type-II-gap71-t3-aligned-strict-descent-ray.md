---
kind: claim
claim_id: type-II-gap71-t3-aligned-strict-descent-ray
title: gap 71 的 t=3 对齐 Type II 严格递降射线
statement: 对每个 a>=0，令 p=4465+5112a、n=63+71a、u=8+9a。若 p 为素数，则它是核心素数，且 gap m=71 同时具有 Type I 证书 d_I=126+142a 和固定 Type II 证书 d_II=2。后者给出 4/n=1/(18n)+1/(2u)+1/(18nu)，并通过保留第一分母、将后两尾乘 p 严格提升为 4/p；n<p。该进程 primitive，故含无穷多个素数参数。控制 p=709921 是 R=3 G 且此前五路 terminal dispatch 的残余，但由该射线直接终止并严格递降至 9861。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-factor-pair-carrier-strict-descent
  - type-I-24c-minus-one-adaptive-divisor-terminal-family
topics:
  - type-I
  - type-II
  - strict-descent
  - two-tail-lift
  - gap-seventy-one
  - adaptive-divisor
  - dirichlet-ray
  - R3-G
  - proof-boundary
sources:
  - claim: short-certificate-equivalence
    role: Type-I-and-Type-II-divisor-reconstruction
  - claim: type-II-factor-pair-carrier-strict-descent
    role: strict-two-tail-lift-principle
  - claim: type-I-24c-minus-one-adaptive-divisor-terminal-family
    role: t-equals-three-Type-I-terminal-selector
  - reproduction: reproductions/type_ii_gap71_t3_aligned_strict_descent_ray.py
    role: symbolic-ray-and-R3-G-control
visibility: public
last_checked: '2026-08-12'
---

# gap \(71\) 的 \(t=3\) 对齐 Type II 严格递降射线

对 \(a\ge0\)，令

\[
p=4465+5112a,
\qquad
n=63+71a,
\qquad
u=8+9a.
\tag{1}
\]

于是

\[
p=72n-71,
\qquad
x=\frac{p+71}{4}=18n.
\tag{2}
\]

若 \(p\) 为素数，则 \(p\equiv1\pmod {24}\)，且

\[
72\mid p-1,
\qquad
n=\frac{p+71}{72}<p.
\tag{3}
\]

全余因子 selector 的 \(m=71,t=3\) 分支给出

\[
d_{\mathrm I}=\frac{p+71}{36}=126+142a,
\qquad
71\mid9p+1.
\tag{4}
\]

与此同时，固定取 \(d_{\mathrm{II}}=2\)。因为

\[
x+2
=18(63+71a)+2
=71\cdot2(8+9a),
\tag{5}
\]

且 \(2\mid x^2\)，所以这是 gap \(71\) 的 Type II certificate。定义

\[
y=2u,
\qquad
z=18nu.
\tag{6}
\]

又

\[
x+\frac{x^2}{2}
=18n+162n^2
=71\cdot18nu.
\tag{7}
\]

故标准 Type II 重建式化为

\[
\boxed{
\frac4n
=\frac1{18n}+\frac1{2u}+\frac1{18nu},}
\tag{8}
\]

\[
\boxed{
\frac4p
=\frac1{18n}+\frac1{2pu}+\frac1{18pnu}.}
\tag{9}
\]

式 (8) 到 (9) 保留首分母、将后两尾乘以 \(p\)，所以是显式 two-tail lift；
自然数势严格从 \(p\) 降至 \(n\)。

\[
\gcd(4465,5112)=1.
\tag{10}
\]

因此 Dirichlet 定理保证该射线含无穷多个素数参数；每个均同时有 Type I terminal、
Type II terminal 和严格递降。

在 \(a=138\) 时，

\[
p=709921,
\qquad
n=9861,
\qquad
u=1250.
\tag{11}
\]

于是

\[
\frac4{9861}
=\frac1{177498}+\frac1{2500}+\frac1{221872500},
\tag{12}
\]

\[
\frac4{709921}
=\frac1{177498}+\frac1{1774802500}+\frac1{157511947072500}.
\tag{13}
\]

又

\[
\frac{3p+1}{4}=532441=7\cdot13\cdot5851,
\tag{14}
\]

三个素因子均为 \(1\pmod3\)，故 \(p\) 在 \(R=3\) G 核心。此前五路 terminal dispatch
在该点保留 residual；(13) 关闭它，且 (12) 给出严格递降。

本结果只覆盖这条无穷参数射线，不构成 \(R=3\) G 的全称 selector 或全局出口证明。

复现命令：`python3 reproductions/type_ii_gap71_t3_aligned_strict_descent_ray.py --verify`
