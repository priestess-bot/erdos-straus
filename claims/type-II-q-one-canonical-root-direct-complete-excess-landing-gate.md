---
kind: claim
claim_id: type-II-q-one-canonical-root-direct-complete-excess-landing-gate
title: Canonical q=1 root direct complete-excess landing has an exact integer kernel
statement: >-
  A same-protocol direct single-side or atomic complete-excess landing at the
  canonical q=1 root is governed by an exact lcm/valuation kernel. Its T5
  ticket forces the source support to be at most B_p, and any root prime power
  at least (p-1)^2 makes such a direct landing impossible. Conversely, a
  p=73 static atomic chart satisfies every local lcm, maximal-excess and E5
  condition, so carrier bounds alone cannot prove a global no-go. The result
  is an arithmetic source gate only; it does not create E1 provenance, a
  terminal-first miss, E3 admission or re-entry.
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-canonical-root-default-entry-capacity-gap
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-root-capacity-strict-carry-support-rebase
topics:
  - type-II
  - q-one
  - canonical-root
  - complete-excess
  - atomic-split
  - single-side
  - well-foundedness
  - E1-E5
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_f3_root_landing_and_tr1_dyadic_boundaries.py
    role: static atomic landing countercontrol
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: lcm charge and canonical target semantics
visibility: public
last_checked: '2026-08-25'
---

# Canonical q=1 root direct complete-excess landing gate

Let \(A_\star\) be the canonical q=1 root support. Consider an ordinary
same-protocol `TYPEI/CHARGED` direct complete-excess landing from a source
chart

\[
K=ac,\qquad 4ac=pR+1,\qquad A_\star=aL.
\tag{1}
\]

The target is required to have support exactly \(A_\star\), not merely a
chart that can be statically rewritten in root coordinates.

## 1. Lcm and valuation gate

Since \(4A_\star\equiv-1\pmod p\), the source cofactor is forced by (1):

\[
\boxed{c=p-\langle L\rangle_p.}
\tag{2}
\]

Write

\[
d=\prod_{q\mid L}q^{v_q(a)},\qquad a=da_0,\qquad (a_0,L)=1.
\tag{3}
\]

For a single-side or atomic maximal complete-excess payload whose lcm target
is \(A_\star\), every prime power which enlarges the support is forced. The
total excess payload is therefore

\[
\boxed{Q_{\rm tot}=dL.}
\tag{4}

For each \(q^e\Vert L\), maximality is equivalent to

\[
\boxed{v_q(c)<e.}
\tag{5}

Equivalently, if \(L=pj+\langle L\rangle_p\), then
\(q^e\nmid j+1\). These are necessary and sufficient arithmetic gates for
the lcm landing; they contain no source-path assertion.

For a single-side occurrence, (4) is equivalent to the finite factor-pair
kernel: there exist positive \(\beta,H,x\) such that

\[
a_0c=x\beta H,\qquad \gcd(x,dL\beta)=1,
\tag{6}
\]

\[
\boxed{x(4d\beta H-p)=pdL\beta+1.}
\tag{7}

Then the selected side is \(dL\beta\) and \(x=R-dL\beta\). For an atomic
occurrence, the exact kernel instead has two nonempty coprime colors:

\[
Q_xQ_y=dL,\quad Q_x,Q_y>1,\quad (Q_x,Q_y)=1,
\tag{8}

\[
\beta_x\beta_yH=a_0c,\quad
\gcd(Q_x\beta_x,Q_y\beta_y)=1,
\tag{9}

\[
\boxed{4d\beta_x\beta_yH
=p(Q_x\beta_x+Q_y\beta_y)+1.}
\tag{10}

Unlike the single-side case, \(Q_xQ_y\) need not be smaller than a raw side;
only each colored arm is smaller than their sum \(R\).

## 2. Exact direct-landing E5 filter

The root target has cofactor \(p-1\). Its charged rank is

\[
\left(0,p-1\right).
\tag{11}

For a direct ordinary same-phase edge, it is strictly below the source rank
only when

\[
\boxed{a\le B_p=\frac{(p-1)^2}{4}.}
\tag{12}

If \(a>B_p\), both outer coordinates are zero and \(p-1<c\) would be needed,
which is impossible. This does not reject a different parent-to-final macro;
it classifies only a direct persistent landing.

Consequently, if a root prime power satisfies

\[
q^e\Vert A_\star,\qquad q^e\ge(p-1)^2,
\tag{13}

then no direct single-side or atomic landing exists. If the full power is in
\(a\), (12) fails. Otherwise one excess arm must contain \(q^e\), but every
arm is less than \(R<4a\le(p-1)^2\), a contradiction. The only remaining
direct-arithmetic sector has all root prime powers below \((p-1)^2\).

## 3. Why a carrier-only no-go is false

For \(p=73\), take

\[
A_\star=590150,\quad a=638,\quad L=925,\quad c=24,\quad
K=15312,\quad R=839.
\tag{14}

The primitive node

\[
25+814=839,\qquad 25=25\cdot1,\qquad814=37\cdot22
\tag{15}

has exact maximal blocks \(Q_x=25\), \(Q_y=37\), with

\[
22\mid K,\qquad(25,814)=1,\qquad
\operatorname{lcm}(638,25,37)=590150.
\tag{16}

The target cofactor is \(72=p-1\), while \(638\le B_{73}=1296\), so even the
direct E5 test passes. This is deliberately a static inverse chart/node, not
an E1 witness: it has no fresh-default source, raw transcript, terminal-first
miss, typed target or re-entry. It proves that the remaining smooth-root sector
cannot be dismissed from support bounds, lcm arithmetic and E5 alone.
