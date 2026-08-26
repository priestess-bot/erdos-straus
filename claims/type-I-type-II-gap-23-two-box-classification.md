---
kind: claim
claim_id: type-I-type-II-gap-23-two-box-classification
title: gap 23 的完整 Type I/II 两盒判据与偶 h 异常残余
statement: >-
  Let p=24h+1 be a core prime, s=h+1 and x=(p+23)/4=6s. Put
  T={7,10,11,15,17,19,20,21,22}, U(s)={u mod 23:u divides s^2}, and let
  R(s) be the complete signed divisor-ratio box modulo 23. A gap-23
  Bradford Type I certificate exists exactly when U(s) meets T, and a Type II
  certificate exists exactly when R(s) meets T. Hence, on the two even-h
  exceptional residue classes s=5,14 mod 23, a complete gap-23 Type I/II
  miss is exactly R(s) contained respectively in {1,5,12,14} or
  {1,2,5,14}; equivalently, s has exactly one simple prime factor congruent
  to s modulo 23 and every other prime factor is 1 modulo 23. This is a
  complete classification for the single gap-23 Bradford screen, not a
  complete terminal schedule or a T6 transition.
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
depends_on:
  - short-certificate-equivalence
  - type-II-coprime-factor-normal-form
  - type-II-factor-pair-carrier-strict-descent
  - type-II-gap-23-odd-h-qnr-terminal-descent
topics:
  - type-I
  - type-II
  - terminal-first
  - gap-twenty-three
  - divisor-residue
  - factor-pair
  - quadratic-residue
  - proof-boundary
sources:
  - claim: short-certificate-equivalence
    role: complete Bradford divisor reconstruction and Type-I residue form
  - claim: type-II-coprime-factor-normal-form
    role: Type-II coprime factor-pair reconstruction
  - claim: type-II-factor-pair-carrier-strict-descent
    role: gap-23 Type-II two-tail strict descent
  - claim: type-II-gap-23-odd-h-qnr-terminal-descent
    role: earlier odd-h quadratic-nonresidue subfamily
visibility: public
last_checked: '2026-08-27'
---

# gap 23 的完整两盒分类

## 1. Scope and notation

Let

\[
p=24h+1=24s-23,
\qquad s=h+1,
\qquad x=\frac{p+23}{4}=6s.
\tag{1}
\]

Since a core prime is not \(23\),

\[
p\equiv s\not\equiv0\pmod {23}.
\tag{2}
\]

Write

\[
T=\{7,10,11,15,17,19,20,21,22\}
=\operatorname{QNR}_{23}\setminus\{5,14\}.
\tag{3}
\]

There are two distinct finite residue boxes:

\[
\mathcal U(s)=\{u\bmod23:u\mid s^2\},
\tag{4}
\]

and the complete signed divisor-ratio box

\[
\mathcal R(s)=
\left\{ab^{-1}\pmod {23}:a,b\mid s,\ (a,b)=1\right\}.
\tag{5}
\]

Equivalently, if \(s=\prod_\ell\ell^{v_\ell(s)}\), then

\[
\mathcal R(s)=
\left\{
 \prod_\ell\ell^{a_\ell}\pmod {23}:
 -v_\ell(s)\le a_\ell\le v_\ell(s)
\right\}.
\tag{6}
\]

All sets in this card are finite and are determined by the complete
factorization of \(s\). They do not refer to a target state, a queue, or an
unknown unit-fraction solution.

## 2. Exact Type-I box

Let \(d\mid x^2\), and put \(e=x^2/d\). The Type-I condition at gap 23 is

\[
23\mid px+d.
\tag{7}
\]

Because \(p\equiv4x\pmod {23}\) and \(x\) is a unit modulo 23, (7) is
equivalent to

\[
e\equiv-4^{-1}\equiv17\pmod {23}.
\tag{8}
\]

Every divisor of \(36s^2\) can be written as \(cu\), where
\(c\mid36\) and \(u\mid s^2\), even when \(s\) has a factor 2 or 3. For
each prime \(\ell\), take

\[
v_\ell(c)=\min\{v_\ell(e),v_\ell(36)\},
\qquad
v_\ell(u)=v_\ell(e)-v_\ell(c).
\tag{9}
\]

The divisor residues of 36 are

\[
\operatorname{Div}_{23}(36)=\{1,2,3,4,6,9,12,13,18\},
\tag{10}
\]

and a direct multiplication gives

\[
17\operatorname{Div}_{23}(36)^{-1}=T.
\tag{11}
\]

It follows that

\[
\boxed{
\text{gap-23 Type I hit}
\Longleftrightarrow
\mathcal U(s)\cap T\ne\varnothing.
}
\tag{12}
\]

