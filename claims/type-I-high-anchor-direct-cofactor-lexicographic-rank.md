---
kind: claim
claim_id: type-I-high-anchor-direct-cofactor-lexicographic-rank
title: 高锚点 direct cofactor 宏步的 token-Omega 良基秩
statement: 固定 p、同一 source_tree_scope 内，限制于 canonical、通过代数 gate 的高锚点 direct cofactor 宏步，并在 terminal/alternate 检查后抑制精确 h=0,c=1 自环。令 T=1/0 表示正相位 token 未消费/已消费，令 rho=Omega(K/A)。则每个非平凡宏步都使 lexicographic rank (T,rho) 严格下降：h>0 消费 T，h=0,c>1 使 rho 严格下降。因此该子程序无无限非平凡链；其非平凡深度至多 2 floor(log_2(p-1))+1。此结果不把外部 support promotion、RESET、fresh-root、非 canonical transient overflow 或 support_reset_paid 纳入同一秩。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-three-phase-nonreturn-window
  - type-I-high-anchor-positive-phase-one-shot-token
  - type-I-fixed-high-anchor-return-one-shot-exhaustion
  - type-I-overflow-cofactor-r-chart-support
topics:
  - type-I
  - high-carrier
  - r-chart
  - nonreturn
  - return
  - well-founded-descent
  - scheduler
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_r_chart_two_anchor.py
    role: p=1201 strict zero-phase support-payment control
  - reproduction: reproductions/type_i_high_r_chart_60913_h2_nonreturn.py
    role: positive h=2 token-consumption control
visibility: public
last_checked: '2026-08-06'
---

# 高锚点 direct cofactor 宏步的 token-Omega 良基秩

## 1. 范围与秩

固定 \(p\equiv1\pmod4\)，并只考虑同一 source_tree_scope 内的 direct
high-cofactor 宏步。其 source 是 canonical 高锚点

\[
pR+1=4K,\qquad A\mid K,\qquad p<R<4A,
\tag{1}
\]

内部 bundle 产生 \(1\le r,C<p\) 的 cofactor chart，且 target gate
\(A_C=\operatorname{lcm}(A,C)\mid rC\) 已通过。令

\[
h=\frac{rC-K}{pA},\qquad K=AB,\qquad
g=(A,C),\quad A=ga,\quad C=gc,\quad r=at.
\tag{2}
\]

三相引理给出 \(h\in\{0,1,2\}\)，并有

\[
A_C=Ac,\qquad ct=B+ph.
\tag{3}
\]

令 \(\Omega(n)\) 表示 \(n\) 的素因子重数总数，且 \(\Omega(1)=0\)。调度状态携带
不可重置的一位 \(T\in\{0,1\}\)：在本 direct cofactor phase 尚未使用正相位时
\(T=1\)，使用后为 \(T=0\)。定义

\[
\rho(p,R,K;A)=\Omega(K/A)=\Omega(B),
\qquad
\mathcal R=(T,\rho)
\tag{4}
\]

并按通常的字典序比较 \(\{0,1\}\times\mathbb N\)。这里 \(T\) 是路径/调度元数据，
不是单靠算术 chart 可恢复的字段。

## 2. 零相位的精确支付

若 \(h=0\)，则 (3) 化为

\[
ct=B,\qquad K_T=rC=K,\qquad R_T=R,\qquad A_T=Ac.
\tag{5}
\]

故 \(c\mid B\) 且

\[
\rho_T=\Omega(K/A_T)=\Omega(B/c)
=\rho-\Omega(c).
\tag{6}
\]

所以 \(c>1\) 时，\(T\) 保持不变而 \(\rho\) 严格下降。这个结论不依赖产生
\((r,C)\) 的 bundle；它适用于任何通过 gate 的零相位宏步。

唯一不支付任何量的是 \(c=1\)。在本范围内它等价于

