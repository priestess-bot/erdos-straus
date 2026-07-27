---
kind: claim
claim_id: type-II-h19-fourth-even-source-subgroup-profile
title: H19 十亿第四压力点平方尾的子群--积集分流
statement: 对 p=640775689、c<=34091 的33条兼容偶源射线，平方尾失败的32条中有23条的目标 -M1 mod r 不在 M1 素因子残数生成的单位群子群内，属字符型障碍；其余9条目标在该子群内但不在实际平方除子积集内，属有限指数积集障碍。唯一 c=34091 命中射线的目标在子群与实际积集内。故第四压力点的剩余理论任务必须分流处理这两类机制。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- even-source
- subgroup
- characters
- divisor-residues
- product-sets
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# H19 十亿第四压力点平方尾的子群--积集分流

对每条兼容偶源射线，平方尾条件是

\[
e_1\in\Pi_r(M_1^2),\qquad e_1\equiv-M_1\pmod r. \tag{1}
\]

令 \(H\le U(r)\) 为 \(M_1\) 的全部素因子模 \(r\) 残数生成的子群。因为
\(\Pi_r(M_1^2)\subseteq H\)，每个未命中射线恰落入两种机制之一：

1. \(-M_1\notin H\)：存在一个在所有 \(M_1\) 素因子上平凡、但在目标上非平凡的单位群
   字符，称为**子群--字符型**；
2. \(-M_1\in H\setminus\Pi_r(M_1^2)\)：字符无法区分，失败仅来自平方除子指数的
   有界积集，称为**有限积集型**。

用素数幂 CRT 的离散对数坐标和 Hermite 正规形精确判定成员资格。对第四压力点的 33 条
兼容射线，结果为：

| 状态 | 数量 |
|---|---:|
| 子群--字符型失败 | 23 |
| 有限积集型失败 | 9 |
| 实际平方尾命中 | 1 |

唯一命中仍是

\[
c=34091,\qquad r=15,\qquad -M_1\equiv11\pmod {15}.
\]

此时生成子群就是整个 \(U(15)\)，阶为 8，且有 12 个实际平方尾因子命中目标残数。

因此下一步不能只寻求一个统一的“尾部因子足够多”引理：对子群--字符型射线，要研究
不同 \(r\) 的角色约束是否能与同一 \(p\) 长期兼容；对有限积集型射线，则需要控制
\(M_1\) 素因子指数、重复与跨射线乘积集何时覆盖目标。

在该压力点，23 条字符型障碍都已有二次角色分离，不需高阶单位群角色，见
[第四压力点平方尾障碍的二次角色化](type-II-h19-fourth-even-source-quadratic-character-profile.md)。

九条有限积集型状态的首达幂并不统一：三条在 \(M_1^{12}\) 内仍未命中，故不能把这一
分支简化为“再增加一次重复”规则，见
[第四压力点有限积集型平方尾的指数缺口](type-II-h19-fourth-even-source-exponent-profile.md)。

## 重建

~~~bash
python3 reproductions/type_ii_h19_fourth_even_source_subgroup_profile.py
python3 -m unittest tests/test_type_ii_h19_fourth_even_source_subgroup_profile.py -q
~~~