The reverse implication is constructive: for \(u\in\mathcal U(s)\cap T\),
choose \(c\mid36\) with \(cu\equiv17\pmod {23}\), take \(e=cu\), and set
\(d=x^2/e\). Equation (8), hence the complete Type-I reconstruction,
follows.

## 3. Exact Type-II box

The complete Type-II gap-23 criterion is equivalent to

\[
-1\in\mathcal R(x).
\tag{13}
\]

For completeness, choose coprime \(A,B\mid x\) with
\(A/B\equiv-1\pmod {23}\), exchange them if necessary so \(A\le B\), and
write \(C=x/(AB)\). Then

\[
d=A^2C\mid x^2,
\qquad d\le x,
\qquad x+d=AC(A+B)\equiv0\pmod {23}.
\tag{14}
\]

Conversely, the standard \(g=(d,x)\), \(A=d/g\), \(B=x/g\),
\(C=g/A\) reconstruction turns every Type-II divisor into such a signed
ratio. Thus (13) includes the real \(d\le x\) condition rather than merely
a residue relaxation.

The small factor has the inverse-closed ratio box

\[
\mathcal R(6)=
F=\{1,2,3,4,6,8,12,13,16\},
\qquad -F=T.
\tag{15}
\]

The equality

\[
\mathcal R(6s)=F\mathcal R(s)
\tag{16}
\]

also holds when \((s,6)>1\). At the primes 2 and 3 this follows from the
exact exponent-interval identity

\[
[-v_\ell(s)-1,v_\ell(s)+1]
=[-1,1]+[-v_\ell(s),v_\ell(s)].
\tag{17}
\]

Using the inverse closure of \(F\), equations (13)--(16) give

\[
\boxed{
\text{gap-23 Type II hit}
\Longleftrightarrow
\mathcal R(s)\cap T\ne\varnothing.
}
\tag{18}
\]

Because \(24\mid p-1\), every hit in (18) also has the established
factor-pair two-tail descent to

\[
n=\frac{p+23}{24}=s<p.
\tag{19}
\]

## 4. The two exceptional even-h boxes

The relation

\[
\mathcal U(s)=s\mathcal R(s)
\tag{20}
\]

rewrites the Type-I criterion as
\(\mathcal R(s)\cap s^{-1}T\ne\varnothing\). Therefore a complete
gap-23 Bradford miss is exactly

\[
\mathcal R(s)\cap\left(T\cup s^{-1}T\right)=\varnothing.
\tag{21}
\]

For the two quadratic-nonresidue classes not covered by the fixed small
divisor fan when \(h\) is even, \(s=h+1\) is odd and

\[
\begin{array}{c|c|c|c}
s\pmod {23}&s\pmod {46}&h\pmod {46}&p\pmod {1104}\\ \hline
5&5&4&97\\
14&37&36&865
\end{array}
\tag{22}
\]

The corresponding Type-I target boxes are

\[
5^{-1}T=\{2,3,4,6,8,9,13,16,18\},
\tag{23}
\]

and

\[
14^{-1}T=\{3,4,6,8,9,12,13,16,18\}.
\tag{24}
\]

Since each is disjoint from \(T\), equation (21) becomes the exact pair of
residual classifications

\[
\boxed{
s\equiv5\pmod {23}
\Longrightarrow
\operatorname{MISS}_{23}
\Longleftrightarrow
\mathcal R(s)\subseteq\{1,5,12,14\},
}
\tag{25}
\]

\[
\boxed{
s\equiv14\pmod {23}
\Longrightarrow
\operatorname{MISS}_{23}
\Longleftrightarrow
\mathcal R(s)\subseteq\{1,2,5,14\}.
}
\tag{26}
\]

Thus the older odd-\(h\) quadratic-nonresidue theorem leaves exactly these
two even-\(h\) divisor-ratio boxes within its fixed gap-23 screen. A prime
factor of \(s\) outside the corresponding four-element box is already a
constructive terminal witness through (12) or (18).

### Exact factorization inside the boxes

The displayed four-element boxes have a stronger, exact factorization form.
The signed ratio box is inverse closed. Let

\[
H=\{1,5,14\}.
\tag{27}
\]

For both residue classes,

\[
\{1,5,12,14\}\cap\{1,5,12,14\}^{-1}
=\{1,2,5,14\}\cap\{1,2,5,14\}^{-1}
=H.
\tag{28}
\]

Hence either residual condition in (25)--(26) first forces
\(\mathcal R(s)\subseteq H\). Every prime divisor \(\ell\mid s\) and its
inverse then lie in \(H\), so

\[
\ell\equiv1,\ 5,\ \text{or }14\pmod {23}.
\tag{29}
\]

