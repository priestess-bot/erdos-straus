# SP-05 standalone type and byte contracts

## Canonical JSON bytes

`Canon(v)` is the ASCII byte string produced by:

```python
json.dumps(
    v,
    sort_keys=True,
    separators=(",", ":"),
    ensure_ascii=True,
    allow_nan=False,
).encode("ascii")
```

Object keys are unique strings. Integer fields require `type(v) is int`; booleans are rejected as integers. A seal is the lowercase SHA-256 hex digest of the canonical unsigned object. State/projection IDs use a type prefix plus this digest.

## Input types

`RootSourceWire` is the exact public `PersistentSelectorStateV1` field set mirrored in `sp05_contract.py`, with root facts, `relation_q=1`, `root_context=p`, and a canonical state ID.

`CanonicalPhaseRootProjectionV2` contains exactly the source-bound `p,t,X`, frozen `R,K`, ROOT_SOL mark, target facts, projection ID, and fixed no-caller-tie-break rule.

`ExternalActualnessAuthority` is not constructible by this package. A production implementation must fresh-resolve an immutable/signed commit trust anchor and replay the exact V5/V6/V7 source chain. Caller-provided IDs, digests or authority booleans are insufficient.

## Terminal outputs

`PrefixResult` is either:

```text
HIT {gap_index, divisor_index, kind_index, certificate, ...}
MISS_REGISTERED_PRIORITY_COMPLETE {ordered_gaps, checks, global_exhaustion=false}
```

`GlobalResult` is either:

```text
HIT {x_index, x_bounds, reduced_residual, factor_pair, certificate, ...}
MISS_COMPLETE {x_bounds, x_positions, factor_pairs_checked,
               coverage_identity, global_exhaustion=true}
```

`SP05CompleteTerminalDecisionV1` binds one exact subject and contains:

```text
receipt_type, schema_version, head_sha,
schedule_id, schedule_semantics,
subject_kind, subject_id, subject_digest,
source_state_id, source_state_digest,
projection_id, projection_digest,
p, ordinary_q1_g,
prefix_result, global_result, anchor_result,
outcome, [hit_family], certificate,
coverage_theorem_id, constructor_id, digest
```

The source schedule omits `hit_family`; the target schedule includes it. A target p-only HIT sets anchor outcome to `NOT_REACHED`.

## Selector result

A production selector must return exactly one of:

```text
TERMINAL
  exact source/target subject binding + verified certificate + no successor

VERIFIED_EDGE
  only after external actualness, source MISS_COMPLETE, independent target
  MISS_COMPLETE, acyclic E1--E5 bundle, target admission and re-entry

REJECT
  stable reason; never downgraded to MISS or edge
```

The standalone implementation can produce terminal decisions and conditional model objects. It intentionally cannot return a repository-authorized `VERIFIED_EDGE` because it bundles no trust resolver, registry grant, issuer, admission gate or queue capability.

Machine-readable closed schemas are in:

- `schemas/sp05-complete-terminal-decision-v1.schema.json`
- `schemas/sp05-status-boundary-v1.schema.json`

`validate_schemas.py` validates the generated evidence against Draft 2020-12.
