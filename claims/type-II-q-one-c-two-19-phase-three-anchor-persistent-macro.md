---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
title: q=1 高 C=2 的 19 相位三 p-anchor persistent 宏出口
statement: >-
  设 ordinary q=1 full-carrier 的 persistent d=1 receiver 进入唯一的 c=2、
  p=912u+769 19 相位，并且 receiver 与三个中间 canonical 图表均未被 terminal-first
  或更高优先级出口抢占。已有 q=1 p-free relay 从 receiver P 严格到达 H_0；随后将
  H_0,H_1,H_2 的三个 p-anchor complete-excess action 作为同一宏内 checkpoint，
  得到 H_3。三段均有实际 source/path、唯一 complete-excess block 和 p-free
  canonical target；终点 capacity 为 c_3=(1536+a(p)p)/2261，且总有
  1<=c_3<=p-2。因而从 P 到 H_3 的组合宏满足 E1--E5、以 Sol(p) 恒等提升，并在
  Lambda_p^sharp=(floor(B_p/A),K/A) 下严格由 (0,p-1) 降到 (0,c_3)。这把此前
  chart-local 的三 p-anchor 链升级为 q=1 persistent image 上一条可提升的固定长度
  strict relay；它仍不解决 H_3 的后续 terminal/selector，也不证明全局退出。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
  - type-II-q-one-c-two-19-phase-p-anchor-capacity-expansion
  - type-II-q-one-c-two-19-phase-second-p-anchor-capacity-expansion
  - type-II-q-one-c-two-19-phase-third-p-anchor-finite-capacity-split
  - type-I-high-support-bundle-carry-capacity-terminal-dispatch
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - high-support
  - nineteen-phase
  - p-anchor
  - complete-excess
  - persistent-macro
  - solution-lift
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-d-one-p-free-gate-exclusion-relay
    role: persistent-receiver-to-h-zero-receipt
  - claim: type-II-q-one-c-two-19-phase-p-anchor-capacity-expansion
    role: first-internal-anchor-receipt
  - claim: type-II-q-one-c-two-19-phase-second-p-anchor-capacity-expansion
    role: second-internal-anchor-receipt
  - claim: type-II-q-one-c-two-19-phase-third-p-anchor-finite-capacity-split
    role: third-internal-anchor-receipt-and-c-three-selector
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_three_anchor_persistent_macro.py
    role: exact-composed-carrier-and-endpoint-potential-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的三 p-anchor persistent 宏出口

## 1. Why the macro starts before the capacity-two target

Let \(P\) be the persistent immediate \(d=1\) receiver in the unique
q=1 capacity-two phase.  Its charged support, residual, and capacity are

\[
A_P=\frac{(p-1)(2p+1)}4,
\qquad
R_P=p(2p-3),
\qquad
K_P=A_P(p-1).
\tag{1}
\]

Thus \(A_P>B_p=(p-1)^2/4\) and

\[
\Lambda_p^\sharp(P)=(0,p-1).
\tag{2}
\]

The receiver's raw \(p\)-source is not primitive because \(p\mid R_P\).
This is exactly why the preceding q=1 relay uses its named least-coprime
source repair.  Conditional on terminal-first not returning a certificate,
that relay already supplies a persistent, E1--E5, p-free path from \(P\) to
the capacity-two high chart

\[
H_0=(p,R_0,K_0;M_0,\sigma),
\tag{3}
\]

where

\[
\begin{aligned}
F&=2p^2-3p-1,\\
M_0&=A_P\frac F2=\frac{(p-1)(2p+1)F}{8},\\
K_0&=2M_0,\\
R_0&=4p^3-8p^2-p+4.
\end{aligned}
\tag{4}
\]

The three subsequent p-anchor moves must not be entered one at a time: their
first two capacity changes rise.  Instead, they are a fixed, finite internal
word attached to the already persistent \(P\).  This is the same
``internal checkpoint, endpoint E5'' discipline used by high-anchor macro
admission; it does not register a rising checkpoint as a recursive edge.

## 2. The fixed internal word

For \(i=0,1,2\), write

