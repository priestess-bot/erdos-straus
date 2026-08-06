---
kind: claim
claim_id: type-II-p-plus-12-36-divisor-terminal-fan
title: p+12 / p+36 因子给出的 Type II 终端扇
statement: 设 p=24h+1 为核心素数，d 属于 {3,9}。对任意 k>=1，令 m=12k-1、x=(p+m)/4=6h+3k。则 d|x^2 且 d<=x，并且该 (m,d) 是 Type II 证书当且仅当 m|p+4d（等价于 m|x+d）。因此 p+12 或 p+36 的每个 11 (mod 12) 因子都给出一个显式 Type II terminal。对每个固定的 (k,d)，相应核心素数构成一个互素的 Dirichlet 算术进程，故产生无穷多个正例；但任意固定有限组 (k,d) 模板均遗漏无穷多个核心素数，且这一遗漏可分别限制在 h 的每个模 3 类中。该扇不构成全称覆盖或递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - short-certificate-equivalence
  - type-II-shared-gap-23-automatic-fan
  - type-I-g-anchor-complement-seed-n-minus-two-terminal-sieves
  - type-II-factor-square-tail-descent-family
topics:
  - type-II
  - terminal-first
  - divisor-criterion
  - congruence-certificate
  - dirichlet-progressions
  - finite-fan-boundary
  - proof-program
sources:
  - claim: short-certificate-equivalence
    role: Type-II-criterion-and-reconstruction
  - claim: type-II-shared-gap-23-automatic-fan
    role: k-equals-2-d-equals-3-special-case
  - claim: type-I-g-anchor-complement-seed-n-minus-two-terminal-sieves
    role: seed-derived-k-equals-1-d-equals-3-and-k-equals-2-d-equals-9-special-cases
visibility: public
last_checked: '2026-08-06'
---

# \(p+12/p+36\) 因子给出的 Type II 终端扇

本卡给出一张只作用于原始核心素数的 Type II terminal fan。它不使用任何
G-anchor source receipt，也不把分母恒等式解释为递降。

## 1. 通用 \(m=12k-1\) 终端

令

\[
p=24h+1
\]

为核心素数，取

\[
k\ge1,
\qquad
m=12k-1,
\qquad
d\in\{3,9\},
\qquad
x=\frac{p+m}{4}=6h+3k.
\tag{1}
\]

于是 \(m\equiv11\pmod {12}\)，特别地 \(m\equiv3\pmod4\) 且
\((m,6)=1\)。由于 \(3\mid x\)，对两个允许的 \(d\) 都有

\[
d\mid x^2.
\tag{2}
\]

核心素数最小为 \(73\)，故 \(x\ge21\)，也有 \(d\le x\)。Type II 的余下
整除条件恰好可改写为

\[
\begin{aligned}
m\mid x+d
&\Longleftrightarrow m\mid4(x+d)\\
&\Longleftrightarrow m\mid p+4d.
\end{aligned}
\tag{3}
\]

第二个等价使用 \(4x=p+m\)，第一个使用 \((4,m)=1\)。因此，只要

\[
\boxed{m=12k-1\mid p+4d,}\tag{4}
\]

就得到 Type II 证书。其分母可直接恢复为

\[
y=\frac{p(x+d)}m,
\qquad
z=\frac{p x(x+d)}{md},
\tag{5}
\]

并满足

\[
\frac4p
=\frac1x+\frac1y+\frac1z.
\tag{6}
\]

这里 \((m,d)=1\)；结合 (2)、(3)，式 (5) 的两个分母均为整数。这正是
`short-certificate-equivalence` 的 Type II 正规形在 \(d=3,9\) 上的专门化。

## 2. \(p+12\) 与 \(p+36\) 的等价因子判据

分别取 \(d=3\) 与 \(d=9\)，(4) 成为

\[
\begin{array}{c|c|c}
d&m\text{ 的条件}&\text{给出的终端}\\
\hline
3&m\mid p+12&x=(p+m)/4\\
9&m\mid p+36&x=(p+m)/4
\end{array}
\tag{7}
\]

其中总要求 \(m\equiv11\pmod {12}\)。反过来，若 \(m\) 是 \(p+4d\) 的任一
此类因子，写 \(m=12k-1\) 即回到第 1 节。故对每个固定 \(d\)，有精确等价：

\[
\boxed{
\exists k\ge1:\ 12k-1\mid p+4d
\quad\Longleftrightarrow\quad
p+4d\ \text{有一个}\ 11\pmod {12}\ \text{因子}.
}
\tag{8}
\]

该因子自动落在标准 gap 范围。实际上 \(p+4d\equiv1\pmod {12}\)，所以一个
\(11\pmod {12}\) 因子不可能等于 \(p+4d\) 本身；其余因子为大于一的奇数，因而

\[
m\le\frac{p+36}{3}\le p-2.
\tag{9}
\]

最后一个不等式对全部核心素数成立。

这也有一个完全因子化的表述。令 \(N\equiv1\pmod {12}\) 为正奇数且
\((N,6)=1\)。则 \(N\) 有 \(11\pmod {12}\) 因子，当且仅当其素因子中出现

