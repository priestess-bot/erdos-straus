---
kind: claim
claim_id: type-I-c8-second-full-excess-lambda56-strict-capacity-ray
title: c8 second-full-excess target 的 lambda=56 strict-capacity ray
statement: >-
  在 c8 second-full-excess parent target 的 arithmetic domain，令
  75c=64+lambda p、D_lambda=94544+75lambda、beta=gcd(K,R-1)，且
  D_lambda c_next=4096beta+kappa p。则 c_next<c 当且仅当
  (75kappa-lambda D_lambda)p<64D_lambda-75(4096beta)。lambda=56 时
  p=31 mod75 强制 beta=2；再取 p=-1024 mod12343，则
  c_next=(p+1024)/12343<c=(56p+64)/75。该 strict-capacity ray 与 C8
  q-star=103 已知必要同余兼容，但只支付未来 actual rechart 的 arithmetic E5 部分，
  不提供 E1--E4、admission 或 T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-c8-second-full-excess-parent-anchored-next-capacity-residue-boundary
  - type-I-c8-second-full-excess-parent-anchored-target-pfree-overlap-compression
topics:
  - type-I
  - f2
  - c-eight
  - complete-excess
  - capacity
  - strict-descent
  - arithmetic-progression
  - proof-boundary
sources:
  - claim: type-I-c8-second-full-excess-parent-anchored-next-capacity-residue-boundary
    role: exact next-capacity residue formula and beta data
  - claim: type-I-c8-second-full-excess-parent-anchored-target-pfree-overlap-compression
    role: p-free fallback target and canonical capacity scope
visibility: public
last_checked: '2026-08-27'
---

# c8 second-full-excess target 的 lambda=56 strict-capacity ray

## 1. Exact comparison leaf

Use the c8 parent-anchored target notation

\[
75c=64+\lambda p,
\qquad
D_\lambda=94544+75\lambda,
\qquad
B=4096\beta,
\tag{1}
\]

where \(\beta=\gcd(K_T,R_T-1)\). The canonical next capacity is the
representative satisfying

\[
D_\lambda c_{\rm next}=B+\kappa p
\tag{2}

\]

for its uniquely determined integer \(\kappa\). Comparing (2) with (1)
gives the exact strictness criterion

\[
\boxed{
c_{\rm next}<c
\Longleftrightarrow
(75\kappa-\lambda D_\lambda)p
<64D_\lambda-75B.}
\tag{3}

\]

No factorization of \(R_T-1\) is used in (3).

## 2. The lambda=56 ray

Take \(\lambda=56\). The congruence \(\lambda p\equiv11\pmod{75}\)
is exactly

\[
p\equiv31\pmod{75}.
\tag{4}
\]

Since \(X=(p+1)/2\) is odd and
\(\gcd(c,X)\mid\lambda-64=-8\), the exact overlap formula forces

\[
\beta=2.
\tag{5}

\]

Consequently

\[
D_{56}=98744=8\cdot12343,
\qquad
B=8192=8\cdot1024,
\qquad
c=\frac{56p+64}{75}.
\tag{6}

Impose the additional congruence

\[
p\equiv-1024\pmod{12343}.
\tag{7}

Then

\[
c_{\rm next}=\frac{p+1024}{12343},
\qquad
\kappa=8,
\tag{8}

\]

because \(D_{56}c_{\rm next}=8192+8p\). This is the canonical
representative for the positive primes under consideration. Finally,

\[
12343(56p+64)-75(p+1024)
=691133p+713152>0,
\]

so

\[
\boxed{
\frac{p+1024}{12343}
<\frac{56p+64}{75}.}
\tag{9}

\]

Thus this ray has a strict next-capacity decrease.

## 3. Compatibility with the c8 arithmetic phase

The following simultaneous congruences are compatible:

\[
p\equiv1\pmod{48},
\quad p\equiv31\pmod{75},
\quad p\equiv9\pmod{103},
\quad p\equiv-1024\pmod{12343},
\quad p\equiv1\pmod7.
\tag{10}

\]

Their CRT class is

\[
\boxed{
p\equiv7550644081\pmod{10679163600},
\qquad
\gcd(7550644081,10679163600)=1.}
\tag{11}

\]

The first, third, and fifth congruences are respectively the core,
\(s\equiv86\pmod{103}\), and \(u\equiv1\pmod7\) arithmetic conditions.
The finite \(q_\star=103\) roughness exclusions can be appended as ordinary
CRT avoidance conditions without altering the conclusion of this claim.

## 4. Boundary

The ray proves only the arithmetic strictness required by the CHARGED part of
an E5 comparison, conditional on an actual canonical rechart being available.
It does not construct an actual C8 parent/path, terminal policy receipt, E1,
E2, E3, E4, common admission, re-entry, or a global T6 selector.
