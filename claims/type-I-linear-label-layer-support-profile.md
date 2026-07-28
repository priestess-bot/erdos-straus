---
kind: claim
claim_id: type-I-linear-label-layer-support-profile
title: 完整线性源谱中目标命中的坐标标签层支撑边界
statement: 在11个冻结的完整线性源谱中，对32个实际一般B目标命中及其50个有向线性源，以全谱坐标标签差导出的源碰撞、源私有、仿射碰撞、仿射私有四层精确分解K。14个命中定向可由一层的中心化平方除子谱命中，28个至少需两层，8个至少需三层；没有一个需要全部四层。故“任一既有命中总可由至多两块完整标签层提供”的有限断言为假，但该剖面不产生全称源选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- target-square-divisor
- factorization
- coordinate-label
- collision
- private-factors
- finite-product
- boundary
- exhaustive-computation
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 完整线性源谱中目标命中的坐标标签层支撑边界

## 四层的精确含义

固定一个核心素数 (p) 的完整线性源谱，并取其中的定向状态

\[
p=a+s+asR,
\qquad s\equiv1\pmod2,
\qquad R\equiv3\pmod4.
\]

令

\[
\lambda=
\begin{cases}
4,&s\equiv1\pmod4,\\
2,&s\equiv3\pmod4,
\end{cases}
\qquad
\eta=4/\lambda,
\]

\[
\gamma=\frac{sR+1}{\lambda},
\qquad
L=\frac{aR+1}{\eta},
\qquad
K=\frac{pR+1}{4}=\gamma L. \tag{1}
\]

令 (\mathcal T) 是该完整源谱中所有 (a,s) 的坐标标签集合，并定义

\[
J_t=\operatorname{lcm}_{u\in\mathcal T,\ u\ne t}|t-u|. \tag{2}
\]

由[坐标标签碰撞分解](type-I-linear-block-label-collision.md)，不同标签的共同素因子幂只能来自
相应的标签差。这里对 (1) 的两块作精确切分：

\[
G_c=(\gamma,J_s),\quad G_p=\gamma/G_c,
\qquad
L_c=(L,J_a),\quad L_p=L/L_c. \tag{3}
\]

所以

\[
\boxed{K=G_cG_pL_cL_p.} \tag{4}
\]

四项依次称为源碰撞、源私有、仿射碰撞、仿射私有层。它们不必两两互素；(3) 保留每个
素数的真实指数分配，而不是仅记录“这个素数是否出现过”。

对任意正整数 (N) 写

\[
\mathcal C_R(N)=
\left\{\prod_{q\mid N}q^{z_q}\bmod R:
-\nu_q(N)\le z_q\le\nu_q(N)\right\}. \tag{5}
\]

若 (I\) 是四层的非空子集，令 (N_I) 为这些层的乘积。因为 (N_I\mid K)，有

\[
-1\in\mathcal C_R(N_I)
\Longrightarrow -1\in\mathcal C_R(K). \tag{6}
\]

确实，若 (d\mid N_I^2) 且 (d/N_I\equiv-1\pmod R)，则

\[
d\frac K{N_I}\mid K^2,
\qquad
\frac{d(K/N_I)}K\equiv-1\pmod R. \tag{7}
\]

因此它给出一个有效的一般 (B) 目标平方除子。定义该有向状态的标签层支撑为

\[
\ell(p,R,a,s)=
\min\left\{|I|:-1\in\mathcal C_R(N_I)\right\}. \tag{8}
\]

这是一个依赖于完整坐标标签谱的精确有限量，不是从字符值或因子个数作出的启发式分类。

## 冻结完整谱审计

输入合并两组已经完整枚举线性源的压力谱：

- 四个全局线性 (B=1) 失败点的全部线性 (R) 谱；
- 七个六亿内压力点的全部线性 (R) 谱。

二者互不相交，共有 11 个素数。对每个素数，程序重新枚举全部线性源以构造 (2)，然后对每个
冻结为 `hit` 的 (R) 及其每个有向 ((a,s))，逐一枚举 15 个非空子集的 (5)。这不是对
“某个选中的因子”做事后归类：每个子集都重新分解其乘积，并完整枚举其中心化指数盒。

