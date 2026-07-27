---
kind: claim
claim_id: type-II-h19-bounded-r-tail-obstruction-profile
title: H19 固定 r 残余的平方尾障碍剖面
statement: 在 p<=10^9 的 H19 残余中，r<=9999 仍未命中的15个素数并非缺少兼容偶源：它们共有156个 r=7 mod8 兼容状态且平方尾均失败。其中116个目标在 M1 素因子生成子群外，均有显式二次字符分离；另40个目标在子群内而被有限平方指数积集阻断。
claim_status: computationally_reproduced
topics:
- type-I
- descent
- even-source
- divisor-residues
- characters
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-certificate-reconstruction
visibility: public
last_checked: '2026-07-25'
---

# H19 固定 \(r\) 残余的平方尾障碍剖面

固定 \(r\le9999\) 后仍未被偶源平方尾捕获的 15 个 H19 残余，并没有源端因子对缺失。
逐一枚举所有

\[
r\equiv7\pmod8,\qquad
(cr+1)(dr+1)=rp+1
\]

的状态，一共得到 156 个兼容状态，且每个状态的

\[
e_1\mid M_1^2,\qquad e_1\le M_1,\qquad e_1\equiv-M_1\pmod r
\]

均无解。按目标是否属于 \(M_1\) 素因子残数生成的单位子群，精确分类为：

| 类型 | 状态数 | 含义 |
|---|---:|---|
| 子群--字符型 | 116 | 目标残数不在生成子群中 |
| 有限积集型 | 40 | 目标在群中，但 \(M_1^2\) 的指数盒未抵达 |

116 个子群--字符型状态全部有显式二次角色：它在每个 \(M_1\) 素因子上取 \(+1\)，
却在负目标上取 \(-1\)。因此在此有限残余中，不需要高阶角色来解释子群外失败。

这个结论把固定 \(r\) 后的下一步明确分流：字符型状态需要证明其跨 \(r\) 的长期相容性
不可能，有限积集型状态则需要新的重数、因子或不同尾部机制。它不说明任一点在
\(r>9999\) 仍然失败，也不否定可变 \(r\) 的选择器。

## 重建

~~~bash
python3 reproductions/type_ii_h19_bounded_r_selector_boundary.py
python3 reproductions/type_ii_h19_bounded_r_tail_obstruction_profile.py
python3 -m unittest tests/test_type_ii_h19_bounded_r_tail_obstruction_profile.py -q
~~~
