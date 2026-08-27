---
kind: claim
claim_id: type-II-q-one-gap23-residual-cross-linear-separation
title: q=1 G 与 gap-23 残余的跨线性支撑分离
statement: >-
  Let p=24s-23 be a core prime in the exact gap-23 residual factorization
  s=ell*u, ell||s, ell=s mod 23 in {5,14}, with every prime factor of u
  equal to 1 mod 23. If p is ordinary q=1 G, then 5 does not divide s and
  the prime supports of s, 6s-5, 3s-2, and 2s-1 are pairwise disjoint.
  Thus the residual factor cannot be transferred to the q=1 G or Bradford
  gap-7/gap-11 inputs through a common divisor. The ell=5 subleaf is empty.
  The gap-7 and gap-11 prefix misses have exact independent residue-box
  descriptions on 3s-2 and 2s-1. A concrete core-prime control shows these
  conditions can coexist, so this is a factor-separation theorem and
  no-go boundary, not a closure of the whole residual or T6.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-type-II-gap-23-two-box-classification
  - type-II-q-one-full-carrier-phase-root-entry
  - type-II-factor-pair-carrier-strict-descent
topics:
  - T6
  - q-one
  - gap-twenty-three
  - cross-linear
  - factor-separation
  - terminal-first
  - proof-boundary
sources:
  - claim: type-I-type-II-gap-23-two-box-classification
    role: exact residual factorization and p=53089 control
  - claim: type-II-q-one-full-carrier-phase-root-entry
    role: ordinary q=1 G factor semantics
  - claim: type-II-factor-pair-carrier-strict-descent
    role: complete factor-pair criterion for gaps 7 and 11
visibility: public
last_checked: '2026-08-27'
---

# q=1 G Gap-23 Residual Separation

## 1. Exact Domain

Let

\[
p=24s-23,\qquad X=6s-5,\qquad B=3s-2,\qquad C=2s-1.
\tag{1}
\]

Assume the complete gap-23 residual factorization from
type-I-type-II-gap-23-two-box-classification:

\[
s=\ell u,\qquad
\ell\parallel s,\qquad
\ell\equiv s\in\{5,14\}\pmod {23},\qquad
r\mid u\Longrightarrow r\equiv1\pmod {23},
\tag{2}
\]

where \(\ell\) is prime. Also assume the ordinary q=1 G condition:

\[
r\mid X\Longrightarrow r\equiv1\pmod3.
\tag{3}
\]

The symbol \(\ell\) in (2) is a residual prime factor of \(s\); it is not
the Type-II relation parameter \(q=1\).

## 2. Empty q=5 Subleaf

If \(5\mid s\), then

\[
5\mid X=6s-5.
\tag{4}
\]

But \(5\equiv2\pmod3\), contradicting (3). Hence

\[
\boxed{5\nmid s.}
\tag{5}
\]

Within the residual factorization (2), the only possible factor congruent to
5 modulo 23 is \(\ell\). Therefore the entire subleaf \(\ell=5\) is empty
under the q=1 G hypothesis.

The same factorization already excludes 2 and 3 from \(s\), so \(s\) is odd
and

\[
(s,6)=1.
\tag{6}
\]

## 3. Pairwise Support Separation

Equations (5)--(6) give

\[
(s,X)=(s,5)=1,\qquad
(s,B)=(s,2)=1,\qquad
(s,C)=1.
\tag{7}
\]

The remaining three pairs follow from

\[
X-2B=-1,\qquad
X-3C=-2,\qquad
2B-3C=-1.
\tag{8}
\]

Since \(X\) and \(C\) are odd, (8) yields

\[
\boxed{
\operatorname{supp}(s),\operatorname{supp}(X),
\operatorname{supp}(B),\operatorname{supp}(C)
\text{ are pairwise disjoint}.
}
\tag{9}
\]

In particular, each \(r\mid s\) satisfies

\[
X\equiv-5,\qquad B\equiv-2,\qquad C\equiv-1\pmod r.
\tag{10}
\]

