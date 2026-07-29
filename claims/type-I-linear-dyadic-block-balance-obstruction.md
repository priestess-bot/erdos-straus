---
kind: claim
claim_id: type-I-linear-dyadic-block-balance-obstruction
title: 线性 F 型一奇素因子障碍的二进块平衡约束
statement: 设线性源 p=a+s+asR、s 为奇数、R=3 mod4，K=(pR+1)/4，且状态为 F 型。令 T=Stab_H(A)、Q=H/T。若 Q 为 C_{2m}，除一个奇素数 q 外的所有奇素因子在 T 中，qT 生成 Q，并且 2∈H、2T=T，则该状态不可能存在。更一般地，若 2T=(qT)^alpha，两个块 U=sR+1、V=aR+1 的 q 进指数与二进指数满足 r+alpha u=0、(e-r)+alpha v=0 mod 2m；F 型条件等价于相应二维指数矩形的差集避开 m。因此任何剩余的一奇素因子 F 障碍必须保留非平凡二进方向。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- f-obstruction
- dyadic
- cyclic-quotient
- block-balance
- finite-exponent
- subgroup-structure
- mixed-selector
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 线性 F 型一奇素因子障碍的二进块平衡约束

## 设置

固定线性源状态

$$
p=a+s+asR,\qquad s\equiv1\pmod2,\qquad R\equiv3\pmod4,
$$

并令

$$
K=\frac{pR+1}{4},\qquad
U=sR+1,\qquad V=aR+1. \tag{1}
$$

于是

$$
UV=4K,\qquad U\equiv V\equiv1\pmod R. \tag{2}
$$

记 \(\mathcal A=\mathcal A_R(K)\)、\(\mathcal H=\mathcal H_R(K)\)、
\(T=\operatorname{Stab}_{\mathcal H}(\mathcal A)\)，并假设

$$
-1\in\mathcal H\setminus\mathcal C_R(K),
\qquad
\mathcal H/T\cong C_{2m}. \tag{3}
$$

设除一个奇素数 \(q\mid K\) 外的所有奇素数在 \(T\) 中，且 \(qT\) 生成
\(\mathcal H/T\)。暂时再假设 \(2\in\mathcal H\)，并写

$$
2T=(qT)^\alpha,\qquad
e=v_q(K),\qquad
\kappa=v_2(K). \tag{4}
$$

若 \(2\not\mid K\)，约定 \(\kappa=0\)；此时 \(2\) 只作为块同余中的单位群元素出现，
而不是 \(\mathcal A\) 的一个独立除子坐标。

## 二进块平衡方程

记

$$
u=v_2(U),\quad v=v_2(V),\quad
r=v_q(U),\quad e-r=v_q(V). \tag{5}
$$

则

$$
r+\alpha u\equiv0\pmod{2m},
\qquad
(e-r)+\alpha v\equiv0\pmod{2m}, \tag{6}
$$

且

$$
u+v=\kappa+2. \tag{7}
$$

证明中不需要 \(q\) 只出现在一个块；\(r\) 可以在
\(0\le r\le e\) 的整个范围内变化。

## 单一奇素因子、二进平凡时的排除

若进一步有

$$
2T=T\quad(\text{即 }\alpha\equiv0\pmod{2m}), \tag{8}
$$

则 (6) 给出 \(2m\mid r\) 以及 \(2m\mid(e-r)\)。另一方面，F 型条件和
\(qT\) 的阶 \(2m\) 给出

$$
e<m. \tag{9}
$$

所以 \(0\le r,e-r<m<2m\) 时只能有 \(r=e-r=0\)，与
\(e=v_q(K)\ge1\) 矛盾。故得到：

$$
\boxed{
\text{线性 F 型状态若只有一个非平凡奇素因子方向，}
\ 2T=T\text{ 时不可能存在。}
} \tag{10}
$$

换言之，任何真正的“一奇素因子”低复杂度 F 障碍都必须满足以下二者之一：

- \(2\notin\mathcal H\)，二进单位根根本不在该商的定义域中；
- \(2\in\mathcal H\) 且 \(2T\ne T\)，二进方向本身是商群中的第二个活跃方向。

## 商群中的精确剩余模型

在 \(2\in\mathcal H\) 的情形，令 \(g=qT\)，则

$$
\overline{\mathcal A}
=\left\{g^{\,i+\alpha j}:0\le i\le e,\ 0\le j\le\kappa\right\}
\subseteq C_{2m}. \tag{11}
$$

因此 F 型未命中恰好等价于

$$
m\notin
\left\{i+\alpha j-i'-\alpha j':
0\le i,i'\le e,\ 0\le j,j'\le\kappa\right\}
\pmod{2m}. \tag{12}
$$

式 (6) 说明两个同余于 \(1\pmod R\) 的块，必须分别把各自的二进幂
\(2^u,2^v\) 与奇素因子方向平衡掉；式 (12) 则把剩余 F 障碍压缩成一个二维
指数矩形，而不是此前的单方向区间。

## 证明

把两个块写成

$$
U=2^uU_{\mathrm o},\qquad V=2^vV_{\mathrm o},
$$

其中 \(U_{\mathrm o},V_{\mathrm o}\) 为奇数。由 \(UV=4K\)，它们都是 \(K\) 的除子。
除 \(q\) 外的奇素数在 \(T\) 中，所以在商群 \(Q=\mathcal H/T\) 中

$$
\overline{U_{\mathrm o}}=g^r,\qquad
\overline{V_{\mathrm o}}=g^{e-r}. \tag{13}
$$

另一方面 \(U\equiv V\equiv1\pmod R\)，且 \(2T=g^\alpha\)。把 (13) 分别乘上
\(2^u\)、\(2^v\) 的商群残数即得 (6)。二进赋值相加给出 (7)。

由于 \(g\) 阶为 \(2m\)，若 \(e\ge m\)，则
\(\overline{\mathcal A}\) 同时含 \(T\) 与 \(g^mT=-T\)，与
\(\mathcal A\cap(-\mathcal A)=\varnothing\) 矛盾，故有 (9)。
在 \(\alpha=0\) 时，(6) 与 \(e<m\) 迫使 \(r=e-r=0\)，矛盾。

最后，每个 \(K\) 的除子在 \(Q\) 中只贡献 \(g^i\) 和（若 \(\kappa>0\)）
\(2^jT=g^{\alpha j}\)，得到 (11)。反足点 \(-T=g^mT\) 属于
\(\overline{\mathcal A}\overline{\mathcal A}^{-1}\) 当且仅当 (12) 失败，证毕。

## 对原选择器的推进

这条结论消除了一个容易误判的低复杂度分支：不能把 F 型状态压缩成
“一个奇素因子、其余全部稳定”的单向指数区间，然后期待跨 \(R\) 只追踪这个素因子。
在线性源的两块结构中，块同余会强制该方向与二进因子平衡；二进平凡时直接矛盾，
二进非平凡时则必须处理 (11)--(12) 的二维矩形。

因此下一阶段可按以下严格分叉推进：

1. 先证明某个源状态的 \(2\) 不在 \(\mathcal H_R(K)\)，从而把状态送入 G 型或直接改变
   角色分类；
2. 若 \(2\in\mathcal H_R(K)\)，则排除 \(\alpha=0\) 后，研究二维矩形的差集缺口；
3. 将二维缺口与跨状态模数差预算、标签碰撞层和多块 Kneser 判据联合，尝试得到目标
   命中或严格源状态递降。

本卡不声称所有二维 F 障碍都能被排除，也不证明原混合终端选择引理；它给出的是一个
严格的局部结构定理和下一步必须处理的最小剩余模型。
