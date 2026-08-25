---
kind: claim
claim_id: type-I-t6-f3-tr1-r-four-dyadic-fresh-exclusion
title: R4 h-supported TR1 has no dyadic-fresh subleaf
statement: >-
  In the R4 h-supported TR1 domain, m=3 and p,h are odd. Therefore
  D=3p+1-h is odd, so D_star is odd and 2 cannot divide gcd(D_star,E).
  This removes only the R4 dyadic-fresh branch; it does not supply a terminal,
  source occurrence, physical TR1 transition, or closure of R4/R6.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - t6-f3-proper-root-domain-v1
  - type-I-t6-f3-tr1-fresh-dstar-endpoint-split
topics:
  - type-I
  - F3
  - TR1
  - R-four
  - dyadic
  - proper-root
  - proof-boundary
sources:
  - concept: t6-f3-proper-root-domain-v1
    role: R4 m-equals-three quantifier
  - claim: type-I-t6-f3-tr1-fresh-dstar-endpoint-split
    role: dyadic-fresh discriminator
visibility: public
last_checked: '2026-08-25'
---

# R4 dyadic-fresh exclusion

In the R4 h-supported domain, \(m=3\), while a core prime \(p\) and a
root height \(h=3u\) are both odd. Hence

\[
D=mp+1-h=3p+1-h
\tag{1}
\]

is odd. Since

\[
D_*=\frac{D}{(D,h^2-1)}
\tag{2}
\]

is a divisor of \(D\), it too is odd. Therefore

\[
\boxed{2\nmid D_*,\qquad 2\nmid(D_*,E).}
\tag{3}
\]

The dyadic-fresh first-child analysis belongs only to the \(m>3\) R6 branch.
Equation (3) does not turn an R4 state into a terminal or a physical TR1
edge; all non-dyadic occurrence, terminal-priority, admission and re-entry
obligations remain.
