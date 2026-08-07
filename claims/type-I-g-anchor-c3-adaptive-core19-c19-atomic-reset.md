---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-c19-atomic-reset
title: c=3 adaptive core-19 的 C=19 原子 raw-to-R=63 RESET
statement: 设 high-R Type-I chart 的 forward raw leaf 解码为固定余因子 C=c、载体 M=K/c。令 1<=a<4c 满足 ap=-1 (mod 4c)，则其 A=1 r-side dual RESET 精确落到 (R_r,K_r)=(a,(ap+1)/4)。对 c=19、h=8 (mod 19) 有 a=63。一个固定 C=19 mixed-side factor-block grammar 给出 target-independent sufficient raw language；但同 chart 的 C0=p-3 与 C1=19 leaf 在旧 A=1 state hash 下有后继碰撞，故 C1 入口必须携带 immutable entry digest，或将 root receipt 与 reset 做成不持久化中间 seed 的原子宏。v=5 控制以非规范未界 F 见证和 R=63 的显式 hit 完成局部 E1--E5 回执，但被直接 Type II terminal-first 截断，未登记 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-v5-dual-leaf-f19-control
  - type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
  - type-I-overflow-a-one-dual-outer-rank-reset
  - type-I-fg-fourier-to-type-II-role-demand-bridge
  - denominator-escape-state-contract
topics:
  - type-I
  - c3
  - core19
  - raw-source
  - factor-block
  - root-entry
  - atomic-macro
  - dual-reset
  - well-founded-descent
  - F-state
  - q-primary
  - terminal-first
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_c19_atomic_reset.py
    role: exact raw grammar, F/hit, reset, state-collision, and terminal control
  - claim: type-I-g-anchor-c3-adaptive-core19-v5-dual-leaf-f19-control
    role: source raw tree and q=19 fixed-layer control
  - claim: type-I-overflow-a-one-dual-outer-rank-reset
    role: E4/E5 reset theorem
visibility: public
last_checked: '2026-08-07'
---

# \(c=3\) adaptive core-19 的 \(C=19\) 原子 RESET

本卡给出一个可重放的 local root-entry structure：固定 \(C=19\) 的 mixed-side
raw leaf 有一个确定的低模 RESET。它不宣称所有核心素数都有该 leaf，也不把
terminal-preempted control 登记为 selector edge。

## 1. 固定余因子的低模 RESET

设

\[
pR+1=4K,\qquad R>p,\qquad c\mid K,\qquad 1\le c<p,
\tag{1}
\]

并且一个 forward raw leaf 已解码为

\[
C=c,\qquad M=K/c,\qquad d=p-c,\qquad n=4M-R.
\tag{2}
\]

则 \(pn=4Md+1\)。因为 \(p\nmid K\)，有 \((p,4c)=1\)。令 \(a\) 为唯一满足

\[
1\le a<4c,\qquad ap\equiv-1\pmod {4c}
\tag{3}
\]

的整数，并定义

\[
r=\frac{ap+1}{4c},\qquad
s=\frac{ap-ac+1}{c}.
\tag{4}
\]

**固定 \(c\) RESET 引理。** \(r\) 是 \(M\bmod p\) 的唯一代表
\(1\le r<p\)，且

\[
ps=4r(p-c)+1,\qquad
\boxed{R_r=4r-s=a,\qquad K_r=r(p-(p-c))=cr=\frac{ap+1}{4}.}
\tag{5}
\]

从 \(4cM=pR+1\) 得 \(M\equiv(4c)^{-1}\pmod p\)，故 (3) 的 \(r\)
确为所需代表。再由

\[
\frac{4r(p-c)+1}{p}
=\frac{(ap+1)(p-c)+c}{cp}
=\frac{ap-ac+1}{c}
\]

得到 (5)。

若 \(a<p\)，目标 chart 是 marked_absorb。对于已授权的 \(A=1\) raw root，
这正是 [A=1 对偶外层秩 RESET](type-I-overflow-a-one-dual-outer-rank-reset.md)
的 \(r\)-侧：用图表无关的 \(\operatorname{Sol}(p)\) 作恒等 lift，且

\[
\left\lfloor B_p/r\right\rfloor<B_p,\qquad
B_p=(p-1)^2/4,
\]

分别给 E4 和 E5。式 (1)--(5) 本身不制造 raw provenance。

