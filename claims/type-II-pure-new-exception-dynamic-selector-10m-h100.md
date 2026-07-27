---
kind: claim
claim_id: type-II-pure-new-exception-dynamic-selector-10m-h100
title: 真实 pure-new 例外在 1000 万、H=100 范围的动态选择器闭合与尺度诊断
statement: 对全部不超过 10000000 且同余于 1 模 24 的素数，按 H19 旧支持和 20<=s<=100 的 canonical fan 纯新因子定义精确重算，得到 7056 个真实 E_new(10000000,100) 例外。在全部 q,k|(p-1)/4 构成的有限域上作完备存在性搜索并在命中后确定性短路，动态低缺陷尾与完整平方尾外源出口的可用性分类为 both=7016、tail-only=32、external-only=8、neither=0；因此两分支并集在这个有限范围覆盖 7056/7056。尾分支的最小支持缺陷仅为 0 或 1，但达到该最小缺陷所需的最小尺度最大为 q=714，出现在 p=4435369；这是一项动态尺度需求的有限诊断，不是尺度无界定理。
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
- scale-selection
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-certificate-context
visibility: public
last_checked: '2026-07-27'
---

# 真实 pure-new 例外在 1000 万、\(H=100\) 范围的动态选择器闭合与尺度诊断

## 精确范围与联合覆盖

对每个 \(p\le10^7\)、\(p\equiv1\pmod{24}\)，程序按
[动态低缺陷尾或外源出口选择器](dynamic-low-defect-tail-or-external-exit-selector.md) 中的
定义重算 \(E_{\mathrm{new}}(10^7,100)\)。82,887 个核心素数中，75,831 个具有规范纯新
因子；余下

\[
\lvert E_{\mathrm{new}}(10^7,100)\rvert=7056.
\]

对每个例外，分支 T 在全部 \(q\mid(p-1)/4\) 上穷尽支持缺陷至多 2 的普通 Type II
尾；分支 E 在全部 \(k\mid(p-1)/4\) 上穷尽 \(M_k^2\) 的完整平方尾除子。命中时按固定顺序
短路，未命中则已经遍历该点的完整有限候选域。可用性分类为：

| 可用分支 | 数目 |
|---|---:|
| T 与 E 都可用 | 7016 |
| 仅 T 可用 | 32 |
| 仅 E 可用 | 8 |
| 两者都不可用 | 0 |

优先选 T 后，有

\[
7056=7048_{\mathrm{tail}}+8_{\mathrm{external}}+0_{\mathrm{unresolved}}.
\]

尾分支的全局最小支持缺陷分布是

\[
6790_{\delta=0}+258_{\delta=1}+0_{\delta=2}=7048.
\]

这再次说明完整平方尾外源出口不是样本中的冗余分支，同时没有把有限零遗漏升级为统一
`Selector-Enew` 定理。

## 动态尺度诊断

对于每个保存的 T 见证，程序先最小化支持缺陷，再在达到该缺陷的尺度中选最小的
\(q\)。在百万范围中该尺度最大为 \(174\)；本范围中升至

\[
q=714=2\cdot3\cdot7\cdot17
\]

并发生在 \(p=4435369\)。此时

\[
\frac{p-1}{4}=1108842=714\cdot1553,
\qquad u=1554,
\qquad m=4q-1=2855,
\]

而 \(d=9604=2^2\cdot7^4\) 满足 \(d\mid(qu)^2\)、\(d\le qu\)、
\(d\equiv-qu\pmod{2855}\)。所以该点有支持缺陷 0 的 Type II 尾，并严格降至分母
\(u=1554\)。

这不是“所需尺度必无界”的证明：有限样本只能表明一个固定小菜单不能解释当前所有命中。
它与已有固定有限菜单的条件性逃逸边界一致，并把可证明的下一步精确化为：从
\(p\in E_{\mathrm{new}}(X,H)\) 的结构中选择一个随状态变化的 \(q\)，而非预先固定
有限多个尺度。

## 可复现锚点

紧凑结果保留 7,056 个例外素数、分类边界、8 个 `external-only` 完整记录和完整记录数组的
规范 SHA-256：

\[
\texttt{28b97d12289fedd7df9662341fb9328751ce1a424480a8e8344d950d58c7e2cb}.
\]

- 实现：
  [`reproductions/type_ii_pure_new_exception_dynamic_selector.py`](../reproductions/type_ii_pure_new_exception_dynamic_selector.py)
- 紧凑结果：
  [`reproductions/type-ii-pure-new-exception-dynamic-selector-10m-h100-summary.json`](../reproductions/type-ii-pure-new-exception-dynamic-selector-10m-h100-summary.json)
- 确定性复现测试：
  [`tests/test_type_ii_pure_new_exception_dynamic_selector.py`](../tests/test_type_ii_pure_new_exception_dynamic_selector.py)

~~~bash
python3 reproductions/type_ii_pure_new_exception_dynamic_selector.py \\
  --limit 10000000 --shift-bound 100 --max-support 2 --compact \\
  --output reproductions/type-ii-pure-new-exception-dynamic-selector-10m-h100-summary.json
python3 -m unittest tests.test_type_ii_pure_new_exception_dynamic_selector -v
~~~

## 边界条件

这是一项精确的有限计算复现。它只说明给定范围和给定两个分支内没有反例；对任意
\(X,H\) 的全称选择器、对 \(q\) 的统一上界或任何 Erdős--Straus 猜想的逐点结论均未证明。
