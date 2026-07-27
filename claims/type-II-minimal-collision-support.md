---
kind: claim
claim_id: type-II-minimal-collision-support
title: H19 单新因子证书的最小碰撞支持
statement: 在 p<=5*10^8、s<=200 的341个 H19 新因子状态中，332个可取纯新因子证书，8个均可取恰含一个碰撞素因子的单新因子证书，另有372271201一状态最低需要两个碰撞素因子，首见于s=89、h=3*7*1051。该结论是有限审计，不断言窗口外仍成立。
claim_status: computationally_reproduced
topics:
- type-II
- multishift
- factorization
- new-factor
- collision-factor
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# H19 单新因子证书的最小碰撞支持

## 问题

[纯新因子选择边界](type-II-pure-new-factor-boundary.md) 发现七个状态在当前窗口内不能令
碰撞因子 \(e=1\)。这里进一步逐个枚举同一窗口中全部单新因子 Type II 除子，测量每个
状态可达到的最小碰撞素因子重数。

## 五亿结果

在 341 个含新因子状态中，最小碰撞重数的精确分布为

\[
0:332,\qquad 1:8,\qquad 2:1. \tag{1}
\]

八个必须保留一次碰撞支持的窗口状态包括原有七个纯新因子失败点及
\(p=362{,}665{,}921\)。另有

\[
p=372{,}271{,}201,\qquad s=89,\qquad h=3\cdot7\cdot1051
\]

在完整 \(s\le200\) 窗口中最低需要两个碰撞素因子。因此“三亿范围无高阶碰撞积”的
观测不能外推到五亿范围。八个一次碰撞状态的碰撞素数分布为

\[
3:4,\qquad5:1,\qquad7:1,\qquad13:1,\qquad17:1. \tag{2}
\]

例如 \(p=55{,}722{,}241\) 最早在 \(s=48\) 以
\(h=13\cdot827=10{,}751\) 命中；而 \(p=372{,}271{,}201\) 是最小的两碰撞压力点。

## 边界

式 (1) 不证明碰撞积有统一大小界。特别地，\(p=372{,}271{,}201\) 在 \(s\le400\)
仍无零/一碰撞单新因子，但在 \(s=401\) 释放为一次碰撞、在 \(s=484\) 释放为纯新因子，
见[首个两碰撞状态的延迟释放边界](type-II-h19-two-collision-release-boundary.md)。
所以“固定窗口内只需一碰撞”与“最终会释放为一碰撞”是不同命题；任何全称证明仍须解释
碰撞重数或释放深度的状态依赖演化，或在选择失败时给出可提升的递降。

## 重建

    python3 reproductions/type_ii_minimal_collision_support.py
    python3 -m unittest tests/test_type_ii_minimal_collision_support.py -q
