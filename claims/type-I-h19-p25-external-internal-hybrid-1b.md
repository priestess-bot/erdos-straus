---
kind: claim
claim_id: type-I-h19-p25-external-internal-hybrid-1b
title: H19 p等于25模48类的外部尺度--低支撑内桥混合闭合
statement: H19十亿p≡25 mod48残余的243个点精确分为124个固定k=2终止、48个固定k=6终止、43个变量偶尺度外源终止和28个外源纯剩余障碍；后28个全部由严格偶源Type I正规形内桥终止，其中桥素因子支撑为1的有11个、为2的有17个。故该有限类以243=124+48+43+11+17完全闭合。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- external-source
- variable-scale
- normal-form
- hybrid-closure
- finite-audit
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-context
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-27'
---

# H19 p 等于 25 模 48 类的外部尺度--低支撑内桥混合闭合

H19 十亿源自由残余中，$p\equiv25\pmod{48}$ 的243个点先经外部偶源族得到互斥分流：

$$
243=124_{k=2}+48_{k=6}+43_{\text{变量尺度}}+28_{\text{外部剩余}}.
$$

其中最后28点已被证明在所有允许变量尺度上均没有目标剩余类的除子，见
[变量偶尺度剩余的纯除子剩余障碍](type-I-h19-variable-even-scale-residue-boundary-1b.md)。
将它们与独立的 [H19 偶桥支撑边界](type-I-h19-even-source-support-boundary-1b.md) 对接，
每点均有一条严格、偶源的 Type I 正规形反向边，且其最小桥因子只需一或两种不同素因子：

$$
28=11_{\operatorname{supp}E=1}+17_{\operatorname{supp}E=2}.
$$

所以这个有限同余子类完整闭合为

$$
243=124+48+43+11+17.
$$

这不是统一选择器定理。它反而给出一个更精确的理论靶标：解释为何完整外部尺度族的
纯剩余障碍会强制一个低支撑的内部偶桥，或构造另一条可读出的递降边。有限结果没有说明
该切换能否对任意核心素数发生。

可复现命令：

~~~bash
python3 reproductions/type_i_h19_p25_external_internal_hybrid.py
python3 -m unittest tests/test_type_i_h19_p25_external_internal_hybrid.py -q
~~~
