---
kind: claim
claim_id: h19-k23-m27-canonical-support-defect-1048576
title: H19-k23 m=27 替代尾的规范支持缺陷审计
statement: 在1048576层 H19-k23 的5081条原共享缺口m=27替代尾中，按每个首个普通尾缺口的规范基底重算最小支持缺陷delta_B，全部满足delta_B<=2，且精确分布为2419条缺陷0、2631条缺陷1、31条缺陷2、零条缺陷大于2或无证书。全局可用尾使用最大仿射统一基底B_m=rad(qg_m)；非全局的m=63仅使用q的素因子{2}，仍无遗漏。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- divisor-selection
- factor-support
- potential-function
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: ordinary-Type-II-tail-context
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 \(m=27\) 替代尾的规范支持缺陷审计

取 1,048,576 层普通双尾闭合中原共享缺口为 \(27\) 且需要替代尾的全部 5,081 条记录。
对其按 \(p-1\) 递增扫描得到的**首个**尾缺口 \(m=4q-1\)，使用

\[
B_m=\operatorname{rad}(qg_m),
\qquad g_m=\gcd(a,b_1,\ldots,b_{14}), \tag{1}
\]

其中 \(u=(p+m)/(m+1)=at+b_i\)。这是全局可用尾的最大仿射统一基底，见
[H19-k23 普通双尾的最大统一基底不变量](h19-k23-uniform-tail-base-invariant.md)。
\(m=63\) 不全局可用，故审计刻意只取 \(q=16\) 的素因子 \(\{2\}\)，而不从该
子样本额外抽取固定因子。

对每个点穷尽 \(x^2=q^2u^2\) 中所有基底除子、至多两个不同非基底素数的全部合法幂，
并逐项以平方根补全标准形核验。因为按支持度 \(0,1,2\) 顺序穷尽，首次命中即为精确
最小缺陷 \(\delta_{B_m}\)。结果为：

\[
5\,081=2\,419_{\delta=0}+2\,631_{\delta=1}+31_{\delta=2}
+0_{\delta>2\text{ or miss}}. \tag{2}
\]

| 首尾缺口 | \(\delta=0\) | \(\delta=1\) | \(\delta=2\) |
|---:|---:|---:|---:|
| 31 | 2287 | 1443 | 0 |
| 35 | 0 | 734 | 2 |
| 39 | 0 | 278 | 15 |
| 47 | 83 | 131 | 9 |
| 59 | 42 | 33 | 1 |
| 63 | 0 | 5 | 1 |
| 71 | 5 | 5 | 1 |
| 79 | 2 | 1 | 1 |
| 91 | 0 | 1 | 0 |
| 95 | 0 | 0 | 1 |

先前的分层支持度二梯得到 \(2\,419+2\,628+34\)，并不被 (2) 否定。旧审计为构造性
便利，只允许某些基底素数的固定指数；本审计按 \(\delta_B\) 的定义允许基底素数在
\(x^2\) 中的所有合法幂。恰有三条记录因此从“二新增”降为“一新增”：分别位于
\(m=35,63,79\)。所以 (2) 是对规范支持缺陷的更强、但同样有限的表述。

这仍不证明跨缺口势能律：它仅表明在该加倍样本及此首尾链上，没有出现规范缺陷三。
下一步必须证明缺陷三会强制后续缺口下降、另一类递降，或构造其真实反例。

重建命令：

~~~bash
python3 reproductions/h19_k23_canonical_tail_support_defect_audit.py \\
  --input reproductions/h19-k23-shared-selector-tail-descent-1048576.json \\
  --output reproductions/h19-k23-canonical-tail-support-defect-1048576.json
python3 -m unittest tests/test_h19_k23_canonical_tail_support_defect_audit.py -q
~~~
