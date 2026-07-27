---
kind: claim
claim_id: type-I-source-state-one-repeat-boundary
title: Type I源状态的一重复因子选择器与两重复边界
statement: 对一个固定已选偶源状态，若存在素数q与因子D满足q|D|K、4qD=-1 modR及gcd((K/D+q)/R,q)=1，则取B=q、C=D/q得到严格Type I正规形反向边。H19十亿664条固定状态中B=1或一重复覆盖662条、留2条两重复边界；五亿1717条固定状态中覆盖1711条、留6条两重复边界。
claim_status: established
topics:
- type-I
- normal-form
- descent
- source-state
- divisor-residues
- exponent-overflow
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# Type I 源状态的一重复因子选择器与两重复边界

在 [源状态单残数实现判据](type-I-normal-source-state-realization.md) 中，取一个已存在的素因子
$q$ 作为 $B$。若

$$
q\mid D\mid K,\qquad 4qD\equiv-1\pmod R,\qquad
\gcd\left(\frac{K/D+q}{R},q\right)=1, \tag{1}
$$

则令

$$
B=q,\qquad C=\frac Dq,\qquad H=\frac KD
$$

便满足正规形实现条件，恢复严格偶源 Type I 反向边。这是一个完全可读出的“一重复因子”
证书：只需在 $K$ 的因子中选择一个被标记素数 $q$ 整除的 $D$。

对两个独立压力集，先取 $B=1$，失败后再完整枚举 (1)，得到

$$
664=647_{B=1}+15_{\text{一重复}}+2_{\text{两重复边界}},
$$

以及

$$
1717=1645_{B=1}+66_{\text{一重复}}+6_{\text{两重复边界}}.
$$

故89个 $B=1$ 失败中，81个已由一重复分支严格终止；真正需要至少两次指数溢出的仅8个。
这些是固定已选源状态的边界，并非目标级反例；逐目标改选正规形后，两个压力集已由
$B=1,2,8$ 直接闭合，见
[H19与五亿尾遗漏的目标级小B偶源闭合](type-I-direct-small-b-even-source-audit.md)。它仍没有给出
从任意源状态选择 $q$ 的全称规则。

可复现命令：

~~~bash
python3 reproductions/type_i_source_state_one_repeat_boundary.py
python3 -m unittest tests/test_type_i_source_state_one_repeat_boundary.py -q
~~~
