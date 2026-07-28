---
kind: claim
claim_id: type-I-linear-finite-exponent-antipodal-density-profile-600m
title: 七点线性 F 型状态的反足点半密度边界
statement: 对七个完整线性压力谱的68个有限指数F型状态，逐项直接计算单边除子剩余集A_R(K)和素因子生成子群H_R(K)的精确阶，均有2|A_R(K)|不超过|H_R(K)|。其中p=64214329的R=39与R=55恰取等号但仍无目标命中，说明半密度充分判据尖锐；另一状态(p,R)=(64214329,10702387)只有2|A|/|H|=120/10702386，说明F型不普遍接近半密度。因此单状态的半密度计数不能单独证明一般B选择器，必须结合更细商群增长或跨源重选。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- finite-exponent
- centered-spectrum
- divisor-lattice
- finite-product
- obstruction
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-28'
---

# 七点线性 F 型状态的反足点半密度边界

## 审计对象

输入为[七点全线性目标谱的角色与有限指数混合剖面](type-I-linear-general-b-obstruction-mixture-profile-600m.md)
冻结的全部 68 个有限指数状态，即

\[
-1\in\mathcal H_R(K)\setminus\mathcal C_R(K),
\qquad K=\frac{pR+1}{4}. \tag{1}
\]

对每个状态直接构造

\[
\mathcal A_R(K)=\{d\bmod R:d\mid K\}, \tag{2}
\]

并从既有的单位群离散对数格证书恢复 \(|\mathcal H_R(K)|\)。若分量循环群阶为
\(n_1,\ldots,n_r\)，而生成元对数与 \(n_i\mathbf e_i\) 生成的整格的 HNF 行列式为 \(I\)，则

\[
|\mathcal H_R(K)|=\frac{\prod_i n_i}{I}. \tag{3}
\]

这是因为 \(I=[(\mathbb Z/R\mathbb Z)^\times:\mathcal H_R(K)]\)。测试独立重建 (2)、格指数和
目标的子群成员性。

## 结果

所有 68 个 F 型状态均满足反足点定理所要求的严格必要不等式

\[
2|\mathcal A_R(K)|\le |\mathcal H_R(K)|. \tag{4}
\]

其中两个状态已经达到边界而仍不命中：

| (p) | (R) | (K) | (|mathcal A_R(K)|) | (|mathcal H_R(K)|) |
| ---: | ---: | ---: | ---: | ---: |
| 64,214,329 | 39 | 626,089,708 | 12 | 24 |
| 64,214,329 | 55 | 882,947,024 | 20 | 40 |

故在这两点中

\[
\mathcal A_R(K)\sqcup-\mathcal A_R(K)=\mathcal H_R(K), \tag{5}
\]

半密度充分判据的严格不等号不能弱化为非严格不等号。

更强的负面例子是

\[
\begin{aligned}
p&=64{,}214{,}329,\qquad R=10{,}702{,}387,\\
(a,s)&=(6,1),\\
K&=171{,}811{,}649{,}975{,}831
=29\cdot41\cdot53\cdot881\cdot1019\cdot3037.
\end{aligned} \tag{6}
\]

这里

\[
2|\mathcal A_R(K)|=120,
\qquad |\mathcal H_R(K)|=10{,}702{,}386=R-1, \tag{7}
\]

即半密度缺额为 \(10{,}702{,}266\)。在本审计中最大缺额为
\(12{,}958{,}626\)，出现在
\((p,R)=(105{,}295{,}129,35{,}098{,}375)\)。

## 含义与边界

[反足点除子刻画](type-I-general-b-antipodal-divisor-spectrum.md)给出的半密度阈值仍是严格的
充分命中机制；本页没有反驳它。相反，两个等号状态证明它在固定状态上已是尖锐的。

但 (6)--(7) 表明，不能期望通过“每个 F 型状态的 \(\mathcal A_R(K)\) 都接近半个生成子群”来
推出全称选择器。下一步必须利用单一状态计数之外的信息：例如碰撞/私有层在商群中的逐层增长，
或同一核心素数不同 \(R\) 状态之间的重选。任何声称仅凭统一半密度余量闭合一般 \(B\) 的路线，
都已被这张完整谱的 F 型记录排除。

## 复现

~~~bash
python3 reproductions/type_i_linear_finite_exponent_antipodal_density_profile_600m.py
python3 -m unittest tests.test_type_i_linear_finite_exponent_antipodal_density_profile_600m -v
~~~
