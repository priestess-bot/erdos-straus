---
kind: claim
claim_id: standard-tail-descent-finite-audit
title: 两条无条件标准大尾递降的有限覆盖审计
statement: 以精确整数算术逐一枚举 p<=10000、p=1 mod24 的全部 143 个核心素数，以及每个 p 的所有 p/2<n<p 偶数标准源和 3|n 标准源。偶数大尾分支命中 119 个，三倍数大尾分支命中 75 个，二者并集命中 126 个；共同未命中恰为 73,97,193,577,601,1153,1801,1873,4801,5209,5881,6121,7393,7993,8161,8689,9001。这是有限实验，不能推出全称覆盖或反例。
claim_status: computationally_reproduced
topics:
- descent
- computation
- certificate
- finite-audit
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: "Section 2"
  role: standard-source-context
visibility: public
last_checked: '2026-07-24'
---

# 两条无条件标准大尾递降的有限覆盖审计

## 范围与判据

对每个核心素数 \(p\le10^4\)，精确枚举两组源分母：

\[
\frac p2<n<p,\quad 2\mid n,
\]

并应用 `even-standard-two-tail-descent` 的完整因子判据；以及

\[
\frac p2<n<p,\quad 3\mid n,
\]

并应用 `three-divisible-standard-two-tail-descent` 的完整因子判据。固定 \((p,n)\)
时，这两张卡片各自穷尽相应标准源中“保留一个大尾、重组另外两项”的所有提升。

实现是 `standard_tail_descent_audit`，使用最小素因子表分解每个候选尾项的平方因子，
并用 `fractions.Fraction` 在每个成功见证处进行恒等式核验。

## 结果

\[
\begin{array}{c|r}
\text{量} & \text{数目}\\
\hline
\text{核心素数 }p\le10^4 & 143\\
\text{偶数标准大尾命中} & 119\\
\text{三倍数标准大尾命中} & 75\\
\text{至少一条命中} & 126
\end{array}
\]

共同未命中的核心素数恰为

\[
73,97,193,577,601,1153,1801,1873,4801,5209,5881,6121,
7393,7993,8161,8689,9001. \tag{1}
\]

所以这两条“无条件源”的大尾递降虽在该小范围覆盖约 \(88\%\)，但已经有具体共同
未命中点。特别地，不能把它们提升为一个对所有核心素数有效的选择器；例如 \(p=5209\)
需要非标准偶数分裂 `even-split-source-descent` 才能得到本库记录的递降边。
`standard-tail-type-I-coordinate-equivalence` 还说明，这里的“命中”精确等价于在指定
第二分母窗口找到 Type I 证书；所以该审计衡量的是一个因子搜索坐标的覆盖率，不是独立于
短证书的归纳成功率。

## 可复现边界

测试 `test_standard_tail_descent_finite_audit` 在 \(p\le5000\) 的独立子范围核对
完整计数及共同未命中列表。更大的 \(10^4\) 结果来自同一精确枚举器。这些数据只说明
所列两族在一个有限盒内的行为；它既不证明它们在无穷多素数上失败，也不对任何
未命中 \(p\) 否定其它 Type I/II 证书或非标准递降。