Thus a residual factor of \(s\) cannot be reused as a prime factor of the
q=1 G input or of either later prefix input.

## 4. Exact Prefix Form

The q=1 G condition itself is exactly the complete gap-3 MISS:
every divisor of \(X^2\) is \(1\pmod3\), while both Bradford types require
residue \(2\pmod3\).

For gap 7, \(x_7=2B\). Put

\[
H_7=\{1,2,4\}\subset(\mathbb Z/7\mathbb Z)^\times.
\tag{11}
\]

The complete Type-I/II gap-7 condition reduces to

\[
\boxed{
\operatorname{MISS}_7
\Longleftrightarrow
\forall r\mid B,\quad r\bmod7\in H_7.
}
\tag{12}
\]

Indeed \(2\) is a quadratic residue modulo 7. Any nonresidue factor of
\(B\) gives the Type-II factor-pair certificate; if all factors are in
\(H_7\), every square divisor residue is also in \(H_7\), whereas both
Type-I and Type-II targets lie in its nonresidue coset.

For gap 11, \(x_{11}=3C\). Define the signed ratio box

\[
\mathcal R_{11}(C)=
\left\{
\prod_{r\mid C}r^{a_r}\pmod {11}:
-v_r(C)\le a_r\le v_r(C)
\right\},
\tag{13}
\]

and let \(N_{11}=\{7,8,10\}\). The complete joint criterion is

\[
\boxed{
\operatorname{MISS}_{11}
\Longleftrightarrow
\mathcal R_{11}(C)\cap
\left(N_{11}\cup C^{-1}N_{11}\right)=\varnothing.
}
\tag{14}
\]

For Type II, \(\mathcal R_{11}(3)=\{1,3,4\}\), so
\(-\mathcal R_{11}(3)^{-1}=N_{11}\). For Type I, the target residue is
\(8\), and the divisor residues of \(9\) produce the complementary
\(C^{-1}N_{11}\) term. This derives (14) without turning the finite prefix
into a complete terminal universe.

Therefore the residual plus current prefix has the exact normal form

\[
\text{gap-23 factor condition on }s
\quad+\quad
\text{G factor condition on }X
\quad+\quad
\text{QR}_7\text{ condition on }B
\quad+\quad
\text{ratio-box condition on }C,
\tag{15}
\]

with pairwise disjoint supports. It is factor separation, not a claim of
probabilistic independence.

## 5. Coexistence Control

The core prime

\[
p=53089,\qquad s=\ell=2213\equiv5\pmod {23}
\tag{16}
\]

satisfies the residual factorization, q=1 G, and the complete current prefix
MISS. Its q=1 G input is

\[
X=13273=13\cdot1021,
\qquad13,1021\equiv1\pmod3.
\tag{17}
\]

For the three prefix gaps:

\[
\begin{array}{c|c|c|c|c}
m&x_m&\operatorname{Div}_m(x_m^2)&e_{\rm I}&d_{\rm II}\\ \hline
3&13\cdot1021&\{1\}&2&2\\
7&2\cdot6637&\{1,2,4\}&5&5\\
11&3^2\cdot5^2\cdot59&\{1,3,4,5,9\}&8&2
\end{array}
\tag{18}
\]

Every target residue misses its complete divisor-residue set. The factorizations
are complete by trial division; the primality of \(53089\) is likewise
certified by trial division through its square-root bound.

Thus

\[
\exists p\,
\left[
\mathrm{G}(p)\land
\mathrm{Residual}_{23}(s)\land
\operatorname{MISS}_{3,7,11}(p)\land
\operatorname{MISS}_{23}(p)
\right].
\tag{19}
\]

It follows that the existing conditions cannot prove a contradiction or force
a certificate at gaps \(3,7,11,23\).

## 6. Boundary

This theorem closes only the \(\ell=5\) subleaf and rules out common-factor
transfer as a cross-linear proof strategy. It does not close the remaining
\(\ell\equiv5,14\pmod {23}\) residuals, discover a new terminal family,
construct an E1--E5 successor, or advance F1/F2/F3/T6 status.
