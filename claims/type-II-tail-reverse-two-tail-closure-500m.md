---
kind: claim
claim_id: type-II-tail-reverse-two-tail-closure-500m
title: 五亿普通 Type II 尾遗漏的短反向二尾全闭合
statement: 对p<=500000000的3,292,848个核心素数，普通Type II尾抽缩遗漏1,717个。对这1,717个点按m=3 mod4从3至1003扫描Type I/II除子证书，并对每张Type I最大尾用E|4K^2的完整反向二尾选择器。1,717点全部命中，最大选中缺口127，无遗漏；1,423条源为偶数、294条为奇数。这是目标侧的完整有限严格边闭合，不是全局归纳选择器。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- reverse-lift
- finite-audit
- boundary-case
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: divisor-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿普通 Type II 尾遗漏的短反向二尾全闭合

五亿完整审计覆盖 $3{,}292{,}848$ 个核心素数。普通 Type II 双尾抽缩直接闭合
$3{,}291{,}131$ 个，留下 $1{,}717$ 个点。对这整个遗漏集，本审计按

$$
3\le m\le1003,\qquad m\equiv3\pmod4
$$

扫描 Bradford Type I/II 除子证书，直至找到第一条严格边；每张 Type I 正规形的最大尾均以
[Type I 正规形最大尾选择器](type-I-normal-reverse-two-tail-selector.md) 完整枚举
$E\mid4K^2$。

## 结果

| 项目 | 数值 |
|---|---:|
| 普通尾遗漏点 | 1,717 |
| 找到严格反向边 | 1,717 |
| 未命中 | 0 |
| 最大选中缺口 | 127 |
| 扫到首边前检查的 Type I 证书 | 11,762 |
| 扫到首边前检查的 Type II 证书 | 7,979 |
| 偶数源 | 1,423 |
| 奇数源 | 294 |
| 最小严格差 $p-n$ | 1 |

每条记录都保存目标三元组、源三元组、正规形、反向因子及其精确有理数核验。所有选中边都
替换 Type I 目标的最大项。此前需要平移平方外源补齐的 124 个共同压力点只是该完整闭合的
一个子集，见 [压力集子审计](type-II-tail-pressure-reverse-two-tail-closure-500m.md)。

## 含义

这大幅收紧了五亿范围的经验边界：普通尾抽缩遗漏并不意味着缺少短的严格递降边；在本审计中，
每个遗漏点都在 $m\le127$ 找到一条。

但它仍不是 Erdős--Straus 猜想的证明。选择器首先读取目标 $p$ 的 Type I 正规形，随后反求
源状态；全局递降证明仍须构造可从源侧维护的正规形标记，或证明这种目标选择能递归地实现。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_pressure_reverse_two_tail_closure.py \
  --input reproductions/type-ii-tail-deflation-500m-full-results.json \
  --miss-field misses --gap-cap 1003 \
  --output reproductions/type-ii-tail-reverse-two-tail-500m-all-misses-results.json
python3 -m unittest tests/test_type_ii_tail_reverse_two_tail_all_misses_500m.py -q
~~~
