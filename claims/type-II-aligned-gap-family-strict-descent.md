---
kind: claim
claim_id: type-II-aligned-gap-family-strict-descent
title: 对齐 24c-1 缺口族的 Type I/II 严格递降
statement: 对任意 c,q>=1，令 m=24c-1、n=mq-8、p=24c(n-1)+1。若 p 为素数，则 p 是核心素数，且 gap m 同时具有 Type I 证书 d_I=2n 和固定 Type II 证书 d_II=2。后者给出 4/n=1/(6cn)+1/(2(3cq-1))+1/(6cn(3cq-1))，并通过保留第一分母、将后两尾乘 p 严格提升为 4/p；n<p。对每个固定 c，q 参数进程是 primitive，故含无穷多个素数参数。c=3,q=139 给出 p=709921，它是 R=3 G 且此前五路 terminal dispatch 的残余，但由该全族直接终止并严格递降至 9861。
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
  - gap-family
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
    role: all-cofactor-Type-I-selector
  - reproduction: reproductions/type_ii_aligned_gap_family_strict_descent.py
    role: symbolic-family-and-R3-G-control
visibility: public
last_checked: '2026-08-12'
---

# 对齐 \(24c-1\) 缺口族的 Type I/II 严格递降

## 1. 统一构造

对任意 \(c,q\ge1\)，令

\[
m=24c-1,
\qquad
n=mq-8,
\qquad
p=24c(n-1)+1.
\tag{1}
\]

则

\[
p=(m+1)n-m,
\qquad
x=\frac{p+m}{4}=6cn,
\qquad
m+1\mid p-1.
\tag{2}
\]

特别地 \(n=(p+m)/(m+1)<p\)。若 \(p\) 是素数，则 \(p\equiv1\pmod {24}\)。

**定理。** 对每个这样的核心素数 \(p\)，同一个 gap \(m\) 同时存在

\[
d_{\mathrm I}=2n
\tag{3}
\]

的 Type I certificate，及

\[
d_{\mathrm{II}}=2
\tag{4}
\]

的 Type II certificate；后者还给出严格 two-tail descent。

**证明。** 先有

\[
d_{\mathrm I}=\frac{p+m}{12c},
\qquad
px+d_{\mathrm I}=d_{\mathrm I}(3pc+1).
\tag{5}
\]

而 \(p=(m+1)n-m\) 与 \(n=mq-8\) 给出

\[
3pc+1
\equiv3cn+1
\equiv-24c+1
\equiv0\pmod m.
\tag{6}
\]

再由 \(d_{\mathrm I}\mid x\)，这就是全余因子 \(t=c\) 的 Type I 条件。

对 Type II，定义

\[
y=2(3cq-1),
\qquad
z=6cn(3cq-1).
\tag{7}
\]

由 \(n=mq-8\)，有

\[
x+2
=6c(mq-8)+2
=m\cdot2(3cq-1)
=my,
\tag{8}
\]

\[
x+\frac{x^2}{2}
=6cn+18c^2n^2
=m\cdot6cn(3cq-1)
=mz.
\tag{9}
\]

又 \(2\mid x^2\)、\(2\le x\)，故 \(d_{\mathrm{II}}\) 是 Type II certificate。标准
重建式即给出

\[
\boxed{
\frac4n
=\frac1{6cn}+\frac1{2(3cq-1)}+\frac1{6cn(3cq-1)},}
\tag{10}
\]

\[
\boxed{
\frac4p
=\frac1{6cn}+\frac1{2p(3cq-1)}+\frac1{6pcn(3cq-1)}.}
\tag{11}
\]

式 (11) 从 (10) 保留首分母、把后两尾乘以 \(p\) 得到。故它是显式全域 lift，
自然数 \(p\mapsto n\) 严格下降。证毕。

## 2. 无穷射线

固定 \(c\) 后，(1) 的 \(q\)-参数化为

\[
p=
\left(24c(24c-1)\right)q
-216c+1.
\tag{12}
\]

其首项与步长互素。事实上任一共同因子都整除
\(1-216c\) 与 \(24c(24c-1)\)；前者与 \(24c\) 互素，且模
\(24c-1\) 等于 \(-8\)，同时它是奇数，故也与 \(24c-1\) 互素。因此该进程
primitive，Dirichlet 定理保证每个 \(c\) 都有无穷多个素数参数。

## 3. R=3 G 控制

取 \(c=3,q=139\)，则

\[
p=709921,
\qquad
n=9861,
\qquad
m=71.
\tag{13}
\]

此时

\[
\frac4{9861}
=\frac1{177498}+\frac1{2500}+\frac1{221872500},
\tag{14}
\]

\[
\frac4{709921}
=\frac1{177498}+\frac1{1774802500}+\frac1{157511947072500}.
\tag{15}
\]

又

\[
\frac{3p+1}{4}=532441=7\cdot13\cdot5851,
\tag{16}
\]

所以 \(p\) 是 \(R=3\) G，且此前五路 terminal dispatch 在该点保留 residual。
(15) 关闭该 residual，(14) 给出严格递降。

该全族没有证明所有 G/Type I 状态都具有 (1) 的参数表示，因此不能替代全局出口定理。

复现命令：`python3 reproductions/type_ii_aligned_gap_family_strict_descent.py --verify`
