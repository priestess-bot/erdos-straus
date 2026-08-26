# T6 Phase 2 terminal-decision assembler handoff

Date: 2026-08-26

## Result

The q=1 root terminal pipeline now executes end to end as non-authorizing
evidence:

```text
exact repository HEAD/tree
  -> fresh registry/root-envelope/scheduler/verifier modules
  -> CanonicalBody -> RootAnchor -> RawRootState
  -> state-derived scheduler domain
  -> registered gaps-3/7/11 scheduler
  -> independent coverage replay
  -> terminal-hit or prefix-miss evidence sidecar
```

The assembler accepts only a repository locator, full commit ID and raw q=1 G
integers. It does not accept a caller registry, callable, state, scheduler
domain, evidence object, coverage result or authority flag.

## Exact execution boundary

An initial review rejected the implementation because restoring a dependency's
file after malicious import did not restore already-loaded internal helper
objects. The accepted implementation no longer invokes any top-level imported
T6 dependency. After checking its own backing file, it reads the registry
resolver, root envelope, scheduler and coverage verifier from regular blobs at
the requested HEAD, compiles each blob into a fresh private module namespace and
uses only those fresh objects.

Tests preload malicious scheduler, coverage and root-envelope helpers, then
restore disk bytes to the HEAD version. None of their markers execute. Canonical
module wrappers and a self-restoring resolver wrapper likewise have no call
path. The currently executing assembler remains the explicit trusted-process
root; it does not claim to prove its own pre-import integrity from inside itself.

## Controls

```text
p=73      Type II gap-7 root-terminal hit evidence
p=193     Type I gap-7 d=10 root-terminal hit evidence
p=1201    gaps-3/7/11 prefix-miss evidence
p=2521    gaps-3/7/11 prefix-miss evidence
```

Each decision binds HEAD/tree, registry and role-manifest digests, the two
grants and semantic pins, module binding, body/anchor/state IDs, state-derived
domain, scheduler invocation/evidence, independent coverage replay and the
three scan digests. A hit additionally replays its selected certificate and the
root equation. A miss requires a null selected certificate.

The decision is a post-state sidecar. Its ID never enters the root state ID.

## Authority boundary

Every output fixes:

```text
source_actualness = false
initializer_authority = false
issuer_authority = false
terminal_authority = false
e1_authority = false
queue_authority = false
producer_continuation_allowed = false
```

Focused tests pass 9/9, with Ruff, `py_compile` and `git diff --check` passing;
the final independent review accepted the fresh-execution and claim boundaries.

The next authority change must be explicit: a separate registry must grant a
root initializer and terminal issuer, and a production issuer must convert this
evidence into a source-bound terminal result. E1 and queue admission remain
separate later grants. Gate 2, Gate 4 and T6 remain open.
