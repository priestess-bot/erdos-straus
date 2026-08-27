# F2 C8 q-star=103 Gap-403 Terminal-Only Guard Boundary (2026-08-27)

This is a coordinator interface request, not an active C8 producer.

It consumes only an admitted `c8_terminal_first_surviving_parent` with a
continuous q-star=103 relay and roughness receipt. It returns a terminal on
one of two positive gap-403 certificates:

1. `u = -1 mod 403`: Type II with divisor `103`.
2. `u = 14 mod 179`: Type I with complementary divisor `103 * 179`.

The guard is hit-only. A non-hit is `GuardMissV1`, not `MISS_COMPLETE`, and
cannot authorize the second-full-excess macro or any queue action.

The non-atomic C8 fallback remains ordered after a genuine complete terminal
MISS. The lambda=56 strict-capacity ray is later still: it concerns the
admitted fallback target's next full-excess rechart, not the C8 parent.

Activation is blocked by the lack of an admitted C8 parent/source-path
receipt, C8 terminal scheduler, common E3/admission, and re-entry. The request
does not change F2, T6, or the conjecture.
