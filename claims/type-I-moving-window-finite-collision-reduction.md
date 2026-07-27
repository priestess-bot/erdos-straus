---
kind: claim
claim_id: type-I-moving-window-finite-collision-reduction
title: Type I 移动窗口失败的有限碰撞--私有因子分解
statement: 对固定窗口 \(j=1,\ldots,J\)，令 \(m_j=4j-1\)、\(x_j=(p+m_j)/4\)，并从 \(x_j\) 剥离全部小于 \(J\) 的素因子幂，写 \(x_j=E_jR_j\)。则 \(R_1,\ldots,R_J\) 两两互素，且 Type I 的完整平方除子残数集分解为 \(\Pi_{m_j}(E_j^2)\Pi_{m_j}(R_j^2)\)。第 j 个位置失败当且仅当私有积集避开有限目标 \((-1/4)\Pi_{m_j}(E_j^2)^{-1}\)。首个六小缺口共同失败 \(p=21169,J=7\) 逐项精确复现该分解。
claim_status: established
topics:
- type-I
- moving-window
- collision
- divisor-residues
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 1
  role: Type-I-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# Type I 移动窗口失败的有限碰撞--私有因子分解

## 定理

固定 \(J\ge2\)，令 \(p>4J\) 为核心素数，并对 \(1\le j\le J\) 写

\[
m_j=4j-1,\qquad x_j=\frac{p+m_j}{4}.
\]

把 \(x_j\) 中所有小于 \(J\) 的素因子幂收进 \(E_j\)，其余部分记为 \(R_j\)：

\[
x_j=E_jR_j. \tag{1}
\]

则 \(R_1,\ldots,R_J\) 两两互素。又令

\[
\Pi_m(N^2)=\{e\bmod m:e\mid N^2\}.
\]

由于 \((x_j,m_j)=1\)，有精确乘积分解

\[
\Pi_{m_j}(x_j^2)
=\Pi_{m_j}(E_j^2)\Pi_{m_j}(R_j^2). \tag{2}
\]

第 \(j\) 个位置没有 Type I 证书，当且仅当

\[
\Pi_{m_j}(R_j^2)\cap
\left(-\frac14\right)\Pi_{m_j}(E_j^2)^{-1}=\varnothing. \tag{3}
\]

这里右边是由碰撞部分 \(E_j\) 完全确定的有限目标集。

## 证明

若素数 \(\ell\mid x_j,x_k\)，则

\[
\ell\mid x_j-x_k=j-k. \tag{4}
\]

所以一个同时整除 \(R_j,R_k\) 的素数满足 \(\ell\ge J\) 且
\(\ell\mid|j-k|<J\)，矛盾，证明私有部分两两互素。

若 \(\ell\mid x_j,m_j\)，则 \(\ell\mid4x_j-m_j=p\)。但
\(\ell\le m_j<p\)，矛盾；故各因子在模 \(m_j\) 中都是单位。平方因子的唯一分解立即给出
(2)。Bradford 的 Type I 判据等价于

\[
-\frac14\in\Pi_{m_j}(x_j^2). \tag{5}
\]

将 (2) 代入 (5) 并把碰撞残数移到另一侧，即得 (3)。

## 首个小扇失败

对

\[
p=21169,\qquad J=7,\qquad m_j=3,7,11,15,19,23,27,
\]

七个位置都没有 Type I 证书；下一个缺口 \(m=31\) 才首次恢复。此时碰撞素数为
\(2,3,5\)，所有 \(R_j\) 两两互素。程序逐项枚举 \(E_j^2\)、\(R_j^2\) 的全部除子残数，
并精确检验 (2)、(3)。

这把 “六小缺口同时失败” 转写为七个彼此私有的有限乘积集约束，而不是一个单一的固定
同余障碍。

## 含义

这条分解与既有的 Type II 窗口状态兼容，但 Type I 目标是固定残数 \(-1/4\)，而非
随 \(x_j\) 变化的 \(-x_j\)。因此下一步可检验的命题是：当窗口增长时，这些两两互素的
私有因子积集是否能无限期同时避开 (3) 的目标集。

现阶段不能假定答案是否定。有限窗口可以存在共同失败，且
[深层 AC 逃逸的 Type I 仿射边界](type-I-escape-affine-boundary.md) 排除了最简单的
统一因子解释。任何跨缺口强迫引理都必须使用真实私有因子的残数演化，不能只增加固定
缺口或固定模板。

## 重建

    python3 reproductions/type_i_moving_window_collision.py
    python3 -m unittest tests/test_type_i_moving_window_collision.py -q
