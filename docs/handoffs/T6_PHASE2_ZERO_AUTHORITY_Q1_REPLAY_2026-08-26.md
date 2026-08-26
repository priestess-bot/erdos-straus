# T6 Phase 2 zero-authority runtime and q=1 replay handoff

Date: 2026-08-26

## Established results

The Phase 2 migration now has a production-facing V2 entry that can be opened
only from one exact Git commit. The executing runtime, acyclic bundle module,
terminal contract, coordinator resolver and governing registries are bound to
that commit. Under the current registry it derives exactly:

```text
role grants             = 0
initializer grants      = 0
successor routes        = 0
COMPLETE schedules      = 0
queue                    = ()
```

Caller registries, callables, artifact manifests, evidence IDs, legacy boolean
validation, local terminal misses and V1 raw states are not accepted by this
entry. A factory-produced acyclic V2 target/bundle/sidecar is replayed for its
terminal seals and references, then rejected because no route is authorized.
This is a zero-authority safety theorem, not a positive admission result.

The independent q=1 replay separately recomputes, without importing the q=1
runtime or historical reproduction modules:

```text
p prime and p = 1 mod 24
ordinary q=1 G from the complete factorization of X
X=(p+3)/4, t=(p-1)/24
R_X=16t+3, K_X=X(16t+1)
uniqueness of the low X-divisible Type-I chart
fresh p-source -> (1,R_X-1,1)
Sol(p) identity lift
T5 N^7 TYPEII_G_HANDOFF -> TYPEI phase drop
```

Its type labels are branch-local expectations, not a replay of the complete
common classifier or global family precedence. Every output fixes terminal and
role authority to `BLOCKED`, issuance to false and the T5 ticket to evidence
only. This removes the lack of an independent arithmetic implementation but
does not create an independent-validator role.

## Verification

Focused verification at integration time established:

```text
legacy bootstrap hardening                 11 tests PASS
zero-authority runtime V2                  16 tests PASS
acyclic transition bundle V2               23 tests PASS
complete-terminal receipt boundary         14 tests PASS
coordinator role inventory                 21 tests PASS
independent q=1 mathematical replay        20 tests PASS
Ruff / py_compile / git diff --check        PASS
```

Both new claims received independent read-only review. Their claim metadata
remains `internal_review`; subagent review in this development session is not
being promoted to external peer review.

## Open boundary

Gate 2 remains open. The active historical q=1 runtime still uses caller-owned
V1 registration, local terminal miss records, same-module roles and E1--E4
booleans. The coordinator registry still grants no role, the terminal registry
still has no COMPLETE schedule, and the V2 runtime deliberately has no positive
path. F1, F2, F3 and T6 therefore retain their existing open statuses.

The next evidence-producing step is a complete terminal schedule for one exact
q=1 source domain. It must bind the ordered terminal families, owner-domain
coverage theorem, domain replay, independent coverage verifier, certificate
verifier and lift verifier. Only after that result may a coordinator registry
v2 consider separate producer, projector and independent-validator grants and
a positive structured V2 transition.
