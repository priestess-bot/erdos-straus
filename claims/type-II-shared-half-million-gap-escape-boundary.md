---
kind: claim
claim_id: type-II-shared-half-million-gap-escape-boundary
title: 共享 Type II 选择器的半百万缺口逃逸边界
statement: 对核心素数 p=33011449，完整枚举全部 3<=m<=500000、m=3 mod4 的缺口；每个缺口均完整检查 Type II 除子条件和 p+m 的全部 1 modm 非平凡除子。125000 个合法缺口均无共享 Type II 证书。故固定 m<=500000 的共享因子扇不能覆盖全部核心素数。
claim_status: computationally_reproduced
topics:
- type-II
- shared-divisor
- gap-selection
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

# 共享 Type II 选择器的半百万缺口逃逸边界

## 完整单点审计

取

\[
p=33011449.
\]

对每个

\[
3\le m\le500000,\qquad m\equiv3\pmod4, \tag{1}
\]

令 \(x=(p+m)/4\)。审计首先完整枚举 \(x^2\) 的除子，以检查

\[
-x\in\Pi_m(x^2), \tag{2}
\]

然后在 (2) 成立时完整枚举 \(p+m\) 的非平凡除子，以检查

\[
D\mid p+m,\qquad D\equiv1\pmod m. \tag{3}
\]

因此扫描的正是 `type-II-shared-residue-selector-conjecture` 在每个给定缺口的两项
条件，而不是一个 \(k\)、因子长度或除子大小截断。

## 结果

(1) 中最后一个合法缺口为 \(499999\)，共计

\[
125000
\]

个。所有这些缺口都没有同时满足 (2) 与 (3)；即最小共享 Type II 见证为 `null`。

运行：

    python3 reproductions/type_ii_shared_gap_escape.py \
      --prime 33011449 --gap-cap 500000 \
      --output reproductions/type-ii-shared-gap-escape-p33011449-500k-results.json

可重建该空扫描。

## 含义与严格限制

这严格排除任何仅承诺

\[
m\le500000
\]

的共享 Type II 因子扇覆盖定理，哪怕允许因子 \(D\) 的首尺度、素因子支撑和长度
完全随 \(p,m\) 自适应。

它不表示 \(p=33011449\) 没有 Erdős--Straus 分解，也不表示该素数在
\(m>500000\) 没有共享 Type II 证书。事实上，该素数已在较小缺口

\[
m=19,\qquad x=\frac{p+19}{4},\qquad d=49
\]

满足直接 Type II 的除子条件 \(d\equiv-x\pmod {19}\)。所以这里失败的是额外的
共享因子标记，而不是 Type II 表示本身。

这项审计只说明共享选择器若为真，所需缺口不能由一个固定的半百万上界控制；后续论证
必须允许真正增长的缺口，或转向不依赖这类共享标记的直接 Type I/II 证书。
