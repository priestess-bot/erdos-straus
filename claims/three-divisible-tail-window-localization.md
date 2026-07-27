---
kind: claim
claim_id: three-divisible-tail-window-localization
title: 三倍数标准大尾提升的有效窗口定位
statement: 令 p=1 mod24 为素数、0<n<p 且 3|n；从标准源解保留一个 2n 并重组另两项。n<=p/8 时目标余项非正；p/8<n<p/4 时成功恰等价于目标 p 在缺口 8n-p 的直接证书；p/4<n<p/2 时其因子条件、输出和命中性与偶数标准源 2n 的大尾提升完全相同。因此该三倍数分支相对于直接证书与偶数大尾的唯一非冗余窗口是 p/2<n<p。
claim_status: established
topics:
- descent
- certificate
- redundancy
- three-divisible-source
- even-source
- solution-lift
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: divisor-certificate-and-lift-context
visibility: public
last_checked: '2026-07-24'
---

# 三倍数标准大尾提升的有效窗口定位

## 定理

设 \(p\equiv1\pmod {24}\) 为素数，\(0<n<p\) 且 \(3\mid n\)。考虑从标准源解

\[
\frac4n=\frac1{n/3}+\frac1{2n}+\frac1{2n} \tag{1}
\]

保留一个 \(2n\)，并把其余两项重组为目标解

\[
\frac4p=\frac1{2n}+\frac1u+\frac1v. \tag{2}
\]

令

\[
R=8n-p,\qquad S=2np. \tag{3}
\]

则这条候选提升的参数窗口有如下完全分类。

1. 当 \(n\le p/8\) 时，(2) 不可能成立。
2. 当 \(p/8<n<p/4\) 时，(2) 的存在等价于 \(p\) 在缺口
   \[
   m=8n-p \tag{4}
   \]
   处有一张自然范围的 Type I 或 Type II 除子证书；这不是独立递降。
3. 当 \(p/4<n<p/2\) 时，(2) 的因子判据、所有 \((u,v)\) 输出及其证书命中性，
   与从偶数标准源分母 \(N=2n\) 出发的
   `even-standard-two-tail-descent` 完全相同。

因此，除去直接证书与偶数大尾已经覆盖的窗口后，三倍数标准大尾的唯一非冗余区间是

\[
\frac p2<n<p. \tag{5}
\]

这正是 `three-divisible-standard-two-tail-descent` 采用的范围。

## 证明

从 (2) 减去保留项，得到

\[
\frac1u+\frac1v=\frac4p-\frac1{2n}
=\frac{8n-p}{2np}=\frac RS. \tag{6}
\]

若 \(n\le p/8\)，右侧不正，故没有正整数 \(u,v\)。以下设 \(n>p/8\)。
此时 \(R>0\)，并且

\[
\gcd(R,S)=\gcd(8n-p,2np)=1, \tag{7}
\]

因为 \(R\) 为奇数，且
\(\gcd(R,n)=\gcd(p,n)=1\)、\(\gcd(R,p)=\gcd(8n,p)=1\)；其中
\(p\nmid n\) 来自 \(0<n<p\)。所以一分母提升的因子形式为

\[
e\mid S^2,\qquad e\le S,\qquad R\mid S+e, \tag{8}
\]

并恢复

\[
u=\frac{S+e}{R},\qquad
v=\frac{S+S^2/e}{R}. \tag{9}
\]

若 \(p/8<n<p/4\)，保留分母 \(c=2n\) 落在 \(p/4<c<p/2\)。由
`middle-coordinate-lift-certificate-equivalence`，(2) 等价于首分母 \(c\) 的直接
除子证书；其缺口正是 \(4c-p=8n-p\)，即 (4)。

若 \(p/4<n<p/2\)，令 \(N=2n\)。则 \(N\) 为偶数且

\[
\frac p2<N<p,\qquad
4N-p=8n-p=R,\qquad
Np=2np=S. \tag{10}
\]

偶数标准源

\[
\frac4N=\frac1{N/2}+\frac1N+\frac1N
=\frac1n+\frac1{2n}+\frac1{2n} \tag{11}
\]

保留一个 \(N=2n\) 的 two-tail 提升，正好使用同一方程 (6)、同一因子条件 (8)
与同一恢复式 (9)。所以两条分支对每个因子 \(e\) 给出同一个目标三元组
\((2n,u,v)\)，并具有完全相同的自然证书命中性。这证明第三项。

剩余的 \(p/2<n<p\) 区间中 \(2n>p\)，不能把 \(2n\) 作为较小的偶数源分母；
同时它不在中间分母区间。因此上述两种化简都不适用，留下 (5) 的非冗余三倍数分支。

## 含义

有限扫描中把三倍数源窗口从 \(p/2<n<p\) 机械地下探，可能提高该单一标签的命中数，
却不会增加“偶数大尾或三倍数大尾”的并集覆盖：新增部分已逐因子等同于偶数源
\(N=2n\)。这避免在标记状态图中把同一因子选择器误记为两条独立的递降机制。

该定位并未证明 (5) 内总有因子 \(e\) 满足 (8)，因此也不提供目标引理所需的全称选择器。
