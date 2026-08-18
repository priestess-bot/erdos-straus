---
kind: claim
claim_id: type-I-root-capacity-stutter-common-divisor-alignment
title: proper-root stutter 的 Eisenstein 商公共因子对齐
statement: >-
  设整数 p,h,m,e,a 满足 a=em-h、pa=e(h-1)+1、h|(p^2+p+1)，并令
  b=e-1、N=a^2-ab+b^2=hk。则 gcd(a,b) 整除 gcd(h,k)。因此对 actual
  proper-root stutter，任何同时整除 a 与 e-1 的素因子也同时整除 root height h
  和 Eisenstein quotient k；若该素因子不等于 3，它还整除 u=h/3，因而属于
  既有 root-capacity source menu 的输入类型。反过来，任何 quotient-only
  因子 q|k、q不整除h，都不能同时整除 a 和 e-1。该约束不保证 menu 命中，
  不 physicalize q|k，也不构造 E1--E5 successor。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-positive-definite-norm-bound
  - type-I-root-capacity-stutter-provenance-dispatch
topics:
  - type-I
  - root-capacity
  - stutter
  - eisenstein-quotient
  - common-divisor
  - provenance
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: actual-stutter-linear-identities
  - claim: type-I-root-capacity-stutter-positive-definite-norm-bound
    role: proper-root-norm-notation-and-range
  - claim: type-I-root-capacity-stutter-provenance-dispatch
    role: h-supported-factor-source-menu-boundary
  - reproduction: reproductions/type_i_root_capacity_stutter_common_divisor_alignment.py
    role: identity-controls-and-cyclotomic-assumption-negative-control
visibility: public
last_checked: '2026-08-18'
---

# proper-root stutter 的 Eisenstein 商公共因子对齐

## 1. Statement

This is an arithmetic alignment lemma. It does not assert that an actual
proper-root stutter exists, and it does not add a recursive edge.

Assume

$$
a=em-h,\qquad pa=e(h-1)+1,\qquad h\mid p^2+p+1,
$$

and put

$$
b=e-1,\qquad N=a^2-ab+b^2=hk.
$$

Then

$$
\boxed{\gcd(a,b)\mid\gcd(h,k).}
$$

For an actual proper-root stutter, these are existing arithmetic hypotheses.
Thus a factor shared by the two Eisenstein coordinates is never a
quotient-only factor.

## 2. Cyclotomic identity

The linear identity gives $pa+b=eh$. Let $P=p^2+p+1$. Substitution of
$pa=eh-b$ yields

$$
\begin{aligned}
a^2P
&=(pa)^2+(pa)a+a^2\\
&=(eh-b)^2+(eh-b)a+a^2\\
&=e^2h^2+eh(a-2b)+N\\
&=h\left(e^2h+e(a-2b)+k\right).
\end{aligned}
$$

Write $P=hv$. Hence

$$
a^2v=e^2h+e(a-2b)+k.
$$

This is the only use of the cyclotomic root condition. The formal stutter
curve alone does not imply this integral quotient.

## 3. Valuation proof

Put $g=\gcd(a,b)$. Since $g\mid a,b$, we have $e=b+1\equiv1\pmod g$.
Reducing the preceding identity modulo $g$ gives $g\mid h+k$. Also
$g^2\mid N=hk$.

For a prime $q$, write

$$
\alpha=v_q(h),\qquad \beta=v_q(k),\qquad r=v_q(g).
$$

Then $r\le v_q(h+k)$ and $2r\le\alpha+\beta$. If $\alpha<\beta$, the
first inequality gives $r\le\alpha$; the symmetric case gives
$r\le\beta$. If $\alpha=\beta$, the second inequality gives
$r\le\alpha$. Thus in all cases $r\le\min(\alpha,\beta)$, proving the
claim.

## 4. Consequences for the k>1 residual

If $q\mid\gcd(a,e-1)$, then $q\mid h$ and $q\mid k$. For $q\ne3$, actual
proper-root notation $h=3u$ gives $q\mid u$, so the factor is eligible for
the existing root-capacity source-menu input described by the
[provenance dispatch](type-I-root-capacity-stutter-provenance-dispatch.md).

If $q\mid k$ but $q\nmid h$, then $q\nmid\gcd(a,e-1)$. It cannot be
reclassified as a root-capacity source through a shared Eisenstein-coordinate
factor; it remains a quotient-only factor requiring QC1 or TR1.

The lemma proves neither that an eligible finite menu is nonempty nor that a
quotient-only factor has a physical source occurrence. It supplies no target,
global solution lift, or T5 ticket. Therefore
`PROPER_ROOT_QC1_OR_TR1 = OPEN`.

## 5. Sharpness control

The withdrawn numeric clue

$$
(p,h,m,e)=(20\,065\,847\,377,138\,378\,387,6768,20446)
$$

has $\gcd(a,b)=141$ but $\gcd(h,k)=3$. It is not a counterexample: its height
fails $h\mid p^2+p+1$, and the resulting right-hand side above is not divisible
by $a^2$. This shows the cyclotomic condition is essential and gives a direct
diagnostic for why the clue could not be an actual proper-root receipt.

## 6. Focused reproduction

```bash
python3 reproductions/type_i_root_capacity_stutter_common_divisor_alignment.py --verify
```

The verifier checks the exact cyclotomic identity, two controls with coprime
and non-coprime $(h,k)$, and the failed-clue boundary. It does not scan primes,
denominators, or selector paths. The universal implication is the valuation
proof above.
