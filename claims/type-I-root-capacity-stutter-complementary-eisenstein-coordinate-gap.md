---
kind: claim
claim_id: type-I-root-capacity-stutter-complementary-eisenstein-coordinate-gap
title: proper-root stutter 的互补 Eisenstein 坐标缺口与固定坐标约化
statement: >-
  对核心素数 p≡1 mod24 的任意 terminal-first 后 actual proper-root stutter receipt，令
  v=(p^2+p+1)/h、b=e-1、U=e(p+1)-av、W=U-e=ep-av。则 W≥5。
  更精确地，令 eta=b-a、delta=p-h，则 eta≥5、eta<W≤eta^2+2eta-3，且
  k=e eta-aW=eta(eta+1)-a(W-eta)、h(W+1)=b delta+eta。令
  t=((W+1)m+W eta)/b，便有 t∈Z_{>0}、
  delta=(W+1)(m-1)+t 和 h|(delta^2+delta+1)。固定 w=W 后，令
  F=delta^2+delta+1=nh、L=w(m-1)+t，则 1≤t≤2w+1、
  1≤n<(8/3)(w+1)^2，且 L 整除
  C=w^2-wt+t^2+n(w-t)。若 C=0，则 t=w+r，其中 r>0、r|w^2，且
  n=w^2/r+w+r。原始 stutter 等式进一步排空全部 C=0 例外子纤维，
  故每个固定 w 的子纤维完全由显式有限整除门控制。并且 gcd(eta,W)=1，
  故剩余坐标分支必为 primitive。若 gamma=W-eta、d=gcd(gamma,k)，则
  d|gcd(W+1,a^2-a+1) 且 3不整除d。若 g=gcd(D,d)、
  g^sharp=g/gcd(g,7)，则 g|Phi(h)=h^4-h^3+3h^2-h+1，且 g^sharp|D_*；
  g^sharp 的每个素因子在 D、D_*、D_T=D/gcd(D,(p^2-1)/2) 中保持相同赋值，并避开 p^2-1。
  唯一可能被 h^2-1 吸收的 resonant 素因子是至多一次的 7。若 g>1，则 4g<=p-2。
  因而由 sh=1 mod g、s=3 mod4 确定的最小正 variable gap 总在自然范围内；令
  C=(p+s)/(4g)，且 gcd(s,C)=1；每个满足 r|g 且 s|g+r 的 r 都给出一张直接
  Type II 证书。
  该结论仍不证明 g>1 或该有限 divisor fan 必命中，不构造 E1--E5 edge，也不闭合
  QC1、TR1 或 T6 totality。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-finite-curve-constraint
  - type-I-root-capacity-stutter-positive-definite-norm-bound
  - type-I-root-capacity-stutter-eisenstein-support
  - type-I-root-capacity-stutter-actual-small-root-exclusion
  - type-I-root-capacity-stutter-k-one-universal-exclusion
  - type-I-root-capacity-stutter-transverse-residual-capacity-map
  - type-I-root-capacity-stutter-transverse-root-residue-low-gap-descent
  - gap-three-criterion
  - short-certificate-equivalence
topics:
  - type-I
  - root-capacity
  - stutter
  - eisenstein-norm
  - complementary-coordinate
  - infinite-family-reduction
  - divisor-fiber
  - resonant-intersection
  - transverse-allocation
  - low-gap-obstruction
  - variable-gap
  - large-carrier-bound
  - terminal-dispatch
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-finite-curve-constraint
    role: actual-stutter-identities
  - claim: type-I-root-capacity-stutter-positive-definite-norm-bound
    role: proper-root-range-and-m-le-e
  - claim: type-I-root-capacity-stutter-eisenstein-support
    role: oddness-of-the-norm-quotient
  - claim: type-I-root-capacity-stutter-actual-small-root-exclusion
    role: actual-m-mod-three-classification
  - claim: type-I-root-capacity-stutter-k-one-universal-exclusion
    role: k-is-not-one-in-the-actual-proper-root-domain
  - claim: type-I-root-capacity-stutter-transverse-residual-capacity-map
    role: D-star-to-T-side-capacity-allocation
  - claim: type-I-root-capacity-stutter-transverse-root-residue-low-gap-descent
    role: existing-positive-low-gap-adapter-being-tested
  - claim: gap-three-criterion
    role: terminal-first-gap-three-miss-for-the-general-A-exception
  - claim: short-certificate-equivalence
    role: direct-Type-II-certificate-reconstruction-for-the-variable-gap-fan
visibility: public
last_checked: '2026-08-19'
---

# proper-root stutter 的互补 Eisenstein 坐标缺口

## 1. Scope and notation

Fix an actual, terminal-first-surviving proper-root stutter receipt in the
core domain:

\[
p\equiv1\pmod {24},\qquad 2\le h<p,\qquad h\mid P:=p^2+p+1,
\]

\[
h=3u,\qquad 3\nmid u,
\tag{1a}
\]

\[
a=em-h,\qquad pa+(e-1)=eh,\qquad
a^2-a(e-1)+(e-1)^2=hk.
\tag{1}
\]

Put

\[
b=e-1,\qquad v=\frac Ph,\qquad
U=e(p+1)-av,\qquad W=U-e=ep-av,
\tag{2}
\]

\[
\eta=b-a,\qquad \delta=p-h.
\tag{3}
\]

The established proper-root estimates used below are

\[
m\ge3,\qquad m\not\equiv2\pmod3,\qquad
1\le a<e,\qquad e>\sqrt h,\qquad m<1+\sqrt h.
\tag{4}
\]

