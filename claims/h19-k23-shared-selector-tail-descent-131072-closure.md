---
kind: claim
claim_id: h19-k23-shared-selector-tail-descent-131072-closure
title: H19-k23 共享选择器 131072 层的普通双尾递降闭合
statement: H19-k23 共享 Type II 选择器 131072 层审计中的299782个实际素数记录，均有普通 Type II 双尾严格递降。其中298987条的最小共享证书缺口本身满足m+1|p-1；剩余795条仅来自共享缺口27、43、51、55、63、83、87，完整枚举p-1的4倍数因子缺口后均找到替代 Type II 双尾递降。因此该有限残存样本有299782=298987+795个严格递降出口，零遗漏。
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

# H19-k23 共享选择器 131,072 层的普通双尾递降闭合

在 131,072 层产物中，先由最小共享缺口 \(m\) 的 \(m+1\mid p-1\) 条件直接重建固定首分母
的 Type II 双尾源；仅对不兼容行完整扫描 \(p-1\) 的全部 \(4\) 倍数因子缺口。

\[
299\,782=298\,987_{\text{shared-gap descents}}
+795_{\text{alternative descents}}+0_{\text{misses}}. \tag{1}
\]

795 条失配行只来自

\[
768_{m=27}+14_{m=43}+4_{m=51}+5_{m=55}+1_{m=63}+1_{m=83}+2_{m=87}. \tag{2}
\]

替代扫描总计穷尽 511,252 个候选缺口。失配缺口的类别比 65,536 层只增加了 \(m=63\)，
没有产生普通双尾递降遗漏。这一有限闭合不外推为所有核心素数的统一递降定理，也没有把
带标记递降变成原猜想的独立归纳证明。

重建命令：

~~~bash
python3 reproductions/h19_k23_shared_selector_tail_descent_closure.py \\
  --input reproductions/h19-k23-shared-selector-audit-131072.json \\
  --output reproductions/h19-k23-shared-selector-tail-descent-131072.json
python3 -m unittest tests/test_h19_k23_shared_selector_tail_descent_closure.py -q
~~~
