---
kind: claim
claim_id: type-II-fixed-factor-progression-trap
title: 固定因子冻结余因子的 Type II 进程陷阱引理
statement: 令 p=p0+16Qk，其中 p0=1 mod24，Q 是一个移动窗口模数，3<=m<=p0-2 且 m=3 mod4 是未来缺口，x0=(p0+m)/4，E=gcd(4Q,x0)。若 m|(4Q/E)，且存在 a|E 使 a(x0/E)=-x0 modm，则对进程中的每个核心素数 p，令 x=(p+m)/4、N=x/E、d=aN，便有 d|x、d<=x 且 d=-x modm；故 (m,d) 是直接 Type II 证书。
claim_status: established
topics:
- type-II
- arithmetic-progression
- moving-window
- certificate
- factorization
- state-closure
- proof-program
sources:
- paper: bradford2024
  locator: Proposition 2
  role: Type-II-divisor-criterion
visibility: public
last_checked: '2026-07-25'
---

# 固定因子冻结余因子的 Type II 进程陷阱引理

## 定理

令 \(p_0\equiv1\pmod {24}\)，令 \(Q\) 为正整数，取

\[
p=p_0+16Qk,\qquad
3\le m\le p_0-2,\qquad
m\equiv3\pmod4,\qquad
x=\frac{p+m}{4}. \tag{1}
\]

记

\[
x_0=\frac{p_0+m}{4},\qquad
E=\gcd(4Q,x_0). \tag{2}
\]

假设

\[
m\mid\frac{4Q}{E}, \tag{3}
\]

且存在 \(a\mid E\) 使

\[
a\frac{x_0}{E}\equiv-x_0\pmod m. \tag{4}
\]

则对任意该进程中的核心素数 \(p\)，令

\[
N=\frac{x}{E},\qquad d=aN, \tag{5}
\]

有 \((m,d)\) 为 \(p\) 的直接 Type II 除子证书。

## 证明

由 (1)--(2)，

\[
x=4Qk+x_0=E\left(\frac{4Q}{E}k+\frac{x_0}{E}\right),
\]

所以 \(N\) 是整数。由 (3)，

\[
N\equiv\frac{x_0}{E}\pmod m. \tag{6}
\]

将 (6) 代入 (4)，得到

\[
d=aN\equiv-x_0\equiv-x\pmod m, \tag{7}
\]

其中最后一步再次由 (3) 给出。又 \(a\mid E\)，故

\[
d=aN\mid EN=x,\qquad d\le x. \tag{8}
\]

于是 \(d\mid x^2\)、\(d\le x\) 且 (7) 为 Type II 目标同余。若 \(p\) 是核心素数，
自然缺口范围成立时 Bradford 判据恢复 Type II 分解，证毕。

## 作用与算法化

这条引理把一个窗口状态的未来闭合缩为有限算术：

1. 计算 \(E=\gcd(4Q,x_0)\)；
2. 检查 (3)；
3. 枚举 \(E\) 的除子，检查 (4)。

`type_ii_progression_trap.py` 正是这个完整枚举器。对记录共同失败点
\(p_0=153633769\)、窗口 \(J=31\)，它在 \(J<j\le131\) 中唯一找到

\[
j=52,\quad m=207,\quad E=9682,\quad a=47,
\]

即 `type-II-gap-207-progression-certificate`。在另一种子
\(p_0=33011449,J=20\) 中，它找到

\[
j=36,\quad m=143,\quad E=426,\quad a=3.
\]

还可作**完整**而非有界的失败核查。由 (3)，任何这类陷阱缺口必整除 \(4Q\)，故只要
枚举 \(4Q\) 的全部因子便穷尽该机制。对 \(p_0=8803369,J=20\)，共有 3,929 个
满足自然范围及 \(m\equiv3\pmod4\) 的候选未来缺口，全部失败；结果在
`type-ii-progression-trap-p8803369-j20-complete-results.json`。这说明判据是严格的
充分机制，而不是对任意状态都自动成立的重述。

## 边界

引理只捕获满足 (3)--(4) 的单一固定因子状态。失败时，仍可能有其它 Type II 证书、
更复杂的多因子残数构造或可提升递降。它不提供对所有核心素数的统一 \(Q,m,a\) 选择；
后续目标是证明每个持久残余状态终会触发这类陷阱，或导出另一种严格递降。

若种子 \(p_0\) 是核心素数且 \(\gcd(p_0,16Q)=1\)，则每个陷阱进程本身由 Dirichlet
定理含有无穷多个核心素数；因而命中不是单个数值样本，而是一条无条件无限证书族。
