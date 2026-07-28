---
kind: claim
claim_id: type-I-mixed-terminal-dense-800m
title: 七亿至八亿连续核心区间的混合终端闭合
statement: 对700000000<p<=800000000的611543个核心素数，611280个具有完整普通 Type II p-1 双尾证书；其余263个全部在m<=215的完整 Type I 正规形与最大尾反向提升搜索中得到偶源。每条桥均满足 E|4K^2、E=1 mod R、E<=4K-2R 且E为偶数，未闭合点为零。最大首选缺口为215，出现在p=784596409；将该点的搜索上限放宽到m<=1999仍得到同一m=215首个偶桥。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-I
- type-II
- terminal-bridge
- even-source
- descent
- mixed-selector
- finite-audit
- continuous-interval
- boundary
sources:
- paper: bradford2024
  locator: Propositions 1--4
  role: Type-I-and-Type-II-certificate-context
- paper: chamberland2026
  locator: Theorem 1
  role: Type-II-factorization-context
visibility: public
last_checked: '2026-07-29'
---

# 七亿至八亿连续核心区间的混合终端闭合

## 审计范围

对整个连续区间

\[
700{,}000{,}000<p\le800{,}000{,}000,
\qquad p\equiv1\pmod {24},
\]

先穷尽每个 \(d\mid p-1\)、\(4\mid d\) 的普通 Type II 双尾条件。对遗漏点再按

\[
3\le m\le215,\qquad m\equiv3\pmod4
\]

枚举全部 Type I 正规形及其严格最大尾反向提升，并保留首个偶源。每条记录都从正规形、
目标解、反向桥和偶源解重建 \(p^2E\)，核验

\[
E\mid4K^2,\qquad E\equiv1\pmod R,\qquad
E\le4K-2R,\qquad 2\mid E.
\]

## 结果

| 分支 | 核心素数数目 |
| --- | ---: |
| 普通 Type II \(p-1\) 双尾 | 611,280 |
| Type I 正规形偶终端桥 | 263 |
| 未闭合 | 0 |
| 合计 | 611,543 |

因此有精确分流

\[
611{,}543=611{,}280_{\mathrm{Type\ II\ tail}}
+263_{\mathrm{Type\ I\ even\ terminal}}.
\]

263 条回退记录的首选缺口分布为

\[
\begin{array}{c|rrrrrrrrrrrrrrrrrr}
m&15&19&27&31&35&39&43&47&51&55&59&63&67&71&79&87&119&215\\
\hline
\text{数量}&82&50&13&51&9&9&2&17&5&7&3&5&1&4&1&2&1&1
\end{array}
\]

最大缺口为

\[
p=784{,}596{,}409,\qquad m=215.
\]

该点的首个偶桥为正规形

\[
(A,B,C)=(34509,4,1421),
\]

并在第 27 张正规形、第四条严格反向提升处出现。对同一点将上限分别放宽到
\(m\le999\) 和 \(m\le1999\)，首个偶桥仍为 \(m=215\) 的同一记录。

## 结论边界

该区间没有发现 \(m\le215\) 盒内的混合终端反例，并把连续有限覆盖推进到
800M。\(p=784596409\) 同时提供了当前首选缺口的明确压力峰值，但它不是反例：
放宽搜索后仍有偶终端桥。

这仍不是全称证明。所有区间结论都受有限 \(m\) 盒限制；\(m=215\) 的出现反而说明
不能把此前较小的经验上界当作稳定常数。下一步应继续监测缺口是否无界，并寻找能从
普通 Type II 遗漏的因子结构直接构造 Type I 正规形的理论关系。

## 复现

~~~bash
python3 reproductions/type_i_mixed_terminal_dense_interval.py \
  --lower-exclusive 700000000 \
  --upper 800000000 \
  --gap-cap 215 \
  --output reproductions/type-i-mixed-terminal-dense-700m-800m-results.json
~~~

单点边界放宽检查：

~~~bash
python3 - <<'PY'
import importlib.util
from pathlib import Path
root = Path('.')
spec = importlib.util.spec_from_file_location(
    'even_source',
    root / 'reproductions' / 'type_i_tail_reverse_even_source_closure.py',
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
witness, _, _ = module.first_even_source_edge(784596409, 1999)
assert witness['gap'] == 215
PY
~~~

结果文件：
[type-i-mixed-terminal-dense-700m-800m-results.json](../reproductions/type-i-mixed-terminal-dense-700m-800m-results.json)
