# SP-21 Proof Review

**Review date:** 2026-08-29

## Verdict

The submitted proof establishes the abstract scope-bound terminal-priority
safety theorem after two necessary repairs:

1. An earlier reject prevents the selected action from being reached, so
   PriorClear alone is insufficient. The operational theorem must require
   Reach, equivalently PriorClear plus NoRejectBefore.
2. An arbitrary earlier terminal HIT is a reliable certificate but not
   necessarily the actual selector output when an earlier producer has already
   fired. The actual-terminal theorem must require reachability of that terminal
   action.

With these repairs, the finite-prefix induction, selected-producer theorem,
policy-relative clearance theorem, and non-interference of later/unregistered
terminal formulas are correct.

## Arithmetic Review

The finite q=1 control was independently recomputed:

* Pocklington data for \(p=21169\) with witness \(13\) are valid.
* The full factor-pair residue sets for all six M23 gaps exclude the required
  \(-D_g\) residue, so each defined finite action misses.
* For gap 31, the factor pair \((21169,594637210000)\) reconstructs

\[
\frac4{21169}
=\frac1{5300}+\frac1{3619899}+\frac1{19185464700}.
\]

Thus M23 clearance is a valid scope miss and not a global terminal miss.

## Archival Disposition

The submitted source had SHA-256
`282eaf10b9dcd0a63e39e4e117db241f9454ce0b01ae647c5c47d6880bf18773`
before archive whitespace normalization. Its tracked archival copy is at
docs/archive/proof-submissions/2026-08-29/SP-21-submitted-proof-2026-08-29.md
with SHA-256
`db033259df625f8bc3f4bec1c898e516cc38f19a655f87e5d5836541fdd5cc5f`.
The only archival change is removal of one final blank line for repository
formatting checks.

The canonical, typeset proof is
SP-21-ABSTRACT-SAFETY-PROOF-2026-08-29.md. It is the source for the established
abstract claim.

## Remaining Open Work

The original SP-21 dossier remains OPEN_PROPOSITION because it still lacks:

* a concrete coordinator-owned frozen policy and action registry;
* proof that every overlapping registered terminal is ordered before, or is
  disjoint from, the selected producer;
* external authority binding, actual source receipt, common admission and
  queue/re-entry implementation;
* an independent executable prefix replayer for that concrete policy.

This result changes the P0 task from proving abstract safety to instantiating it
for one real policy. It does not establish SP-22, F1/F2/F3/T6 totality, or the
Erdős--Straus conjecture.
