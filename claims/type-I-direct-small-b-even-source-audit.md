---
kind: claim
claim_id: type-I-direct-small-b-even-source-audit
title: H19与五亿尾遗漏的目标级小B偶源闭合
statement: 对H19十亿664条与五亿普通尾遗漏1717条，直接逐目标枚举m≤215的全部Type I正规形与偶源最大尾反向边。H19全部664条在B=1、最大m=91命中；五亿集合按B=1、2、8分流为1713、3、1条，全部命中且最大m=215。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- even-source
- small-parameter
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# H19 与五亿尾遗漏的目标级小 B 偶源闭合

此前的源状态审计固定了一个已选择的桥，因而其 $B=1$ 或两重复边界可能只是选择效应。这里改为
对每个目标素数直接枚举所有

$$
m\le215,\qquad m\equiv3\pmod4
$$

的 Type I 正规形，并对每张正规形完整枚举最大尾反向边，只保留严格偶源。结果为：

$$
664_{\mathrm{H19}}=664_{B=1},\qquad \max m=91,
$$

以及

$$
1717_{\mathrm{500M}}=1713_{B=1}+3_{B=2}+1_{B=8},
\qquad \max m=215. \tag{1}
$$

五亿集合唯一进入第三阶段的点为 $p=172657489$，其 $B=8$ 边在 $m=111$ 命中。故两个存储的
压力集在目标级均有低 $B$、严格偶源的直接反向边。

这也重新解释了固定源状态的两重复边界：它不是目标级反例。例如 H19 的两个点与五亿的六个点
均在另一张正规形上获得 $B=1$、$2$ 或 $8$ 的边。该结果仍是有限 $m\le215$ 审计，不能推出
对任意核心素数的统一小 $B$ 定理或递归选择规则。

可复现命令：

~~~bash
python3 reproductions/type_i_direct_small_b_even_source_audit.py
python3 -m unittest tests/test_type_i_direct_small_b_even_source_audit.py -q
~~~
