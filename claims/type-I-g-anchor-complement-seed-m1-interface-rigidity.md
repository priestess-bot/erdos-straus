---
kind: claim
claim_id: type-I-g-anchor-complement-seed-m1-interface-rigidity
title: G-anchor 补余 seed 的 m=1 raw 词互反性与 source-adapter 刚性
statement: 对任一 determinant seed pR+1=4Mx、R=4M-n、x=p-d，任何从 m=1 canonical anchor {1,R-1} 到 {x,R-x} 的 raw 词，其素数标签乘积必满足 Theta=+/-n (mod R)。在 full-Q 的 c=3 补余族中，seed 只有唯一直接 m=1 前驱，并且必经一个 t=4,2,1 的 2-adic even-tail 链；链上未标记 physical determinant 行完全相同。在 c=9 补余族中，seed 在整个 m=1 raw 图中没有入边。对于 c=3，任何把旧 universal p-source 映到 target universal p-source 且 intertwine 其唯一 q=p raw 边的映射，都被端点唯一性强制送旧 anchor 到 target canonical anchor，不能送到 even-tail seed。故 old G source 的 full-Q raw 迁移或单一 source-preserving p-edge adapter 不能证明该 candidate；这不排除独立的 target-chart raw source path、m>1 前驱或非 raw source-switch。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-even-tail-complement-source-switch
  - type-I-g-anchor-full-q-complement-r11-reset-boundary
  - type-I-g-anchor-torsor-source-adapter-boundary
  - type-I-g-anchor-marked-raw-peeling-calculus
  - type-I-bottom-word-lattice-pareto-cycle-capacity-selector
  - type-I-universal-p-source-capacity-anchor-orbit
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - complement-torsor
  - raw-path
  - m1
  - even-tail
  - source-adapter
  - no-go
  - phase
  - proof-boundary
sources:
  - claim: type-I-g-anchor-even-tail-complement-source-switch
    role: complement-seed-even-tail-realization
  - claim: type-I-g-anchor-full-q-complement-r11-reset-boundary
    role: conditional-R11-reset
  - claim: type-I-bottom-word-lattice-pareto-cycle-capacity-selector
    role: raw-word-matrix-semantics
  - concept: denominator-escape-state-contract
    role: E1-E5-boundary
visibility: public
last_checked: '2026-08-06'
---

# G-anchor 补余 seed 的 \(m=1\) raw 词互反性与 source-adapter 刚性

## 1. 底层 raw 词的终点互反性

固定一个合法 Type I 图表

\[
4K=pR+1,
\qquad
R\equiv3\pmod4.
\tag{1}
\]

把 primitive \(m=1\) node 写作

\[
N_R(u)=\{u,R-u\},
\qquad
0<u<R,
\qquad
(u,R)=1.
\tag{2}
\]

若素数 \(q\mid u\) 满足 \(v_q(u)>v_q(K)\)，formal raw 规则在这一层没有
gcd 约分，并且为

\[
N_R(u)\xrightarrow{q}N_R(u/q).
\tag{3}
\]

令一条从 canonical anchor \(N_R(1)\) 出发的 \(m=1\) raw 词的标签积为

\[
\Theta=\prod_i q_i.
\tag{4}
\]

