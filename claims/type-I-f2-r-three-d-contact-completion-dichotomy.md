---
kind: claim
claim_id: type-I-f2-r-three-d-contact-completion-dichotomy
title: R=3 hard-core D-contact completion dichotomy
statement: >-
  In the F2 R=3 hard core with D=2p-3, every genuine Type-II AC defining
  contact with D is exactly parameterized by a tuple
  h=4ACK-1, B=Km-A, m=(A+B)/K, and g=gcd(h,D) with 1<g<h.
  Writing h=g*s, D=g*r, T=(8A^2C+3)=g*t and L=(3K+2A)=g*ell,
  completion is equivalent to B=(K*r+ell)/(2*s) being a positive integer,
  B>=A and gcd(A,B)=1, together with the legal core/order conditions.
  If D is prime, g=1 and the mixed family is empty. Composite D has genuine
  positive controls, so no structural empty theorem follows; partial q-contact
  alone is not a certificate.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-f2-r-three-d-contact-terminal-boundary
  - type-II-coprime-factor-normal-form
  - type-I-f2-high-support-c1-r-three-hard-core-arithmetic-partition
topics:
  - type-I
  - type-II
  - F2
  - R-three
  - hard-core
  - mixed-completion
  - AC-normal-form
  - D-contact
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_f2_r_three_d_contact_completion.py
    role: exact parameterization, terminal controls and partial-contact countercontrol
  - claim: type-I-f2-r-three-d-contact-terminal-boundary
    role: D-prime and full-factor boundary
visibility: public
last_checked: '2026-08-25'
---

# R=3 hard-core D-contact completion dichotomy

Let \(p\equiv1\pmod {24}\) be in the R=3 hard core and put

\[
D=2p-3.
\tag{1}
\]

Use the Type-II coprime normal form

\[
x=ABC,\qquad d=A^2C,\qquad (A,B)=1,\qquad A\le B,
\qquad m=\frac{A+B}{K}\in\mathbb N,
\tag{2}
\]

and define

\[
h=4ACK-1,\qquad B=Km-A.
\tag{3}
\]

The defining identity is

\[
h\,m=p+4A^2C,
\qquad p=hm-4A^2C.
\tag{4}
\]

Set

\[
T=8A^2C+3,\qquad L=3K+2A.
\tag{5}
\]

Direct elimination gives

\[
D+T=2hm,\qquad
T=4ACL-3h,
\tag{6}
\]

and \((h,4AC)=1\). Consequently

\[
(h,D)=(h,T)=(h,L).
\tag{7}
\]

For any \(q\mid D\), \(q>1\), the partial contact conditions are exactly

\[
q\mid h\ \text{and}\ q\mid(Kp+A)
\Longleftrightarrow
q\mid L\ \text{and}\ q\mid T,
\tag{8}
\]

because \(2(Kp+A)\equiv3K+2A=L\pmod q\) and
\(T=4ACL-3h\). These are only partial contacts; the \(h/q\) cofactor
and the \(B\), order and gcd gates in (11) are still required.

Let

\[
g=(h,D).
\tag{9}
\]

If \(1<g<h\), write

\[
h=gs,\quad D=gr,\quad T=gt,\quad L=g\ell.
\tag{10}
\]

Dividing (6) and \(hB=Kp+A\) gives the exact quotient system

\[
\boxed{r+t=2sm,\qquad t=4AC\ell-3s,\qquad
2sB=Kr+\ell.}
\tag{11}
\]

Thus completion is equivalent to

\[
\boxed{B=\frac{Kr+\ell}{2s}\in\mathbb N,\qquad
B\ge A,\qquad (A,B)=1,}
\tag{12}
\]

with \(m=(A+B)/K\) and the original core/order conditions. The equivalence
retains the full \(h/g\) and \(D/g\) cofactors; neither \(g\) nor \(h/g\)
may be discarded.

Conversely, any positive tuple satisfying (2), (4), (9)--(11), with \(p\)
  core prime and \(m\equiv3\pmod4\), reconstructs a legal Type-II certificate:
\(p+m=4ABC\), \(d=A^2C\mid x^2\), \(d\le x\), and
  \(m\mid x+d=AC(A+B)\). This is an exact parameterization, not merely a
necessary congruence filter.

## Prime-D empty stratum

For \(B\ge A\), \(m\ge3\), and \(p=4ABC-m\), first note the exact
identity

\[
D-hm=4AC(B-A)-(m+3).
\tag{13}
\]

Put \(e=B-A\ge0\). The case \(e=0\) would force \(A=B=1\) by
\((A,B)=1\), and then \(m=2/K<3\), impossible. For \(e\ge1\),
\(m\le2A+e\), so

\[
D-hm\ge(4Ce-2)A-e-3.
\tag{14}
\]

The only nonpositive small parameter cases in (13) are
\((A,C,e)=(1,1,1)\) and \((2,1,1)\), which give respectively
\((p,m)=(5,3)\) and \((19,5)\), not core primes. Thus \(hm<D\) in the
core domain.

Also,

\[
A^2C\le ABC=\frac{p+m}{4},
\qquad
hm=p+4A^2C\le2p+m.
\tag{15}
\]

Hence \(h\le(2p-5)/3<D\) for core \(p>3\). If \(D\) is prime, any
\(g>1\) dividing \(D\) would equal \(D\), contradicting \(h<D\). Therefore

\[
\boxed{D\ \mathrm{prime}\Longrightarrow
\text{the genuine mixed-D Type-II family is empty}.}
\tag{16}
\]

The control \(p=2521\) has \(D=5039\) prime and lies in the hard core, so
this is a genuine residual reduction rather than a sampled absence.

The parity is slightly sharper. Both \(D\) and \(hm\) are odd, and the
strict inequality gives \(D-hm\ge2\). Hence every legal core tuple obeys

\[
\boxed{4A^2C\le p-5,\qquad
h\le\frac{2p-5}{m}\le\frac{2p-5}{3}.}
\tag{17}
\]

This is a parameter bound for the exact mixed-completion system, not a
certificate for every core prime.

## Composite controls and boundary

The family is not empty for composite \(D\). Examples include:

\[
\begin{array}{c|c|c|c|c|c}
p&A&B&C&K&m\\ \hline
769&1&14&14&1&15\\
21937&1&2771&2&12&231\\
20809&1&1308&4&11&119
\end{array}
\]

Each row satisfies (2)--(11) and reconstructs a Type-II certificate. In
contrast, \(p=118801,A=1,C=46,K=17\) has two partial congruences at
\(q=53\mid D\), but (11) gives nonintegral \(B\); \(p=1009\) fails
\(B\ge A\), and \(p=769,A=3,C=1,K=3\) fails \((A,B)=1\).

Therefore the exact remaining F2 arithmetic leaf is the composite-D
completion system (11), followed by terminal-first and actual source/E1
requirements. This claim does not prove terminal totality, common admission,
or F2/T6 closure.
