---
kind: claim
claim_id: odd-distance-even-source-exchange-symmetry
title: 奇距离偶源递降的距离--源因子交换对称性
statement: 设 c,d=1 mod4、r=3 mod4，且 p=d+c+cdr。则 (c,d,r) 与 (d,c,r) 都满足奇距离偶源的源端参数条件，并具有相同的 M1=(dr+1)(cr+1)/4。因此任何满足 e1|M1^2、e1<=M1、e1=-M1 mod r 的平方尾因子同时给出两条严格递降，它们的目标三元组与 Type I 证书完全相同，仅源分母分别为 p-c 与 p-d。
claim_status: established
topics:
- type-I
- descent
- even-source
- symmetry
- divisor-residues
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# 奇距离偶源递降的距离--源因子交换对称性

令

\[
c\equiv d\equiv1\pmod4,\qquad r\equiv3\pmod4,\qquad
p=d+c+cdr.
\]

将 \(c\) 视为距离、\(d\) 视为 \(p-c\) 的因子，则

\[
p-c=d(1+cr),\qquad k=\frac{dr+1}{4},\qquad
M_1=\frac{(dr+1)(cr+1)}4. \tag{1}
\]

交换 \(c,d\) 后，

\[
p-d=c(1+dr),\qquad k'=\frac{cr+1}{4},\qquad
M_1'=\frac{(cr+1)(dr+1)}4=M_1. \tag{2}
\]

所以两组参数都满足奇距离偶源定理的源端条件。若

\[
e_1\mid M_1^2,\qquad e_1\le M_1,\qquad e_1\equiv-M_1\pmod r, \tag{3}
\]

则由 (2) 可知同一个 \(e_1\) 也满足交换后的平方尾条件。由

\[
u=\frac{M_1+e_1}{r},\qquad v=\frac{M_1u}{e_1}
\]

可见 \(u,v\)、目标三元组 \((pM_1,u,v)\) 以及 Type I 证书均不变；两条不同的源三元组
只在首项分别为 \(dM_1\) 与 \(cM_1\)。

这给出偶源参数空间上的一个可证明对合。它可在 \(c,d\equiv1\pmod4\) 的区域合并交换
轨道，但不能强制 (3) 成立，因此不是递降选择器本身。

在第四压力点的首释放扇中，25 条射线满足交换的同余前提；19 条的交换伙伴仍落在已审计
窗口，形成 10 个交换轨道，其中 1 个为不动点。每个成对轨道的平方尾命中数相同，见
[第四压力点的源射线与平方尾分离](type-II-h19-fourth-even-source-tail-profile.md)。

## 重建

~~~bash
python3 reproductions/even_source_exchange_symmetry.py
python3 -m unittest tests/test_even_source_exchange_symmetry.py -q
~~~
