---
kind: claim
claim_id: type-I-short-relation-odd-distance-even-source
title: 短关系偶终端的奇数距离偶源提升
statement: >-
  对冻结的 291 个短关系偶终端，令 c=p-n。完整枚举奇数距离偶源参数
  n=d(1+cr)、dr=-1 mod 4 及 e1|M1^2、e1<=M1、e1=-M1 mod r 的平移平方尾，
  得到 11 个参数状态和 6 条严格 Type I 提升；6 条提升全部来自
  p=437817769、n=437817744、c=25、d=23569、r=743、M1=81324650592。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- short-relation
- even-source
- odd-distance
- descent
- solution-lift
- divisor-parametrization
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: Type-I-certificate-and-lift-context
visibility: public
last_checked: '2026-07-30'
depends_on:
  - type-I-short-relation-even-terminal
  - odd-distance-even-source-descent
---

# 短关系偶终端的奇数距离偶源提升

## 分支定义

短关系引理对每个冻结状态给出一个偶数 (n<p)。令

\[
c=p-n.
\]

由于 (p\equiv1\pmod {24}) 且 (4\mid n)，这里的 (c) 是奇数。对每个
(d\mid n)，枚举

\[
s=n/d=1+cr,
\qquad dr\equiv-1\pmod4,
\qquad k=(dr+1)/4,
\qquad M_1=ks.
\]

对每个合法参数，再完整枚举

\[
e_1\mid M_1^2,
\qquad e_1\le M_1,
\qquad e_1\equiv-M_1\pmod r.
\]

令

\[
u=(M_1+e_1)/r,
\qquad v=M_1u/e_1,
\qquad m=(4e_1+1)/r,
\qquad D=u^2/e_1.
\]

奇数距离偶源定理给出精确的源—目标恒等式

\[
\frac4n=\frac1{dM_1}+\frac1u+\frac1v,
\qquad
\frac4p=\frac1{pM_1}+\frac1u+\frac1v,
\]

并且 \((m,D)\) 是目标的 Type I 除子证书。

## 冻结审计结果

复现脚本
`reproductions/type_i_short_relation_odd_distance_even_source.py` 对
`type-i-short-relation-even-terminal-results.json` 做哈希锁定，逐个状态枚举上述
所有参数与平方尾因子，并用有理数恒等式、正性、整除性和 Type I 同余逐条复核。

结果为：

```text
record_count: 291
parameter_state_count: 3
parameter_count: 11
tail_candidate_count: 6
hit_state_count: 1
hit_prime_count: 1
hit_prime: 437817769
```

唯一命中状态的公共参数为

\[
(p,n,c,d,s,r,k,M_1)
=(437817769,437817744,25,23569,18576,743,4377942,81324650592).
\]

它给出 6 个 (e_1)：

\[
282897,\ 396576,\ 952331148,\ 1335014784,\ 7366795776,\ 20837706752.
\]

例如取 (e_1=282897)，得到

\[
u=109454823,\qquad v=31465074695328,\qquad m=1523,
\qquad D=42348834657,
\]

以及严格提升

\[
\frac4{437817744}
=\frac1{1916740689802848}
 +\frac1{109454823}
 +\frac1{31465074695328},
\]

\[
\frac4{437817769}
=\frac1{35605377086893969248}
 +\frac1{109454823}
 +\frac1{31465074695328}.
\]

## 逻辑边界

这是一条新的、可复现的局部递降边：它证明短关系偶终端并非只能停在标准偶数源，
在合适的奇数距离分解下可以产生真正的 Type I 提升。它仍然没有证明 291 个状态
全部有此分支，也没有给出对所有核心素数选择 (c,d,e_1) 的全称规则；因此不能关闭
跨状态容量或“短证书或递降”引理。下一步应研究参数条件

\[
n/d=1+c r,
\qquad dr\equiv-1\pmod4
\]

能否由短关系的因子结构或跨状态容量强制，或将该分支与其它距离的标记源统一成
可递归闭合的状态图。

## 复现

```text
python3 reproductions/type_i_short_relation_odd_distance_even_source.py
```

结果文件：

```text
reproductions/type-i-short-relation-odd-distance-even-source-results.json
```
