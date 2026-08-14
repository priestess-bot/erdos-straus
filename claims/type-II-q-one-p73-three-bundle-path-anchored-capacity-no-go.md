---
kind: claim
claim_id: type-II-q-one-p73-three-bundle-path-anchored-capacity-no-go
title: p=73 规范根三 bundle path-anchored 容量 no-go
statement: >-
  对 p=73、q=1 canonical root r=3，A_root=590150=2*5^2*11*29*37。
  在 current low universal_raw_default_entry grammar 中，若每个支撑更新都是单侧
  path_anchored complete-excess bundle，且每次都 canonical rechart，则从任一合法
  low default anchor 经至多三次 strict support-changing bundle 不可能得到 A_root。
  原因是单调 lcm 迫使每个中间 support 整除 A_root；精确枚举只留下五个首 bundle 与
  五个满足完整 receipt 门 (R-y)*beta|K、gcd(Q,(R-y)beta)=1 的第二 bundle，
  而它们没有一个第三 bundle 能满足同一门并使 lcm(A_2,Q_2)=A_root。
  这是一张 p=73 的有限 strict capacity map，排除最短的 single-side bundle ladder；
  它不排除 atomic split、overflow determinant、更多 bundle，或有独立 E1 admission
  的新 source grammar。
claim_status: computationally_reproduced
proof_provenance: computational_reproduction
review_status: internal_review
depends_on:
  - type-II-q-one-canonical-root-default-entry-capacity-gap
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - type-I
  - p73
  - root-entry
  - complete-excess
  - path-anchored
  - capacity-ladder
  - E1
  - counterexample
sources:
  - claim: type-II-q-one-canonical-root-default-entry-capacity-gap
    role: current-entry two-update capacity lower bound
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: complete-excess receipt and lcm support semantics
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: distinction from the excluded atomic-split grammar
  - concept: denominator-escape-state-contract
    role: source-tree and single-side bundle admission conditions
  - reproduction: reproductions/type_ii_q_one_p73_three_bundle_path_anchored_no_go.py
    role: exact finite capacity enumeration
visibility: public
last_checked: '2026-08-15'
---

# p=73 规范根三 bundle path-anchored 容量 no-go

## 1. Scope

Fix the smallest core control

\[
p=73,
t=r=3,
A_{\rm root}=590150=2\cdot5^2\cdot11\cdot29\cdot37.
\tag{1}
\]

The preceding capacity map proves that a low default entry cannot reach this root in one or two
support-changing primitives. This card asks the first remaining numerical possibility, but only
in the existing **single-side** `path_anchored complete_excess_bundle` grammar. Atomic split,
determinant, reset, and new root-entry grammars are deliberately outside scope.

At a primitive bottom node \(\{R-y,y\}\), write the selected side as

\[
y=Q\beta,
Q=\prod_{v_q(y)>v_q(K)}q^{v_q(y)}.
\tag{2}
\]

For a single-side path-anchored receipt, the complete-excess contract requires in particular

\[
\boxed{(R-y)\beta\mid K,\ (Q,(R-y)\beta)=1,\ Q\nmid K.}
\tag{3}
\]

The next charged support is \(\operatorname{lcm}(A,Q)\). If a monotone lcm ladder ends in
\(A_{\rm root}\), every intermediate support must divide (1), making the control finite.

## 2. The only admissible first and second bundles

Among all legal low default anchors \(3\le R_0\le71\), the first path-anchored receipts whose
support can still divide (1) are exactly

\[
\begin{array}{c|c|c|c|c}
R_0&K_0&Q_0&\beta_0&A_1\\ \hline
3&55&2&1&2\\
11&201&10&1&10\\
23&420&11&2&11\\
51&931&50&1&50\\
59&1077&58&1&58.
\end{array}
\tag{4}
\]

Canonical rechart after each row, followed by an exhaustive check of every primitive side
\(1\le y<R_1\) satisfying (3), leaves exactly these five strict second bundles that retain the
possibility of reaching (1):

\[
\begin{array}{c|c|c|c|c|c|c}
R_0&A_1&R_1&K_1&y_1&(Q_1,\beta_1)&A_2\\ \hline
3&2&7&128&5&(5,1)&10\\
11&10&23&420&11&(11,1)&110\\
11&10&23&420&22&(11,2)&110\\
23&11&3&55&2&(2,1)&22\\
51&50&63&1150&58&(29,2)&1450.
\end{array}
\tag{5}
\]

For example, the tempting \(R_1=143\), \(y=111\), \(Q=37\) capacity occurrence has
\(\beta=3\), but

\[
(143-111)\beta=96\nmid2610.
\tag{6}
\]

So it is not a path-anchored bundle, even though it is a primitive raw node and its bare lcm
would look favorable. This is the exact field that a capacity-only search omits.

## 3. Exhaustion of the third bundle

For each row of (5), rechart canonically and test every primitive side \(y_2\). The verifier
requires the full receipt gate (3), strict support growth, and

\[
\operatorname{lcm}(A_2,Q_2)=590150.
\tag{7}
\]

The resulting set is empty. Therefore

\[
\boxed{
\begin{array}{c}
\text{low default entry}\\
\xrightarrow{\text{single-side path-anchored bundle}}A_1\\
\xrightarrow{\text{single-side path-anchored bundle}}A_2\\
\xrightarrow{\text{single-side path-anchored bundle}}A_{\rm root}
\end{array}
\text{does not exist for }p=73.}
\tag{8}
\]

This is stronger than a source-path miss: the enumeration gives every bottom side the benefit of
the doubt, so an actual raw path cannot restore a candidate which already fails (3).

## 4. Boundary

Equation (8) does not establish a global descent theorem. It says that the first support length
compatible with the size bound is still insufficient for the most natural existing bundle
grammar at the base control. A future q=1 handoff must use at least one of:

1. a longer single-side receipt ladder;
2. the separately governed atomic-split grammar;
3. an overflow determinant bridge; or
4. a new target-independent source grammar with its own E1/E3 admission proof.

None of these alternatives can be replaced by a bare factorization or by a target-derived raw
parent. Terminal-first, typed reclassification, the global solution lift, and a non-resetting
well-founded phase remain unproved.

## Focused reproduction

```bash
python3 reproductions/type_ii_q_one_p73_three_bundle_path_anchored_no_go.py --verify
```

The script performs exact finite enumeration for one prime, its legal low anchors, and the
resulting canonical bottom-node charts. It does not scan primes, denominators, or selector
histories.
