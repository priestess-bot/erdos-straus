---
kind: claim
claim_id: type-I-source-state-b1-product-boundary
title: Type I源状态B等于1失败的有限积集边界
statement: 对H19十亿的17个与五亿普通尾的72个B=1单除子剩余失败，目标类-1/4 modR全部属于K的素因子剩余所生成的乘法子群；但K的实际有限除子积集均未命中。共89个失败中子群障碍为0、有限积集障碍为89。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- source-state
- divisor-residues
- product-set
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# Type I 源状态 B 等于 1 失败的有限积集边界

由 [B 等于 1 单除子剩余判据](type-I-normal-source-state-b1-realization.md)，失败恰表示
$K$ 的全部实际除子都避开目标类

$$
-\frac14pmod R. \tag{1}
$$

对每个失败状态，进一步忽略每个素因子的实际指数上限，只取 $K$ 的素因子残数生成的乘法
子群。两个独立压力集的完整结果为：

$$
17_{\mathrm{H19}}+72_{\mathrm{500M}}=89
$$

个 $B=1$ 失败中，目标类全部落在该生成子群内；但在每一个点都不属于有限除子积集。因此

$$
89_{\text{有限积集/指数障碍}}
+0_{\text{子群或角色障碍}}. \tag{2}
$$

这排除了用单纯单位群角色来解决当前 $B=1$ 边界的希望。下一步必须控制素因子指数、重复因子，
或证明有限积集失败触发外部尺度/较大 $B$ 的替代证书。结论只针对存储的两类有限压力集。

可复现命令：

~~~bash
python3 reproductions/type_i_source_state_b1_product_boundary.py
python3 -m unittest tests/test_type_i_source_state_b1_product_boundary.py -q
~~~
