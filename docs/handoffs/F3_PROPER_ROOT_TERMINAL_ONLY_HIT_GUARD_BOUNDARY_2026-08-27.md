# F3 Proper-Root Terminal-Only Hit Guard Boundary (2026-08-27)

This is a coordinator interface request, not an active producer registration.

The proposed branch consumes only an admitted
`proper_root_stutter_k_gt_one` source with the full F3 actual-persistent
envelope. It returns a verified terminal on a positive short certificate or a
nonexhaustive `GuardMissV1`. It cannot produce a candidate, target owner, T5
ticket, or queue mutation.

The deterministic positive-hit order is:

1. Gap 3 Type II: a divisor of `(p+3)/4` congruent to `2 mod 3`.
2. Type II: a `3 mod 4` divisor of `p+4` with certificate divisor `1`.
3. Type I: a `3 mod 4` divisor of `(p+1)/2` with complementary divisor
   `x=(p+m)/4`.

Each hit is p-only once an admitted source supplies the shared root `p`; it
does not require a raw QC1/TR1 occurrence. A miss must remain a local guard
miss. It cannot certify that the complete F3 terminal universe, a cofactor
subfamily, or QC1/TR1 has missed without complete factor/divisor coverage.

`core_d=13` and `stutter_m=3` are source-domain labels. They must not be
serialized into Bradford's `certificate_divisor` or `certificate_gap` fields.

Activation remains blocked by the absence of an admitted F3 proper-root source
and source-path receipt. The request narrows the first safe terminal-only
integration point; it does not change F1, F3, T6, or the conjecture.
