# T6 q=1 Exact-HEAD Source Replay Candidate Review

Date: 2026-08-27

Reviewed files:

- data/t6-wave1/t6-coordinator-role-registry-v6.json
- schemas/t6-coordinator-role-registry-v6.schema.json
- schemas/t6-q-one-exact-head-source-input-v1.schema.json
- scripts/t6_coordinator_role_registry_v6.py
- scripts/t6_q_one_exact_head_source_input_v1.py
- scripts/t6_q_one_exact_head_source_input_orchestrator_v1.py
- scripts/t6_q_one_exact_head_source_input_receipt_replayer_v1.py
- tests/test_t6_q_one_exact_head_source_input_v1.py

## Initial Rejection

The first implementation allowed a public binder to accept caller-supplied,
self-sealed V3--V6 maps and emit three true source-evidence markers. Even
though its controlled orchestrator and replayer rejected forged chains, that
public path was an authority bypass and was rejected.

## Accepted Revision

The revised implementation is accepted only after a safe downgrade:

1. Every serializable source-input wire fixes all three source-evidence
   markers to false.
2. Generic/successor E1, producer, admission, queue, E2--E5, T5, re-entry,
   and global markers are also false.
3. The source-input schema is closed-world, with full dataclass
   required/properties parity.
4. Public parsing and public V2 projection reject candidate wires.
5. Exact-HEAD success is reported solely as the independent replayer's
   runtime result, not as a serializable grant.

The isolated fixture verifies p=1201 candidate wire reconstruction; it rejects
authority tampering, V3 terminal-first preemption, schema extras, and
worktree drift. Ruff and compilation pass.

## Verdict

~~~text
ACCEPT for REPLAY_CANDIDATE_ONLY_NO_SERIALIZED_SOURCE_AUTHORITY.
NOT source authentication, E1, owner, admission, queue, or successor authority.
~~~

Any future consumer needing source actualness must independently invoke the
exact-HEAD replayer and must not trust the replay-candidate wire alone.