Hence \(m\le e\).  The Eisenstein support theorem also makes \(k\) odd.

## 2. Complementary factorization

Let \(\omega^2-\omega+1=0\), so that
\(N(x-y\omega)=x^2-xy+y^2\).  Directly from (1) and \(P=hv\),

\[
hU=eh(p+1)-aP=(p+1)b-a.
\tag{5}
\]

Consequently

\[
\boxed{
(p+\omega)(a-b\omega)=h(e-U\omega).
}
\tag{6}
\]

The constant coefficient in (6) is \(pa+b=eh\); the coefficient of
\(\omega\) is \(a-(p+1)b=-hU\).  Multiplication by the conjugate
\(p+1-\omega\) gives

\[
\boxed{vb=pU+e.}
\tag{7}
\]

Taking norms gives

\[
\boxed{vk=e^2-eU+U^2=e^2+eW+W^2.}
\tag{8}
\]

There is a second exact identity.  Equation (5) says

\[
pb=a-b+hU.
\]

Multiply this by \(a\), compare it with \(b(pa+b)=ehb\), and use the
norm equation in (1).  This yields \(k+aU=eb\), hence

\[
\boxed{k=e\eta-aW.}
\tag{9}
\]

## 3. Excluding \(W\le3\)

As \(h\le p-1\),

\[
v=\frac Ph\ge\frac P{p-1}>p+2,
\qquad\text{hence}\qquad v\ge p+3.
\tag{10}
\]

If \(W\le-1\), then \(U\le e-1\), and (7) gives

\[
vb\le p(e-1)+e.
\]

But (10) gives \(vb\ge(p+3)(e-1)\), larger by \(2e-3>0\).  Thus
\(W\ge0\).  As \(a\le b\), \(\eta\ge0\); if \(\eta=0\), then (9) gives
\(k=-aW\le0\).  Therefore

\[
\boxed{1\le\eta\le e-2.}
\tag{11}
\]

Substitute \(p=h+\delta\) and \(a=b-\eta\) in (5).  This gives

\[
\boxed{h(W+1)=b\delta+\eta.}
\tag{12}
\]

Since \(h=b(m-1)+m+\eta\), define

\[
\boxed{
t:=\frac{(W+1)m+W\eta}{b}\in\mathbb Z_{>0},
\qquad
\delta=(W+1)(m-1)+t.
}
\tag{13}
\]

Finally \(p\equiv\delta\pmod h\) and \(h\mid P\) give

\[
\boxed{h\mid\delta^2+\delta+1.}
\tag{14}
\]

### 3.1 The case \(W=0\)

Here \(b\mid m\).  By (4), \(3\le m\le e=b+1\).  The case \(b=2\) is
impossible; otherwise \(m=b\).  From (13), \(\delta=b\), while

\[
h=e(m-1)+\eta+1=b^2+\eta.
\]

By (14), \(h\) divides \(b^2+b+1\), hence divides

\[
(b^2+b+1)-h=b+1-\eta=e-\eta.
\]

This is a positive integer smaller than \(h\), a contradiction.  Hence
\(W\ne0\).

### 3.2 The case \(W=1\)

If \(e\) were odd, \(a\equiv\eta\pmod2\), and (9) would make
\(k=e\eta-a\) even.  Thus \(e,\eta\) are even and \(b\) is odd.  Now

\[
t=\frac{2m+\eta}{b}
\]

is even.  Its numerator is at most \(2e+(e-2)=3b+1<4b\), so \(t=2\).
Thus

\[
m=b-\frac\eta2,\qquad
\delta=2m,\qquad
p=e^2-\frac{e\eta}{2}-1.
\tag{15}
\]

The actual modulo-\(3\) alternatives are \(m\equiv0,1\pmod3\).  If
\(m\equiv1\pmod3\), then (1) gives

\[
(e,a,b,\eta)\equiv(2,2,1,2)\pmod3,
\]

contradicting the first identity in (15).  If \(m\equiv0\pmod3\), then
\(a\equiv0\pmod3\); the same identity forces
\(e\equiv1\) and \(\eta\equiv0\pmod3\), and the second identity in (15)
gives \(p\equiv0\pmod3\).  Both alternatives are impossible, so
\(W\ne1\).

### 3.3 The case \(W=2\)

If \(e\) were even, (9) would make \(k=e\eta-2a\) even.  Therefore
\(e,\eta\) are odd and \(m\) is even.  Here

\[
t=\frac{3m+2\eta}{b},\qquad 1\le t\le5.
\]

Because \(p=h+3(m-1)+t\equiv1\pmod3\), one has \(t\in\{1,4\}\).
For \(t=4\), \(\delta=3m+1\) is odd, hence \(p\) is even.

For \(t=1\),

\[
b=3m+2\eta,\qquad
h=3m^2-2m+(2m-1)\eta,\qquad
\delta^2+\delta+1=9m^2-9m+3.
\tag{16}
\]

Write the last integer as \(nh\).  As \(\eta>0\),

\[
h\ge3m^2-1,\qquad nh<3(3m^2-1),
\]

so \(n=1\) or \(2\).  For \(n=1\), (16) gives

\[
(2m-1)\eta=6m^2-7m+3=(2m-1)(3m-2)+1,
\]

which is impossible for \(m\ge4\).  For \(n=2\),

\[
(4m-2)\eta=3m^2-5m+3,
\]

whose two sides have opposite parity.  Thus \(W\ne2\).

