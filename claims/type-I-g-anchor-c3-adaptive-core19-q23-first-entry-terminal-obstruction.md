---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-q23-first-entry-terminal-obstruction
title: c=3 core-19 的 q=23 首标签 C=19 入口与全分支 terminal 障碍
statement: 在 c=3 chart p=24h+1、R=104h-9 中，universal p-edge 后若首个 ordered raw 标签为 23，则 h=20 (mod 23)，并由 (m,d)=(23,12) 给出直接 Type II terminal。因此任何以 q=23 开始的后续 raw topology 都不能成为 selector edge。另一方面，h=8 (mod 19)、h=20 (mod 23) 时存在与既有三段 q=5 grammar 不同的两段 actual C=19 raw language：若 p=9313+10488v 为素数且 gcd(Q,KR)=1，则 23;Fac(Q) 到达 (19,R-19,1)，其中 h=388+437v、Q=2031+2288v。该族的 exact gcd gate 是 v 不等于 0 (mod 3)、3 (mod 5)、5 (mod 19)，但整个族仍被上述 q=23 terminal-first 规则截断。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-ambient19-terminal-screen
  - type-I-g-anchor-c3-adaptive-divisor-factor-block-normal-form
topics:
  - type-I
  - type-II
  - c3
  - core19
  - raw-source
  - factor-block
  - terminal-first
  - terminal-obstruction
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_q23_first_entry_terminal_obstruction.py
    role: q=23 raw replay and terminal arithmetic
visibility: public
last_checked: '2026-08-07'
---

# q=23 首标签的 C=19 入口障碍

本卡排除一个看似很短的 `C=19` raw 入口。它同时给出该入口的 exact
factor-block language，所以结论不是由失败搜索得出。

## 1. 首标签已经强制 terminal

固定 c=3 chart

\[
p=24h+1,\qquad R=104h-9.
\tag{1}
\]

universal \(p\)-edge 后的 canonical node 为 \((1,R-1,1)\)。若第一条 ordered
raw edge 的标签为 \(23\)，则

\[
23\mid R-1=104h-10.
\]

由于 \(104\equiv12\pmod {23}\)，这等价于

\[
h\equiv20\pmod {23}.
\tag{2}
\]

令

\[
m=23,\qquad d=12,\qquad x=\frac{p+m}{4}=6(h+1).
\tag{3}
\]

当 (2) 成立时，\(12\mid x^2\)，并且

\[
x+d=6(h+3)\equiv0\pmod {23}.
\tag{4}
\]

对正的 core parameter 有 \(d\le x\)。因此 Type II factor-pair construction 的
完整整除条件成立，给出直接 terminal。这里的 terminal 只由第一条 \(23\)-edge
的必要条件决定，与随后如何分解或到达哪个 raw leaf 无关。

**q=23 首标签障碍。** 每个以 \(23\) 为首标签的 c=3 raw branch 都必须在
terminal-first 分派处停止；它不可以登记为 selector edge 或拿来支付后续容量。

## 2. 一个不同的两段 C=19 raw language

再施加 core-19 条件 \(h\equiv8\pmod {19}\)。与 (2) 联立得到

\[
h=388+437v,
\tag{5}
\]

从而

\[
\begin{aligned}
p&=9313+10488v, & R&=40343+45448v,\\
b&=\frac{R-1}{23}=1754+1976v,
&Q&=\frac{R-b}{19}=2031+2288v.
\end{aligned}
\tag{6}
\]

若 \(p\) 为素数且

\[
\gcd(Q,KR)=1,
\tag{7}
\]

则从 \((1,R-1,1)\) 执行

\[
(1,23);\quad (1,\operatorname{Fac}(Q))
\tag{8}
\]

便先到 \((b,R-b,1)\)，再到 \((19,R-19,1)\)。第一枚 \(Q\) 的素因子选右侧；
之后 ordered raw step 将被除坐标写到左侧，故余下因子都选左侧。式

\[
R-1=23b,\qquad R-b=19Q
\tag{9}
\]

给出 endpoint。条件 (7) 使每个 \(Q\)-factor 在 \(K\) 中的高度为零且为
\(R\)-unit；而 \(23\nmid K\)、\(R\equiv1\pmod {23}\)。因此每一步都有
strict capacity、unit condition 和 \(\gcd\)-reduction \(=1\)。

这个 gcd 条件可精确化为

\[
\boxed{
\gcd(Q,KR)=1
\Longleftrightarrow
v\not\equiv0\pmod3,\quad
v\not\equiv3\pmod5,\quad
v\not\equiv5\pmod{19}.}
\tag{10}
\]

证明只需比较 (6) 的线性因子。\(Q\) 与 \(26h+1\) 的公共素因子只可能来自
\(3,5,19\)，对应的根依次为 \(0,3,5\)；与 \(p-3\) 的公共素因子只可能为
\(19\)，而 \(Q\) 与 \(R\) 无公共素因子。其余 resultant 因子在相应线性
因子上恒为 unit。

## 3. 控制点与边界

取 \(v=1\)，有

\[
h=825,\quad p=19801,\quad R=85791,\quad Q=7\cdot617.
\]

所以

\[
(1,23),(1,7),(0,617)
\]

是一个 actual primitive word，并到达 \((19,85772,1)\)。这个控制点也有
\((m,d)=(7,4)\) 的直接 Type II terminal；它仅用于复现 raw grammar，绝不作为
nonterminal 反例。

更强的 (3)--(4) 已经说明，无论其他参数点的 terminal screen 如何表现，整个
q=23-first language 都被 \((23,12)\) 截断。下一步应避开首标签 \(23\)，而不是扩大
这个分支的参数扫描。
