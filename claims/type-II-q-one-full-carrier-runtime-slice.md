---
kind: claim
claim_id: type-II-q-one-full-carrier-runtime-slice
title: q=1 initial G 到第二-anchor final target 的 runtime slice
statement: >-
  A deterministic runtime slice now executes the actual q=1 initializer
  branch for every core prime: a gap-3 Type II terminal is returned when
  X=(p+3)/4 has a 2 modulo 3 factor, and a proved gap-7 terminal preempts
  the p=265 modulo 336 odd-low class after that miss. Otherwise a
  content-addressed q=1 G endpoint is bootstrapped and the common runtime
  issues the full-carrier PHASE_DROP followed by the root-to-second-anchor
  final macro. Each
  persistent transition replays source identity, a versioned terminal scope,
  independent projection/validation, common owner classification and N7
  ticket. The final target is intentionally left without a dispatch route;
  its verified DEAD_END control demonstrates that this is a producer slice,
  not post-G totality, F2 closure or T6 closure.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-initial-q-one-root-terminal-or-full-carrier-dispatch
  - type-II-q-one-full-carrier-phase-root-entry
  - type-II-q-one-full-carrier-root-second-anchor-contraction
  - type-II-q-one-odd-low-final-gap-seven-preemption
  - t6-persistent-selector-runtime-v1
  - t6-persistent-selector-state-v1
topics:
  - type-II
  - q-one
  - runtime
  - full-carrier
  - terminal-first
  - E1
  - E5
  - T6
  - proof-boundary
sources:
  - reproduction: scripts/t6_q_one_full_carrier_runtime_slice_v1.py
    role: complete runtime slice, terminal serializers and negative final-reentry control
  - claim: type-II-q-one-full-carrier-root-second-anchor-contraction
    role: final macro target and root-to-final T5 ticket
visibility: public
last_checked: '2026-08-25'
---

# q=1 full-carrier runtime slice

## 1. Exact scope

This card closes a concrete runtime binding for one source chain. It does not
claim that the resulting final target has a total successor.

For every core prime \(p\), let

\[
X=\frac{p+3}{4}.
\tag{1}
\]

The initializer first runs the complete gap-3 direct Type I/II predicate.
If a least prime \(\ell\mid X\) satisfies \(\ell\equiv2\pmod3\), it
returns the directly verified Type II terminal

\[
\frac4p=
\frac1X+
\frac1{p(X+\ell)/3}+
\frac1{p(X+X^2/\ell)/3}.
\tag{2}
\]

After its gap-3 miss, it also runs the proved odd-low preemption: when
\(p\equiv265\pmod {336}\), the gap-7 divisor \(d=2\) gives a direct Type
II terminal. Only after both named checks miss does it emit the q=1 G state.

Otherwise it emits the content-addressed ordinary \(q=1\) G state with
`ROOT_SOL`, `TYPEII_G_HANDOFF`, and the declared gap-3 MISS receipt. This
is a genuine initializer queue item, not a synthetic test fixture.

## 2. Runtime path

The executable registry has exactly the following two nonterminal routes:

\[
\begin{array}{rcl}
\texttt{type_ii_relation_g_endpoint}
&\xrightarrow{\texttt{q_one_g_full_carrier_runtime_v1}}&
\texttt{type_i_full_carrier_post_g},\\
\texttt{type_i_full_carrier_post_g}
&\xrightarrow{\texttt{q_one_root_second_anchor_runtime_v1}}&
\texttt{overflow}\ \text{or}\ \texttt{marked_absorb}.
\end{array}
\tag{3}
\]

The first route projects the target-independent full-carrier root. The
second route uses the checkpoint contraction, so its first child and
second-anchor high determinant remain inside the witness payload and never
become persistent queue states.

The runtime independently performs these ordered terminal checks:

1. gap-3, then the \(265\pmod {336}\) gap-7 preemption, at the initial endpoint;
2. direct anchor-sink terminal on the full-carrier root;
3. direct anchor-sink terminal on the macro-internal first child;
4. direct anchor-sink terminal on the final target.

An anchor-sink hit is not a boolean label. For a chart
\(4K=pR+1\) with \(R-1\mid K\), it serializes

\[
\left\{\frac K{R-1},K,pK\right\},
\tag{4}
\]

whose reciprocal sum is exactly \(4/p\). A MISS is only claimed for this
named anchor-sink scope; it is not a claim that all possible terminal
families have been exhausted.

## 3. E1--E5 binding

For each route in (3), the shared runtime, rather than the candidate,
creates the source/target transition receipt. It checks:

- the admitted source `state_id` and recomputed owner digest;
- the route's source terminal MISS;
- a runtime-issued one-use candidate with no owner/family authority fields;
- a separate projector and transition validator for E1--E4;
- target terminal priority before queue mutation;
- common state-contract owner classification and an independently recomputed
  N7 ticket.

The macro witness additionally seals the first-child anchor MISS and the
full nonpersistent checkpoint arithmetic. Thus its final receipt is tied to
the actual runtime parent, not merely to a bare prime or a chart formula.

For \(p=73\), the final target is the overflow

\[
(R,K;A)=(231,4216;62)
\tag{5}
\]

with `LOCAL_DROP`. The \(p=601\) odd-low control is now preempted at gap 7.
For \(p=1033\), the local slice instead reaches the low chart

\[
(R,K;A)=(247,63788;862)
\tag{6}
\]

with `TYPEI/ABSORB`, cursor \((1,246,1)\), and `PHASE_DROP`. These are
not numerical-only controls: both paths are executed through the shared
queue and state classifier.

## 4. Deliberate final boundary

The final owner has no registered dispatch route in this slice. Calling the
runtime on that state returns `DEAD_END` without queue mutation. This is a
required negative control:

\[
\boxed{\texttt{Q1\_RUNTIME\_SLICE} \ne \texttt{T6\_TOTALITY}.}
\tag{7}
\]

The slice also does not add a persistent `AtomicPending` state or declare a
new global T2 arm. Its checkpoint disposition is local to this unregistered
macro configuration and must be reviewed again before any shared Gate-3
producer registry adopts it.

Consequently the retained conclusion is only:

```text
q1 initializer -> q1 G -> full-carrier root -> final checkpoint macro
is executable with common runtime receipts;
final target re-entry = OPEN.
```

It does not prove the post-G selector total, F1 reachable-state exhaustion,
F2, T6, or the Erdős--Straus conjecture.
