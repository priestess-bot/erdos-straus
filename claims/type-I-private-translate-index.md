---
kind: claim
claim_id: type-I-private-translate-index
title: Type I 私有因子平移首达指数判据
statement: 设 \(x=Er^b\)、\(A=\Pi_m(E^2)\)、\(t=-1/4\bmod m\)，其中 r 在 \(U(m)\) 中的阶为 h。令 \(J=\{0\le i<h:t\in Ar^i\}\)。则 Type I 证书存在当且仅当某个 \(i\in J\) 满足 \(i\le2b\)。若 \(J\) 非空，最小首达指数 \(\delta=\min J\) 给出最小所需私有重数 \(b\ge\lceil\delta/2\rceil\)；若 \(J\) 为空，单独增加 r 的任意幂都不能产生证书。当前一私有模型的403个积集型失败中，121个有 \(\delta=3\)，235个有 \(\delta\ge4\)，47个 \(J\) 为空。
claim_status: established
topics:
- type-I
- divisor-residues
- product-sets
- private-factors
- moving-window
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# Type I 私有因子平移首达指数判据

## 定理

设

\[
x=Er^b,\qquad A=\Pi_m(E^2),\qquad t=-\frac14\pmod m, \tag{1}
\]

其中 \((Er,m)=1\)，\(r\) 在 \(U(m)\) 中的阶为 \(h\)。定义目标平移指标集

\[
J(E,r;t)=\{i\in\{0,\ldots,h-1\}:t\in Ar^i\}. \tag{2}
\]

则

\[
t\in\Pi_m(x^2)
\quad\Longleftrightarrow\quad
\exists i\in J(E,r;t)\ \text{使}\ i\le2b. \tag{3}
\]

若 \(J\ne\varnothing\)，记 \(\delta=\min J\)，则最小可行私有重数为

\[
b_{\min}=\left\lceil\frac\delta2\right\rceil. \tag{4}
\]

若 \(J=\varnothing\)，则任意 \(b\ge0\) 都不能仅靠增加同一私有因子 \(r\) 获得
Type I 证书。

## 证明

平方除子中 \(r\) 的指数恰可取

\[
0,1,\ldots,2b.
\]

所以

\[
\Pi_m(x^2)=\bigcup_{i=0}^{2b}Ar^i. \tag{5}
\]

指数按 \(h\) 循环，故 (5) 包含目标当且仅当 (2) 中某个代表元不超过 \(2b\)，这就是
(3)。最小化 \(b\) 得到 (4)。若 \(J\) 为空，所有 \(r\) 的幂平移都不含目标，结论立即
成立。

## 一私有状态剖面

对 [Type I 自适应逃逸深度剖面](type-I-adaptive-escape-seed-profile.md) 中的 403 个
一私有积集型失败，当前 \(b=1\)，故证书要求 \(\delta\le2\)，而所有记录都满足
\(\delta\ge3\) 或 \(J=\varnothing\)：

| 类型 | 位置数 | 构造含义 |
|---|---:|---|
| \(\delta=3\) | 121 | 将 \(r\) 的重数从1提高到2即可命中 |
| \(\delta\ge4\) | 235 | 需要更高的同一私有因子重数 |
| \(J=\varnothing\) | 47 | 必须扩张碰撞部分 \(A\) 或引入不同私有残数 |

这把原来的“有限积集型失败”分成可由少量私有重数修复、需高重数修复和根本不能由单一
私有因子修复的三个精确类别。

## 研究用途与边界

若能从相邻窗口或递降源构造中强制 \(r^2\mid x\)，就能直接消去 \(\delta=3\) 的类别；
若能证明长期逃逸中 \(J=\varnothing\) 持续出现会迫使碰撞因子复杂度无界，则可处理最后
一类。

该判据本身不保证可以自由改变 \(r\) 的重数，也不说明不同私有因子的组合如何作用；
因此它是一个精确构造目标，而非对一般 Type I 失败的全称解决。

## 重建

    python3 reproductions/type_i_adaptive_escape_seed_profile.py
    python3 -m unittest tests/test_type_i_adaptive_escape_seed_profile.py -q
