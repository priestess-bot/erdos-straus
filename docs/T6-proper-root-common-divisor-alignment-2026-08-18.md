# T6 proper-root common-divisor alignment

> Status: a structural proper-root lemma is established; `QC1`, `TR1`, and
> `T6_GLOBAL_SELECTOR_TOTALITY` remain `OPEN`.

The new [common-divisor alignment claim](../claims/type-I-root-capacity-stutter-common-divisor-alignment.md)
proves

$$
\gcd(a,e-1)\mid\gcd(h,k)
$$

for the actual proper-root stutter notation
$N=a^2-a(e-1)+(e-1)^2=hk$. It uses the cyclotomic root condition
$h\mid p^2+p+1$, not a finite control or a relaxed divisor gate.

This separates the remaining quotient factors cleanly:

- A shared factor of the two Eisenstein coordinates is necessarily
  `h`-supported. Apart from 3, it divides `u=h/3` and is eligible for the
  already known root-capacity menu input.
- A factor of `k` coprime to `h` is genuinely quotient-only and cannot be
  reclassified as a root-capacity source through `gcd(a,e-1)`.
- Neither classification proves that a finite certificate menu is nonempty or
  gives a physical source/path, target, lift, or T5 ticket.

The previous non-actual numeric clue is a sharpness control: it has
`gcd(a,e-1)=141` but `gcd(h,k)=3`, exactly because its reconstructed height
does not divide `p^2+p+1`. This prevents the alignment lemma from being
overextended to abstract curve points.

Reproduce the focused check with:

```bash
python3 reproductions/type_i_root_capacity_stutter_common_divisor_alignment.py --verify
python3 -m unittest tests/test_type_i_root_capacity_stutter_common_divisor_alignment.py
```

The immediate research use is narrower than a selector theorem: split QC1
into an `h`-supported subcase, where source-menu nonemptiness is the missing
fact, and a quotient-only subcase, where an independent physicalization or
TR1-style adapter is required.

The follow-up [primitive quotient normalization](../claims/type-I-root-capacity-stutter-primitive-quotient-normalization.md)
keeps this split after dividing out the whole shared factor. In coordinates
\(a=gA\), \(e-1=gB\), \(h=g\alpha\), and \(k=g\kappa\), it proves the
actual-root-only saturation identity

\[
e^2\alpha+e(A-2B)+\kappa
=gA^2\frac{p^2+p+1}{h}.
\]

For a quotient-only prime \(q\mid\kappa,\ q\nmid h\), its cyclotomic
complement satisfies

\[
q\mid\frac{p^2+p+1}{h}
\quad\Longleftrightarrow\quad
q\mid e\ \text{or}\ B\equiv(p+1)A\pmod q.
\]

Thus the unresolved quotient carrier is localized in the primitive
\(\kappa\)-part and split by an exact arithmetic condition, while shared
factors remain only a source-menu input type. This refines the QC1 split; it
still supplies neither menu nonemptiness nor a physical E1--E5 edge.
