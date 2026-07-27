---
kind: claim
claim_id: type-II-h19-two-collision-release-boundary
title: H19 首个两碰撞单新因子状态的延迟释放边界
statement: 在 p=372271201 的 H19 残余状态中，完整 s<=200 的单新因子审计最少需要两个碰撞素因子，首个见证为 s=89、h=3*7*1051；完整扫描至 s=400 仍无零/一碰撞单新因子，s=401 首次释放为一碰撞 h=5*26947，s=484 首次释放为纯新因子 h=3343。这是状态依赖深度的有限边界，不给出统一上界。
claim_status: computationally_reproduced
topics:
- type-II
- multishift
- collision-factor
- new-factor
- release-depth
- boundary
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
visibility: public
last_checked: '2026-07-25'
---

# H19 首个两碰撞单新因子状态的延迟释放边界

在五亿 H19 审计中，\(p=372{,}271{,}201\) 是首个在 \(s\le200\) 的完整单新因子窗口内
最低碰撞重数为二的状态。对同一状态逐移位延长枚举，得到：

| 移位上限 | 最低碰撞见证 | 首个零/一碰撞 | 首个纯新 |
|---:|---|---|---|
| 200 | \(s=89,\ h=3\cdot7\cdot1051\) | 无 | 无 |
| 400 | 同左 | 无 | 无 |
| 401 | 同左 | \(s=401,\ h=5\cdot26947\) | 无 |
| 483 | 同左 | 同左 | 无 |
| 484 | \(s=484,\ h=3343\) | 同左 | \(s=484,\ h=3343\) |

每一行都完整枚举 \(20\le s\) 至该上限的全部单新因子规范 Type II 因子，并重建证书。
所以 \(s\le200\) 的“零/一碰撞单新因子”有限强化版在此点失败，但该点不是未限定移位
选择器的反例：它在更深的状态依赖移位释放。

这三层还带有精确的来源标签迁移。\(s=89\) 的碰撞因子 \(3,7\) 分别来自 H19 的
\(2\bmod3\) 与 \(5\bmod7\) 移位类；\(s=401\) 的因子 \(5\) 来自
\(1\bmod5\) 类；\(s=484\) 的纯新因子没有碰撞来源标签。所有这些同余都由
\(\ell\mid p+4t,\ell\mid p+4s\Rightarrow s\equiv t\pmod\ell\) 逐项核验。
故若存在可证明的释放势能，它至少需要记录来源标签集合，而不能只记录碰撞重数。

这个例子同时否定两种不充分的推进方式：把三亿范围的零/一分布外推为固定窗口规律，或把
窗口内两碰撞状态误判为永久障碍。真正待证的状态不变量必须能解释何时以及为何碰撞重数
下降，且不能预设统一的释放深度。

重建：

~~~bash
python3 reproductions/type_ii_h19_two_collision_release_boundary.py
python3 -m unittest tests/test_type_ii_h19_two_collision_release_boundary.py -q
~~~
