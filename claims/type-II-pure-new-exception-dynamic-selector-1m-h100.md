---
kind: claim
claim_id: type-II-pure-new-exception-dynamic-selector-1m-h100
title: 真实 pure-new 例外在 100 万、H=100 范围的动态选择器闭合
statement: 对全部不超过 1000000 且同余于 1 模 24 的素数，按 H19 旧支持和 20<=s<=100 的 canonical fan 纯新因子定义精确重算，得到 1285 个真实 E_new(1000000,100) 例外。在全部 q,k|(p-1)/4 构成的有限域上作完备存在性搜索并在命中后确定性短路，动态低缺陷尾与完整平方尾外源出口的可用性分类为 both=1266、tail-only=16、external-only=3、neither=0；因此两分支并集在这个有限范围覆盖 1285/1285。三个 external-only 素数为 67369、454969、967129。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
topics:
- type-II
- pure-new-factor
- support-defect
- external-source
- selector
- computation
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 真实 pure-new 例外在 100 万、\(H=100\) 范围的动态选择器闭合

## 精确范围与结果

令 \(E_{\mathrm{new}}(1000000,100)\) 为所有满足 \(p\le1000000\)、
\(p\equiv1\pmod{24}\) 的素数，并且对每个 \(20\le s\le100\) 都没有
H19 旧支持外的规范纯新因子。定义、两个选择器分支以及严格源提升恒等式见
[动态低缺陷尾或外源出口选择器](dynamic-low-defect-tail-or-external-exit-selector.md)。

程序从定义重算 9,732 个核心素数：其中 8,447 个被纯新因子捕获，留下

\[
\lvert E_{\mathrm{new}}(1000000,100)\rvert=1285.
\]

对每个例外，分支 T 在全部 \(q\mid(p-1)/4\) 上搜索支持缺陷至多 2 的普通
Type II 尾；分支 E 在全部 \(k\mid(p-1)/4\) 上搜索 \(M_k^2\) 的完整平方尾
除子。搜索在首次命中后按固定顺序短路；若一个分支没有命中，则该点上该分支的有限
候选域已经穷尽。结果是：

| 可用分支 | 数目 |
|---|---:|
| T 与 E 都可用 | 1266 |
| 仅 T 可用 | 16 |
| 仅 E 可用 | 3 |
| 两者都不可用 | 0 |

优先选 T 时，\(1282\) 个点走低缺陷尾、\(3\) 个点走外源出口，没有未决点。存在
T 见证的 1,282 个点中，最小支持缺陷为 0 的有 1,237 个，为 1 的有 45 个，为 2 的有
0 个。仅 E 可用的边界点与完整见证分别保存在结果文件中：

\[
\begin{array}{c|c|c|c|c}
p & k & 4k-1 & n_k & e\\
\hline
67369 & 6 & 23 & 64562 & 684\\
454969 & 3 & 11 & 417055 & 239\\
967129 & 1 & 3 & 725347 & 113
\end{array}
\]

这三个记录各自通过精确整数除法和 \(\operatorname{Fraction}\) 恒等式重放源解与提升后的
目标解。它们说明分支 E 在这一范围仍然不是冗余分支；但不说明完整平方尾相对任一较窄
子族在覆盖意义下必不可少。

## 紧凑、可校验的产物

完整记录包含所有 1,285 个例外的证书，因而没有直接提交。紧凑产物保留例外素数列表、
分类边界点、三个 `external-only` 完整记录与规范化完整记录数组的 SHA-256：

\[
\texttt{d0dacf0650e5d29b093f6754bd1ec916ea7ed9d74c8b3dfc2040925a400863ac}.
\]

规范化方式是以 UTF-8 编码、`ensure_ascii=false`、键排序且分隔符为 `(',', ':')` 的
JSON `records` 数组。测试会重新运行全部实验、重建该紧凑报告并要求字节语义相同，而不是
只比较聚合计数。

- 实现：
  [`reproductions/type_ii_pure_new_exception_dynamic_selector.py`](../reproductions/type_ii_pure_new_exception_dynamic_selector.py)
- 紧凑结果：
  [`reproductions/type-ii-pure-new-exception-dynamic-selector-1m-h100-summary.json`](../reproductions/type-ii-pure-new-exception-dynamic-selector-1m-h100-summary.json)
- 复现测试：
  [`tests/test_type_ii_pure_new_exception_dynamic_selector.py`](../tests/test_type_ii_pure_new_exception_dynamic_selector.py)

~~~bash
python3 reproductions/type_ii_pure_new_exception_dynamic_selector.py \\
  --limit 1000000 --shift-bound 100 --max-support 2 --compact \\
  --output reproductions/type-ii-pure-new-exception-dynamic-selector-1m-h100-summary.json
python3 -m unittest tests.test_type_ii_pure_new_exception_dynamic_selector -v
~~~

## 边界条件

这是一项确定性的有限复现，状态只能是 `computationally_reproduced`。它把真实
`Selector-Enew` 的已检验边界从 \(X=100000,H=50\) 推至 \(X=1000000,H=100\)，但没有
证明任意 \(X,H\) 的统一选择器，更不能单独推出 Erdős--Straus 猜想。
