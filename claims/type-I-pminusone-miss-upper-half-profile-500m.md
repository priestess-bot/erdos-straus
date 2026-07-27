---
kind: claim
claim_id: type-I-pminusone-miss-upper-half-profile-500m
title: 五亿 p减一桥遗漏的最短上半区源剖面
statement: 在 p<=500000000、m<=215 的共享 Type I 正规形盒中，普通 Type II p-1 双尾遗漏的185个 p-1 桥遗漏均有非 p-1 的最短偶源小侧桥。其源距离 p-n 的最小值为3、最大值为48244917；126种桥因子 E 和18种正规形 B 值出现。因此该有限压力集的上半区 Type I 分支不能收缩为 p-1 源、固定短距离或固定桥因子菜单。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- p-minus-one
- upper-half-source
- normal-form
- small-side
- selector-boundary
- finite-audit
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-and-terminal-bridge-context
visibility: public
last_checked: '2026-07-28'
---

# 五亿 p减一桥遗漏的最短上半区源剖面

输入为 [p减一桥边界](type-I-tail-reverse-pminusone-boundary-500m.md)中的全部

\[
185
\]

个普通 Type II \(p-1\) 双尾遗漏。将它们逐点连接到
[最短偶源距离剖面](type-I-tail-reverse-even-source-min-distance-boundary-500m.md)的见证；后者在相同

\[
p\le5\cdot10^8,\qquad 3\le m\le215,\qquad m\equiv3\pmod4
\]

正规形盒中，完整枚举 Type I 正规形及严格最大尾反向提升，并最小化偶源距离 \(p-n\)。

对每一条连接记录，程序从保存的 \((m,A,B,C,E)\) 重新计算

\[
R=\frac{4B^2C+1}{m},\qquad
K=BC(AR-B),\qquad L=2K,
\]

并精确验证

\[
4K=pR+1,\qquad E\mid4K^2,\qquad E\equiv1\pmod R,
\qquad n=\frac{4K-E}{R}.
\]

再把 \(E/L\) 既约化为 \(a/b\)，验证

\[
(a,b)=1,\qquad a,b\mid L,\qquad a<b,\qquad a\equiv2b\pmod R,
\]

以及目标、源两边的单位分数恒等式。因此每条记录都是一个
[小侧--上半区等价](type-I-normal-even-source-small-side-simplification.md)意义下的上半区偶源桥。

## 结果

| 项目 | 数值 |
| --- | ---: |
| \(p-1\) 桥遗漏 | 185 |
| 已连接的最短偶源记录 | 185 |
| 小侧上半区桥 | 185 |
| 上半区遗漏 | 0 |
| 最小源距离 \(p-n\) | 3 |
| 最大源距离 \(p-n\) | 48,244,917 |
| 不同桥因子 \(E\) | 126 |
| 不同正规形 \(B\) 值 | 18 |

最短距离并不集中成一个可用于全称证明的固定菜单：距离 \(9\) 出现 72 次，然而仍有 18
条记录的最短距离超过 \(p/1000\)。最大距离点是

\[
p=493936249,\quad n=445691332,\quad p-n=48244917,
\quad(m,A,B,C)=(215,21,1,5880196).
\]

最大桥因子出现于

\[
p=357834409,\quad E=14187863155684,
\quad(m,A,B,C)=(95,1,1,89458626).
\]

## 含义与边界

这一结果与 p减一边界合在一起给出精确的有限图景：在共享正规形盒中，185 点都**不能**以
\(p-1\) 为源，但都可以用别的上半区偶源终止。故
[上半区混合终端选择猜想](type-I-upper-half-mixed-terminal-selector-conjecture.md)的 Type I 分支必须允许
实际因子状态驱动的源和正规形重选。

它并不证明全称混合终端选择引理，也没有证明不存在某个更一般的参数化短源规则；排除的是
本有限压力集中的 \(p-1\) 收缩、固定短距离收缩和固定桥因子收缩。

重建命令：

~~~bash
python3 reproductions/type_i_pminusone_miss_upper_half_profile_500m.py
python3 -m unittest tests/test_type_i_pminusone_miss_upper_half_profile_500m.py -q
~~~
