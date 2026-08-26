# T6 q=1 Gap-23 Two-Box Independent Review

Date: 2026-08-27

Reviewed claim:
[type-I-type-II-gap-23-two-box-classification](../../claims/type-I-type-II-gap-23-two-box-classification.md)

## Verdict

~~~text
ACCEPT for the stated single-gap arithmetic theorem.
NOT an E2/E3/E4/E5, terminal-schedule, producer, queue, F1/F2/F3, or T6 result.
~~~

## Independent Checks

For \(p=24s-23\), \(x=6s\), and \(23\nmid s\), the review independently
rederived the following facts.

1. The Type-I divisor condition is exactly

   \[
   e=x^2/d\equiv-4^{-1}\equiv17\pmod {23}.
   \]

   The decomposition of every divisor of \(36s^2\) into a divisor of 36
   times a divisor of \(s^2\) remains valid when \(2\mid s\) or \(3\mid s\).
   The resulting target residue set is

   \[
   17\operatorname{Div}_{23}(36)^{-1}
   =\{7,10,11,15,17,19,20,21,22\}.
   \]

2. The Type-II condition including the genuine \(d\le x\) bound is equivalent
   to \(-1\in\mathcal R_{23}(x)\). A signed-ratio witness reconstructs
   coprime \(A,B\mid x\), then

   \[
   d=A^2C,\qquad C=x/(AB),
   \]

   so \(d\le x\) and \(23\mid x+d\) hold without a relaxed residue-only
   inference.

3. The non-coprime factor case is handled by exponent intervals:

   \[
   [-v_\ell(s)-1,v_\ell(s)+1]
   =[-1,1]+[-v_\ell(s),v_\ell(s)]
   \]

   at \(\ell=2,3\). Hence

   \[
   \mathcal R_{23}(6s)=
   \{1,2,3,4,6,8,12,13,16\}\mathcal R_{23}(s)
   \]

   even when \((s,6)>1\).

4. Combining the Type-I and Type-II conditions gives the two exact residual
   boxes:

   \[
   s\equiv5\pmod {23}\Longrightarrow
   \operatorname{MISS}_{23}
   \iff\mathcal R(s)\subseteq\{1,5,12,14\},
   \]

   \[
   s\equiv14\pmod {23}\Longrightarrow
   \operatorname{MISS}_{23}
   \iff\mathcal R(s)\subseteq\{1,2,5,14\}.
   \]

5. The finite q=1 G control \(p=21169\) was independently recomputed. Its
   six complete divisor-residue screens at gaps
   \(3,7,11,15,19,23\) all miss their Type-I and Type-II targets. Its
   Pocklington base-13 values and listed factorizations also replay.

An independent enumeration over \(1\le s\le10^4\), including values sharing
2 or 3 with the small factor, found no contradiction. That enumeration is a
sanity control only; the accepted result is the algebraic derivation above.

## Scope Boundary

The proof classifies every Bradford Type-I/II certificate at gap 23. It does
not show that other gaps or other terminal families miss, does not prove a
complete terminal schedule, and does not connect a certificate or miss to an
actual T6 source occurrence. In particular, the q=1 G condition constrains
\(6s-5\), not the full signed divisor-ratio box of \(s\); no cross-linear-form
coverage theorem was supplied.
