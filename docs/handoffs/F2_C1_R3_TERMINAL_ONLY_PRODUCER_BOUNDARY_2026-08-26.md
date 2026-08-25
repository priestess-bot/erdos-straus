# F2 C=1 R=3 terminal-only producer boundary

This is a coordinator interface request, not an active producer registration.

The proposed branch consumes only an already admitted
type_i_a_gt_one_overflow_residual source with

\[
A>B_p,\qquad K=A,\qquad R=3,\qquad R>p,
\]

and a replayable terminal-first MISS. It may return a verified direct terminal
or a guard miss. It cannot return a candidate or mutate the queue.

The deterministic terminal order is:

1. the existing source terminal schedule;
2. the \(p+4\), \(q\equiv3\pmod4\) Type-II certificate;
3. the \(N=(3p+1)/4\), \(q\equiv2\pmod3\) Type-I certificate;
4. the fixed-\(p\) composite-\(D\) divisor table, using its least mixed row.

The new TerminalOnlyProducerRegistrationV1 models this branch without
inventing target owners, projectors or T5 tickets. The independent verifier
must recompute every certificate from the admitted source facts and bind the
source state ID, owner digest and schedule scope. A GuardMissV1 is the only
nonterminal result; a CandidateTransitionV1 is rejected by the runtime.

Activation remains blocked because no actual C=1 source producer/path is
currently registered, and the R3-G remainder still needs a complete terminal
or successor route. The request therefore narrows the next implementation
task without changing F2 or T6 status.