\[
Q_i=\frac{R_i-1}{2},
\qquad
M_{i+1}=M_iQ_i,
\qquad
K_i=M_ic_i,
\qquad
R_i=\frac{4K_i-1}{p},
\tag{5}
\]

with

\[
c_0=2,
\qquad
c_1=\frac{2p+4}{3},
\qquad
c_2=\frac{13p+16}{19},
\tag{6}
\]

and

\[
c_3=\frac{1536+a(p)p}{2261},
\qquad
a(p)p\equiv-1536\pmod {2261},
\quad 1\le a(p)\le2260.
\tag{7}
\]

The three preceding p-anchor results prove, respectively,

\[
\gcd(R_i-1,K_i)=2,
\qquad
(Q_i,M_i)=1,
\qquad
p\nmid Q_i
\quad (i=0,1,2).
\tag{8}
\]

Their high-chart raw source gates are also explicit:

\[
R_0\equiv4,
\qquad
R_1\equiv\frac{25}{6},
\qquad
R_2\equiv\frac{3173}{912}pmod p.
\tag{9}
\]

All three residues are nonzero for this phase.  Hence each internal line has
an actual universal \(p\)-source, a one-step raw path to its anchor, and a
unique p-free complete-excess bundle.  Let

\[
H_i=(p,R_i,K_i;M_i,\sigma)quad(0\le i\le3).
\tag{10}
\]

The composed action is the fixed word

\[
\boxed{P\Longrightarrow H_0\Longrightarrow H_1
\Longrightarrow H_2\Longrightarrow H_3.}
\tag{11}
\]

Only \(P\) and \(H_3\) are macro endpoints.  The first arrow is the
already charged q=1 relay; the remaining arrows are not separately queued.

## 3. Endpoint E5 is strictly paid

The selector in (7) always gives \(c_3<p\).  It cannot equal \(p-1\): if
it did, (7) and the capacity congruence would force

\[
p\mid2261+1536=3797.
\tag{12}
\]

But the only positive prime divisor is \(3797\), and
\(3797\not\equiv769\pmod {912}\).  Therefore

\[
\boxed{1\le c_3\le p-2.}
\tag{13}
\]

Moreover \(M_3>M_0>p^2>B_p\), so both endpoints of (11) are high-support
states.  Their endpoint ranks are exactly

\[
\Lambda_p^\sharp(P)=(0,p-1),
\qquad
\Lambda_p^\sharp(H_3)=(0,c_3).
\tag{14}
\]

Equation (13) makes (14) a strict lexicographic decrease.  It is important
that this compares the actual persistent receiver with the final target,
not either of the two rising intermediate capacities.

## 4. E1--E5 composition

The macro is selected only after the versioned terminal/alternate prefix has
been evaluated on \(P,H_0,H_1,H_2\).  A terminal output preempts (11); if
all four checks miss, its receipt is:

| Check | Receipt |
|---|---|
| E1 | The q=1 receiver has its persistent parent and named least-coprime source from the preceding relay.  Each \(H_i\), \(i=0,1,2\), replays the high-chart universal \(p\)-source, anchor and complete-excess data in (8)--(9). |
| E2 | Equations (4)--(7) recompute all lcm carriers, canonical determinants, positive high targets and \(M_3\mid K_3\). |
| E3 | A macro receipt binds the existing \(P\to H_0\) digest, the three p-anchor bundle payloads, all five content-addressed typed charts, and the unchanged scope \(\sigma\).  Each chart is independently reclassified rather than inheriting F/G/hit data. |
| E4 | Every chart has equation target \(4/p\) and uses \(W=\operatorname{Sol}(p)\); the lift \(H_3\to P\) is the identity. |
| E5 | The endpoint calculation (14) is strict. |

Thus the macro can place \(H_3\) in the selector's pending-dispatch domain
without treating \(H_0,H_1,H_2\) as standalone edges.  The 64/32 split for
\(c_3-c_2\) remains useful for the next selector decision, but is not needed
to pay this macro's endpoint descent.

This gives a real, fixed-length strict relay on the q=1 capacity-two image.
It does not yet supply a terminal certificate or a successor from \(H_3\),
so it does not complete the global G/Type I exit theorem.

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_three_anchor_persistent_macro.py --verify
```
