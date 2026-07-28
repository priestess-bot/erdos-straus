---
kind: claim
claim_id: type-I-linear-high-order-pair-phase-compatibility-159108889
title: 159,108,889 的双四阶 G 型碰撞仍保持完整相位相容
statement: 在p=159108889的完整线性谱中，两个最小分离二幂角色阶均为4的G型状态R=47227和R'=53036295共享可分裂奇素数q=70841。前者的两个四阶分离子为局部系数(2,1)、(2,3)，后者为(2,0,1,1)、(2,0,3,3)。以q的规范高斯因子rho=245+104i逐项计算，R端有(q/83)_2(q/pi_569)_4=(-1)(-1)=1；R'端有(q/3)_2(q/pi_13)_4(q/pi_271981)_4=(-1)(-1)(1)=1。三个四次分量均满足各自的源标签拉回。故即使两个高阶G型状态在同一个可分裂K素因子上相交，完整四次相位也可相容；这种碰撞不自动迫使Type I目标命中。此为有限边界，不反驳或证明混合终端选择器。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- subgroup-character
- order-four-character
- gaussian-integers
- quartic-reciprocity
- shared-factors
- counterexample-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 159,108,889 的双四阶 G 型碰撞仍保持完整相位相容

## 两个高阶状态

[高阶角色普查](type-I-linear-b-gt-one-high-order-separator-census-600m.md)在同一个核心素数

\[
p=159{,}108{,}889
\]

中找到两条最小分离二幂角色阶均为 \(4\) 的 G 型状态：

\[
\begin{array}{c|c|c}
R&K&\text{共享奇素数}\\ \hline
47{,}227=83\cdot569&70{,}841\cdot26{,}517{,}961&70{,}841\\
53{,}036{,}295=3\cdot5\cdot13\cdot271{,}981&
2^2\cdot19\cdot1{,}123\cdot70{,}841\cdot348{,}923&70{,}841
\end{array}
\]

这里 \(q=70{,}841\equiv1\pmod4\) 是可分裂的，取其规范高斯因子

\[
\rho=245+104i,
\qquad N(\rho)=70{,}841.
\]

两条状态中 \(q\) 都来自标签块 \(tR+1\) 的同一端点 \(t=3\)。

## 四阶角色与相位

按各局部原根的离散对数坐标，左状态恰有两个四阶分离子

\[
(2,1),\quad(2,3)
\]

（局部素数顺序为 \(83,569\)）；右状态恰有

\[
(2,0,1,1),\quad(2,0,3,3)
\]

（顺序为 \(3,5,13,271{,}981\)）。每一个在 \(-1\) 上取 \(-1\)，并在对应 \(K\) 的全部
素因子上取 \(1\)。

令 \(\pi_r\) 为规范高斯因子，且 \(R=C r\)。对这三个实际出现的可分裂局部素数，直接计算
高斯四次符号，得到源标签相位等式

\[
\left(\frac q{\pi_r}\right)_4
=
\left(\frac{\pi_r}{\rho}\right)_4^2
\left(\frac{-Ct}{\rho}\right)_4.
\]

数值如下：

| 状态 | \(r\) | \(C\) | \((q/\pi_r)_4\) | \((\pi_r/\rho)_4\) | \((-Ct/\rho)_4\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| \(R=47{,}227\) | 569 | 83 | \(-1\) | \(1\) | \(-1\) |
| \(R'=53{,}036{,}295\) | 13 | 4,079,715 | \(-1\) | \(i\) | \(1\) |
| \(R'=53{,}036{,}295\) | 271,981 | 195 | \(1\) | \(1\) | \(1\) |

因此共享素数的完整角色条件同时成立：

\[
\left(\frac q{83}\right)_2
\left(\frac q{\pi_{569}}\right)_4
=(-1)(-1)=1,
\]

\[
\left(\frac q3\right)_2
\left(\frac q{\pi_{13}}\right)_4
\left(\frac q{\pi_{271981}}\right)_4
=(-1)(-1)(1)=1.
\]

## 边界

这给出了比二次影子更强的负面结果：即使保留四次相位、源标签和共享素因子的高斯分解，两个不同
高阶 G 型状态仍可完全相容。故下述尝试不能成为全称选择器证明：

\[
\text{“两个高阶 G 型状态共享一个可分裂的 }K\text{ 素因子”}
\Longrightarrow
\text{“其中一个状态必逃逸”。}
\]

后续若要把高次互反变成正向机制，还须引入不止一个共享相位，或把相位条件与 F 型反足点积集增长
联系起来。本页不构造 Type I 证书，也不提供混合终端选择引理的证明或反例。

## 复现

~~~bash
python3 reproductions/type_i_linear_high_order_pair_phase_compatibility_159108889.py
python3 -m unittest tests.test_type_i_linear_high_order_pair_phase_compatibility_159108889 -v
~~~
