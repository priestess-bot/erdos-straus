---
kind: claim
claim_id: type-II-a-one-gap-three-factor-terminal
title: A=1 gap=3 的因子型 Type II 终端
statement: 设 p≡1 (mod 24)，x=(p+3)/4。若存在正整数 B,D 使 x=BD 且 B≡2 (mod 3)，则 gap=3 的 Type II 三项恒等式成立：4/p=1/x+1/[p(x+D)/3]+1/[p(x+x^2/D)/3]。其规范参数为 (A,B,D)=(1,B,D)，除子为 D，且所有分母均为正整数；这是直接 terminal certificate，不产生递归边。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-coprime-factor-normal-form
topics:
- type-II
- direct-certificate
- gap-three
- factor-ray
- a-one
- terminal
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: exact gap-three factor constructor and verifier
visibility: public
last_checked: '2026-08-04'
---

# \(A=1\)、gap \(=3\) 的因子型 Type II 终端

令

\[
x=\frac{p+3}{4}=BD,\qquad B\equiv2\pmod3,
\]

其中 \(p\equiv1\pmod{24}\)，\(B,D\) 为正整数。取 Type II 规范参数
\[
(A,B,C)=(1,B,D),\qquad m=3.
\]

因为 \(B\equiv2\pmod3\)，有 \(3\mid(1+B)\)。于是

\[
y=\frac{p(x+D)}{3}
  =\frac{pD(B+1)}{3},
\qquad
z=\frac{p(x+x^2/D)}{3}
  =\frac{p\,x(B+1)}{3}
\]

都是正整数。直接计算：

\[
\frac1x+\frac1y+\frac1z
=\frac1x+\frac{3}{pD(B+1)}+\frac{3}{px(B+1)}
=\frac4p.
\]

因此

\[
\boxed{\frac4p=\frac1x+\frac1{p(x+D)/3}
+\frac1{p(x+x^2/D)/3}}.
\]

该证书的 gap 为 \(3\)，满足 \(3\le m\le p-2\)；其 A=1 规范条件
\(A\le B\) 与 \(m\mid A+B\) 分别由正性和 \(B\equiv2\pmod3\) 保证。它是直接
terminal_leaf，不需要来源标记集、提升或递归势。

例如
\[
p=15601,\qquad x=3901=83\cdot47,
\]
取 \(B=83,D=47\)，得到
\[
y=20530916,\qquad z=1704066028,
\]
并精确验证 \(4/15601=1/3901+1/y+1/z\)。

复现：

    python3 reproductions/type_i_representation_dual_capacity_selector.py --verify

