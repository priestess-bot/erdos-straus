# SP-05 Complete Terminal Package Review

**Review date:** 2026-08-29
**Source ZIP SHA-256:** 7c2e2ff5158412b1aa8230700d945e9f2e8cec2443ce6a528fc04d4c1a3b7f29
**Verdict:** MERGED AS AN ESTABLISHED BOUNDARY; SP-05 ACTUAL EDGE REMAINS OPEN.

## Verified Contents

The package contains a self-contained proof and two non-importing implementations of a finite
terminal decision procedure. The source constructor enumerates factor exponents; the independent
replayer uses a separate primality/factorization and divisor traversal route. The package checksum
manifest was verified before execution. Its focused suite passed 12 tests, and its Draft 2020-12
schema validation passed.

The central mathematical statement is sound. After ordering a candidate solution as
\(x\le y\le z\), its first denominator lies in the finite interval

\[
\lfloor p/4\rfloor+1\le x\le\lfloor3p/4\rfloor.
\]

For each \(x\), reduction of \(4/p-1/x\) to \(a/b\) yields the exact factor-pair
equivalence

\[
(ay-b)(az-b)=b^2.
\]

This proves both soundness and completeness of the finite terminal decision for one fixed \(p\).

## Critical Boundary

The package correctly rejects the previous inference from a registered six-gap MISS to a
nonterminal edge. Its \(p=21169\) control is ordinary \(q=1,G\), has a six-gap M23 MISS, and yet
the global fallback reconstructs

\[
\frac4{21169}=\frac1{5300}+\frac1{3619899}+\frac1{19185464700}.
\]

Thus a complete-terminal-first selector must terminal-preempt before any phase-root projection.
For any actual source, MISS_COMPLETE is equivalent to absence of an Erdős--Straus solution;
therefore a concrete SP-05 nonterminal edge would require both an ordinary \(q=1,G\) counterexample
and separately issued source/admission authority.

The package also correctly uses the frozen T5 vectors

\[
(p,3,0,0,0,0,0)
\longrightarrow
\left(p,2,4,(p-1)^2/4,K,0,0\right),
\]

so its conditional E5 is a real PHASE_DROP, not the incompatible custom phase coordinate from the
earlier draft.

## Integration Choice

The full package is tracked under reproductions/sp05_complete_terminal_decision/. It is evidence
for the complete decision and the conditional phase-root branch only; it does not modify the active
production terminal registry, source actualness, common successor admission, queue, or T6 status.

During integration, the package runner was made reproducible: the source run_all.sh overwrote the
manifested test transcript with a run-time-dependent duration, making a second checksum pass fail.
The integrated runner leaves that immutable snapshot untouched and prints current unittest output to
the console. The independent replayer was also changed from a 64-bit-only Miller--Rabin primality
test to its independent complete sieve-factorization path, and both implementations now reject
bool/float aliases for integer state fields. The source ZIP remains in the ignored local temp/
intake directory.
