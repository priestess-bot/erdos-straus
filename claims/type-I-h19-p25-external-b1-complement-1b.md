---
kind: claim
claim_id: type-I-h19-p25-external-b1-complement-1b
title: H19 p等于25模48类的外部尺度--B等于1互补覆盖
statement: H19十亿p≡25 mod48的243条源状态中，237条有B=1内部实现，余6条均被外部尺度终止，其中固定k=2有1条、固定k=6有1条、变量尺度有4条；全部28个外部纯剩余点均有B=1实现。因此外部尺度与B=1内部因子对的并集覆盖全部243条。
claim_status: computationally_reproduced
topics:
- type-I
- normal-form
- descent
- external-source
- variable-scale
- source-state
- hybrid-closure
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# H19 p 等于 25 模 48 类的外部尺度--B 等于 1 互补覆盖

将完整外部尺度审计与 [B 等于 1 源状态边界](type-I-h19-b1-source-state-boundary-1b.md) 交叉：

$$
\#\{p\equiv25\pmod{48}\}=243,\qquad
\#\{B=1\text{ 内部实现}\}=237.
$$

余下6条 $B=1$ 失败点为

$$
165479161,\ 178618441,\ 356911129,\ 675458281,\ 697980889,\ 910014121.
$$

它们全被外部尺度终止：1条在固定 $k=2$、1条在固定 $k=6$、4条在变量尺度分支。反过来，
完整外部尺度族的28个纯除子剩余障碍全部有 $B=1$ 内部实现。因此

$$
\#\{\text{外部尺度终止}\ \cup\ B=1\text{ 内部实现}\}=243. \tag{1}
$$

这是覆盖而非不交分割，且只针对存储的 H19 有限输入。它把下一条全称候选聚焦为“外部尺度
选择器或 $B=1$ 互补因子对选择器”这一双机制，而不是要求其中任一机制单独全覆盖。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_p25_external_b1_complement.py
python3 -m unittest tests/test_type_i_h19_p25_external_b1_complement.py -q
~~~
