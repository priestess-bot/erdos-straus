# T6 F2/F3 Wave1 Residual Frontier

Machine-readable source: `data/t6-wave1/t6-f2-f3-residual-frontier-v1.json`.

The wave has completed integration baseline, runtime protocol Freeze A, and E3 type-space Freeze B.
It has not passed Gate 3 producer freeze. The table below therefore records only exact residual groups,
not informal “almost complete” status.

| Area | Exact remaining obstruction | First missing obligation |
|---|---|---|
| F1 | 9 inventoried unknown source/runtime items; no proof every legacy write uses the runtime | D1/D2/D3 |
| F2 post-G/H4/c8 | arithmetic reductions exist, but q1 source/target schedules and the first-child ABSORB protocol are not continuous in runtime | E1/E3 |
| F2 high C=1 | two terminal sieves reduce it to the exact (R=3)-G hard-core branch; 11-character and P-min screens refine it, but its ABSORB cursor has a formal self-loop | E1/E3/E5 |
| F2 high C>1 | checkpoint/carry alone cannot force bounded descent; factor-saturation lacks structural E1 provenance | E1/E5 |
| F3 high | strict carry waits for E3; high stutter splits into Pell (k=1) and odd (k\ge3) residuals, and its two divisor gates are root-lift saturated | E3 / canonical valuation, terminal, or source data |
| F3 QC1 | ideal factor has no integer raw occurrence or conserved support charge | E1 |
| F3 TR1 | h-menu/D-star factors are only arithmetic eligibility, not consumable occurrences | E1 |
| F3 m3 q5 | nonminimal, regeneration p-free failure, one-sided and two-sided (p^2) leaves remain | E1/E2/E3/E5 |

No source factor, local checkpoint, synthetic receipt, finite control or status field is counted as a closure.
The next run should consume this ledger directly and update a group only after the entire stated quantified
domain becomes `FAMILY_EMPTY`, `TERMINAL`, or `VERIFIED_SUCCESSOR_E1_E5_REENTRY`.
