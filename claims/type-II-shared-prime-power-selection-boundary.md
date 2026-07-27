---
kind: claim
claim_id: type-II-shared-prime-power-selection-boundary
title: 共享 Type II 选择器的单素数幂边界
statement: 在 p<=10^7 的 84 个四自动缺口后且无 k=1 选择器的核心素数中，完整扫描所有 m<=239、m=3 mod4 的 Type II 缺口以及 p+m 的全部素数幂除子 q^e。9 个点由 e=1 命中，另一个点 p=454969 由 5^3=125 在 m=31 命中；余下 74 点没有任何单素数幂共享因子。因此在该 74 点主残余的每个共享 Type II 证书中，D 必须使用至少两个不同素因子。
claim_status: computationally_reproduced
topics:
- type-II
- shared-divisor
- factorization
- prime-powers
- divisor-residues
- computation
- obstruction
- proof-program
sources:
- paper: bradford2024
  locator: "Proposition 2"
  role: Type-II-divisor-criterion
- paper: chamberland2026
  locator: "Theorem 1"
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-25'
---

# 共享 Type II 选择器的单素数幂边界

## 检验对象

对每个四自动缺口后、无 \(k=1\) 选择器的核心素数 \(p\)，以及每个有 Type II
证书的合法缺口

\[
3\le m\le239,\qquad m\equiv3\pmod4,
\]

枚举 \(p+m\) 的所有单素数幂除子：

\[
D=q^e\mid p+m,\qquad e\ge1,\qquad q^e\equiv1\pmod m. \tag{1}
\]

令 \(k=(D-1)/m\)。脚本以完整 SPF 分解枚举 (1)，并重建缩放首分母的 Type II
表示，故这里既检查除子残数，也检查同缺口的表示兼容性。

## 精确结果

在千万范围的 84 个压力点中：

\[
\begin{aligned}
\#\{\text{有单素数幂共享证书}\}&=10,\\
\#\{\text{无单素数幂共享证书}\}&=74.
\end{aligned} \tag{2}
\]

前 9 个正好是单素因子边界中的点。额外的、唯一真正素数幂救回为

\[
p=454969,\qquad m=31,\qquad D=5^3=125,\qquad k=4. \tag{3}
\]

按最小命中缺口，10 点分布为：

| 最小缺口 | 点数 |
|---:|---:|
| 15 | 1 |
| 31 | 3 |
| 39 | 5 |
| 95 | 1 |

百万范围中，15 个相应压力点只有 (3) 这一点被单素数幂命中，剩余 14 点皆无。

运行：

    python3 reproductions/type_ii_automatic_residual_k1_funnel.py \
      --limit 10000000 --gap-cap 239 --single-prime-profile \
      --prime-power-profile \
      --output reproductions/type-ii-automatic-residual-prime-power-profile-10m-results.json

会重建 (2)、(3) 和全部 74 个遗漏。

## 推论与边界

对这 74 个点，若 \(D\mid p+m\)、\(D\equiv1\pmod m\) 且 \(D\) 给出同缺口的
共享 Type II 证书，则 \(D\) 不能是任何 \(q^e\)。由唯一分解，\(D\) 因而至少有
两个不同的素因子。这是当前有限范围内的严格排除，而不是关于所有素数的定理。

这就把正向问题从“找到一个具有目标残数的素因子或素数幂”收紧为：给定
\(p+m\) 的带重数素因子，何时存在一个多素支撑除子积 \(D\equiv1\pmod m\)，并与
Type II 目标除子条件在同一 \(m\) 同时满足。当前的最小支撑审计还显示，固定为
两个或三个不同素因子也不足以覆盖压力集，见
`type-II-shared-bounded-support-selection-boundary`。这个双重残数命中问题才是
共享选择器方向可推广的核心。

该边界不构成 Erdős--Straus 猜想的反例，也不把带标记的共享 Type II 表示误作
无标记递降步骤。
