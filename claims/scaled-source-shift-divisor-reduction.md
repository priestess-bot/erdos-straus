---
kind: claim
claim_id: scaled-source-shift-divisor-reduction
title: 非倍数缩放源的移位因子约化
statement: 设 p 为奇素数、n=p-c，且 b 属于 {2,4}、gcd(a,b)=1。若 b(p-d)=4ac 且 d|an/b，则 gcd(a,d)=1 并有 d|n/b。反之，在 d|n/b 且 a=b(p-d)/(4c) 为正整数并与 b 互素时，d|an/b 自动成立。因此 b=2,4 的缩放源候选可由 n/b 的因子完整枚举。
claim_status: established
topics:
- descent
- scaled-source
- factorization
- divisor-reduction
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 非倍数缩放源的移位因子约化

在缩放一坐标提升中，记 \(n=p-c\)，并考虑唯一可能的非倍数比例

\[
A=\frac{an}{b},\qquad b\in\{2,4\},\qquad \gcd(a,b)=1.
\]

设目标首项为 \(Ap/d\)，并满足该提升的结构等式

\[
b(p-d)=4ac,\qquad d\mid\frac{an}{b},\qquad 0<d<p. \tag{1}
\]

因为 \(b\) 是二的幂，\(a\) 为奇数。令 \(g=\gcd(a,d)\)。由 (1)，\(g\mid bp\)；
又 \(g\) 为奇数，故 \(g\mid p\)。而 \(g\le d<p\)，所以

\[
\gcd(a,d)=1. \tag{2}
\]

由 \(d\mid an/b\) 和 (2) 立即得到

\[
d\mid\frac nb. \tag{3}
\]

反过来，固定 \(d\mid n/b\)，式 (1) 强制

\[
a=\frac{b(p-d)}{4c}. \tag{4}
\]

只要 (4) 是正整数且与 \(b\) 互素，便自动有 \(d\mid an/b\)。所以连续的 \(a\)
搜索精确缩减为 \(n/2\) 或 \(n/4\) 的有限因子枚举。

在 15 个 \(r\le9999\) H19 残余的245条偶源射线上，这个约化按射线记录产生 3,519 个
结构候选：456 个属于 \(b=2\)，3,063 个属于 \(b=4\)。同一偶源可能从不同 \(r\) 状态
重复出现；按 \((p,n,a,b,d)\) 去重后实际有 1,025 个不同候选。这些只是满足首项缩放和
整除的候选；是否给出递降仍需独立满足完整平方尾与证书条件。

## 重建

~~~bash
python3 reproductions/type_ii_h19_bounded_r_scaled_source_candidate_profile.py
python3 -m unittest tests/test_type_ii_h19_bounded_r_scaled_source_candidate_profile.py -q
~~~
