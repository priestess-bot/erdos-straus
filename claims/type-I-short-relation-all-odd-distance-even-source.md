---
kind: claim
claim_id: type-I-short-relation-all-odd-distance-even-source
title: 全部短关系终端的奇数距离偶源提升审计
statement: >-
  对冻结的 291 个分色 F 状态，原始指数盒内共有 658 个非零核关系；定向并去重后得到
  329 个偶终端。将奇数距离偶源平移平方因子扇应用于全部终端，得到 34 个参数状态、
  15 条严格 Type I 提升，命中终端来自 p=30997849 与 p=437817769。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- short-relation
- relation-lattice
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
  - type-I-short-relation-odd-distance-even-source
---

# 全部短关系终端的奇数距离偶源提升审计

## 审计口径

对每个冻结状态

\[
K=\prod_i q_i^{\nu_i},\qquad
\Lambda=\{\lambda:\prod_i q_i^{\lambda_i}\equiv1\pmod R\},
\]

完整枚举原始指数盒
\[
|\lambda_i|\le\nu_i
\]
内的所有非零关系，而不是只取一个规范最短关系。对每个关系定向为
\(\rho=\prod_iq_i^{\lambda_i}<1\)，令

\[
U=K\rho,\qquad E=4U,\qquad n=(4K-E)/R.
\]

随后对每个不同的 \(n\) 应用奇数距离偶源参数化：令 \(c=p-n\)，枚举

\[
n=d(1+cr),\qquad dr\equiv-1\pmod4,
\qquad M_1=((dr+1)/4)(n/d),
\]

以及

\[
e_1\mid M_1^2,\qquad e_1\le M_1,\qquad
e_1\equiv-M_1\pmod r.
\]

每个候选都检查源、目标单位分数恒等式、正性、缺口范围、\(e_1\mid u^2\) 和 Type I
同余。

## 精确结果

复现脚本为
reproductions/type_i_short_relation_all_odd_distance_even_source.py，结果文件为
reproductions/type-i-short-relation-all-odd-distance-even-source-results.json。

~~~text
record_count: 291
raw_relation_vector_count: 658
oriented_terminal_count: 329
parameter_count: 34
parameter_terminal_count: 9
tail_candidate_count: 15
hit_terminal_count: 2
hit_prime_count: 2
hit_primes: 30997849, 437817769
~~~

原始关系数分布为：

\[
2:259,\qquad4:27,\qquad6:4,\qquad8:1.
\]

## 两个命中终端

第一个命中来自

\[
p=30997849,\quad R=35,\quad K=271231179,\quad
n=30997848,\quad U=9,\quad c=1.
\]

其中一组平移参数为

\[
d=1291577,\quad s=24,\quad r=23,\quad
M_1=178237632,\quad e_1=684,
\]

从而

\[
u=7749492,\qquad v=2019372958016,\qquad m=119,\qquad
D=u^2/e_1=87799161196.
\]

第二个命中是上一轮已发现的
\[
p=437817769,\quad n=437817744,\quad c=25,
\]
并产生 6 条提升。

## 逻辑边界

穷举全部短关系把该正向分支从 1 条提升扩大到 15 条、从 1 个核心素数扩大到 2 个，
说明提升失败并不只来自“选错了最短关系”。但 329 个不同终端中仍只有 2 个命中，
所以该结果仍是有限状态内的局部递降证书，不是全称选择器。

当前真正未解的问题是：能否利用多个关系之间的相对支撑、终端距离
\(c=p-n\) 的因子结构，或跨状态 \(q\)-进容量，强制至少一个终端满足
\[
n/d=1+cr,\qquad dr\equiv-1\pmod4
\]
及平方尾同余；否则必须证明失败终端会严格下降到另一类可提升状态。

## 复现

python3 reproductions/type_i_short_relation_all_odd_distance_even_source.py
