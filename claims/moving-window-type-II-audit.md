---
kind: claim
claim_id: moving-window-type-II-audit
title: 固定 Type II 移动窗口至 5*10^8 的精确审计
statement: 对所有 p<=10^7、p=1 mod24，首分母缺口 m=4j-1 的纯 Type II 移动窗口在 j<=20 时遗漏且仅遗漏 p=8803369，其首个命中为 j=27。窗口 j<=27 覆盖 p<=10^8，但在 p<=2*10^8 恰遗漏 p=153633769；后者首个 Type II 命中为 j=32、m=127、d=2821949。窗口 j<=32 在 p<=5*10^8 的有限范围覆盖全部 3292848 个核心素数。
claim_status: computationally_reproduced
topics:
- type-II
- short-certificate
- moving-window
- computation
- proof-program
sources:
- paper: adaptive_divisor_clouds2026
  locator: "Theorem 5.1, Conjecture 13.1, computational discussion"
  role: moving-window-context
- paper: bradford2024
  locator: "Propositions 2 and 4"
  role: Type-II-certificate-equivalence
visibility: public
last_checked: '2026-07-25'
---

# 固定 Type II 移动窗口至 \(5\cdot10^8\) 的精确审计

## 计算结论

对每个核心素数 \(p=24t+1\)，令

\[
m_j=4j-1,\qquad x_j=\frac{p+m_j}{4}=6t+j.
\]

精确枚举 \(x_j^2\) 的除子，并检查 Type II 条件

\[
d\mid x_j^2,\qquad d\le x_j,\qquad d\equiv-x_j\pmod {m_j},
\]

得到：

\[
\begin{array}{c|c|c|c}
\text{范围} & J & \text{命中核心素数数} & \text{遗漏}\\
\hline
p\le10^7 & 20 & 82{,}886/82{,}887 & 8{,}803{,}369\\
p\le10^7 & 27 & 82{,}887/82{,}887 & \varnothing\\
p\le10^8 & 27 & 719{,}781/719{,}781 & \varnothing\\
p\le2\cdot10^8 & 27 & 1{,}383{,}889/1{,}383{,}890 & 153{,}633{,}769\\
p\le2\cdot10^8 & 32 & 1{,}383{,}890/1{,}383{,}890 & \varnothing\\
p\le5\cdot10^8 & 32 & 3{,}292{,}848/3{,}292{,}848 & \varnothing\\
\end{array}
\]

遗漏素数的首个 Type II 命中为

\[
p=8{,}803{,}369,\qquad j=27,\qquad m=107,\qquad
x=2{,}200{,}869,\qquad d=121.
\]

200M 中 \(J=27\) 的唯一遗漏有首个 Type II 命中

\[
p=153{,}633{,}769,\qquad j=32,\qquad m=127,\qquad
x=38{,}408{,}474,\qquad d=2{,}821{,}949.
\]

结果由 `moving_window.py` 生成；新增机器可读输出为
`moving-window-j27-200m-results.json`、`moving-window-j32-200m-results.json` 与
`moving-window-j32-500m-results.json`。

## 算法与交叉核查

每个候选先由 Type II 除子同余恢复 \((x,y,z)\)，再以精确有理数验证
\(4/p=1/x+1/y+1/z\)。因此这里没有概率筛或浮点近似。小范围单元测试独立检查
窗口 \(J=16\) 在 \(p\le10^4\) 的完整覆盖和记录保持者。

## 不能推出的结论

这个审计否定了 \(J=20\) 和 \(J=27\) 的全称稳定性；\(J=32\) 只是一项截至
\(5\cdot10^8\) 的记录。它既不证明存在某个全局固定 \(J_0\)，也不构造未命中时的
严格递降。因此它不能完成“短证书或递降”引理；它给任何固定窗口饱和证明施加可重复
的下界 \(J_0\ge32\)，并把下一步定位为解释记录缺口为何增长的跨移位结构问题。