每一步若选择第一坐标，则 \(q u'=u\)；若选择另一坐标，则该另一坐标满足同一
恒等式。又两个坐标之和为 \(R\)。逐步归纳给出：若终点为 \(N_R(x)\)，则

\[
\boxed{\Theta x\equiv\pm1\pmod R.}
\tag{5}
\]

符号只记录终点把 \(x\) 放在哪个有序坐标，故不会因把 node 视为无序而消失。

现在假设这个 node 同时是一个 physical determinant seed。即

\[
K=Mx,
\qquad
R=4M-n,
\qquad
x=p-d.
\tag{6}
\]

由 \(4Mx=pR+1\) 得

\[
xn=x(4M-R)=R(p-x)+1=Rd+1.
\tag{7}
\]

所以 \(n\) 是 \(x\) 在 \(U(R)\) 中的逆元。与 (5) 合并，得到下面的精确
endpoint gate。

**定理（determinant--raw 互反门）。** 任意如上的 \(m=1\) raw 词必满足

\[
\boxed{\Theta\equiv\pm n\pmod R.}
\tag{8}
\]

这是 raw path 的必要同余，不是 Type I/II certificate，也不产生 E1--E5 边。

## 2. \(c=3\) seed 的唯一入边与精确尾链

令

\[
p=24h+1,
\qquad
h\not\equiv2\pmod3.
\tag{9}
\]

full-\(Q\) 补余 seed 为

\[
\begin{aligned}
R&=104h-9, & M&=26h+1, & n&=13,\\
x&=24h-2, & y&=80h-7, & K&=Mx.
\end{aligned}
\tag{10}
\]

这里 \((x,R)=1\)、\(y>R/2\)，且

\[
4x<R<5x,
\qquad
v_2(x)=v_2(K)=1.
\tag{11}
\]

一个进入 \(N_R(x)\) 的 \(m=1\) raw 边不能从 \(y\) 一侧来，因为 \(2y>R\)。
若从 \(x\) 一侧来，其前驱只能是 \(N_R(qx)\)，由 (11) 只需考察
\(q\in\{2,3\}\)。

\(q=2\) 总是有效。对 \(q=3\)：若 \(h\equiv0\pmod3\)，则 \(3\mid R\)，
不满足 raw unit 条件；若 \(h\equiv1\pmod3\)，则 \(3\mid M\) 而
\(3\nmid x\)，故 \(v_3(3x)\le v_3(K)\)。因此只有一条直接入边：

\[
\boxed{
N_R(2x)=\{48h-4,56h-5\}
\xrightarrow{2}
N_R(x).
}
\tag{12}
\]

并且 \(N_R(2x)\) 自身只有一个可指向它的 \(m=1\) 前驱：

\[
N_R(4x)\xrightarrow{2}N_R(2x)
\xrightarrow{2}N_R(x).
\tag{13}
\]

确实 \(4x<R<8x\)，而从另一坐标制造前驱在几何上不可能；两个 \(2\)-边都由
\(v_2(2^j x)>v_2(K)\) 给出。

偶侧编码在 (13) 的三个 node 上分别为

\[
(M,C,t)=(26h+1,24h-2,4),\quad
(26h+1,24h-2,2),\quad
(26h+1,24h-2,1).
\tag{14}
\]

因此三者给出的未标记 physical determinant 行完全相同：

\[
(M,C,d,n)=(26h+1,24h-2,3,13).
\tag{15}
\]

这条局部 raw 链无法让任何只读取 (15) 的势严格下降；精确尾 \(t\) 或等价相位是
不可省略的状态字段。

由 (8)，到 seed 的词必须有 \(\Theta\equiv\pm13\pmod R\)。更细地，到
\(N_R(4x)\) 的前缀词必须满足

\[
\Theta\equiv\pm\frac{13}{4}\equiv\pm M\pmod R,
\tag{16}
\]

因为 \(4M=R+13\)。故任何从 target canonical anchor 到 seed 的正长度
\(m=1\) path 都必须以 (13) 结尾，并先到达带相位 \(\pm M\) 的 \(t=4\) node。
这把 \(c=3\) 的 source 问题缩小为一个具体的、带标签的到达性问题。

## 3. \(c=9\) seed 在 \(m=1\) 图中无入边

令 \(h\equiv2\pmod3\)。此时

\[
R=\frac{200h-67}{3},
\qquad
M=\frac{50h+2}{3},
\qquad
x=24h-8,
\qquad
y=\frac{128h-43}{3},
\qquad
n=25.
\tag{17}
\]

有 \(y>R/2\) 以及

\[
2x<R<3x.
\tag{18}
\]

所以进入 \(N_R(x)\) 的唯一几何候选是从 \(N_R(2x)\) 经 \(q=2\) 来。
但写 \(h=3k+2\) 后

\[
M=50k+34
\tag{19}
\]

为偶数，从而

\[
v_2(2x)\le v_2(K)=v_2(x)+v_2(M).
\tag{20}
\]

这个候选不是 raw 边。因此

\[
\boxed{\text{\(c=9\) complement seed 在整个 \(m=1\) raw 图中没有入边。}}
\tag{21}
\]

同样地，(8) 要求任何假想的 anchor word 有 \(\Theta\equiv\pm25\pmod R\)，但
(21) 表明它不可能由正长度纯 \(m=1\) word 实现。该结论不排除 \(m>1\) 前驱及其
gcd 约分。

## 4. full-\(Q\) 词的整体剩余类障碍

旧 G-anchor 的 full 标签积为

\[
Q_0=\frac{p-3}{2}=12h-1.
\tag{22}
\]

即使暂时忽略先前已经证明的逐素数容量失效，若一个 target-anchor word 仍保留这个
完整标签积，则 (8) 也要求

\[
Q_0\equiv\pm13\pmod{104h-9}
\tag{23}
\]

或在 \(c=9\) 分支要求

\[
Q_0\equiv\pm25\pmod{(200h-67)/3}.
\tag{24}
\]

在核心域这两式均不成立：\(Q_0>13\)（分别 \(>25\)）且
\(Q_0<R-13\)（分别 \(Q_0<R-25\)）。所以 old full-\(Q\) word 不仅不能逐边
raw-preserving 地迁移，也不能以同一总标签积终止于补余 seed。

## 5. universal \(p\)-edge 的 source-adapter no-go

仍在 \(c=3\) 分支，令

\[
R_0=p-2,
\qquad
R_T=104h-9,
\qquad
\Delta=R_T-R_0=80h-8.
\tag{25}
\]

每个图表都有有序 universal source 与唯一 \(q=p\) 后继

\[
\mathsf S_R=(p,R(p-1)-p,p-1)
\xrightarrow{p}
\mathsf A_R=(1,R-1,1).
\tag{26}
\]

这里 \(p\nmid K\)、shift 为 \(1\)、gcd reduction 为 \(1\)，故该 \(p\)-边是
确定的。定义两种最自然的单坐标仿射注入：

\[
J_V(U,V,m)=(U,V+\Delta m,m),
\qquad
J_U(U,V,m)=(U+\Delta m,V,m).
\tag{27}
\]

前者精确满足

\[
J_V(\mathsf S_{R_0})=\mathsf S_{R_T},
\qquad
J_V(\mathsf A_{R_0})=\mathsf A_{R_T};
\tag{28}
\]

所以它确实 intertwine (26)。后者则把 anchor 送到 seed 的反向定向：

\[
J_U(1,p-3,1)=(80h-7,24h-2,1),
\tag{29}
\]

但它不把 \(\mathsf S_{R_0}\) 送到 \(\mathsf S_{R_T}\)。固定的全局坐标交换只同时
交换 (28) 两端，不能改变这个结论。

事实上不需要局限在 (27)。若任意映射 \(F\) 同时满足

\[
F(\mathsf S_{R_0})=\mathsf S_{R_T},
\qquad
F\bigl(T_p(\mathsf S_{R_0})\bigr)=T_p\bigl(F(\mathsf S_{R_0})\bigr),
\tag{30}
\]

则 (26) 的唯一性强制

\[
F(\mathsf A_{R_0})=\mathsf A_{R_T}
\tag{31}
\]

（至多差一个同样的全局坐标交换）。但 seed 的两个坐标都大于 \(1\)，所以它不是
\(\mathsf A_{R_T}\)。因此没有任何 source-preserving、\(q=p\)-edge-intertwining
adapter 能同时把 old anchor 送到 even-tail seed。

## 6. 范围与下一步

本卡严格排除了保留 old G source/full-\(Q\) 语义的 \(m=1\) raw 迁移，以及 single
source-preserving \(p\)-edge intertwiner 作为补余 seed provenance 的解释。它没有排除：

1. \(c=3\) 中从 target source 出发、到 \(N_R(4x)\) 的另一条带相位 \(\pm M\) 的 raw path；
   [affine-prime target-source 模板](type-I-g-anchor-c3-affine-prime-target-source-template.md)
   及其 [双中间节点推广](type-I-g-anchor-c3-two-intermediate-target-source-template.md)
   已在多个条件性素数族上构造这种 raw receipt，但其 E3--E5 合同仍未完成；
2. \(c=9\) 中的 \(m>1\) 前驱或独立 source tree；
   [二进高层前驱卡](type-I-g-anchor-c9-dyadic-high-layer-predecessor.md) 已给出无穷多局部
   raw 前驱，但不提供 source provenance；
3. 一个明确记录换向、容量饱和与 scope 的新 source macro；
4. 已有 verified seed receipt 之后的 \(R=11\) dual-RESET。

特别地，(13)、(21) 和 (31) 都只属于 raw/source provenance 分析。它们没有提供
E3 verifier、全域 \(\operatorname{Sol}(p)\) lift 或 E5 支付，故不构成
`verified_edge`，更不声称 Erdos--Straus 猜想已被解决。

作为一致性例子，\(p=73\) 时 \((R,x,M,n)=(303,70,79,13)\)。已知 target-anchor
路径在最后三点经过

\[
\{23,280\}\xrightarrow2\{140,163\}\xrightarrow2\{70,233\},
\tag{32}
\]

其完整标签积为

\[
151\cdot43\cdot2\cdot37\cdot13\cdot2\cdot2
\equiv-13\pmod{303},
\tag{33}
\]

而到 \(\{23,280\}=N_R(4x)\) 的前缀积为 \(-79\pmod{303}\)，恰与 (16) 一致。
该控制点的完整条件性 source path 及逐边容量检查见
[affine-prime target-source 模板](type-I-g-anchor-c3-affine-prime-target-source-template.md)；
其可枚举双中间节点推广见
[双中间节点 target-source 模板](type-I-g-anchor-c3-two-intermediate-target-source-template.md)。
