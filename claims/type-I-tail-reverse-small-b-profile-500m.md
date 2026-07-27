---
kind: claim
claim_id: type-I-tail-reverse-small-b-profile-500m
title: 五亿普通尾遗漏的低溢出反向二尾选择器剖面
statement: 对五亿普通Type II尾抽缩的1,717个遗漏，完整枚举m<=127的Type I正规形并以E|4K^2检查最大尾反向边。限制B<=5时1,717点全部命中；限制B<=4时唯一遗漏为p=36851929。该点在(m,A,B,C)=(31,34766,5,53)有两条反向边。因此B=5是在这个有限m<=127盒中使该选择器全覆盖的最小整数上界。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- reverse-lift
- normal-form
- finite-audit
- bounded-parameter
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: divisor-certificate-context
- paper: elsholtz_tao2013
  locator: Section 2, Proposition 2.3
  role: Type-I-parametrization-context
visibility: public
last_checked: '2026-07-27'
---

# 五亿普通尾遗漏的低溢出反向二尾选择器剖面

在五亿普通 Type II 尾抽缩的 $1{,}717$ 个遗漏上，限制 Type I 正规形

$$
x=ABC,\qquad3\le m\le127,\qquad m\equiv3\pmod4,
$$

并使用 [最大尾反向二尾选择器](type-I-normal-reverse-two-tail-selector.md) 检查每个
$E\mid4K^2$。这里的 $B$ 是正规形中记录目标除子溢出的坐标，不是一般的素数界。

## 精确低溢出边界

| 限制 | 命中 | 遗漏 |
|---|---:|---:|
| $B\le1$ | 1,707 | 10 点 |
| $B\le2$ | 1,715 | $36851929,193288489$ |
| $B\le3$ | 1,715 | $36851929,193288489$ |
| $B\le4$ | 1,716 | $36851929$ |
| $B\le5$ | 1,717 | 无 |

所以在这个**固定有限盒**中，$B=5$ 是全覆盖所需的最小整数上界。它不是关于所有素数或
所有缺口的无界性定理。

这里的层级并不随 $B$ 平滑增长：$B=3$ 相对 $B=2$ 没有新增命中；从 $B=1$ 到 $B=2$
新增 $8$ 点，从 $B=3$ 到 $B=4$ 只新增 $193288489$，从 $B=4$ 到 $B=5$ 只新增
$36851929$。因此未来若要解释小溢出选择器，必须解释这些离散状态跃迁，而不能仅用
“增大 $B$ 会增大除子数”的粗略计数替代。

唯一 $B\le4$ 残余点在 $B=5$ 时有

$$
p=36{,}851{,}929,\qquad(m,A,B,C)=(31,34{,}766,5,53),
$$

并且最大尾选择器给出两条严格边，其中按源分母最小的一条为

$$
36{,}851{,}929\longrightarrow33{,}401{,}130.
$$

因此“只需普通除子 $B=1$”并不成立，但非常小的溢出预算已覆盖完整五亿尾遗漏集。这把
下一步理论目标进一步集中为：解释为什么 $m\le127,B\le5$ 的目标正规形在有限审计中足够，
并寻找可从源侧生成这种低溢出状态的规则。

可复现命令：

~~~bash
python3 reproductions/type_i_tail_reverse_small_b_profile.py \
  --tail reproductions/type-ii-tail-deflation-500m-full-results.json \
  --gap-cap 127 --b-cap 5 \
  --output reproductions/type-i-tail-reverse-small-b5-500m-results.json
python3 reproductions/type_i_tail_reverse_small_b_profile.py \
  --tail reproductions/type-ii-tail-deflation-500m-full-results.json \
  --gap-cap 127 --b-cap 4 \
  --output reproductions/type-i-tail-reverse-small-b4-500m-results.json
python3 -m unittest tests/test_type_i_tail_reverse_small_b_profile.py -q
~~~
