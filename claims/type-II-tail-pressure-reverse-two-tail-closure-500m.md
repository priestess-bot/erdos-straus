---
kind: claim
claim_id: type-II-tail-pressure-reverse-two-tail-closure-500m
title: 五亿平移外源压力集的短缺口反向二尾全闭合
statement: 对p<=500000000时平移平方外源严格递降共同遗漏的124个核心素数，按m=3 mod4从3至1003完整枚举Type I/II除子证书；对每张Type I证书的每个目标项完整枚举D|4p^2t^2的二分母保留反向边。124点全部命中，最大选中缺口为111，无遗漏；其中106条源分母为偶数、18条为奇数。这是该有限压力集的目标侧严格递降全闭合，不是可归纳的全素数选择器。
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

# 五亿平移外源压力集的短缺口反向二尾全闭合

五亿审计中，普通 Type II 尾抽缩及三层外源递降共同遗漏的压力集为 124 个核心素数。
对每个这样的 $p$，本审计按

$$
3\le m\le1003,\qquad m\equiv3\pmod4
$$

的顺序分解 $x=(p+m)/4$、枚举所有 $d\mid x^2$ 并核验 Type I/II 证书，直至该点得到
第一条严格边或达到盒上限。对每张已检查 Type I 证书的三个目标项 $t$，再用

$$
D\mid4p^2t^2
$$

的完整有限反演枚举保留其余两项的严格源边，见
[gap-27 的二分母保留严格递降](boundary-gap-27-reverse-two-tail-bridge.md)。所有选中边均替换
Type I 的最大项，实际执行时使用等价但更小的
[Type I 正规形最大尾选择器](type-I-normal-reverse-two-tail-selector.md)。

## 结果

| 项目 | 数值 |
|---|---:|
| 压力点 | 124 |
| 找到严格反向边 | 124 |
| 未命中 | 0 |
| 最大选中缺口 | 111 |
| 扫到首边前检查的 Type I 证书 | 721 |
| 扫到首边前检查的 Type II 证书 | 531 |
| 偶数源 | 106 |
| 奇数源 | 18 |
| 最小严格差 $p-n$ | 217 |

因此，先前“平移平方外源共同压力集”在允许不同的二分母保留提升后已全部闭合。特别地，
五亿最大的平移外源边界点 $477015289$ 选中 $m=27$，并严格降到偶数源 $32897608$。

## 正确解释

这并不是 Erdős--Straus 猜想的全局递降证明。每条边均是精确的严格源、目标单位分数恒等式，
但算法先从目标 $p$ 的除子证书选出 $(m,d)$，再反求源标记。要变成归纳证明，仍须给出只依赖
源侧状态的统一选择规则，或证明目标侧这类因子选择可被递归维护。

不过它确实消除了一个此前保留的有限边界：在这 124 个点上，“外源递降均失效”的现象不是
真实的递降缺口，而是限制在平移平方外源及规范尾形时的机制缺口。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_pressure_reverse_two_tail_closure.py \
  --input reproductions/type-ii-tail-deflation-external-boundary-500m-results.json \
  --gap-cap 1003 \
  --output reproductions/type-ii-tail-pressure-reverse-two-tail-500m-results.json
python3 -m unittest tests/test_type_ii_tail_pressure_reverse_two_tail_closure.py -q
~~~
