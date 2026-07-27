---
kind: claim
claim_id: type-I-tail-reverse-surplus-external-hybrid-500m
title: 五亿多素因子反向边界的平方外源混合闭合
statement: 五亿普通Type II尾遗漏中，线性或单素幂反向剩余量S=E/gcd(E,4K)未命中的34个点，26个有零偏移完整平方因子外源严格递降；余8个均有平移平方外源严格递降，最小偏移仅为9或25（各4个）。故34=26+8且无遗漏；多素因子平方剩余量是切换至外源递降的有限识别信号，而非新的严格递降障碍。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- reverse-lift
- external-source
- hybrid-closure
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: certificate-and-lift-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿多素因子反向边界的平方外源混合闭合

在[反向证书平方剩余量边界](type-I-tail-reverse-single-surplus-boundary-500m.md)中，普通
Type II $p-1$ 尾遗漏的 $1{,}717$ 个点有 $34$ 个不具备

$$
S=rac{E}{\gcd(E,4K)}=1\quad\text{或}\quad q^a
$$

的严格 Type I 最大尾反向边。对这 $34$ 点，独立重建完整平方因子外源递降及其必要的平移
射线，得到严格且逐点的分区：

$$
34=26_{\text{零偏移平方外源}}+8_{\text{平移平方外源}}. \tag{1}
$$

八条平移分支的首次偏移分布为

| 偏移 $s$ | 点数 |
|---:|---:|
| 9 | 4 |
| 25 | 4 |

因此在这个有限边界集上，没有必要把反向选择器从“至多一个额外素因子”机械地扩大到二或三
素因子：一旦该较简单选择族失败，已知的平方外源族已提供另一条严格源边。

这是一项机制分区，而非全称递降引理。它仍先从目标 $p$ 的因子结构选择外源状态，尚未给出
对任意源实例可维护的统一规则；也不说明偏移 $9,25$ 在更大范围内足够。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_surplus_external_hybrid.py
python3 -m unittest tests/test_type_i_tail_reverse_surplus_external_hybrid.py -q
~~~
