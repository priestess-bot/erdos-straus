# F2 c8 / Atomic Cross-Audit

审查对象：`sol/f2-c8-atomic-closure` 的 `742cf58`、`916e349`、`14e1217`，审查时
HEAD 为 `14e1217`。本复核由 post-G/H4 track 完成，未调用
`f2_c8_*.py` 的 verifier 作为数学证明证据；只读取实现、claims、现有活动合同和既有
terminal evidence，并独立重算关键 c8 恒等式。

## Verdict

```text
C8_SECOND_FULL_EXCESS_ARITHMETIC = SOUND_RELATIVE_TO_ACTUAL_PARENT_AND_MISS
H4_C8_TARGET_OWNER_SHAPE = SOUND_RELATIVE_TO_SOURCE_SPECIFIC_GUARDS
ACTIVE_COMMON_E3_ADMISSION = NOT_ESTABLISHED
ATOMIC_TARGET_CLASSIFIER_TOTALITY = NOT_ESTABLISHED
C8_OUTGOING_TRACK_CLOSURE = BLOCKED
```

second-full-excess fallback 的数学构造是可保留的。它正确避免把 internal
(8\to c_T) capacity increase 当作 E5：应比较实际 parent 的 (p-1) 与 final
(9\le c_T\le p-2)。但当前代码和 receipts 仍把 caller-provided strings/booleans 封装成
actual parent、terminal miss、E1--E4 与 re-entry；因此不能作为 F1 common admission 或
`VERIFIED_SUCCESSOR` 的证据。

## Confirmed Mathematics

对 c8 normal form

\[
p=48s+1,\qquad K_H=8M,\qquad Q=\frac{R_H-1}{2},
\]

source-side gcd identities给 (Q) 为奇数且 ((M,Q)=1)。所以在 canonical
((1,2Q,1)) anchor，relative to (8M) 的 complete-excess block 正是 (Q)，余块为
(2)。这是 actual parent/path receipt 已经存在时的正确 E1 source occurrence，不依赖
double-low witness。

独立代数重算为

\[
32M\equiv1\pmod p,
\qquad
8Q\equiv75\pmod p,
\]

因此 final support (A_T=MQ) 的 capacity 满足

\[
4A_T\equiv\frac{75}{64}\pmod p,
\qquad
75c_T\equiv64\pmod p.
\]

对 (1\le c\le8)，(0<75c-64\le536<p)；而 (c=p-1) 会迫使
(p\mid139)。在 written (p\ge4129) domain，故

\[
\boxed{9\le c_T\le p-2.}
\]

若 parent 的 charged capacity 是 (p-1)，则 final target 的 N7 local tuple 严格下降；
checkpoint 的 (8\to c_T) 上升不能用于、也不需要用于 E5。这个 parent-to-final calculation
是正确的 relative macro theorem。

同样，H4/c8 atomic final target 若 source-specific guard 已给
(A_T>A_H>B_p\)、(c_T<C_P)，则 (A_T>1)、(R_T>p) 且 final target 的 F/G
只属于 certificate context。它应 re-enter existing
`type_i_a_gt_one_overflow_residual`，不需要新 F/G family。H4 (C=1) 仍须作为 Agent 2
downstream residual，Agent 3 receipt 对此保留正确。

## Findings

### Critical: Synthetic Common Admission

`reproductions/f2_c8_second_full_excess_parent_macro_v1.py` lines 149-234 and
`reproductions/f2_c8_atomic_common_admission_v1.py` lines 135-258 fabricate a sealed
terminal MISS and a `SUCCESSOR_RECEIPT` with `E1`--`E5` all set to `True`.

The only validation of evidence is nonempty strings. `ProducerRuleV1` is constructed locally,
not derived from the shared registry; the common gate therefore checks the new synthetic schema,
not a replay of an actual source receipt. This is exactly the forbidden inference

```text
caller-provided evidence / local producer rule != actual E1/E3 admission.
```

