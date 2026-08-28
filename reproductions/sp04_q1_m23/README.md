# SP-04 evidence package

This package proves and replays only the six registered gaps

```text
3, 7, 11, 15, 19, 23
```

for the Bradford Type-I/Type-II definitions in `SP-04-proof.md`.

Run:

```bash
./run_all.sh
```

The final required line is:

```text
SP-04 INDEPENDENT VERIFICATION: PASS
```

## Main files

- `SP-04-proof.md` — self-contained mathematical proof and exact control tables.
- `sp04_constructor.py` — implementation A: factorization plus exponent-product divisor generation.
- `sp04_verifier.py` — independent implementation B: divisor-pair scan through `k <= x`; no import from A.
- `divisor_transcript.tsv` — constructor output: every divisor row for 42 registered gap replays plus the external `p=21169,m=31` boundary replay.
- `independent_divisor_transcript.tsv` — independently recomputed verifier output; checked row-for-row against the constructor transcript.
- `primality_transcript.tsv` and `independent_primality_transcript.tsv` — constructor and verifier trial-divisor replays for the seven control primes.
- `definition.rec` — fixed schedule-definition encoding.
- `replays/*.rec` — per-gap replay encodings; no source payloads.
- `bindings/*.rec` — source-binding encodings; separate from definition and replay objects.
- `outcomes.json` and `replay_index.json` — human-readable indexes.
- `verification_report.txt` — independent verification and precedence-mutation results.
- `MANIFEST.sha256` — packaging checksums only; it is not accepted as mathematical evidence without recomputation.

## Exact miss semantics

```text
MISS_REGISTERED_PRIORITY_COMPLETE
coverage = REGISTERED_PRIORITY_ONLY
next_unchecked_gap = 27
global_exhaustion = false
```

The package does not claim natural-gap global exhaustion and does not claim a proof of the Erdős–Straus conjecture.
