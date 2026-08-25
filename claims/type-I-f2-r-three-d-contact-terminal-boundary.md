---
kind: claim
claim_id: type-I-f2-r-three-d-contact-terminal-boundary
title: R=3 hard-core D-contact cannot directly carry a new Type II terminal
statement: >-
  Put D=2p-3 in the F2 R=3 hard core. Any Type II AC defining factor
  h=4ACK-1 which divides both D and Kp+A reduces to one of two cases: h=7,
  already preempted by the gap-7 terminal, or h=11, incompatible with the
  p+4 hard-core condition. Thus D cannot itself be a new Type II defining
  factor. A proper divisor q|D can only contact an AC factor through two
  exact congruences, and Type I D-contact has an analogous exact identity.
  These are terminal-search boundaries, not an exhaustive terminal theorem
  or a recursive E1/E3 route.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f2-high-support-c1-r-three-hard-core-arithmetic-partition
  - type-II-coprime-factor-normal-form
  - gap-residue-reachability
topics:
  - type-I
  - type-II
  - F2
  - R-three
  - hard-core
  - terminal
  - AC-normal-form
  - D-contact
  - proof-boundary
sources:
  - claim: type-I-f2-high-support-c1-r-three-hard-core-arithmetic-partition
    role: exact R=3 hard-core domain
  - claim: type-II-coprime-factor-normal-form
    role: AC Type II normal form
  - claim: gap-residue-reachability
    role: gap-7 terminal criterion
visibility: public
last_checked: '2026-08-25'
---

# R=3 hard-core D-contact terminal boundary

Let \(p\equiv1\pmod {24}\) be in the F2 \(R=3\) hard core and put

\[
D=2p-3,\qquad P=p+4.
\tag{1}
\]

Thus every prime factor of \(P\) is \(1\pmod4\), and the earlier fixed-gap
terminal rules have already been applied.

## 1. A defining factor cannot divide \(D\)

Consider a Type II AC factor in the usual form

\[
h=4ACK-1,\qquad h\mid Kp+A,\qquad A,C,K\ge1.
\tag{2}
\]

If also \(h\mid D\), then \(2p\equiv3\pmod h\). Multiplying the second
congruence in (2) by \(2\) gives

\[
3K+2A\equiv0\pmod h.
\tag{3}
\]

Consequently

\[
4ACK-1=h\le3K+2A.
\tag{4}
\]

The positive-integer solutions of the inequality in (4) are only

\[
(A,C,K;h)=(1,1,1;3),(1,1,2;7),(1,1,3;11),(2,1,1;7).
\tag{5}
\]

Substituting back into (3) removes the first two. Hence the only possible
defining-factor contacts are

\[
\boxed{(A,C,K;h)=(2,1,1;7),\quad (1,1,3;11).}
\tag{6}
\]

For \(h=7\), \(7\mid D\) means \(p\equiv5\pmod7\), which is already a
gap-7 terminal. Explicitly, with \(B=(p+2)/7\),

\[
\frac4p=\frac1{2B}+\frac1{2p}+\frac1{pB}.
\tag{7}
\]

For \(h=11\), \(11\mid D\) means \(p\equiv7\pmod {11}\), so
\(11\mid P=p+4\). This contradicts the hard-core condition because
\(11\equiv3\pmod4\). Therefore no hard-core terminal can arise by simply
taking the full Type II defining factor \(h\) to divide \(D\).

## 2. The residual mixed Type II contact

Let \(q>1\) divide \(D\). Then \((q,3p)=1\), and the two partial contacts

\[
q\mid4ACK-1,\qquad q\mid Kp+A
\tag{8}
\]

are equivalent to

\[
\boxed{
3K+2A\equiv0\pmod q,\qquad
8A^2C+3\equiv0\pmod q.}
\tag{9}
\]

Indeed, (8) implies the first congruence as above; eliminating \(A\) from
the first congruence and \(4ACK\equiv1\) gives the second. The same steps
reverse because \(2p\equiv3\pmod q\). Condition (9) does not imply the
remaining cofactor \(h/q\) divides \(Kp+A\), nor does it establish the
positivity/order conditions of a Type II certificate. Thus any surviving
\(D\)-mediated Type II route must be a genuine mixed completion with
\(q\) only a proper factor of \(h\).

## 3. The parallel Type I contact identity

For a Type I normal form satisfying

\[
p=4ABC-m,\qquad (A,B)=1,\qquad m\mid(Bp+A),
\tag{10}
\]

one has \(m\mid4B^2C+1\), and exactly

\[
\boxed{m\mid D\Longleftrightarrow m\mid(2A+3B).}
\tag{11}
\]

Modulo \(m\), use \(4B^2C\equiv-1\) and

\[
D=2p-3\equiv8ABC-3\equiv-2AB^{-1}-3.
\tag{12}
\]

Multiplication by \(B\) proves one direction. Conversely,
\(2A\equiv-3B\) gives
\(8ABC=4BC(2A)\equiv-12B^2C\equiv3\pmod m\), proving the other.

This does not rule out Type I certificates with \(m\nmid D\), nor mixed
Type II completions. It says only that a fixed Type I or Type II template
cannot turn an arbitrary growing factor of \(D\) into a universal new
hard-core terminal.
