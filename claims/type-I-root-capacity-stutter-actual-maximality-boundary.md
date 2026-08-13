---
kind: claim
claim_id: type-I-root-capacity-stutter-actual-maximality-boundary
title: 根容量 stutter 的 actual-maximality 不可由除子交集替代
statement: >-
  在根容量图表中，即使一个候选 D0 同时满足 root layer、D0|R-h、D0|K、
  D0|ph+1、D0=1-h mod p 和完整三参数 stutter 曲线，它也不必是 canonical
  maximal complete-excess receipt 的实际 D。两个固定控制分别显示：未超过容量的
  2-adic residual 必须留在 beta，和超过容量后的 (A,Q) 归一化仍可把 2 因子带回 D。
  因而不能把“D 是 actual maximal receipt”放松为上述有限除子条件；这不是核心素数
  proper-root stutter 门为空的证明，也不产生 Type I/II 证书或全局递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-general-endpoint-divisor-gate
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-receipt-factor-split
topics:
  - type-I
  - root-capacity
  - stutter
  - complete-excess
  - maximality
  - valuations
  - counterexample
  - proof-boundary
sources:
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: canonical-D-and-stutter-gate
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: relaxed-three-parameter-stutter-conditions
  - reproduction: reproductions/type_i_root_capacity_stutter_actual_maximality_boundary.py
    role: fixed-residual-and-normalization-controls
visibility: public
last_checked: '2026-08-14'
---

# 根容量 stutter 的 actual-maximality 不可由除子交集替代

## 1. 要排除的错误放松

在根容量图表中，令

\[
z=R-h,
\qquad
Q=\prod_{v_q(z)>v_q(K)}q^{v_q(z)},
\qquad
\beta=\frac zQ,
\]

并令

\[
g_A=(A,Q),
\qquad E=\frac Q{g_A},
\qquad D=\beta g_A.
\tag{1}
\]

这里的 \(D\) 才是 complete-excess receipt 的 canonical 实际除子。一个看似自然、但
不充分的放松是取某个 \(D_0\) 并只检查

\[
D_0\mid z,qquad D_0\mid K,qquad
D_0\mid ph+1,qquad D_0\equiv1-h\pmod p,
\tag{2}
\]

再加上三参数曲线

\[
D_0=mp+1-h,\qquad eD_0=ph+1,\qquad
p(em-h)=e(h-1)+1,\qquad h\mid F(e,m).
\tag{3}
\]

本条给出两个严格整数控制，说明 (2)--(3) 仍不能推出 \(D_0=D\)。它们分别隔离
公式 (1) 中不可删除的两个部分。

## 2. 容量内 residual 不能任意删去

取

\[
p=54481=7\cdot43\cdot181,\qquad r=2543533812.
\]

虽然 \(p\equiv1\pmod{24}\) 且这是 proper-root 高度，本例中的 \(p\) 是合数，故只是
边界控制。直接计算

\[
M=989411281,\qquad u=(2r+1,M)=4021,\qquad h=12063<p.
\]

令

\[
D_0=696191=743\cdot937,\qquad m=13,\qquad e=944,\qquad a=209.
\]

则 (3) 成立，且

\[
D_0\mid z,qquad D_0\mid K,qquad
D_0\equiv1-h=42419\pmod {54481}.
\tag{4}
\]

但实际 valuation 数据为

\[
z=2^4\cdot19\cdot421\cdot743\cdot937\cdot9232485580519,
\]

\[
K=2^4\cdot3\cdot5\cdot227\cdot743\cdot937\cdot1321\cdot4021
\cdot27241\cdot2041561.
\]

所以 \(2^4\)、\(743\) 和 \(937\) 都未超过 \(K\) 的对应容量，必须留在
\(\beta\)，而不是任选一个 \(D_0\) 的子因子。由 (1)，

\[
Q=73850652158571481,\qquad g_A=1,\qquad
D=11139056=16D_0.
\]

实际 \(D\) 仍整除 \(ph+1\)，但

\[
D\equiv24932\not\equiv42419\equiv1-h\pmod {54481}.
\tag{5}
\]

因此这个 shadow stutter 并不对应实际 stutter。

## 3. excess 后的归一化因子也不能删去

取另一个独立控制

\[
p=67,\qquad r=25311,\qquad M=1519,\qquad u=31,\qquad h=93.
\]

这里 \(p\) 是素数，但 \(p\not\equiv1\pmod {24}\) 且 \(h>p\)，同样不属于目标域。令

\[
D_0=779=19\cdot41,\qquad m=13,\qquad e=8,\qquad a=11.
\]

它再次满足 (2)--(3)。但

\[
z=2^3\cdot19\cdot41\cdot2442527,
\]

\[
K=2^2\cdot3\cdot5\cdot11\cdot17\cdot19\cdot31\cdot41\cdot941.
\]

此时 \(2^3\) 进入 \(Q\)，而 \(A\) 与 \(Q\) 仍有一个共同的 2 因子：

\[
Q=19540216,\qquad \beta=779,\qquad g_A=2,\qquad D=1558=2D_0.
\]

故虽然 \(D_0\equiv1-h\pmod {67}\)，实际 \(D\) 满足

\[
D\equiv17\not\equiv42\equiv1-h\pmod {67}.
\tag{6}
\]

这个控制表明，即使已正确识别 excess block，若省略 \(g_A=(A,Q)\)，仍会把非实际
除子误报为 stutter。

## 4. 结论与边界

两例分别对应 (1) 中的 \(\beta\) 和 \(g_A\) 机制。故任何试图关闭 proper-root
stutter 门的论证，必须从原始 \((R-h,K,A)\) 重建 (1) 的逐素数 canonical receipt；
仅对一个抽象 \(D_0\) 验证曲线、同余和 \(D_0\mid(z,K)\) 不足以进入 non-strict
gate。

这是一条证明路线的严格边界，不是核心素数上的反例：第一个控制缺少素数性，第二个
控制缺少核心同余与 proper-root 范围。它不构造 Type I/II 短证书、解提升或全局严格势；
核心素数 proper-root 的 actual stutter 门仍保持开放。

## 聚焦复现

```bash
python3 reproductions/type_i_root_capacity_stutter_actual_maximality_boundary.py --verify
```

脚本只重算两个固定整数图表、完整 valuation receipt 与一个 shadow divisor；不扫描
素数、根层或证书菜单。
