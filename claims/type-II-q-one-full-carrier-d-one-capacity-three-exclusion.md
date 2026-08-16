---
kind: claim
claim_id: type-II-q-one-full-carrier-d-one-capacity-three-exclusion
title: q=1 full-carrier 的 d=1 立即接收态容量三全称排除
statement: >-
  设 ordinary q=1 G full-carrier root 的第二-anchor fixed-n 宏进入 persistent
  high target，且其强制 full-product fold 产生 d=1 receiver
  A=(pn-1)/4、R=(p-1)n-1、K=A(p-1)，其中 n>1。令该 receiver 的 p-free
  complete-excess canonical target 的 residual capacity 为 c。则 c 不可能等于
  3。奇 t 分支的容量三同余把问题压到唯一 p=73 边界行，而该行的障碍数为 20；
  偶 t=2s 分支只可能留下 (k,g)=(1,23),(2,1),(4,5) 三个形状，其中两条
  affine j 界直接越过 j<3q_*，最后一条由 q_* 同时整除 6s-1 和 jp+4 强迫
  q_*|1239，亦与 j<3q_* 矛盾。因此 q=1 immediate image 不进入 c=3 容量面。
  该结论不处理 c>=4，也不构造一般 Type I terminal、严格 edge 或 global exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-second-anchor-fixed-n-macro
  - type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - full-carrier
  - type-I
  - d-one
  - complete-excess
  - residual-capacity
  - c-three
  - finite-rigidity
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
    role: parity-normal-forms-for-the-persistent-immediate-receiver
  - claim: type-II-q-one-full-carrier-second-anchor-fixed-n-macro
    role: q-star-source-and-bound-j-less-than-three-q-star
  - claim: type-I-overflow-full-product-d-one-complete-excess-capacity-map
    role: canonical-capacity-congruence
  - reproduction: reproductions/type_ii_q_one_full_carrier_d_one_capacity_three_exclusion.py
    role: focused-boundary-and-finite-shape-receipt
visibility: public
last_checked: '2026-08-17'
---

# q=1 full-carrier 的 d=1 立即接收态容量三全称排除

## 1. 范围与容量公式

固定 ordinary \(q=1\) G full-carrier root 的第二-anchor fixed-\(n\) 宏。若宏已经
在低图表 absorbed，或 full-product fold 的 successor 已低于 \(p\)，则不在本卡范围内。
只考虑其 persistent immediate \(d=1\) receiver：

\[
A=\frac{pn-1}{4},\qquad
R=(p-1)n-1,\qquad
K=A(p-1),\qquad n>1.
\tag{1}
\]

已有 p-free gate 排除保证 complete-excess carrier \(M=AE\) 有唯一 canonical
target。记其 residual capacity 为

\[
c=\frac{K_M}{M}\in\{1,\ldots,p-1\}.
\tag{2}
\]

本卡只证明

\[
\boxed{c\ne3.}
\tag{3}
\]

这是一条关于这个 *immediate q=1 image* 的容量映射结论。它不把一般 high
\(C=3\) 图表与最小 \(C=3\) 边界同一化，也不把 (3) 升级为全局 handoff。

## 2. 奇 \(t\) 分支

令 \(p=24t+1\)，其中 \(t\) 为奇数。既有宏和 p-free relay 的闭式给出唯一 \(j\)：

\[
14\delta+3=jp,\qquad 1\le j\le13,
\tag{4}
\]

\[
21n=5jp+7j-15,\qquad
\alpha=\frac{p+1}{2},\quad v=\frac{n+1}{2},\quad
g=(\alpha,v),\quad g\mid j+3.
\tag{5}
\]

消去 \(t\) 的恒等式给出容量同余

\[
c(7j+27)\equiv42g\pmod p.
\tag{6}
\]

若 \(c=3\)，由于 \(p\ne3\)，则

\[
p\mid D_o:=7j+27-14g.
\tag{7}
\]

由 \(1\le j\le13\) 和 \(1\le g\le j+3\)，有

\[
-106\le D_o\le104.
\tag{8}
\]

同时 \(D_o\equiv27\equiv6\pmod7\)，所以 \(D_o\ne0\)。因此 (7) 强制
\(p\le106\)。奇支有 \(t\ge3\)，且 \(p\equiv1\pmod{24}\)，故唯一仍可能的核心
素数是

\[
p=73,\qquad t=3.
\tag{9}
\]

