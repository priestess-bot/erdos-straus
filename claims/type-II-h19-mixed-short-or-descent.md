---
kind: claim
claim_id: type-II-h19-mixed-short-or-descent
title: H19 十亿残余的半径六 AC 或 mixed-factor 严格递降闭合
statement: 对存储的 p<=10^9 的664个 H19 残余，647个有 max(A,C)<=6 的直接 AC Type II 证书，656个有 mixed-factor 外部源严格递降，交集639个；余下精确分为17个仅 mixed-factor 递降和8个仅直接证书，无未闭合状态。17个仅递降状态的首次 mixed-factor 尺度最大为 k=14。这是有限闭合，不给出全称半径或尺度界。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- ac-rays
- descent
- external-source
- finite-audit
- h19
sources:
- paper: bradford2024
  locator: Propositions 1 and 3
  role: Type-I-and-Type-II-certificate-context
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-27'
---

# H19 十亿残余的半径六 AC 或 mixed-factor 严格递降闭合

设 H19 残余为前19条规范 Type II 射线未命中的 \(p\le10^9\) 核心素数。比较两个已精确
验证的出口：

\[
\begin{aligned}
\mathrm{AC}_6 &: \max(A,C)\le6\text{ 的直接 Type II AC 证书};\\
\mathrm{Mixed} &: q=4k-1,\quad n=\frac{qp+1}{q+1},\quad
g\mid kn,\quad g\le n,\quad g\equiv-1\pmod q
\end{aligned} \tag{1}
\]

其中 Mixed 由 \(e=kg\mid(kn)^2\) 给出从 \(n<p\) 到 \(p\) 的严格可提升 Type I
证书。它严格包含普通因子外部源分支，但比允许任意 \(e\mid(kn)^2\) 的完整平方因子递降窄。

| 分类 | 状态数 |
| --- | ---: |
| \(\mathrm{AC}_6\) | 647 |
| \(\mathrm{Mixed}\) | 656 |
| 两者均命中 | 639 |
| 仅 \(\mathrm{Mixed}\) | 17 |
| 仅 \(\mathrm{AC}_6\) | 8 |
| 两者均未命中 | 0 |

因此，整个存储十亿剖面满足精确析取

\[
\mathrm{AC}_6\quad\text{或}\quad\mathrm{Mixed}. \tag{2}
\]

这比“\(\mathrm{AC}_6\) 或完整平方因子递降”更强：它不需要平方因子尾中一般的
\(e\mid(kn)^2\) 机制。17 个仅 Mixed 状态的首次尺度只出现

\[
k\in\{1,2,3,5,10,14\},
\]

最大为14；8 个仅 AC 状态则全部在半径5内已经命中。该分流把今后的理论问题压缩为：
证明半径六 AC 失败如何强制一个 mixed-factor 因子 \(g\)，而不是先处理更宽的平方因子
除子集。

范围必须保留：H19、十亿上界、半径6和尺度14均来自有限审计；它们不是固定全称选择器。
尤其现有仿射逃逸边界排除了把有限 AC 模板直接外推为全局证明。

可复现命令：

~~~bash
python3 reproductions/type_ii_h19_mixed_short_or_descent.py \
  --ac-profile reproductions/type-ii-h19-residual-ac-profile-1b-results.json \
  --descent-profile reproductions/type-ii-h19-targeted-quadratic-descent-1b-results.json \
  --output reproductions/type-ii-h19-mixed-short-or-descent-1b-results.json
python3 -m unittest tests/test_type_ii_h19_mixed_short_or_descent.py -q
~~~
