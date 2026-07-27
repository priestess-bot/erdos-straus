---
kind: claim
claim_id: weighted-cyclic-complete-repeated-tail-audit
title: 加权循环传输对全部重复尾源的完整有限审计
statement: 对 p<=5000、p=1 mod24，全部既约权重 0<r<s<=50，以及全部严格更小的重复尾源 4/n=1/a+2/b，按循环重排后可完整归约为 b=nk、a=nk/(4k-2)。精确审计 54271557 个候选，得到两个互为方向反转的见证，均来自 p=2161、k=552、r/s=1/49 或 48/49、n=1103。它们的目标均有两条 p 倍分母；排序后恢复同一张 Type II 证书 (m,d)=(47,12)。因此该有限盒中的重复尾命中是直接 Type II 证书的标记重参数化，不提供新的无标记递降边。
claim_status: computationally_reproduced
topics:
- descent
- type-II
- weighted-transport
- repeated-tail
- computation
- finite-audit
- marked-solution
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II certificate reconstruction
- paper: elsholtz_tao2013
  locator: Section 2
  role: Egyptian-fraction equation context
visibility: public
last_checked: '2026-07-25'
---

# 加权循环传输对全部重复尾源的完整有限审计

## 完整参数化

考虑任意严格更小的重复尾源

\[
\frac4n=\frac1a+\frac1b+\frac1b,\qquad 2\le n<p. \tag{1}
\]

循环重排后总可把不同分母放在第一坐标，故不失一般性可用 (1) 的次序。
对既约权重 \(0<r<s\)，加权循环传输的中间目标倒数为

\[
\frac1B
=\frac n{ps}\left(\frac r b+\frac{s-r}b\right)
=\frac n{pb}. \tag{2}
\]

若目标分母 \(B\) 是整数，由 \(\gcd(n,p)=1\) 得 \(n\mid b\)。写

\[
b=nk. \tag{3}
\]

将它代回 (1)，唯一得到

\[
a=\frac{nk}{4k-2}. \tag{4}
\]

所以 \(n\) 必为

\[
n_k=\frac{4k-2}{\gcd(k,4k-2)}
=
\begin{cases}
4k-2,&k\ \text{奇},\\
2k-1,&k\ \text{偶}
\end{cases} \tag{5}
\]

的倍数。反过来 \(n=n_k\) 确实使 (4) 成为整数，故

\[
n_k<p \tag{6}
\]

当且仅当存在某个秩小于 \(p\) 的重复尾源具有该 \(k=b/n\)。这说明只枚举最小源
\(n_k\) 已穷尽这个源形状，而不是人为挑选一个 \(n\)。

把 (3)--(4) 代入加权循环式后，目标三元组为

\[
\left(
\frac{psk}{4rk+s-3r},\
pk,\
\frac{psk}{4(s-r)k-2s+3r}
\right). \tag{7}
\]

因此整性恰为 (7) 的两个显示分母整除 \(psk\)，可用精确整数算术完整审计。

## \(5000\) 内结果

运行

    python3 reproductions/weighted_cyclic_complete_repeated_tail_audit.py \
      --limit 5000 \
      --weight-denominator-bound 50 \
      --output reproductions/weighted-cyclic-complete-repeated-tail-5k-s50-results.json

得到

\[
\begin{array}{c|r}
\text{量} & \text{数目}\\
\hline
\text{核心素数 }p\le5000 & 76\\
\text{既约权重 }0<r<s\le50 & 773\\
\text{完整重复尾候选} & 54{,}271{,}557\\
\text{有向整数提升} & 2\\
\text{不同的无向见证} & 1
\end{array}
\]

两个有向命中互为 \(r/s\leftrightarrow(s-r)/s\) 的坐标反转。其共同数据为

\[
p=2161,\quad \frac rs=\frac1{49},\quad
k=552,\quad n=1103,
\]

\[
\frac4{1103}
=\frac1{276}+\frac1{608856}+\frac1{608856},
\]

\[
\frac4{2161}
=\frac1{25932}+\frac1{1192872}+\frac1{552}. \tag{8}
\]

排序目标分母后，

\[
(552,25932,1192872)=(552,2161\cdot12,2161\cdot552).
\]

令 \(m=4\cdot552-2161=47\)。则

\[
d=47\cdot12-552=12,\qquad
d\mid552^2,\qquad d\equiv-552\pmod {47}. \tag{9}
\]

故 (8) 恢复的是 Type II 证书

\[
(m,d)=(47,12), \tag{10}
\]

而非此前未知的无标记归纳提升。

## 含义

此前固定 \(n=4k-2\) 的最小重复尾分支在同一 \(p\)、权重盒内为空；
\(k=552\) 是偶数，其真正最小源是 \(2k-1=1103\)，所以不在那条较窄分支中。
这显示最小源正规化是必要的，而不能把某个方便的参数截面误作完整源族。

weighted-cyclic-repeated-tail-type-II-rigidity 已把这里的现象提升为全称结论：
只要权重分母 \(s<p\)，重复尾加权循环就必保留两条 \(p\) 倍目标分母，因而落在已有
Type II 证书坐标。该审计为定理提供独立实现核对。尚未排除三项互异源、权重
\(s\ge p\) 的加权命中，或非循环/带偏移传输。