\[
q\equiv11\pmod {12},
\qquad\text{或同时出现}\qquad
q_5\equiv5\pmod {12},\quad q_7\equiv7\pmod {12}.
\tag{10}
\]

这是单位群 \((\mathbb Z/12\mathbb Z)^\times\) 的四元群乘法的直接结果：若没有
\(11\) 类且不同时有 \(5\)、\(7\) 类，任意因子只能落在 \(1\)、\(5\) 或
\(7\) 类。将 \(N\) 分别取为 \(p+12\)、\(p+36\)，(10) 是 (8) 的等价
素因子筛。

例如 \(p=193\) 时

\[
p+12=205=5\cdot41,
\qquad
p+36=229.
\tag{11}
\]

两者均没有 \(11\pmod {12}\) 因子，故该 \(p\) 不在本 terminal fan 中；这只说明
本扇未命中，不否定它的其它 Type I/II 证书。

## 3. 每条固定射线的无穷正例

写 \(d=3\delta\)，其中 \(\delta\in\{1,3\}\)。由 (3) 或直接由 \(m\mid x+d\)，
固定 \((k,d)\) 的命中条件可写成

\[
h\equiv r_{k,d}
\equiv-2k(3k+d)
\equiv-6k(k+\delta)
\equiv-\frac{k+\delta}{2}\pmod {12k-1}.
\tag{12}
\]

这里最后的 \(1/2\) 是模 \(12k-1\) 的逆元；使用了
\(6^{-1}\equiv2k\pmod {12k-1}\)。等价地，素数本身满足互素的 CRT 条件

\[
p\equiv1\pmod {24},
\qquad
p\equiv-4d\pmod {12k-1}.
\tag{13}
\]

右边两个剩余分别与 \(24\)、\(12k-1\) 互素。因此 Dirichlet 算术进程素数定理
给出每一条固定 \((k,d)\) 射线上的无穷多个核心素数，且每个点都由 (5) 给出显式
Type II terminal。

这一无穷性还可分别限制到 \(h\) 的任一模 \(3\) 类。因为
\((12k-1,3)=1\)，把 (12) 与任意预定的 \(h\equiv\epsilon\pmod3\) 合并，所得
\(p\) 是模 \(72(12k-1)\) 的一个互素剩余类。于是每条射线在两个
\(c=3\) 子类和 \(c=9\) 子类中都各有无穷多正例。

两个已记录特例正好嵌入此扇：

\[
\begin{array}{c|c|c|c|c}
k&d&m&h\pmod m&\text{一组分母}\\
\hline
1&3&11&10&(63,1446,30366)\quad(p=241)\\
2&9&23&9&(198,6921,152262)\quad(p=769)
\end{array}
\tag{14}
\]

前一行是 G-anchor 补余 \((d,n)=(3,13)\) 所提示的 gap-11 子族，后一行是
\((d,n)=(9,25)\) 所提示的 gap-23 子族。这里的推导不再附加原先为连接相应
seed 而出现的 \(h\pmod3\) 限制。\(k=2,d=3\) 则是
`type-II-shared-gap-23-automatic-fan` 中 \(d=3\) 的自动共享特例。

## 4. 固定有限扇不能全覆盖

设 \(\mathcal F\) 是任意非空有限集，元素为允许的模板 \((k,d)\)。令

\[
L=\operatorname{lcm}_{(k,d)\in\mathcal F}(12k-1).
\tag{15}
\]

式 (12) 中每个 \(r_{k,d}\) 都非零模 \(12k-1\)。事实上

\[
r_{k,d}\equiv-6k(k+\delta),
\tag{16}
\]

而 \((6k,12k-1)=1\)、\(0<k+\delta<12k-1\)。因此取

\[
h\equiv0\pmod L
\tag{17}
\]

就同时避开 \(\mathcal F\) 中的全部命中剩余。又

\[
p=24h+1\equiv1\pmod {24L}
\tag{18}
\]

是一个互素算术进程，Dirichlet 定理给出无穷多个这样的核心素数。它们均未由
\(\mathcal F\) 的任何固定 \((k,d)\) terminal 处理。

同样可把 (17) 与任意 \(h\equiv\epsilon\pmod3\) 合并：\((L,3)=1\)，相应
\(p\) 仍是模 \(72L\) 的互素剩余类。故有限扇的遗漏不仅无穷，而且在每个
\(h\pmod3\) 分支内都无穷。

这个边界只排除**固定有限**的 \((k,d)\) 菜单成为全称选择器；它不排除随 \(p\)
增长的因子搜索、其它 \(d\)、其它 Type I/II 模板，或任何保持标签的严格递降机制。

## 5. 研究接口

本扇应作为 source/path 机制之前的 terminal-first 检查：只要 \(p+12\) 或
\(p+36\) 出现相应的 \(11\pmod {12}\) 因子，即可输出 (5) 的可核短证书。它与
`type-II-factor-square-tail-descent-family` 的关系仅是共享 Type II 正规形：后者在
额外的 \(m+1\mid p-1\) 条件下能给出递降，而本卡一般只有原始 \(p\) 的 terminal，
不能据此声称递降或覆盖全部核心素数。
