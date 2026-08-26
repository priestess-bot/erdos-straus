---
kind: claim
claim_id: t6-acyclic-transition-bundle-v2-contract
title: T6 non-authorizing acyclic transition bundle V2 contract
statement: >-
  Outputs of the public V2 factories, and mappings accepted by the V2 parsers
  when replayed against explicitly supplied upstream objects, have a typed
  topological dependency order over the contract's reserved fields: projection;
  preclassification, terminal and T5 drafts; edge anchor; raw target/state ID;
  final receipt-digest bundle/transition ID; admission sidecar. Every typed
  upstream artifact is fully revalidated before use, so malformed exact-class
  objects and mismatched reserved references are rejected even when their local
  content seals are recomputed. This is a non-authorizing structural result.
  It gives opaque digests no provenance, does not recognize semantic synonyms
  or digest preimages, does not establish E1--E5 correctness, and does not close
  Gate 2 or change F1/F2/F3/T6 status.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
topics:
  - T6
  - content-addressing
  - structured-receipts
  - acyclicity
  - proof-boundary
sources:
  - reproduction: scripts/t6_acyclic_transition_bundle_v2.py
    role: slotted factories, typed invariant validation, seals and dependency replay
  - reproduction: tests/test_t6_acyclic_transition_bundle_v2.py
    role: field, type, swap, cycle and ID-independence negative controls
  - source: schemas/t6-acyclic-transition-bundle-v2.schema.json
    role: exact machine-readable V2 field contracts
visibility: public
last_checked: '2026-08-26'
---

# T6 non-authorizing acyclic transition bundle V2 contract

## Established dependency order

The content-addressed objects form the following directed acyclic graph:

```text
CanonicalTargetProjectionV2
  |-- PreclassificationDigestV2 ---------|
  |-- TerminalDigestSetV2 ---------------+-> EdgeAnchorV2
  `-- T5CoordinateDraftV2 ---------------|
                                                |
                                                v
                                      RawTargetStateV2 / state_id
                                                |
                                                v
                              FinalTransitionReceiptBundleV2 / transition_id
                                                |
                                                v
                                    StateAdmissionSidecarV2
```

Every downstream public factory consumes exact-class upstream objects, first
revalidates all their typed fields, and then replays identifiers and bare
SHA-256 content digests. Parsers require exact reserved field sets and
reconstruct the expected artifact from explicitly supplied upstream
dependencies. Thus a cross-chain substitution of a reserved reference is
rejected against those supplied dependencies even if the substituted mapping's
local seal is recomputed.

The Python dataclasses use `slots=True` and `frozen=True`, but that is not a
security or immutability theorem: Python callers can deliberately bypass normal
construction with `object.__new__` and `object.__setattr__`. The validation
boundary is the complete type-specific invariant replay performed whenever an
artifact is serialized or consumed downstream. Tests forge exact-class objects
through that bypass and confirm that valid recomputed seals do not rescue
invalid integers, strings, digests, facts, coordinate tuples or origin refs.

## Layer boundaries

`CanonicalTargetProjectionV2` contains mathematical target data and declared
projector/tie-break digest pins. For the reserved field vocabulary, its free
facts reject terminal, anchor, state, owner, potential, transition, receipt,
bundle, admission and E1--E5 keys. It also rejects boolean values. These are
syntactic restrictions only: keys such as `admitted`, `verified` or arbitrary
semantic synonyms are allowed as ordinary data, and opaque digest values can
encode content this layer cannot inspect. The module has no consumer that turns
such data into authority.

The three draft objects bind declared digests and, for T5, a draft vector in
`N^7`. A syntactically valid digest is not evidence of its source or contents.
These objects do not state that normal form, terminal completeness or strict
descent has been proved.

`EdgeAnchorV2` binds the source, producer, candidate, projection and three
drafts. It has no target state ID, transition ID or E3--E5 receipt field. This
is the last object constructed before the target state exists.

`RawTargetStateV2` produced by the public factory is derived from the canonical
projection and contains a two-field `SuccessorOriginAnchorRefV2` as its only
reserved edge-origin metadata. Its typed field set contains no transition
bundle, transition ID, owner, potential receipt, admission result or E1--E5
boolean. Its `state_id` is structurally independent of those later typed
fields. This does not rule out a semantic synonym or a digest preimage carrying
equivalent information as uninterpreted data.

The public factory for `FinalTransitionReceiptBundleV2` requires a validated raw
target state and binds the source, target, anchor and five opaque structured-
receipt digest declarations before deriving `transition_id`. Those digest pins
carry neither provenance nor verification of the referenced receipts.

`StateAdmissionSidecarV2` is the only shape carrying owner, grammar, admission-
gate and target-potential receipt digests. In particular, `owner_digest` is a
bare 64-character lowercase hexadecimal SHA-256 digest, never a prefixed or
self-describing string. For public-factory outputs, the sidecar is built after
`transition_id` and is not an input to any upstream identifier.

The JSON Schema is a structural interoperability contract. JSON Schema defines
mathematically integral JSON numbers such as `2.0` as integers, whereas the
canonical Python parser deliberately accepts only exact Python `int` values.
The schema also cannot recompute content seals or establish digest provenance.
The regression suite records this difference; no schema/Python type-equivalence
claim is made.

## Negative controls

The focused regression suite covers:

- exact dataclass-to-schema reserved field equality and slotted/frozen public
  outputs, without treating those Python flags as a security boundary;
- forged exact-class upstream objects with recomputed seals but invalid string,
  digest, integer, facts, coordinate or origin-ref shapes;
- booleans masquerading as integers, coordinates, receipt evidence or digests;
- projection imports of terminal, anchor, state, owner, potential, transition
  and E fields;
- edge-anchor imports of target state, transition and E3--E5 fields;
- raw-state imports of bundle, transition and E booleans;
- projection, sibling-draft, anchor, target and bundle swaps after resealing;
- explicit reserved-field references to later state and transition identifiers;
- invariance of projection, anchor and state identifiers under downstream
  receipt or sidecar changes;
- legacy E1--E4 boolean dictionaries, for which no fallback parser exists;
- unreserved `admitted` and `verified` synonym keys remaining inert because no
  admission, issuance, registry, dispatch or queue consumer exists here;
- the deliberate JSON Schema `integer` versus exact Python `int` distinction.

## Explicit non-results

This contract does not prove actual occurrence, deterministic mathematical
projection, common typing, universal lifting, T5 descent, terminal completeness
or recursive re-entry. It contains no producer/validator registry, receipt
issuer, admission decision, runtime dispatch or queue operation. Consequently
it is a prerequisite data-model result only: Gate 2 and T6 remain open until a
separate coordinator-owned integration independently constructs and replays
the substantive E1--E5 receipts. It also does not prove that arbitrary payloads
are semantically acyclic: the theorem concerns only the explicit typed fields
and references enumerated by this contract.
