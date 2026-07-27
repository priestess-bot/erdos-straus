---
kind: claim
claim_id: dynamic-distance-polynomial-descent-boundary
title: 深层 AC 条件逃逸进程的动态距离多项式尾递降边界
statement: 对 p(t)=245044800t+1，取每个奇数 c|((245044800)/4)，并用动态尺度 k(t)=245044800t/(4c) 将外部源写为 p(t)-c。完整枚举全部215个可行固定源移位状态；对每个状态，枚举 M1(t)^2 的所有整系数多项式因子 e(t) 且最终满足 e(t)<=M1(t)，并检查完整平方尾同余 e(t)=-M1(t) mod r(t)。共检查7001744个候选，命中为零。故这条条件逃逸进程没有该动态距离族的统一固定移位多项式尾严格递降。
claim_status: computationally_reproduced
topics:
- descent
- external-source
- polynomial-factors
- conditional-boundary
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: Type-I-descent-context
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-25'
---

# 深层 AC 条件逃逸进程的动态距离多项式尾递降边界

## 动态距离族

令 \(N=245044800\)、\(p(t)=Nt+1\)。对每个奇数 \(c\mid N/4\)，取

\[
k(t)=\frac{Nt}{4c},\qquad q(t)=4k(t)-1.
\]

相应外部源恰为

\[
\frac{q(t)p(t)+1}{q(t)+1}=p(t)-c. \tag{1}
\]

对源 \(p(t)-c\) 的固定移位 \(a\)，写

\[
s(t)=\frac{p(t)-c}{a}=1+cr(t),\qquad
k_1(t)=\frac{a r(t)+1}{4},\qquad M_1(t)=k_1(t)s(t). \tag{2}
\]

完整平方尾递降要求一个满足

\[
e(t)\mid M_1(t)^2,\qquad e(t)\le M_1(t),\qquad
e(t)\equiv-M_1(t)\pmod {r(t)}. \tag{3}
\]

的因子。这里仅审计 \(e(t)\) 为整系数多项式且不等式对充分大 \(t\) 成立的统一情形。

## 精确结果

固定移位的整除性、\(s(t)=1+cr(t)\) 及模四条件将可能状态压为 215 个。
每个 \(M_1(t)\) 是两个整系数一次式与固定内容的乘积；故 \(M_1(t)^2\) 的次数不超过
二、且最终不超过 \(M_1(t)\) 的所有多项式因子均可由这两个一次因子的指数
\(0,1,2\) 及固定内容平方的因子穷尽。

| 项目 | 数量 |
|---|---:|
| 动态距离固定移位状态 | 215 |
| 最终有界的多项式平方尾因子 | 7,001,744 |
| 满足 (3) 的递降尾 | 0 |

重建：

    python3 reproductions/dynamic_distance_polynomial_descent_boundary.py \
      --output reproductions/dynamic-distance-polynomial-descent-boundary-results.json
    python3 -m unittest tests/test_dynamic_distance_polynomial_descent_boundary.py -q

## 含义与边界

这不排除从 \(p(t)-c\) 选择非多项式因子，也不排除多个源状态的耦合提升或其它递降。
但它排除了利用该进程固定可见因子、以统一多项式尾把动态 \(p-c\) 源接回目标的最直接
方案。后续正向工作必须对因子分布给出新的输入，或构造依赖多个源解状态的严格提升。
