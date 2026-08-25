# F2 C>=p+1 Noncanonical Handoff

> Track: F2-HIGH-SUPPORT-CGT1-NONCANONICAL
> Base: 332c0f7ed48d453ca76d35639a618659d9b559ca
> Status: arithmetic split frozen; E1/E3/re-entry open

## Frozen Scope

The scope is an actual persistent TYPEI/CHARGED overflow

\[
A>B_p,\qquad 4K=pR+1,\qquad R>p,\qquad A\mid K,\qquad C=K/A\ge p+1,
\]

after terminal-first MISS and the earlier F2 precedence guards. It excludes
transient charts, post-hoc determinant identities, fixtures and unregistered
queue mutations.

The three machine-readable freeze artifacts are:

- data/t6-wave1/f2-high-support-cgt1-noncanonical-scope-freeze-v1.json
- data/t6-wave1/f2-high-support-cgt1-noncanonical-residual-matrix-v1.json
- data/interface-requests/f2-high-support-cgt1-noncanonical-target-shapes-v1.json

## Arithmetic Result

For a fixed chart, define

\[
\mathcal D(C)=\{c:2\le c<p,\ c\mid C\}.
\]

There is a proper determinant image with \(M=Ab<K\) exactly when
\(\mathcal D(C)\ne\varnothing\). The image has

\[
M=A(C/c),\qquad d=p-c,\qquad K=M c,\qquad
(0,C)\longrightarrow(0,c).
\]

This is a deterministic arithmetic target only. A divisor \(c\mid C\) does not
identify a raw occurrence, a parent, a terminal-first MISS, an owner or a queue
admission.

The complementary p-rough stratum \(\mathcal D(C)=\varnothing\) has no proper
determinant image. It is not thereby terminal or family-empty. Formal charts
exist for every core prime; the explicit \(p=73,q=151\) control is recorded in
the claim and is not an actual source assertion.

## E1/E3 Gate

The only candidate route currently justified is:

    actual source-bound determinant occurrence
      -> same-chart support M=A(C/c)
      -> target terminal-first
      -> independent PersistentSelectorStateV1 projection
      -> owner/admission
      -> shared-runtime re-entry

The route is not registered. In particular:

- c|C is not an E1 occurrence;
- a p-rough certificate is not a terminal certificate;
- the local (0,C)->(0,c) drop is not an admitted T5 ticket;
- no target owner may be supplied by the candidate payload.

## Next Proof Decision

For the small-divisor stratum, the next useful theorem is a source-bound
occurrence theorem for one named producer, followed by a common projector and
re-entry replay. For the p-rough stratum, the next useful result must be a
terminal proof, an actual-domain FAMILY_EMPTY theorem, or an independently
source-bound alternative producer. More congruence conditions on C alone do
not meet the closure contract.

Shared README.md, frontier files and generated indexes are intentionally not
modified by this handoff. F2 and T6 remain OPEN.