### 3.4 The case \(W=3\)

Parity now makes \(e,\eta\) even and \(t\) even.  The bound from (13)
gives \(t\in\{2,4,6\}\).  Reducing
\(p=h+4(m-1)+t\) modulo \(3\) leaves two cases:

\[
(m,t)\equiv(0,2)\quad\text{or}\quad(1,4)\pmod3.
\tag{17}
\]

For the first case write \(\eta=2s\).  The equation \(2b=4m+3\eta\)
gives

\[
e=2m+3s+1,\qquad
h=2m^2-m+(3m-1)s,\qquad
\delta=4m-2.
\tag{18}
\]

Actual parity makes \(s\) odd, and the actual modulo-\(3\) condition makes
\(3\mid s\).  Let \(nh=16m^2-12m+3\).  Here \(n<8\).  Reducing this
equality modulo \(3m-1\), after multiplication by \(9\), gives

\[
3m-1\mid n+7.
\tag{19}
\]

Since \(m\) is a positive multiple of \(3\), (19) forces \(m=3,n=1\).
Equation (18) then gives \(s=12\), contradicting the oddness of \(s\).

For the second case, \(4b=4m+3\eta\), so write

\[
\eta=4s,\qquad e=m+3s+1,\qquad
h=m^2+(3m+1)s,\qquad\delta=4m.
\tag{20}
\]

Here \(m\ge4\), \(s\equiv2\pmod3\), and \(a=m-s>0\).  Let
\(nh=16m^2+4m+1\).  Since \(n\le17\), reduction modulo \(3m+1\), after
multiplication by \(9\), gives

\[
3m+1\mid13-n.
\tag{21}
\]

As \(3m+1\ge13\) and \(\lvert13-n\rvert\le12\), \(n=13\).  Equations
(20)--(21) give \(m+1=13s\), and then

\[
p=h+4m=208s^2+24s-3\equiv5\pmod8.
\]

This contradicts \(p\equiv1\pmod {24}\).  Thus \(W\ne3\), and

\[
\boxed{W\ge4.}
\tag{22}
\]

## 4. Fixed-\(W\) divisor reduction

Fix \(w=W\ge4\), and write

\[
F=\delta^2+\delta+1=nh,\qquad L=w(m-1)+t.
\tag{23}
\]

From \(m\le e=b+1\), \(1\le\eta\le b-1\), and (13),

\[
tb=(w+1)m+w\eta
\le(w+1)(b+1)+w(b-1)=(2w+1)b+1.
\]

As \(b>1\),

\[
\boxed{1\le t\le2w+1.}
\tag{24}
\]

Also

\[
h=e(m-1)+\eta+1\ge m(m-1)+2,
\qquad
\delta\le(w+1)m+w.
\]

For \(m\ge3\),

\[
F<(\delta+1)^2\le(w+1)^2(m+1)^2
\le\frac{16}{9}(w+1)^2m^2,
\]

while \(h\ge m(m-1)\ge2m^2/3\).  Therefore

\[
\boxed{1\le n<\frac83(w+1)^2.}
\tag{25}
\]

There is an exact divisor gate.  Equation (12) rearranges to

\[
wh+m=bL.
\tag{26}
\]

Since \(\delta=L+m-1\), multiplying (26) by \(n\) gives
\(L\mid wF+nm\).  Reducing after multiplication by \(w\), using

\[
wm\equiv w-t\pmod L,\qquad
F\equiv m^2-m+1\pmod L,
\]

gives

\[
\boxed{
L\mid C_{w,t,n}:=w^2-wt+t^2+n(w-t).
}
\tag{27}
\]

If \(C_{w,t,n}\ne0\), then (27) bounds \(L\), and thus \(m\), for its
fixed triple \((w,t,n)\).  If \(C_{w,t,n}=0\), put \(r=t-w\).
Necessarily \(r>0\): for \(t\le w\), both
\(w^2-wt+t^2\) and \(n(w-t)\) are nonnegative and the former is positive.
Then

\[
0=w^2+wr+r^2-nr,
\]

so

\[
\boxed{
t=w+r,\qquad r\mid w^2,\qquad
n=\frac{w^2}{r}+w+r.
}
\tag{28}
\]

The exceptional shapes admit a further exact normal form.  Put

\[
A=w^2+wr+r^2,\qquad R=r^2-r+1.
\]

Solving (26) and the defining equation for \(t\) gives

\[
\boxed{
\begin{aligned}
Ab&=r(w+1)^2m+wR,\\
Aa&=(w+1)(w+r-r^2)m-rR,\\
A\eta&=(w+1)\bigl(w(r-1)+r^2\bigr)m+(w+r)R.
\end{aligned}
}
\tag{29}
\]

Since \(a>0\), every exceptional shape must satisfy

\[
\boxed{r^2<w+r.}
\tag{30}
\]

The apparent exceptional shapes are all empty once the original stutter
equality is retained.  Put

\[
Q:=w(r-1)+r^2,\qquad x:=(w+1)m.
\]

Using (29), \(h=e(m-1)+\eta+1\), and
\(w+r-r^2+Q=r(w+1)\), direct collection in \(x\) gives

\[
\boxed{
Ah=r\bigl(x^2+(2r-1)x+R\bigr).
}
\tag{31}
\]

The original equality in (1) is \(eh-(pa+b)=0\).  Since
\(p=h+\delta\) and \(e-a=\eta+1\), its left side is
\(h(\eta+1)-\delta a-b\).  Substitution of (29) into this expression
gives the exact factorization