| 最小层支撑 (\ell) | 有向目标命中数 |
| ---: | ---: |
| 1 | 14 |
| 2 | 28 |
| 3 | 8 |
| 4 | 0 |
| **合计** | **50** |

这些 50 个有向状态位于 32 个不同的实际命中模数中。逐素数的分布如下；空列表示零。

| (p) | 命中 (R) 数 | 有向命中源数 | (\ell=1) | (\ell=2) | (\ell=3) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 214,729 | 3 | 4 | 0 | 4 | 0 |
| 878,089 | 1 | 1 | 0 | 1 | 0 |
| 2,210,569 | 3 | 4 | 2 | 2 | 0 |
| 3,942,409 | 4 | 4 | 0 | 4 | 0 |
| 13,782,409 | 1 | 1 | 0 | 0 | 1 |
| 62,588,089 | 2 | 5 | 0 | 3 | 2 |
| 64,214,329 | 4 | 5 | 3 | 2 | 0 |
| 105,295,129 | 4 | 6 | 2 | 3 | 1 |
| 297,640,249 | 4 | 7 | 0 | 3 | 4 |
| 477,015,289 | 2 | 4 | 2 | 2 | 0 |
| 536,944,489 | 4 | 9 | 5 | 4 | 0 |

三层反例集中在以下五个命中模数；表中每一个定向状态均已直接排除全部四个单层和全部六个
双层子积。

| (p) | (R) | 有向 ((a,s)) |
| ---: | ---: | --- |
| 13,782,409 | 131 | ((11680,9)) |
| 62,588,089 | 495 | ((227,557),(557,227)) |
| 105,295,129 | 119 | ((10,88409)) |
| 297,640,249 | 55 | ((1761,3073),(3073,1761)) |
| 297,640,249 | 231 | ((11,117089),(117089,11)) |

## 含义与边界

这给出一个明确的反例优先边界：在这种完整标签分解下，不能把每张实际 Type I 命中规范为
“至多两个完整标签层的乘积”。八张三层状态已经逐个排除了该收缩。它与[源块和仿射块的
混合剖面](type-I-linear-general-b-two-block-hit-profile-500m.md)一致，并更细地说明两块内部的
碰撞/私有指数层也不能任意丢弃。

其中 (p=13{,}782{,}409) 排除了“改选另一张线性源即可回到两层”的退路。其完整谱有
41 个不同 (R)、78 个有向线性源，精确分类为一张命中、九张有限指数障碍和31张子群角色
障碍；唯一命中就是

\[
(R,a,s)=(131,11680,9),\qquad
K=451373895=5\cdot59\cdot63\cdot24287. \tag{9}
\]

相对于该完整谱的标签，四层依次为

\[
(G_c,G_p,L_c,L_p)=(5,59,63,24287). \tag{10}
\]

这里 (\ell=3)，唯一最小层集合是

\[
\{G_c,L_c,L_p\}. \tag{11}
\]

故在这个素数的**全部**线性源中，不存在一张目标命中能由至多两层给出。特别地，有限
重选断言“每个有线性命中的压力素数可重选至两层命中”已被这个完整单点反驳。

反过来，当前有限资料中没有状态需要全部四层。这只是待解释的经验边界，**不是**
\(\ell\le3\) 的全称命题，更不能推出存在某个命中 (R)。本页不比较不同 (R) 的角色证书，
也不处理非命中状态的有限指数障碍；因此它不能证明[线性一般 (B) 终端选择猜想](type-I-linear-source-general-b-terminal-selector-conjecture.md)。

下一条有效理论必须同时允许三层指数积集，或证明总能重选到一张两层命中源。直接把该有限
剖面升级为“任意命中不超过两层”的路线已被这八个状态否定。

## 可复现检查

~~~bash
python3 reproductions/type_i_linear_label_layer_support_profile.py
python3 -m unittest tests.test_type_i_linear_label_layer_support_profile -v
~~~
