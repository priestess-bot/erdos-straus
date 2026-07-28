---
kind: claim
claim_id: type-I-linear-label-reselection-profile-31m
title: 三千一百万以内普通尾遗漏的三标签层线性源重选剖面
statement: 对p不超过31000000的全部200个冻结普通Type II p-1双尾遗漏，完整枚举每个p的全部线性源谱，并按全谱坐标标签把每个一般B目标命中分为源碰撞、源私有、仿射碰撞、仿射私有四层。每个p均可重选到至多三层的命中：185点一层、13点两层、2点三层。全体2779个有向命中中仍有29个需四层，故该结论本质上依赖源重选；两个三层点13782409与26034649各自在完整谱中只有一条目标命中，故两层重选界在该范围已被反驳。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- target-square-divisor
- coordinate-label
- reselection
- collision
- private-factors
- terminal-bridge
- finite-product
- exhaustive-computation
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 三千一百万以内普通尾遗漏的三标签层线性源重选剖面

## 审计对象

输入为冻结的五亿普通 Type II \(p-1\) 双尾遗漏表，并取其中全部

\[
p\le31{,}000{,}000. \tag{1}
\]

这给出恰好200个严格递增的核心素数，末项为

\[
30{,}997{,}849, \tag{2}
\]

下一项已超过该上界。输入素数表的换行 SHA-256 为
`7d5ce7fdacdb45e44c8293f5fe1285cc1d5a691bf029b02e9d5a4d73cd5cd203`。

对每个 \(p\)，完整枚举所有线性源

\[
p=a+s+asR,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4, \tag{3}
\]

及其全部诱导模数 \(R\)。对每个状态，令

\[
K=\frac{pR+1}{4}=\gamma L,\qquad
G_c=(\gamma,J_s),\ G_p=\gamma/G_c,\quad
L_c=(L,J_a),\ L_p=L/L_c, \tag{4}
\]

其中 \(J_t\) 由这个 **同一 \(p\) 的完整源谱** 的坐标标签差定义，详见
[标签层支撑分解](type-I-linear-label-layer-support-profile.md)。程序对每一个
\(R\) 直接判定

\[
-1\in\mathcal C_R(K), \tag{5}
\]

并对每个实际命中状态枚举四层的15个非空子积。选定最小层支撑、再按
\((R,a,s)\) 字典序打破平局的状态。

## 重选结果

每一个素数至少有一张一般 \(B\) 目标命中，且最短层支撑为

| 重选后的最小层数 | 素数数 |
| ---: | ---: |
| 1 | 185 |
| 2 | 13 |
| 3 | 2 |
| 4 | 0 |
| **合计** | **200** |

所以在此完整有限范围内，重选后恒有

\[
\ell_{\rm reselect}(p)\le3. \tag{6}
\]

这不是因为四层状态不存在。对全部目标命中的有向状态（而非每素数只保留一张）统计为

| 固定状态的最小层数 | 有向命中数 |
| ---: | ---: |
| 1 | 1,734 |
| 2 | 839 |
| 3 | 177 |
| 4 | 29 |
| **合计** | **2,779** |

因此 (6) 是一个真正的**源重选**现象；它不能由“任意命中都天然是三层以内”解释。
[372409 的四层边界](type-I-linear-four-label-layer-boundary-372409.md)给出了固定状态需要四层的
完全显式实例。

## 两层界的尖锐反例

两点的完整源谱根本没有一层或两层替代命中：

| (p) | 完整 (R) 数 | 有向源数 | 唯一命中 ((R,a,s)) | 最小层数 |
| ---: | ---: | ---: | --- | ---: |
| 13,782,409 | 41 | 78 | ((131,11680,9)) | 3 |
| 26,034,649 | 27 | 41 | ((187,15460,9)) | 3 |

前者的唯一三层命中已在[三层单点边界](type-I-linear-label-layer-support-profile.md)中给出。后者的
四层值为

\[
(G_c,G_p,L_c,L_p)=(1,421,7,413003), \tag{7}
\]

其唯一最小子集是 \(\{G_p,L_c,L_p\}\)。这两条完整谱反驳如下有限重选加强：

\[
\text{“每个有线性目标命中的素数都可重选到至多两层”。} \tag{8}
\]

另一方面，对任何选定状态，线性源本身给出

\[
E=sR+1,\qquad n=p-s=aE. \tag{9}
\]

因而每张选中证书都逐项验证

\[
2\mid E,\qquad E\mid4K^2,\qquad E\equiv1\pmod R,\qquad
E\le4K-2R. \tag{10}
\]

所以该重选剖面是原混合终端选择引理的严格有限证据，而不只是模群目标命中统计。

## 后续猜想与范围

本页支持但不证明下列更强的开放路线：每个普通双尾遗漏核心素数都存在一个线性源目标命中，
其完整谱标签层支撑至多为三。该命题在下一张开放卡中精确定义。

有限扫描不能控制任意大的 \(p\)，也不能排除某个未来素数所有目标命中都需四层，或根本
没有线性目标命中。故 (6) 不能替代全称混合终端选择引理的证明。

## 可复现检查

~~~bash
python3 reproductions/type_i_linear_label_reselection_profile_31m.py
python3 -m unittest tests.test_type_i_linear_label_reselection_profile_31m -v
~~~