`AtomicPendingTargetV1.make_pending` has the same defect: lines 226-283 require only nonempty
parent/path tokens and an arbitrary (\mathbb N^7) tuple. `finalize_successor` accepts a boolean
`reentry_verified` at lines 441-463. Neither value is cryptographically or semantically bound to
an admitted parent trace.

This blocks E1, E3 and D8. The resulting accepted controls are contract fixtures, not actual
persistent successors.

### Critical: Fiber Classifier Has No Totality Proof

`reproductions/f2_c8_atomic_pending_target_v1.py` lines 292-345 rejects with
`FIBER_WORK_LIMIT` when either the bounded box or support subgroup exceeds 250,000 nodes. No
theorem bounds every actual H4/c8 target below that cutoff. Consequently it is not a total
terminal/F/G classifier on the claimed quantifier, even though its result is correct when it
finishes. A closure implementation needs an unbounded terminating finite procedure, or a proved
alternative certificate path for all over-limit targets.

### Major: Terminal-Preempted Control Can Be Admitted as MISS

The fallback control at `s=3279`, (p=157393), is correctly described in the new claim as
terminal-preempted. Existing active evidence gives

\[
\frac4{157393}=
\frac1{39375}+\frac1{57920624}+\frac1{2280624570000}.
\]

Nevertheless `parent_to_final_receipt(3279)` followed by `common_admission` manufactures
`outcome="MISS"` and accepts the target (`f2_c8_second_full_excess_parent_macro_v1.py`
lines 175-203 and 237-264). The formula control is legitimate, but it cannot also be a positive
common-admission control. A real dispatcher must replay the complete terminal policy first and
return the terminal for this fixture.

### Major: c8 Dispatch Does Not Establish Its Candidate Universe

`f2_c8_outgoing_trichotomy_v1.py` lines 62-114 chooses the least item from a caller-supplied
sequence of `DoubleLowReceipt`s. A receipt is qualified by booleans `e1_e5_verified` and
`common_reentry_verified`; primality, the actual raw occurrence, raw-prime threshold, target
serializer and complete candidate universe are not replayed. Omitting a candidate changes the
selected disposition. The fallback is mathematically available independently, so totality can be
recovered by always selecting it after a genuine terminal miss, but the stated deterministic
double-low precedence needs a complete, source-bound candidate enumeration or should be replaced
by unconditional fallback precedence.

### Major: H4 Source Owner Is Incompatible With the Fused Macro Proposal

`f2_c8_atomic_common_admission_v1.py` lines 47-58 declares the H4 source owner as
`type_i_c2_19_macro_target`. The paired Agent 1 reduction fuses H0--H4 as nonpersistent
checkpoints whose only persistent source is the q=1 d=1 receiver in
`type_i_full_carrier_post_g`. These cannot both be compiled into the same `ProducerRuleV1`.

Coordinator must choose one source protocol. If the fused macro is adopted, the H4 atomic
producer must bind the original parent plus full H0--H4 path receipt, not a standalone C2 target.

## Required Repair Before Integration

1. Replace all caller-supplied MISS/E1--E4/N7/re-entry values with sealed receipts replayed from
   an already admitted parent and the shared producer registry.
2. Remove the 250,000-node cutoff as a semantic rejection, or prove a total certificate method
   for every target crossing it.
3. Make terminal-first replay precede fallback construction; retain (p=157393) only as an
   arithmetic control that exits terminal.
4. Either provide a complete deterministic double-low candidate enumerator or select the universal
   second-full-excess fallback unconditionally after a real terminal miss.
5. Reconcile H4 source ownership with the parent-to-final fused macro before a shared grammar
   freeze.

Until these repairs, the correct integration label is

```text
C8_OTHER_ARITHMETIC_FALLBACK = ESTABLISHED_RELATIVE
H4_C8_ATOMIC_TARGET_REENTRY = CONDITIONAL_INTERFACE_PROPOSAL
GAP_O3_C8_OUTGOING = OPEN_AT_ACTIVE_SELECTOR_LEVEL
GAP_O1_ATOMIC_TARGET_CLOSURE = OPEN_AT_ACTIVE_SELECTOR_LEVEL
```
