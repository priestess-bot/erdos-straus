# T6 Phase 2 prefix-role and root-envelope handoff

Date: 2026-08-26

## Exact-HEAD prefix roles

Coordinator registry v2 grants exactly two executable capabilities for the q=1
gaps-3/7/11 registered priority prefix:

```text
TERMINAL_SCHEDULER
INDEPENDENT_COVERAGE_VERIFIER
```

The verifier's domain, certificate and root-terminal checks are capabilities of
the same independent replay, not extra roles. The tracked source registry has no
HEAD; the resolver produces an ephemeral manifest for one exact full commit and
disables Git replacement objects.

The first independent review rejected the implementation after reproducing
three authority attacks: code drift silently inherited a grant, dynamic imports
through aliases escaped the closure audit, and a later module-level binding
could replace the authorized function. The accepted revision now requires:

```text
tracked expected blob SHA-256
tracked stable symbol-AST SHA-256
tracked local-import-closure digest
tracked semantic digest
grant-level semantic digest pin
```

It also forbids dynamic loader modules and calls, audits every relevant
module-scope store/delete binding, rejects shared local helpers and unresolved
forbidden-root imports, and requires the scheduler and verifier to have distinct
paths, blobs, semantics and local closures. Python 3.12.14 and 3.13.5 produce the
same pinned authority digests; interpreter version remains diagnostic rather
than changing the grant.

The resolved status is deliberately:

```text
HEAD_BOUND_PREFIX_SCHEDULE_AUTHORITY_NO_ISSUER
issuer_count = 0
issuer/E1/queue/producer/initializer/T5 authority = false
authorized branches = []
```

Thus the registry authorizes code identity and scope only. It neither executes
the schedule nor signs a terminal result.

## Acyclic root source

The q=1 source now has a root-specific V2 content DAG:

```text
CanonicalQOneGSourceBodyV2
  -> RootInitializerAnchorV2
  -> RawRootSourceStateV2
```

The body independently verifies the core prime, (4/p), ordinary q=1 G,
`ROOT_SOL(p)` and the complete factorization of (X=(p+3)/4). The anchor has no
`state_id`; the state carries only a two-field root-origin reference. The anchor
domain replay pin is derived uniquely from the body and fixed structural
contract, not supplied by the caller.

Terminal, schedule, result, owner, potential, E1--E5, transition, admission and
queue fields are absent from every ID preimage. A later schedule result can bind
the state without making the state depend on that result. All three objects
remain evidence-only and set initializer/admission/queue authority to false.

## Verification and next step

Focused results:

```text
coordinator registry v2             29 tests PASS
root initializer envelope v2        11 tests PASS
Ruff / py_compile / schemas          PASS
Python 3.12.14 / 3.13 authority pins MATCH
independent reviews                  ACCEPT
```

The next required object is a separate terminal issuer. It must consume the
exact-HEAD registry, the root state, scheduler evidence and independent coverage
replay, but the current registry must reject it because no `TERMINAL_ISSUER`
grant exists. Adding the issuer role will be a distinct authority change. Even
after issuance, E1 and queue admission remain separate future contracts, so
Gate 2, Gate 4 and T6 stay open at this handoff.
