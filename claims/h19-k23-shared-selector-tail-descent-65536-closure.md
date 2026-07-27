---
kind: claim
claim_id: h19-k23-shared-selector-tail-descent-65536-closure
title: H19-k23 共享选择器 65536 层的普通双尾递降闭合
statement: H19-k23 共享 Type II 选择器 65536 层审计中的152893个实际素数记录，均有普通 Type II 双尾严格递降。其中152474条的最小共享证书缺口本身满足m+1|p-1；剩余419条仅来自共享缺口27、43、51、55、83、87，完整枚举p-1的4倍数因子缺口后均找到替代 Type II 双尾递降。因此该有限残存样本有152893=152474+419个严格递降出口，零遗漏。
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

# H19-k23 共享选择器 65,536 层的普通双尾递降闭合

对 65,536 层产物逐条检查最小共享缺口 \(m\) 是否满足 \(m+1\mid p-1\)。兼容的 152,474
条从已存的 \((x,d)\) 精确重建目标及源端恒等式；其余 419 条完整分解 \(p-1\)，并穷尽每个
\(4\) 倍数因子缺口的 Type II 除子。

\[
152\,893=152\,474_{\text{shared-gap descents}}
+419_{\text{alternative descents}}+0_{\text{misses}}. \tag{1}
\]

419 条失配行只来自

\[
402_{m=27}+9_{m=43}+3_{m=51}+2_{m=55}+1_{m=83}+2_{m=87}. \tag{2}
\]

完整替代扫描累计检查 265,048 个 \(p-1\) 候选缺口。新增的 \(m=83\) 记录以缺口
\(159\) 给出 Type II 双尾源；两个 \(m=87\) 记录仍分别以 \(95\)、\(99\) 闭合。
该结论是当前 14 条 H19-k23 进程在有限参数范围内的严格出口闭合，不是全体核心素数的
递降定理或原猜想的归纳证明。

重建命令：

~~~bash
python3 reproductions/h19_k23_shared_selector_tail_descent_closure.py \\
  --input reproductions/h19-k23-shared-selector-audit-65536.json \\
  --output reproductions/h19-k23-shared-selector-tail-descent-65536.json
python3 -m unittest tests/test_h19_k23_shared_selector_tail_descent_closure.py -q
~~~
