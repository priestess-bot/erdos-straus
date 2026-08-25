---
kind: claim
claim_id: type-I-t6-f3-tr1-dstar-freshness-capacity-gate
title: R4/R6 h-supported transverse D-star factors have an exact freshness-capacity gate
statement: >-
  For an actual low proper-root stutter receipt in R4 or R6 with k_perp=1,
  every q dividing D_star is also T- and A-supported. Its canonical maximal
  normalization is fresh exactly when v_q(R-h)>v_q(K), equivalently q divides
  the canonical E multiplier, and is capacity-saturated otherwise. The exact
  gate is q|E iff p*sigma=-1 mod q, where E=1+p*sigma and
  sigma*D=2T-(m+2r). The p+1, p-1, and pure-T branches give the valuation
  tables below. k_perp=1 does not imply freshness. Existing q-primary controls
  realize both fresh and saturated valuation patterns but are explicitly
  nonactual root receipts; no actual R4/R6 saturation example is claimed.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t6-f3-h-supported-canonical-carrier-partition
  - type-I-t6-f3-tr1-fresh-dstar-endpoint-split
  - type-I-root-capacity-stutter-receipt-factor-split
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-I-root-capacity-stutter-transverse-overlap-complete-excess-valuation-classification
  - type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
topics:
  - type-I
  - F3
  - TR1
  - R4
  - R6
  - proper-root
  - D-star
  - freshness
  - capacity-saturation
  - valuations
  - provenance
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-receipt-factor-split
    role: canonical primewise maximality formula
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: D-star divides T and transverse coprimality
  - claim: type-I-root-capacity-stutter-transverse-overlap-complete-excess-valuation-classification
    role: p-plus-one and p-minus-one valuation tables
  - claim: type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
    role: pure-T capacity split and q-primary controls
visibility: public
last_checked: '2026-08-25'
---

# R4/R6 transverse freshness versus capacity saturation

## 1. Scope and notation

Fix an `ACTUAL_PERSISTENT` low proper-root stutter receipt after the complete
terminal-first prefix has missed, in either

\[
R4:\ m=3,\quad 5\nmid D_*;
\qquad
R6:\ m>3,
\tag{1}
\]

with

\[
2\le h=3u<p,\qquad k>1,\qquad k_\perp=1,
\qquad
D_*={D\over(D,h^2-1)}>1.
\tag{2}
\]

The condition \(k_\perp=1\) says that every prime of the primitive quotient
\(k\) divides \(h\). It does not refer to the support capacity of the root
chart. Use

\[
A={p+1\over2}T,\qquad
K=A(p-1),\qquad
z=R-h=ED,
\tag{3}
\]

and, for \(q\mid D_*\), write

\[
\delta=v_q(D),\quad s=v_q(h^2-1),\quad
\tau=v_q(T),\quad \zeta=v_q(z),
\quad a=v_q(A),\quad c=v_q(p-1).
\tag{4}
\]

Since the established transverse divisor theorem gives \(D_*\mid T\), every
\(q\mid D_*\) also divides \(T\) and \(A\). Since \((D_*,h)=1\), such a \(q\)
is outside the primitive h-support; this still does not determine its q-adic
height in \(z\).

## 2. Exact canonical split

The maximal complete-excess normalization is primewise:

\[
(v_q(D),v_q(E))=
\begin{cases}
(\zeta,0),&\zeta\le a+c,\\
(a,\zeta-a),&\zeta>a+c.
\end{cases}
\tag{5}
\]

Consequently, for every \(q\mid D_*\),

\[
\boxed{
q\mid E\Longleftrightarrow \zeta>a+c
\Longleftrightarrow q\text{ is fresh},}
\tag{6}
\]

and

\[
\boxed{
q\nmid E\Longleftrightarrow \zeta=\delta\le a+c
\Longleftrightarrow q\text{ is capacity-saturated}.}
\tag{7}
\]

There is also an exact source-readable unit gate. Actual stutter identities
give

\[
E=1+p\sigma,\qquad
\sigma D=2T-(m+2r),
\tag{8}
\]

and the root-chart identity can be written

\[
z=D+p\bigl(2T-(m+2r)\bigr)=D(1+p\sigma).
\tag{9}
\]

Thus

\[
\boxed{q\mid E\Longleftrightarrow p\sigma\equiv-1\pmod q.}
\tag{10}
\]

Equivalently, after putting \(\widehat D=D/q^\delta\) and

\[
\widehat S={2T-(m+2r)\over q^\delta},
\tag{11}
\]

one has \(z/q^\delta=\widehat D+p\widehat S\); the congruence

\[
\widehat D+p\widehat S\equiv0\pmod q
\tag{12}
\]

