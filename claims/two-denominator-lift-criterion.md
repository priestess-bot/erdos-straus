---
kind: claim
claim_id: two-denominator-lift-criterion
title: 保留两个源分母的一项替换提升判据
statement: 设 2<=n<p 且 4/n=1/a+1/b+1/c。存在正整数 a' 使 4/p=1/a'+1/b+1/c，当且仅当 D=np-4(p-n)a 为正且 D 整除 npa；此时 a'=npa/D。等价地，置 N=np、C=4(p-n)，则 D(N+Ca')=N^2。
claim_status: established
topics:
- descent
- egyptian-fractions
- divisors
- solution-lift
- proof-program
sources:
- paper: bradford2024
  locator: "Propositions 1--4"
  role: divisor-factorization-context
visibility: public
last_checked: '2026-07-23'
---

# 保留两个源分母的一项替换提升判据

## 定理

设 \(2\le n<p\)，并给定源解

\[
\frac4n=\frac1a+\frac1b+\frac1c.
\]

令

\[
N=np,\qquad C=4(p-n),\qquad D=N-Ca.
\]

存在正整数 \(a'\)，使

\[
\frac4p=\frac1{a'}+\frac1b+\frac1c, \tag{1}
\]

当且仅当

\[
D>0,\qquad D\mid Na. \tag{2}
\]

此时替换分母唯一，且为

\[
a'=\frac{Na}{D}. \tag{3}
\]

它还等价于如下因子形式：

\[
D(N+Ca')=N^2. \tag{4}
\]

因而可通过枚举 \(N^2\) 的因子 \(D\) 检验候选：必须有

\[
0<D<N,\qquad D\equiv N\pmod C,\qquad
C\mid \frac{N^2}{D}-N. \tag{5}
\]

由 (5) 恢复 \(a=(N-D)/C\)、\(a'=(N^2/D-N)/C\) 后，(1) 即成立。

## 证明

由源式和 (1) 相减，

\[
\frac1{a'}=\frac1a+\frac4p-\frac4n
=\frac1a-\frac{4(p-n)}{np}
=\frac{N-Ca}{Na}=\frac D{Na}. \tag{6}
\]

因此存在正整数 \(a'\) 当且仅当 \(D>0\) 且 \(D\mid Na\)，并立即得到 (3)。
再将 \(Ca=N-D\) 代入 \(a'D=Na\)，得到

\[
Ca'D=N(N-D),
\]

即 (4)。反过来，(4) 和正性给出 (3)，再代入 (6) 即恢复 (1)。式 (5) 只是 (4)
按 \(D\mid N^2\) 反解 \(a,a'\) 的整数性条件。

## 正例与 m=3 的边界

该判据确实能给出严格降阶的局部提升。取

\[
n=33,\qquad p=73,\qquad a=15,
\]

则 \(N=2409\)、\(C=160\)、\(D=9\)，所以 \(a'=4015\)。具体地，

\[
\frac4{33}=\frac1{15}+\frac1{22}+\frac1{110}
\quad\Longrightarrow\quad
\frac4{73}=\frac1{4015}+\frac1{22}+\frac1{110}. \tag{7}
\]

这说明不能把 gap-three-two-denominator-lift-obstruction 误读为所有源缺口的障碍。
对该卡片所研究的特殊自然源 \(n=(p+3)/4\)，(2) 对核心素数的任何正 \(a\) 都不可能
成立；但其它 \(n=(p+m)/4\) 可以有 (7) 这样的提升。

## 对目标引理的边界

这是真正读取源解坐标 \(a\) 的提升公式，且 \(n<p\) 保证了严格降阶。它定义了一个
目标依赖的标记源解集：只保留满足 (2) 的三元组；在该集合上，(3) 是全域提升。
因此不必要求 \(\operatorname{Sol}(n)\) 的每个输入都可提升。严格归纳只需递归地保证
这个标记集非空，形式化见 marked-solution-descent-closure。

不过这仍不构成目标引理：必须为每个没有预定短证书的核心素数选择一个较小 \(n\)，并构造
可闭合的标记状态。例 (7) 只证明一个局部成功实例；它不提供这种全覆盖选择器。

这一点甚至在正例本身就可见。精确枚举 \(4/33\) 的 29 个按升序三元组后，只有

\[
(15,20,220),\qquad (15,22,110)
\]

含有可替换坐标 \(15\)；其余 27 个三元组的三个坐标逐一代入 (2) 都失败。因此，
“从输入三元组中保留两个分母”这一个模板不能定义 \(33\) 到 \(73\) 的
\(\operatorname{Sol}(33)\) 全域提升映射，即使它确实有 (7) 的局部成功例。
但这不妨碍它作为一个**带标记**递降边：上述两个源解已经足以证明相应标记集非空。
这个有限反例不排除同时重组更多坐标的映射。
