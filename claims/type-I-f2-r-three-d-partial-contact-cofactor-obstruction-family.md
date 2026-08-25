---
kind: claim
claim_id: type-I-f2-r-three-d-partial-contact-cofactor-obstruction-family
title: R=3 hard-core composite-D partial-contact cofactor obstruction family
statement: >-
  For the fixed AC template (A,C,K)=(1,46,17), put h=3127=53*59,
  T=371=53*7, L=53 and p_t=505+1272t.  For every t>=0 for which p_t is a
  core prime, q=53 gives the two mixed-D partial-contact congruences
  q|D_t, q|h and q|(Kp_t+A), equivalently q|L and q|T.  Completion through
  the full h/q cofactor requires 59|(13+24t), equivalently t=56 mod59.
  Hence every core-prime member with t not congruent to 56 mod59 is a
  genuine partial-contact but cofactor-empty candidate for this fixed q.
  The result does not exclude another q or prove global R=3 terminality.
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
  - hard-core
  - mixed-D
  - partial-contact
  - cofactor-obstruction
  - proof-boundary
sources:
  - claim: type-I-f2-r-three-d-contact-completion-dichotomy
    role: exact mixed-D quotient completion gate
  - reproduction: reproductions/type_i_f2_r_three_d_contact_completion.py
    role: arithmetic progression and core-prime controls
visibility: public
last_checked: '2026-08-25'
---

# R=3 hard-core partial-contact cofactor obstruction

This card isolates a repeatable failure of the two partial congruences in the
composite-(D) branch. It is useful because it separates a genuine contact
with (D=2p-3) from a completed Type-II certificate.

## Fixed template

Take

\[
(A,C,K)=(1,46,17).
\]

The associated quantities are

\[
h=4ACK-1=3127=53\cdot59,
\quad T=8A^2C+3=371=53\cdot7,
\quad L=3K+2A=53.
\tag{1}
\]

For \(t\ge0\), define

\[
p_t=505+1272t,
\quad D_t=2p_t-3=53(19+48t).
\tag{2}
\]

Every \(p_t\) is \(1\pmod {24}\). If \(p_t\) is additionally a core prime,
the tuple is in the same R=3 hard-core arithmetic domain used by the mixed-D
completion theorem.

## Partial contact is automatic

For \(q=53\), equations (1)--(2) give \(q\mid D_t,h,T,L\). The equivalence

\[
q\mid h\text{ and }q\mid(Kp+A)
\quad\Longleftrightarrow\quad
q\mid L\text{ and }q\mid T
\tag{3}
\]

therefore holds for every \(t\). Thus this progression supplies an infinite
arithmetic family of partial-contact candidates before any primality
subselection. It is not a claim that all members are prime.

## Exact cofactor gate

For this template,

\[
p_t+4A^2C=689+1272t=53(13+24t).
\tag{4}
\]

The full defining factor is \(h=53\cdot59\). Consequently the missing
\(h/q=59\) cofactor divides the right side of (4) exactly when

\[
59\mid13+24t
\quad\Longleftrightarrow\quad
t\equiv56\pmod {59}.
\tag{5}
\]

For every core-prime member with \(t\not\equiv56\pmod {59}\), the \(q=53\)
partial contact cannot complete to the exact mixed-D quotient system. In the
terminology of the completion claim, this is a `COFACTOR_EMPTY` leaf for the
fixed contact (q), not a terminal certificate by itself.

The progression contains many core-prime controls, including

\[
p=1777,\ 22129,\ 33577,\ 47569,\ 55201,\ 60289,\
84457,\ 117529,\ 118801,\ 142969,
\]

all with (t\not\equiv56\pmod {59}). These examples only witness that the
obstruction occurs inside the hard-core congruence domain; the universal
content is the exact progression identity (3)--(5).

## Boundary

The result does **not** say that \(q=53\) is the only divisor of \(D_t\), that
another divisor cannot yield a completed Type-II certificate, or that the
entire R=3 state is terminal. It only proves that the frequently used
partial-contact test is insufficient on a whole arithmetic progression and
that the missing cofactor must be checked before any terminal admission.

Focused replay:

```bash
python3 reproductions/type_i_f2_r_three_d_contact_completion.py --verify
```
