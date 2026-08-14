---
kind: claim
claim_id: type-II-q-one-canonical-root-default-entry-capacity-gap
title: q=1 规范根的默认入口容量缺口
statement: >-
  在当前 denominator-escape state contract 中，任何
  universal_raw_default_entry_v1 都从 A_0=1 且 3<=R_0<=p-2 的低图表开始。
  它的第一个 path-anchored complete-excess bundle 若非终端，写作
  R_0-1=Q beta，则 Q<R_0<p，故 canonical target 的 charged support 精确为
  M=lcm(1,Q)=Q<p。反之，对每个核心素数 p=24t+1，q=1 Type II G exit 的
  预声明 r=t canonical Type-I root 有 A=g(p^2t-g)>B_p=(p-1)^2/4>p，且
  R_root>p。因此当前默认入口本身及其首个 bundle 都不可能就是该 root 的
  persistent source；再结合 gcd((p+3)/4,K_root)=1，不能将 q=1 Type II
  carrier 重命名为该 source。这个结论只排除 current default-entry grammar 中的
  direct one-entry bridge：在不扩张该 grammar 的前提下，任何 handoff 都须在 fresh
  scope 中先构造一个真实的中间 charged-support lineage，并另行支付 terminal-first、
  typed reclassification 与全局 E5；它不排除多步桥或一个有独立准入证明的新 grammar。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-canonical-root-slice-support-disjointness
  - type-I-root-capacity-strict-carry-support-rebase
  - type-I-universal-p-source-capacity-anchor-orbit
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - type-I
  - root-entry
  - fresh-source-tree
  - charged-support
  - capacity-gap
  - source-provenance
  - E1
  - proof-boundary
sources:
  - claim: type-II-q-one-canonical-root-slice-support-disjointness
    role: canonical-root arithmetic and Type-II support disjointness
  - claim: type-I-root-capacity-strict-carry-support-rebase
    role: root support lower bound and high-R normal form
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: low-chart universal source and first complete-excess bundle
  - concept: denominator-escape-state-contract
    role: fresh default-entry and charged-support semantics
  - reproduction: reproductions/type_ii_q_one_canonical_root_entry_capacity_gap.py
    role: fixed low-entry and canonical-root arithmetic controls
visibility: public
last_checked: '2026-08-15'
---

# q=1 规范根的默认入口容量缺口

## 1. 问题的精确形状

令

\[
p=24t+1,
\qquad
X=\frac{p+3}{4},
\qquad
r=t.
\tag{1}
\]

前一张规范根卡已证明：这个选择没有任意 root 参数，且它的 actual proper-root
receipt 总有严格 carry。它也证明

\[
\gcd(X,K_{\rm root})=1.
\tag{2}
\]

式 (2) 排除了把 q=1 Type II endpoint 当前的物理 source support 直接继承为 root
support。但仍有一个看似可行的说法：也许可以从现有的 fresh default entry 出发，在第一个
complete-excess bundle 中直接获得 canonical root。这里给出它的精确否定。

本卡的结论仅针对当前已定义的 `universal_raw_default_entry_v1` grammar。它不限制以后
可能建立的多步 fresh-source bridge，也不把 contract-level no-go 误称为 Erdős--Straus
猜想的数学反例。

## 2. 默认入口的首个容量上界

现有 structured default entry 的 universal source 输入是一个低图表

\[
3\le R_0\le p-2,
\qquad
4K_0=pR_0+1,
\qquad
A_0=1.
\tag{3}
\]

它先实际到达 anchor \(\{1,R_0-1\}\)。若该 anchor 已终端，则没有 root handoff。
否则其第一个 path-anchored complete-excess receipt 写为

\[
R_0-1=Q\beta,
\tag{4}
\]

其中 \(Q\) 是所有超过 \(K_0\) 容量的完整素数幂块。特别地

\[
Q\mid R_0-1,
\qquad
1<Q\le R_0-1<p.
\tag{5}
\]

