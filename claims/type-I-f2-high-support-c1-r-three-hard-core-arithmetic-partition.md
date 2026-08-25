---
kind: claim
claim_id: type-I-f2-high-support-c1-r-three-hard-core-arithmetic-partition
title: R=3 G hard-core 11-character bridge and P-min mixed-gap partition
statement: >-
  Let p be a core prime, P=p+4, and N=(3p+1)/4. In the R=3 G hard core,
  where every prime divisor of P is 1 modulo 4 and every prime divisor of
  N is 1 modulo 3, one has 3P-4N=11, gcd(P,N)=1, p is not 7 modulo 11,
  and the Jacobi identity (33/N)=(P/11). This gives an exact 11-character
  split of N. If P is composite and h is its least prime divisor, then the
  legal gap m=3h has an exact Type I/II divisor-residue partition: Type I
  occurs exactly for a divisor d of x^2 with d=2 modulo 3 and
  d=-4^(-1) modulo h; Type II occurs exactly for d=2 modulo 3 and d=1
  modulo h, where x=(p+3h)/4. These are arithmetic screens only; they do
  not establish an actual C1 source, an ABSORB entry, a terminal for every
  hard-core prime, or F2/T6 closure.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f2-high-support-c1-r-three-terminal-g-split
  - type-I-type-II-mod-three-double-g-exit-obstruction
  - gap-residue-reachability
topics:
  - type-I
  - F2
  - high-support
  - cofactor-one
  - R-three
  - G-state
  - Jacobi-symbol
  - terminal-first
  - proof-boundary
sources:
  - claim: type-I-f2-high-support-c1-r-three-terminal-g-split
    role: defines the P/N hard-core residual
  - claim: gap-residue-reachability
    role: exact fixed-gap Type I/II criterion
  - reproduction: reproductions/type_i_f2_high_support_c1_r_three_hard_core_partition.py
    role: arithmetic identities and hard-core mixed-gap control
visibility: public
last_checked: '2026-08-25'
---

# R=3 G hard-core arithmetic partition

## 1. Exact hard-core domain

Put

\[
P=p+4,\qquad N=\frac{3p+1}{4}.
\tag{1}
\]

This card works only under the residual hypotheses left by the two existing
terminal screens:

\[
p\equiv1\pmod {24},\qquad
q\mid P\Longrightarrow q\equiv1\pmod4,
\qquad
q\mid N\Longrightarrow q\equiv1\pmod3.
\tag{2}
\]

The first condition says that the \(p+4\) terminal has missed; the second
says that the \(R=3\) chart is G. They do not say that the original
Erdos--Straus equation has no certificate by another route.

## 2. The 11 separation and character bridge

The two linear forms satisfy the exact identity

\[
\boxed{3P-4N=11.}
\tag{3}
\]

Thus \((P,N)\mid11\). If \(11\mid P\), then \(p\equiv7\pmod {11}\),
but \(11\equiv3\pmod4\) contradicts the first hard-core condition in (2).
Consequently

\[
\boxed{(P,N)=1,\qquad p\not\equiv7\pmod {11}.}
\tag{4}
\]

The excluded residue would in fact trigger both old terminal tests:
\(11\mid P\) is a \(p+4\) Type II terminal factor, while
\(11\mid N\) is a \(2\pmod3\) Type I terminal factor.

Because all prime factors of \(P\) are \(1\pmod4\), one has
\(P\equiv1\pmod4\). Using (3), quadratic reciprocity, and the fact that
\(4\) is a square gives

\[
\begin{aligned}
\left(\frac{33}{N}\right)
&=\left(\frac{P}{N}\right)
=\left(\frac{N}{P}\right)
=\left(\frac{-11}{P}\right)
=\left(\frac{11}{P}\right)
=\boxed{\left(\frac{P}{11}\right)}.
\end{aligned}
\tag{5}
\]

For completeness, modulo \(N\) equation (3) reads
\(P\equiv11\cdot3^{-1}\), whose Jacobi symbol is
\(\left(\frac{11}{N}\right)\left(\frac3N\right)\). Modulo \(P\), it
reads \(N\equiv-11\cdot4^{-1}\). Reciprocity has no sign because
\(P\equiv1\pmod4\), and the final reciprocity step between \(11\) and
\(P\) likewise has no sign. These are precisely the equalities in (5).

