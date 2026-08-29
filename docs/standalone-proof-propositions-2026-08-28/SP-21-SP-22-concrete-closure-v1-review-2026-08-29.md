# SP-21/SP-22 Concrete Closure V1 Review

**Review date:** 2026-08-29
**Disposition:** `computationally_reproduced` prototype; not an active SP-21 or
SP-22 closure.

## Submitted Scope

The submitted `sp21_sp22_concrete_closure_v1.zip` defines a new finite policy
on the decidable ordinary \(q=1,G\) root predicate domain:

\[
(3,7,11,15,19,23)\text{ terminal actions}
\;\to\;
\text{phase-root producer}
\;\to\;
31\text{ later terminal action}.
\]

It supplies a signed policy/lock pair, a constructor, an independent replay
program, a pilot admission queue, a \(p=21169\) positive trace, and a bounded
census below \(100000\). The original extracted material is preserved at
`docs/archive/proof-submissions/2026-08-29/sp21-sp22-concrete-closure-v1/`.

## Reproduction Results

1. The submitted ZIP has SHA-256
   `5db5a12c2b91e80037b4949a856e68398de9877a72e1b678c56a1812ba9e81fa`.
2. Its internal `MANIFEST.sha256` passed for all 25 listed files.
3. In an isolated Git worktree at its declared base
   `e6e9e4a8c41b90a330b9ef333e542c18c2cb7be4`, the supplied installer completed
   and all 37 focused tests passed.
4. The constructor and independent replayer regenerated the submitted evidence
   IDs `7eb2bdbc44d67acba8c4357a917b4ed4d446ceb46bf1de468f34f36d83b7da99`
   and `fec547d83b6af59c2785968d67f6ec285174c1e381b61b883e6c7f81eefee69d`.
5. The independent replayer has no repository-local imports and does not invoke
   the selected producer. Its divisor enumeration is structurally distinct from
   the constructor's exponent-product enumeration.

The package therefore gives useful reproducible evidence for a self-contained
M23-priority selector prototype and for the \(p=21169\) arithmetic trace. In
particular, it correctly retains the gap-31 certificate as a later terminal and
does not serialize M23 clearance as global exhaustion.

## Blocking Findings

### 1. The claimed external authority has no external trust binding

The RSA signature verifies relative to a public key that is pinned inside the
submitted constructor and independent replayer. No signed Git tag, GitHub
attestation, identity certificate, or other repository-external provenance binds
that public key to an independent coordinator. Absence of the private key from
the ZIP establishes neither key ownership nor authority external to the supplied
artifact. It is therefore an internal cryptographic fixture, not an independently
verified actual-source authority.

### 2. `base_head_sha` is asserted but not checked against the current checkout

`verify_artifact_lock` checks the lock's declared base string and hashes only its
enumerated artifacts; it does not run `git rev-parse HEAD` or otherwise compare
the current checkout to the declared base. This was reproduced by copying the
locked overlay files into an isolated checkout at
`eaf8059455844f6ac170fc09f11296453aafbc6b`: the constructor accepted and emitted
the same evidence ID while its receipt still declared the old `e6e9e4a` base.

Thus the package binds a selected file set, not the claimed exact repository
commit. This is insufficient for an `actual source` or external-policy claim in
the active repository.

### 3. The admission and re-entry runtime is a new isolated pilot

The package deliberately does not activate the existing persistent selector. Its
`PersistentPilotRuntime`, potential evaluator, owner classifier, queue ingress,
and source wire are defined inside the submitted module. Consequently, its
successful E1--E5/R trace proves behavior in that newly defined slice, not that
the active `t6_persistent_selector_state_v1` / current T5 state universe accepts
the same source or target. The required common admission and production re-entry
for SP-21/SP-22 remain unproved.

## Active Status

The active dossiers remain `OPEN_PROPOSITION`:

* SP-21 retains its established abstract safety theorem, but lacks an externally
  trusted, current-repository concrete policy instance.
* SP-22 retains its requirement for an actual current-state source, common E3,
  current fixed E5 evaluator, and re-entry into the existing selector.

This review does not dispute the package's internal arithmetic or its scoped
policy case split. It rejects only the upgrade from an isolated signed prototype
to an active repository closure.

## Required Revision

To promote this prototype, a successor package must provide all of the following:

1. a coordinator trust root verifiable outside the submitted bytes, with an
   authority statement that identifies the signer and its authorization scope;
2. a binding to the exact active commit/tree, or a precise artifact-only claim
   that does not call the result an exact-HEAD or actual-source proof;
3. adapters that consume the existing source initializer, T5 evaluator, common
   admission gate, and persistent selector rather than a private pilot runtime;
4. an independent replayer for those active receipts plus the same mutation,
   source-swap, order-swap, and queue-bypass controls.
