---
kind: claim
claim_id: type-II-window-descent-hybrid-10m
title: 20 窗口与平方因子外部源递降的千万级混合闭合
statement: 在所有 p<=10^7、p=1 mod24 的 82887 个核心素数中，直接 Type II 移动窗口 j<=20 捕获 82886 个，唯一残余为 p=8803369。该点完整逃过固定因子进程陷阱的全部 3929 个候选未来缺口，但有平方因子外部源严格递降，源分母 n=8768435<p。因此“j<=20 的直接证书或所列严格递降”在该千万级样本覆盖全部核心素数。
claim_status: computationally_reproduced
topics:
- type-II
- moving-window
- descent
- type-I
- fixed-factor-trap
- computation
- proof-program
sources:
- paper: bradford2024
  locator: Propositions 1 and 2
  role: certificate-and-descent-context
visibility: public
last_checked: '2026-07-25'
---

# 20 窗口与平方因子外部源递降的千万级混合闭合

## 审计对象

对每个 \(p\le10^7\)、\(p\equiv1\pmod {24}\)，先检查直接 Type II 移动窗口

\[
m_j=4j-1,\qquad 1\le j\le20. \tag{1}
\]

未命中时，再依次执行：

1. `type-II-fixed-factor-progression-trap` 的完整因子枚举；
2. `quadratic-factor-external-source-descent` 的严格提升搜索。

三者均使用整数整除和精确有理数重建，且递降项要求显式给出源分母、源解和到目标的提升。

## 结果

直接窗口在 82,887 个核心素数中命中 82,886 个，唯一残余为

\[
p=8{,}803{,}369. \tag{2}
\]

对 (2)，固定因子陷阱机制的全部可能未来缺口已被完整穷尽：共有 3,929 个候选，但
没有一个命中。这排除了把该单一机制误作窗口残余的全称解释。

但平方因子外部源给出严格下降：

\[
n=8{,}768{,}435<p,\qquad
k=63,\quad q=251,\quad e=17{,}014{,}725. \tag{3}
\]

对应的显式源解与目标解为

\[
\frac4n=
\frac1{552{,}411{,}405}
+\frac1{2{,}268{,}630}
+\frac1{73{,}654{,}854},
\]

\[
\frac4p=
\frac1{4{,}863{,}081{,}438{,}023{,}445}
+\frac1{2{,}268{,}630}
+\frac1{73{,}654{,}854}. \tag{4}
\]

因此样本中的每个核心素数都满足“(1) 中的直接短证书”或“(3)--(4) 中的严格递降”。

运行

    python3 reproductions/type_ii_hybrid_window_descent_audit.py \
      --limit 10000000 --window 20 \
      --output reproductions/type-ii-hybrid-window20-descent-10m-results.json

可复现完整分类。

## 边界

这是一个有限样本闭合，不能推出 \(J=20\) 为全称窗口界，也不能推出平方因子外部源对
所有未来残余有效。其意义是建立一份无歧义的混合基准：任何推广“短证书或递降”的规则
至少应处理此处直接窗口失败、固定因子陷阱失败而严格递降成功的状态。