## 2. \(c=19\) 的固定 \(R=63\) 分支

在 \(c=3\) family 中，\(h\equiv8\pmod {19}\) 时

\[
p=24h+1\equiv41\pmod {76}.
\]

取 \(c=19\)，式 (3) 的解为 \(a=63\)，所以每个已解码的 \(C=19\)
leaf 满足

\[
r=\frac{63p+1}{76},\qquad
s=\frac{63p-1196}{19},\qquad
\boxed{(R_r,K_r)=\left(63,\frac{63p+1}{4}\right).}
\tag{6}
\]

这里 \(1196=1197-1\)，因为 \(4r-63=(63p+1-1197)/19\)。
故 \(R=63\) 不是搜索偶然性，而是固定余因子正规形的算术强制结果。

## 3. C=19 actual raw 子语言

以下只刻画一条指定 side/block topology。假设

\[
R\equiv1\pmod5,\qquad 5\nmid K,\qquad19\mid K,\qquad(19,R)=1.
\tag{7}
\]

取正整数 \(a,b,Q_1,Q_2,Q_3\)，满足

\[
R-1=5bQ_1,\qquad
4R+b=5aQ_2,\qquad
R-a=95Q_3,
\tag{8}
\]

并要求 block 的末次剥离保留严格容量：

\[
\begin{aligned}
\ell\mid Q_1&\Longrightarrow v_\ell(b)\ge v_\ell(K),\\
\ell\mid Q_2&\Longrightarrow v_\ell(a)\ge v_\ell(K),\\
\ell\mid Q_3&\Longrightarrow v_\ell(19)\ge v_\ell(K).
\end{aligned}
\tag{9}
\]

从 declared universal \(p\)-source 的 \(p\)-edge 后交换 anchor 坐标，则

\[
5;\ \operatorname{Fac}(Q_1);\ 5;\ \operatorname{Fac}(Q_2);\
5;\ \operatorname{Fac}(Q_3)
\tag{10}
\]

是一个无 gcd reduction 的 actual raw word，终点为
\((19,R-19,1)\)。三个 \(5\)-step 的关键坐标依次为

\[
bQ_1,\qquad (R-b)/5,\qquad19Q_3,
\]

而第二 block 的互补坐标为 \(aQ_2\)。故 (8) 给 endpoint，(9) 给每个
factor block 的 endpoint reserve；反向的无约分 replay 也强制 (8)--(9)。
这只是一条 sufficient-and-necessary sublanguage，不是完整 \(C=19\) Reach
分类。其 physical tail 是

\[
t=1,\qquad\epsilon=+1,\qquad\Phi=-n\pmod R.
\tag{11}
\]

在当前 adaptive ray

\[
\begin{aligned}
p(v)&=181740263041+204127330680v,\\
R(v)&=787541139831+884551766280v,
\end{aligned}
\]

固定 v=5 skeleton 的三个 block 候选可写为

\[
B=(R-1)/5,\qquad
Q_1=B/11246,\qquad
Q_2=(4R+11246)/1930,\qquad
Q_3=(R-386)/95.
\]

这给出精确条件

\[
11246\mid B\Longleftrightarrow v\equiv5\pmod {5623},
\]

\[
1930\mid4R+11246\Longleftrightarrow v\equiv5\pmod {193},
\]

而 \(95\mid R-386\) 对全部 \(v\) 成立。因此该整数 skeleton 成立当且仅当

\[
\boxed{v\equiv5\pmod {1085239}.}
\]

若该类中的 \(p(v)\) 为素数且 \(\gcd(Q_1Q_2Q_3,K(v))=1\)，逐素因子展开每个
\(Q_i\) 就给出 (10) 的 actual primitive word。这是一条条件性的同源 raw
dual-leaf family，不是只属于 \(v=5\) 的单点现象；也不声称这条 topology 覆盖
全部 C=19 Reach。

固定常数 label word 不可能覆盖无界 family：若其标签积恒为 \(\Theta\)，则 endpoint
reciprocity 给 \(19\Theta\equiv\pm1\pmod R\)，所以
\(R\mid19\Theta\mp1\)，只可能有有限多个 \(R\)。因此参数化 factor blocks 或
canonical forward Reach search 是必要的。

## 4. v=5 的 F-to-hit 原子控制

