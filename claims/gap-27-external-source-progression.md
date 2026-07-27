---
kind: claim
claim_id: gap-27-external-source-progression
title: gap-27 的外源同余直接证书族
statement: 对任意正整数p满足27|(p+29)和116|(p+27)，令A=(p+27)/116、B=(p+29)/27，则4/p=1/(29A)+1/(29AB)+1/(pAB)。在核心同余p=1 mod24中，这等价于p=5425 mod6264。五亿偏移边界点477015289属于该族，故有显式Type I直接证书；该公式本身不构成严格递降。
claim_status: established
topics:
- type-I
- congruence-family
- external-source
- parametrization
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# gap-27 的外源同余直接证书族

设

$$
27\mid p+29,\qquad116\mid p+27,
$$

并定义

$$
A=\frac{p+27}{116},\qquad B=\frac{p+29}{27}.
$$

则有恒等式

$$
\frac4p
=\frac1{29A}+\frac1{29AB}+\frac1{pAB}. \tag{1}
$$

证明只需通分。由 $4\cdot29A=p+27$ 与 $27B=p+29$，右边乘以
$p\cdot29A B$ 后的分子为

$$
pB+p+29=(p+27)B=4\cdot29AB.
$$

因此 (1) 是 Type I gap-27 证书，其第一分母为

$$
x=29A=\frac{p+27}{4},
$$

相应因子取 $d=29x=29^2A$。

两个同余条件在模 $\operatorname{lcm}(27,116)=3132$ 下等价于

$$
p\equiv2293\pmod{3132}.
$$

再加核心条件 $p\equiv1\pmod{24}$，得到单一核心进程

$$
p\equiv5425\pmod{6264}. \tag{2}
$$

五亿平移平方外源边界点

$$
p=477{,}015{,}289\equiv5425\pmod{6264}
$$

正属于此族。此时

$$
A=4{,}112{,}201,\qquad B=17{,}667{,}234,
$$

故 (1) 给出一个独立的 gap-27 Type I 直接证书。

这里的“外源”仅指同余参数 $29$，不是已经构造出的严格源到目标提升。虽然 $29<p$ 且
$4/29$ 可解，(1) 的三分母并非由把一条源分母乘以 $p$ 得到。因此该族解释五亿边界点
为何仍有短直接证书，但**不**解决其严格递降缺口。
