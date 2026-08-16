---
kind: claim
claim_id: type-I-high-anchor-automatic-q-phase-descent-trichotomy
title: automatic q 高锚来源的参数相位—递降三分法
statement: >-
  对互素 beta_0=2、Q_1=R-1 的 automatic C=qA 高锚来源，q 只能为 2 或 3。
  写 p=2A+b 或 p=3A+b，并令 k 为相应 b-k-u 参数。严格 q=2 来源的 root/bundle
  奇偶性强制 B 为奇、h=1 和 k 为偶；k 为奇、h=0 仅是不可实现的形式同余行。
  q=3 时 k=2,0,1 mod 3 分别强制 h=2,1,0。令 e=q-h-1；direct cofactor target
  的 canonical residual 精确满足 n_T=n+4Ae。因此所有实际 q=2 行与 q=3 的
  k=2 mod 3 行有 e=0 并保留 n_T=n，可作为既有 fixed-n 严格势递降桥的条件输入；
  q=3 的其余两类有 e>=1，强制 n_T>p，不能通过该 direct automatic-cofactor 路径
  提供题设所需的 n<p 递降；但其 automatic support qA 仍可在独立宏准入后提供严格的
  outer-rank state exit。该结论不建立
  terminal-first、parent、typed lift 或全局 selector edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-q2-minimal-phase-forcing
  - type-I-high-anchor-q2-bku-source-parameterization
  - type-I-high-anchor-q3-bku-source-parameterization
  - type-I-high-anchor-positive-phase-terminal-boundary
  - type-I-high-anchor-minimal-positive-phase-fixed-n-bridge
topics:
  - Erdos-Straus
  - type-I
  - high-anchor
  - automatic-q
  - phase
  - strict-descent
  - fixed-n
  - no-go
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_high_anchor_automatic_q_phase_descent_trichotomy.py
    role: exact-parameter-table-and-four-fresh-root-controls
visibility: public
last_checked: '2026-08-16'
---

# automatic \(q\) 高锚来源的参数相位—递降三分法

## 1. 范围

固定互素 two-anchor automatic 来源：

\[
p\equiv1\pmod {24},\qquad p<R<4A,\qquad
Q_0=A,\ \beta_0=2,\qquad Q_1=R-1,\ \beta_1=1,
\]

\[
(A,R-1)=1,\qquad M=A(R-1),\qquad C=qA<p.
\tag{1}
\]

high window 已强制 \(q\in\{2,3\}\)。令

\[
K=AB,\qquad r=M\bmod p,\qquad
K_T=rC,\qquad A_T=C=qA.
\tag{2}
\]

automatic congruence 给出 \(qr\equiv B\pmod p\)。因此有唯一的

\[
h={qr-B\over p},\qquad 0\le h<q.
\tag{3}
\]

这里讨论的只是 direct cofactor target 的算术；它尚未获得 global
terminal-first admission 或标记解提升。

## 2. 相位完全由 \(k\) 的小模类决定

对 \(q=2\)，既有 \(b\)-\(k\)-\(u\) 参数式给

\[
B\equiv k+1\pmod2.
\tag{4}
\]

由 (3) 和 \(p\equiv1\pmod2\)，得到

\[
h\equiv k+1\pmod2.
\tag{5}
\]

作为形式同余，偶数 \(k\) 给 \(h=1\)，奇数 \(k\) 给 \(h=0\)。但 (1) 的严格
two-anchor 输入还给出 \(A\equiv3\pmod4\)、\(R\equiv3\pmod8\)。因此

\[
K=\frac{pR+1}{4}\equiv1\pmod2,
\qquad A\equiv1\pmod2,
\qquad B=K/A\equiv1\pmod2.
\tag{5a}
\]

由 (3) 的相位式可知 \(h\equiv-B\equiv1\pmod2\)，故每一条**实际** \(q=2\)
来源都满足 \(h=1\)，并由 (4) 强制 \(k\) 为偶数。\(k\) 为奇的 \(h=0\) 行只保留为
脱离该来源域时的形式相位计算，不能作为本卡的 nonminimal source branch。精确证明见
[beta_0=2 两锚 automatic q=2 来源的最小相位强制](type-I-high-anchor-q2-minimal-phase-forcing.md)。

