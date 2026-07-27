---
kind: claim
claim_id: type-I-one-private-three-coset-saturation
title: Type I 一私有因子的三余类饱和判据
statement: 设 \(x=Er\)，其中 \(r\) 是一个与 m 互素的私有素因子，令 \(K\) 为 E 的素因子残数生成子群、\(t=-1/4\bmod m\)。若 \(\Pi_m(E^2)=K\)，且 r 在 \(H/K\) 中的阶至多3（\(H=\langle K,r\rangle\)），则 \(t\in H\) 必推出 Type I 证书。逐素因子阶条件 \(2a_q\ge\operatorname{ord}_m(q)-1\) 是 \(\Pi_m(E^2)=K\) 的充分条件。故若 \(t\in H\) 仍失败，要么固定平方除子残数未饱和，要么私有残数在商群中的阶至少4。当前403个有限积集型位置中，350个为前者、53个为后者。
claim_status: established
topics:
- type-I
- divisor-residues
- product-sets
- subgroup
- moving-window
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# Type I 一私有因子的三余类饱和判据

## 定理

设 \(m\) 是合法缺口，\(x=Er\)，其中

\[
E=\prod_q q^{a_q},\qquad (Er,m)=1,
\]

而 \(r\) 是一私有素因子模型中的私有素数残数。置

\[
K=\langle q\bmod m:q\mid E\rangle,\qquad
H=\langle K,r\bmod m\rangle,\qquad
t=-\frac14\pmod m. \tag{1}
\]

假设固定因子的平方除子残数已经饱和：

\[
\Pi_m(E^2)=K, \tag{2}
\]

并且 \(rK\) 在商群 \(H/K\) 中的阶至多 3。则

\[
t\in H\quad\Longrightarrow\quad t\in\Pi_m(x^2), \tag{3}
\]

即存在 Type I 证书。

所以在 \(t\in H\) 但 Type I 仍失败时，必有：

\[
\text{(i) }\Pi_m(E^2)\ne K
\quad\text{或}\quad
\text{(ii) }\operatorname{ord}_{H/K}(rK)\ge4. \tag{4}
\]

## 证明

私有素因子在 \(x^2\) 中只可取 \(r^0,r^1,r^2\)，所以

\[
\Pi_m(x^2)=K\{1,r,r^2\}. \tag{5}
\]

若 \(rK\) 的商阶不超过3，则

\[
H=K\cup Kr\cup Kr^2=K\{1,r,r^2\}. \tag{6}
\]

式 (2)、(5)--(6) 给出 \(\Pi_m(x^2)=H\)，故 \(t\in H\) 时 Bradford Type I 判据成立。
逆否命题就是 (4)。

一个便于检验的充分条件是：若 \(E=\prod q^{a_q}\) 且每个 \(q\mid E\) 满足

\[
2a_q\ge\operatorname{ord}_m(q)-1, \tag{7}
\]

则 \(q^0,\ldots,q^{2a_q}\) 覆盖 \(\langle q\rangle\)，从而 \(\Pi_m(E^2)=K\)。

## 当前状态剖面

在 [Type I 自适应逃逸深度剖面](type-I-adaptive-escape-seed-profile.md) 的 403 个
“目标已在生成子群中但仍失败”的位置中：

| 障碍 | 数量 |
|---|---:|
| 固定因子未饱和，商阶至多 3 | 350 |
| 固定因子未饱和，商阶至少 4 | 14 |
| 固定因子已饱和，商阶至少 4 | 39 |

特别地，当前积集型主残余的 \(350/403\) 已被压缩为“碰撞因子指数不够”的问题，而非
大商群的不可控残数。

## 研究用途与边界

这给出一个直接的推进靶点：证明增长窗口中长期逃逸会迫使某些碰撞素因子指数达到 (2)，
或证明未饱和状态的持续出现需要无界的新私有因子复杂度。

商阶至少4时仍可能碰巧命中 \(t\)，所以表中的三类不是完整的反向分类，只是 Type I
证书的严格充分闭合机制。

完整饱和也不是必要条件。例如纯字符逃逸链的 \(m=95\) 闭合有
\(E=306\)、\(r=89\)、\(t=71\)，且 \(\Pi_{95}(E^2)\ne K\)，但
\(4\in\Pi_{95}(E^2)\) 并满足 \(4r=t\)。因此后续状态势函数不能只记录
“是否饱和”，还应记录目标相对于三平移
\(\Pi_m(E^2),\Pi_m(E^2)r,\Pi_m(E^2)r^2\) 的距离。

## 重建

    python3 reproductions/type_i_adaptive_escape_seed_profile.py
    python3 -m unittest tests/test_type_i_adaptive_escape_seed_profile.py -q
