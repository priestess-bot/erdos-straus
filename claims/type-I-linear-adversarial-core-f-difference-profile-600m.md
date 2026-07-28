---
kind: claim
claim_id: type-I-linear-adversarial-core-f-difference-profile-600m
title: 四个真实对抗核心的 F 型除子差集近饱和仍不命中
statement: 对四个一般B命中唯一且全谱无B=1的真实对抗核心，共有45个有限指数F型状态。逐项构造单边除子谱A_R(K)及差集D_R=A_R(K)A_R(K)^(-1)，45个状态均不含目标-1。差集覆盖率最高的是(p,R)=(26034649,375)，D_R在生成子群的200个元素中覆盖192个，达到96%，但目标-1=374仍是8个缺失类之一。因此即使差集达到96%覆盖，单状态积集密度仍不足以推出一般B命中；下一步必须使用缺失类结构、标签碰撞或跨源重选，而不能只提高密度下界。此为有限完整审计，不推出全称选择器或反例。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- linear-source
- general-b
- finite-exponent
- divisor-lattice
- finite-product
- difference-set
- adversarial-core
- obstruction
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 四个真实对抗核心的 F 型除子差集近饱和仍不命中

## 审计对象

输入是[两百个完整线性谱中的高阶 G 型分离角色普查](type-I-linear-b-gt-one-full-spectrum-profile-600m.md)
所使用的 200 点完整线性谱，选取四个一般 \(B\) 命中唯一且全谱无 \(B=1\) 的核心

\[
p\in\{878{,}089,26{,}034{,}649,57{,}399{,}241,283{,}319{,}689\}.
\]

对每个 F 型状态定义

\[
\mathcal A_R(K)=\{d\bmod R:d\mid K\},
\qquad
\mathcal D_R(K)=\mathcal A_R(K)\mathcal A_R(K)^{-1}.
\]

由反足点刻画，\(-1\in\mathcal D_R(K)\) 等价于一般 \(B\) 目标命中。程序同时从单位群格证书
恢复 \(\mathcal H_R(K)\) 的精确阶，并计算差集覆盖缺额

\[
\delta_R=|\mathcal H_R(K)|-|\mathcal D_R(K)|.
\]

## 结果

四个核心共有 45 个 F 型状态，逐项结果均为

\[
-1\notin\mathcal D_R(K),
\qquad
\mathcal D_R(K)\subsetneq\mathcal H_R(K).
\]

差集最接近饱和的状态为

\[
p=26{,}034{,}649,
\qquad R=375,
\qquad K=2{,}440{,}748{,}344.
\]

这里 \(|\mathcal H_R(K)|=200=\varphi(375)\)，而

\[
|\mathcal A_R(K)|=70,
\qquad
|\mathcal D_R(K)|=192,
\qquad
\delta_R=8.
\]

八个缺失的单位剩余类为

\[
127,133,172,251,254,313,344,374.
\]

目标 \(-1\equiv374\pmod{375}\) 正好位于缺失集合中。换言之，差集已经覆盖生成群的
\(192/200=96\%\)，但仍没有目标。

四点的最大差集覆盖率分别为：

| \(p\) | F 状态数 | 最大 \(|\mathcal D|/|\mathcal H|\) | 最小差集缺额 |
| ---: | ---: | ---: | ---: |
| 878,089 | 2 | \(205/502\) | 127 |
| 26,034,649 | 6 | \(192/200\) | 8 |
| 57,399,241 | 24 | \(246/288\) | 19 |
| 283,319,689 | 13 | \(1004/1944\) | 67 |

## 含义与边界

这个结果把 F 型正向路线的要求收紧了一步。半密度判据只要求
\(|\mathcal A|>|\mathcal H|/2\) 才能强制命中；而差集覆盖是更直接的目标侧量。即使差集覆盖
达到 96%，它仍可把 \(-1\) 留在唯一的少数缺失类中。因此下列形式不足以作为全称证明：

\[
\text{“所有 F 型状态的差集覆盖率达到某个低于96\%的统一阈值”}
\Longrightarrow
\text{“存在一般 B 命中”。}
\]

下一步应研究缺失类的结构，而非只继续增大 \(|\mathcal D|\)：

* 缺失类是否由标签块碰撞指数决定；
* 两个线性块的积集是否能在商群中定向填入目标缺口；
* 同一核心其他 \(R\) 的共享素因子是否能提供缺失类的跨源拉回。

本页只给出四个有限完整谱的边界，不证明混合终端选择引理，也不构成反例。

## 复现

~~~bash
python3 reproductions/type_i_linear_adversarial_core_f_difference_profile_600m.py
python3 -m unittest tests/test_type_i_linear_adversarial_core_f_difference_profile_600m.py -v
~~~
