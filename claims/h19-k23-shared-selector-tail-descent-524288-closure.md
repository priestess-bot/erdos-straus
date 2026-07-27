---
kind: claim
claim_id: h19-k23-shared-selector-tail-descent-524288-closure
title: H19-k23 共享选择器 524288 层的普通双尾递降闭合
statement: H19-k23 共享 Type II 选择器 524288 层审计中的1155128个实际素数记录，均有普通 Type II 双尾严格递降。其中1152335条的最小共享证书缺口本身满足m+1|p-1；剩余2793条仅来自共享缺口27、43、51、55、63、83、87，完整枚举p-1的4倍数因子缺口后均找到替代 Type II 双尾递降。因此该有限残存样本有1155128=1152335+2793个严格递降出口，零遗漏。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- p-minus-one
- shared-divisor
- computation
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 共享选择器 524,288 层的普通双尾递降闭合

对 524,288 层的 1,155,128 条记录，若最小共享缺口满足 \(m+1\mid p-1\)，则从已验证
的 Type II 证书直接重建双尾源；否则完整枚举 \(p-1\) 的 \(4\) 倍数因子缺口。结果为

\[
1\,155\,128=1\,152\,335_{\text{shared-gap descents}}
+2\,793_{\text{alternative descents}}+0_{\text{misses}}. \tag{1}
\]

替代部分仍仅来自既有七类

\[
2\,710_{m=27}+43_{m=43}+19_{m=51}+14_{m=55}
+4_{m=63}+1_{m=83}+2_{m=87}. \tag{2}
\]

完整替代扫描穷尽 1,888,144 个 \(p-1\) 候选缺口，未发现任何普通双尾递降遗漏。
该结论是有限 H19-k23 样本的精确闭合，而非全体核心素数的选择器或原猜想的归纳证明。

重建命令：

~~~bash
python3 reproductions/h19_k23_shared_selector_tail_descent_closure.py \\
  --input reproductions/h19-k23-shared-selector-audit-524288.json \\
  --output reproductions/h19-k23-shared-selector-tail-descent-524288.json
~~~
