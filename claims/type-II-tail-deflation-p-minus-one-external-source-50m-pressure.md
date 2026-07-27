---
kind: claim
claim_id: type-II-tail-deflation-p-minus-one-external-source-50m-pressure
title: 五千万低位移残余的完整二次外部源递降边界
statement: p<=5*10^7 时，双尾抽缩、p-1 严格递降和规范位移s<=2共同遗漏的四个核心素数25073689、33011449、42622969、48825529，在普通、混合因子及完整二次因子外部源严格递降的完整枚举中均无命中。因此它们是这三类外部源递降与低位移扇的共同压力集。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- external-source
- tail-deflation
- scaled-source
- canonical-ray
- boundary
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# 五千万低位移残余的完整二次外部源递降边界

在 \(p\le5\cdot10^7\) 的审计中，先取双尾抽缩和完整 \(p-1\) 缩放严格递降后，
再限制直接短证书到规范位移 \(s\le2\)，留下

\[
25\,073\,689,\quad33\,011\,449,\quad42\,622\,969,\quad48\,825\,529.
\]

对每一点，完整枚举三层嵌套的外部源严格递降：

\[
\text{ordinary}\subseteq\text{mixed-factor}\subseteq\text{quadratic-factor}.
\]

三层命中数均为零。每个构造都逐项验证更小源分母、源和目标单位分数恒等式，以及恢复的
Type I 证书。

因此这四点不能仅靠放宽现有外部源的尾因子来吸收。它们仍有位移 \(3,3,4,5\) 的直接
Type II 短证书，故不是猜想反例；这个边界只排除三类具体严格递降族作为固定低位移扇的
补集。

## 重建

~~~bash
python3 reproductions/type_ii_tail_deflation_p_minus_one_external_source_pressure.py
python3 -m unittest tests/test_type_ii_tail_deflation_p_minus_one_external_source_pressure.py -q
~~~
