# T6 q=1 production terminal final independent review

Date: 2026-08-26

## Verdict

```text
V3 coordinator registry contract     ACCEPT
Production issuer/replayer contract  ACCEPT
Complete Gate 4                      OPEN
Gate 5 / F1 / F2 / F3 / T6           OPEN
```

This is a repository-level independent implementation and proof-contract
review. It is not external academic peer review.

## Frozen implementation bytes

The accepted pre-commit worktree used:

```text
terminal issuer blob SHA-256           e1cb56239afb1fbe662900eaa70e4cf8baa6e310c336637461ea88b899af500b
receipt verifier blob SHA-256          384dabb8cdc5aad35d49c9b6720d3458f70778892ef3dcb7c64a7aa8a879c4c4
production schema blob SHA-256         7aa00565cd4802711587af2dee9d7b287fbe532998f022de705c121f9e6c4cac
```

The V3 source registry binds these bytes and their stable symbol, closure,
dependency-manifest and semantic digests. These byte hashes identify the
reviewed artifacts; they are not a substitute for the required post-commit
exact-HEAD replay.

## Resolved blocking findings

The implementation was not accepted on first construction. Review found and
resolved the following issues:

1. V3 policy objects and the receipt authority matrix were initially not all
   compared exactly. The resolver and schema now freeze every policy field.
2. V2 and V3 semantic digests use different methods. Cross binding now compares
   each digest to its own pin while separately requiring the same path, blob,
   symbol and schedule.
3. Root actualness originally lacked explicit root-problem and initial-branch
   preimages. It now embeds and replays raw q1 G, the marked `4/p` problem and
   the deterministic G branch.
4. Dependency manifests initially did not transmit dependency semantics.
   `artifact_semantic_pins` now bind every execution and binding dependency,
   so a dependency update requires an explicit consumer repin.
5. A fully repinned issuer could add an undeclared `compile/exec` path.
   The fixed policy now pins each controlled loader helper, caller, executable
   path table and call set. The claim is deliberately limited to the current
   resolver policy and bytes; a new execution mechanism is a new authority
   policy requiring a new proof.
6. The verifier rejected ordinary `Path` values by comparing against the
   abstract `Path` factory type. It now accepts only the exact platform path
   class and rejects subclasses.
7. Issuer and verifier reconstructed different module-binding names. Both now
   use the stable issuer ID, making canonical and alternate import aliases
   produce identical receipts.
8. Initial claim prose listed mutation controls that had not been individually
   executed. The final claims distinguish Schema/content-seal rejection from
   coherent deep replay and explicitly list unimplemented mutation cases.

## Replayed results

The accepted focused suites report:

```text
V3 coordinator registry                         23/23 PASS
Production issuer and post-issuance replay       6/6 PASS
V1 zero-authority evidence inventory            21/21 PASS
Adjacent V2/prefix/root/assembler suites         77/77 PASS
Ruff / py_compile / Draft 2020-12 schemas        PASS
KB validation                                    1462 documents PASS
git diff --check                                 PASS
```

Production positive controls are:

```text
p=73       ROOT_TERMINAL_HIT, Type II, gap 7, d=1
p=193      ROOT_TERMINAL_HIT, Type I, gap 7, d=10
p=241441   ROOT_TERMINAL_HIT at gap 11
p=1201     MISS_REGISTERED_PRIORITY_COMPLETE for gaps 3,7,11
p=2521     MISS_REGISTERED_PRIORITY_COMPLETE for gaps 3,7,11
```

For both MISS controls:

```text
global_exhaustion = false
next_unchecked_gap = 15
terminal_leaf_authority = false
e1_authority = false
queue_authority = false
producer_continuation_allowed = false
```

## Serializer boundary

The review constructed a coherent adversarial control: raw/root problem remain
at `p=73`, while body, anchor and state references are consistently replaced by
a valid `p=1201` root chain and all local seals are recomputed. The issuer-local
serializer accepts that internally consistent receipt. The independent
exact-HEAD replayer reconstructs the expected `p=73` source and rejects it.

Therefore a content seal is not production authority. A consumer must require
successful post-issuance replay; it must not authorize from the receipt object
or local serializer alone.

## Exact remaining boundary

The result establishes only the parentless ordinary q1 G root registered-prefix
issuance/replay subgate. It does not establish:

```text
common owner classification
scope-aware E1 consumption
an active recursive producer or branch
E2, E3, E4 or E5 for a successor
target re-entry
queue mutation
complete terminal schedules for other owner domains
global terminal exhaustion
```

After publication, the new commit must be replayed as an exact full Git HEAD.
Only a green Gate 0/live-snapshot run on that commit can serve as the published
provenance record. No F1/F2/F3/T6 status changes are authorized by this review.