is exactly the first fresh layer. This is a receipt-unit condition, not an E1
occurrence theorem.

## 3. Branch tables

For the \(p+1,h-1,m\) overlap, put

\[
b=v_q(m)=v_q(p+1)=v_q(h-1),\qquad t=\delta-b>0.
\tag{13}
\]

Then \(a=b+\tau\), \(c=0\), and

\[
\boxed{q\mid E\Longleftrightarrow \tau=t,\ \zeta>b+t;\qquad
q\nmid E\Longleftrightarrow \tau\ge t,\ \zeta=b+t.}
\tag{14}
\]

For the \(p-1,h+1,m+2\) overlap, put

\[
b=v_q(m+2)=v_q(p-1)=v_q(h+1),\qquad t=\delta-b>0.
\tag{15}
\]

Then \(a=\tau\), \(c=b\), and

\[
\boxed{q\mid E\Longleftrightarrow \tau=b+t,\ \zeta>2b+t;\qquad
q\nmid E\Longleftrightarrow \tau\ge t,\ \zeta=b+t.}
\tag{16}
\]

In the pure-\(T\) transverse branch \(q\nmid p^2-1\), one has \(a=\tau\),
\(c=0\), hence

\[
\boxed{q\mid E\Longleftrightarrow \zeta>\tau,\qquad
q\nmid E\Longleftrightarrow \zeta\le\tau.}
\tag{17}
\]

The \(q\mid m+2,2p+1\) branch belongs here and must not be silently merged
with the \(p-1\) overlap.

## 4. Why \(k_\perp=1\) does not close the gate

For \(q\mid D_*\), \((q,h)=1\), so \(k_\perp=1\) only implies
\(q\nmid k\). The capacity quantities in (4), and the receipt unit
\(\sigma\bmod q\) in (10), are not fixed by that primitive quotient support.

The existing pure-\(T\) controls exhibit both compatible local patterns:

\[
\begin{array}{c|cccc|c}
\text{control}&\tau&\delta&\epsilon=v_q(E)&\zeta&\text{disposition}\\ \hline
\texttt{T-slack}&2&1&0&1&\text{capacity-saturated}\\
\texttt{high-excess E}&1&1&2&3&\text{fresh}
\end{array}
\tag{18}
\]

Both are \(p=313,q=17,m=4\) q-primary controls from the focused relay
reproduction. They are deliberately not actual root receipts: their height
payloads do not satisfy the full \(h\mid p^2+p+1\) root condition and their
\(D\) is a synthetic q-primary divisor. They refute only the valuation-only
inference, not the conjecture or an actual R4/R6 state.

As a separate domain-boundary control, the canonical chart
\(p=283,r=550,h=1101,D=32,D_*=4\) has \(q=2\) saturated with
\(v_2(z)=v_2(K)=5\) and \(v_2(E)=0\), but lies outside the core-prime and
low-height domain. No actual R4/R6 saturated receipt is claimed here.

## 5. Consequences for TR1

Two established local terminal implications must be applied before a freshness
decision can create a TR1 residual:

\[
q\mid(D_*,m),\quad q\equiv3\pmod4
\Longrightarrow\text{ direct Type-I terminal},
\tag{18a}
\]

and

\[
q\mid(D_*,m+2,2p+1),\quad q\equiv5\pmod8
\Longrightarrow\text{ direct Type-II terminal}.
\tag{18b}
\]

Thus a terminal-first MISS removes these two residue subdomains from the
remaining saturated or fresh-factor search. The complementary (p-1,h+1)
overlap and the other pure-(T) residues remain open.

The full (W_y) word is an arithmetic macro only with a frozen occurrence order
(for example, nondecreasing prime order) and a terminal-first replay at every
internal prefix. If an internal prefix hits a terminal, the macro returns that
terminal immediately; an initial MISS does not silently certify all later
prefixes. After all prefix misses, the deterministic TR1 factor rule must replay
all prior terminal menus, recompute (4)--(7) from the actual maximal receipt,
reject capacity-saturated factors as non-consumable raw labels, and select the
least factor with a separately verified fresh integer occurrence before
attempting E1--E5.

The lemma proves no family empty, Type-I/II terminal, or persistent successor for
the remaining fresh factors. It removes only the invalid shortcut
\(q\mid D_*\Rightarrow q\mid E\).

## 6. Boundary

```text
R4 = OPEN_MINIMAL_RESIDUAL
R6 = OPEN_MINIMAL_RESIDUAL
TR1_INTEGER_RAW_OCCURRENCE = OPEN
OPEN_TR1_PHYSICAL_SERIALIZER = OPEN
F3 = OPEN
T6 = OPEN
```

No finite scan or synthetic control upgrades any status above.
