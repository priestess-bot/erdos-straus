---
kind: claim
claim_id: type-II-scaled-first-tail-deflation-audit
title: 缩放首分母双尾递降覆盖三百万范围的一阶残余
statement: 以 p<=3*10^6 的全体核心素数为样本，普通 k=1 双尾递降选择器遗漏 41 个。对这 41 个点，在 1<=k<=2000、3<=m<=20000 的参数盒中，缩放首分母双尾递降全部命中；其中此前最末两点 p=967129、2978089 分别需要 (k,m)=(361,47)、(1081,95)。这是精确有限审计，不能推出固定参数盒覆盖全体素数。
claim_status: computationally_reproduced
topics:
- type-II
- descent
- computation
- factor-selection
- proof-program
sources:
- paper: bradford2024
  locator: Section 2, Type II divisor certificates
  role: certificate-context
visibility: public
last_checked: '2026-07-24'
---

# 缩放首分母双尾递降覆盖三百万范围的一阶残余

## 审计

先运行 `type-II-tail-deflation-selector-audit` 的同一选择器至
$p\le3\cdot10^6$。它在 $26{,}983$ 个核心素数中命中 $26{,}942$ 个，留下
$41$ 个 $k=1$ 残余。

然后对每个残余枚举

\[
1\le k\le2000,\qquad 3\le m\le20000,\qquad m\equiv3\pmod4,
\]

先检查 $km+1\mid kp-1$，仅在通过时运行完整 Type II 除子证书检查。

```bash
python3 reproductions/type_ii_tail_deflation_full_audit.py --limit 3000000 \
  --output reproductions/type-ii-tail-deflation-3m-full-results.json
python3 reproductions/type_ii_scaled_first_tail_deflation_audit.py \
  --output reproductions/type-ii-scaled-first-tail-deflation-3m-results.json
```

输出给出

\[
\#\{\text{输入残余}\}=41,\qquad
\#\{\text{缩放首分母命中}\}=41,\qquad
\#\{\text{未命中}\}=0.
\]

窗口边界压力最大的两点为

\[
\begin{array}{c|c|c|c}
p&k&m&n\\
\hline
967129&361&47&20577\\
2978089&1081&95&31349
\end{array}
\]

每项均以精确整数整除和有理数恒等式复核。

## 解释与边界

这项结果显著改变了残余研究的优先级：一阶 $k=1$ 因子选择器并未暴露稳定的反例族，
其三百万范围残余完全由同一 Type II 证书机制的首分母标记扩张吸收。因而下一步应研究
$km+1\mid kp-1$ 与 Type II 除子残数之间的统一选择，而不是继续增加彼此无关的
固定缺口分支。根据 `type-II-scaled-tail-marked-lift-equivalence`，该结论是短证书
选择证据，不能把所构造的源表示误作从任意源解开始的归纳递降。

参数盒的全覆盖仍只是有限事实。尤其 $k=1081$ 已说明不能把“小 $k$”误读为可证明
的统一常数；未来定理必须允许 $k$ 随 $p$ 变化，或给出不同的结构性上界。
