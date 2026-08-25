---
kind: claim
claim_id: type-I-f2-c8-qstar103-fixed-gap-cover-boundary
title: C8 q-star=103 两条必要射线的固定 gap 覆盖边界
statement: >-
  在 q-star=103 c=8 的两条必要射线
  p=9073+34608v 与 p=33793+34608v 上，Bradford 2026 明列的 k=0
  有限同余类族不是覆盖：存在两个 primitive arithmetic progressions
  preserving the exact q-star=103 roughness conditions and avoiding all listed
  classes, hence Dirichlet gives infinitely many core primes outside that finite
  congruence list. This result does not decide a finite menu of factor-dependent
  Bradford certificates d|((p+m)/4)^2; the least actual C8 residual therefore
  remains complete terminal-first MISS plus q=1 G, core, roughness, parent/path,
  and common E1/E3 admission guards.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-full-carrier-d-one-zero-k-capacity-ray-classification
  - type-II-q-one-full-carrier-qstar-103-rough-selection-criterion
  - bradford-2026-cover-gap
topics:
  - type-I
  - type-II
  - f2
  - c-eight
  - q-star-103
  - fixed-gap
  - covering-system
  - proof-boundary
sources:
  - claim: type-II-q-one-full-carrier-d-one-zero-k-capacity-ray-classification
    role: necessary-two-ray-normal-form
  - claim: type-II-q-one-full-carrier-qstar-103-rough-selection-criterion
    role: exact-roughness-guard
  - paper: bradford2026
    locator: "Lemma 1, Lemma 2, and the k=0 list"
    role: finite-congruence-list
visibility: public
last_checked: '2026-08-25'
---

# C8 q-star=103 两条必要射线的固定 gap 覆盖边界

## 1. 射线与 roughness

The necessary source rays are

\[
p_+(v)=9073+34608v,
\qquad
p_-(v)=33793+34608v.
\]

Their \(q_\star=103\) tails are

\[
6s_+(v)-1=103(42v+11),
\qquad
6s_-(v)-1=103(42v+41).
\]

The exact roughness guard is \(25\nmid(42v+c)\) and
\(\ell\nmid(42v+c)\) for every prime \(7\le\ell<103\), with \(c=11,41\)
respectively.

## 2. Explicit countercontrol for the listed finite congruences

Set

\[
R=25\prod_{7\le\ell<103}\ell,
\qquad L=8R.
\]

On the plus ray take \(v=26+Lw\); on the minus ray take \(v=6+Lw\). Then

\[
\begin{array}{c|c|c|c}
&p_0&s_0&42v_0+c\\
\hline
 +&908881&18935&1103\\
 -&241441&5030&293
\end{array}
\]

Since \(L\) is divisible by \(25\) and every prime \(7\le\ell<103\), the
roughness residues remain nonzero for every \(w\).

The \(p\)-progressions are

\[
p_+(26+Lw)=908881+34608Lw,
\]

\[
p_-(6+Lw)=241441+34608Lw.
\]

The relevant Bradford \(k=0\) classes are

\[
p\equiv29,41\pmod{44};\quad
p\equiv13,17\pmod{20};\quad
p\equiv5\pmod8;\quad
p\equiv93,137\pmod{140}.
\]

The two initial residues modulo \((44,20,8,140)\) are respectively

\[
(17,1,1,1),\qquad(13,1,1,81),
\]

so both progressions avoid every listed class. The step \(34608L\) is
divisible by all four moduli. Direct Euclidean calculation gives

\[
\gcd(908881,34608L)=\gcd(241441,34608L)=1.
\]

Therefore Dirichlet's theorem gives infinitely many prime terms in both
progressions. They are all \(1\pmod{24}\), hence core primes.

This is an infinite countercontrol for the named finite **congruence list**.
It is not a countercontrol for the complete factor-dependent Bradford screen.

## 3. Why this does not settle a full fixed-gap cover

For a fixed legal gap \(m\equiv3\pmod4\), put \(x_m=(p+m)/4\) and define

\[
\mathcal D_I(p,m)=\{d:d\mid x_m^2,\ m\mid px_m+d\},
\]

\[
\mathcal D_{II}(p,m)=\{d:d\mid x_m^2,\ d\le x_m,\ m\mid x_m+d\}.
\]

Avoiding finitely many congruence classes for \(p\) does not control the
factorization of \(x_m\), and therefore does not imply

\[
\mathcal D_I(p,m)=\mathcal D_{II}(p,m)=\varnothing.
\]

Conversely, proving that a finite set of fixed gaps has no such divisor for
every prime on either ray would be a new factor-dependent covering theorem;
the repository has no such theorem. The existing finite scans and q1 local
schedule cannot fill this quantifier.

## 4. Least C8 residual

For an actual terminal-first-surviving C8 parent, the smallest unresolved guard is

\[
\begin{aligned}
& p=p_+(v)\text{ or }p_-(v),\quad p\text{ core},
\quad \mathrm{rough}_{103}(v),\quad q=1\ G(p),\\
&\mathrm{MISS}_{\mathcal M}(p),\quad
\text{actual admitted parent/path and raw occurrence},
\end{aligned}
\]

where \(\mathcal M\) is the complete terminal-prefix menu and

\[
\mathrm{MISS}_{\mathcal M}(p)
\iff
\forall m\in\mathcal M,
\mathcal D_I(p,m)=\mathcal D_{II}(p,m)=\varnothing.
\]

If this MISS is real, the existing second-full-excess calculation provides a
deterministic arithmetic 'OTHER' target with \(9\le c_T\le p-2\); it does not
provide E1 source/path validity or E3 common admission. The 'DOUBLE_LOW' branch
likewise remains conditional on a complete source-bound candidate universe.

Hence the correct status is:

    named Bradford k=0 congruence list: NOT A COVER (established)
    complete factor-dependent fixed-gap cover: OPEN
    C8 TERMINAL/FAMILY_EMPTY: NOT ESTABLISHED
    C8 VERIFIED_SUCCESSOR: CONDITIONAL arithmetic only; E1/E3/re-entry open
