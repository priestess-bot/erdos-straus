---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-residue-terminal-dispatch
title: q=1 高 C=2 的 19 相位 63 类仿射终端分派
statement: >-
  对 q=1 high C=2 19 相位 p=912u+769，按 u (mod 119) 排除 p 被 7 或 17 整除的
  23 类后，剩余 96 个可能核心素数类中有 60 类由固定 Type II raw ray 给出直接终端：
  48 类使用 h=7 的三个模板，12 类使用 h=119 的有限模板表。另有 3 个未被该 Type II
  菜单覆盖的类由固定 Type I normal form 终端。因此一个显式 terminal-first 菜单直接
  覆盖 63 类，余下精确为 33 个 u (mod 119) 类。对这 33 类，所有在单一 residue
  progression 上参数恒定的 Type II raw ray 已穷尽失败，但这不排除随参数变化的
  Type II、其它 Type I、或后继 strict relay；已有三 p-anchor persistent 宏仍可作为
  terminal-first miss 后的严格可提升出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-coprime-factor-normal-form
  - type-II-coprime-factor-normal-form
  - type-II-q-one-c-two-19-phase-third-p-anchor-finite-capacity-split
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - terminal-first
  - affine-ray
  - finite-selector
  - residue-dispatch
  - short-certificate
  - proof-boundary
sources:
  - claim: type-I-coprime-factor-normal-form
    role: type-i-terminal-normal-form-verifier
  - claim: type-II-coprime-factor-normal-form
    role: type-ii-raw-ray-terminal-normal-form-verifier
  - claim: type-II-q-one-c-two-19-phase-third-p-anchor-finite-capacity-split
    role: exact-u-mod-119-phase-domain
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: strict-relay-after-terminal-first-miss
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_residue_terminal_dispatch.py
    role: finite-affine-ray-and-normal-form-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) 19-phase 的 63 类仿射终端分派

## 1. The finite residue domain

Write

\[
p=p_u+Lt,
\qquad
p_u=912u+769,
\qquad
L=912\cdot119=108528,
\qquad
0\le u<119.
\tag{1}
\]

The phase condition fixes \(p\equiv9\pmod {19}\).  A member of (1) cannot
be a phase prime when

\[
u\equiv4\pmod7
\quad\text{or}\quad
u\equiv12\pmod {17},
\tag{2}
\]

because these are exactly the classes for which \(7\mid p\) or
\(17\mid p\).  There are

\[
119-17-7+1=96
\tag{3}
\]

remaining residue classes.  All claims below are affine identities on the
whole progression (1), not tests over a range of primes.

## 2. Exhaustive fixed Type II rays on one residue progression

Fix a Type II raw ray \((A,C,k)\), and put

\[
h=4Ack-1,
\qquad
B=\frac{kp+A}{h}.
\tag{4}
\]

If this is a parameter-constant ray throughout (1), then subtracting its
divisibility condition at consecutive values of \(t\) gives

\[
h\mid kL.
\tag{5}
\]

Since \((h,k)=1\), necessarily \(h\mid L\).  Conversely, if

\[
h\mid L,
\qquad
h\mid kp_u+A,
\tag{6}
\]

then (4) is integral for every \(t\).  The Type II normal form applies once
\(A\le B\), which holds already at the listed base point and persists as
\(t\) grows.

The possible defining factors are therefore exactly

\[
h\in\{3,7,19,51,119,323,399,6783\}.
\tag{7}
\]

For each one, \(Ack=(h+1)/4\), so there are only 151 positive factor triples
to check.  This finite divisor calculation has the following exact union.

Define

\[
\mathcal U_7=
\left\{u:\ u\not\equiv4\pmod7,\ u\not\equiv12\pmod{17},\
u\equiv0,2,3\pmod7\right\}.
\tag{8}
\]

It has 48 elements.  The three templates are

| \(u\pmod7\) | \(h\) | \((A,C,k)\) | \(B\) |
|---:|---:|---:|---:|
| 0 | 7 | \((1,2,1)\) | \((p+1)/7\) |
| 2 | 7 | \((1,1,2)\) | \((2p+1)/7\) |
| 3 | 7 | \((2,1,1)\) | \((p+2)/7\) |

The only additional Type II residue classes are

\[
\mathcal U_{119}=
\{47,48,55,61,64,71,76,82,106,110,113,118\}\pmod {119},
\tag{9}
\]

with the following \(h=119\) templates.

| \(u\) | \((A,C,k)\) | \(u\) | \((A,C,k)\) |
|---:|---:|---:|---:|
| 47 | \((1,10,3)\) | 48 | \((2,5,3)\) |
| 55 | \((3,10,1)\) | 61 | \((5,6,1)\) |
| 64 | \((6,5,1)\) | 71 | \((2,3,5)\) |
| 76 | \((10,3,1)\) | 82 | \((1,3,10)\) |
| 106 | \((1,5,6)\) | 110 | \((3,5,2)\) |
| 113 | \((5,3,2)\) | 118 | \((1,6,5)\) |

For every row, (4) is a Type II normal form and hence gives a direct
certificate for every phase prime in that residue progression.  Conversely,
the exact enumeration implied by (7) gives

\[
\boxed{
\text{fixed Type II ray coverage}
=\mathcal U_7\sqcup\mathcal U_{119},
\qquad |\mathcal U_7\sqcup\mathcal U_{119}|=60.
}
\tag{10}
\]

Thus the complement has no parameter-constant Type II raw ray on its own
\(u\pmod {119}\) progression.  This is a ray boundary only: it does not
exclude a per-prime varying Type II certificate.

## 3. Three additional fixed Type I terminals

For a constant Type I normal form \((A,B,m)\), the two congruences persist
along (1) whenever

\[
4AB\mid L,
\qquad m\mid BL,
\tag{11}
\]

and they hold at \(p_u\).  The following three rows satisfy the complete
Type I normal form conditions and are disjoint from (10):

| \(u\pmod {119}\) | \((A,B,m)\) |
|---:|---:|
| 33 | \((1,17,7)\) |
| 50 | \((1,34,7)\) |
| 89 | \((1,17,3)\) |

Indeed, each row has

\[
4AB\mid p+m,
\qquad m\mid Bp+A,
\tag{12}
\]

on its entire progression, so \(C=(p+m)/(4AB)\) completes the Type I
certificate.

## 4. Dispatch and exact remaining menu boundary

Let

\[
\mathcal U_{\rm term}=
\mathcal U_7\sqcup\mathcal U_{119}\sqcup\{33,50,89\}.
\tag{13}
\]

Then \(|\mathcal U_{\rm term}|=63\).  Its complement in the 96 admissible
classes is exactly

\[
\begin{aligned}
\mathcal U_{\rm rem}=\{&1,5,6,8,13,15,19,20,22,26,27,34,36,40,41,43,54,57,\\
&62,68,69,75,78,83,85,90,92,96,99,103,104,111,117\}\pmod {119}.
\end{aligned}
\tag{14}

For \(u\in\mathcal U_{\rm term}\), terminal-first emits the displayed
direct Type I/II certificate.  For \(u\in\mathcal U_{\rm rem}\), the
fixed-ray Type II subroutine is exhausted and terminal-first can continue
with other menus; if they all miss, the q=1 three-p-anchor persistent macro
is a strict, identity-lifted successor.  Thus (14) is a precise next input,
not a claim that the 33 classes lack solutions.

The third-anchor selector further splits (14) into 22 classes with
\(c_3<c_2\) and 11 with \(c_3>c_2\), providing a small finite target for a
non-template terminal or cross-chart descent construction.

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_residue_terminal_dispatch.py --verify
```