Any \(5\)- or \(14\)-residue prime can occur only to exponent one, since

\[
5^2\equiv2,
\qquad14^2\equiv12\pmod {23},
\tag{30}
\]

and neither residue lies in \(H\). There cannot be two nontrivial factors:
two 5-residue factors give 2, two 14-residue factors give 12, and a
5-residue factor divided by a 14-residue factor gives

\[
5/14\equiv2\pmod {23}.
\tag{31}
\]

All three values would belong to \(\mathcal R(s)\), contradicting
\(\mathcal R(s)\subseteq H\).

Since \(s\equiv5\) or \(14\pmod {23}\), exactly one such prime factor must
remain. Therefore the two residual boxes are equivalently

\[
\boxed{
\operatorname{MISS}_{23}
\Longleftrightarrow
s=q\,u,\quad
q\parallel s,\quad
q\equiv s\pmod {23},\quad
\ell\mid u\Longrightarrow\ell\equiv1\pmod {23}.
}
\tag{32}
\]

Here \(q\) is prime and \(q\parallel s\) means that it occurs with exponent
one. Conversely, (32) gives
\(\mathcal R(s)=\{1,5,14\}\), so it is contained in the relevant box. This
factorization equivalence itself does not use the parity of \(h\); even
\(h\) is the subdomain in which the earlier fixed small-divisor fan leaves
these two classes.

There is also a strict obstruction to treating gap 23 as a universal exit.
If \(s\) itself is prime and \(s\equiv5\) or \(14\pmod {23}\), then

\[
\mathcal R(s)=\{1,5,14\},
\tag{33}
\]

which lies in the appropriate box in (25) or (26). Thus the complete
gap-23 Type-I/II screen misses. This conditional observation does not assert
that infinitely many such \(p=24s-23\) are prime, nor that any such prime is
q=1 G.

## 5. A q=1 finite-schedule control

The core prime

\[
p=21169=24\cdot882+1,
\qquad X=5293=67\cdot79
\tag{28}
\]

is ordinary q=1 G because both factors of \(X\) are \(1\pmod3\).
For a short primality check,

\[
p-1=2^4\cdot3^3\cdot7^2,
\]

and base \(13\) has

\[
13^{21168}\equiv1,\quad
13^{10584}\equiv21168,\quad
13^{7056}\equiv10710,\quad
13^{3024}\equiv20207\pmod p,
\]

with the final three values minus one coprime to \(p\); Pocklington's
criterion applies. It
misses the complete Type-I/II divisor screens at the six natural gaps through
23:

\[
\begin{array}{c|c|c|c|c}
m&x_m&\text{factorization of }x_m&e_{\rm I}&d_{\rm II}\\ \hline
3&5293&67\cdot79&2&2\\
7&5294&2\cdot2647&5&5\\
11&5295&3\cdot5\cdot353&8&7\\
15&5296&2^4\cdot331&11&14\\
19&5297&5297&14&4\\
23&5298&2\cdot3\cdot883&17&15
\end{array}
\tag{29}
\]

For each row, the complete residue set of divisors of \(x_m^2\) avoids both
displayed targets. In order, those sets are

\[
\begin{array}{c|c}
m&\{d\bmod m:d\mid x_m^2\}\\ \hline
3&\{1\}\\
7&\{1,2,4\}\\
11&\{1,3,4,5,9\}\\
15&\{1,2,4,8\}\\
19&\{1,15,16\}\\
23&\{1,2,3,4,6,8,9,12,13,16,18\}.
\end{array}
\tag{30}
\]

Here \(e_{\rm I}=-4^{-1}\pmod m\), while
\(d_{\rm II}=-x_m\pmod m\). Thus even the continuous finite prefix
\([3,7,11,15,19,23]\) has a genuine ordinary q=1 G all-miss control. It is a
negative control against calling that finite prefix a complete terminal
universe, not a counterexample to the Erdos--Straus conjecture or an assertion
that no other terminal family applies to \(21169\). Every factorization in
(29) is complete by trial division through its square-root bound.

## 6. Boundary

This theorem exactly classifies a single Bradford gap. The q=1 G condition
only constrains the factors of \(X=6s-5\), while the two boxes above use the
factorization of \(s\). Since

\[
\gcd(s,6s-5)=\gcd(s,5),
\tag{34}
\]

no existing q=1 G or registered-prefix theorem forces either residual box to
be empty. In its exact factor form, the remaining cross-linear question is
whether q=1 G and the registered prefix can coexist with the factorization
(32). A new cross-linear-form theorem would be needed for that.

This card does not create a target terminal receipt, prove a complete terminal
schedule, issue E1--E5, authorize a producer or queue, close a T6 residual,
or prove the Erdos--Straus conjecture.
