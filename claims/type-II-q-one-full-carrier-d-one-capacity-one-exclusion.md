---
kind: claim
claim_id: type-II-q-one-full-carrier-d-one-capacity-one-exclusion
title: q=1 full-carrier 的 d=1 立即接收态容量一全称排除
statement: >-
  设 ordinary q=1 G full-carrier root 的第二-anchor fixed-n 宏进入 persistent
  high target，且其强制 full-product fold 产生 d=1 receiver
  A=(pn-1)/4、R=(p-1)n-1、K=A(p-1)，其中 n>1。令其 p-free complete-excess
  canonical target 的 residual capacity 为 c。则 c 不可能等于 1。奇 t 分支的
  假设强迫非零障碍数 D=7j+27-42g 被 p 整除，故 p<=554；完整的有限 q=1
  boundary 只含 p=73,313,409，其 D 分别为 -8,48,-8，均不整除。偶 t=2s
  分支仅留下 (k,g)=(1,1),(1,7),(3,5)，分别导致 j=48s+5、48s-43、
  144s-25，均违反 j<3q_*<=18s-3。因此 q=1 immediate image 不进入 c=1
  容量面。该结论不处理 c>=5，也不构造一般 Type I terminal、strict edge 或
  global exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-phase-root-entry
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
  - c-one
  - finite-boundary
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-phase-root-entry
    role: ordinary-q-one-G-root-condition-X-equals-six-t-plus-one
  - claim: type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
    role: parity-normal-forms-for-the-persistent-immediate-receiver
  - claim: type-I-overflow-full-product-d-one-complete-excess-capacity-map
    role: canonical-capacity-congruence
  - reproduction: reproductions/type_ii_q_one_full_carrier_d_one_capacity_one_exclusion.py
    role: exact-finite-odd-boundary-and-even-shape-receipt
visibility: public
last_checked: '2026-08-17'
---

# q=1 full-carrier 的 d=1 立即接收态容量一全称排除

## 1. 范围

只考虑 ordinary \(q=1\) G full-carrier root 的第二-anchor fixed-\(n\) 宏所产生的
persistent immediate \(d=1\) receiver：

\[
A=\frac{pn-1}{4},\qquad
R=(p-1)n-1,\qquad
K=A(p-1),\qquad n>1.
\tag{1}
\]

其 p-free complete-excess canonical target 的 residual capacity 记为

\[
c=\frac{K_M}{M}\in\{1,\ldots,p-1\}.
\tag{2}
\]

本卡证明

\[
\boxed{c\ne1.}
\tag{3}
\]

此处的 ordinary \(q=1\) 条件等价于 \(X=6t+1\) 的每个素因子均为
\(1\pmod3\)。因此下文奇支的有限边界会同时筛去虽然 \(p\) 为核心素数、但不是
\(q=1\) G root 的行。

## 2. 奇 \(t\) 分支的完全有限边界

令 \(p=24t+1\)，其中 \(t\) 为奇数。已有闭式为

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

\[
c(7j+27)\equiv42g\pmod p.
\tag{6}
\]

若 \(c=1\)，则

\[
p\mid D_o:=7j+27-42g.
\tag{7}
\]

由 \(1\le j\le13\) 和 \(1\le g\le j+3\)，有

\[
-554\le D_o\le76.
\tag{8}
\]

又 \(D_o\equiv27\equiv6\pmod7\)，所以 \(D_o\ne0\)。因此 \(p\le554\)，从而
\(t\le23\)。在奇 \(t\) 的这个范围内，\(p=24t+1\) 为素数的候选仅为

\[
(t,p)=(3,73),(13,313),(17,409),(19,457).
\tag{9}
\]

最后一行不是 ordinary \(q=1\) root，因为

\[
X=6\cdot19+1=115=5\cdot23
\tag{10}
\]

含有 \(5\equiv2\pmod3\)。其余三行由固定-\(n\) macro 的闭式直接重放为

\[
\begin{array}{c|c|c|c|c|c}
t&p&\delta&n&j&g&D_o\\ \hline
3&73&5&17&1&1&-8\\
13&313&201&673&9&1&48\\
17&409&29&97&1&1&-8.
\end{array}
\tag{11}
\]

表中每一行都满足 (4)--(6)，但 \(p\nmid D_o\)。这与 (7) 矛盾，故奇支没有
\(c=1\)。

## 3. 偶 \(t\) 分支的有限形状

令 \(t=2s\)，则

\[
p=48s+1,\qquad s\ge2,
\tag{12}
\]

\[
q_\star\mid6s-1,\qquad
1\le j<3q_\star\le18s-3,\qquad
j\equiv2\pmod3,
\tag{13}
\]

\[
\alpha=24s+1,\qquad v=6js+1,\qquad
g=(\alpha,v),\qquad g\mid j-4.
\tag{14}
\]

容量同余 (6) 的偶支版本是

\[
c(12-j)\equiv8g\pmod p.
\tag{15}
\]

若 \(c=1\)，写作

\[
j+8g=12+kp.
\tag{16}
\]

若 \(j=2\)，则 \(g=1\)，而 (16) 强制 \(p\mid2\)，不可能。于是 \(j\ge5\)。
由 \(g\le j-4\) 和 (13)，有

\[
13\le j+8g\le9j-32\le162s-68<4p.
\tag{17}
\]

故

\[
1\le k\le3.
\tag{18}
\]

由于 \(g\mid\alpha=24s+1\)，有 \(g\) 为奇数、\(3\nmid g\)、\(p\equiv-1\pmod g\)。
将 (16) 模 \(g\) 和模 \(3\) 化简，分别得到

\[
g\mid8-k,\qquad
k\equiv2+2g\pmod3.
\tag{19}
\]

(18)--(19) 的全部可能性为

\[
\begin{array}{c|c|c}
k&g&j=12+kp-8g\\ \hline
1&1&48s+5\\
1&7&48s-43\\
3&5&144s-25.
\end{array}
\tag{20}
\]

对 \(s\ge2\)，三行均严格大于 \(18s-3\)，与 (13) 矛盾。因此偶支也没有
\(c=1\)。

## 4. 结论与低容量谱

\[
\boxed{\text{ordinary }q=1\text{ full-carrier 的 persistent immediate }d=1
\text{ receiver 从不以 }c=1\text{ 离开。}}
\tag{21}
\]

现在 immediate image 的低容量面已有精确分流：\(c=1,3,4\) 全空，\(c=2\) 仅可能
落在 \(q_\star=19\) 的高相位；尚未分类的是 \(c\ge5\) 及其后的
terminal-first / strict-edge selector。这个谱描述不等同于全局 G/Type I exit。

聚焦复核：

~~~bash
python3 reproductions/type_ii_q_one_full_carrier_d_one_capacity_one_exclusion.py --verify
~~~

复现器仅重放 (9)--(11) 的有限 q=1 边界及 (20) 的有限形状表；它不进行无界素数扫描、
终端枚举或一般 Type I 搜索。
