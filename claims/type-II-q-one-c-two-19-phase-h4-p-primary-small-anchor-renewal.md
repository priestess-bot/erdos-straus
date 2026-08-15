---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
title: q=1 高 C=2 19 相位 H4 p-primary 残余的 overlap 小锚 renewal
statement: >-
  在 q=1 high C=2 19-phase 的 actual persistent H4 receipt 中，若 R4=1 (mod p)，令
  h=gcd(R4-1,K4)=2 gcd((p+1)/2,c3-s4)，则从 H4 universal p-source 的 anchor
  真实剥尽 R4-1 中的 p-block 后，再沿同一所选侧做完整容量剥离，实际到达
  {h,z=R4-h}。因此 2<=h|p+1。把 z 作相对于 K4 的完整超额分解 z=Q delta，并令
  D=gcd(z,K4)，则 D|ph+1、z>D、Q>1、h delta|K4、gcd(Q,h delta)=1，故 Q 是新的 path-anchored
  clean bundle。并且 p 不整除 Q 当且仅当 h<p+1；所以原 H4 p-free failure 在所有
  proper-overlap h<p+1 的情形重新得到 p-free receipt。令 M_alt=lcm(M4,Q)、
  c_alt 为 canonical capacity：若 c_alt<=p-2，则在既有 P=>H4 parent、terminal-first、
  typed 与 serializer guards 通过时可组成从 (0,p-1) 到 (0,c_alt) 的 strict macro；若
  c_alt=p-1，则目标精确进入完整乘积 d=1 top-capacity normal form。在纯局部 H4 contract
  中，唯一仍使 renewal 本身含 p-block 的情况是 h=p+1；后续的 phase-specific 前驱排除
  已证明该分支在此 actual 19-phase receipt 域为空。本卡不声称 top-capacity normal form
  已有全称 exit。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-p-free-p-block-provenance-obstruction
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - p-primary-peeling
  - complete-excess
  - small-anchor
  - p-free-renewal
  - capacity-map
  - guarded-macro
  - full-overlap-boundary
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-p-free-p-block-provenance-obstruction
    role: actual-p-primary-prefix-and-direct-p-free-rechart-no-go
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: exact-H4-overlap-and-height-bound
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: actual-capacity-peeling-and-clean-bundle-contract
  - claim: type-I-high-support-bundle-carry-capacity-terminal-dispatch
    role: canonical-high-support-target-and-E5-gate
  - concept: denominator-escape-state-contract
    role: persistent-E1-to-E5-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_p_primary_small_anchor_renewal.py
    role: exact-H4-local-small-anchor-renewal-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 p-primary 残余的 overlap 小锚 renewal

## 1. 形式删块以后仍有一条实际小锚路径

保留 H4 persistent receipt 的记号：

\[
K_4=M_4c_4,
\qquad
pR_4+1=4K_4,
\qquad
M_4>B_p=\frac{(p-1)^2}{4},
\qquad
1\le c_4\le p-2.
\tag{1}
\]

设

\[
R_4\equiv1\pmod p,
\qquad
R_4-1=p^eQ_0\beta,
\qquad
e\ge1,
\tag{2}
\]

其中 \(p^eQ_0\) 是相对于 \(K_4\) 的完整超额块，\((Q_0,\beta)=1\)。此前已经
证明，直接把 \(p^e\) 从该块删除所得的 \(Q_0\) 没有 clean E1 receipt；不能把
它登记为 rechart。

这里改为保留实际路径。因为 \(p\nmid R_4K_4\)，H4 universal \(p\)-source 实际到达
\(\{1,R_4-1\}\)。沿含 \(p\) 的一侧恰做 \(e\) 次 raw peeling 后得到

\[
y=Q_0\beta,
\qquad
x=R_4-y.
\tag{3}
\]

令

\[
h=(R_4-1,K_4).
\tag{4}
\]

由于 \(p\nmid K_4\)，(2)--(3) 给出

\[
(y,K_4)=(R_4-1,K_4)=h.
\tag{5}
\]

所以通用容量剥离定理不是形式替换，而是从 (3) 出发的一条实际 raw word，并把所选侧
恰好压到 \(h\)。记另一侧为

\[
z=R_4-h.
\tag{6}
\]

由 H4 exact overlap identity，

\[
\boxed{
h=2\left(\frac{p+1}{2},c_3-s_4\right),
\qquad
2\le h\mid p+1.
}
\tag{7}
\]

特别地，(3) 之后的真实 `competing-excess Reach` 已经不再是任意大的未知 anchor：
它至少有一条指定实际路径到 \(\{h,z\}\)，其中 \(h\le p+1\)。

## 2. 小锚上的新 clean bundle

首先 \(h\mid R_4-1\)，故

\[
(h,z)=(h,R_4-h)=1.
\tag{8}
\]

令

\[
D=(z,K_4).
\tag{9}
\]

由 \(4K_4=pz+(ph+1)\)，有精确整除约束

\[
\boxed{D\mid ph+1\le p^2+p+1.}
\tag{10}
\]

另一方面，H4 height bound 与 (7) 给出（\(p\ge73\)）

