---
kind: claim
claim_id: type-II-q-one-full-carrier-d-one-capacity-four-exclusion
title: q=1 full-carrier 的 d=1 立即接收态容量四全称排除
statement: >-
  设 ordinary q=1 G full-carrier root 的第二-anchor fixed-n 宏进入 persistent
  high target，且其强制 full-product fold 产生 d=1 receiver
  A=(pn-1)/4、R=(p-1)n-1、K=A(p-1)，其中 n>1。令其 p-free complete-excess
  canonical target 的 residual capacity 为 c。则 c 不可能等于 4。奇 t 分支把
  假设压到唯一 p=73 边界行，而该行的障碍数为 47；偶 t=2s 分支只有
  (k,g)=(2,1),(2,7) 两个兼容形状，分别强迫 j=48s+11 或 j=48s-1，均违反
  j<3q_*<=18s-3。因此 q=1 immediate image 不进入 c=4 容量面；特别地，
  p=25 (mod 48) 的已知最小 high C=4 canonical stutter 图表不可能是该 immediate
  image 的直接 target。该结论不排除后续一般 Type I 路径到达 C=4，也不处理 c>=5。
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
  - c-four
  - stutter-avoidance
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
    role: parity-normal-forms-for-the-persistent-immediate-receiver
  - claim: type-II-q-one-full-carrier-second-anchor-fixed-n-macro
    role: q-star-source-and-bound-j-less-than-three-q-star
  - claim: type-I-overflow-full-product-d-one-complete-excess-capacity-map
    role: canonical-capacity-congruence
  - claim: type-I-high-support-c4-canonical-stutter-boundary
    role: adjacent-c-four-stutter-family-not-reached-at-the-immediate-step
  - reproduction: reproductions/type_ii_q_one_full_carrier_d_one_capacity_four_exclusion.py
    role: focused-boundary-and-finite-shape-receipt
visibility: public
last_checked: '2026-08-17'
---

# q=1 full-carrier 的 d=1 立即接收态容量四全称排除

## 1. 要排除的容量面

固定 ordinary \(q=1\) G full-carrier root 的第二-anchor fixed-\(n\) 宏。只考虑其
persistent immediate \(d=1\) receiver：

\[
A=\frac{pn-1}{4},\qquad
R=(p-1)n-1,\qquad
K=A(p-1),\qquad n>1.
\tag{1}
\]

已有 p-free gate 排除使 complete-excess carrier 的 canonical target 唯一；记该
target 的 residual capacity 为

\[
c=\frac{K_M}{M}\in\{1,\ldots,p-1\}.
\tag{2}
\]

本卡证明

\[
\boxed{c\ne4.}
\tag{3}
\]

与容量三卡一样，这只描述 q=1 的 *immediate image*；它不是一般 high \(C=4\) 图表
或全局 Type I selector 的结论。

## 2. 奇 \(t\) 分支

令 \(p=24t+1\)，其中 \(t\) 为奇数。已有闭式给出

\[
14\delta+3=jp,\qquad1\le j\le13,
\tag{4}
\]

\[
\alpha=\frac{p+1}{2},\qquad
v=\frac{n+1}{2},\qquad
g=(\alpha,v),\qquad g\mid j+3,
\tag{5}
\]

以及容量同余

\[
c(7j+27)\equiv42g\pmod p.
\tag{6}
\]

若 \(c=4\)，因 \(p\) 为奇素数，

\[
p\mid D_o:=14j+54-21g.
\tag{7}
\]

由 \(1\le j\le13\)、\(1\le g\le j+3\)，有

\[
-100\le D_o\le215.
\tag{8}
\]

又 \(D_o\equiv54\equiv5\pmod7\)，所以 \(D_o\ne0\)。于是 \(p\le215\)。在奇
\(t\) 且 \(p=24t+1\) 的核心素数中，唯一可能是

\[
p=73,\qquad t=3.
\tag{9}
\]

