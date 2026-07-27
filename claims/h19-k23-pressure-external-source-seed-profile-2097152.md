---
kind: claim
claim_id: h19-k23-pressure-external-source-seed-profile-2097152
title: H19-k23 两条固定因子桥缺口的外部源种子递降
statement: H19-k23 全局尾压力进程中没有固定因子外部源桥的两个种子 2220549727681245601 与 748375048866405601 仍各有标准外部源严格递降。前者取 k=1、源因子 f=48989；后者取 k=120、源因子 f=41672。完整分解、因子同余 n/f=-1 mod(4k-1) 与有理数恒等式均已逐项核验。该结果只解决两个实际种子，不使变量因子在整条压力进程上固定。
claim_status: computationally_reproduced
topics:
- type-I
- external-source
- strict-descent
- factorization
- pressure-family
- h19
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: external-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 两条固定因子桥缺口的外部源种子递降

[固定因子外部源桥](h19-k23-global-tail-pressure-external-source-bridge-2097152.md)
在 22 条压力进程中统一覆盖 20 条；余下两条只说明不存在由平稳尺度的**固定**源因子
独自给出的整条进程递降。它们不是无递降实例。

对标准外部源

\[
q=4k-1,\qquad n=\frac{qp+1}{4k}, \tag{1}
\]

若 (f\mid n) 且 (n/f\equiv-1pmod q)，令

\[
r=\frac{n/f+1}{q}. \tag{2}
\]

则有严格提升

\[
\frac4p=\frac1{knp}+\frac1{kfr}+\frac1{knr}. \tag{3}
\]

对两个种子，穷尽各自全部平稳尺度的源分母分解和全部因子，得到：

| 种子 (p) | (k) | (q) | 选定 (f) | (n/f) |
|---:|---:|---:|---:|---:|
| (2220549727681245601) | 1 | 3 | 48989 | 33995637709709 |
| (748375048866405601) | 120 | 479 | 41672 | 17921288495423 |

两行均满足 (2)，并以精确有理数核验 (3)。前一源分母的分解为

\[
13\cdot79\cdot48989\cdot33101886767,
\]

后一源分母的分解为

\[
2^3\cdot223\cdot2843\cdot3137\cdot5209\cdot9011.
\]

因此“固定因子桥缺口”应理解为一个**统一性**而非实例存在性问题：已知种子仍由实际
变量因子给出严格下降；未解决的是如何在整条进程上无界自适应地选择这种因子，或将其
压缩为有限可证明状态。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_external_source_seed_profile.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-external-source-seed-profile-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_external_source_seed_profile.py -q
~~~
