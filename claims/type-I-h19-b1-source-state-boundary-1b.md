---
kind: claim
claim_id: type-I-h19-b1-source-state-boundary-1b
title: H19偶桥的B等于1源状态实现边界
statement: H19十亿664条最小偶桥源状态中，647条存在B=1的Type I正规形实现，17条没有。在p≡25 mod48的243条中，237条存在B=1实现，6条没有。这给出B=1互补因子对选择器的明确有限边界。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- source-state
- divisor-residues
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# H19 偶桥的 B 等于 1 源状态实现边界

对 H19 十亿源自由集合的664条已最小化偶桥，固定其源状态 $(p,n,E)$，再完整枚举
[源状态实现判据](type-I-normal-source-state-realization.md) 中所有 $BC\mid K$ 的正规形。
其中有647条至少存在一个 $B=1$ 实现，17条则所有兼容正规形均满足 $B>1$：

$$
664=647_{B=1}+17_{B>1\text{ 必需}}.
$$

限制到 $p\equiv25\pmod{48}$ 的243条，得到

$$
243=237_{B=1}+6_{B>1\text{ 必需}}.
$$

这不是全称的 $B=1$ 定理，但把此前的28点现象放入独立大样本：$B=1$ 双因子选择器是强而非
普遍的机制，17点是其明确的有限压力边界。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_b1_source_state_boundary.py
python3 -m unittest tests/test_type_i_h19_b1_source_state_boundary.py -q
~~~
