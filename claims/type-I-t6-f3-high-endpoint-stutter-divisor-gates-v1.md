---
kind: claim
claim_id: type-I-t6-f3-high-endpoint-stutter-divisor-gates-v1
title: F3 high stutter 的 root-quotient 与 capacity 双 divisor gate
statement: >-
  对 ACTUAL_PERSISTENT、PROPER_FACTOR_ROOT、h>p、terminal_first_miss 的
  high stutter state，令 M=(p^2+p+1)/3、u=gcd(2r+1,M)、v=M/u、
  omega=(2r+1)/u、delta=h-p-1、n=m-1，且 D=mp+1-h=np-delta。则
  D 整除 F_root=delta^3+n delta^2+n^2 delta+v n^3，且
  D 整除 F_capacity=(delta^2-n^2)(omega delta^2-3v n^2)。这两个
  整除式来自 actual D|ph+1 与 actual D|K；它们不使用低高度 D_star、QC1/TR1
  或 Eisenstein quotient。该 gate 是 actual high stutter 的必要条件，不能替代
  canonical maximality、terminal-first、E1-E5 或 family-empty 证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-t6-f3-high-endpoint-normal-form-v1
  - type-I-root-capacity-general-endpoint-divisor-gate
topics:
  - type-I
  - root-capacity
  - f3
  - high-endpoint
  - stutter
  - divisor-gate
  - actual-receipt
  - proof-boundary
sources:
  - claim: type-I-t6-f3-high-endpoint-normal-form-v1
    role: high-domain variables and stutter normal form
  - claim: type-I-root-capacity-general-endpoint-divisor-gate
    role: actual D divides K and p*h+1
  - reproduction: reproductions/type_i_t6_f3_high_endpoint_stutter_divisor_gates.py
    role: exact divisibility and shadow-boundary controls
visibility: public
last_checked: '2026-08-24'
---

# F3 high stutter 的双 divisor gate

## 1. High-only setup

Keep the exact high source domain and actual maximal receipt:

\[
\mathrm{ACTUAL\_PERSISTENT}\land\mathrm{PROPER\_FACTOR\_ROOT}
\land h>p\land\mathrm{terminal\_first\_miss},
\]

\[
M=\frac{p^2+p+1}{3},\quad
u=(2r+1,M),\quad v=\frac Mu,\quad
\omega=\frac{2r+1}{u},\quad h=3u.
\tag{1}
\]

On the stutter branch define

\[
\delta=h-p-1>0,\qquad n=m-1\ge2,\qquad
D=mp+1-h=np-\delta.
\tag{2}
\]

The actual receipt supplies

\[
D\mid ph+1,\qquad D\mid K,\qquad (D,h)=1.
\tag{3}
\]

No low-height \(D_*\), \(k_\perp\), QC1, or TR1 object is used below.

## 2. Root-quotient gate

Because \(hv=p^2+p+1\), multiplying the first divisibility in (3) by \(v\)
gives

\[
D\mid p(p^2+p+1)+v=p^3+p^2+p+v.
\tag{4}
\]

Modulo \(D\), (2) gives \(np\equiv\delta\). Multiply (4) by \(n^3\), obtaining

\[
\boxed{
D\mid F_{\rm root}:=
\delta^3+n\delta^2+n^2\delta+vn^3.}
\tag{5}
\]

This is valid even when \((D,n)>1\), because no modular inverse of \(n\) was
taken.

## 3. Capacity gate

The root chart has

\[
2T=u(p^2\omega-3v),
\qquad
4K=(p^2-1)u(p^2\omega-3v).
\tag{6}
\]

Since \((D,h)=1\), also \((D,u)=1\). Thus \(D\mid K\) implies

\[
D\mid (p^2-1)(p^2\omega-3v).
\tag{7}
\]

Multiplying by \(n^4\) and again using \(np\equiv\delta\pmod D\) gives

\[
\boxed{
D\mid F_{\rm capacity}:=
(\delta^2-n^2)(\omega\delta^2-3vn^2).}
\tag{8}
\]

Equations (5) and (8) are additional necessary constraints on any claimed
actual high stutter receipt. They do not say that every integer satisfying
them is a maximal receipt.

## 4. Boundary controls

The non-core high curve control \(p=67,r=25311,h=93,D=779,m=13\) satisfies
both displayed divisor gates but is not in the theorem domain. Thus the gates
do not replace core primality or canonical maximality.

For the high curve shadows \((p,h,D,m)=(283,1101,32,4)\),
\((2383,37623,506,16)\), and \((3607,8337,13306,6)\), the root gate (5)
holds because their shadow divisor satisfies \(D\mid ph+1\), while the
capacity gate (8) fails. This shows why actual \(D\mid K\) is a substantive
extra input rather than a decorative restatement.

## 5. Exact next use

The next theorem may intersect (5)--(8) with canonical maximality and
terminal-first to prove an empty family, direct terminal, or E1--E5
successor. Without that additional step, the status remains:

HIGH_STUTTER_DIVISOR_GATES = ESTABLISHED_NECESSARY_ONLY;  
HIGH_ENDPOINT_TOTAL_EXIT = OPEN.
