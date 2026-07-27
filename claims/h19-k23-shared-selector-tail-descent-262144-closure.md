---
kind: claim
claim_id: h19-k23-shared-selector-tail-descent-262144-closure
title: H19-k23 共享选择器 262144 层的普通双尾递降闭合
statement: H19-k23 共享 Type II 选择器 262144 层审计中的588526个实际素数记录，均有普通 Type II 双尾严格递降。其中586995条的最小共享证书缺口本身满足m+1|p-1；剩余1531条仅来自共享缺口27、43、51、55、63、83、87，完整枚举p-1的4倍数因子缺口后均找到替代 Type II 双尾递降。因此该有限残存样本有588526=586995+1531个严格递降出口，零遗漏。
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

# H19-k23 共享选择器 262,144 层的普通双尾递降闭合

对 262,144 层的 588,526 条记录，兼容原缺口 \(m+1\mid p-1\) 时直接重建 Type II 双尾源；
不兼容时完整枚举 \(p-1\) 的 \(4\) 倍数因子缺口。结果为

\[
588\,526=586\,995_{\text{shared-gap descents}}
+1\,531_{\text{alternative descents}}+0_{\text{misses}}. \tag{1}
\]

替代分支仍只来自

\[
1\,490_{m=27}+22_{m=43}+8_{m=51}+7_{m=55}+1_{m=63}+1_{m=83}+2_{m=87}. \tag{2}
\]

这说明新的最大共享缺口 \(m=99\) 本身是尾兼容的，并未扩大原缺口失配类别。替代扫描
累计穷尽 1,006,776 个 \(p-1\) 候选缺口，零遗漏。结论仅是当前 14 条 H19-k23 进程的
有限闭合，不是原猜想的全称递降定理。

重建命令：

~~~bash
python3 reproductions/h19_k23_shared_selector_tail_descent_closure.py \\
  --input reproductions/h19-k23-shared-selector-audit-262144.json \\
  --output reproductions/h19-k23-shared-selector-tail-descent-262144.json
python3 -m unittest tests/test_h19_k23_shared_selector_tail_descent_closure.py -q
~~~
