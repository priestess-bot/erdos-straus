---
kind: claim
claim_id: type-II-tail-deflation-external-boundary-10m
title: 双尾缩减失败不强制标准外源递降的千万边界
statement: 在 p<=10^7 的84个普通 Type II 双尾缩减失败核心素数中，自适应外源严格递降命中70个，mixed-factor 与完整平方因子外源均命中77个；214729、297049、878089、1511449、3942409、5478169、6294649 同时逃过三族。因此“普通双尾缩减失败必强制标准、自适应 mixed 或完整平方因子外源递降”在该有限范围已被否定。
claim_status: computationally_reproduced
topics:
- type-II
- type-I
- descent
- external-source
- tail-deflation
- finite-audit
- boundary
sources:
- paper: bradford2024
  locator: Propositions 1--3
  role: certificate-and-lift-context
- paper: ventas2026
  locator: Theorem 2.3
  role: external-source-context
visibility: public
last_checked: '2026-07-27'
---

# 双尾缩减失败不强制标准外源递降的千万边界

普通 Type II 双尾缩减在 \(p\le10^7\) 的全体核心素数中留下84个状态。对每个状态完整枚举
所有 \(k\mid(p-1)/4\)，并逐项精确检查三层嵌套外源分支：

\[
\begin{array}{rcl}
\mathrm{Adaptive}&:&g\mid n,\quad g\equiv-1\pmod{4k-1};\\
\mathrm{Mixed}&:&g\mid kn,\quad g\le n,\quad g\equiv-1\pmod{4k-1};\\
\mathrm{Quadratic}&:&e\mid(kn)^2,\quad e\le kn,\quad e\equiv-kn\pmod{4k-1}.
\end{array} \tag{1}
\]

每个命中均重建严格源 \(n<p\)、源解、目标提升和 Type I 证书。结果为：

| 分支 | 命中数 | 遗漏数 |
| --- | ---: | ---: |
| Adaptive | 70 | 14 |
| Mixed | 77 | 7 |
| Quadratic | 77 | 7 |

三层共同遗漏恰为

\[
214{,}729,\ 297{,}049,\ 878{,}089,\ 1{,}511{,}449,\
3{,}942{,}409,\ 5{,}478{,}169,\ 6{,}294{,}649. \tag{2}
\]

因此，H19 十亿残余中的 \(662+2\) 全严格递降闭合不能直接提升为一般引理：
普通双尾缩减失败并不强制上述任一标准外源递降。尤其完整平方因子外源在这84个尾失败点上
没有超过 mixed-factor 的覆盖率。

这七点不是猜想反例，且不排除其他递降或直接证书。它们构成检验补充机制的最小独立压力集。

可复现命令：

~~~bash
python3 reproductions/type_ii_tail_deflation_external_boundary.py \
  --input reproductions/type-ii-tail-deflation-10m-full-results.json \
  --output reproductions/type-ii-tail-deflation-external-boundary-10m-results.json
python3 -m unittest tests/test_type_ii_tail_deflation_external_boundary.py -q
~~~
