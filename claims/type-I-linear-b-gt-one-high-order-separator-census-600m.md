---
kind: claim
claim_id: type-I-linear-b-gt-one-high-order-separator-census-600m
title: 两百个完整线性谱中的高阶 G 型分离角色普查
statement: 对六亿冻结压力集中首达一般 B 证书取 B>1 的200个核心素数，完整线性谱的6522个G型状态逐项重建最小分离二幂角色阶。6461个最小阶为2、49个为4、12个为8；61个高阶状态属于57个素数。涉及高阶状态的同源共享奇素因子关系有387条，其中恰有两条两端均高阶：p=159108889的R=47227与53036295在q=70841相交，及p=403509649的R=843与33625803在q=211相交。故“所有G型障碍均为二次”与“两个高阶G型状态共享素因子必不相容”都不能作为一般选择器证明步骤。此为有限完整谱审计，不推出全称选择器或反例。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- subgroup-character
- quadratic-character
- order-four-character
- order-eight-character
- shared-factors
- exhaustive-computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 两百个完整线性谱中的高阶 G 型分离角色普查

## 审计对象

输入是[两百个首达 B 大于一线性证书的完整谱重选剖面](type-I-linear-b-gt-one-full-spectrum-profile-600m.md)
冻结的 200 个核心素数。对其中每一个 G 型状态

\[
-1\notin\mathcal H_R(K),
\qquad
K=\frac{pR+1}{4},
\]

程序重新分解 \(K\)，重建 \((\mathbb Z/R\mathbb Z)^\times\) 的离散对数格证书，并求使
\(-1\) 首次脱离二幂饱和支持格的最小二幂角色阶。这个数为 \(2\) 时存在二次分离角色；
为 \(4\) 或 \(8\) 时，纯二次角色不足以处理该状态。

同时，对同一 \(p\) 的每一对 G 型状态检查 \(K\) 的共享奇素因子。只保存至少一端为高阶的
关系，以筛选可能容纳高次互反比较的实际输入。

## 结果

\[
\begin{array}{c|r}
\text{最小分离二幂角色阶}&\text{G 型状态数}\\ \hline
2&6{,}461\\
4&49\\
8&12\\ \hline
\text{合计}&6{,}522
\end{array}
\]

因此有 \(61=49+12\) 个高阶状态，分布在 57 个核心素数中。它们不是只出现在此前已知的
\(p=57{,}399{,}241\) 或 \(p=536{,}944{,}489\) 的孤立边界。

高阶状态参与的同源共享奇素因子关系共有 387 条，涉及 342 对 \((R,R')\)。其中只有如下两条
关系的两端都需要高阶角色：

| \(p\) | \(R\) | \(R'\) | 最小阶 | 共享奇素数 \(q\) |
| ---: | ---: | ---: | ---: | ---: |
| 159,108,889 | 47,227 | 53,036,295 | \(4,4\) | 70,841 |
| 403,509,649 | 843 | 33,625,803 | \(4,4\) | 211 |

前一条的 \(70{,}841\equiv1\pmod4\)，所以两个状态的局部四次分量可被拉回到同一个高斯
素因子；后一条的 \(211\equiv3\pmod4\)，不属于该分裂高斯素数情形。两条关系在当前所有
支持角色条件下均实际存在，故共享素因子本身不是矛盾。

此外，1,607 个 G 型状态存在 \(t\equiv3\pmod4\) 的半块二残数注入，1,085 个状态满足
\(-1\in\langle2\bmod R\rangle\)，且逐项没有状态同时满足二者。这与
[半块二残数逃逸](type-I-linear-half-block-two-residue-escape.md)一致；它描述了排除 G 型的
必要机制，不能关闭已存在的 G 型状态。

## 含义与边界

这份审计给出两条严格的路线边界：

1. 不能把二次互反拉回提升为无例外的全称桥；至少 61 个有限样本状态需要四阶或八阶相位。
2. 也不能断言两个高阶 G 型状态一旦在 \(K\) 的素因子上相交便自动不相容；上表是直接反例。

\(p=159{,}108{,}889\) 的第一行是目前最小的有效相位比较对象：其共享素数可分裂，且两端都
有真正四阶分离角色。下一步必须保留四次相位、源标签和两个不同模数的局部分量；仅平方为二次
角色会再次退化为不足以强制逃逸的影子条件。

本页不证明存在命中 \(R\)，也不构成混合终端选择引理的证明或反例。它的作用是把高次互反的
后续工作缩小到可重放的最小跨源对象，并排除两条过强但自然的简化路线。

## 复现

~~~bash
python3 reproductions/type_i_linear_b_gt_one_high_order_separator_census_600m.py
python3 -m unittest tests.test_type_i_linear_b_gt_one_high_order_separator_census_600m -v
~~~
