---
kind: claim
claim_id: type-I-source-state-b1-overflow-profile
title: Type I源状态B等于1失败的平方除子溢出剖面
statement: 对H19十亿的17个与五亿普通尾的72个B=1失败，完整枚举F|K^2且4F=-1 modR，并从F规范恢复有效正规形。89个点均在K的指数库存之外只需额外1或2次素因子：81个最小溢出为1、8个为2。
claim_status: computationally_reproduced
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

# Type I 源状态 B 等于 1 失败的平方除子溢出剖面

对 $B=1$，需要 $K$ 的一个除子命中 $-1/4pmod R$。若它失败，改在平方因子盒中枚举

$$
Fmid K^2,\qquad 4F\equiv-1pmod R. \tag{1}
$$

对每个命中的 $F$，将其超出 $K$ 的指数部分规范化为

$$
B=\frac F{\gcd(F,K)},
$$

再恢复 $C,H,A,m$ 并逐项核验源、目标恒等式。定义溢出代价为 $F$ 中超过 $K$ 现有指数的
总次数。两个独立压力集的89个 $B=1$ 失败给出

$$
89=81_{\text{最小溢出 }1}+8_{\text{最小溢出 }2}. \tag{2}
$$

其中 H19 十亿部分为 $15+2$，五亿普通尾部分为 $66+6$。因此这些边界并不需要新的素因子
剩余类，只差已有因子的极低重复指数。需要注意：低指数溢出不保证小整数 $B$，所以 (2) 不能
替代小 $B$ 菜单；它更适合作为源状态势函数或“重复因子触发替代递降”的候选。

可复现命令：

~~~bash
python3 reproductions/type_i_source_state_b1_overflow_profile.py
python3 -m unittest tests/test_type_i_source_state_b1_overflow_profile.py -q
~~~
