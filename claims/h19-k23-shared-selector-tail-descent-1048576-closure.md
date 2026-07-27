---
kind: claim
claim_id: h19-k23-shared-selector-tail-descent-1048576-closure
title: H19-k23 共享选择器 1048576 层的普通双尾递降闭合
statement: H19-k23 共享 Type II 选择器 1048576 层审计中的2270418个实际素数记录均有普通 Type II 双尾严格递降。其中2265174条直接沿最小共享缺口递降，5244条经完整p-1因子缺口扫描找到替代递降，零遗漏。替代记录来自共享缺口27,43,51,55,63,67,75,83,87；因此较524288层新增67和75两类，但不构成遗漏。
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

# H19-k23 共享选择器 1,048,576 层的普通双尾递降闭合

紧凑共享证书产物保留每个点的 \(p,m,x,d\)，并独立重建所有普通双尾源。结果为

\[
2\,270\,418=2\,265\,174_{\text{shared-gap descents}}
+5\,244_{\text{alternative descents}}+0_{\text{misses}}. \tag{1}
\]

替代记录按原共享缺口分布为

\[
5\,081_{27}+84_{43}+33_{51}+33_{55}+7_{63}+1_{67}
+2_{75}+1_{83}+2_{87}. \tag{2}
\]

完整替代扫描检查了

\[
3\,579\,046
\]

个 \(p-1\) 的 \(4\) 倍数因子缺口，未发现普通双尾递降遗漏。新出现的 \(67,75\)
只是最小共享缺口的有限谱扩展；最大最小共享缺口仍为 \(99\)。

这是 H19-k23 有限样本的精确闭合，不是原猜想的归纳证明，也不证明共享选择器在全体
核心素数上有界。

重建命令：

~~~bash
python3 reproductions/h19_k23_shared_selector_tail_descent_closure.py \
  --input reproductions/h19-k23-shared-selector-audit-1048576.json \
  --output reproductions/h19-k23-shared-selector-tail-descent-1048576.json
~~~
