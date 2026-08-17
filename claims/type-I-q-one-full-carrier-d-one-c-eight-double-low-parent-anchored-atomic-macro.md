---
kind: claim
claim_id: type-I-q-one-full-carrier-d-one-c-eight-double-low-parent-anchored-atomic-macro
title: q=1 容量八 double-low 原子 split 的父接收态 checkpoint 宏
statement: >-
  设 P 是一个已持久化、terminal-first 已 miss 的 ordinary q=1 full-carrier
  d=1 receiver，并且其已有严格 complete-excess relay 重放出 q_star=103 的
  c=8 charged checkpoint H=(p,R,8M;M)。若 H 的 chart-local source
  (p,V,p-1) 上存在实际 V-side strict raw prime q>2(p-1)，其 m=1 endpoint
  (a,b) 同时满足 direct capacity c_a 与 atomic-split capacity c_Sigma 都属于
  {1,...,7}，则不必把 H 或该 universal source 当作新 root：以 P 为唯一 persistent source
  的 checkpoint macro 可重放 P=>H、q-word、双侧 maximal complete-excess payload
  与 target 的 terminal-first hit/F/G rechart。它输出 terminal，或输出同 scope、
  charged-history 的 atomic target T，并条件性支付 E1--E5。其严格势直接为
  (floor(B_p/A),p-1)>(0,c_Sigma)，其中 A 是 P 的 support、B_p=(p-1)^2/4。
  因此 double-low 残余不再有独立的 source/provenance 或 E5 缺口；尚未证明的是
  任何实际 endpoint 必命中 double-low、唯一 (D,c,C,g_b)=(1,1,4,47) marker
  可实现，或宏观 g_b 分支有全称出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
  - type-I-chart-least-coprime-prime-anchor-source
  - type-I-q-one-full-carrier-d-one-c-eight-universal-source-non-p-separation
  - type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-path-anchored-atomic-split-total-typed-rechart
  - type-I-q-one-full-carrier-d-one-c-eight-double-low-split-overlap-bridge
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - full-carrier
  - c-eight
  - checkpoint-macro
  - atomic-split
  - source-provenance
  - terminal-first
  - solution-lift
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
    role: persistent-d-one-parent-and-c-eight-checkpoint-relay
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: chart-local-source-is-internal-to-an-existing-persistent-state
  - claim: type-I-q-one-full-carrier-d-one-c-eight-low-gate-complement-pfree-split-interface
    role: actual-raw-q-word-and-forced-p-free-two-sided-payload
  - claim: type-I-path-anchored-atomic-split-total-typed-rechart
    role: target-local-terminal-first-and-total-hit-F-G-rechart
  - claim: type-I-q-one-full-carrier-d-one-c-eight-double-low-split-overlap-bridge
    role: remaining-marker-and-macroscopic-overlap-arithmetic
  - reproduction: reproductions/type_i_q_one_full_carrier_d_one_c_eight_double_low_parent_anchored_atomic_macro.py
    role: checkpoint-source-binding-rank-and-refusal-controls
visibility: public
last_checked: '2026-08-17'
---

# q=1 容量八 double-low 原子 split 的父接收态 checkpoint 宏

## 1. 缺口的准确位置

容量八高 \(R\) chart 的 source 是

\[
\mathsf S_H=(p,V,p-1),\qquad V=R(p-1)-p.
\tag{1}
\]

对一条实际 V-side strict raw prime \(q>2(p-1)\)，它给出无约分的

\[
\mathsf S_H\xrightarrow{q}(a,b,1),\qquad
a=\frac Vq,\quad b=R-a.
\tag{2}
\]

若 direct capacity \(c_a<8\)，已有互补 p-free 定理强制同一 endpoint 具有

\[
a=Q_a\beta_a,\qquad b=Q_b\beta_b,\qquad
Q_a,Q_b>1,\qquad p\nmid Q_aQ_b.
\tag{3}
\]

所以 atomic split 的算术 payload 并不缺失。真正的语义问题是：\(\mathsf S_H\)
由 high-\(R\) chart 反向写出，不能单独为裸 \(H\) 创造 fresh root。

本卡采用已有的正确区分：

1. target-derived source 不能创建新的 state origin；
2. 已从真实 charged parent 到达的 state 可以使用 chart-local source 作为内部
   raw-path witness。

以下只使用第二项。

## 2. 父接收态与 checkpoint

令 \(P\) 是 q=1 second-anchor 宏 full-product fold 后的 persistent receiver：

\[
P=(p,R_P,K_P;A),\qquad K_P=A(p-1),\qquad
B_p=\frac{(p-1)^2}{4}.
\tag{4}
\]

其 receipt 必含 state id、source scope、terminal-first miss 与可重放的 strict
relay \(P\Longrightarrow H\)。在 zero-\(k\), \(q_\star=103\),
\(j=11\), \(g=1\) 行，macro-local checkpoint 为

\[
H=(p,R,8M;M),\qquad pR+1=32M,
\tag{5}
\]

\[
p=48s+1,\qquad
M=9s(176s+5)(3168s^2+24s-1).
\tag{6}
\]

既有 p-free relay 给出

\[
M>p^2>B_p.
\tag{7}
\]

