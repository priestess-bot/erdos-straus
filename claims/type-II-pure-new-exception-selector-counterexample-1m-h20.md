---
kind: claim
claim_id: type-II-pure-new-exception-selector-counterexample-1m-h20
title: 真实 E_new(100 万,20) 中动态 T/E 选择器的三个完整反例
statement: 令 T 为任意 q|(p-1)/4 上支持缺陷至多2的普通 Type II 尾分支，E 为任意 k|(p-1)/4 上的完整平方尾外源出口分支。素数 p=214729、297049、878089 均属于 E_new(1000000,20)，但对每个 q|(p-1)/4 均不存在任何 d|(B+q)^2、d<=B+q、d=-(B+q) mod(4q-1)，且对每个 k|(p-1)/4 均不存在 e|M_k^2、e<=M_k、e=-M_k mod(4k-1)。因此当前全称 Selector-Enew 为假；这不构成 Erdős--Straus 猜想的反例。
claim_status: contradicted
proof_provenance: computational_reproduction
review_status: independent_review
topics:
- type-II
- pure-new-factor
- support-defect
- external-source
- selector
- counterexample
- computation
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 真实 \(E_{\mathrm{new}}(10^6,20)\) 中动态 T/E 选择器的三个完整反例

## 被否定的命题

令 \(B=(p-1)/4\)。当前 `Selector-Enew` 的两个分支是：

\[
\begin{aligned}
\mathrm{T}:&\quad \exists q\mid B,\ \exists d\mid(B+q)^2,\quad
d\le B+q,\quad d\equiv-(B+q)\pmod{4q-1},\\
&\hspace{36mm}\left|\operatorname{Supp}(d)\setminus\operatorname{Supp}(q)\right|\le2;\\
\mathrm{E}:&\quad \exists k\mid B,\ \exists e\mid M_k^2,\quad
e\le M_k,\quad e\equiv-M_k\pmod{4k-1}.
\end{aligned}
\]

在 \(X=10^6,H=20\) 的精确输入上，主枚举从 9,732 个核心素数得到 9,195 个真实
\(E_{\mathrm{new}}\) 元素。其中恰有三个点同时未命中 T 与 E：

\[
214729,\qquad297049,\qquad878089.
\]

## 独立完整穷尽

下表的候选数是独立审计中实际逐一检查的合法除子数。T 列遍历每个 \(q\mid B\) 的全部
\(d\mid(B+q)^2\)、\(d\le B+q\)；E 列遍历每个 \(k\mid B\) 的全部
\(e\mid M_k^2\)、\(e\le M_k\)。三行的相应同余命中数都是零。

| \(p\) | \(B\) 的分解 | \(p+80\) 的分解 | \(\#(q\mid B)\) | T 合法除子数 | \(\#(k\mid B)\) | E 合法除子数 |
|---:|---|---|---:|---:|---:|---:|
| 214729 | \(2\cdot3\cdot23\cdot389\) | \(3\cdot7\cdot53\cdot193\) | 16 | 803 | 16 | 2399 |
| 297049 | \(2\cdot3\cdot12377\) | \(3\cdot7\cdot14149\) | 8 | 118 | 8 | 400 |
| 878089 | \(2\cdot3\cdot36587\) | \(3\cdot17\cdot67\cdot257\) | 8 | 133 | 8 | 580 |

对 \(H=20\)，唯一新增移位的规范模数为 \(4a_{20}c_{20}=40\)。表中每个 \(p+80\)
的全部素因子都不等于 \(-1\pmod{40}\)，所以三点直接满足真实 \(E_{\mathrm{new}}\) 定义，
无需把旧支持当作近似代理。

更强地，T 的三次完整搜索没有任何同余除子，故不依赖支持缺陷阈值：对三个点，普通
\(p-1\) Type II 尾的所有尺度均失败。E 的完整平方尾搜索同样无命中。独立脚本不导入
主 SPF 选择器，而是以 SymPy 的 `factorint` 与 `divisors` 直接枚举；回归测试还会重跑
主实现并要求其未决列表完全一致。

## 结论与边界

因此“对每个真实筛例外，T 或 E 至少一个出现”的当前全称 `Selector-Enew` 为假。这个结论
只否定该递降接口，不能推出这三个素数没有其他单位分数分解，也不反驳 Erdős--Straus
猜想。尤其，单纯把 T 的支持缺陷上界从 2 提高到任意有限值也无法修复这三点，因为 T 的
同余候选集合本身为空。

## 反例之外的终端短证书

三点并非 Erdős--Straus 反例。独立的 AC 审计为它们给出直接 Type II 证书：

| \(p\) | \((A,C)\) | \(k\) | \(h\) | 首分母 \(x\) |
|---:|---|---:|---:|---:|
| 214729 | \((1,2)\) | 4 | 31 | 55414 |
| 297049 | \((1,1)\) | 32 | 127 | 74847 |
| 878089 | \((1,1)\) | 33 | 131 | 221198 |

这些证书是目标 \(4/p\) 的终端分解，不是由更小源提升而来。因此它们不会挽回 T/E
二分选择器，却指出一个不同的第三分支：`AC_2` 终端短证书。现有千万核心素数审计中，
普通双尾、完整平方因子外源与 \(\max(A,C)\le2\) 的 AC 证书合计闭合全部 82,887 个点，
见[双尾、平方因子外源递降或半径二 AC 闭合](type-II-tail-external-ac2-closure-10m.md)。
该有限闭合尚不是新的统一选择器定理。

- 主范围扫描：
  [`reproductions/type-ii-pure-new-exception-dynamic-selector-1m-h20-summary.json`](../reproductions/type-ii-pure-new-exception-dynamic-selector-1m-h20-summary.json)
- 独立穷尽产物：
  [`reproductions/type-ii-pure-new-exception-selector-counterexample-1m-h20.json`](../reproductions/type-ii-pure-new-exception-selector-counterexample-1m-h20.json)
- 独立穷尽实现：
  [`reproductions/type_ii_pure_new_exception_selector_counterexample_h20.py`](../reproductions/type_ii_pure_new_exception_selector_counterexample_h20.py)
- 交叉重放测试：
  [`tests/test_type_ii_pure_new_exception_selector_counterexample_h20.py`](../tests/test_type_ii_pure_new_exception_selector_counterexample_h20.py)

~~~bash
python3 reproductions/type_ii_pure_new_exception_dynamic_selector.py \\
  --limit 1000000 --shift-bound 20 --max-support 2 --compact \\
  --output reproductions/type-ii-pure-new-exception-dynamic-selector-1m-h20-summary.json
python3 reproductions/type_ii_pure_new_exception_selector_counterexample_h20.py
python3 -m unittest tests.test_type_ii_pure_new_exception_selector_counterexample_h20 -v
~~~
