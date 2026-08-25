---
kind: claim
claim_id: type-I-f2-r-three-d-composite-terminal-ray
title: R=3 hard-core composite-D mixed terminal arithmetic ray
statement: >-
  Put (A,C,K)=(1,14,1), h=55, T=115 and L=5.  For every t>=0 for which
  p_t=769+1320t is prime, the parameters m_t=15+24t and B_t=14+24t
  satisfy the exact mixed-D quotient system with g=gcd(h,2p_t-3)=5,
  and reconstruct a legal Type-II terminal certificate.  Since gcd(769,1320)=1,
  Dirichlet gives infinitely many prime points in this arithmetic ray.  The
  ray is an arithmetic terminal family, not a proof that all its prime points
  satisfy the R=3 hard-core conditions.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f2-r-three-d-contact-completion-dichotomy
topics:
  - type-I
  - F2
  - R-three
  - hard-core
  - mixed-D
  - terminal-ray
  - proof-boundary
sources:
  - claim: type-I-f2-r-three-d-contact-completion-dichotomy
    role: exact quotient completion and certificate reconstruction
  - reproduction: reproductions/type_i_f2_r_three_d_contact_completion.py
    role: progression controls
visibility: public
last_checked: '2026-08-25'
---

# R=3 composite-D mixed terminal ray

This is a positive companion to the fixed-contact cofactor obstruction. It
shows that the composite-(D) stratum is not structurally empty.

Fix

\[
(A,C,K)=(1,14,1),
\quad h=4ACK-1=55,\quad T=8A^2C+3=115,\quad L=3K+2A=5.
\tag{1}
\]

For \(t\ge0\), set

\[
p_t=769+1320t,
\quad m_t=15+24t,\quad B_t=14+24t.
\tag{2}
\]

The defining identity is immediate:

\[
h m_t-4A^2C=55(15+24t)-56=p_t.
\tag{3}
\]

Moreover

\[
D_t=2p_t-3=5(307+528t),
\quad g=(h,D_t)=5,
\tag{4}
\]

and the quotient data are

\[
s=11,
\quad r=307+528t,
\quad t_q=23,
\quad \ell=1.
\tag{5}
\]

They satisfy

\[
r+t_q=2s m_t,
\quad t_q=4AC\ell-3s,\quad 2sB_t=Kr+\ell.
\tag{6}
\]

Thus whenever \(p_t\) is prime (automatically \(p_t\equiv1\pmod {24}\)),
the exact completion theorem reconstructs a legal Type-II certificate with

\[
x=A B_t C,\quad d=A^2C,\quad m=m_t.
\]

The progression is primitive because (gcd(769,1320)=1). Dirichlet's
theorem therefore supplies infinitely many prime points. This use of
Dirichlet concerns only the arithmetic ray; it does not assert that every
point is in the stricter R=3 hard-core subset (which also imposes factor
residue conditions on (p+4) and ((3p+1)/4)).

The result closes no F2 family by itself. It establishes a positive terminal
subfamily and prevents the incorrect structural claim that composite (D)
always gives an empty mixed-contact stratum.

Focused replay:

```bash
python3 reproductions/type_i_f2_r_three_d_contact_completion.py --verify
```
