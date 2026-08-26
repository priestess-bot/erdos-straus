# T6 Phase 2 terminal-scope and q=1 priority-prefix handoff

Date: 2026-08-26

## Result

The terminal contract now distinguishes two statements that were previously
both liable to be called `MISS_COMPLETE`:

```text
MISS_REGISTERED_PRIORITY_COMPLETE
  = every family in one declared finite priority prefix missed

TERMINAL_UNIVERSE_MISS_EVIDENCE_ONLY
  = a shape declaring that the full natural terminal universe missed
```

The taxonomy parser validates only exact field/type structure, scope constants
and a self-seal. It deliberately does not execute the opaque registry,
primality, schedule, factorization, coverage or reverse-equivalence artifacts.
Neither shape has an issuer, E1 authority or queue authority. A universe claim
can never continue to a producer; after a future full semantic verification it
would instead report a root counterexample.

## q=1 prefix theorem

The first independently replayed finite prefix is

```text
ordered gaps = (3, 7, 11)
candidate order = gap, divisor, Type I before Type II
next unchecked gap = 15
```

For each gap, the scheduler factors (x_m=(p+m)/4), generates every positive
divisor of (x_m^2), and reconstructs every Type I and Type II hit. A different
module, which imports neither the scheduler nor the old runtime/reproductions,
independently rebuilds the complete factorization, divisor lattice, certificate
list, root equations, precedence, scan digests and outer canonical wire.

The exact controls are:

```text
p=73       gap 7 Type II d=1 is the first terminal
p=241441   gap 11 Type II d=27 is first; historical d=1083 also matches
p=1201     gaps 3/7/11 all miss; unregistered gap 23 Type I d=34 hits
p=2521     gaps 3/7/11 all miss
```

The p=1201 control proves why a registered-prefix miss is not global terminal
exhaustion. The prefix evidence fixes terminal/role authority to `BLOCKED`,
issuance to false and `global_exhaustion` to false.

## Reverse completeness proof

The terse reverse direction in `short-certificate-equivalence` has been
replaced by a repository proof. For an ordered solution and (m=4x-p), it uses

\[
(my-px)(mz-px)=p^2x^2
\]

to recover the Type I or Type II divisor. The Type I argument derives
(4(x^2/d)\equiv-1\pmod m), proves that (h=2x-p>0) would force (h=1),
and then excludes that boundary by parity. The Type II factorization directly
gives (d\le x). Both cases therefore yield the full natural range
(3\le m\le p-2). This closes the proof omitted in Bradford's Type II
statement rather than treating the citation as sufficient.

The same review found and fixed a reversed Type I divisibility check in
`reproductions/short_certificate.py`: `p % y` is now the intended `y % p`.

## Verification and boundary

The q=1 prefix suite passes 10 focused tests; the terminal-scope taxonomy passes
18. Both received independent read-only review after adversarial mutation
testing. Knowledge-base validation is performed before integration commit.

This stage still grants zero coordinator roles and registers zero production
COMPLETE schedules. The next step is an exact-HEAD registry v2 plus a semantic
prefix verifier/issuer binding the admitted source, domain, schedule and family
artifacts. Until then Gate 2, Gate 4, F1, F2, F3 and T6 remain open.
