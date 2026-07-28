---
kind: claim
claim_id: type-I-linear-four-label-layer-boundary-372409
title: 372409 的完整线性源谱含必须四标签层的 Type I 目标命中
statement: 对普通 Type II 双尾遗漏核心素数 p=372409，完整枚举其31个线性源模数和53个有向状态。五个模数具有一般B目标命中；其中R=471的两个有向状态各自把K精确分为源碰撞、源私有、仿射碰撞、仿射私有四层，且任一真子积的中心化平方除子谱都不含-1，只有四层全取才命中。因此固定成功线性源状态的目标证书不能总被规范为至多三层标签积集；两条状态仍各自给出原混合终端引理要求的偶 Type I 桥。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- target-square-divisor
- coordinate-label
- collision
- private-factors
- finite-product
- terminal-bridge
- boundary
- exhaustive-computation
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 372409 的完整线性源谱含必须四标签层的 Type I 目标命中

## 完整单点谱

取

\[
p=372409. \tag{1}
\]

该素数属于冻结的五亿普通 Type II \(p-1\) 双尾遗漏。完整枚举

\[
p=a+s+asR,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4, \tag{2}
\]

的平方根界给出 31 个不同的 \(R\)、53 个有向状态和44个坐标标签。对每个 \(R\)，令

\[
K_R=\frac{pR+1}{4}, \tag{3}
\]

并直接枚举全部 \(d\mid K_R^2\) 满足

\[
d\equiv-K_R\pmod R. \tag{4}
\]

恰有五个目标命中模数：

\[
R\in\{7,59,83,131,471\}. \tag{5}
\]

它们一共给出 11 个有向命中状态。按[完整线性源谱中目标命中的坐标标签层支撑边界](type-I-linear-label-layer-support-profile.md)
的四层分解，其最小层支撑分布为

\[
8_{\ell=1}+1_{\ell=2}+0_{\ell=3}+2_{\ell=4}. \tag{6}
\]

## 两个四层状态

两个 \(\ell=4\) 状态都有 \(R=471\)，并共享

\[
K=43851160=2^3\cdot5\cdot17\cdot59\cdot1093. \tag{7}
\]

它们只是同一无向分解的两个合法源定向：

\[
(a,s)=(1,789),\qquad (a,s)=(789,1). \tag{8}
\]

相对于所有44个完整谱标签，式 (7) 的四层分别为

\[
\begin{array}{c|cccc}
(a,s)&G_c&G_p&L_c&L_p\\
\hline
(1,789)&85&1093&8&59\\
(789,1)&2&59&340&1093.
\end{array} \tag{9}
\]

每行四项的乘积都是 \(K\)。在完整 \(K^2\) 中，目标平方除子恰为

\[
d\in\{27200,70695743873\},
\qquad d\equiv-K\pmod {471}. \tag{10}
\]

例如第一个定向的较小见证满足

\[
\frac dK
=2^3\cdot5\cdot59^{-1}\cdot1093^{-1}
\equiv-1pmod {471}. \tag{11}
\]

它在四个层中都使用非零中心化指数。更强地，程序对每个真子集

\[
I\subsetneq\{G_c,G_p,L_c,L_p\}
\]

直接枚举 \(N_I^2\) 的全部除子，确认

\[
-1\notin\mathcal C_{471}(N_I) \tag{12}
\]

对两个定向都成立；只有 \(I\) 为全部四层时才有 \(-1\in\mathcal C_{471}(K)\)。
所以这里不存在重新分配同一四层中完整因子而得到的一层、两层或三层目标命中。

## 与原终端目标的关系

这不是抽象的模群例子。对 (8) 的每个定向，令

\[
E=sR+1,\quad n=p-s=aE. \tag{13}
\]

则直接验证

\[
2\mid E,\quad E\mid4K^2,\quad E\equiv1\pmod R,
\qquad E\le4K-2R. \tag{14}
\]

故这两个状态都能恢复原混合终端选择引理所要求的偶 Type I 桥；四层复杂性只出现在
**证明目标平方除子存在**的层面，而不是终端桥本身失效。

## 边界

该单点否定如下过强的压缩：

\[
\text{“每一张成功线性源状态的目标命中均可由至多三层标签子积给出”。} \tag{15}
\]

它不否定对同一个 \(p\) 重新选择另一 \(R\) 或另一源后可能得到较小支撑；事实上 (5) 中
其它命中状态已具有一层或两层见证。因此它不是线性一般 \(B\) 选择器的反例，也不影响
该素数的 Type I 终端闭合。其作用是排除把四层积集理论预先压缩成三层的证明路线。

## 可复现检查

~~~bash
python3 reproductions/type_i_linear_four_label_layer_boundary_372409.py
python3 -m unittest tests.test_type_i_linear_four_label_layer_boundary_372409 -v
~~~
