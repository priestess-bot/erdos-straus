# T6 F2/F3 Wave1 Residual Frontier

Machine-readable source: `data/t6-wave1/t6-f2-f3-residual-frontier-v1.json`.

The wave has completed integration baseline, runtime protocol Freeze A, and E3 type-space Freeze B.
It has not passed Gate 3 producer freeze. The table below therefore records only exact residual groups,
not informal “almost complete” status.

| Area | Exact remaining obstruction | First missing obligation |
|---|---|---|
| F1 | q1 local slice uses runtime, but 9 inventoried unknown source/runtime items remain and no legacy-write exhaustion is proved | D1/D2/D3 |
| F2 post-G/H4/c8 | C9 R=23 has one fixed-tail terminal subray, but remaining fixed-R rows and all post-G outputs lack full terminal/re-entry routes | E1/E3 |
| F2 high C=1 | two terminal sieves reduce it to the exact R=3-G hard core; its canonical anchor is T5-inadmissible, leaving only non-anchor exits | E1/E3/E5 |
| F2 high C>1 | checkpoint/carry alone cannot force bounded descent; SPF saturation is neither fixed-n nor same-chart full-excess E1 | E1/E5 |
| F3 high | strict carry lacks a high source/re-entry; high stutter lift also preserves every Theta-only terminal menu | E3 / a nonrecurrent terminal predicate or source data |
| F3 QC1 | q_perp endpoint excess gives a strict raw-deflation target, but the remaining source/path and atomic-stutter leaves lack admission | E1/E3 |
| F3 TR1 | every root-height Q|u menu must miss before D-star routing; D-star factors are only arithmetic eligibility, not consumable occurrences | E1 |
| F3 m3 q5 | nonminimal, regeneration p-free failure, one-sided and two-sided p2 leaves remain; direct p2 rechart is unpaid | E1/E2/E3/E5 |

No source factor, local checkpoint, synthetic receipt, finite control or status field is counted as a closure.
The next run should consume this ledger directly and update a group only after the entire stated quantified
domain becomes `FAMILY_EMPTY`, `TERMINAL`, or `VERIFIED_SUCCESSOR_E1_E5_REENTRY`.