\[
z>\frac{p^3}{2}-\frac1p-(p+1)>p^2+p+1\ge D.
\tag{11}
\]

故 \(z\nmid K_4\)。把它按完整素数幂定义分解为

\[
z=Q\delta,
\qquad
Q=Q_{K_4}(z).
\tag{12}
\]

则

\[
Q>1,
\qquad
\delta\mid D,
\qquad
(Q,\delta)=1,
\qquad
(Q,h)=1.
\tag{13}
\]

由 (8)、(9)，\((h,D)=1\)。又 \(h\mid K_4\)、\(\delta\mid D\mid K_4\)，所以

\[
\boxed{h\delta\mid K_4.}
\tag{14}
\]

这正是 \(\{h,z\}\) 上所需的 residual-divisibility：从 H4 source、p-block raw
prefix 和容量 raw word 连起来，(12) 不是无来源的算术候选，而是一张新的
`path_anchored` clean complete-excess receipt；特别地，(13) 还给出
\((Q,h\delta)=1\)。

## 3. p-free 门只剩 full overlap

因为 \(p\nmid K_4\)，\(p\mid Q\) 当且仅当 \(p\mid z\)。由 \(R_4\equiv1\pmod p\)，

\[
p\mid z
\quad\Longleftrightarrow\quad
h\equiv1\pmod p.
\tag{15}
\]

但 (7) 给出 \(2\le h\le p+1\)，所以 (15) 精确化为

\[
\boxed{
p\mid Q
\quad\Longleftrightarrow\quad
h=p+1.
}
\tag{16}
\]

因此此前 \(R_4\equiv1\pmod p\) 的 p-free failure 现在分成两类：

| H4 overlap | 实际后继 bundle | 结论 |
|---|---|---|
| \(2\le h<p+1\) | \(Q\) p-free，且有 (14) | 合法 p-free renewal |
| \(h=p+1\) | \(p\mid Q\) | full-overlap root p-block boundary |

原本的形式 p-free chart \(\operatorname{lcm}(M_4,Q_0)\) 仍然不合法；这里的
renewal 使用的是先实际到达 \(\{h,z\}\) 后重新计算的 \(Q\)，二者不可混同。

## 4. 高支撑容量分派

现在设 \(h<p+1\)，并写

\[
M_{\rm alt}=\operatorname{lcm}(M_4,Q)=M_4L,
\qquad
c_{\rm alt}\equiv c_4L^{-1}\pmod p,
\qquad
1\le c_{\rm alt}\le p-1.
\tag{17}
\]

由 (12) 的完整超额性，\(Q\) 至少有一个素数幂超过 \(K_4\) 的容量，故该素数幂也超过
\(M_4\) 的容量；所以 \(L>1\)。式 (16) 又给出 \(p\nmid L\)，从而 (17) 是合法的
canonical high-support chart。

若

\[
c_{\rm alt}\le p-2,
\tag{18}
\]

则已有 \(P\Rightarrow H4\) persistent prefix 与本卡的实际 raw suffix 在
terminal-first、typed 与 serializer guards 均通过时可合成：E1 是 (3)--(14) 的路径和
bundle receipt，E2 是 (17)，E3 重新核验目标图表，E4 仍为 \(\operatorname{Sol}(p)\)
恒等提升，而

\[
\Lambda_p^\sharp(P)=(0,p-1)>(0,c_{\rm alt})
\tag{19}
\]

支付 E5。因此 (18) 是一条真正的 strict macro 出口。

若 \(c_{\rm alt}=p-1\)，则不应伪称 (19) 已支付。它精确转入 full-product \(d=1\)
normal form：

\[
n_{\rm alt}=\frac{4M_{\rm alt}+1}{p}>1,
\qquad
n_{\rm alt}\equiv1\pmod4,
\tag{20}
\]

\[
M_{\rm alt}=\frac{pn_{\rm alt}-1}{4},
\qquad
R_{\rm alt}=(p-1)n_{\rm alt}-1.
\tag{21}
\]

这是一个已明确命名的 top-capacity continuation，而不是新的无界 H4 p-free failure。

## 5. 边界

本卡没有排除 (21) 的 \(a=1\) p-primary continuation；局部控制甚至表明，proper
overlap \(h<p+1\) 与 \(c_{\rm alt}=p-1,a=1\) 在一般 H4 算术图表中可以同时发生。
在 actual 19-phase H3 predecessor 域中，后续的
[H4 full-overlap 实际前驱排除](type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion.md)
已消除 \(h=p+1\) root boundary。因此该域内 \(R_4\equiv1\pmod p\) 的残余已统一为
p-free clean renewal，唯一尚未关闭的接口是其 top-capacity continuation；它仍不是
G/Type I 全局出口定理。

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_p_primary_small_anchor_renewal.py --verify
```

回执重放三个满足 H4 局部高度、overlap 和 p-adic 条件的整数控制：proper-overlap
strict renewal、proper-overlap top-capacity \(a=1\) continuation，以及 full-overlap
p-block boundary。它们不是 actual 19-phase H3 ancestors。
