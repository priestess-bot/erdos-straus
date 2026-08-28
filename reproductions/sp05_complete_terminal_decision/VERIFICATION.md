# Verification record

Run from this directory:

```bash
./run_all.sh
```

The executable checks are secondary to the mathematical proof. They cover:

1. constructor factor-pair search versus an independent direct-`y` scan for every prime `p <= 1000`;
2. `p=21169`: 204 M23 checks MISS, then the complete fallback finds `(5300,3619899,19185464700)`;
3. six earliest-hit Bradford controls;
4. source/target subject-separated independent replay;
5. projection, anchor gcd, frozen T5 vectors and `PHASE_DROP`;
6. fake `MISS_COMPLETE`, source/q-path/tie-break/target-subject/T5/re-entry mutations;
7. rejection of both the reference actualness fixture and a forged, correctly sealed nonzero-digest actualness object.
8. rejection of bool and float values masquerading as the integer q=1 source field.

No positive nonterminal-edge test exists in the package. Such a fixture would require both a complete-miss `p`—an Erdős--Straus counterexample—and exact repository authority.
