---
kind: claim
claim_id: type-I-g-anchor-c3-adaptive-core19-generalized-q-block-fixed-c
title: c=3 core-19 的广义 q 三段 raw 语言与 C=19^2 固定 RESET 候选
statement: 设 high-R chart 的 swapped canonical anchor 满足 q 与 KR 互素、c|K，且 R-1=q bQ1、(q-1)R+b=q aQ2、R-a=qcQ3。若每个 Qi 的素因子都是 R-unit，且对其相应 endpoint b、a、c 保留严格 K-capacity，则 side schedule q;Fac(Q1);q;Fac(Q2);q;Fac(Q3) 是到 (c,R-c,1) 的 actual primitive raw word。该统一 q=5 的既有 C=19 grammar。对 ambient core-19 ray，取 c=361、q=5、b=11246、a=386，三式同时成立当且仅当 v=1085244 (mod 20619541)；该子射线上 c|K，固定-c reset 落到 R=747。此构造仍是 conditional：需要 p 素性与具体 factor-reserve/unit gate，当前没有 terminal-free actual control，不能登记 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-adaptive-core19-c19-atomic-reset
  - type-I-overflow-a-one-dual-outer-rank-reset
  - type-I-g-anchor-c3-adaptive-core19-ambient19-terminal-screen
topics:
  - type-I
  - c3
  - core19
  - raw-source
  - factor-block
  - fixed-c
  - dual-reset
  - conditional-family
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_c3_adaptive_core19_generalized_q_block_fixed_c.py
    role: generalized q-block congruences and C=19^2 candidate ray
visibility: public
last_checked: '2026-08-07'
---

# 广义 q 三段 raw 语言与 C=19^2 候选

本卡把现有 `C=19` 的三个 \(5\)-block 提升为一个固定 \(c\) 的 raw language，
并给出第一个不只是 \(c=19\) 的明确核心-19 参数射线。它是条件性构造，不是
selector 覆盖定理。

## 1. 广义 q-block 引理

设

\[
pR+1=4K,\qquad (q,KR)=1,\qquad c\mid K,
\tag{1}
\]

其中 \(q\) 为素数。取正整数 \(a,b,Q_1,Q_2,Q_3\)，满足

\[
R-1=qbQ_1,
\qquad (q-1)R+b=qaQ_2,
\qquad R-a=qcQ_3.
\tag{2}
\]

对每个 \(Q_i\) 的素因子 \(\ell\)，要求它是 \(R\)-unit，并保留相应 endpoint
的 strict capacity：

\[
\begin{aligned}
\ell\mid Q_1&\Longrightarrow v_\ell(b)\ge v_\ell(K),\\
\ell\mid Q_2&\Longrightarrow v_\ell(a)\ge v_\ell(K),\\
\ell\mid Q_3&\Longrightarrow v_\ell(c)\ge v_\ell(K).
\end{aligned}
\tag{3}
\]

从 swapped anchor \((R-1,1,1)\) 出发，采用如下 side schedule：先在左侧做
\(q;\operatorname{Fac}(Q_1)\)，再在右侧做 \(q;\operatorname{Fac}(Q_2)\)，
最后在右侧做 \(q\)，然后在左侧做 \(\operatorname{Fac}(Q_3)\)。则它到达

\[
(c,R-c,1).
\tag{4}
\]

确实，第一段把 \(R-1\) 化到 \(b\)。第二个 \(q\)-step 后，互补坐标是

\[
R-\frac{R-b}{q}=\frac{(q-1)R+b}{q}=aQ_2,
\]

所以第二个 factor block 到达 \((a,R-a,1)\)。最后一个 \(q\)-step 的被除坐标为

\[
\frac{R-a}{q}=cQ_3,
\]

第三个 block 因而到达 (4)。式 (3) 是每一段末次剥离的容量条件；\(R\)-unit
条件和 \((q,KR)=1\) 给 unit condition，所有步骤都保持 \(m=1\)，故没有
gcd reduction。反向 replay 也强制 (2)--(3)，所以这给出指定 side topology 的
完整刻画。

一旦 (4) 是已解码 raw leaf，固定-\(c\) RESET 引理适用：令

\[
1\le\rho<4c,\qquad \rho p\equiv-1\pmod {4c},
\tag{5}
\]

则 r-side target 是

\[
\boxed{(R_\rho,K_\rho)=\left(\rho,\frac{\rho p+1}{4}\right).}
\tag{6}
\]

## 2. C=19^2 的条件性子射线

保留既有 ambient core-19 ray

\[
\begin{aligned}
p(v)&=181740263041+204127330680v,\\
R(v)&=787541139831+884551766280v.
\end{aligned}
\tag{7}
\]

在 (2) 中取

\[
q=5,\qquad c=361,\qquad b=11246,\qquad a=386.
\tag{8}
\]

前两个整除条件分别给

\[
v\equiv5pmod {5623},\qquad v\equiv5pmod {193},
\tag{9}
\]

而最后一个条件 \(R-a\equiv0pmod {5\cdot361}\) 给

\[
v\equiv2pmod {19}.
\tag{10}
\]

CRT 因而给出唯一 progression

\[
\boxed{v\equiv1085244pmod {20619541}.}
\tag{11}
\]

在这个 progression 上 \(h\equiv160pmod {361}\)。此时 \(26h+1\) 与
\(p-3\) 各含一个 \(19\) 因子，所以 \(361\mid K\)。同时

\[
747p\equiv-1pmod {1444},
\]

故 (6) 固定为

\[
\boxed{(R_\rho,K_\rho)=\left(747,\frac{747p+1}{4}\right).}
\tag{12}

第一个 parameter 的

\[
p=221528142596748961
=2579\cdot282413\cdot304153543
\tag{13}
\]

不是素数。相应 prime progression 与其步长互素，故包含无穷多素数值；但本卡没有
证明那些素数值满足全部 \(Q_i\) factor-reserve 和 unit gate，更没有找到
terminal-free actual control。因此 (11)--(12) 只定义下一条精确的候选构造路线。

在 v=5 的既有 q=5 三段 topology 中，第三段的 \(19\)-进容量已经饱和：它不能
直接提升到 \(c=361\)，也不能产生 \(c=38\) 或 \(722\)。这只是该 topology 的
局部障碍，不是所有 C=19^2 raw path 的 no-go。
