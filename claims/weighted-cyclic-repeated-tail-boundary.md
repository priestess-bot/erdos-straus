---
kind: claim
claim_id: weighted-cyclic-repeated-tail-boundary
title: 加权循环传输的最小非标准重复尾边界
statement: 在所有 p<=5000、p=1 mod24 的 76 个核心素数上，枚举全部 n=4k-2<p 的显式非标准源解 4/n=1/k+2/(nk)，以及全部既约循环权重 0<r<s<=50，共 36181038 个候选；没有一个加权循环传输同时产生三个整数目标分母。这个有限空结果越过了两条标准源障碍，但不排除更大权重、三项互异源或非循环传输。
claim_status: computationally_reproduced
topics:
- descent
- solution-lift
- weighted-transport
- computation
- finite-audit
- nonstandard-source
- proof-program
sources:
- paper: elsholtz_tao2013
  locator: Section 2
  role: Egyptian-fraction equation context
visibility: public
last_checked: '2026-07-25'
---

# 加权循环传输的最小非标准重复尾边界

## 显式源族

对每个 \(k\ge1\)，令

\[
n=4k-2,\qquad
\frac4n=\frac1k+\frac1{nk}+\frac1{nk}. \tag{1}
\]

它是一个显式、非标准的源解：除 \(k=1\) 的退化端点外，首分母 \(k\) 既不是
\(n/2\)，也不是 \(n/3\)。因此它越过了
cyclic-reciprocal-transport-obstruction 所排除的两条无条件标准源。

对既约权重 \(0<r<s\)，将该三元组代入加权循环式

\[
\begin{aligned}
\frac1A&=\frac n{ps}\left(\frac r a+\frac{s-r}b\right),\\
\frac1B&=\frac n{ps}\left(\frac r b+\frac{s-r}c\right),\\
\frac1C&=\frac n{ps}\left(\frac r c+\frac{s-r}a\right), \tag{2}
\end{aligned}
\]

其中 \((a,b,c)=(k,nk,nk)\)。三个目标分母可直接化简为

\[
A=\frac{psk}{4rk+s-3r},\qquad
B=pk,\qquad
C=\frac{psk}{4(s-r)k-2s+3r}. \tag{3}
\]

所以 (2) 的整性恰等价于 (3) 中两个显示分母整除 \(psk\)。这把该源族的搜索
缩成纯整数整除，不需要枚举一般源解。

## 有限审计

运行

    python3 reproductions/weighted_cyclic_repeated_tail_audit.py \
      --limit 5000 \
      --weight-denominator-bound 50 \
      --output reproductions/weighted-cyclic-repeated-tail-5k-s50-results.json

以精确整数整除检查得到

\[
\begin{array}{c|r}
\text{量} & \text{数目}\\
\hline
\text{核心素数 }p\le5000 & 76\\
\text{既约权重 }0<r<s\le50 & 773\\
\text{候选 }(p,r,s,k) & 36{,}181{,}038\\
\text{整数加权循环提升} & 0
\end{array}
\]

每个可能命中都会以精确有理数重建源、目标恒等式；本次没有命中。
测试中的 \(p=31,r/s=1/2,k=8\) 正例会重建

\[
\frac4{30}=\frac18+\frac1{240}+\frac1{240}
\longmapsto
\frac4{31}=\frac1{16}+\frac1{248}+\frac1{16},
\]

从而验证审计器不会把非核心的真实命中误作失败。

## 解释与边界

这个结果首次同时避开了“对称循环对所有源的核心障碍”之外的非均匀权重，
以及两条无条件标准源。它仍只是一个有限参数盒：

1. \(s>50\) 的权重未被排除；
2. 源解 \(4/n=1/a+1/b+1/c\) 的三个分母可以彼此不同；
3. 加入偏移的倒数传输、非循环矩阵和因子依赖映射未被检查。

因此下一条有信息量的正向路线，必须给三项互异的非标准源解提供可递归的因子标记，
或证明更大矩阵族的整数性选择器；不能把此空结果夸大为加权循环提升的全称反例。
