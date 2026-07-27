---
kind: claim
claim_id: type-II-h19-fourth-even-source-exponent-profile
title: H19 十亿第四压力点有限积集型平方尾的指数缺口
statement: 对 p=640775689 的9条偶源平方尾有限积集型失败，目标在 M1^3、M1^5、M1^7 首次进入平方尾除子残数集的状态数分别为1、1、4；另3条直到 M1^12 仍未进入。故即使角色障碍消失，实际平方尾覆盖仍可能要求高重数或额外因子，不能由生成子群成员资格替代。
claim_status: computationally_reproduced
topics:
- type-I
- type-II
- descent
- even-source
- divisor-residues
- product-sets
- exponent-deficit
- finite-audit
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# H19 十亿第四压力点有限积集型平方尾的指数缺口

设 \(M_1\) 为一条兼容偶源射线的尾尺度。实际递降只允许

\[
e_1\mid M_1^2.
\]

对目标已在 \(M_1\) 素因子生成子群内、但仍无实际平方尾证书的九条射线，定义首达幂

\[
L_{\min}=\min\{L\ge2:-M_1\bmod r\in\Pi_r(M_1^L)\}. \tag{1}
\]

将搜索截断于 \(L\le12\)，得到：

| 首达幂 | 射线数 |
|---:|---:|
| 3 | 1 |
| 5 | 1 |
| 7 | 4 |
| \(>12\) | 3 |

所以当前平方尾 \(L=2\) 的所有九条均失败；即使目标已在抽象生成子群，最小的指数扩张也
未必很小。距离 \(c=5\) 的一条状态在 \(L=3\) 首达，距离 \(c=16323\) 的状态在
\(L=5\) 首达；距离 \(1,21,7\) 的三条状态直到 \(L=12\) 仍无命中。

这个剖面不允许把 \(M_1^L\) 的额外重复当作已实现的证书：实际问题仍是如何从同一 \(p\)
的因子结构、相邻射线或递降关系强制这种重复或引入新的素因子。它只给出精确的最低指数
门槛，供后续构造或反证使用。

## 重建

~~~bash
python3 reproductions/type_ii_h19_fourth_even_source_exponent_profile.py
python3 -m unittest tests/test_type_ii_h19_fourth_even_source_exponent_profile.py -q
~~~
