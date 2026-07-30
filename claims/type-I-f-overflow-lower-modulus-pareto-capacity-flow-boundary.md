---
kind: claim
claim_id: type-I-f-overflow-lower-modulus-pareto-capacity-flow-boundary
title: 低模数 Pareto 溢出的局部超载与全局可行流边界
statement: 对冻结的 42 个低模数 F-box miss，可精确闭合全部单位权最小值及 111 个单位最优 Pareto 需求列。若块、模数差、标签差资源仅在因子支撑的 R 窗口内池化，即使三通道完全可加，\(p=62704849\) 的完整目标纤维仍由共同价格 \((5,6,5)\) 严格分离：需求价格至少 65，而容量价格为 64。若进一步取消 R 窗口并把完整线性源谱全局池化，则存在覆盖全部 42 个状态的整数三通道流，需求为 210，使用 75 个 \((p,q)\) 资源且仅 3 个饱和。因此无局部性的最乐观容量模型不能产生超载证明；局部窗口可以产生条件性障碍，但溢出到资源消耗的算术映射仍未证明。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-I-f-overflow-lower-modulus-pareto-overflow
  - type-I-f-overflow-lower-modulus-weighted-cost-interface
  - type-I-pareto-overflow-capacity-separation-theorem
  - type-I-linear-hybrid-label-modulus-q-adic-capacity
topics:
- type-I
- F-state
- lower-modulus
- Pareto-frontier
- integer-flow
- convex-duality
- q-adic
- capacity
- locality
- finite-audit
- proof-program
sources:
- claim: type-I-f-overflow-lower-modulus-pareto-overflow
  role: truncated-pareto-input
- claim: type-I-pareto-overflow-capacity-separation-theorem
  role: common-price-separation
- claim: type-I-linear-hybrid-label-modulus-q-adic-capacity
  role: local-capacity-interface
visibility: public
last_checked: '2026-07-30'
---

# 低模数 Pareto 溢出的局部超载与全局可行流边界

## 精确需求集

对状态 \(s\) 的低模数目标纤维 \(F_s\)，记

\[
e_s(z)_i=(|z_i|-\nu_i)_+,
\qquad
\Omega_1(s)=\min_{z\in F_s}\sum_i e_s(z)_i,
\]

并定义单位权最优需求集

\[
E_s^{(1)}
=
\left\{
e_s(z):z\in F_s,
\sum_i e_s(z)_i=\Omega_1(s)
\right\}.
\tag{1}
\]

\(E_s^{(1)}\) 与 Smith 原像或 BFS 代表的选择无关，并且每个成员都是全局
Pareto 极小点。否则若有严格较小的可实现向量逐坐标支配它，其单位总成本也会严格
小于 \(\Omega_1(s)\)，矛盾。

cap-9 Pareto 前沿已经完整给出 36 个状态的单位最小壳层。对其余 6 个状态，脚本用
一条已验证目标关系的溢出成本作为上界，把坐标分成两半；对每个半边剩余类只保留
最低单位成本及该成本下的全部溢出模式，再匹配乘积为 \(-1\pmod t\) 的剩余类。
任何全局最小表示的两个半边都必须分别是相应剩余类的最低成本表示，故该
meet-in-the-middle 计算完整保留全部单位最优模式。

6 个此前只有下界的精确值为：

| \(p\) | \(t\) | \(\Omega_1\) |
|---:|---:|---:|
| 62704849 | 649 | 12 |
| 75056809 | 21113 | 11 |
| 310002289 | 107977 | 18 |
| 312918169 | 16649 | 10 |
| 366108649 | 11057 | 12 |
| 373561609 | 208577 | 15 |

全部 42 个状态共有 111 个单位最优需求列，并且

\[
\sum_s\Omega_1(s)=197.
\]

精确分布为：

~~~text
1:12, 2:8, 3:2, 4:4, 5:2, 6:2, 7:2, 8:3, 9:1,
10:1, 11:1, 12:2, 15:1, 18:1
~~~

## 三通道整数流

资源坐标为 \((p,q,c)\)，其中

\[
c\in
\left\{
\operatorname{block},
\operatorname{modulus\ difference},
\operatorname{label\ difference}
\right\}.
\]

对每个有序线性源槽，三个高度分别取：

\[
\begin{aligned}
h^{\mathrm{block}}_{q}
&=
\max\{v_q(aR+1),v_q(sR+1)\},\\
h^{\mathrm{mod}}_{q}
&=
\max_{R'\ne R}v_q((R-R')/4),\\
h^{\mathrm{label}}_{q}
&=
\max_{\substack{x\in\{a,s\}\\y\ne x}}v_q(x-y).
\end{aligned}
\tag{2}
\]

令 \(x_{s,e}\in\{0,1\}\) 表示状态 \(s\) 选择需求列 \(e\)，并令
\(y_{s,q,c}\in\mathbb Z_{\ge0}\) 表示其向通道 \(c\) 路由的整数层数。模型为

\[
\sum_{e\in D_s}x_{s,e}=1,
\tag{3}
\]

\[
\sum_c y_{s,q,c}
=
\sum_{e\in D_s}e_qx_{s,e},
\qquad
\sum_s y_{s,q,c}\le C_{p,q,c}.
\tag{4}
\]

