---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-structured-node-carry-obstruction
title: q=1 零 k 容量八 target 的两条结构 m=1 节点增容障碍
statement: >-
  设 ordinary q=1 G full-carrier 的 terminal-first 未命中 even fixed-n 宏在零 k 层给出
  c=8,j=11,g=1，并令其首条 p-free relay target 为 K=8M、pR+1=4K，其中
  M=9s(176s+5)(3168s^2+24s-1)。该 target 的两条由宏因子确定的 primitive m=1
  节点 N_E=(E,R-E) 与 N_L=(3L,R-3L) 都有唯一 maximal complete-excess
  multiplier：前者为 F=139392s^2+1980s-59，后者在 s 奇时为
  16(132s+1)(1584s^2+12s-1)、在 s 偶时为
  (132s+1)(1584s^2+12s-1)。两种 canonical rechart 的 capacity 都严格大于 8。
  因而即使未来有独立 source/path adapter 抵达这些节点，随后采用其强制完整 excess
  bundle 也不能支付 c=8 target 的 E5 strict edge。本结论不声称这些节点已有 E1--E4
  来源，也不排除其它 raw 节点、terminal 或跨图表递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - type-I-raw-universal-p-parent-root-policy-boundary
  - denominator-escape-state-contract
topics:
  - type-I
  - q-one
  - full-carrier
  - d-one
  - c-eight
  - structured-node
  - complete-excess
  - carry-obstruction
  - E5
  - proof-boundary
sources:
  - claim: type-I-q-one-full-carrier-d-one-c-eight-second-full-excess-carry-obstruction
    role: c-eight-target-normal-form-and-first-full-excess-boundary
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: maximal-complete-excess-and-lcm-charge-semantics
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: canonical-capacity-carry-gate
  - claim: type-I-raw-universal-p-parent-root-policy-boundary
    role: reverse-raw-parent-is-not-source-provenance
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_structured_node_carry_obstruction.py
    role: exact-node-factorizations-maximality-and-capacity-receipts
visibility: public
last_checked: '2026-08-17'
---

# q=1 零 \(k\) 容量八 target 的两条结构 \(m=1\) 节点增容障碍

## 1. 范围与两条内禀节点

沿用首条完整 excess relay 后的 \(c=8\) target 正规形：

\[
\begin{aligned}
p&=48s+1, & s&\ge86,\\
L&=176s+5, & E&=3168s^2+24s-1,\\
n&=132s+1, & M&=9sLE,\\
K&=8M, & pR+1&=4K=32M.
\end{aligned}
\tag{1}
\]

因此

\[
R=3345408s^3+50688s^2-1392s-1.
\tag{2}
\]

定义两个完全由 (1) 的 macro 因子给出的 \(m=1\) 节点：

\[
\begin{aligned}
N_E&=(E,Y_E),&
Y_E&=R-E=24sF,&
F&=139392s^2+1980s-59,\\
N_L&=(3L,Y_L),&
Y_L&=R-3L=16nH,&
H&=1584s^2+12s-1.
\end{aligned}
\tag{3}
\]

它们不是由希望得到的 capacity 反推出来的：两个小坐标分别就是既有 c=8
normal form 中的因子 \(E\) 和 \(3L\)。直接有

\[
\begin{aligned}
R-2E&=3345408s^3+44352s^2-1440s+1>0,\\
R-6L&=3345408s^3+50688s^2-2448s-31>0
\end{aligned}
\tag{4}
\]

对 \(s\ge86\) 成立，故 (3) 的首坐标确为小坐标。又

\[
E\mid M,\qquad 3L\mid K,
\tag{5}
\]

并且 \((R,K)=1\) 来自 \(pR+1=4K\)。所以两条节点均为 primitive：

\[
\gcd(E,Y_E)=\gcd(3L,Y_L)=1.
\tag{6}
\]

本卡只计算它们在完整-excess 语义下不可避免的 E5 carry。它不把存在的 formal
反向 \(p\)-parent 误作已注册的 source/path provenance。

## 2. \(E\)-节点的精确 multiplier

令 \(s_{59}=59^{v_{59}(s)}\)。下列整数关系控制 \(F\) 与当前 support 的全部交集：

\[
\begin{aligned}
F&\equiv-59\pmod s,\\
-4F+(3168s-45)L&=11,\\
-(168s+4)F+(7392s+225)E&=11,\\
F&\equiv7\pmod{11},\qquad F\equiv1\pmod3,\qquad F\equiv1\pmod2.
\end{aligned}
\tag{7}
\]

