---
kind: claim
claim_id: type-II-gap71-t5-aligned-strict-descent-ray
title: gap 71 的 t=5 对齐 Type II 严格递降射线
statement: 对每个 b>=0，令 p=19009+25560b、n=265+355b、L=53+71b。若 p 为素数，则它是核心素数，且 gap m=71 同时具有 Type I 证书 d_I=318+426b 和固定 Type II 证书 d_II=1620。后者给出 4/n=1/(90L)+1/(90(b+1))+1/(5L(b+1))，并通过保留第一分母、将后两尾乘 p 严格提升为 4/p；n<p。该进程 primitive，故含无穷多个素数参数。控制 p=530209 是 R=3 G 且此前六路 terminal dispatch 的残余，但由该射线直接终止并严格递降至 7365。
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
    role: t-equals-five-Type-I-terminal-selector
  - reproduction: reproductions/type_ii_gap71_t5_aligned_strict_descent_ray.py
    role: symbolic-ray-and-R3-G-control
visibility: public
last_checked: '2026-08-12'
---

# gap \(71\) 的 \(t=5\) 对齐 Type II 严格递降射线

令

\[
p=19009+25560b,
\qquad
n=265+355b,
\qquad
L=53+71b.
\tag{1}
\]

则

\[
p=72n-71,
\qquad
n=5L,
\qquad
x=\frac{p+71}{4}=90L.
\tag{2}
\]

当 \(p\) 为素数时，\(p\equiv1\pmod {24}\)，且

\[
72\mid p-1,
\qquad
n=\frac{p+71}{72}<p.
\tag{3}
\]

全余因子 Type I selector 的 \(m=71,t=5\) 分支给出

\[
d_{\mathrm I}=\frac{p+71}{60}=318+426b,
\qquad
71\mid15p+1.
\tag{4}
\]

同时固定取 \(d_{\mathrm{II}}=1620\)。因为

\[
\frac{x^2}{d_{\mathrm{II}}}=5L^2,
\qquad
x+d_{\mathrm{II}}
=90(53+71b)+1620
=71\cdot90(b+1),
\tag{5}
\]

所以 \(d_{\mathrm{II}}\mid x^2\)、\(d_{\mathrm{II}}\le x\)，且
\(71\mid x+d_{\mathrm{II}}\)。令

\[
y=90(b+1),
\qquad
z=5L(b+1).
\tag{6}
\]

又

\[
x+\frac{x^2}{d_{\mathrm{II}}}
=90L+5L^2
=71\cdot5L(b+1).
\tag{7}
\]

因此标准 Type II 重建式在此化为

\[
\boxed{
\frac4n
=\frac1{90L}+\frac1{90(b+1)}+\frac1{5L(b+1)},}
\tag{8}
\]

\[
\boxed{
\frac4p
=\frac1{90L}+\frac1{90p(b+1)}+\frac1{5pL(b+1)}.}
\tag{9}
\]

式 (8) 是严格较小分母 \(n<p\) 的解；保留首分母并将后两尾乘以 \(p\)，即得到
(9)。所以它给出显式 two-tail lift 与自然数势 \(p\mapsto n\)。

\[
\gcd(19009,25560)=1.
\tag{10}
\]

Dirichlet 定理保证 (1) 含无穷多个素数参数；每个这样的参数同时具有 (4) 的 Type I
terminal 和 (8)--(9) 的严格递降。

在 \(b=20\) 时，

\[
p=530209,
\qquad
n=7365,
\qquad
L=1473,
\tag{11}
\]

\[
\frac4{7365}
=\frac1{132570}+\frac1{1890}+\frac1{154665},
\tag{12}
\]

\[
\frac4{530209}
=\frac1{132570}+\frac1{1002095010}+\frac1{82004774985}.
\tag{13}
\]

又

\[
\frac{3p+1}{4}=397657=13^3\cdot181,
\tag{14}
\]

其素因子均为 \(1\pmod3\)，故 \(p\) 属于 \(R=3\) G 核心。此前六路 terminal
dispatch 在此点保留 residual；(13) 关闭该残余，而 (12) 额外提供严格递降。

这是一条无穷、可提升且严格递降的子射线，但没有证明每个 \(R=3\) G 状态都落在
此处或任何固定参数射线上。它不能替代全局出口定理。

复现命令：`python3 reproductions/type_ii_gap71_t5_aligned_strict_descent_ray.py --verify`
