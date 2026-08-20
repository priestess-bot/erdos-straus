---
kind: claim
claim_id: type-I-high-support-empty-improvement-c1-local-minimum-boundary
title: 高支撑空改善分支的 C=1 局部最小元与付费 reset 边界
statement: >-
  对 fixed-p TYPEI/CHARGED 高支撑状态 H=(p,R,K;A) 满足 A>B_p、K=A、
  eta_p=0，其 T5 local tuple 为 (0,1,0,0)，是整个 CHARGED 层的绝对最小元。
  因而任意 complete-excess target 的 cofactor c>=1：c=1 只会 stutter，c>1
  上升；任何只把中间上升 chart 当 transient、最终仍回到同 rho 的 CHARGED
  finite macro 也不可能支付 parent-to-final E5。total-cofactor 在 C=1<p 时精确为
  identity。最小 canonical C=1 high chart 是 A_1=(p+1)^2/4、R_1=p+2、K_1=A_1；
  其两个 determinant dual chart 虽为 (p-2,B_p) 与 (3,(3p+1)/4)，却都丢弃旧
  charged support，不能冒充 joined-support edge。故空改善 H 的精确剩余出口只有
  root terminal、严格 outer-rank drop，或带 target-totality 的具名
  CHARGED-to-lower-protocol reset。本卡是全称 local no-go 与接口归约，不关闭 H、F2、
  T6 或 Erdős--Straus 猜想。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-I-high-support-rank-aware-sink-bundle-selector
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - type-I-overflow-total-cofactor-canonical-projection-persistence-rank
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-high-anchor-direct-c1-finite-menu-exhaustion
  - type-I-t5-full-contract-level-global-well-foundedness
topics:
  - type-I
  - high-support
  - empty-improvement
  - residual-capacity
  - cofactor-one
  - local-minimum
  - phase-reset
  - no-go
  - proof-boundary
sources:
  - claim: type-I-high-support-rank-aware-sink-bundle-selector
    role: nonempty-improvement-edge-and-empty-family-no-go
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: exact-canonical-carry-formula
  - claim: type-I-overflow-total-cofactor-canonical-projection-persistence-rank
    role: canonical-projection-stutter-boundary
  - concept: t5-global-well-foundedness-contract-v2
    role: fixed-protocol-order-and-local-rank
  - reproduction: reproductions/type_i_high_support_c1_local_minimum_boundary.py
    role: symbolic-C1-boundary-and-p73-two-bundle-control
visibility: public
last_checked: '2026-08-20'
---

# 高支撑空改善分支的 $C=1$ 局部最小元与付费 reset 边界

## 1. 固定 T5 下的绝对局部底层

固定核心素数 $p\equiv1\pmod {24}$，并记

\[
B_p=\frac{(p-1)^2}{4}.
\tag{1}
\]

设 actual persistent high-support 状态为

\[
H=(p,R,K;A,\sigma),
\qquad
A>B_p,
\qquad
A\mid K,
\qquad
C=K/A.
\tag{2}
\]

在没有 active $d=1$ regeneration token 时，固定 T5 的 `TYPEI/CHARGED` local tuple
是

\[
\lambda(H)=
\left(\left\lfloor\frac{B_p}{A}\right\rfloor,C,0,0\right)
=(0,C,0,0).
\tag{3}
\]

因此 $C=1$ 时

\[
\boxed{\lambda(H)=(0,1,0,0)}
\tag{4}
\]

是该固定 $(p,\rho,\mathrm{TYPEI},\mathrm{CHARGED})$ 层的绝对最小元。

任一合法 complete-excess candidate 的 canonical target cofactor 都满足

\[
1\le c\le p-1.
\tag{5}
\]

其 support $M>A>B_p$，故 target local tuple 为 $(0,c,0,0)$。于是

\[
c=1\Longrightarrow\text{stutter},
\qquad
c>1\Longrightarrow\text{strict rise}.
\tag{6}
\]

