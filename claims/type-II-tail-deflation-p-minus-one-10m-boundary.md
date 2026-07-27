---
kind: claim
claim_id: type-II-tail-deflation-p-minus-one-10m-boundary
title: Type II 双尾抽缩与 p-1 严格递降的一千万边界
statement: 在 p<=10^7 的82887个核心素数中，完整 Type II 双尾抽缩严格递降覆盖82803个；对其84个遗漏完整枚举 p-1 的 b=1,2,4 缩放源后，再覆盖77个，留下7个明确压力点。因此该两分支在此范围给出82887=82803+77+7，而非全覆盖。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- tail-deflation
- scaled-source
- p-minus-one
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# Type II 双尾抽缩与 \(p-1\) 严格递降的一千万边界

从完整一千万 Type II 双尾抽缩审计的 84 个遗漏出发，对每个点完整枚举源
\(n=p-1\) 的 \(b=1,2,4\) 缩放候选（其中 \(b=1\) 是距离一标准偶源参数化），并逐项验证强制平方尾、源单位分数恒等式、目标
恒等式和 Type I 证书。结果为

\[
82\,887=82\,803+77+7.
\]

前一项是 \(m+1\mid p-1\) 的 Type II 双尾抽缩，第二项是独立的 \(p-1\) 严格
缩放递降。它们合计覆盖 82,880 个核心素数；以下 7 个仍未被这两个严格递降分支命中：

\[
214\,729,297\,049,878\,089,1\,511\,449,3\,942\,409,5\,478\,169,6\,294\,649.
\]

因此 \(p-1\) 缩放不是普通双尾抽缩选择器的普适补集；这 13 点是下一步应研究的最小
明确压力集。它们不是猜想反例，也不排除其他 Type I/II 证书或带标记提升。

## 重建

~~~bash
python3 reproductions/type_ii_tail_deflation_p_minus_one_10m_boundary.py
python3 -m unittest tests/test_type_ii_tail_deflation_p_minus_one_10m_boundary.py -q
~~~
