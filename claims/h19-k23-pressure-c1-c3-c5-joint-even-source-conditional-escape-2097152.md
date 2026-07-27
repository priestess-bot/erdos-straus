---
kind: claim
claim_id: h19-k23-pressure-c1-c3-c5-joint-even-source-conditional-escape-2097152
title: H19-k23 压力进程距离一、三、五偶源扇的联合 Dickson 条件性逃逸
statement: 假定 Dickson 素数元组猜想，存在无穷多个同一 H19-k23 压力进程核心素数同时逃过完整距离一、三、五偶源扇。三个完整扇的 29 个一次因子出现位置压缩为 24 个正、本原且局部可采纳的一次型；充分大同时素数值使每个分量审计的实际因子模式完整受控，故 24 条射线均只留下已排除的点态或有限参数情形。
claim_status: conditional
topics:
- type-I
- even-source
- conditional
- dickson
- prime-tuples
- factorization
- strict-descent
- pressure-family
- h19
sources:
- paper: bradford2024
  locator: Proposition 1
  role: even-source-descent
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 压力进程距离一、三、五偶源扇的联合 Dickson 条件性逃逸

此前对同一压力进程分别完成了距离 \(c=1,3,5\) 的**完整**偶源扇审计。不能从三个
独立的“无穷多个参数”结论直接推出它们有共同参数，故这里重新从压力输入运行每个分量审计，
并将所有要求为素数的本原一次因子合并。

三个分量的规模为：

| 距离 | 完整兼容射线数 | 最终平方尾模式数 | 一次型出现数 |
| --- | ---: | ---: | ---: |
| \(1\) | 18 | 104,563 | 19 |
| \(3\) | 2 | 5,491 | 4 |
| \(5\) | 4 | 20,414 | 6 |

原始的 29 个一次型出现位置合并为 24 个不同的正、本原一次型；其中包括共同的目标型和
跨距离重复出现的因子型。对所有不超过 24 的素数作根覆盖检查，元组局部可采纳。

假定 Dickson 猜想，24 个型同时取充分大素数无穷次发生。各分量中所有实际素因子便恰由其
固定内容和相应的线性素数给出，所以三个独立的完整因子枚举可在**同一个参数**上同时应用。
距离一、三、五的 18、2、4 条射线分别仍只有点态避靶或有限参数异常；取足够大参数后，
24 条射线全部失败。

因此在 Dickson 条件下，无穷多个核心素数同时逃过完整的距离一、三、五偶源扇。这不反驳
Erdős--Straus 猜想，也不排除其它距离、非偶源 Type I、Type II 或其它递降状态。它明确
排除了一个自然但不足的策略：用这三个固定奇距离的标准偶源扇取并集来获得全称递降。

可复现命令：

~~~bash
python3 reproductions/h19_k23_pressure_c1_c3_c5_joint_even_source_conditional_escape.py \
  --input reproductions/h19-k23-global-tail-pressure-external-source-bridge-2097152.json \
  --output reproductions/h19-k23-pressure-c1-c3-c5-joint-even-source-conditional-escape-2097152.json
python3 -m unittest tests/test_h19_k23_pressure_c1_c3_c5_joint_even_source_conditional_escape.py -q
~~~
