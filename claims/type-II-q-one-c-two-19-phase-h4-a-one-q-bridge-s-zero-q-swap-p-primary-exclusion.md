---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-s-zero-q-swap-p-primary-exclusion
title: H4 q-bridge s=0 的 q-block swap、小锚界与 secondary p-primary 有限排除
statement: >-
  在满足 R4=1 (mod p) 的 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity
  a_alt=1 clean q bridge 中，
  若唯一 q-bridge stutter 的 E_x 恰等于 q（即 E_x=q+ps 的 s=0），则 endpoint 的
  x-side maximal complete-excess block 精确为 Q_x=q，且 q 是原 z-block Q 的 unitary
  divisor。故可从 x_q 侧再实际剥尽 q，达到 primitive node (xi,zeta)=(x_q/q,R4-x_q/q)，
  其中 xi|K4、xi|ph-q+1。写 w=(p+1)/2、d=gcd(w,M4)、q=w/d、h=2e；clean-q 与
  H4 overlap 强迫 e|d，而 actual phase provenance 给 d|Delta=|1536-a(p)|、
  1<=Delta<=1535。若新 zeta-side complete-excess block 含 p，则
  p 整除 C(d,e)=1-2d+4d^2(1-2e)。对所有 11495 个 d in [1,1535]、e|d 的非零固定
  常数作精确因子分解，只有七个因子落入实际 31 residual phase 的进程，且全部违反
  d|Delta；因此 secondary p-primary gate 在 actual phase domain 中为空。于是 s=0
  总给出一个不依赖 atomic adapter 的 actual 分派：若 zeta|K4 则为 Type I terminal，
  否则为 p-free single-side receipt，其唯一 capacity stutter 只是 E_zeta=L0 (mod p)，其中
  E_zeta=Q_zeta/gcd(M4,Q_zeta)、L0=lcm(M4,Q)/M4；非该同余时得到 parent capacity
  c_zeta<=p-2。该结果不关闭这条新的单侧 capacity gate 或 terminal/typed guards。
claim_status: established
proof_provenance: mixed
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
  - type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - a-one
  - fresh-carrier
  - raw-path
  - complete-excess-bundle
  - carry-stutter
  - p-primary
  - finite-sieve
  - small-anchor
  - source-provenance
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-stutter-a-coordinate-transduction
    role: s-zero-stutter-normal-form-and-q-word-reentry
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
    role: exact-q-bridge-block-and-parent-capacity-formula
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-clean-q-word-and-primitive-endpoint
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: fresh-carrier-delta-bound-and-original-top-capacity
  - claim: type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
    role: actual-overlap-h-equals-two-e-identity
  - claim: type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
    role: actual-31-phase-domain-and-selector-a
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: single-side-complete-excess-receipt-and-terminal-contract
  - concept: denominator-escape-state-contract
    role: terminal-typed-lift-and-potential-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_s_zero_q_swap_p_primary.py
    role: exact-finite-secondary-p-primary-screen-and-gate-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q\)-bridge \(s=0\) 的 \(q\)-block swap

## 1. 范围

保留 actual q=1 high \(C=2\) 19-phase H4 proper-overlap top-capacity
\(a_{\rm alt}=1\) clean \(q\) bridge 的记号：

\[
K_4=M_4c_4,
\qquad pR_4+1=4K_4,
\qquad R_4\equiv1\pmod p,
\qquad
h=(R_4-1,K_4)<p+1,
\tag{1}
\]

\[
z=R_4-h=Q\delta,
\qquad
w=\frac{p+1}{2},
\qquad
d=(w,M_4),
\qquad q=\frac wd>1.
\tag{2}
\]

clean bridge 给出

\[
(q,K_4)=(q,M_4)=1,
\qquad q\mid Q\mid z,
\qquad p\equiv-1\pmod q.
\tag{3}
\]

At its actual primitive endpoint

\[
(x_q,y_q)=\left(R_4-\frac zq,\frac zq\right),
\tag{4}
\]

write the maximal complete-excess blocks relative to \(K_4\) as

\[
x_q=Q_x\beta_x,
\qquad y_q=Q_y\beta_y.
\tag{5}
\]

The prior exact reduction supplies

\[
Q_y=\frac Qq,
\qquad E_x=\frac{Q_x}{(M_4,Q_x)},
\qquad
c_q=p-1\Longleftrightarrow E_x\equiv q\pmod p.
\tag{6}
\]

This card treats only the sharpened equality case

\[
\boxed{E_x=q,}
\tag{7}
\]

equivalently \(s=0\) in \(E_x=q+ps\). It does not use the conditional
atomic split target at (4): every raw word below remains inside the original,
already actual H4 path.

## 2. The carrier swaps sides exactly