\[
\boxed{
c=1
\Longleftrightarrow
r\mid K,\ R<4r,\ K/r\mid A
\Longleftrightarrow
r\in\mathcal D_{p,R,K}\ \text{且}\ B\mid r.
}
\tag{7}
\]

事实上，\(h=0\) 的回返判据给出 \(C=K/r\)；\(c=1\) 正是 \(C\mid A\)，
等价于 \(r=B(A/C)\)。此时 (5) 给出完整的算术 checkpoint
\((p,R,K;A)\) 不变。

因此一个 action 只有在其 full capability digest、bundle digest 和 phase token 均未
带来新信息时，才可记录为 STUTTER_EXHAUSTED 并不进入递归队列。该抑制只删除
同一 action 的重复 macro successor；它不删除不同 bundle 的 terminal 或 alternate
检查，也不把同图表的严格 support promotion 误删。

## 3. 正相位与字典序下降

若 \(h>0\)，正相位一次性令牌引理表明在这个 direct canonical+gate phase 内不能
再次出现正相位。调度器只允许

\[
T=1\longmapsto T_T=0.
\tag{8}
\]

目标的 \(\rho_T\) 可以改变甚至增大，但 (8) 仍使 \(\mathcal R\) 严格下降。若
\(h=0,c>1\)，则由 (6) 同样严格下降；若 \(h=0,c=1\)，它是 (7) 的被抑制 identity，
不构成递归边。

于是每一条被允许入队的 direct cofactor 宏边均满足

\[
\boxed{\mathcal R_T<_{\rm lex}\mathcal R_S.}
\tag{9}
\]

由于字典序在 \(\{0,1\}\times\mathbb N\) 上良基，该子程序不存在无限非平凡链。

## 4. 显式深度界

对任一高 canonical chart，\(R\le4A-1\) 蕴含

\[
B=\frac{pR+1}{4A}
\le p-\frac{p-1}{4A}<p.
\tag{10}
\]

故 \(\Omega(B)\le\lfloor\log_2(p-1)\rfloor\)。正相位 target 仍是高 canonical
chart，所以它自己的 \(B_T=K_T/A_T\) 也满足同一界。正相位前、后的所有严格零相位
分别至多有 \(\lfloor\log_2(p-1)\rfloor\) 条，而正相位至多一条。因此 direct
cofactor phase 的非平凡深度至多为

\[
\boxed{2\lfloor\log_2(p-1)\rfloor+1.}
\tag{11}
\]

这是一条子程序深度界，不是对全部 selector 路径的界。

## 5. 两个控制边界

\(p=1201\) 的首次高锚点回返具有

\[
(R,K;A)=(1839,552160;986),\qquad
C=952,\quad r=580,\quad c=28.
\]

这里 \(h=0\)、\(A_T=27608\)，且

\[
K/A=560=2^4\cdot5\cdot7,\qquad
K/A_T=20=2^2\cdot5,
\]

所以 \(\rho:6\to3\)。这说明回返不等于 no-op；严格支撑支付由 (6) 精确记录。

相反，\(p=97\) 取

\[
R=99,\qquad K=A=2401=7^4.
\]

high-\(R\) complete-excess adapter 给出

\[
Q=2,\quad M=4802,\quad r=C=49,\quad h=0,\quad c=1,
\]

并精确回到 \((R_T,K_T;A_T)=(99,2401;2401)\)。这是实际的 macro self-loop，
不是空洞的调度可能性。此例有 \(A=B_p+p>B_p\)，故不应被误读为盒内 E5 证据。

## 6. 选择器边界

本卡只关闭 direct high-cofactor phase 内的非平凡重复。它不授权把当前
candidate_transition 自动改为全局 verified_edge：完整 parent ledger、全域
F/G lift、terminal-first 分派，以及离开本 phase 后的 RESET/reentry 仍须各自满足
E1--E5。特别地，support_reset_paid、forgetful RESET、fresh-root 重建、跨
source_tree_scope 或非 canonical transient carrier 必须显式离开此秩，不能把
\(\mathcal R\) 当作它们的全局势。
