---
kind: claim
claim_id: type-I-f2-r-three-d-fixed-prime-arithmetic-scheduler
title: R=3 composite-D fixed-prime arithmetic contact scheduler
statement: >-
  Fix a core prime p congruent to 1 modulo 24 and D=2p-3. All Type-II
  AC-normal-form contacts with 1<gcd(h,D)<h are in a finite table of triples
  (A,C,h) satisfying A^2 C <= (p-5)/4, h | (p+4A^2 C),
  3 <= h <= (2p-5)/3 and h congruent to -1 modulo 4AC. Setting
  K=(h+1)/(4AC), m=(p+4A^2 C)/h and B=Km-A, each table row failing
  m congruent to 3 modulo 4, 3<=m<=p-2, B>=A or gcd(A,B)=1 is FAMILY_EMPTY;
  every remaining row with 1<gcd(h,D)<h reconstructs a legal Type-II
  terminal certificate. Rows with gcd(h,D)=1 are non-D-contact and rows
  with gcd(h,D)=h belong to the already separated full-contact branch.
  This is an arithmetic per-prime coverage theorem, not an E1/runtime or
  global F2 closure theorem.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f2-r-three-d-contact-completion-dichotomy
  - type-I-f2-r-three-d-contact-terminal-boundary
topics:
  - type-I
  - F2
  - R-three
  - composite-D
  - arithmetic-scheduler
  - finite-divisor-table
  - terminal
  - proof-boundary
sources:
  - claim: type-I-f2-r-three-d-contact-completion-dichotomy
    role: exact normal form and mixed-D quotient system
  - reproduction: reproductions/type_i_f2_r_three_d_fixed_prime_scheduler.py
    role: finite-table controls and certificate reconstruction
visibility: public
last_checked: '2026-08-25'
---

# R=3 composite-D fixed-prime arithmetic scheduler

This result closes the arithmetic enumeration of the composite-D contact
subproblem for one fixed prime. It does not claim that an actual selector has
already supplied the source occurrence or terminal-first receipt.

## Finite table

Fix a core prime \(p\equiv1\pmod {24}\) and put

\[
D=2p-3,\qquad M_{A,C}=p+4A^2C.
\]

Define the finite table

\[
\mathcal H_p=
\left\{(A,C,h):
\begin{array}{l}
A,C\ge1,\quad 4A^2C\le p-5,\\
h\mid M_{A,C},\quad
3\le h\le(2p-5)/3,\\
h\equiv-1\pmod {4AC}
\end{array}
\right\}.
\tag{1}
\]

For a row in \(\mathcal H_p\), set

\[
K=\frac{h+1}{4AC},\qquad
m=\frac{M_{A,C}}h,\qquad
B=Km-A.
\tag{2}
\]

The deterministic row order is lexicographic in \((A,C,h)\), followed by the
guards in this order:

1. \(m\equiv3\pmod4\) and \(3\le m\le p-2\);
2. \(B\ge A\);
3. \(\gcd(A,B)=1\);
4. \(g=\gcd(h,D)\).

Failure of any of the first three guards is FAMILY_EMPTY for that row. If
\(g=1\), the row is not a \(D\)-contact. If \(g=h\), it is delegated to the
previously isolated full-contact branch. The only new terminal leaf is
\[
1<g<h.
\]

## Proof of exactness

For a legal Type-II AC normal form,

\[
x=ABC,\qquad d=A^2C,\qquad
h=4ACK-1,\qquad B=Km-A,
\]

and the defining identity is

\[
hm=p+4A^2C=M_{A,C}.
\tag{3}
\]

The mixed-D bound already proved for this normal form gives

\[
4A^2C\le p-5,\qquad
h\le(2p-5)/3.
\tag{4}
\]

Thus every genuine contact occurs in \(\mathcal H_p\), and (2) recovers its
original \(K,m,B\) uniquely. This proves the forward inclusion.

Conversely, take a row passing the first three guards and \(1<g<h\). Equation
(3) holds by construction, \(h=4ACK-1\) holds by (2), and
\(B=Km-A\) gives
\[
A+B=Km.
\]
The order and coprimality guards make the AC normal form legal. The standard
reconstruction
\[
x=ABC,\quad d=A^2C,\quad
y=\frac{p(x+d)}m,\quad
z=\frac{p(x+x^2/d)}m
\]
then yields an exact Type-II certificate for \(4/p\). Since \(1<g<h\), it is
in the mixed-D branch. This proves the reverse inclusion.

Therefore, for each fixed \(p\), the table is an exhaustive arithmetic
dichotomy:

\[
\text{row failure}\Longrightarrow\mathrm{FAMILY\_EMPTY},
\qquad
1<g<h\Longrightarrow\mathrm{TERMINAL}.
\]

The theorem is deliberately not an E1 statement: it does not prove that every
row is reached by the current selector, nor does it provide a shared runtime
queue, terminal-first receipt, E3 admission or recursive re-entry. Across
varying \(p\), it also does not say that the table is always nonempty.

Focused replay:

~~~bash
python3 reproductions/type_i_f2_r_three_d_fixed_prime_scheduler.py --verify
~~~