Put \(g_x=(M_4,Q_x)\). From (7),

\[
Q_x=qg_x,
\qquad (q,g_x)=1.
\tag{8}
\]

### Lemma 1

\[
\boxed{g_x=1,\qquad Q_x=q.}
\tag{9}
\]

**Proof.** Suppose \(\ell\mid g_x\). Since \(q\) is coprime to \(M_4\),
it is also coprime to \(g_x\); hence

\[
v_\ell(Q_x)=v_\ell(g_x)\le v_\ell(M_4).
\tag{10}
\]

But \(Q_x\) is a maximal complete-excess block relative to \(K_4\), so a
prime in \(Q_x\) occurs in \(x_q\) to its full exponent and satisfies

\[
v_\ell(Q_x)=v_\ell(x_q)>v_\ell(K_4)\ge v_\ell(M_4),
\tag{11}
\]

contradicting (10). Thus \(g_x=1\), and (8) proves (9). \(\square\)

Because (4) is primitive, \((Q_x,Q_y)=1\). Combining (9) with (6) gives

the additional exact restriction

\[
\boxed{\left(q,\frac Qq\right)=1.}
\tag{12}
\]

Thus \(q\) is not merely a divisor of the original \(z\)-block: in the
\(s=0\) cell it is a unitary divisor of \(Q\), removed completely from the
\(y\)-block and appearing completely as the new \(x\)-block.

Let

\[
\xi=\beta_x=\frac{x_q}{q}.
\tag{13}
\]

Then \(\xi\mid K_4\), \((\xi,q)=1\), and every prime factor of \(q\) is
absent from \(K_4\). Consequently its prime-factor word is an actual raw
word from (4), with no gcd reduction, and reaches

\[
\boxed{
\{x_q,y_q\}
\rightsquigarrow
\{\xi,\zeta\}:=\{\xi,R_4-\xi\}.
}
\tag{14}
\]

This is stronger than a chart-level reparametrization: (14) is a replayable
word attached to the existing H4 prefix and does not require atomic-split
admission.

## 3. The swapped anchor is small on the H4 phase scale

The two representations of \(R_4\), namely

\[
R_4=q\xi+y_q,
\qquad qy_q=R_4-h,
\tag{15}
\]

give

\[
(q-1)y_q=q\xi-h.
\tag{16}
\]

Since \(\xi\mid K_4\), reducing \(pR_4+1=4K_4\) modulo \(\xi\) gives
\(py_q+1\equiv0\pmod\xi\). Multiplying by \(q-1\) and using (16) yields

\[
\boxed{\xi\mid ph-q+1.}
\tag{17}
\]

Now retain the actual H4 overlap identity

\[
h=2e,
\qquad e\mid w.
\tag{18}
\]

Because \(h\mid K_4\) and (3) gives \((q,K_4)=1\), \((e,q)=1\). Also
\(d\mid M_4\) and (3) give \((d,q)=1\); as \(w=qd\), (18) therefore
implies

\[
\boxed{e\mid d.}
\tag{19}
\]

The actual H3-to-H4 provenance gives

\[
d\mid\Delta:=\lvert1536-a(p)\rvert,
\qquad 1\le\Delta\le1535.
\tag{20}
\]

Consequently the swapped anchor lies in the explicit linear-size box

\[
\boxed{
1\le\xi\le ph-q+1\le2pd-q+1<2pd\le2p\Delta.
}
\tag{21}
\]

This is an actual bounded anchor certificate, not a claim of a smaller
denominator lift. It will be used only for the p-primary gate below.

## 4. Exact secondary p-primary gate

The second endpoint in (14) is primitive. Let

\[
\zeta=Q_\zeta\beta_\zeta
\tag{22}
\]

be its maximal complete-excess decomposition relative to \(K_4\). Since
\(p\nmid K_4\),

\[
p\mid Q_\zeta
\quad\Longleftrightarrow\quad
p\mid\zeta
\quad\Longleftrightarrow\quad
\xi\equiv1\pmod p,
\tag{23}
\]

where the final equivalence uses \(R_4\equiv1\pmod p\). From (4), (13),
and \(qy_q=R_4-h\),

\[
q^2\xi=qR_4-(R_4-h)=(q-1)R_4+h.
\tag{24}
\]

Thus (23) is equivalent to

\[
\boxed{h\equiv q^2-q+1\pmod p.}
\tag{25}
\]

Substitute \(h=2e\) and \(q=(p+1)/(2d)\). As \(d<w<p\), multiplication by
\(4d^2\) is legitimate modulo \(p\), and (25) becomes

\[
\boxed{
p\mid C(d,e):=1-2d+4d^2(1-2e).
}
\tag{26}
\]