事实上 target 仍必为 overflow。因为 $M/A\ge2$、$A>B_p$ 且核心素数
$p\ge73$，

\[
4M\ge8A>2(p-1)^2>p^2+1.
\tag{6a}
\]

所以对任意 $c\ge1$，

\[
R_M=\frac{4Mc-1}{p}>p.
\tag{6b}
\]

因此不能把 $c=1$ target 偷换成 $R_M<p$ 的 marked phase 来支付下降。

更一般地，允许任意有限个不入队的上升 intermediate chart 也没有帮助：只要宏的真实
parent 和最终 persistent target 仍处于同一 CHARGED 层，E5 比较的仍是
$(0,1,0,0)$ 与 $(0,c,0,0)$，所以不可能严格下降。内部某一步先升后降不能替代
parent-to-final ticket。

整体余因子投影也不提供出口。已有精确式

\[
C_S=C_A+pt,
\tag{7}
\]

在 $C_S=1<p$ 时只能有 $C_A=1,t=0$，故 target 与 source 是同一 canonical
chart。

已有 direct-cofactor control 也正好落在同一边界：对 $p=97$，

\[
(R,K;A)=(99,2401;2401)
\tag{7a}
\]

就是 (9)--(10) 的 universal $C=1$ chart。其冻结 $Q_*=2,M=4802$ action 完整
回返 $c=1$，只能作为非入队 exhaustion bookkeeping；当前 T5-v2 local rank 没有
action-menu 剩余数坐标，故该回返不能成为 persistent edge。这是一手 stutter control，
不是“再试一次 direct action 即可离开 C=1”的证据。

## 2. 最小 canonical $C=1$ high chart

canonical $C=1$ 要求

\[
4A\equiv1\pmod p,
\qquad
A>B_p.
\tag{8}
\]

所有解相差 $p$，而刚好越过 $B_p$ 的第一个解为

\[
\boxed{
A_1=B_p+p=\frac{(p+1)^2}{4}.}
\tag{9}
\]

相应图表为

\[
\boxed{
H_1(p)=
\left(p,p+2,\frac{(p+1)^2}{4};\frac{(p+1)^2}{4}\right).}
\tag{10}
\]

它的 determinant 数据为

\[
M=A_1,
\quad
d=p-1,
\quad
n=p^2+p-1,
\quad
r=M\bmod p=\frac{3p+1}{4},
\quad
s=3p-2.
\tag{11}
\]

两个算术 dual chart 精确为

\[
(R_d,K_d)=\left(p-2,B_p\right),
\tag{12}
\]

\[
(R_r,K_r)=\left(3,\frac{3p+1}{4}\right).
\tag{13}
\]

这个 family 对每个核心 $p$ 都是显式合法的抽象 high-support chart，不是有限样本的
偶发现象。其 universal anchor 是 $\{1,p+1\}$。由于 $(p+1)/2$ 为奇数且
$K=((p+1)/2)^2$，完整超额首块为

\[
Q=2,
\qquad
\beta=\frac{p+1}{2},
\qquad
L=2,
\tag{13a}
\]

canonical target cofactor 为

\[
c=2^{-1}\pmod p=\frac{p+1}{2}>1.
\tag{13b}
\]

所以最自然的首 bundle 在每个核心 $p$ 上都严格上升。这里没有声称图表对每个 $p$
都 actual reachable；它严格否定的是“不加 reach/terminal/phase 信息，仅凭 C=1 和
universal source 就有下降 bundle”的过强定理。对 $p=73$，图表
$(R,K;A)=(75,1369;1369)$ 还由模 $75$ 的 Jacobi 角色给出一个显式 G local-minimum
控制。

这两个小图表本身都合法，但它们的自然 support 分别是 $p-1$ 或
$(3p+1)/4$ 的因子；均小于旧承诺 $A_1$。若按 joined-support 规则保留旧 support，
则 $\operatorname{lcm}(A_1,t)>K_t$，不可能整除 $K_t$。所以 (12)--(13) 只能成为
一个另行付款的 forgetful reset 候选，不能伪装成 CHARGED local edge。