脚本按核心素数分块完整枚举离散选择，再给出逐通道的整数流；因此这里报告的
“可行”是整数可行，不只是凸松弛可行。

## 因子支撑窗口的完整纤维障碍

局部模型对固定 \((p,q)\) 只把满足

\[
R_{\min}(p,q)\le R\le R_{\max}(p,q)
\]

的源槽放入容量池；窗口端点取冻结 42 状态中因子分解含 \(q\) 的全部状态。
模数差和标签差的比较对象仍允许来自完整源谱，三个通道也完全相加，因此该模型在
窗口内已经有意放宽。

对

\[
p=62704849,
\qquad
t=649,
\qquad
(q_1,q_2,q_3)=(53,349,1650083),
\]

三通道可加容量为

\[
C=(6,4,2).
\]

完整单位最优集为

\[
E_s^{(1)}
=
\{(1,11,0),(2,10,0),(3,9,0)\},
\qquad
\Omega_1=12.
\]

取共同正价格

\[
w=(5,6,5).
\]

则容量价格为

\[
w\cdot C
=
5\cdot6+6\cdot4+5\cdot2
=64.
\tag{5}
\]

单位最优三列的最低价格为 69。任何其它目标关系的单位总成本至少为 13，故其价格
至少为

\[
13\min_i w_i=65.
\]

所以对整个无限目标纤维，而不只是已枚举的 3 个最优表示，均有

\[
\boxed{
\min_{z\in F_s}w\cdot e_s(z)
\ge65>64=w\cdot C
}.
\tag{6}
\]

这是严格的有限共同价格证书：在局部三通道账本的条件下，允许任意非最优表示也不能
修复该状态。

## 取消窗口后的可行反例

再把模型放宽为：对每个 \((p,q)\)，允许使用该核心素数完整线性源谱中的所有源槽，
三个通道仍完全独立相加。此时若只允许 \(E_s^{(1)}\)，仍有 5 个核心素数不可行；
这说明“先各自最小化单位成本，再装箱”并不是正确的全局选择规则。

脚本随后对每个状态按单位总成本递增，完整判定容量盒内每个溢出向量是否命中目标
纤维。第一次命中的向量仍是全局 Pareto 点：若有严格支配它的目标向量，该向量也在
同一容量盒内且单位成本更低，已应更早命中。共检查 41096 个溢出向量；42 个状态
全部得到候选。5 个状态必须有意放弃单位最小表示：

| \(p\) | \(t\) | \(\Omega_1\) | 所选成本 | 所选溢出向量 |
|---:|---:|---:|---:|---|
| 99151369 | 27337 | 9 | 12 | \((0,0,11,1,0)\) |
| 223474729 | 233 | 8 | 10 | \((2,6,2)\) |
| 312918169 | 16649 | 10 | 12 | \((4,6,2,0,0)\) |
| 366108649 | 11057 | 12 | 16 | \((5,8,1,2)\) |
| 487572409 | 106017 | 8 | 10 | \((0,5,0,3,2)\) |

最终得到覆盖 42 个状态、35 个核心素数的整数流：

~~~text
total demand: 210
used (p,q) resources: 75
maximum demand/capacity ratio: 1
saturated resources: 3
~~~

三个饱和坐标为
\((223474729,56393)\)、\((366108649,4693697)\)、
\((487572409,6965317)\)，其需求和容量均为 2。

因此，若“最乐观资源模型”允许跨越全部 \(R\) 窗口全局池化，冻结 42 状态并不必然
超载；JSON 中给出的逐状态表示及逐通道流是一个显式反例。真正有辨识力的容量定理
必须证明局部性或迁移成本，不能只证明完整源谱的总资源有限。

## 逻辑边界

上述有限结论分为两层：

1. 目标关系、\(\Omega_1\)、Pareto 列、各整数的 \(q\)-进高度、价格不等式和流可行性
   都是精确有限结论。
2. “一个盒外指数层必须消耗一个块、标签差或模数差资源单位”尚未证明。三通道相加
   还可能重复计算同一个算术来源，全局模型更允许需求跨 \(R\) 窗口迁移。

所以 (6) 不是 Erdos--Straus 猜想的无条件反证式矛盾；它说明一旦能证明局部收费
映射，已经存在严格的容量障碍。反过来，全局可行流也不是实际 Type I/II 证书；它只
排除了“忽略局部性、依靠最乐观总容量仍必超载”的证明策略。

下一条真正需要证明的桥应是以下二者之一：

- 盒外层只能在因子支撑的 \(R\)-窗口内收费，或跨窗口迁移必须支付额外严格高度；
- 若无法建立这样的局部收费，则该表示产生一个更小且可提升的算术状态。

## 复现

~~~bash
python3 reproductions/type_i_f_overflow_lower_modulus_pareto_capacity_flow.py
~~~

结果文件：

~~~text
reproductions/type-i-f-overflow-lower-modulus-pareto-capacity-flow-results.json
~~~

结果 SHA-256：

~~~text
993b3280dd8551e7c26bfbf9164f68172c87ac1412b6827c3bda8b44647b6cb4
~~~