For \(d,e\ge1\), \(C(d,e)<0\), so there is no zero-constant exception.
Equation (26) has converted a dynamic secondary p-block event into divisibility
of a fixed integer indexed only by the finite H4 phase data.

## 5. Exact finite phase screen

The actual q=1 high \(C=2\) 19-phase domain has

\[
p\equiv769\pmod{912},
\qquad
u=\frac{p-769}{912}\pmod{119}\in\mathcal U_{31},
\tag{27}
\]

where \(\mathcal U_{31}\) is the existing terminal-first residual menu, and
\(a(p)\) is its canonical third-anchor selector. By (19)--(20), every actual
secondary p-primary event must occur among the finite supermenu

\[
1\le d\le1535,
\qquad e\mid d,
\qquad p\mid C(d,e).
\tag{28}
\]

There are exactly

\[
\sum_{d=1}^{1535}\tau(d)=11\,495
\tag{29}
\]

fixed nonzero constants. Exact factorization gives 48 phase-prime factor
records; only the following seven have \(u\in\mathcal U_{31}\) before the
mandatory provenance test \(d\mid\Delta\):

| \(p\) | \(u\) | \(a(p)\) | \(\Delta\) | \(d\) | \(e\) |
|---:|---:|---:|---:|---:|---:|
| 84,673 | 92 | 1,761 | 225 | 885 | 885 |
| 145,777 | 40 | 184 | 1,352 | 555 | 37 |
| 161,281 | 57 | 830 | 706 | 449 | 449 |
| 620,929 | 85 | 1,894 | 358 | 881 | 881 |
| 708,481 | 62 | 526 | 1,010 | 1,410 | 94 |
| 734,017 | 90 | 1,457 | 79 | 260 | 10 |
| 745,873 | 103 | 2,179 | 643 | 950 | 38 |

Every row violates \(d\mid\Delta\). Therefore the screen is empty on actual
H4 receipts:

\[
\boxed{p\nmid Q_\zeta.}
\tag{30}
\]

The screen factors bounded constants; it does not scan a prime interval or
assert that the seven rows are actual H4 states. For example, without the
actual phase/provenance restriction the gate is genuinely possible:
\(p=2161,d=23,e=1,q=47,h=2\) has \(C(d,e)=-2161\). This fixed control is why
the finite H4 data in (20), rather than a bare congruence argument, is essential.

## 6. A p-free single-side handoff without atomic admission

By (30), \(Q_\zeta\) is p-free. Since \((\xi,\zeta)=1\), both
\(\xi\mid K_4\) and \(\beta_\zeta\mid K_4\), and hence

\[
\boxed{\xi\beta_\zeta\mid K_4.}
\tag{31}

\]

If \(Q_\zeta=1\), then \(\zeta\mid K_4\) and (31) is a direct Type I
terminal. Otherwise (14), (22), and (31) are a path-anchored **single-side**
complete-excess receipt from the original H4 source; it no longer needs the
two-sided atomic adapter.

Let

\[
E_\zeta=\frac{Q_\zeta}{(M_4,Q_\zeta)},
\qquad
L_0=\frac{\operatorname{lcm}(M_4,Q)}{M_4}.
\tag{32}

\]

The original top-capacity relation is \(c_4L_0^{-1}\equiv-1\pmod p\), while
the single-side target has capacity \(c_\zeta\equiv c_4E_\zeta^{-1}\pmod p\).
Therefore its unique non-strict capacity gate is

\[
\boxed{
c_\zeta=p-1
\quad\Longleftrightarrow\quad
E_\zeta\equiv L_0\pmod p.
}
\tag{33}

\]

When (33) fails, \(c_\zeta\le p-2\). The existing persistent H4 prefix,
the two actual q raw words, this single-side receipt, terminal-first/typed
validation, and the identity \(\operatorname{Sol}(p)\) lift then conditionally
compose to a strict parent macro. The only \(s=0\) arithmetic residual is now
the p-free one-side gate (33), not a p-primary or atomic-split ambiguity.

## 7. Boundary

This card does not prove that (33) is empty, nor does it turn \(\xi\mid
ph-q+1\) into a smaller-denominator solution lift. It also preserves every
terminal-first, typed, serializer, and persistent-scope guard. Its concrete
advance is narrower and verifiable: the q-bridge \(s=0\) checkpoint has an
actual q-block swap, an \(O(p\Delta)\) anchor box, no secondary p-primary
continuation in the real 19-phase domain, and a one-sided rather than atomic
remaining capacity gate.

## 8. Focused verification

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_s_zero_q_swap_p_primary.py --verify
```

The verifier checks the algebraic p-primary gate on one p-free and one
phase-free positive control, then exactly factors the 11,495 fixed constants
and confirms the seven-row screen above and its zero actual-provenance output.
It performs no prime-range or denominator scan.
