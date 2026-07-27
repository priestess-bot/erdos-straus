---
kind: claim
claim_id: type-II-tail-deflation-selector-audit
title: 因子标记 Type II 双尾递降选择器的百万级覆盖谱
statement: 精确审计表明，在全部 9732 个 p<=10^6、p=1 mod24 的核心素数中，p-1 因子标记的 Type II 双尾递降选择器命中 9717 个、遗漏 15 个；最大最小成功缺口为 695，保持者 p=565849。十五个遗漏点全部仍有普通 Bradford 短证书，但其成功缺口不满足 m+1|p-1。这个有限覆盖谱支持将因子选择器作为递降研究主线，却不证明其对全体核心素数成立。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- factor-selection
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Section 2, Type I/II divisor certificates
  role: certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-24'
---

# 因子标记 Type II 双尾递降选择器的百万级覆盖谱

## 审计对象

对每个 $p\equiv1\pmod {24}$，枚举

\[
d\mid p-1,\qquad 4\mid d,\qquad m=d-1,
\]

并在 $x=(p+m)/4$ 的平方除子中检查 Type II 残数条件

\[
e\mid x^2,\qquad e\le x,\qquad e\equiv-x\pmod m.
\]

每个命中均由 `type-II-two-tail-deflation-descent` 给出严格源
$n=(p+m)/(m+1)<p$。

## 精确有限结果

运行

```bash
python3 reproductions/type_ii_tail_deflation_full_audit.py --limit 1000000 \
  --output reproductions/type-ii-tail-deflation-1m-results.json
```

得到

\[
\begin{array}{c|r}
\text{核心素数数目}&9{,}732\\
\text{选择器命中}&9{,}717\\
\text{选择器遗漏}&15\\
\text{最大最小成功缺口}&695
\end{array}
\]

最大最小缺口的保持者是

\[
p=565849,\qquad m=695.
\]

遗漏中的前两个为 $67369,85369$。它们不是猜想反例：脚本也为每个遗漏点记录一张
普通 Bradford 证书；例如 $p=67369$ 有 Type I 缺口 $31$，但 $32\nmid p-1$，
故不能进入此双尾递降核。

## 解释

该结果的价值在于压力测试而非覆盖率本身。选择器仅观察 $p-1$ 的因子，却已经命中
此前外部源递降组合留下的全部三百万范围逃逸点，且在独立的全体百万范围审计中只留下
十五点。残余点应作为下一阶段的反例搜索集：比较其 $p-1$ 的因子格与
$x=(p+d-1)/4$ 的除子残数，寻找能解释遗漏的结构性障碍，或者找到补充的选择器。

有限范围不允许推出“遗漏稀疏”或“最终无遗漏”。特别是，固定有限经验不能替代
对所有 $p$ 的因子选择定理。
