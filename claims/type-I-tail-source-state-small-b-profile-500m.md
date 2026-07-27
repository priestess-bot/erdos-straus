---
kind: claim
claim_id: type-I-tail-source-state-small-b-profile-500m
title: 五亿偶源状态的最小B跨样本边界
statement: 对五亿普通Type II尾遗漏的1717条已选择偶源状态，最小Type I正规形B分布为1:1645、2:37、3:16、4:5、5:5、7:1、8:3、9:1、11:1、14:1、16:1、17:1。故H19中观察到的B∈{1,2,4,7,13}菜单在此样本遗漏29条；最大最小B为17，出现在p=425855929。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- source-state
- small-parameter
- selector-boundary
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿偶源状态的最小 B 跨样本边界

对五亿普通 Type II 尾遗漏的1,717条已选择偶源状态，按
[源状态实现判据](type-I-normal-source-state-realization.md) 重枚举所有 Type I 正规形，并最小化
$B$，得到

$$
1717=1645_{B=1}+37_{B=2}+16_{B=3}+5_{B=4}+5_{B=5}+1_{B=7}
+3_{B=8}+1_{B=9}+1_{B=11}+1_{B=14}+1_{B=16}+1_{B=17}. \tag{1}
$$

最大最小值是 $B=17$，发生在 $p=425855929$。这直接检验并否定了 H19 中有限观察到的

$$
\{1,2,4,7,13\}
$$

作为跨样本通用菜单：29条记录的最小 $B$ 不在此集合中。该结果并不否定“存在某个统一有界
$B$”的可能性，但表明证明不能简单固定 H19 菜单，且必须允许新的局部因子结构。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_source_state_small_b_profile.py
python3 -m unittest tests/test_type_i_tail_source_state_small_b_profile.py -q
~~~