该行给出 \(j=1,g=1\)，所以

\[
D_o=47,
\tag{10}
\]

不被 \(73\) 整除。故奇支不可能有 \(c=4\)。

## 3. 偶 \(t\) 分支的两种伪形状

令 \(t=2s\)。则

\[
p=48s+1,\qquad s\ge2,
\tag{11}
\]

并有强制 excess prime \(q_\star\) 和整数 \(j\)：

\[
q_\star\mid6s-1,\qquad
1\le j<3q_\star\le18s-3,\qquad j\equiv2\pmod3,
\tag{12}
\]

\[
\alpha=24s+1,\qquad v=6js+1,\qquad g=(\alpha,v),\qquad g\mid j-4.
\tag{13}
\]

容量同余现在为

\[
c(12-j)\equiv8g\pmod p.
\tag{14}
\]

假设 \(c=4\)。将 (14) 除以 \(2\)，可写成

\[
2j+4g=24+kp
\tag{15}
\]

的整数 \(k\)。若 \(j=2\)，则 \(g=1\)，而 (15) 强迫 \(p\mid16\)，不可能。故
\(j\ge5\)。由 \(g\le j-4\) 和 (12)，有

\[
14\le2j+4g\le6j-16\le108s-40<3p.
\tag{16}
\]

因此

\[
0\le k\le2.
\tag{17}
\]

又 \(p\) 为奇数，(15) 的右侧必须为偶数，故 \(k\) 为偶数。并且
\(g\mid\alpha\) 蕴含 \(g\) 为奇数、\(3\nmid g\) 及 \(p\equiv-1\pmod g\)。把
(15) 模 \(g\) 化简，得到

\[
g\mid16-k.
\tag{18}
\]

最后，\(j\equiv2\pmod3\) 与 (15) 等价于

\[
k-g\equiv1\pmod3.
\tag{19}
\]

由 (17)--(19)，\(k=0\) 只能给 \(g=1\)，但这违反 (19)；其余全部可能性恰为

\[
\begin{array}{c|c|c}
k&g&j=(24+kp-4g)/2\\ \hline
2&1&48s+11\\
2&7&48s-1.
\end{array}
\tag{20}
\]

两行均违反 (12)，因为

\[
48s+11>18s-3,\qquad48s-1>18s-3
\tag{21}
\]

对一切 \(s\ge2\) 成立。因此偶支也不可能有 \(c=4\)。

## 4. 与已知 \(C=4\) stutter 的关系

最小 high \(C=4\) canonical stutter 的正分支处于

\[
p\equiv25\pmod{48}.
\tag{22}
\]

这恰与奇 \(t\) 的 q=1 支的素数同余类一致。然而 (3) 表明，q=1 full-carrier
宏的 immediate receiver 不能直接把该类素数送入任何 \(c=4\) target，所以更不能
直接送入该最小 stutter 图表。

这只是一次入口排除：它不声称该 stutter 图表没有其他 source，也不排除 q=1 后续的
一般 Type I relay 最终抵达 \(C=4\)。

## 5. 结论与边界

\[
\boxed{\text{ordinary }q=1\text{ full-carrier 的 persistent immediate }d=1
\text{ receiver 从不以 }c=4\text{ 离开。}}
\tag{23}
\]

结合既有 \(c=2\) 的单一 19 相位刚性与新近 \(c=3\) 的全空结论，q=1 immediate
image 的低容量谱已被进一步压缩；仍未分类的是 \(c=1\)、\(c\ge5\) 及这些 target
上的全称 terminal/strict-edge dispatch。

聚焦复核：

~~~bash
python3 reproductions/type_ii_q_one_full_carrier_d_one_capacity_four_exclusion.py --verify
~~~

复现器只重放奇支唯一有限边界，以及偶支的有限 \((k,g)\) 形状和 affine 不等式；它不做
素数范围扫描或一般 terminal 搜索。