\[
\boxed{
\begin{aligned}
A^2\bigl(eh-(pa+b)\bigr)
={}&\bigl(x^2+(2r-1)x+R\bigr)\\
&\cdot
\bigl(rQx+A(r^2-w)+r(w+r)R\bigr).
\end{aligned}
}
\tag{32}
\]

The first factor is positive.  Thus an actual receipt on an exceptional
shape would satisfy

\[
rQx=A(w-r^2)-r(w+r)R.
\]

Combining this with the third line of (29) yields

\[
\boxed{
\eta=\frac{w-r^2}{r},\qquad
w=rs,\qquad s:=r+\eta\in\mathbb Z_{>r}.
}
\tag{33}
\]

Suppose first that \(r>1\).  Write
\(H:=s^2+s+1\) and \(S:=(r-1)s+r\).  Then \(A=r^2H\), \(Q=rS\),
and the displayed consequence of (32) together with the second line of
(29) gives the exact identity

\[
\begin{aligned}
rHSa
&=(s-r+1)\bigl(rH(s-r)-(s+1)R\bigr)-RS\\
&=H\bigl(rs^2-2r^2s+rs+r^3-2r^2+r-1\bigr).
\end{aligned}
\]

After cancellation of the positive factor \(H\), one obtains

\[
a=
\frac{rs^2-2r^2s+rs+r^3-2r^2+r-1}
{r\bigl((r-1)s+r\bigr)}.
\]

The numerator is \(-1\pmod r\), whereas the denominator is a positive
multiple of \(r\).  This contradicts \(a\in\mathbb Z\).

It remains to consider \(r=1\).  Then \(w=s\), \(Q=R=1\), and the
displayed consequence of (32) gives

\[
(s+1)m=(s^2+s+1)(s-1)-(s+1)=s^3-s-2
=(s+1)(s^2-s)-2.
\]

But \(s>1\), so \(s+1\nmid2\), contradicting \(m\in\mathbb Z\).
Consequently

\[
\boxed{C_{w,t,n}=0\text{ is impossible for every actual proper-root
stutter receipt}.}
\]

Thus each fixed complementary coordinate has only finitely many ordinary
divisor fibers; there is no exceptional infinite remainder.

## 5. The \(W=4\) fiber

It remains to test the first fiber not removed in Section 3.  Suppose
\(W=4\).  If \(e\) were even, then \(h\) odd would force \(\eta\) even,
and (9) would make \(k=e\eta-4a\) even.  Hence

\[
e,\eta\text{ are odd},\qquad m\text{ is even}.
\tag{34}
\]

The parity of \(p=h+\delta\), together with (13), makes \(t\) odd.
Reducing \(p=h+5(m-1)+t\) modulo \(3\) gives

\[
\begin{array}{c|c}
m\pmod3&t\\ \hline
0&3\ \text{or}\ 9\\
1&1\ \text{or}\ 7 .
\end{array}
\tag{35}
\]

For the four rows, the root divisor (14) has the following explicit form:

\[
\begin{array}{c|c|c|c}
t&h\text{ (after clearing }t\text{)}&
F=\delta^2+\delta+1&\text{bound on }n=F/h\\ \hline
1&h=5m^2-4m+(4m-3)\eta&25m^2-35m+13&n<5\\
3&3h=5m^2-2m+(4m-1)\eta&25m^2-15m+3&n<15\\
7&7h=5m^2+2m+(4m+3)\eta&25m^2+25m+7&n<35\\
9&9h=5m^2+4m+(4m+5)\eta&25m^2+45m+21&n<45.
\end{array}
\tag{36}
\]

For \(t=3,9\), the \(m\equiv0\pmod3\) branch has
\(\eta\equiv0\pmod3\), hence \(\eta\ge3\); for the other rows
\(\eta\ge1\).  These facts give the four displayed bounds directly.

Equation (27), with \(w=4\), gives respectively

\[
\begin{array}{c|c|c}
t&L& C_{4,t,n}\\ \hline
1&4m-3&13+3n\\
3&4m-1&13+n\\
7&4m+3&37-3n\\
9&4m+5&61-5n .
\end{array}
\tag{37}
\]

For \(t=1\), the only possible even \(m\equiv1\pmod3\) with
\(L\le13+3n\le25\) is \(m=4\), where \(L=13\) divides none of
\(16,19,22,25\).  For \(t=3\), the only possible even
\(m\equiv0\pmod3\) is \(m=6\); then \(L=23\) forces \(n=10\), but
\(10\nmid813=F\).

For \(t=7\), \(C_{4,7,n}\ne0\) and \(\lvert C_{4,7,n}\rvert\le65\).
Thus \(m\) can only be \(4\) or \(10\).  At \(m=4\), divisibility by
\(L=19\) forces \(n=6\) or \(25\), neither dividing \(F=507\); at
\(m=10\), it forces \(n\equiv41\pmod{43}\), outside \(1\le n<35\).

For \(t=9\), \(C_{4,9,n}\ne0\) and
\(\lvert C_{4,9,n}\rvert\le159\).  Hence

\[
m\in\{6,12,18,24,30,36\}.
\]

The remaining exact congruences are:

\[
\begin{array}{c|c|c}
m&\text{forced }n&F\bmod n\\ \hline
6&18&3\\
12&44&25\\
18&43&30\\
24&93&\text{outside the bound}\\
30&\text{none}&-\\
36&42&21 .
\end{array}
\tag{38}
\]

