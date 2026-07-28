---
kind: claim
claim_id: type-I-fixed-pminusone-ray-pressure-profile-600m
title: 固定 p 减一射线将六亿普通尾压力集压缩至二十五点
statement: 对冻结的1964个不超过六亿的普通 Type II p-1 双尾遗漏，先用 p+1 的三模四因子 B=1 桥，再按 R=3,7,11,15,23,35,47,71,143 的固定 p-1 B=1 除子射线选择，精确覆盖1939个，留下25个明确素数。该结果只描述冻结有限压力集，不是全称选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- b1
- p-minus-one
- terminal-bridge
- factorization
- fixed-ray
- pressure-set
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 固定 (p-1) 射线将六亿普通尾压力集压缩至二十五点

输入由两个已冻结的普通 Type II (p-1) 双尾遗漏档案组成：

| 区间 | 数量 |
| --- | ---: |
| (p\le500{,}000{,}000) | 1,717 |
| (500{,}000{,}000<p\le600{,}000{,}000) | 247 |
| 合计 | 1,964 |

对每个点先测试 [(p+1) 的显式 (B=1) 桥](type-I-p-plus-one-b1-upper-bridge.md)。对其余点，使用
[九条固定 (p-1) 射线](type-I-fixed-universal-pminusone-b1-rays.md)，并按

\[
R=3,7,11,15,23,35,47,71,143
\]

的顺序取第一个满足 (K=(pR+1)/4) 含有

\[
4C\equiv-1\pmod R
\]

的除子 (C) 的射线。每个记录都以精确有理数复查目标和源的三项单位分数恒等式。

## 精确结果

| 优先分支 | 首次覆盖数 |
| --- | ---: |
| (p+1) 因子桥 | 760 |
| (p-1,R=3) | 431 |
| (p-1,R=7) | 387 |
| (p-1,R=11) | 200 |
| (p-1,R=15) | 65 |
| (p-1,R=23) | 52 |
| (p-1,R=35) | 11 |
| (p-1,R=47) | 19 |
| (p-1,R=71) | 10 |
| (p-1,R=143) | 4 |
| 已覆盖 | 1,939 |
| 未覆盖 | 25 |

(R=3) 单独覆盖 714 点，其中 283 点已经被 (p+1) 分支覆盖；这与两条旧因子桥的
(1,191) 点并集一致。其余八条固定 (p-1) 射线再将该联合残余从 773 点降至 25 点。

未覆盖列表为

\[
\begin{aligned}
&297049,3942409,19504489,36583369,40944649,42486889,53712409,57399241,72148729,\\
&82282489,119091289,171292489,172657489,174600409,176110489,212973049,239182969,\\
&259423609,319207849,328186681,340352329,401991529,405660649,437817769,459147049.
\end{aligned}
\]

这些数并不是猜想的反例：它们已由更一般的有限 Type I 桥审计闭合。本剖面的价值在于给出一个
可复现、结构明确的剩余集合，供下一步只研究真正需要自适应 (E,R) 或非零源距离的状态。

复现：

~~~bash
python3 reproductions/type_i_fixed_pminusone_ray_pressure_profile_600m.py
python3 -m unittest tests.test_type_i_fixed_pminusone_ray_pressure_profile_600m -q
python scripts/kb.py validate
~~~
