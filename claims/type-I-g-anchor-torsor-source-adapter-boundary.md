---
kind: claim
claim_id: type-I-g-anchor-torsor-source-adapter-boundary
title: full-Q torsor target 的 canonical raw adapter 局部 no-go
statement: 设旧 G-anchor 为 R_0=p-2、Q_0=(p-3)/2。对 full-Q 的 z=1 平移 target 及两类补余 target，仿射映射 (U,V,m)->(U,V+(R_T-R_0)m,m) 精确对齐 universal p-source 和其首个 p-边，但不能对齐 canonical full-Q 分支。更强地，z=1 target 与 c=3 补余 target 满足 gcd(Q_0,Q_T)=1，故旧 full-Q word 的每个素数首边都不能在目标 canonical anchor 原样出现；c=9 补余 target 满足 gcd(Q_0,Q_T)|5<Q_0，故至少有一个首边必失效。目标 anchor 的 complete-excess lcm carrier 也不可能等于 torsor determinant seed carrier，因为前者不整除 K_T 而后者整除 K_T。以上只排除 canonical prime-labelled word 和 carrier-identification 接口；不排除 nonlocal raw-word replacement、带尾标记投影、多图表步骤、独立 source tree 或新的 E5-付费 RESET。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-jacobi-odd-complete-excess-source-menu
  - type-I-g-anchor-fixed-chart-affine-complement-overflow-torsor
  - type-I-g-anchor-raw-fixed-chart-factor-projection
  - type-I-universal-p-source-capacity-anchor-orbit
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - full-Q
  - torsor
  - universal-source
  - raw-path
  - adapter
  - complete-excess
  - no-go
  - proof-boundary
sources:
  - claim: type-I-g-anchor-jacobi-odd-complete-excess-source-menu
    role: old-canonical-full-Q-word
  - claim: type-I-g-anchor-fixed-chart-affine-complement-overflow-torsor
    role: target-torsor-families
  - claim: type-I-g-anchor-raw-fixed-chart-factor-projection
    role: marked-projection-boundary
visibility: public
last_checked: '2026-08-06'
---

# full-\(Q\) torsor target 的 canonical raw adapter 局部 no-go

## 1. 旧 anchor 与三类 target

固定

\[
p=24h+1,
\qquad
R_0=p-2,
\qquad
Q_0=\frac{R_0-1}{2}=12h-1.
\tag{1}
\]

旧 G-anchor 的 canonical 完整超额块正是 \(Q_0\)。从它的 anchor
\(\{1,2Q_0\}\) 出发，full-\(Q_0\) raw word 需使用每个 \(q\mid Q_0\) 的素数
幂。

令 \(R_T\) 是以下任一个 torsor target 的半径，并置

\[
Q_T=\frac{R_T-1}{2}.
\tag{2}
\]

对 \(\epsilon\in\{3,9\}\)，\(z=1\) 平移族为

\[
R_T=R_0+4\epsilon,
\qquad
Q_T=Q_0+2\epsilon.
\tag{3}
\]

补余族分别为

\[
\begin{array}{c|c|c}
\epsilon&R_T&Q_T\\ \hline
3&104h-9&52h-5\\
9&(200h-67)/3&(100h-35)/3.
\end{array}
\tag{4}
\]

第二行使用 \(h\equiv2\pmod3\)，所以其中的整数性已包含在分支假设中。

## 2. 只能对齐首个 \(p\)-边

设 \(\Delta=R_T-R_0\)。对形式源定义

\[
\Phi_\Delta(U,V,m)=(U,V+\Delta m,m).
\tag{5}
\]

这保持 \(U+V=R_0m\) 的结构，并精确地送出

\[
\begin{aligned}
&\Phi_\Delta\bigl(p,R_0(p-1)-p,p-1\bigr)\\
&\hspace{1.5cm}=
\bigl(p,R_T(p-1)-p,p-1\bigr).
\end{aligned}
\tag{6}
\]

所以它也保持 universal source 的首个 \(q=p,t=1\) raw 边。但 canonical
full-\(Q\) 分支在 anchor 的大坐标上作用。如果把大坐标写在第一位，则

\[
\Phi_\Delta(R_0-1,1,1)
=(R_0-1,1+\Delta,1)
\ne(R_T-1,1,1).
\tag{7}
\]