No listed \(n\) divides \(F\).  All four branches in (35) are empty, so

\[
\boxed{W\ge5.}
\tag{39}
\]

## 6. The companion gap \(\eta\ge5\)

The \(k=1\) domain is already empty, and \(k\) is odd.  Hence

\[
k\ge3.
\tag{40}
\]

Together with (9), \(W\ge5\), and \(a=e-1-\eta\), this reduces the four
small values of \(\eta\) to finite cases.

For \(\eta=1\),

\[
k\le e-5(e-2)=10-4e<1,
\]

which is impossible.  For \(\eta=2\), parity forces \(e,W\) even and odd,
respectively; positivity in (9) leaves only

\[
(e,a,W,k)=(4,1,5,3).
\]

But \(h=4m-1\) being divisible by \(3\) gives \(m\equiv1\pmod3\), whereas
the actual \(m\equiv1\pmod3\) branch requires \(a\equiv2\pmod3\).

For \(\eta=3\), parity forces \(e\) odd and \(W\) even.  Positivity and
(40) leave \(e=5\) or \(7\).  The \(e=5,a=1\) cases violate the actual
modulo-\(3\) classification.  The remaining case is

\[
e=7,\qquad a=3,\qquad W=6,\qquad k=3.
\]

It has \(m=6M\) and, from (13),

\[
t=7M+3,\qquad h=42M-3,\qquad \delta=49M-4,
\]

so

\[
p=h+\delta=7(13M-1),
\]

contrary to primality.

For \(\eta=4\), parity makes \(e\) even and \(W\) odd.  The actual
modulo-\(3\) conditions force \(m\equiv0\pmod3\) and
\(e\equiv2\pmod3\).  Positivity in (9) then leaves exactly

\[
(e,W)\in\{(20,5),(14,5),(8,5),(8,7),(8,9)\}.
\tag{41}
\]

In each case, (13) and \(3\mid m\) force the following parametrization:

\[
\begin{array}{c|c|c}
(e,W)&m&p\\ \hline
(20,5)&3+57r&59+1500r\\
(14,5)&27+39r&7(77+114r)\\
(8,5)&6+21r&83+312r\\
(8,7)&21r&360r-7\\
(8,9)&9+21r&167+408r .
\end{array}
\tag{42}
\]

The second row is divisible by \(7\).  The first row is
\(11+12r\pmod {24}\), hence is \(11\) or \(23\pmod {24}\); the last
three rows are \(11,17,23\pmod {24}\), respectively.  None is a core
prime.
Thus \(\eta=4\) is impossible.  Combining the four cases,

\[
\boxed{\eta\ge5.}
\tag{43}
\]

## 7. The strict coordinate order \(\eta<W\)

The two complementary coordinates are not independent.  Since \(U=e+W\),
(5) and \(pa+b=eh\) give

\[
\boxed{
hW=hU-eh=(p+1)b-a-eh=p\eta-a.
}
\tag{44}
\]

The bounds in (4) give \(h=em-a>2e>a\).  As \(p>h\), (44) rules out
\(W\le\eta-1\): that inequality would give

\[
hW\le h\eta-h<h\eta-a<p\eta-a=hW.
\]

If \(W=\eta\), then (44) gives \(a=\eta(p-h)\), and hence

\[
k=e\eta-aW=\eta(e-a)=\eta(\eta+1),
\]

which is even, contrary to the oddness of \(k\).  Therefore

\[
\boxed{W>\eta.}
\]

Writing \(\gamma:=W-\eta\), the exact norm quotient identity becomes

\[
\boxed{a\gamma=\eta(\eta+1)-k.}
\tag{45}
\]

Its right side is odd, so both \(a\) and \(\gamma\) are odd.  Since
\(a\ge1\) and \(k\ge3\) by (40), it also gives

\[
\boxed{
1\le\gamma\le\eta(\eta+1)-3,
\qquad
\eta<W\le\eta^2+2\eta-3.
}
\]

## 8. Complementary-coordinate primitivity

Put

\[
g:=\gcd(\eta,W).
\]

Assume that a prime \(q\) divides \(g\).  Equation (44) gives
\(q\mid a\), because both \(hW\) and \(p\eta\) are then divisible by
\(q\).  Hence \(q\mid b=a+\eta\), so \(e=b+1\equiv1\pmod q\).  Reduce
the two original linear identities modulo \(q\):

\[
pa+b=eh\quad\Longrightarrow\quad h\equiv0\pmod q,
\]

\[
W=ep-av\quad\Longrightarrow\quad p\equiv0\pmod q.
\]

Thus \(q\mid h\) and \(q\mid p\), impossible because \(p\) is prime and
\(0<h<p\).  Therefore

\[
\boxed{\gcd(\eta,W)=1.}
\tag{46}
\]

Together with (45), this also gives \(\gcd(\eta,\gamma)=1\).  This is a
primitivity theorem, not a terminal theorem: it does not produce an E1--E5
successor or physicalize a quotient factor.

## 9. Difference--quotient cyclotomic resonance

Put

\[
d:=\gcd(\gamma,k).
\]

Equation (45), together with \(\gcd(\eta,\gamma)=1\), gives

\[
\eta(\eta+1)\equiv0\pmod d,
\qquad
\eta\in(\mathbb Z/d\mathbb Z)^\times.
\]

Hence

\[
\boxed{d\mid\eta+1,\qquad d\mid W+1.}
\tag{47}
\]

