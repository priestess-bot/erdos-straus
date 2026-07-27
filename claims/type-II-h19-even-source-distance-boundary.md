---
kind: claim
claim_id: type-II-h19-even-source-distance-boundary
title: H19 二次递降遗漏的小距离偶源不可约边界
statement: 在 p<=5*10^8 的三条 H19 平方因子递降遗漏上，完整偶源扇的距离1、3、5、7分别命中0、2、0、1点；35840809 仅在距离7命中，132285169 与141326089 仅在距离3命中。因此当前压力集不能由单一小距离偶源补救。
claim_status: computationally_reproduced
topics:
- descent
- even-source
- obstruction
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# H19 二次递降遗漏的小距离偶源不可约边界

对完整平方因子外部源递降在五亿 H19 剖面中的三个遗漏，逐一运行完整的奇距离偶源扇，
只比较

\[
c\in\{1,3,5,7\}.
\]

精确命中矩阵为：

| \(p\) | 命中距离 |
|---:|---|
| \(35{,}840{,}809\) | 7 |
| \(132{,}285{,}169\) | 3 |
| \(141{,}326{,}089\) | 3 |

所以 \(c=1,5\) 在这三点均无严格提升；\(c=3\) 和 \(c=7\) 都不可删。这只是一个有限
不可约性结果，不证明 \(\{3,7\}\) 对更大范围足够，也不排除某点在未测试的大距离再次命中。

## 重建

    python3 reproductions/type_ii_h19_even_source_distance_boundary.py
    python3 -m unittest tests/test_type_ii_h19_even_source_distance_boundary.py -q