Here all Jacobi symbols are defined: (2) excludes \(3\mid N\), and (4)
excludes \(11\mid N\). Since a core prime is not \(0\pmod {11}\), the
hard-core residues split exactly as

\[
\begin{array}{c|c}
p\bmod11 & (33/N)\\ \hline
\{2,3,4,6,9\} & -1\\
\{1,5,8,10\} & +1.
\end{array}
\tag{6}
\]

In the first row, prime factors \(q\mid N\) with
\(\left(\frac{33}{q}\right)=-1\) occur with odd total multiplicity. This
is a genuine factor-character constraint on the G hard core, but it is not
yet an integer source occurrence or a terminal certificate.

## 3. Modulo-24 parity profiles

Let \(e_a\) be the parity of the total exponent of prime factors of \(P\)
congruent to \(a\pmod {24}\). Only \(a\in\{1,5,13,17\}\) can occur under
(2), and \(P\equiv5\pmod {24}\) gives exactly

\[
\boxed{(e_5,e_{13},e_{17})=(1,0,0)\quad\text{or}\quad(0,1,1).}
\tag{7}
\]

Likewise, write \(f_a\) for the parity of prime factors of \(N\) in
\(a\in\{7,13,19\}\pmod {24}\). The complete profile is

\[
\begin{array}{c|c}
p\bmod96&(f_7,f_{13},f_{19})\\ \hline
1 &(0,0,0)\text{ or }(1,1,1)\\
25&(0,0,1)\text{ or }(1,1,0)\\
49&(0,1,0)\text{ or }(1,0,1)\\
73&(1,0,0)\text{ or }(0,1,1).
\end{array}
\tag{8}
\]

Equations (7)--(8) are finite parity constraints, not assertions that a
particular residue-class factor can be consumed by an F2 producer.

## 4. P-min mixed-residue terminal screen

Suppose additionally that \(P\) is composite, and let

\[
h=\operatorname{spf}(P),\qquad m=3h,\qquad x=\frac{p+3h}{4}.
\tag{9}
\]

The hard-core condition makes \(h\equiv1\pmod4\), so \(m\equiv3\pmod4\)
and \(x\) is integral. Since \(h\le\sqrt{p+4}\) and \(p\ge73\),

\[
3\le m\le3\sqrt{p+4}\le p-2.
\tag{10}
\]

The fixed-gap criterion applies. Modulo \(3\), both of its targets are
\(2\): \(p\equiv x\equiv1\pmod3\). Modulo \(h\), use
\(p\equiv-4\pmod h\), hence \(x\equiv-1\pmod h\). Chinese remaindering
therefore gives the exact screen

\[
\begin{aligned}
\mathrm{Type\ I}
&\Longleftrightarrow
\exists d\mid x^2:
d\equiv2\pmod3,\quad d\equiv-4^{-1}\pmod h,\\
\mathrm{Type\ II}
&\Longleftrightarrow
\exists d\mid x^2:
d\equiv2\pmod3,\quad d\equiv1\pmod h.
\end{aligned}
\tag{11}
\]

For the Type II line, the paired-divisor argument in the fixed-gap criterion
automatically chooses a matching divisor not exceeding \(x\). A miss is a
deterministic `P_MIN_MIXED_RESIDUE_RESIDUAL`, not evidence that no other
terminal or successor exists.

## 5. Hard-core control and boundary

The existing double-G control

\[
p=118801,\qquad P=5\cdot23761,\qquad
N=89101,\qquad X=\frac{p+3}{4}=7\cdot4243
\tag{12}
\]

satisfies all of (2). It misses gaps \(3,7,\ldots,55\) and first has a
Type II certificate at gap \(59\). The complete legal `m=3h` menu obtained
from \(h\mid P\), namely \(h=1,5,23761\), also misses both fixed-gap
targets.  The \(h=1\) item is the pre-existing gap-3 screen; the P-min
screen in (11) is the nontrivial \(h=5\) item.
Thus neither the 11-character bridge nor the P-factor mixed-gap menu is a
closure theorem.

This card adds two exact screens to the R=3-G hard core. It does not give an
actual high-support C=1 parent E1 receipt, an ABSORB E3 serializer, a
non-upward re-entry theorem, a universal terminal, F2 closure, T6 closure,
or a proof of the conjecture.
