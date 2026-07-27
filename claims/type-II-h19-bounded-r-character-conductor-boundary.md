---
kind: claim
claim_id: type-II-h19-bounded-r-character-conductor-boundary
title: H19 固定 r 残余的共同局部角色导子边界
statement: 在 r<=9999 未命中的15个 H19 残余中，对每个固定素数 p，其所有子群--字符型失败状态的 r 模数最大公因数均为1。因此不存在一个非平凡模数能同时整除该 p 的全部局部状态模数；固定局部导子的二次角色不能单独统一解释这些失败。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- characters
- congruences
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# H19 固定 \(r\) 残余的共同局部角色导子边界

在 \(r\le9999\) 的 15 个平方尾残余上，固定一个 \(p\)，收集所有子群--字符型失败所
对应的状态模数

\[
\mathcal R_p=\{r:\ -M_1\notin\langle\operatorname{supp}(M_1)\rangle
\pmod r\}.
\]

精确计算得到每个 \(p\) 都有

\[
\gcd_{r\in\mathcal R_p} r=1. \tag{1}
\]

若一种局部二次角色论证要求固定的非平凡导子 \(q\) 同时整除所有这些状态模数，式 (1)
立即排除它。因而不能把每个状态的二次分离角色误读成同一个固定模数上的全局筛。

这个边界并不排除依赖于 \(r\) 的角色、不同模数之间的 CRT 关系，或完全不同的平方尾
机制；它只明确排除最直接的“固定局部导子”统一证明模型。

## 重建

~~~bash
python3 reproductions/type_ii_h19_bounded_r_tail_obstruction_profile.py
python3 reproductions/type_ii_h19_bounded_r_character_conductor_boundary.py
python3 -m unittest tests/test_type_ii_h19_bounded_r_character_conductor_boundary.py -q
~~~