Modulo \(d\), one has \(\gamma\equiv0\), \(\eta\equiv-1\), and
therefore \(W\equiv-1\), \(b=a+\eta\equiv a-1\), and \(e\equiv a\).
The identity (44) gives \(h\equiv p+a\).  Reduce \(pa+b=eh\) with
these substitutions:

\[
pa+a-1\equiv a(p+a)\pmod d,
\]

so

\[
\boxed{d\mid a^2-a+1.}
\tag{48}
\]

The actual three-adic split excludes \(3\mid d\).  Indeed, if
\(m\equiv0\pmod3\), then \(a\equiv0\pmod3\).  Since \(3\mid h\mid N\),
the congruence \(N\equiv b^2\pmod3\) gives \(b\equiv0\pmod3\).  Hence
\(e\equiv p\equiv1\pmod3\), \(W\equiv1\pmod3\), and
\(\gamma\equiv1\pmod3\).  If \(m\equiv1\pmod3\), then
\(a\equiv2\), \(b\equiv1\pmod3\).  Write \(a=-b+3z\); then

\[
N=3\bigl(b^2-3bz+3z^2\bigr),
\]

whose parenthesis is a unit modulo \(3\).  The actual root height has
\(v_3(h)=1\), so \(3\nmid k=N/h\).  Therefore

\[
\boxed{
d\mid\gcd(W+1,a^2-a+1),
\qquad 3\nmid d.
}
\tag{49}
\]

Every prime factor of a nontrivial \(d\) is consequently \(1\pmod3\).
This is a tight local condition on a quotient factor, not a physical carrier:
it does not show \(d\mid D_*\), construct a terminal, or provide an E1--E5
successor.

## 10. The composite resonant intersection with the actual divisor

Recall the actual stutter divisor identities

\[
D=mp+1-h,\qquad eD=ph+1,\qquad (D,h)=1,
\]

and write \(D_*=D/(D,h^2-1)\).  Set

\[
g:=(D,d).
\]

It is odd, \((g,3h)=1\), and the identities above can be used modulo the
whole composite modulus \(g\), not merely a prime divisor.  Since \(g\mid
D\), they give

\[
ph\equiv-1\pmod g,
\qquad
m\equiv h(1-h)\pmod g.
\tag{50}
\]

Since \(g\mid d\), (47) gives \(e\equiv a\pmod g\).  Thus
\(a=em-h\) gives

\[
h\equiv a(m-1)\pmod g.
\]

Put \(A:=h^2-h+1\).  Combining this with (50) gives

\[
m-1\equiv-A\pmod g,
\qquad
a\equiv-hA^{-1}\pmod g.
\tag{51}
\]

Here \(A\) is a unit modulo \(g\): every prime common divisor of \(A\) and
\(g\) would divide \(h\) by the preceding relation, contrary to
\((D,h)=1\).  Substitute (51) into (48).  After multiplication by
\(A^2\), this gives the composite divisibility

\[
\boxed{
g\mid\Phi(h):=h^4-h^3+3h^2-h+1.
}
\tag{52}
\]

Let \(q\) be a prime divisor of \((g,h^2-1)\).  Then
\(h\equiv1\) or \(-1\pmod q\), while \(\Phi(1)=3\) and
\(\Phi(-1)=7\).  Because \(3\nmid g\), the only possibility is

\[
q=7,
\qquad h\equiv-1\pmod7.
\]

This exceptional factor is at most simple.  Indeed, with \(x=h+1\),

\[
\Phi(-1+x)=7-14x+12x^2-5x^3+x^4.
\]

Thus \(7\mid x\) implies \(\Phi(h)\equiv7\pmod{49}\).  By (52),

\[
7\mid g\quad\Longrightarrow\quad v_7(g)=1.
\tag{53}
\]

Define

\[
g^\sharp:=\frac{g}{(g,7)}.
\]

All its prime factors are disjoint from \(h^2-1\).  Since \(g^\sharp\mid
D\), no valuation of \(g^\sharp\) is removed in forming \(D_*\).  Hence

\[
\boxed{
g^\sharp\mid\gcd(D_*,\Phi(h)).
}
\tag{54}
\]

The same carrier is visible from the root prime alone.  The polynomial
\(\Phi\) is reciprocal, and (50) gives \(-p\equiv h^{-1}\pmod g\).  Hence

\[
\boxed{
g\mid\Psi(p):=\Phi(-p)
=p^4+p^3+3p^2+p+1,
\qquad
g^\sharp\mid\gcd(D_*,\Psi(p)).
}
\tag{54a}
\]

Equivalently,

\[
\Psi(p)=N\bigl(p^2+1+p\omega\bigr),
\qquad
\Phi(h)=N\bigl(h^2+1-h\omega\bigr).
\]

This carrier has a precise transverse allocation.  Let \(q\) be a prime
factor of \(g^\sharp\), and put \(\delta_q=v_q(D)\).  Since

\[
\Psi(1)=7,
\qquad
\Psi(-1)=3,
\]

the facts \(q\mid\Psi(p)\), \(q\ne7\), and \(q\ne3\) imply
\(q\nmid p^2-1\).  By construction also \(q\nmid h^2-1\).  The actual
\(C/T\) factor split, with
\(D_T=D/(D,(p^2-1)/2)\), and the transverse residual map therefore give

\[
\boxed{
v_q(D_*)=v_q(D_T)=v_q(D)=\delta_q,
\qquad
q^{\delta_q}\mid\gcd\!\left(\frac Tu,m+2r\right).
}
\tag{54b}
\]

