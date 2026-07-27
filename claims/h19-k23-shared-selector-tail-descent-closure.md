---
kind: claim
claim_id: h19-k23-shared-selector-tail-descent-closure
title: H19-k23 共享选择器 16384 层的普通双尾递降闭合
statement: H19-k23 共享 Type II 选择器 16384 层审计中的39658个实际素数记录，均有普通 Type II 双尾严格递降。其中39552条的最小共享证书缺口本身满足m+1|p-1；剩余106条仅来自共享缺口27、43、55，完整枚举p-1的4倍数因子缺口后均找到替代 Type II 双尾递降。因此该有限残存样本有39658=39552+106个严格递降出口，零遗漏。
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

# H19-k23 共享选择器 16,384 层的普通双尾递降闭合

共享选择器的每一条记录已经有直接 Type II 证书，但该记录的最小缺口 \(m\)
未必满足普通双尾去 \(p\) 所需的 \(m+1\mid p-1\)。对 16,384 层产物中的全部
39,658 条实际素数记录，分两类精确核验：

1. 若其最小共享缺口满足 \(m+1\mid p-1\)，从已存的 \((x,d)\) 重新计算两条
   \(p\)-尾、目标恒等式及源恒等式；
2. 否则完整分解 \(p-1\)，穷尽所有 \(4\) 倍数因子所给缺口，并在每个缺口完整枚举
   Type II 平方除子。

结果为

| 路径 | 记录数 | 说明 |
|---|---:|---|
| 原共享缺口 | 39,552 | 已有 Type II 证书且 \(m+1\mid p-1\) |
| 替代 \(p-1\) 缺口 | 106 | 对所有合法因子缺口作完整 Type II 检查 |
| 遗漏 | 0 | 无 |

故有限闭合恒等式为

\[
39\,658=39\,552_{\text{shared-gap descents}}
+106_{\text{alternative descents}}+0_{\text{misses}}. \tag{1}
\]

106 条不兼容原缺口的记录恰来自

\[
103_{m=27}+2_{m=43}+1_{m=55}. \tag{2}
\]

失配行合计穷尽了 72,236 个 \(p-1\) 候选缺口。每一条命中均用精确分数核对

\[
\frac4p=\frac1x+\frac1y+\frac1z,
\qquad
\frac4n=\frac1x+\frac1{y/p}+\frac1{z/p},
\qquad 2\le n<p.
\]

因此，这不是共享标记表示，而是每条记录都有普通固定首分母的 Type II 双尾严格递降。
它仍只闭合当前 14 条 H19-k23 进程的有限参数样本，不能外推为所有核心素数的递降定理。

重建命令：

~~~bash
python3 reproductions/h19_k23_shared_selector_tail_descent_closure.py
python3 -m unittest tests/test_h19_k23_shared_selector_tail_descent_closure.py -q
~~~
