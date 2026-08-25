# q1 C9 Fixed-n Local Candidate

**Status:** established arithmetic candidate; not an active Gate-3 successor.

This note records a source-specific alternative continuation for the q1
third-anchor C=9 target. It is retained as a local proof option, not as an
F2/F3/T6 closure result.

## Exact Scope

The input is not every prime congruent to `25 mod 336`. It must already be an
actual q1-G third-anchor trace with its declared terminal-prefix misses. Write

\[
p=336k+25,
\qquad
M=2(140k+11)(40k+3),
\]

\[
(R,K;A)=(1200k+95,9M;M).
\]

The congruence alone is insufficient: for example, \(p=2377\) has this
residue but its q1 initializer is preempted by the gap-3 terminal.

## Fixed-n Construction

Set

\[
d=p-9,
\qquad n=4M-R,
\qquad L=2M,
\qquad \delta=\frac{p-9}{2}.
\]

Then

\[
pn=4Md+1,
\qquad \frac{Md}{L}=\delta<p,
\]

so this is the ordinary positive fixed-\(n\) case, with no quotient-fold
re-entry. The deterministic target is

\[
T_{18}=(p,4M+R,M(p+9);2M).
\]

It satisfies

\[
p(4M+R)+1=4M(p+9),
\qquad 2M\mid M(p+9),
\]

and its cofactor is \((p+9)/2\). Moreover

\[
B_p-2M=5824k^2+592k+12>0,
\]

\[
3M-B_p=5376k^2+1128k+54>0.
\]

Hence \(M<2M<B_p<3M\), and the charged T5 tuple strictly decreases:

\[
(p,2,4,2,9,0,0)
>
\left(p,2,4,1,\frac{p+9}{2},0,0\right).
\]

The arithmetic target is a low-support `TYPEI/CHARGED` overflow shape and
matches `type_i_a_gt_one_overflow_residual` at type-space level. The lift is
the identity on \(\operatorname{Sol}(p)\).

## Non-Admission Boundary

This candidate is deliberately not registered as the generic fixed-\(n\)
selector output. On the local C=9 control \(p=1033\), the generic
bounded-divisor selector has several eligible divisors and chooses its largest
one, not \(L=2M\). Therefore this rule needs its own q1-C9 source predicate,
precedence, projector, terminal schedule, validator, and re-entry theorem.

The current q1 runtime admits the C=9 source only in its local registry and
then returns `DEAD_END` for the resulting overflow owner. Consequently this
note establishes only E2 and relative E4/E5 for a possible source-specific
extension. It does not establish E1 registration, E3 common admission, D8
re-entry, F2 totality, T6 totality, or the conjecture.
