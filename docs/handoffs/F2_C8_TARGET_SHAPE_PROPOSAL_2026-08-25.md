# F2 C8 Target-Shape Proposal (2026-08-25)

> Proposal only. It is not a registry change and does not authorize queue
> mutation.

## Common Source Receipt

Every future C8 producer must consume a runtime-issued receipt containing:

```text
schema_id: f2_c8_actual_parent_receipt_v1
parent_state_id
parent_owner_digest
source_scope_digest
q_star_103_roughness_receipt
complete_terminal_first_receipt
parent_to_checkpoint_path
raw_occurrence_receipt
```

The receipt must bind to an already admitted parent. Nonempty strings,
`recursive_edge_eligible`, and caller-provided owner/family fields are not
substitutes for these fields.

## C8 OTHER Shape

For a real `C8-O3` input, construct the second-full-excess endpoint

\[
H=(p,R,8M;M),\qquad Q=\frac{R-1}{2},\qquad A_T=MQ,
\]

\[
c_T=\left\langle(4A_T)^{-1}\right\rangle_p,
\qquad K_T=A_Tc_T,
\qquad R_T=\frac{4K_T-1}{p}.
\]

The relative arithmetic theorem supplies

\[
75c_T\equiv64\pmod p,
\qquad 9\le c_T\le p-2,
\]

and, against the actual parent capacity \(p-1\), the proposed T5 `LOCAL_DROP`.
The target facts must be recomputed from \((p,A_T,K_T,R_T)\), never inherited
from the checkpoint. A nonterminal target has the proposed existing owner shape:

```text
major_phase: TYPEI
type_i_protocol: CHARGED
provenance_kind: OVERFLOW
is_overflow: true
atomic_arm: NONE
dispatch_status: NONE
support_A: A_T
chart_R: R_T
chart_K: K_T
```

This shape is not an E3 admission. The shared extractor, owner validator,
terminal classifier, and re-entry receipt must accept it independently.

## C8 DOUBLE_LOW Shape

For a source-bound O2 occurrence, the internal object is explicitly
nonpersistent:

```text
artifact_class: nonpersistent_atomic_serializer_input
must_never_enter_queue: true
parent_state_id
raw_occurrence_digest
Q_x, beta_x, Q_y, beta_y
canonical_support_A_T
canonical_chart_digest
```

Final output is exactly one of:

```text
AtomicTypedTerminalV1
AtomicTypedFSuccessorV1
AtomicTypedGSuccessorV1
REJECT_BEFORE_QUEUE
```

F/G labels must be recomputed from the target chart's complete \(K_T\)
factorization and may not be inherited from the source. The proposed persistent
projection is the existing `type_i_a_gt_one_overflow_residual` owner shape when
the proved support/capacity guards hold. This remains a proposal until E1/E3,
universal lift, T5 comparison, and selector re-entry are independently replayed.

## Explicit Non-Claims

This proposal does not assert that a C8 parent exists on either necessary ray,
that a complete terminal-first MISS exists, that a double-low occurrence exists,
or that any proposed target is currently admitted. It does not add a new family,
modify shared grammar, or close `GAP-O3-C8-OUTGOING`.