因为 default support 是 \(A_0=1\)，现有 complete-excess 规则强制首个 canonical
target 的 support 为

\[
M_1=\operatorname{lcm}(A_0,Q)=Q<p.
\tag{6}
\]

这一步不依赖 F/G 标签、factorization 的具体形状或 selector history；它只是 low-entry
range 和 maximal bundle 定义的直接结果。

## 3. 规范根的支撑严格在这个范围之外

规范 \(r=t\) root 的参数为

\[
g=\frac{p+1}{2},
\qquad
T=p^2t-g,
\qquad
A_{\rm root}=gT,
\tag{7}
\]

\[
K_{\rm root}=A_{\rm root}(p-1),
\qquad
4K_{\rm root}=pR_{\rm root}+1.
\tag{8}
\]

strict-root capacity estimate gives

\[
A_{\rm root}>B_p:=\frac{(p-1)^2}{4}.
\tag{9}
\]

Every core prime has \(p\ge73\), and

\[
(p-1)^2-4p=p^2-6p+1>0.
\tag{10}
\]

Thus

\[
\boxed{A_{\rm root}>B_p>p>M_1.}
\tag{11}
\]

The same root estimate gives \(R_{\rm root}>p\), whereas the entry state in (3) has
\(R_0<p\). Hence neither the default state itself nor the canonical target after its first
bundle can equal the root state: their `absorbed_support` fields already disagree by (11),
and their chart ranges disagree before any bundle.

## 4. Direct-entry no-go

Combining (2), (6), and (11) gives the promised admission boundary:

\[
\boxed{
\begin{array}{c}
\text{q=1 Type II G endpoint}\\
\text{+ current universal fresh default entry}\\
\text{+ its first complete-excess bundle}
\end{array}
\not\Longrightarrow
\begin{array}{c}
\text{canonical }r=t\text{ root as a persistent source.}
\end{array}}
\tag{12}
\]

The obstruction has two independent parts.

| Component | Exact fact | Consequence |
|---|---|---|
| Type II carrier | \(\gcd(X,K_{\rm root})=1\) | Current q=1 physical factors cannot be relabelled as root support. |
| Default entry | \(A_0=1\), \(R_0<p\) | The high root is not the entry state. |
| First bundle | \(M_1=Q<p\) | The first support update cannot reach \(A_{\rm root}>p\). |

Within the current default-entry grammar, a valid adapter needs at least one intermediate,
content-addressed charged state in `fresh_source_tree_only` scope before it can request the root
support. That intermediate must have an actual source/path receipt; defining it backwards from
\(A_{\rm root}\) would fall under the existing universal p-parent root-policy no-go. A genuinely
new root-entry grammar is not prohibited, but it would need its own independent admission proof.
Either route must still run terminal-first, recompute F/G/hit types, preserve the identity lift,
and place its actions in a global non-resetting well-founded phase.

## 5. What remains open

This boundary does **not** prove that every multi-step fresh-source ladder fails. Nor does it
provide the required intermediate lineage. Its value is narrower: it removes the direct
default-entry proposal from the search space and turns the next research object into a precise
one:

\[
\text{construct or rule out a target-independent fresh charged bridge from }A<p
\text{ to }A_{\rm root}>B_p.
\]

Any claimed solution of that object must exhibit the bridge's source policy, every actual raw
occurrence, typed state hashes, terminal-first misses, the full solution lift, and a global
potential. Without those fields, it remains `analysis_evidence` rather than a Type II--Type I
recursive edge.

## Focused reproduction

```bash
python3 reproductions/type_ii_q_one_canonical_root_entry_capacity_gap.py --verify
```

The script checks only three fixed core controls and two legal low-entry endpoints per control.
It recomputes (3)--(11), including the actual first complete-excess block for those endpoints.
It performs no prime-range, denominator-range, or selector-history scan.
