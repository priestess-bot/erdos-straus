---
kind: claim
claim_id: type-I-g-anchor-q-supported-p14281-full-scale-exclusion
title: p=14281 的全尺度 Q-supported 外部源精确排除
statement: >-
  对核心素数 p=14281，令 H=(p-1)/4=3570、Q=(p-3)/2=11^2*59。对每个尺度
  k|H，令 q=4k-1、n=(qp+1)/(q+1)、M=kn。不存在正整数 e 满足
  rad(e)|Q、e|M^2、e<=M 和 e=-M (mod q)。故整个 Q-supported 平方因子
  external-source 分支在这个核心素数上为空，即使允许选择所有 k|H。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-q-supported-power-external-source-ray
topics:
  - type-I
  - G-state
  - G-anchor
  - external-source
  - q-supported
  - scale-selection
  - capacity-map
  - complete-exclusion
  - proof-boundary
sources:
  - claim: type-I-g-anchor-q-supported-power-external-source-ray
    role: full-Q-supported-CRT-converse
  - reproduction: reproductions/type_i_g_anchor_q_supported_p14281_full_scale_exclusion.py
    role: complete-divisor-scale-residue-control
visibility: public
last_checked: '2026-08-16'
---

# \(p=14281\) 的全尺度 \(Q\)-supported 外部源精确排除

## 定理

令 \(p=14281\)，它是一个核心素数，并记

\[
H=\frac{p-1}{4}=3570=2\cdot3\cdot5\cdot7\cdot17,
\qquad
Q=\frac{p-3}{2}=7139=11^2\cdot59.
\tag{1}
\]

对任意 \(k\mid H\)，定义

\[
q=4k-1,\qquad
n=\frac{qp+1}{q+1},\qquad
M=kn.
\tag{2}
\]

则不存在正整数 \(e\) 同时满足

\[
\operatorname{rad}(e)\mid Q,\qquad
e\mid M^2,\qquad
e\le M,\qquad
e\equiv-M\pmod q.
\tag{3}
\]

所以完整 \(Q\)-supported 平方因子 external-source 菜单在此 \(p\) 的全部
\(k\mid H\) 上都为空。

## 证明

[全 \(Q\)-supported 赋值菜单的 CRT 正规形](type-I-g-anchor-q-supported-power-external-source-ray.md)
的逆向完备性说明：若 (3) 成立，则 \(e\) 的每个素因子既来自 \(\{11,59\}\)，又整除

\[
6k-1.
\tag{4}
\]

因为 \(H\) 是五个不同素数的乘积，其 32 个除子可直接列出并筛选 (4)，得到

\[
\begin{aligned}
\{k\mid H:11\mid6k-1\}&=\{2,35,255,1190\},\\
\{k\mid H:59\mid6k-1\}&=\{10,1190\}.
\end{aligned}
\tag{5}
\]

其余 27 个尺度没有非平凡 \(Q\)-supported 素因子；\(e=1\) 又会与
\(e\equiv-M\equiv-k\pmod q\) 矛盾。故只须检查 (5) 的并集。

令

\[
\mathcal R_k=
\left\{
11^\alpha59^\beta\bmod q:
0\le\alpha\le2v_{11}(M),\
0\le\beta\le2v_{59}(M)
\right\}.
\tag{6}
\]

由 \(e\mid M^2\)，任何剩余候选的模 \(q\) 余类都在 \(\mathcal R_k\) 中；而
\(M\equiv k\pmod q\)，所需目标为 \(-k\bmod q\)。下表列出全部有限候选：

| \(k\) | \(q\) | \((v_{11}(M),v_{59}(M))\) | \(-k\bmod q\) | \(\mathcal R_k\) |
|---:|---:|---:|---:|---|
| 2 | 7 | \((1,0)\) | 5 | \(\{1,2,4\}\) |
| 10 | 39 | \((0,2)\) | 29 | \(\{1,5,10,20,22\}\) |
| 35 | 139 | \((1,0)\) | 104 | \(\{1,11,121\}\) |
| 255 | 1019 | \((1,0)\) | 764 | \(\{1,11,121\}\) |
| 1190 | 4759 | \((2,1)\) | 3569 | \(\{1,11,59,121,219,364,649,1190,1331,2380,2385,2409,2440,2704,3481\}\) |

每一行的目标都不在相应 \(\mathcal R_k\) 中，故 congruence 条件已经失败。此处甚至
不必使用 \(e\le M\)：表中包含了所有 \(e\mid M^2\) 的 \(Q\)-supported 余类。于是
(3) 对每个 \(k\mid H\) 都不可能成立。\(\square\)

## 后果

这给出的是该外源机制的一个 **全尺度** 严格反例，而不是 Erdős–Straus 猜想的反例：
\(p=14281\) 当然仍可能由其他 Type I/II 证书或不同的严格递降解决。

它关闭了一个具体的全称策略：不能希望“对每个核心素数，某个 \(k\mid(p-1)/4\) 的
\(Q\)-supported 平方因子外源必成功”。因此这条机制最多是选择器中的局部分支；全域
G/Type I 证明必须从其空菜单转向不同的 Type I/II 证书、不同 source，或真实的
可提升递降。

## 聚焦回执

~~~bash
python3 reproductions/type_i_g_anchor_q_supported_p14281_full_scale_exclusion.py --verify
~~~

回执只枚举 \(H=3570\) 的 32 个因子尺度，并在 \(Q\) 的两种支撑素数上重算有限的
赋值—残类菜单；它不搜索素数、分母或历史状态。