Thus a nonexceptional resonant factor is fully allocated to the \(T\)-side
of the actual receipt.  This is a valuation location theorem, not an
invocation of the older low-gap negative-root relays.

This is a composite conditional receipt bridge.  It does not prove \(g>1\),
but if a non-\(7\) quotient resonance meets \(D\), its full multiplicity is
an actual transverse \(D_*\) carrier rather than merely a quotient factor.

There are two useful local consequences.  From (50) and (52), a prime of
\((g,m)\) would force \(h\equiv1\) and hence divide \(\Phi(1)=3\), so

\[
\boxed{(g,m)=1.}
\tag{55}
\]

Likewise, a prime of \((g,m+2)\) forces
\(h^2-h-2\equiv0\), hence \(h\equiv2\) or \(-1\).  Equation (52) then
leaves only \(19\) or \(7\), respectively.  After the exceptional factor
has been removed,

\[
q\mid(g^\sharp,m+2)
\quad\Longrightarrow\quad
q=19,\quad h\equiv2\pmod{19},\quad p\equiv9\pmod{19}.
\tag{56}
\]

Thus the resonant carrier cannot enter the existing \(m\)-side terminal
branch; its only possible \(m+2\) contact is the specific \(19\)-adic
\(2p+1\) branch, not the \(q\equiv5\pmod8\) terminal subcase.

## 11. Existing fixed low-gap prime-carrier adapters miss the resonant carrier

The established root-residue adapter has positive low gaps

\[
\mathcal G=\{3,7,11,23\}.
\]

Suppose a prime \(q\mid g^\sharp\) entered one of its positive branches.
For its permitted odd \(A_0\mid p+3\), that branch has

\[
K\equiv A_0h\pmod q,
\qquad
s=\frac{q+A_0}{K}.
\]

Therefore \(sh\equiv1\pmod q\).  Combining this with (52) gives

\[
q\mid s^4\Phi(h)\equiv\Phi(s)\pmod q.
\tag{57}
\]

The four fixed values factor as

\[
\begin{array}{c|c}
s&\Phi(s)\\ \hline
3&79\\
7&3\cdot733\\
11&13\cdot1051\\
23&307\cdot877.
\end{array}
\tag{58}
\]

For \(s=7,11\), the adapter only allows \(A_0=1\), hence requires
\(q\equiv-1\pmod{2s}\).  The possible nonzero residues from (58) are

\[
733\equiv5\pmod{14},\qquad
13,1051\equiv13,17\pmod{22},
\]

none of which is \(-1\).  For \(s=23\), the allowed values are
\(A_0=1,5\).  The corresponding conditions are
\(q\equiv-1,-5\pmod{46}\), whereas

\[
307,877\equiv31,3\pmod{46}.
\]

It remains to consider the flexible \(s=3\) row.  Here (57) gives
\(q=79\), and integrality of \(K=(q+A_0)/3\) forces
\(A_0\equiv2\pmod3\).  But a terminal-first survivor has missed the exact
gap-\(3\) predicate, so every odd divisor of
\((p+3)/4\), and hence every eligible odd \(A_0\mid p+3\), is
\(1\pmod3\).  This is impossible.

Consequently, no prime factor of \(g^\sharp\) can by itself be consumed by
the existing positive root-residue low-gap adapter.  This is an obstruction
to one prime-carrier terminal/descent route, not a nonexistence theorem for
direct certificates or a proof that \(g^\sharp\) is nontrivial.  In
particular, it does not exclude a composite \(Q\mid D_*\) whose additional
prime factors are not resonant.

The negative low-gap relays are disjoint as well.  Their extra condition is

\[
q\mid s(h-1)+1,
\qquad q\equiv-1\pmod {2s}.
\]

It makes \(h\equiv(s-1)s^{-1}\pmod q\), so (52) gives

\[
q\mid\Theta(s):=s^4\Phi\!\left(\frac{s-1}{s}\right)
=3s^4-6s^3+6s^2-3s+1.
\tag{59}
\]

For the same four gaps,

\[
\begin{array}{c|c}
s&\Theta(s)\\ \hline
3&127\\
7&5419\\
11&7\cdot5233\\
23&769627.
\end{array}
\]

Their possible nonexceptional prime residues modulo \(2s\) are respectively
\(1\pmod6\), \(1\pmod{14}\), \(19\pmod{22}\), and \(1\pmod{46}\),
never \(-1\).  Thus no prime factor of \(g^\sharp\) enters the existing
low-gap negative-root relays by itself either.  This does not settle a
future whole-divisor or mixed-carrier construction.

## 12. The resonant carrier has a canonical natural variable gap

The preceding fixed-gap obstruction does not mean that the resonant carrier
has no natural gap at all.  In fact, its actual stutter relations force a
canonical variable one.  First eliminate \(p\) between the two congruences

\[
m p^2+p+1\equiv0\pmod g,
\qquad
\Psi(p)\equiv0\pmod g.
\tag{60}
\]

Put

\[
\begin{aligned}
A_m&=m^3-4m^2+3m-1,\\
B_m&=m^3-3m^2+2m-1,\\
\chi(m)&=m^4-6m^3+12m^2-9m+3.
\end{aligned}
\tag{61}
\]

Reduction of \(m^3\Psi(p)\) by the first congruence in (60) gives

\[
m^3\Psi(p)\equiv A_mp+B_m\pmod g.
\tag{62}
\]

Multiplying the first congruence in (60) by \(A_m^2\), then using (62),
gives