容量八闭式还给出 \(p\nmid R\)。因此 (1) 是 \(H\) 的 actual chart-local
raw source；它继承 \(P\) 的 charged history，却绝不成为 \(H\) 的新 state origin。
宏可以重放 \(H\)，但不允许删掉 \(P\) 后把 \(H\) 独立入队。

## 3. Double-low suffix

定义

\[
N=\operatorname{lcm}(M,Q_a,Q_b),\qquad
L=\frac NM,\qquad
C=\left\langle8L^{-1}\right\rangle_p.
\tag{8}
\]

complete-excess maximality 给出

\[
N>M,\qquad p\nmid N,\qquad
K_T=NC,\qquad R_T=\frac{4NC-1}{p}.
\tag{9}
\]

本卡的唯一分支前提是

\[
1\le c_a\le7,\qquad1\le C\le7.
\tag{10}
\]

于是 macro 的唯一输出为

\[
P\Longrightarrow H
\xRightarrow[\text{actual}]{\mathsf S_H\to(a,b,1)}
(Q_a,Q_b)
\Longrightarrow
\begin{cases}
\text{terminal},\\
T=(p,R_T,K_T;N,\sigma),
\end{cases}
\tag{11}
\]

其中 \(\sigma\) 原样继承 \(P\) 的 source scope。target 的 direct screen、centered
hit/F/G、signed defect、normal form 和 state id 全部由 \((p,R_T,K_T,N)\) 重算。
不能从 \(P\) 或 \(H\) 复制 typed fields。

owner 绑定同一个 physical occurrence：

\[
\operatorname{owner}=
\bigl(
\text{c8-double-low-parent-macro-v1},
\operatorname{state\_id}(P),
\operatorname{digest}(P\Longrightarrow H),
\operatorname{digest}(\mathsf S_H\xrightarrow q(a,b,1))
\bigr).
\tag{12}
\]

target 的 charged-history parent link 指向 \(P\)，而 \(H\) 及 raw q-word 保存在
checkpoint payload。故交换左右显示不会产生第二个 owner。

## 4. E1--E5

E1 由 \(P\) 的 persistent history、\(P\Longrightarrow H\)、(1)--(3) 的 actual
raw witness 与两侧 maximality 组成。这里的 chart-local source 只作为已存在 checkpoint
的内部 witness，不担任 root policy。

E2 由 (8)--(9) 的唯一 lcm charge 和 canonical target 支付。target-local terminal
优先于递归输出。

E3 重放 parent receipt、checkpoint digest、raw q-word、two-color payload、scope、
owner、target validator 与内容寻址 state id；缺失 parent receipt 的 bare \(H\) 必须在
任何 suffix 运算前被拒绝。

E4 使用图表无关的恒等 lift：

\[
W_P=W_T=\operatorname{Sol}(p),\qquad
\Phi_{T\to P}=\operatorname{id}.
\tag{13}
\]

E5 不需要把 \(H\) 误当成新 source。由 (4)、(7)、(9)：

\[
\Lambda(P)=
\left(\left\lfloor\frac{B_p}{A}\right\rfloor,p-1\right),
\qquad
\Lambda(T)=(0,C).
\tag{14}
\]

若 \(A\le B_p\)，第一坐标严格下降。若 \(A>B_p\)，两边第一坐标为零，而 (10)
给出 \(C\le7<p-1\)。所以

\[
\boxed{\Lambda(T)<\Lambda(P).}
\tag{15}
\]

因此在完整 parent/typed verifier 接受时，(11) 是一条条件性 E1--E5 strict macro，
而非一条 target-derived raw source 的伪递归边。

## 5. 与 overlap bridge 的分工

double-low overlap bridge 已把此分支的剩余算术压为：

\[
(D,c_a,C,2^\epsilon g_b)=(1,1,4,47),
\tag{16}
\]

或

\[
p\le1568g_b+15\,052\,023.
\tag{17}
\]

本卡使 (16)--(17) 不再附带独立的 source/provenance、target typing 或 E5 缺口。
一旦出现满足 (10) 的 actual endpoint，剩余任务仅是它的算术存在性、terminal priority
与 (16)--(17) 的因子分配分析。

## 6. 固定拒绝控制与边界

已知 \(s=3279\), \(p=157393\) 的 c=8 checkpoint 确实由 q=1 parent 重放。其
actual V-side label

\[
q=5963047
\tag{18}
\]

给出

\[
c_a=11230,\qquad C=38261.
\tag{19}
\]

这个控制还会被 terminal-first 抢占，故它故意不是正例。它仅验证 checkpoint-parent
绑定、chart-local source、non-low 拒绝与 bare-checkpoint 拒绝。

本卡没有证明任何 actual double-low endpoint 存在，没有证明唯一 marker 可实现，也没有
关闭宏观 \(g_b\) 分支或 G/Type I global exit。

聚焦复核：

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_q_one_full_carrier_d_one_c_eight_double_low_parent_anchored_atomic_macro.py \
  --verify
~~~

复现器只重放一个真实 c=8 checkpoint、一个真实但 non-low 的 raw receipt、rank 的两种
逻辑分支和 bare-checkpoint 拒绝；不扫描参数、素数、V 的因子或历史测试。
