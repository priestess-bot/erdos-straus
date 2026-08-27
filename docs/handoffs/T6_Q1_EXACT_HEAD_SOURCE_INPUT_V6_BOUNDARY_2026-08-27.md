# T6 q=1 Exact-HEAD Source Input V6 Boundary

Date: 2026-08-27

## Purpose

The implemented V2 prestate accepts only an explicitly non-E1 external source
binding. The next narrow problem is to bind that shell to the actual V5/V6
source chain at one reviewed exact HEAD, without relabeling it as generic E1
or admitting anything to a queue.

This document freezes the contract for that bridge. It is not a V6 authority
implementation and does not change any T6 status.

## Existing Evidence

V5 conditionally establishes, under the reviewed repository-selected exact
commit trust condition:

~~~text
V1 ROOT_INITIALIZER_OUTPUT state
v1_state_id and full v1_state_wire_digest
source owner type_ii_relation_g_endpoint
persistent_admission=true, queue/enqueue=false
~~~

V6 conditionally and pointwise rebinds the V4 root occurrence to that V5 V1
source. It recomputes the V1 source owner, both V1 digest domains, source
potential, V3 prefix scope, and the V4/V5 source map. Its output remains
DERIVED_WITNESS_NOT_V1_STATE_PATH and all generic/successor E1 authority
bits are false.

V6 still lacks an exact-HEAD registry, resolver, controlled orchestrator,
independent post-issuance replayer, and an external trust binding for its role.

## Required Wrapper

The proposed wrapper is:

~~~text
ExactHeadQOneActualSourceInputV1
scope = EXACT_HEAD_Q1_ROOT_SOURCE_INPUT_SCOPED_NOT_GENERIC_E1
~~~

It contains all of the following:

~~~text
external_binding_id / digest
head_sha / head_tree_sha
V3, V4, V5, V6 registry IDs, resolved digests, role-manifest digests
V3 prefix-MISS receipt ID / digest
V4 consumer, owner, and scope receipt IDs / digests
V5 base-admission and materialization receipt IDs / digests
V6 rebind receipt ID / digest
V2 source state ID / digest
V1 source state ID
V1 state-ID suffix digest
V1 full state-wire digest
V1 owner ID / digest and source facts digest
source-rebind-map digest and semantic-origin-exclusion digest
scope ID, coverage semantics, ordered gaps [3,7,11],
next_unchecked_gap=15, global_exhaustion=false
~~~

The V1 state-ID suffix digest and the full V1 state-wire digest are distinct
domains and must never be substituted for one another.

The exact binder must recreate the four fields consumed by the existing
zero-authority V2 shell:

~~~text
v1_source_state_id              = V6.v1_source_state_id
v1_source_wire_digest           = V6.v1_state_wire_digest
source_prefix_receipt_digest    = V6.v3_terminal_receipt_digest
source_phase_root_preimage_digest =
  hash(V4/V5/V6 source map, semantic-origin exclusion, exact HEAD)
~~~

It must recreate them rather than accept an existing caller-supplied shell.

## Required Order

~~~text
V3 exact-HEAD replay
-> V4 exact-HEAD replay
-> V5 exact-HEAD replay
-> V6 exact-HEAD replay
-> ExactHeadQOneActualSourceInputV1
-> zero-authority ExternalQOneSourceBindingV2 projection
-> P/C/L/D/A/Q prestate
~~~

The V6 orchestrator may accept only repository locator, full requested HEAD,
raw q=1 input, and the V3 production result. It must fresh-load all
V3/V4/V5/V6 resolvers from the same Git tree. It must reject caller grants,
registry pins, V4/V5 receipts, state wires, and authority booleans. An
independent replayer must rebuild the exact source-input wire without calling
the orchestrator or issuer.

## Authority Boundary

An accepted exact source-input wrapper may establish only:

~~~text
source_actualness_input=true
v1_base_admission_evidence=true
v6_rebind_evidence=true
~~~

It must keep all of these false:

~~~text
generic_e1, successor_e1, e1_authority
producer, branch, admission, queue
E2, E3, E4, E5, T5, re-entry
global_exhaustion
~~~

The reason is structural: V3/V4/V5/V6 establish only the finite registered
prefix MISS, while the generic structured E1 contract requires
MISS_COMPLETE. The wrapper authenticates source input for a future
phase-root-specific path; it does not create a normal successor transition.

## Exact Next Claim

The next implementation claim must prove:

\[
\operatorname{Valid}_{H}(\mathrm{V3,V4,V5,V6})
\Longrightarrow
\exists!\,\mathrm{ExactHeadQOneActualSourceInputV1},
\]

subject to the existing reviewed selected-commit trust condition. It must
state explicitly that the conclusion is source authentication only and not
generic E1.