## 3. $p=73$ 的两-bundle 正控制及其终点

已有 terminal-first-preempted 的算术状态

\[
H_0=(73,143,2610;1305),
\qquad C_0=2.
\tag{14}
\]

从它的 universal anchor 沿实际 raw path 到 $(45,98)$，取

\[
Q_1=49,
\quad
\beta_1=2,
\quad
45\beta_1=90\mid2610,
\quad
M_1=63945,
\tag{15}
\]

得到不入队 checkpoint

\[
H'_1=(73,21023,383670;63945),
\qquad C'_1=6.
\tag{16}
\]

再从 $H'_1$ 的 universal anchor 到 $(30,20993)$，取

\[
Q_2=2999,
\quad
\beta_2=7,
\quad
30\beta_2=210\mid383670,
\quad
M_2=191771055,
\tag{17}
\]

得到

\[
H_2=(73,10508003,191771055;191771055),
\qquad C_2=1.
\tag{18}
\]

比较真实宏端点可得

\[
(0,2)>(0,1),
\tag{19}
\]

所以在已经具备 actual parent、scope、terminal-priority 和 versioned adapter 的条件下，
这是一条 $C=2\to1$ 的 parent-to-final 严格宏；中间的 $2\to6$ 不入队。三个图表
均须独立重算 fiber typing 和 state ID，E4 只使用
$W=\operatorname{Sol}(4,73)$ 的恒等映射。

但 (18) 正好落在 (4) 的底层，故它不能关闭 high-support family。并且 $p=73$ 有直接
Type II root certificate $(20,219,4380)$，实际 terminal-first 会先结束；因此该宏当前
只能登记为 conditional/analysis control，不能冒充 actual selector edge。

## 4. H 的精确剩余量词

对 empty-improvement high-support 状态，现有证明现在给出完整二分：

1. $C>1$ 时，rank-aware bundle 若有下降候选就已有 E1--E5；某些 $C$ 还可由有限
   多-anchor 宏下降，$p=73,C=2\to1$ 是正控制；
2. $C=1$ 时，任何仍留在同一 CHARGED 层的 bundle 或 total-cofactor finite macro 都被
   (4)--(7) 全称排除。

因此真正剩下的 theorem 不是“再枚举一个 bundle”，而是

\[
\boxed{
\begin{aligned}
&H\text{ actual, terminal-first miss, }A>B_p,C=1\\
&\quad\Longrightarrow
\text{OUTER\_RANK\_DROP}
\ \lor\
\text{paid lower-protocol target with recursively total owner}.
\end{aligned}}
\tag{20}
\]

或者证明该 actual family 为空。一个只丢弃 $A$ 的 arithmetic dual、一个没有 target
totality 的 CHARGED-to-RESET、或一个最终仍为 CHARGED 的有限 bundle 串都不能证明
式 (20)。

## 5. 逻辑状态

本卡严格建立的是：

```text
H-C1-CHARGED-LOCAL-MINIMUM = ESTABLISHED
H-C1-BUNDLE-OR-TOTAL-COFACTOR-EXIT = IMPOSSIBLE_UNDER_FIXED_LOCAL_TICKET
H-C1-PAID-RESET-OR-OUTER-DROP = OPEN
```

所以 `GAP-O1-HIGH-SUPPORT-ROOT-CAPACITY` 仍为 OPEN。若把 H 连同 F1、其余 family
totality、F3、F4 和 F5 都闭合，T5 良基归纳才会给出全局根证书；当前仓库并没有这些
前提。尤其不能用有限 root-terminal 普查倒推出式 (20)。

聚焦验证：

```bash
python reproductions/type_i_high_support_c1_local_minimum_boundary.py --verify
```