\[
0\equiv mB_m^2-A_mB_m+A_m^2
=m^3\chi(m)\pmod g.
\tag{63}
\]

The earlier local consequence \((g,m)=1\) in (55) therefore upgrades this
to the whole-composite carrier relation

\[
\boxed{g\mid\chi(m).}
\tag{64}
\]

This is compatible with, but sharper in its coordinate interpretation than,
the identity

\[
\chi\bigl(h(1-h)\bigr)=\Phi(h)\Phi(1-h),
\tag{65}
\]

Indeed, (50) gives \(m\equiv h(1-h)\pmod g\), while (52) selects the
actual \(\Phi(h)\)-oriented factor rather than the second factor in (65).

There is also a useful global size consequence.  Suppose for contradiction
that \(4g>p-2\).  Write \(p=4\lambda+1\).  Then \(g\ge\lambda\).  Since

\[
g\mid d\mid\eta+1,
\qquad
\eta+1\le e-1,
\tag{66}
\]

we obtain \(e\ge\lambda+1=(p+3)/4\).  On the other hand,

\[
D\ge(m-1)p+2,
\qquad
eD=ph+1\le p^2-p+1.
\tag{67}
\]

If \(m\ge5\), (67) gives the contradiction

\[
p^2-p+1\ge eD
\ge\frac{p+3}{4}(4p+2)>p^2-p+1.
\tag{68}
\]

Thus \(m=3\) or \(4\), because the actual domain has
\(m\ge3\) and \(m\not\equiv2\pmod3\).  At \(m=3\), (64) gives
\(g\mid\chi(3)=3\), contrary to \(3\nmid g\).  At \(m=4\), (64) gives
\(g\mid\chi(4)=31\).  Since \(p\ge73\) and \(g\ge(p-1)/4\ge18\), this
forces \(g=31\).  But (62) is then

\[
11p+23\equiv0\pmod{31},
\qquad
p\equiv12\pmod{31}.
\tag{69}
\]

Together with \(p\equiv1\pmod{24}\), this gives

\[
p\equiv601\pmod{744},
\tag{70}
\]

so \(p\ge601\), which contradicts \(4g=124>p-2\).  Therefore

\[
\boxed{g>1\Longrightarrow4g\le p-2.}
\tag{71}
\]

Assume now that \(g>1\), and let \(s\) be the unique representative modulo
\(4g\) satisfying

\[
sh\equiv1\pmod g,
\qquad
s\equiv3\pmod4,
\qquad 1\le s\le4g.
\tag{72}
\]

The modulus is valid because \(g\) is odd and \((g,h)=1\).  The second
congruence makes \(3\le s\le4g-1\), and (71) yields the natural range

\[
3\le s\le p-2.
\tag{73}
\]

Combining (50) with (72) gives \(g\mid p+s\).  Since also
\(4\mid p+s\), put

\[
C=\frac{p+s}{4g}\in\mathbb Z_{>0},
\qquad x=gC=\frac{p+s}{4}.
\tag{74}
\]

For every divisor \(r\mid g\), define \(d_r=rC\).  Then

\[
d_r\mid x^2,
\qquad d_r\le x,
\qquad x+d_r=C(g+r).
\tag{75}
\]

Consequently each actual divisor hit

\[
\boxed{r\mid g,
\qquad s\mid C(g+r)}
\tag{76}
\]

is a direct Type II certificate with gap \(s\) and divisor \(d_r\).  This
is a whole-carrier variable-gap terminal fan: it uses the actual composite
\(g\), not a synthetic prime factor or a fixed low-gap menu.  Its hit
condition has a sharper form because \(p\) is prime.  If
\(c=(s,C)\), then \(c\mid4gC-s=p\).  But \(c\le s\le p-2\), so

\[
\boxed{(s,C)=1.}
\tag{77}
\]

Also \(sh\equiv1\pmod g\) gives \((s,g)=1\).  Hence (76) is exactly the
single divisor-residue condition

\[
\boxed{s\mid C(g+r)
\quad\Longleftrightarrow\quad
s\mid g+r.}
\tag{78}
\]

The endpoint divisor \(r=g\) can never satisfy (78), since
\((s,2g)=1\) and \(s\ge3\).  The divisor \(r=1\) satisfies it precisely
when \(s\mid g+1\).  Therefore terminal-first failure of the whole fan
forces

\[
\boxed{s\nmid g+1,}
\tag{79}
\]

and the only remaining question is whether some proper divisor
\(r\mid g\) lies in the single residue class \(r\equiv-g\pmod s\).
For prime \(g\), (79) is the complete description of failure of this fan.

For a terminal-first survivor, the remaining resonant branch is now exact:
either \(g=1\), or the finite divisor set in (76) is empty.  No assertion
here says that the latter cannot happen.  Its nonemptiness, or an
identity-lifted descent for its failure, is the still-open part of the
proper-root physicalization problem.

## 13. Boundary

This is a structural reduction inside the actual proper-root stutter domain.
It proves that the fixed-\(W\) exceptional shapes are empty and locates a
resonant \(k\)-factor precisely when it meets \(D\).  It additionally turns
every nontrivial such intersection into a canonical natural-gap, finite
whole-carrier Type II menu, but it does not prove that the intersection is
nontrivial or that this menu always hits, bound \(W\) globally, or construct
an E1--E5 edge.  The fixed low-gap result only removes the current
prime-carrier adapter routes.  QC1, TR1, and
T6_GLOBAL_SELECTOR_TOTALITY therefore remain open.