对 \(q=3\)，参数式给

\[
B\equiv k-1\pmod3,
\tag{6}
\]

故 (3) 给

\[
h\equiv1-k\pmod3.
\tag{7}
\]

所以 \(k\equiv2,0,1\pmod3\) 分别给 \(h=2,1,0\)。这不是经验筛选；
\(h\) 的范围使同余类成为精确值。

## 3. residual 三分法

写 anchor 与 target 的 complements 为

\[
d=p-B,\qquad d_T=p-r,\qquad
n=4A-R,\qquad n_T=4A_T-R_T.
\tag{8}
\]

令

\[
e=q-h-1.
\tag{9}
\]

从 \(qr=B+ph\) 直接得到

\[
q d_T=q(p-r)=d+pe.
\tag{10}
\]

两个 canonical determinant 恒等式为

\[
pn=4Ad+1,\qquad pn_T=4qA d_T+1.
\tag{11}
\]

代入 (10) 后有

\[
\boxed{\ n_T=n+4Ae.\ }
\tag{12}
\]

因为 \(0\le h<q\)，总有 \(e\ge0\)。若 \(e\ge1\)，则高锚
\(A>p/4\) 强制

\[
n_T\ge n+4A>p.
\tag{13}
\]

这条 direct target 已离开 \(0<n<p\) 的递降目标域。若 \(e=0\)，则
\(h=q-1\)、\(n_T=n\)，正是既有 minimal-positive-phase fixed-\(n\) bridge 的
算术输入；该桥仍以完整 terminal-first、E1--E4 receipt 为前提。

综合 (5)、(7)：

| \(q\) | \(k\) 的类 | \(h\) | \(e=q-h-1\) | direct target |
|---:|---:|---:|---:|---|
| 2 | \(0\pmod2\)（实际行强制） | 1 | 0 | 保留 \(n_T=n\)，条件性 fixed-\(n\) bridge |
| 3 | \(2\pmod3\) | 2 | 0 | 保留 \(n_T=n\)，条件性 fixed-\(n\) bridge |
| 3 | \(0\pmod3\) | 1 | 1 | \(n_T>p\) |
| 3 | \(1\pmod3\) | 0 | 2 | \(n_T>p\) |

因此 factor-source 研究不应把所有 automatic \(q\) 行视为候选**小分母**递降边。实际
\(q=2\) 行和表中的 \(q=3,e=0\) 类值得继续支付 parent、priority、typed lift 与
fixed-\(n\) bridge 的成本；\(q=3\) 的其余两类若要有题设所需的 \(n<p\) 出口，必须
使用不同的 terminal 或不同的小分母递降构造。它们并不缺少 direct macro 的 E5 支付：
automatic \(C=qA\) 的全相位 target 都有严格 outer-rank state exit，见
[automatic q 高锚的全相位仿射 target 与外层秩出口](type-I-high-anchor-automatic-q-affine-all-phase-exit.md)。

## 4. 固定控制

下表逐项重放 fresh root、two complete-excess、automatic cofactor 与 target chart：

| \(p\) | \(q\) | \(k\) | \(h\) | \(e\) | \(n\) | \(n_T\) |
|---:|---:|---:|---:|---:|---:|---:|
| 3793 | 2 | 80 | 1 | 0 | 233 | 233 |
| 60913 | 3 | 1088 | 2 | 0 | 2329 | 2329 |
| 41617 | 3 | 2041 | 0 | 2 | 393 | 88801 |
| 93481 | 3 | 2365 | 0 | 2 | 9489 | 219241 |

后两行是实际 fresh-root \(q=3\) automatic 来源，而非形式 chart；它们证明
\(C=3A\) 本身并不意味着可进入 \(n<p\) 的 fixed-\(n\) 递降。

## 5. 边界

本结论只关闭 current direct automatic-cofactor route 的非最小相位类。它不证明
这些素数没有短证书，也不排除另一种 support、external carrier 或 Type II 构造。
对表中两条 \(e=0\) 类，缺口仍是 global terminal-first dispatch、charged parent、
全域解提升与 E1--E5 admission，而不是第二段 fixed-\(n\) 势递降的算术。

## 聚焦验证

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_i_high_anchor_automatic_q_phase_descent_trichotomy.py --verify
~~~