故 (5) 是一个 source 的仿射对齐，不是 canonical full-\(Q\) branch 的
action-preserving adapter。

## 3. 素数标记 raw word 的精确缺口

对平移族，

\[
(Q_0,Q_T)=(Q_0,2\epsilon)=1,
\tag{8}
\]

因为 \(Q_0=12h-1\) 与 \(6\) 及 \(18\) 都互素。对 \(\epsilon=3\) 的补余族，

\[
13Q_0-3Q_T=2,
\tag{9}
\]

两端均为奇数，故

\[
(Q_0,Q_T)=1.
\tag{10}
\]

对 \(\epsilon=9\) 的补余族，

\[
25Q_0-9Q_T=80.
\tag{11}
\]

两数仍均为奇数，所以 \((Q_0,Q_T)\mid5\)。而
\(Q_0\equiv11\pmod{12}\) 不可能是 \(5\) 的幂，因此

\[
(Q_0,Q_T)<Q_0.
\tag{12}
\]

旧 anchor 的每个 \(q\mid Q_0\) 都是合法 raw 边的标记，因为
\((Q_0,K_0)=1\)。若要在 target canonical anchor 保留同一个 \(q\)-标记的首边，
必要条件是

\[
q\mid2Q_T.
\tag{13}
\]

因此：

- 平移族和 \(\epsilon=3\) 补余族使旧 word 的**所有** \(q\)-首边失效；
- \(\epsilon=9\) 补余族至少使其中一条首边失效，因此完整 full-\(Q_0\)
  prime-word 不可以原样迁移。

第二条不能说得更强。例如 \(p=193\) 时 \(Q_0=95\)，\(\epsilon=9\)
的 target 有 \(Q_T=255\)，旧的 \(q=5\) 仍可作为 target anchor 的 raw 边；
缺失的是 \(q=19\)。

## 4. complete-excess carrier 不能等同于 seed carrier

这些 target 都满足 \(R_T-1>p+1\)。如果 target anchor 有
\(R_T-1\mid K_T\)，由 \(pR_T+1=4K_T\) 模 \(R_T-1\) 约化会得
\(R_T-1\mid p+1\)，矛盾。因而这些 anchor 的完整超额块
\(Q_{\rm exc}\) 非平凡，且

\[
Q_{\rm exc}\nmid K_T.
\tag{14}
\]

对任意合法账本 \(A\mid K_T\)，它的 single complete-excess carrier 为

\[
M_{\rm CE}=\operatorname{lcm}(A,Q_{\rm exc}),
\qquad
M_{\rm CE}\nmid K_T.
\tag{15}
\]

另一方面，torsor seed 的 determinant 载体满足

\[
M_{\rm seed}\mid K_T.
\tag{16}
\]

因此

\[
M_{\rm CE}\ne M_{\rm seed}.
\tag{17}
\]

这只排除“把 target-anchor 的单个 complete-excess lcm carrier 直接认作
torsor determinant seed carrier”这种接口。它绝不排除带尾标记的非平凡投影：旧
\(p=73\) G 图表已有

\[
Q_{\rm exc}=35\ne432=M_Q,
\qquad
35\longmapsto(M_Q,t_Q)=(432,23),
\tag{18}
\]

的实际 raw-to-marked-row 投影。

若一条非 RESET 的 lcm 账本历史已纳入 \(Q_{\rm exc}\)，则它不能在保留
账本的情况下回到精确 seed。否则会有

\[
Q_{\rm exc}\mid A\mid M_{\rm seed}\mid K_T,
\tag{19}
\]

与 (14) 矛盾。现有合规 RESET 也要以 lcm 保留旧账本，不能把 (19) 直接
丢弃。

## 5. 精确结论

本卡的 no-go 具有故意狭的范围：它排除 canonical prime-labelled
full-\(Q\) word 的原样迁移，以及 single complete-excess carrier 与种子
carrier 的身份合并。它未排除：

1. 把旧 raw word 非局部地替换为新 target word；
2. 使用精确尾 \(t\) 的新 marked projection；
3. 多张图表或独立 fresh source tree；
4. 带有新的、可证 E5 付款的 RESET。

因此接下来的正向任务不是继续将 torsor 行做算术重参数化，而是构造或排除
一个真正的 marked source/path adapter，并为它补齐 E1、E3、E4 与 E5。
