---
kind: claim
claim_id: type-I-linear-single-active-prime-cross-state-compatibility
title: 线性 F 型单一活跃素因子的跨模数兼容性
statement: 设同一核心素数 p 的两个不同线性源状态均落入 F 型低复杂度分支，且各自的稳定子群商为偶循环群、只有一个奇素数 q_i 在商群中非平凡并生成商群。若两个状态的活跃素数相同为 q，则 q 的最低共同指数整除 |R-R'|/4；并且 q 同时整除两个状态各自某个坐标块对应的 p-t，故 q 整除两个被选坐标标签之差。这是跨状态排除重复单一活跃方向的必要条件，不是全称选择器。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
- type-I
- linear-source
- f-obstruction
- cyclic-quotient
- active-prime
- cross-modulus
- label-collision
- descent
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-linear-normal-form-context
visibility: public
last_checked: '2026-07-29'
---

# 线性 F 型单一活跃素因子的跨模数兼容性

## 设置

固定奇素数 \(p\)，取两个不同的线性源状态

$$
p=a_i+s_i+a_is_iR_i,\qquad R_i\equiv3\pmod4,\qquad
K_i=\frac{pR_i+1}{4},\qquad i=1,2. \tag{1}
$$

在两个状态中均设

$$
-1\in\mathcal H_{R_i}(K_i)\setminus\mathcal C_{R_i}(K_i),
$$

并令 \(T_i=\operatorname{Stab}_{\mathcal H_{R_i}(K_i)}
(\mathcal A_{R_i}(K_i))\)。进一步假设

$$
\mathcal H_{R_i}(K_i)/T_i\cong C_{2m_i}, \tag{2}
$$

且只有一个奇素数 \(q_i\mid K_i\) 在该商群中非平凡，\(q_iT_i\) 生成商群。记

$$
e_i=v_{q_i}(K_i)<m_i. \tag{3}
$$

条件 (3) 正是单一活跃素因子循环商中的 F 型未命中条件。

## 跨状态兼容性定理

若两个状态的活跃素数相同，即 \(q_1=q_2=q\)，则：

1. 共同指数受模数差控制：

   $$
   q^{\min(e_1,e_2)}
   \mid \frac{\lvert R_1-R_2\rvert}{4}. \tag{4}
   $$

2. 对每个 \(i\)，存在 \(t_i\in\{a_i,s_i\}\)，使得

   $$
   q\mid p-t_i. \tag{5}
   $$

   因而

   $$
   q\mid t_1-t_2. \tag{6}
   $$

特别地，如果两个状态的候选标签差不被 \(q\) 整除，或者
\(v_q(\lvert R_1-R_2\rvert/4)<\min(e_1,e_2)\)，则它们不可能由同一个
单一活跃素因子产生 F 型障碍。

## 证明

由 \(4K_i=pR_i+1\) 得

$$
K_1-K_2=\frac{p(R_1-R_2)}4. \tag{7}
$$

同时 \(\gcd(p,K_i)=1\)：若素数 \(q\) 同时整除 \(p\) 与 \(K_i\)，则
\(q\mid pR_i+1\)，从而 \(q\mid1\)，矛盾。于是对共同的奇素数 \(q\)，
(7) 给出 \(q\mid(R_1-R_2)/4\)。

更精确地，已有的跨模数公因子恒等式给出

$$
\gcd(K_1,K_2)
=\gcd\!\left(K_1,\frac{\lvert R_1-R_2\rvert}{4}\right). \tag{8}
$$

因为 \(e_i=v_q(K_i)\)，取 \(q\)-进赋值得到 (4)。

另一方面，\(q\) 为奇素数且 \(q\mid K_i\)。由

$$
4K_i=(s_iR_i+1)(a_iR_i+1), \tag{9}
$$

可知 \(q\) 至少整除其中一个块。若 \(q\mid s_iR_i+1\)，取
\(t_i=s_i\)；若 \(q\mid a_iR_i+1\)，取 \(t_i=a_i\)。在前一种情形
\(s_iR_i+1\mid p-s_i\)，后一种情形 \(a_iR_i+1\mid p-a_i\)，所以均有
\(q\mid p-t_i\)。对两个状态相减即得 (6)。证毕。

## 对证明路线的作用

这张卡把“同一个低复杂度 F 障碍可以在多个 \(R\) 状态重复出现”的可能性压缩为一个
明确的整除图：

- 一个活跃素数 \(q\) 只能连接满足 \(q\mid(R-R')/4\) 的状态；
- 若两端使用不同坐标标签，还必须满足 \(q\mid(t-t')\)；
- 活跃指数的较小者不能超过模数差中的 \(q\)-进预算。

因此，跨完整源谱的下一步不是重新枚举中心化指数盒，而是证明这些
“模数差预算 + 标签差预算”无法覆盖所有候选 F 状态；若仍能覆盖，则剩余对象已被压缩到
有限的活跃素因子与有限指数缺口，可与标签层分解和多块 Kneser 判据联合处理。

该结论只给出必要条件：它不排除不同状态使用不同活跃素因子的 F 障碍，也不处理商群中有
多个非平凡素因子的情形。因此它推进了原三层重选猜想的跨状态部分，但尚未证明该猜想。
