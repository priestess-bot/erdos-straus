---
kind: claim
claim_id: type-II-c3-common-carrier-mark-transfer-no-go
title: c=3 中共同 p-carrier 两尾提升的严格 no-go
statement: 令 p=12q-11。若一个 4/q 解在保留两尾比值的前提下，将两尾共同缩放为 lambda*p 后提升到 4/p，即 4/q=1/a+1/b+1/c 与 4/p=1/x+1/(lambda*p*b)+1/(lambda*p*c)，且目标首分母属于合法 gap 正规形，则必有 lambda=1 且 x=a=3q。因此该自然 transfer 类完全等价于已有 gap-11 Type II 直接证书，不产生新的严格递降边。对 q=3 (mod 4) 的等尾标准源，甚至允许两尾采用不同缩放 lambda*p、mu*p 也不可能产生合法 target gap。结果不排除改变尾比、重组两尾或其它非标准 mark-transfer。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-factor-pair-carrier-strict-descent
  - type-II-c3-q-complementary-divisor-r7mod11-descent
  - short-certificate-equivalence
  - denominator-escape-state-contract
topics:
  - type-II
  - c3
  - mark-transfer
  - strict-descent
  - no-go
  - common-carrier
  - proof-boundary
sources:
  - claim: type-II-factor-pair-carrier-strict-descent
    role: gap-eleven-marked-two-tail-layer
  - claim: short-certificate-equivalence
    role: legal-gap-normal-form
  - concept: denominator-escape-state-contract
    role: lift-boundary
visibility: public
last_checked: '2026-08-06'
---

# \(c=3\) 中共同 \(p\)-carrier 两尾提升的严格 no-go

## 1. 共同尾缩放只会回到 gap \(11\)

令

\[
p=12q-11,\qquad q\ge7,\qquad \lambda\ge1.
\tag{1}
\]

假设存在正整数 \(a,b,c,x\)，使

\[
\frac4q=\frac1a+\frac1b+\frac1c,
\tag{2}
\]

\[
\frac4p=\frac1x+\frac1{\lambda pb}+\frac1{\lambda pc}.
\tag{3}
\]

再要求目标首分母 \(x\) 属于合法 gap 正规形：

\[
m=4x-p,\qquad 3\le m\le p-2,\qquad m\equiv3\pmod4.
\tag{4}
\]

**定理（共同 carrier no-go）。** 在 (1)--(4) 下必有

\[
\boxed{\lambda=1,\qquad m=11,\qquad x=a=3q.}
\tag{5}
\]

所以 (3) 只是已有的 marked gap-\(11\) 形式

\[
\frac4q=\frac1{3q}+\frac1b+\frac1c
\Longrightarrow
\frac4p=\frac1{3q}+\frac1{pb}+\frac1{pc}.
\tag{6}
\]

**证明。** 将 (2) 的两尾和代入 (3)，得到

\[
a=\frac{qx}{p-m(\lambda q-1)},
\qquad
p-m(\lambda q-1)>0.
\tag{7}
\]

故

\[
m<\frac p{q-1}<13,
\tag{8}
\]

所以 \(m\in\{3,7,11\}\)。结合 (7) 的正性，\(\lambda\le3\)，且仅有

\[
(\lambda,m)\in
\{(1,3),(1,7),(1,11),(2,3),(3,3)\}.
\tag{9}
\]

相应的 \(a\) 依次为

\[
\frac{q(3q-2)}{9q-8},\qquad
\frac{q(3q-1)}{5q-4},\qquad
3q,\qquad
\frac{q(3q-2)}{6q-8},\qquad
\frac{q(3q-2)}{3q-8}.
\tag{10}
\]

前两项中分母分别与 \(q\) 互素且大于第二因子，故不为整数。第四项分子为奇数、
分母为偶数。最后一项若为整数，则 \(3q-8\mid6\)，但 \(q\ge7\) 时不可能。
仅第三项存活，给出 (5)。证毕。

例如 \(p=73,q=7\) 时，

\[
\frac47=\frac1{21}+\frac12+\frac1{42}
\Longrightarrow
\frac4{73}=\frac1{21}+\frac1{146}+\frac1{3066},
\tag{11}
\]

正是 (6) 的唯一存活型。另一方面 \(p=313,q=27\) 虽有普通源解

\[
\frac4{27}=\frac19+\frac1{54}+\frac1{54},
\tag{12}
\]

但该类若能提升必须把首项改为 \(81\)。此时

\[
(11b-81)(11c-81)=81^2
\tag{13}
\]

要求某个 \(3\) 的幂为 \(7\pmod{11}\)，而
\(\{3^j\pmod{11}\}=\{1,3,4,5,9\}\)，故 marked gap-\(11\) 集为空。

## 2. 等尾标准源的非对称缩放也失败

当 \(q\equiv3\pmod4\) 时，有标准等尾源

\[
\frac4q
=\frac1{(q+1)/4}
+\frac2{q(q+1)/2}.
\tag{14}
\]

即使把两个相等的尾分别缩放为 \(\lambda pB,\mu pB\)，其中

\[
B=\frac{q(q+1)}2,\qquad \lambda,\mu\ge1,
\tag{15}
\]

目标合法 gap 也必须满足

\[
m=\frac{p(\lambda+\mu)}
{4B\lambda\mu-\lambda-\mu}
\le\frac p{q(q+1)-1}<3.
\tag{16}
\]

这与 (4) 矛盾。因此仅靠等尾的非对称共同 \(p\)-carrier 也不能创造新边。

## 3. 剩余方向

本卡没有排除：

1. 非标准 \(q\)-源上改变两个尾比的变换；
2. 同时重组两尾的非对角传递；
3. 不以 \(q=(p+11)/12\) 为来源的递降；
4. 其它 gap 或直接 terminal。

这些才是寻找真正新 mark-transfer 时需要证明的剩余空间。
