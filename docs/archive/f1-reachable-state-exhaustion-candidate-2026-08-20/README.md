# F1 Candidate Package Archive (2026-08-20)

Status: `ARCHIVED_UNACCEPTED_CANDIDATE`

This directory preserves the package submitted as a proposed closure of
`T6-F1-REACHABLE-STATE-EXHAUSTION`.  It is evidence for review, not an
admitted theorem, selector contract, or proof-frontier update.

## Canonical Artifact

The byte-for-byte source artifact is
[`../../erdos-straus-F1-reachable-state-exhaustion-all-outputs.zip`](../../erdos-straus-F1-reachable-state-exhaustion-all-outputs.zip).

Its SHA-256 digest is:

```
2a7d2744cf72c23fa163c9f75979cd4eb7e92dd9c69b7a74430fa9c6c062eb0c
```

`unzip -t` and the package's own `SHA256SUMS` verification both passed at
archive time.  The raw ZIP is therefore the authoritative preservation of
every submitted byte.

## Extracted Source View

`source/` contains the extracted Markdown, JSON, patch, workflow, Python
source, and recorded validation output exactly as supplied.  It intentionally
omits only the two `__pycache__/*.pyc` files: they are interpreter-specific
binary caches, remain preserved in the raw ZIP, and carry no independent
mathematical content.  The retained `source/SHA256SUMS` is verbatim and still
lists those files, so it must be checked against the raw ZIP extraction rather
than against this source-only view.

## Disposition

The package was reviewed in
[`../../F1-reachable-state-exhaustion-package-review-2026-08-20.md`](../../F1-reachable-state-exhaustion-package-review-2026-08-20.md).
That review found circular ownership definitions, absent integration into the
current state contract, an assumed rather than derived producer enumeration,
and self-referential static checks.  Consequently F1 remains `OPEN` in the
canonical T6 boundary; no material here may be cited as an F1 closure.

The archive exists so later work can repair or reuse its ideas without losing
the exact submitted evidence or confusing it with accepted proof material.
