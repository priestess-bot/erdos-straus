---
kind: claim
claim_id: type-I-g-anchor-c3-root-to-r11-reset-terminal-bridge
title: c=3 一次性 root-to-R=11 RESET 与固定尾 terminal bridge
statement: 若一个 c=3 target-source raw receipt 已按 fresh_source_tree_only 顶层 root policy 完成 E1--E3 初始化，则它可创建 A=1 overflow state (p,104h-9,(26h+1)(p-3);1)，并有一条严格、可提升的 d=3 dual RESET 到 (p,11,3(22h+1);3)。该 RESET 以 Sol(p) 恒等映射给出 E4，以 absorbed-support 势 144h^2>48h^2 给出 E5。对 R=11 目标，有限 exponent-box hit 当且仅当存在第三分母 pK_11 的直接 Type I terminal，因此 terminal-first 可在 root 创建前精确分流。该卡只证明已验证 root receipt 之后的条件性 edge；它不把 raw word、formal p-parent 或未接入的 factor-block path 升级为 verified_edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
  - type-I-g-anchor-c3-factor-block-raw-source-receipts
  - type-I-g-anchor-full-q-complement-r11-reset-boundary
  - type-I-overflow-a-one-dual-outer-rank-reset
  - denominator-escape-state-contract
topics:
  - type-I
  - c3
  - root-entry
  - R11
  - dual-reset
  - terminal-first
  - E4
  - E5
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
    role: root-receipt-fields-and-scope
  - claim: type-I-g-anchor-full-q-complement-r11-reset-boundary
    role: d3-dual-target
  - claim: type-I-overflow-a-one-dual-outer-rank-reset
    role: reset-lift-and-potential-contract
  - concept: denominator-escape-state-contract
    role: E1-E5-edge-contract
visibility: public
last_checked: '2026-08-06'
---

# \(c=3\) 一次性 root-to-\(R=11\) RESET

## 1. 条件性 root receipt

令

\[
p=24h+1,
\qquad
R=104h-9,
\qquad
M=26h+1,
\qquad
x=p-3,
\qquad
K=Mx.
\tag{1}
\]

设 RootRec_c3(h) 是一个已经完成的顶层 raw receipt。它必须从声明式 target
universal \(p\)-source 开始，到达 \(N_R(x)\)，并包含：

\[
pR+1=4K,
\qquad
pn=4Md+1,
\qquad
(d,n)=(3,13),
\tag{2}
\]

以及 fresh_source_tree_only、root-only scope、完整有序 raw transcript、even-tail
\((t,\text{direction},\text{phase})\) 与重新计算的 typed fiber。它初始化，而不是递归产生，

\[
S_h=(p,R,K;A=1).
\tag{3}
\]

本卡从这个已验证前提出发；它不声称任意 local raw path 都可充当 RootRec_c3。

## 2. \(d=3\) RESET 的精确形式

由 (1) 有

\[
M=p+2h,
\qquad
r=M\bmod p=2h.
\tag{4}
\]

于是

\[
s=\frac{4rd+1}{p}
=\frac{24h+1}{p}
=1.
\tag{5}
\]

因此 \(d=3\) 的 dual 参数精确为

\[
R_d=4d-s=11,
\qquad
K_d=d(p-r)=3(22h+1).
\tag{6}
\]

也就是说，(3) 的唯一安全后续候选是

\[
S_h
\Longrightarrow
T_h=(p,11,3(22h+1);A=3).
\tag{7}
\]

这里的双箭头表示一个按既有 dual-RESET 合同验证的 selector edge；它不是 raw word 的
逐边投影。

## 3. E4 与 E5

两端使用同一个图表无关标记解集

\[
W_{S_h}=W_{T_h}=\operatorname{Sol}(p),
\qquad
\Phi_{S_h\to T_h}=\operatorname{id}.
\tag{8}
\]

所以 RESET 的 E4 是完整的恒等 lift：每个单位分数分解与 equation-only 标签均不变。
两张图表上的 F/G/hit 分类必须独立重算，不能把 source classification 复制到 \(R=11\)。

令既有 absorbed-support 外层基势为

\[
B_p=\frac{(p-1)^2}{4}=144h^2.
\tag{9}
\]

则 (7) 的势支付为

\[
\Pi_A(S_h)=B_p=144h^2
>
\frac{B_p}{3}=48h^2
=\Pi_A(T_h).
\tag{10}
\]

因此严格下降发生在 \(A:1\mapsto3\) 的 RESET；raw word 内的坐标交换、以及
\(t=4\to2\to1\) 同一 physical row 的尾部，都不被错误用作 E5。

## 4. \(R=11\) 的固定第三分母 terminal 判据

令

\[
K_{11}=\frac{11p+1}{4}=3(22h+1)=\prod_i q_i^{\nu_i}.
\tag{11}
\]

**定理（有限 box hit 等价于固定尾 Type I terminal）。** 以下两件事等价：

\[
\exists(z_i),\quad
-\nu_i\le z_i\le\nu_i,
\qquad
\prod_iq_i^{z_i}\equiv-1\pmod{11};
\tag{12}
\]

\[
\exists e\mid K_{11}^2,
\qquad
e\equiv-K_{11}\pmod{11}.
\tag{13}
\]

在任一等价条件下，令

\[
u=\frac{K_{11}+e}{11},
\qquad
v=\frac{K_{11}+K_{11}^2/e}{11}.
\tag{14}
\]

则

\[
\boxed{
\frac4p
=\frac1u
+\frac1v
+\frac1{pK_{11}}.}
\tag{15}
\]

**证明。** 从 (12) 令 \(e=K_{11}\prod_iq_i^{z_i}\)，其每个指数落在
\([0,2\nu_i]\)，故 \(e\mid K_{11}^2\)，且同余给出 (13)。反之对 (13) 的
每个 \(q_i\)-进指数减去 \(\nu_i\)，即得到 (12)。

式 (13) 保证 (14) 为正整数。再由

\[
\frac1u+\frac1v=\frac{11}{K_{11}},
\qquad
\frac4p-\frac1{pK_{11}}=\frac{4K_{11}-1}{pK_{11}}
=\frac{11}{K_{11}},
\tag{16}
\]

即得 (15)。证毕。

## 5. terminal-first 调度与边界

因此一个合法的条件性调度是：

1. 先检查 (12)；命中时立即输出 (15)，不创建 root；
2. 未命中且 RootRec_c3(h) 已经有效时，创建 (3) 并执行 (7)；
3. 没有有效 root receipt 时，仅保留未路由证据，绝不从 formal \(p\)-parent 补造 root。

在 \(U(11)\cong C_{10}\) 中，若所有 \(q_i\mid K_{11}\) 都是二次剩余，则
\(-1\) 不在其生成子群，得到 Legendre-G 分类；若有一个非二次剩余素因子，则生成子群
包含 \(-1\)，对应 F/hit 侧。无论哪种情形，分类只服务于 \(R=11\) 的独立 E3 重算，
不改变 (8)--(10) 的 E4/E5 结论。

特别地，形式化 \(p\)-parent 的 \(p\)-step 具有目标依赖的构造签名，不能替代
RootRec_c3 所需的 canonical universal-source \(p\)-edge 与 fresh scope。故本卡不把
factor-block raw receipt、dyadic formal source 或任何 charged history 直接注册为
global verified_edge。
