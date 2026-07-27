---
kind: claim
claim_id: h19-k23-shared-selector-tail-descent-32768-closure
title: H19-k23 共享选择器 32768 层的普通双尾递降闭合
statement: H19-k23 共享 Type II 选择器 32768 层审计中的77823个实际素数记录，均有普通 Type II 双尾严格递降。其中77615条的最小共享证书缺口本身满足m+1|p-1；剩余208条仅来自共享缺口27、43、51、55、87，完整枚举p-1的4倍数因子缺口后均找到替代 Type II 双尾递降。因此该有限残存样本有77823=77615+208个严格递降出口，零遗漏。
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

# H19-k23 共享选择器 32,768 层的普通双尾递降闭合

对 32,768 层共享选择器产物的每一条记录，先测试其最小共享缺口 \(m\) 是否满足
\(m+1\mid p-1\)。兼容时从已存 \((x,d)\) 精确重建 Type II 目标与源端单位分数恒等式；
不兼容时完整分解 \(p-1\)，穷尽每个 \(4\) 倍数因子缺口的 Type II 除子。

| 路径 | 记录数 | 说明 |
|---|---:|---|
| 原共享缺口 | 77,615 | 已有 Type II 证书且 \(m+1\mid p-1\) |
| 替代 \(p-1\) 缺口 | 208 | 对每个合法因子缺口完整检查 Type II 除子 |
| 遗漏 | 0 | 无 |

\[
77\,823=77\,615_{\text{shared-gap descents}}
+208_{\text{alternative descents}}+0_{\text{misses}}. \tag{1}
\]

208 条失配行仅来自

\[
199_{m=27}+4_{m=43}+1_{m=51}+2_{m=55}+2_{m=87}. \tag{2}
\]

特别地，两个新增 \(m=87\) 记录不是递降遗漏，分别以替代缺口 \(95\) 与 \(99\) 闭合。
全部 208 条失配行总计穷尽 132,956 个 \(p-1\) 候选缺口；每个成功点都精确核验
\(4/p\) 的 Type II 证书及其 \(2\le n<p\) 的双尾源恒等式。

这是一项 14 条 H19-k23 进程、有限参数范围内的普通固定首分母 Type II 递降闭合，
不是所有核心素数都可如此递降的定理，也不是原猜想的归纳证明。

重建命令：

~~~bash
python3 reproductions/h19_k23_shared_selector_tail_descent_closure.py \\
  --input reproductions/h19-k23-shared-selector-audit-32768.json \\
  --output reproductions/h19-k23-shared-selector-tail-descent-32768.json
python3 -m unittest tests/test_h19_k23_shared_selector_tail_descent_closure.py -q
~~~