将这行代回 (4)--(5)，得到

\[
j=1,\qquad n=17,\qquad g=1,\qquad D_o=20,
\tag{10}
\]

与 \(73\mid D_o\) 矛盾。故

\[
\boxed{\text{奇 }t\text{ 的 immediate receiver 从不有 }c=3.}
\tag{11}
\]

## 3. 偶 \(t\) 分支的有限形状表

令 \(t=2s\)，则

\[
p=48s+1,\qquad s\ge2.
\tag{12}
\]

宏的强制 excess prime \(q_\star\) 与唯一 \(j\) 满足

\[
q_\star\mid6s-1,\qquad
3q_\star\delta-4=jp,\qquad
1\le j<3q_\star<p,\qquad j\equiv2\pmod3,
\tag{13}
\]

\[
4n=jp+4-j,\qquad
\alpha=24s+1,\qquad v=6js+1,\qquad g=(\alpha,v).
\tag{14}
\]

由 \(4v-j\alpha=4-j\)，有 \(g\mid j-4\)。同样，容量同余为

\[
c(12-j)\equiv8g\pmod p.
\tag{15}
\]

假设 \(c=3\)。于是存在整数 \(k\) 使

\[
3j+8g=36+kp.
\tag{16}
\]

若 \(j=2\)，则 \(g=1\)，而 (16) 会给出 \(p\mid22\)，与 \(p\ge97\) 矛盾。于是
\(j\ge5\)。由 \(g\le j-4\) 及 \(j<3q_\star\le18s-3\)，有

\[
23\le3j+8g\le11j-32\le198s-76<5p.
\tag{17}
\]

因此 (16) 的唯一可能范围是

\[
0\le k\le4.
\tag{18}
\]

又 \(g\mid\alpha\)，故 \(g\) 为奇数、\(3\nmid g\)，且 \(p\equiv-1\pmod g\)。将
(16) 模 \(g\) 化简，再将其按 \(3\) 的整除性化简，分别得到

\[
g\mid24-k,\qquad k+g\equiv0\pmod3.
\tag{19}
\]

在 (18) 下，(19) 的全部可能性恰为

\[
\begin{array}{c|c|c}
k&g&j=(36+kp-8g)/3\\ \hline
1&23&16s-49\\
2&1&32s+10\\
4&5&64s.
\end{array}
\tag{20}
\]

第二、三行分别有

\[
32s+10>18s-3,\qquad64s>18s-3,
\tag{21}
\]

直接违反 (13) 的 \(j<3q_\star\le18s-3\)。

## 4. 最后一种形状也为空

只剩 \((k,g)=(1,23)\)。因为 \(23\mid\alpha=24s+1\)，可写

\[
s=23u+22,\qquad j=16s-49=368u+303\ge303.
\tag{22}
\]

另一方面，(13) 表明 \(q_\star\) 同时整除 \(6s-1\) 与 \(jp+4\)。对
\(j=16s-49,\ p=48s+1\) 有恒等式

\[
3(jp+4)+1239=(6s-1)(384s-1104).
\tag{23}
\]

故 \(q_\star\mid1239=3\cdot7\cdot59\)。但 \(q_\star\mid6s-1\equiv2\pmod3\)，所以

\[
q_\star\in\{7,59\}.
\tag{24}
\]

这与 (13)、(22) 给出的

\[
303\le j<3q_\star\le177
\tag{25}
\]

矛盾。因此偶支也不可能有 \(c=3\)。

## 5. 结论与边界

由 (11) 和 (25)，得到

\[
\boxed{\text{ordinary }q=1\text{ full-carrier 的 persistent immediate }d=1
\text{ receiver 从不以 }c=3\text{ 离开。}}
\tag{26}
\]

这排除了 q=1 immediate image 直接进入 \(c=3\) 容量面；它与最小 high \(C=3\)
边界的 carry no-go 相邻，但两者没有被混写为同一个结论。仍未分类的是 \(c\ge4\) 的
target，以及这些 target 上的一般 terminal-first selector、严格 edge 与全局良基势。

聚焦复核：

~~~bash
python3 reproductions/type_ii_q_one_full_carrier_d_one_capacity_three_exclusion.py --verify
~~~

复现器仅核验奇支的唯一有限边界、偶支的有限 \((k,g)\) 表和 (23) 的整式恒等式；它不做
素数范围扫描、终端枚举或一般 Type I 搜索。