因此 \((F,72LE)=1\)、\((F,s)=(59,s)\)。当 \(59\mid s\) 时还有

\[
L\equiv5\pmod{59},
\qquad
E\equiv-1\pmod{59}.
\tag{8}
\]

逐素数应用 complete-excess 的定义于 \(Y_E=24sF\) 和 \(K=72sLE\)，得到

\[
Q_E=s_{59}F,
\qquad
(M,Q_E)=s_{59}.
\tag{9}
\]

所以不依赖 \(s\) 的 \(59\)-进高度，lcm charge 的真正 multiplier 恰为

\[
\boxed{\frac{\operatorname{lcm}(M,Q_E)}M=F.}
\tag{10}
\]

该 multiplier 的模 \(p\) 形状也完全闭式：

\[
4F=242p^2-319p-159,
\qquad
4F\equiv-159\pmod p.
\tag{11}
\]

设其 canonical target capacity 为 \(c_E\)。由 \(Fc_E\equiv8\pmod p\) 与
(11) 得

\[
159c_E\equiv-32\pmod p.
\tag{12}
\]

若 \(1\le c_E\le8\)，则

\[
0<159c_E+32\le1304<p,
\tag{13}
\]

不可能满足 (12)。故

\[
\boxed{c_E>8.}
\tag{14}
\]

## 3. \(3L\)-节点的精确 multiplier

对于 \(Y_L=16nH\)，下列恒等式消除了所有奇素数的 support 重叠：

\[
\begin{aligned}
3L-4n&=11, & n&\equiv1\pmod{11},\\
24sn-E&=1,\\
-16H+(144s-3)L&=1,\\
-2H+E&=1,\\
(n,s)&=(H,s)=1,\qquad n\equiv1\pmod3,\qquad H\equiv-1\pmod3.
\end{aligned}
\tag{15}
\]

于是 \((nH,M)=1\)，而 \(n,H,L,E\) 均为奇数。\(Y_L\) 的二进高度恒为 \(4\)；
\(K\) 的二进高度为 \(3+v_2(s)\)。因此完整 excess block 和 lcm multiplier 为

\[
\begin{array}{c|c|c}
 &Q_L&\operatorname{lcm}(M,Q_L)/M\\
\hline
s\text{ 奇}&16nH&16nH\\
s\text{ 偶}&nH&nH.
\end{array}
\tag{16}
\]

另外，

\[
64nH=p(278784s^2-1584s-127)+63,
\qquad
64nH\equiv63\pmod p.
\tag{17}
\]

令相应的 canonical capacity 为 \(c_L\)。若 \(s\) 奇，(16)--(17) 与
\((16nH)c_L\equiv8\pmod p\) 给出

\[
63c_L\equiv32\pmod p.
\tag{18}
\]

若 \(s\) 偶，则给出

\[
63c_L\equiv512\pmod p.
\tag{19}
\]

在 \(1\le c_L\le8\) 时，(18) 的差 \(63c_L-32\) 属于 \(1,\ldots,p-1\)，
(19) 的差 \(63c_L-512\) 属于 \(-(p-1),\ldots,-1\)；两者均不可能为 \(p\)
的倍数。因此

\[
\boxed{c_L>8.}
\tag{20}
\]

## 4. 结论与边界

首个 anchor 的第二 full-excess carry 已由前卡证明增容。本卡进一步排除两条不同的、
由 c=8 macro 因子直接指定的 \(m=1\) 节点：

\[
\boxed{
N_E\text{ 的 multiplier }F\text{ 与 }N_L\text{ 的 parity multiplier 都不能使 }8
\text{ 下降。}}
\tag{21}
\]

故即使未来为任一节点补足独立的 source/path、typed reclassification 和全域 lift，
它们随后的强制完整-excess action 也无法作为当前 \(c=8\) 的 E5 strict edge。
剩余路线必须改变实际 raw occurrence、使用非本卡两节点的 complete-excess block、
构造直接 terminal，或建立具有独立势的跨图表宏；这里没有声称这些路线失败。

聚焦复核：

~~~bash
python3 reproductions/type_i_q_one_full_carrier_d_one_c_eight_structured_node_carry_obstruction.py --verify
~~~

复现器只重放 (1)--(20) 与一个已有素数 macro 控制、两个固定 parity 算术控制；不扫描
素数、分解 target 或枚举 raw Reach。
