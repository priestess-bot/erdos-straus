---
kind: claim
claim_id: shifted-quadratic-source-distance-parametrization
title: 平移平方外源射线的源距离因子参数化
statement: 对 p=1 mod24，平移平方外源的兼容参数 (k,s) 与正源距离 d、整数 t 的数据双射：p-d=s(dt+1)、st=3 mod4、k=(st+1)/4。故固定源距离时，候选平移正是 p-d 的满足同余条件的因子；固定平移时，候选 k 正是 (p-s)/4 的因子。
claim_status: established
topics:
- type-I
- descent
- external-source
- parametrization
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: Type-I-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 平移平方外源射线的源距离因子参数化

设 $p\equiv1\pmod {24}$。平移平方外源的一条兼容射线由正整数 $(k,s)$ 给出，满足

$$
0<s<p,\qquad p-s\equiv0\pmod {4k},\qquad s\mid(4k-1). \tag{1}
$$

令

$$
d=\frac{p-s}{4k},\qquad t=\frac{4k-1}{s}.
$$

则 $d,t>0$，并且

$$
p-d=s(dt+1),\qquad st\equiv3\pmod4,\qquad k=\frac{st+1}{4}. \tag{2}
$$

反之，任意正整数 $(d,s,t)$ 满足式 (2) 的前两个条件，令
$k=(st+1)/4$，便恢复式 (1)，且源分母正是 $p-d$。因此这是一一对应。

证明只需代入 $4k=st+1$：

$$
p-s=d(4k)=d(st+1),
\quad\text{故}\quad p-d=s(dt+1).
$$

同余式保证 $k$ 为整数，反向计算立即得到 $p-s=4kd$ 与 $4k-1=st$。

这个重参数化把原先容易误解为“搜索 $k$”的问题转成因子选择问题：固定偏移 $s$ 时，
$k\mid(p-s)/4$；固定源距离 $d$ 时，$s\mid p-d$，还须满足

$$
d\mid\left(\frac{p-d}{s}-1\right),\qquad
s\frac{(p-d)/s-1}{d}\equiv3\pmod4. \tag{3}
$$

它不保证平方尾因子存在，后者仍是递降选择器的核心难点；但它给出正确的外层状态空间。
例如一亿压力集的两个最大偏移边界都取 $d=4$：

$$
878085=3705(4\cdot59+1),\qquad
5478165=7161(4\cdot191+1).
$$

相应 $st\equiv3\pmod4$，并分别恢复 $k=54649,341938$。
