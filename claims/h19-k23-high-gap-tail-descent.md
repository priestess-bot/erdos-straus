---
kind: claim
claim_id: h19-k23-high-gap-tail-descent
title: H19-k23 较高共享缺口记录的普通双尾递降闭合
statement: 在 H19-k23 共享 Type II 选择器 16384 层审计中，最小共享证书缺口至少为15的4562个记录，均有以 p-1 的4倍数因子为缺口的普通 Type II 双尾严格递降。共享缺口15、19、23、31、35、39、47、59、71的记录都在同一缺口递降；仅27、43、55分别转至{31,35,39,47,71}、{47,71}、{59}。因此该有限较高缺口层没有普通双尾递降压力点。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- shared-divisor
- p-minus-one
- computation
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 较高共享缺口记录的普通双尾递降闭合

共享因子选择器审计按“最小直接 Type II 缺口”排序；这个量并不要求
\(m+1\mid p-1\)，所以不能直接视为严格递降的难度。为检验 16,384 层审计中新出现的
较高缺口是否真是递降障碍，对所有最小共享缺口 \(m\ge15\) 的记录完整枚举
\(p-1\) 的全部 \(4\) 倍数因子缺口，并在每个缺口完整检查 Type II 除子。

| 最小共享缺口 | 记录数 | 最小普通双尾缺口谱 |
|---:|---:|---|
| 15 | 2,447 | 15 (2,447 条) |
| 19 | 1,117 | 19 (1,117 条) |
| 23 | 523 | 23 (523 条) |
| 27 | 103 | 31 (73 条), 35 (17 条), 39 (4 条), 47 (8 条), 71 (1 条) |
| 31 | 256 | 31 (256 条) |
| 35 | 57 | 35 (57 条) |
| 39 | 25 | 39 (25 条) |
| 43 | 2 | 47 (1 条), 71 (1 条) |
| 47 | 22 | 47 (22 条) |
| 55 | 1 | 59 (1 条) |
| 59 | 7 | 59 (7 条) |
| 71 | 2 | 71 (2 条) |

因此有限闭合为

\[
4562=4562_{\text{ordinary two-tail descents}}+0_{\text{misses}}.
\]

这消除了一个容易误读：共享缺口谱增长到 \(71\) 表明固定的直接证书缺口界不稳定，
却不表示这些较高缺口记录会保留为普通双尾递降的压力点。该结论仅覆盖上述 4,562 条记录，
不推出 H19-k23 全体记录、也不推出所有核心素数均有普通双尾递降。

重建命令：

~~~bash
python3 reproductions/h19_k23_high_gap_tail_descent.py \\
  --minimum-shared-gap 15 \\
  --output reproductions/h19-k23-elevated-gap-tail-descent-15.json
python3 -m unittest tests/test_h19_k23_high_gap_tail_descent.py -q
~~~