在 [v=5 双 leaf 控制](type-I-g-anchor-c3-adaptive-core19-v5-dual-leaf-f19-control.md) 中，

\[
\begin{aligned}
p&=1202376916441,&R&=5210299971231,\\
K&=2\cdot19^2\cdot193\cdot5351\cdot66383\cdot31641497801.
\end{aligned}
\]

(8) 的实例为

\[
(b,a,Q_1,Q_2,Q_3)
=(11246,386,92660501,10798549169,54845262851).
\tag{12}
\]

源端的 1215 点中心盒不命中 \(-1\)，而明确的长模见证是

\[
31641497801^{105942250765}\equiv-1\pmod R.
\tag{13}
\]

provided_unbounded_modular 回执逐项检查 (13) 和有限盒缺失，并将 signed defect
保存为 prime-exponent factorization，不物化天文大的整数。它证明 F classification，
但标记 canonical_fourier_eligible=false，因此不能替代 canonical
minimum-\(\ell^1\) Fourier witness，也不能直接进入 q-capacity 或 phase bridge。

式 (6) 给

\[
r=996707180734,\qquad s=3986828722873,\qquad
(R_r,K_r)=(63,18937436433946),
\tag{14}
\]

并且 \(K_r=2\cdot19\cdot3169\cdot5657\cdot27799\)。按该因子顺序，

\[
(0,-1,0,1,1)
\tag{15}
\]

是一个盒内 hit witness，直接达到 \(-1\pmod {63}\)。目标类型独立重算为
hit，而不是从源 F label 继承。

## 5. 为什么必须是原子宏

现有 make_state hash 只含

    (4/p, R, K, absorbed support, state class, fiber class, source-tree scope)

它不含 \(C,t,\epsilon,\Phi\) 或 raw_entry_digest。在 v=5，\(C_0=p-3\)
与 \(C_1=19\) 因此给出同一个 legacy \(A=1\) F state id；但 \(C_0\) 的自然
\(d\)-RESET 目标是 \(R=11\)，\(C_1\) 的 \(r\)-RESET 目标是 \(R=63\)。
这个持久 state 无法在不读取未哈希外部证据时确定唯一后继。

所以合同上只有两种修复：

1. 将 immutable entry_digest 写入 root state id；至少包含 \(C\)，若以后允许
   raw action，还要包含 \(t,\epsilon,\Phi\)、ordered lineage、policy/version 和
   full raw digest。
2. 不持久化这个 seed，把 root receipt 与 (6) 做成一个 atomic macro。

本卡采用第二种方案。这是合同必要条件，不是实现偏好。

## 6. q=19 的正确角色

此点的 \(\eta(x)=x^{10}\pmod {191}\) 有精确 19 阶，但
\(\eta(-1)=1\)。它不可能直接分离 target involution。对两条 leaf，

\[
\eta(C_0)=\zeta^3,\qquad
\eta(C_1)=\zeta^{11},\qquad
\eta(C_0C_1^{-1})=\zeta^{11}\ne1.
\tag{16}
\]

所以若未来 mixed-side adapter 把两条 leaf 放入同一个 complete source fiber，
它必须产生相对 SOURCE_RANK_DEMAND(19)，且相对 label map 必须满足

\[
\lambda(C_0)-\lambda(C_1)\equiv11\pmod {19}.
\]

当前 raw receipt 尚未给出这个 source adapter，故不能登记 capacity 或 descent。
这只是对 [Fourier 角色到 source-rank 分派](type-I-fg-fourier-to-type-II-role-demand-bridge.md)
在 target-even odd-primary 情形的精化。

## 7. Terminal-first 状态

v=5 有直接 Type II \((m,d)=(3,11)\) terminal。复现器因此将整个宏标记为
terminal_preempted_control：local E1--E5、F/hit reclassification 和 atomic
state contract 都通过，但 dispatcher 必须先输出 terminal，不能注册该宏为
verified_edge。

窄复现：

    python3 reproductions/type_i_c3_adaptive_core19_c19_atomic_reset.py --verify

当前 exact skeleton 的目标化 terminal screen 尚未产生 terminal-free point，因此下一步
不应扩大同一 short-gap scan；应改变 C=19 中间 topology 或 chart parameterization，再为
新的 raw language 建立 complete mixed-side source adapter。不能以 (13) 的
noncanonical witness 或 (16) 的 target-even character 跳过这两个 gate。
