---
kind: claim
claim_id: h19-k23-global-first-power-selector-conjecture
title: H19-k23 跨全局尾的一新增素因子一次幂选择器猜想
statement: 对 H19-k23 的14条残存仿射进程中的每个实际核心素数 p，猜想存在一个满足 m+1|165600 的全局尾 m=4q-1、一个仅由该尾规范基底素数构成的整数 b，以及一个不在该基底中的素数 ell，使 d=b*ell|((p+m)/4)^2、d<=(p+m)/4 且 d=-(p+m)/4 (mod m)。该数据给出 Type II 短证书和严格双尾递降。
claim_status: open
topics:
- type-II
- conjecture
- descent
- p-minus-one
- global-tail-menu
- factor-support
- one-factor
- cross-tail
- h19
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-26'
---

# H19-k23 跨全局尾的一新增素因子一次幂选择器猜想

H19-k23 的 14 条当前残存进程都满足

\[
165600\mid p-1.
\]

令 \(\mathcal G\) 是所有 \(m=4q-1\) 且 \(m+1\mid165600\) 的 72 个全局尾，令
\(\mathcal B_m\) 是该尾的最大统一仿射规范基底。猜想对每个属于这 14 条进程的实际核心
素数 \(p\)，存在

\[
m\in\mathcal G,\qquad
b\mid x_m^2,\quad
\operatorname{supp}(b)\subseteq\mathcal B_m,\qquad
\ell\notin\mathcal B_m\text{ 为素数}, \tag{1}
\]

使

\[
x_m=\frac{p+m}{4},\qquad
d=b\ell\mid x_m^2,\qquad
d\le x_m,\qquad
d\equiv-x_m\pmod m. \tag{2}
\]

这是一条明确的 Type II 短证书命题。又因为 \(m+1\mid p-1\)，(2) 自动给出

\[
n=\frac{p+m}{m+1}<p \tag{3}
\]

的严格双尾递降；它仍是带标记的递降表示，不能被误作无标记归纳。

## 有限证据与条件性边界

固定规范基底已经有无限素数参数障碍；更强地，任意固定有限的非基底素数支持集也有
无限障碍。因此 \(\ell\) 不可能预先从有限表中选取，必须来自实际 \(u_m=(p+m)/(m+1)\)
的因子化。

有限样本中，新增素因子的高幂不必成为跨尾命题的一部分。在二百万层重写子样本中，46 条
同尾 \(d=b\ell\) 空例都可后移到更大尾的一次幂证书，故全部 5,128 条最终一支持记录均
满足 (1)--(2)，见
[一次幂后移闭合](h19-k23-global-first-power-tail-reroute-2097152.md)。

不过它不能再作为无条件证明路线的首选目标：已有一个 Dickson 条件性逃逸族，使目标素数
与所有 72 尾的剩余非基底仿射余因子同时为素数，且所有这些素因子都落在一次幂禁止残数。
在该假设下，(1)--(2) 对全部尾同时失败，见
[全局一次幂选择器的 Dickson 条件性逃逸](h19-k23-global-first-power-conditional-escape-2097152.md)。
故这个猜想在无条件逻辑中仍是开放命题，却已受到强的条件性反证。更强地，在同一元组上
完整枚举固定部分的全部除子后，高幂和任意多个新增素因子也不能恢复这 72 尾内的 Type II
证书，见 [全局尾完整 Type II 除子的条件性逃逸](h19-k23-global-full-divisor-conditional-escape-2097152.md)。
后续必须转向菜单外尾、不同状态或不同证书类型。

它所保留的自由度为：

\[
\text{尾 }m\text{ 与新素数 }\ell\text{ 随 }p\text{ 无界自适应变化}. \tag{4}
\]

它不宣称有限样本外的覆盖，也不排除某些未来参数需要不同的证书类型或递降状态。

## 可能的证明入口

对两个全局分母 \(d=m+1,e=m'+1\)，相应尾因子满足

\[
d\,u_d-e\,u_e=d-e. \tag{5}
\]

所以除去有限的差值碰撞素数后，各 \(u_d\) 的私有余因子两两互素。单尾总余数与
\(\Omega\) 已被证明不足以强迫 (2)；任何证明必须利用 (5) 的跨尾耦合、私有余因子的
实际素因子分布，或在联合未命中时构造另一种严格下降。

这个命题是研究目标，不是已证结论。
