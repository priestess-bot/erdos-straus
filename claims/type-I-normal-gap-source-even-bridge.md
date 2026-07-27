---
kind: claim
claim_id: type-I-normal-gap-source-even-bridge
title: Type I 正规形的缺口源偶桥判据
statement: 对任一 Type I 正规形 p=4ABC-m、mR=4B^2C+1、K=BC(AR-B)，若固定严格偶源 n=p-m，则桥因子被唯一强制为 E=mR+1=4B^2C+2。该偶桥 E|4K^2 当且仅当 2B^2C+1|(A+mB)^2；命中时 a=(p-m)K/E 给出从 n 到 p 的严格二尾提升。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- normal-form
- descent
- even-source
- divisor-criterion
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I normal-form context
visibility: public
last_checked: '2026-07-27'
---

# Type I 正规形的缺口源偶桥判据

设 Type I 正规形满足

$$
p=4ABC-m,\qquad
mR=4B^2C+1,\qquad
H=AR-B,\qquad K=BCH.
\tag{1}
$$

固定源分母为与缺口相同距离的偶数

$$
n=p-m.
\tag{2}
$$

## 定理

保持正规形前两项的最大尾反向桥在 (2) 下被唯一确定为

$$
E=4K-nR=mR+1=4B^2C+2.
\tag{3}
$$

令

$$
U=2B^2C+1=\frac E2.
\tag{4}
$$

则 $E$ 是偶源选择器的有效桥因子，当且仅当

$$
\boxed{\ U\mid(A+mB)^2.\ }
\tag{5}
$$

命中时

$$
a=\frac{nK}{E},\qquad
\frac4n=\frac1a+\frac1{ABC}+\frac1{ACH}.
\tag{6}
$$

## 证明

由正规形恒等式 $4K=pR+1$ 与 (2)，

$$
4K-nR=pR+1-(p-m)R=mR+1,
$$

这给出 (3)。因为 $U$ 为奇数，$E=2U$，且

$$
n=p-m=2(2ABC-m).
\tag{7}
$$

所以 $E\mid n^2/2$ 当且仅当

$$
U\mid(2ABC-m)^2.
\tag{8}
$$

模 $U$ 有 $2B^2C\equiv-1$，从而

$$
B(2ABC-m)=2AB^2C-mB\equiv-A-mB\pmod U.
\tag{9}
$$

又 $(B,U)=1$，故 (8) 等价于 (5)。根据
[归一化源平方等价](type-I-normal-source-square-bridge-equivalence.md)，
$E\mid n^2/2$ 精确等价于 $E\mid4K^2$。此外自然缺口范围
$3\le m\le p-2$ 给出 $2\le n<p$，而 (3) 是偶数并且
$E=4K-nR\le4K-2R$。于是偶源选择器恢复 (6)。

## 意义

这是混合终端选择器的一个刚性子分支：一旦选择源距离 $p-n=m$，桥因子不再需要枚举，
只剩一个由正规形因子控制的平方整除。它没有证明总能选择满足 (5) 的正规形；例如新增的
六亿稀疏尾遗漏审计所记录的首个见证没有一条使用 $n=p-m$。因此该判据应作为可构造的
候选分支，而不是全称闭合。

可复现检查：

~~~bash
python3 -m unittest tests/test_type_i_normal_gap_source_even_bridge.py -q
~~~
