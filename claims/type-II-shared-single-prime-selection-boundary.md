---
kind: claim
claim_id: type-II-shared-single-prime-selection-boundary
title: 共享 Type II 选择器的单素因子边界
statement: 在 p<=10^7 的 84 个四自动缺口后且无 k=1 选择器的核心素数中，完整扫描所有 m<=239、m=3 mod4 的 Type II 缺口以及 p+m 的全部素因子。仅 9 个点存在素数 q|p+m、q=1 modm，并与同缺口 Type II 证书组成共享证书；余下 75 个没有任何这样的单素因子选择。故在当前最小非 k=1 压力集上，单个 1 modm 素因子规则不是全覆盖机制；后续共享选择必须处理一般除子积集或素因子幂。
claim_status: computationally_reproduced
topics:
- type-II
- shared-divisor
- factorization
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

# 共享 Type II 选择器的单素因子边界

## 判据

固定核心素数 \(p\)、合法缺口 \(m\equiv3\pmod4\)。这里检验最简单的自适应共享
选择：

\[
q\mid p+m,\qquad q\text{ 为素数},\qquad q\equiv1\pmod m. \tag{1}
\]

并独立要求该同一 \(m\) 具有 Type II 除子证书。令

\[
k=\frac{q-1}{m}.
\]

则 (1) 正是共享因子 \(D=q=km+1\) 的特殊情形。脚本还重建相应缩放首分母
表示，以核对这一素因子确实与同缺口 Type II 证书兼容。

这比只查看 `type-II-automatic-residual-k-one-funnel` 所记录的最小缺口更强：对每个
压力点，枚举所有

\[
3\le m\le239,\qquad m\equiv3\pmod4, \tag{2}
\]

而不是只检查其中首次命中的 \(m\)。

## 精确结果

在四自动缺口后无 \(k=1\) 选择器的 84 个核心素数中，得到：

\[
\#\{\text{任一 (2) 有单素因子共享 Type II 证书}\}=9,\qquad
\#\{\text{全部 (2) 均无此证书}\}=75. \tag{3}
\]

九个命中的最小缺口分布为：

| 最小缺口 | 点数 |
|---:|---:|
| 15 | 1 |
| 31 | 2 |
| 39 | 5 |
| 95 | 1 |

余下 75 个点包括此前的全缺口共享小 \(A\) 压力点 \(p=878089\)。

运行

```bash
python3 reproductions/type_ii_automatic_residual_k1_funnel.py \
  --limit 10000000 --gap-cap 239 --single-prime-profile \
  --output reproductions/type-ii-automatic-residual-single-prime-profile-10m-results.json
```

会重建 (3)、九个命中及全部 75 个遗漏。百万范围的 15 个相应压力点则一个也不命中
单素因子分支。

## 正确边界

(3) 不表示 75 个点没有共享 Type II 证书。相反，原有无界首尺度扫描已经为每个点
找到复合共享因子 \(D\equiv1\pmod m\)。这里排除的仅是 \(D\) 可以取为一个素数的
强化。

也不能把“复合”误写为“必有两个不同素因子”：例如一个素数幂也可能满足
\(D\equiv1\pmod m\)。真正尚未处理的对象是 \(p+m\) 素因子（带重数）的完整乘积集
何时到达 \(1\pmod m\)，并与 \(x^2\) 的 Type II 目标 \(-x\pmod m\) 在同一缺口
共同命中。

因此这项边界把共享选择器的正向任务进一步收紧为：研究一般素因子幂与多因子积集的
同步残数到达，不能仅继续添加指定单素因子规则。
