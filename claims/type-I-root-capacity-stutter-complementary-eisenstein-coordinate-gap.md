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
  对任意整数 c，gcd(g,m+c) 整除 c^4+6c^3+12c^2+9c+3；特别地，固定的
  quadratic shift K(K-1) 只能与 Phi(K)Phi(1-K) 的素因子相交。
  唯一可能被 h^2-1 吸收的 resonant 素因子是至多一次的 7。若 g>1，则 4g<=p-2。
  此外，若 n=(delta^2+delta+1)/h、d=gcd(W-eta,k)，则 d|n；把
  (eta+1)、W-eta、n、k 同时除以 d 后，得到 primitive Eisenstein norm。
  在 Z[omega] 中，gcd(d,delta+omega) 有范数 d，并给出一个 exact factor-level
  cancellation；当 d>1 时，其所有 unit-normalization 都不能重回同一 (p,h) 的正 ordinary
  stutter chart。对每个 d>1，由 a-h mod d 定义的 natural gap 有完整的 linear-divisor
  Type II fan，且其 cofactor 满足 C_d>=7、gap 不超过 (p-7)/6；D-overlap 的子因子还定向整除
  Phi(h) 与 Psi(p) 的指定 Eisenstein 因子。
  因而由 sh=1 mod g、s=3 mod4 确定的最小正 variable gap 总在自然范围内；令
  C=(p+s)/(4g)、x=gC，则 C>=2、m<=4C、p<1024C^5，且当 p>=2^15 时 s<8p^(4/5)，
  并有 gcd(s,x)=1。
  每个满足 t|x 且 t=-1 mod s 的 t 都确定给出一张直接 Type II 证书，取 d=x/t；
  这精确参数化了该 canonical gap 上所有满足 d|x 的 Type II 证书，并包含先前
  r|g、s|g+r 的 whole-carrier 子扇。
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
  - oriented-eisenstein-cancellation
  - factor-level-descent
  - unit-normal-form-obstruction
  - shifted-resultant
  - low-gap-obstruction
  - variable-gap
  - large-carrier-bound
  - sublinear-gap
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

In fact these divisibilities identify the whole rational content exactly.
Equation (45) gives \(k\equiv\eta(\eta+1)\pmod\gamma\), and (46) gives
\((\eta,\gamma)=1\).  Therefore

\[
\boxed{
d=(\gamma,k)=(\gamma,\eta+1)=(\eta+1,W+1).
}
\tag{47a}
\]

Thus \(d\) is precisely the integer coefficient content of
\(\epsilon-\beta=(\eta+1)-(W+1)\omega\), not merely a selected divisor
of that difference.

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

### 10.1 The full difference carrier has a primitive norm quotient

The preceding \(D\)-intersection is only a subcarrier of a stronger exact
identity that is present for the whole quotient resonance \(d\).  Recall from
(23) that

\[
\delta^2+\delta+1=nh.
\]

Expanding \(P=(h+\delta)^2+(h+\delta)+1=hv\) first gives

\[
v=h+2\delta+1+n.
\tag{54c}
\]

Substitute this in \(U=e(p+1)-av\), use \(p=h+\delta\),
\(eh=pa+b\), and \(e-a=\eta+1\).  The result is

\[
W=\eta+(\eta+1)\delta-an,
\qquad
\boxed{\gamma=(\eta+1)\delta-an.}
\tag{54d}
\]

By (47), \(d\mid\eta+1\) and \(d\mid\gamma\).  Also
\((a,d)=1\), since \(d\mid a^2-a+1\).  Hence (54d) proves the additional
whole-divisor alignment

\[
\boxed{d\mid n.}
\tag{54e}
\]

There is an equivalent norm form of this fact.  For this subsection put

\[
\beta:=a-b\omega,
\qquad
\epsilon:=e-U\omega,
\qquad
z:=\delta+\omega=p+\omega-h.
\]

Subtracting \(h\beta\) from the two sides of (6) gives the exact difference
factorization

\[
\boxed{
z\beta=h(\epsilon-\beta)
=h\bigl((\eta+1)-(W+1)\omega\bigr).
}
\tag{54f}
\]

Because \(W+1=\eta+1+\gamma\), taking norms in (54f) gives

\[
\boxed{
nk=(\eta+1)^2+(\eta+1)\gamma+\gamma^2.
}
\tag{54g}
\]

Write

\[
\sigma:=\frac{\eta+1}{d},
\qquad
\tau:=\frac{\gamma}{d},
\qquad
n_0:=\frac nd,
\qquad
k_0:=\frac kd.
\]

The quotients are integral by (54e) and the definition of \(d\), and (54g)
becomes

\[
\boxed{
n_0k_0=\sigma^2+\sigma\tau+\tau^2
=N\bigl(\sigma-(\sigma+\tau)\omega\bigr).
}
\tag{54h}
\]

This norm is primitive in its two displayed coordinates: the exact content
identity (47a) directly gives

\[
\boxed{(\sigma,\tau)=1.}
\tag{54i}
\]

### 10.2 Oriented Eisenstein cancellation of the whole \(d\)-carrier

The primitive quotient in (54h) is not merely a norm coincidence.  Let
\(R:=\mathbb Z[\omega]\), with \(\bar\omega=1-\omega\).  Every prime
factor \(q\) of \(d\) is \(1\pmod3\) by (49), so \(q\ne3\).  For
\(q^\nu\Vert d\), the congruences in Section 9 and the original linear
identity give

\[
\eta\equiv W\equiv-1,
\quad b\equiv U\equiv a-1,
\quad e\equiv a,
\quad h\equiv p+a,
\quad \delta\equiv-a
\pmod {q^\nu}.
\tag{54j}
\]

Here the fourth congruence follows from
\(pa+a-1\equiv ah\) and \(a^2-a+1\equiv0\); the element \(a\) is a
unit modulo \(q^\nu\).  Define the two conjugate Eisenstein ideals

\[
\mathfrak p_q=(q^\nu,\omega-a),
\qquad
\bar{\mathfrak p}_q=(q^\nu,\omega-(1-a)).
\]

The evaluation map \(\omega\mapsto a\) shows that
\(N(\mathfrak p_q)=q^\nu\).  The two roots are distinct because
\((2a-1)^2\equiv-3\not\equiv0\pmod q\).  Evaluating the three factors at
their indicated roots gives

\[
\begin{array}{c|c}
\mathfrak p_q & z=\delta+\omega\\
\hline
\bar{\mathfrak p}_q & \beta=a-b\omega,\quad \epsilon=e-U\omega .
\end{array}
\tag{54k}
\]

For example, \(z(a)=\delta+a=0\), while

\[
\beta(1-a)=\epsilon(1-a)
=a-(a-1)(1-a)=a^2-a+1=0.
\]

The opposite evaluations are \(1-2a\) for \(z\), and \(a+1\) for
\(\beta\) and \(\epsilon\); neither vanishes modulo \(q\), since
\(q\ne3\).  Thus these are the exact, rather than merely lower-bounded,
orientations at every prime power of \(d\).

The Eisenstein ring \(R\) is norm-Euclidean.  Hence the product of the
\(\mathfrak p_q\) has a generator \(\zeta_d\) with
\(N(\zeta_d)=d\).  The preceding exact orientations say, at the ideal level,

\[
\boxed{
(\zeta_d)=(d,z),
\qquad
(\bar\zeta_d)=(d,\beta)=(d,\epsilon).
}
\tag{54l}
\]

In particular \(\zeta_d\mid z\) and
\(\bar\zeta_d\mid\beta,\epsilon\).  Define the integral quotient elements

\[
Z_d:=\frac z{\zeta_d},
\qquad
B_d:=\frac\beta{\bar\zeta_d},
\qquad
E_d:=\frac\epsilon{\bar\zeta_d},
\qquad
Q_d:=\sigma-(\sigma+\tau)\omega.
\]

Since \(\epsilon-\beta=dQ_d=\zeta_d\bar\zeta_dQ_d\), both (6) and
(54f) reduce to the exact quotient identities

\[
\boxed{
(p+\omega)B_d=hE_d,
\qquad
E_d-B_d=\zeta_dQ_d,
\qquad
Z_dB_d=hQ_d.
}
\tag{54m}
\]

Their norms are

\[
\boxed{
N(Z_d)=\frac{hn}{d},
\qquad
N(B_d)=\frac{hk}{d},
\qquad
N(E_d)=\frac{vk}{d},
\qquad
N(Q_d)=\frac{nk}{d^2}=n_0k_0.
}
\tag{54n}
\]

Thus whenever \(d>1\), (54m) is a strict factor-level descent in both
positive quotient coordinates \(n\) and \(k\).  It is defined entirely by
the actual receipt: equivalently, \(\zeta_d\) is the Eisenstein gcd of the
rational integer \(d\) and \(\delta+\omega\), unique up to a unit.

### 10.2a Unit-normal-form obstruction for the factor quotient

The unit ambiguity in \(\zeta_d\) cannot repair the missing ordinary
stutter normal form.  More precisely, suppose \(d>1\).  Choose the unique
associate of \(\zeta_d\) in the open Eisenstein sector

\[
\zeta_d=r-s\omega,
\qquad r>s>0,
\qquad d=r^2-rs+s^2.
\tag{54n-1}
\]

Such an associate exists.  A boundary associate would be a unit times a
rational integer.  Since \(\zeta_d\mid z=\delta+\omega\), that rational
integer would divide the two primitive rational coordinates of a unit
multiple of \(z\), hence would be \(1\); this contradicts
\(N(\zeta_d)=d>1\).  The six unit sectors therefore contain one associate
with \(r>s>0\).  In particular,

\[
d-r=r(r-s-1)+s^2>0.
\tag{54n-2}
\]

Put

\[
E_0:=e+\gamma.
\tag{54n-3}
\]

The actual-coordinate bounds \(d\mid\eta+1\le e-1\) and \(\gamma\ge1\)
give

\[
E_0\ge d+2.
\tag{54n-4}
\]

Let \(u\) be any Eisenstein unit.  Replacing \(\zeta_d\) by
\(u\zeta_d\) replaces \((B_d,E_d)\) by \((uB_d,uE_d)\).  Write

\[
u\zeta_d=r_u-s_u\omega,
\qquad
uB_d=A_u-\mathsf b_u\omega,
\qquad
uE_d=\mathsf e_u-\mathsf U_u\omega.
\tag{54n-5}
\]

Using \(B_d=\beta\zeta_d/d\), \(E_d=\epsilon\zeta_d/d\), and
\(b=e-1\), their two coordinates relevant to the ordinary chart are

\[
\mathsf b_u=
\frac{as_u+b(r_u-s_u)}d,
\qquad
\mathsf e_u=\frac{er_u-Us_u}d.
\tag{54n-6}
\]

Since \(U=e+W\) and \(\gamma=W-\eta\), subtraction gives the exact
normal-form defect

\[
\boxed{
\mathsf e_u-\mathsf b_u-1
=\frac{r_u-s_uE_0-d}{d}.}
\tag{54n-7}
\]

An ordinary positive stutter re-entry at the same \((p,h)\) would require

\[
\mathsf e_u=\mathsf b_u+1,
\qquad
\mathsf b_u>0,
\tag{54n-8}
\]

because then \(uB_d\) would have the form
\(a'-(e'-1)\omega\), while \(uE_d\) would have constant coordinate
\(e'\).  The six possible left sides of the numerator condition in
(54n-7) are

\[
\begin{array}{c|c|c}
u&(r_u,s_u)&r_u-s_uE_0\\ \hline
1&(r,s)&r-sE_0\\
-1&(-r,-s)&sE_0-r\\
\omega&(s,s-r)&s+(r-s)E_0\\
-\omega&(-s,r-s)&-s-(r-s)E_0\\
\bar\omega&(r-s,r)&r-s-rE_0\\
-\bar\omega&(s-r,-r)&rE_0-(r-s).
\end{array}
\tag{54n-9}
\]

The rows \(1,-\omega,\bar\omega\) are negative.  The rows
\(\omega,-\bar\omega\) are strictly larger than \(d\): for the latter,

\[
rE_0-(r-s)=r(E_0-1)+s\ge2(d+1)+1>d.
\tag{54n-10}
\]

For \(u=-1\), the value is larger than \(d\) when \(s\ge2\), since

\[
sE_0-r\ge2(d+2)-r>d.
\tag{54n-11}
\]

The only numerical equality not already excluded is \(s=1\) and
\(E_0-r=d\).  But in that case (54n-6) gives

\[
\mathsf b_{-1}=-\frac{a+b(r-1)}d<0,
\tag{54n-12}
\]

contrary to the required positive ordinary coordinate in (54n-8).  Hence

\[
\boxed{
d>1\quad\Longrightarrow\quad
\text{no unit choice of the quotient pair in (54m) re-enters a positive
ordinary stutter chart at the same }(p,h).}
\tag{54n-13}
\]

This is a normal-form obstruction, not a new terminal or recursive edge.
It rules out only the direct strategy of interpreting the canonical quotient
itself as the next ordinary stutter receipt.  A genuine realization would
still need a different target construction together with source provenance,
an all-solution lift, and an E5 admission ticket.

The earlier carrier \(g=(D,d)\) is the \(D\)-visible subproduct of this
whole \(d\)-orientation.  Choose its compatible factor \(\zeta_g\mid
\zeta_d\).  For \(q^\nu\Vert g\), the additional congruence
\(ph\equiv-1\pmod {q^\nu}\) gives, at \(\omega=a\),

\[
h^2+1-ha=h(h-a)+1=ph+1=0,
\qquad
p^2+1+pa=p(p+a)+1=ph+1=0.
\]

Consequently the two norm divisibilities in (54) and (54a) have a fixed
Eisenstein orientation:

\[
\boxed{
\zeta_g\mid h^2+1-h\omega,
\qquad
\zeta_g\mid p^2+1+p\omega.
}
\tag{54o}
\]

This is not yet an actual recursive descent.  Section 10.2a proves that
even the direct unit-rechart of \((B_d,E_d)\) cannot retain the positive
ordinary stutter coordinate form; nor does it address the independent
\(\delta'+\omega\) requirement.  Nothing here supplies a source occurrence,
a legal target, an all-solution lift, or a T5 ticket.  The remaining
realization problem is therefore necessarily a different target construction
or a direct certificate, not a unit-normalization of (54m); without that
step, the factor quotient does not close QC1, TR1, or T6.

### 10.3 A natural full divisor fan for every nontrivial \(d\)

The same whole \(d\)-carrier also supplies a direct terminal family, without
requiring the additional \(D\)-intersection.  First, the proper-root norm
range gives a useful size bound.  Since \(m\ge3\), \(1\le a\le e-1\), and
\(b=e-1\),

\[
0<k=\frac{a^2-ab+b^2}{h}
<\frac{e^2}{h}
<\frac e{m-1}
<\frac h{(m-1)^2}
\le\frac h4<\frac p4.
\tag{54p}
\]

Thus \(d\le k<p/4\).  The divisor \(d\) is odd because
\(a^2-a+1\) is odd.  Assume \(d>1\), and let \(s_d\) be the unique
integer satisfying

\[
s_d\equiv a-h\pmod d,
\qquad
s_d\equiv3\pmod4,
\qquad
1\le s_d\le4d.
\tag{54q}
\]

The congruence \(h\equiv p+a\pmod d\) from (54j) gives
\(d\mid p+s_d\).  Since \(4d<p\), (54q) therefore gives the natural
gap range and an integral cofactor

\[
\boxed{
3\le s_d\le p-2,
\qquad
C_d:=\frac{p+s_d}{4d}\in\mathbb Z_{>0},
\qquad
x_d:=dC_d=\frac{p+s_d}{4}.
}
\tag{54r}
\]

In fact \(C_d\ge2\).  Otherwise \(p=4d-s_d\le4d-3\), contrary to
\(4d<p\).  The actual divisor relation gives a second useful bound:

\[
\boxed{m\le4C_d.}
\tag{54s}
\]

Indeed, \(d\mid\eta+1\le e-1\) gives \(e\ge d+1\), while
\(D\ge(m-1)p+2\) and \(eD\le p^2-p+1\).  If \(m\ge4C_d+1\), then

\[
p^2-p+1\ge eD
\ge(d+1)(4C_dp+2)
=\frac{p+s_d+4C_d}{4C_d}(4C_dp+2)>p^2,
\]

which is impossible.

The apparent endpoint \(C_d=2\) is also absent from the actual
proper-root domain.  Suppose otherwise.  Write

\[
\eta+1=d\sigma.
\]

Every prime factor of \(d>1\) is \(1\pmod3\), so \(d\equiv1\pmod3\).
As \(p=8d-s_d\equiv1\pmod3\), one has \(s_d\equiv1\pmod3\).  Moreover,

\[
h=a(m-1)+md\sigma<8d,
\]

so \(m\sigma<8\).  The actual modulo-\(3\) split used in the proof of
(49) says

\[
\begin{array}{c|c|c}
m\pmod3&a\pmod3&\sigma\pmod3\\
\hline
0&0&1\\
1&2&0.
\end{array}
\tag{54s-1}
\]

Together with \(m\ge3\) and \(m\not\equiv2\pmod3\), this leaves only

\[
(m,\sigma)=(3,1)\quad\text{or}\quad(6,1).
\tag{54s-2}
\]

For \(m=3\), write \(s_d=\lambda d-a\).  Positivity of \(s_d\) and
\(h<p\) give \(1\le\lambda\le4\).  The congruence
\(s_d\equiv1\pmod3\), together with \(a\equiv0\pmod3\), leaves
\(\lambda=1\) or \(4\).  Here

\[
p=(8-\lambda)d+a,
\qquad h=3d+2a,
\qquad e=a+d,
\qquad b=a+d-1.
\]

The exact relation \(pa+b=eh\) becomes

\[
a^2+(\lambda-3)ad-a+3d^2-d+1=0.
\tag{54s-3}
\]

For \(\lambda=4\), every grouped summand in

\[
(a^2-a+1)+ad+(3d^2-d)
\]

is positive.  For \(\lambda=1\), (54s-3), viewed as a quadratic in
\(a\), has discriminant

\[
(2d+1)^2-4(3d^2-d+1)=-8d^2+8d-3<0.
\]

Both cases are impossible.  For \(m=6\), write
\(s_d=\lambda d-4a\).  Positivity and \(h<p\) force \(\lambda=1\), so

\[
p=7d+4a,
\qquad h=6d+5a.
\]

The same exact linear relation now reads

\[
a^2+4ad-a+6d^2-d+1=0,
\]

again impossible because

\[
a^2+4ad-a+6d^2-d+1
=(a^2-a+1)+4ad+(6d^2-d)>0.
\]

Consequently

\[
\boxed{C_d\ge3.}
\tag{54s-4}
\]

The next value \(C_d=3\) is absent as well.  Suppose it occurs.  Then
\(h<p=12d-s_d<12d\), so \(\eta+1=d\sigma\) gives \(m\sigma<12\).
The split (54s-1) leaves only

\[
(m,\sigma)\in\{(3,1),(6,1),(9,1)\}.
\tag{54s-5}
\]

Write \(s_d=\lambda d-(m-2)a\).  The congruence
\(p=12d-s_d\equiv1\pmod3\) gives \(\lambda\equiv2\pmod3\), while
\(h<p\) gives \(\lambda\le11-m\).  Direct substitution in \(pa+b=eh\)
gives

\[
a^2+(2m-13+\lambda)ad-a+md^2-d+1=0.
\tag{54s-6}
\]

For \(m=6,9\), every permitted \(\lambda\) makes (54s-6) a sum of
positive grouped terms.  For \(m=3\), the permitted values are
\(\lambda=2,5,8\); the last is positive, and \(\lambda=5\) has
discriminant \(-8d^2+8d-3<0\).  The only remaining formal shape is

\[
m=3,\quad \sigma=1,\quad \lambda=2,\quad
s_d=2d-a,\quad p=10d+a,\quad h=3d+2a,\quad\delta=7d-a,
\tag{54s-7}
\]

\[
a^2-5ad-a+3d^2-d+1=0.
\tag{54s-8}
\]

Equation (54s-8) yields

\[
a^2-a+1=d(5a-3d+1),
\tag{54s-9}
\]

so \(a>(3d-1)/5\), while \(s_d>0\) gives \(a<2d\).  Reducing
\(\delta^2+\delta+1\) by (54s-8) gives

\[
\delta^2+\delta+1=d(46d-9a+8).
\tag{54s-10}
\]

Here \((h,d)=1\), because \(h=3d+2a\), \(d\) is odd, and \((a,d)=1\).
Thus \(h\mid\delta^2+\delta+1\) gives a positive integer \(q\) with

\[
46d-9a+8=q(3d+2a).
\tag{54s-11}
\]

The bounds above and \(d\ge7\) give

\[
4<q<\frac{203d+49}{21d-2}\le\frac{1470}{145}<11.
\]

Thus \(q\in\{5,6,7,8,9,10\}\).  Solving (54s-11) for \(a\), substituting
in (54s-8), and multiplying by \((9+2q)^2\), gives

\[
\bigl(51q^2-493q+289\bigr)d^2
+\bigl(2q^2-229q-119\bigr)d
+\bigl((9+2q)^2-8(9+2q)+64\bigr)=0.
\tag{54s-12}
\]

For \(q=5,6,7,8,9\), the quadratic, linear, and constant coefficients in
(54s-12) are respectively

\[
\begin{array}{c|rrr|r}
q&A_2&A_1&A_0&A_2+A_1+A_0\\
\hline
5&-901&-1214&273&-1842\\
6&-833&-1421&337&-1917\\
7&-663&-1624&409&-1878\\
8&-391&-1823&489&-1725\\
9&-17&-2018&577&-1458.
\end{array}
\]

Thus the left side is negative at \(d=1\) and strictly decreases thereafter.
For \(q=10\), it becomes
\(459d^2-2209d+673=0\), whose discriminant is \(5\pmod8\), not a square.
This excludes the last shape.  Hence

\[
\boxed{C_d\ge4.}
\tag{54s-13}
\]

The remaining boundary value \(C_d=4\) is absent too.  If it occurred,
then \(h<p=16d-s_d<16d\), hence \(m\sigma<16\).  Applying (54s-1) and
the congruence \(p\equiv1\pmod3\) gives

\[
(m,\sigma)\in
\{(3,1),(3,4),(4,3),(6,1),(9,1),(12,1),(15,1)\}.
\tag{54s-14}
\]

Write \(s_d=\lambda d-(m-2)a\).  The exact relation \(pa+b=eh\) becomes

\[
a^2+\bigl((2m-1)\sigma-16+\lambda\bigr)ad-a
+m\sigma^2d^2-d\sigma+1=0.
\tag{54s-15}
\]

Here \(\lambda\le15-m\sigma\); it is \(0\pmod3\) when \(m\equiv0\pmod3\)
and \(1\pmod3\) when \(m\equiv1\pmod3\).  Thus the complete permitted
list is (the nominal pair \((15,1)\) permits no positive \(\lambda\))

\[
\begin{array}{c|c|c}
m&\sigma&\lambda\\
\hline
3&1&3,6,9,12\\
3&4&3\\
4&3&1\\
6&1&3,6,9\\
9&1&3,6\\
12&1&3 .
\end{array}
\tag{54s-16}
\]

Directly grouping the positive terms in (54s-15), or taking its
discriminant when the \(ad\)-coefficient is \(-2\), eliminates every
entry of this list except

\[
\begin{array}{c|c|c|c|c}
m&\sigma&\lambda&p&\delta\\
\hline
3&1&3&13d+a&10d-a\\
3&1&6&10d+a&7d-a .
\end{array}
\tag{54s-17}
\]

For completeness, the discarded negative-coefficient cases are
\((m,\sigma,\lambda)=(3,1,9)\) and \((6,1,3)\), with discriminants
\(-8d^2+8d-3\) and \(-20d^2+8d-3\), respectively.  All other allowed
cases have nonnegative \(ad\)-coefficient in (54s-15), so are positive
after writing \(a^2-a+1\) as one group.

Consider first the second row of (54s-17).  Its equation is (54s-8), and
the canonical choice \(s_d\le4d-1\) gives \(a\ge2d+1\).  Since the
left side of (54s-8) is negative at both \(2d\) and \(4d\), its lower
root is below \(2d\) and its upper root is above \(4d\).  Hence an
integral root with \(a\ge2d+1\) must satisfy \(a>4d\).  Formula
(54s-10) still applies:

\[
\delta^2+\delta+1=dR,\qquad R=46d-9a+8.
\tag{54s-18}
\]

As \((h,d)=1\), \(h\mid\delta^2+\delta+1\) implies \(h\mid R\).
But \(R>0\), while \(a\ge4d+1\) and \(d\ge7\) give

\[
h-R=(3d+2a)-(46d-9a+8)=11a-43d-8>0.
\]

Thus \(0<R<h\), a contradiction.

For the first row of (54s-17), the relation is

\[
a^2-8ad-a+3d^2-d+1=0.
\tag{54s-19}
\]

Indeed, its values at \(d/3\), \(d/2\), and \(3d\) are respectively
\((2d-3)^2/9>0\), a negative number, and a negative number.  Since
\(s_d=3d-a>0\), the relevant root is therefore constrained by

\[
\frac d3<a<\frac d2.
\tag{54s-20}
\]

Reducing \(\delta^2+\delta+1\) by (54s-18) now gives

\[
\delta^2+\delta+1=d(97d-12a+11).
\tag{54s-21}
\]

Again \((h,d)=1\), so there is a positive integer \(q\) such that

\[
97d-12a+11=q(3d+2a).
\tag{54s-22}
\]

The bounds (54s-19) and \(d\ge7\) imply

\[
22<q<\frac{279d+33}{11d}<26,
\]

so \(q\in\{23,24,25\}\).  Solving (54s-21) for \(a\), substituting into
(54s-18), and multiplying by \((12+2q)^2\), gives

\[
(69q^2-1702q+529)d^2+(2q^2-448q-230)d
+(4q^2+26q+133)=0.
\tag{54s-23}
\]

For \(q=23,24\), respectively, this is

\[
-2116d^2-9476d+2847=0,\qquad
-575d^2-9830d+3061=0,
\]

whose left sides are negative for \(d\ge1\).  For \(q=25\), it is
\(1104d^2-10180d+3283=0\), impossible modulo \(2\).  This excludes
the first row and proves

\[
\boxed{C_d\ge5.}
\tag{54s-24}
\]

The next boundary value \(C_d=5\) is absent as well.  In this case
\(p=20d-s_d\), so \(s_d\equiv1\pmod3\), and \(h<p\) gives
\(m\sigma<20\).  The actual split (54s-1) leaves

\[
(m,\sigma)\in
\{(3,1),(3,4),(4,3),(6,1),(9,1),(12,1),(15,1),(18,1)\}.
\tag{54s-25}
\]

Writing \(s_d=\lambda d-(m-2)a\), the exact relation is

\[
a^2+\bigl((2m-1)\sigma-20+\lambda\bigr)ad-a
+m\sigma^2d^2-d\sigma+1=0.
\tag{54s-26}
\]

Here \(\lambda\le19-m\sigma\).  It is \(1\pmod3\) for
\(m\equiv0\pmod3\), and \(2\pmod3\) for \(m\equiv1\pmod3\).  The full
list is

\[
\begin{array}{c|c|c}
m&\sigma&\lambda\\
\hline
3&1&1,4,7,10,13,16\\
3&4&1,4,7\\
4&3&2,5\\
6&1&1,4,7,10,13\\
9&1&1,4,7,10\\
12&1&1,4,7\\
15&1&1,4\\
18&1&1 .
\end{array}
\tag{54s-27}
\]

The entries \((3,1,13)\), \((6,1,7)\), and \((9,1,1)\) have
\(ad\)-coefficient \(-2\) in (54s-26), with respective discriminants
\[
-8d^2+8d-3,\qquad -20d^2+8d-3,\qquad -32d^2+8d-3,
\]
and are impossible.  For \((3,1,7)\), the gap bounds put
\(3d+1\le a<7d\), while
\[
a^2-8ad-a+3d^2-d+1
\]
is negative at both \(3d\) and \(7d\); its two roots lie outside this
interval.  For \((3,1,10)\), the gap bounds give \(a\ge6d+1\), where
\[
a^2-5ad-a+3d^2-d+1
\]
is strictly increasing and already positive at \(6d\).  The two remaining
negative-coefficient cases with \(m=6\) are positive directly: for
\(\lambda=1\), \(a<d/4\) and

\[
(a^2-a+1)+d(6d-1-8a)>0;
\]

for \(\lambda=4\), \(a<d\) and

\[
(a^2-a+1)+d(6d-1-5a)>0.
\]

Every other entry of (54s-27) has nonnegative \(ad\)-coefficient in
(54s-26), hence is positive after grouping it as
\[
(a^2-a+1)+\bigl((2m-1)\sigma-20+\lambda\bigr)ad
+d\sigma(m\sigma d-1).
\]
Thus only the following two shapes remain:

\[
\begin{array}{c|c|c|c|c}
m&\sigma&\lambda&s_d&(p,\delta)\\
\hline
3&1&1&d-a&(19d+a,16d-a)\\
3&1&4&4d-a&(16d+a,13d-a).
\end{array}
\tag{54s-28}
\]

For the first row, put

\[
f_1(a):=a^2-14ad-a+3d^2-d+1.
\tag{54s-29}
\]

The gap gives \(0<a<d\), and

\[
f_1(d/5)=\frac{6d^2-30d+25}{25}>0,
\qquad
f_1(d/4)=\frac{-7d^2-20d+16}{16}<0.
\]

Since \(f_1(d)<0\), the root allowed by \(a<d\) satisfies

\[
\frac d5<a<\frac d4.
\tag{54s-30}
\]

Here \((h,d)=1\), and reducing \(\delta^2+\delta+1\) by (54s-29) gives

\[
\delta^2+\delta+1=d(253d-18a+17).
\tag{54s-31}
\]

Consequently

\[
253d-18a+17=q(3d+2a)
\tag{54s-32}
\]

for a positive integer \(q\).  If \(d=7\), (54s-30) has no integral
\(a\); otherwise \(d\ge13\), since every prime divisor of \(d\) is
\(1\pmod3\).  The bounds (54s-30) then give

\[
q>\frac{497}{7}=71,
\qquad
74h-(253d-18a+17)=166a-31d-17
>\frac{11d}{5}-17>0.
\]

Thus \(q<74\), so \(q=72\) or \(73\).  Solving (54s-32) for \(a\), substituting in
(54s-29), and multiplying by \(4(q+9)^2\), gives

\[
(105q^2-7630q+1225)d^2+(2q^2-1102q-560)d
+(4q^2+38q+307)=0.
\tag{54s-33}
\]

For \(q=72\), the left side is
\[
-3815d^2-69536d+23779,
\]
which is negative for \(d\ge1\).  For \(q=73\), it is
\[
3780d^2-70348d+24397,
\]
which is impossible modulo \(2\).  This excludes the first row.

For the second row of (54s-28), put

\[
f_2(a):=a^2-11ad-a+3d^2-d+1.
\tag{54s-34}
\]

Indeed,
\[
f_2(d/4)=\frac{5d^2-20d+16}{16}>0,
\qquad
f_2(d/3)=\frac{-5d^2-12d+9}{9}<0,
\qquad
f_2(4d)<0.
\]
Thus the root compatible with \(s_d=4d-a>0\) obeys

\[
\frac d4<a<\frac d3.
\tag{54s-35}
\]

The same coprimality \((h,d)=1\) and a reduction by (54s-34) give

\[
\delta^2+\delta+1=d(166d-15a+14),
\tag{54s-36}
\]

hence

\[
166d-15a+14=q(3d+2a)
\tag{54s-37}
\]

for a positive integer \(q\).  The bounds (54s-35) give
\[
q>\frac{483}{11}>43,
\qquad
q<\frac{649}{14}+\frac4d<47,
\]
so \(q\in\{44,45,46\}\).  After solving (54s-37) for \(a\), substituting
in (54s-34), and multiplying by \((15+2q)^2\), one obtains

\[
(87q^2-3973q+841)d^2+(2q^2-739q-377)d
+(4q^2+32q+211)=0.
\tag{54s-38}
\]

For \(q=44,45\), its coefficients are respectively
\[
(-5539,-29021,9363),\qquad(-1769,-29582,9751),
\]
so the left side is negative for every \(d\ge1\).  For \(q=46\), it is
\[
2175d^2-30139d+10147=0,
\]
which is impossible modulo \(2\).  The second row is excluded too.
Therefore

\[
\boxed{C_d\ge6.}
\tag{54s-39}
\]

There is a parity gate in every fixed-cofactor reduction which shortens the
next case.  Write \(\eta+1=d\sigma\), and use
\[
s_d=\lambda d-(m-2)a.
\]
This is possible because \(s_d\equiv a-h\equiv-(m-2)a\pmod d\).
Since \(a,d,s_d\) are all odd, it gives

\[
\boxed{\lambda\equiv m-1\pmod2.}
\tag{54s-41}
\]

Now suppose \(C_d=6\).  Then \(p=24d-s_d\), so \(s_d\equiv2\pmod3\),
and \(h<p\) gives \(m\sigma<24\).  Combining the actual split (54s-1)
with (54s-41), the complete permitted list is

\[
\begin{array}{c|c|c}
m&\sigma&\lambda\\
\hline
3&1&2,8,14,20\\
3&4&2,8\\
3&7&2\\
4&3&3,9\\
6&1&5,11,17\\
9&1&2,8,14\\
12&1&5,11\\
15&1&2,8\\
18&1&5\\
21&1&2 .
\end{array}
\tag{54s-42}
\]

The nominal pair \((m,\sigma)=(7,3)\) permits no positive \(\lambda\).
For every row in (54s-42), one has \(\lambda\le23-m\sigma\), and the
exact relation is

\[
a^2+\bigl((2m-1)\sigma-24+\lambda\bigr)ad-a
+m\sigma^2d^2-d\sigma+1=0.
\tag{54s-43}
\]

The rows \((3,4,2)\) and \((6,1,11)\) have negative discriminants
\[
-188d^2+20d-3,\qquad -20d^2+8d-3,
\]
respectively.  For \((3,1,8)\), the gap bounds give
\(4d+1\le a<8d\), while
\[
a^2-11ad-a+3d^2-d+1
\]
is negative at both endpoints \(4d\) and \(8d\).  For \((3,1,14)\),
the gap gives \(a\ge10d+1\), where
\[
a^2-5ad-a+3d^2-d+1
\]
is increasing and positive.  Finally, \((9,1,2)\) has discriminant
\(-11d^2+14d-3<0\).  Every remaining row has nonnegative
\(ad\)-coefficient in (54s-43), and is positive after the usual grouping.
Only

\[
\begin{array}{c|c|c|c|c}
m&\sigma&\lambda&s_d&(p,\delta)\\
\hline
3&1&2&2d-a&(22d+a,19d-a)\\
6&1&5&5d-4a&(19d+4a,13d-a)
\end{array}
\tag{54s-44}
\]

remain.

For the first row, set

\[
f_3(a):=a^2-17ad-a+3d^2-d+1.
\tag{54s-45}
\]

The allowed root has

\[
f_3(d/6)=\frac{7d^2-42d+36}{36}>0,
\qquad
f_3(d/5)<0,
\qquad
f_3(2d)<0,
\]
and hence

\[
\frac d6<a<\frac d5.
\tag{54s-46}
\]

As \((h,d)=1\), reducing \(\delta^2+\delta+1\) by (54s-45) gives

\[
\delta^2+\delta+1=d(358d-21a+20),
\tag{54s-47}
\]

so

\[
358d-21a+20=q(3d+2a)
\tag{54s-48}
\]

for a positive integer \(q\).  The bounds (54s-46) give

\[
q>\frac{1769}{17}>104,
\qquad
q<\frac{2127}{20}+\frac6d<108.
\]

Thus \(q\in\{105,106,107\}\).  Solving (54s-48) for \(a\), substituting
in (54s-45), and multiplying by \((21+2q)^2\), gives

\[
(123q^2-12997q+1681)d^2+(2q^2-1537q-779)d
+(4q^2+44q+421)=0.
\tag{54s-49}
\]

For \(q=105\), the left side is
\[
-6929d^2-140114d+49141,
\]
which is negative for \(d\ge1\).  For \(q=106\), it is
\[
6027d^2-141229d+50029,
\]
which is impossible modulo \(2\).  For \(q=107\), it is
\[
19229d^2-142340d+50925=0.
\]
Modulo \(5\) this forces \(5\mid d\), contrary to every prime factor of
\(d\) being \(1\pmod3\).  The first row is impossible.

For the second row, set

\[
f_6(a):=a^2-8ad-a+6d^2-d+1.
\tag{54s-50}
\]

The signs at \(4d/5\), \(6d/7\), and \(5d/4\) show that the root allowed
by \(0<s_d=5d-4a\le4d-1\) satisfies

\[
\begin{aligned}
f_6(4d/5)&=\frac{6d^2-45d+25}{25}>0,\\
f_6(6d/7)&=\frac{-6d^2-91d+49}{49}<0,\\
f_6(5d/4)&=\frac{-39d^2-36d+16}{16}<0,
\end{aligned}
\]

\[
\frac{4d}{5}<a<\frac{6d}{7}.
\tag{54s-51}
\]

Here \((h,d)=1\), because \(h=6d+5a\), \((a,d)=1\), and \(5\nmid d\).
The reduction of \(\delta^2+\delta+1\) is

\[
\delta^2+\delta+1=d(163d-18a+14),
\tag{54s-52}
\]

so

\[
163d-18a+14=q(6d+5a).
\tag{54s-53}
\]

The bounds (54s-51) give
\[
q>\frac{1033}{72}>14,
\qquad
q<\frac{743}{50}+\frac7{5d}<16,
\]
hence \(q=15\).  Substituting
\[
a=\frac{73d+14}{93}
\]
in (54s-50) and multiplying by \(93^2\) gives

\[
2911d^2-23810d+7543=0.
\tag{54s-54}
\]

Modulo \(5\), this would say \(d^2\equiv2\pmod5\), impossible.  The
second row is excluded, and therefore

\[
\boxed{C_d\ge7.}
\tag{54s-55}
\]

Combining \(p=4dC_d-s_d\) with \(s_d\le4d-1\) now sharpens the
canonical-gap range to

\[
\boxed{
s_d\le\frac{p-1}{C_d-1}-1\le\frac{p-7}{6}.
}
\tag{54s-56}
\]

The two factors in (54r) are coprime to the gap:

\[
\boxed{(s_d,d)=(s_d,C_d)=(s_d,x_d)=1.}
\tag{54t}
\]

For the first equality, a common prime would divide both \(d\) and
\(p+s_d\), hence \(p\), but it is smaller than \(p\) by (54p).  For the
second, a common prime would divide \(C_d\), \(s_d\), and
\(p=4dC_d-s_d\), while it is at most \(s_d\le p-2\).

Now let \(t\mid x_d\) satisfy \(t\equiv-1\pmod {s_d}\), and put
\(y=x_d/t\).  Then

\[
y\mid x_d^2,
\qquad y\le x_d,
\qquad s_d\mid x_d+y=y(t+1).
\]

The short-certificate equivalence therefore gives a direct Type II terminal.
Conversely, if \(y\mid x_d\) is a Type II certificate at this same gap,
then \(t=x_d/y\) is integral and (54t) forces
\(t\equiv-1\pmod {s_d}\).  Hence the full linear divisor layer is exactly

\[
\boxed{
\left\{y\mid x_d:s_d\mid x_d+y\right\}
=\left\{\frac{x_d}{t}:t\mid x_d,\ t\equiv-1\pmod {s_d}\right\}.
}
\tag{54u}
\]

Its whole-\(d\) subfan takes \(y=rC_d\) for \(r\mid d\); by (54t), its
hit condition is simply

\[
\boxed{r\mid d,\qquad s_d\mid d+r.}
\tag{54v}
\]

When \(d=g\), this is exactly the earlier canonical \(g\)-gap construction:
the extra relation \(ph\equiv-1\pmod g\) makes
\(a-h\equiv h^{-1}\pmod g\).  For general \(d\), (54u) is strictly
broader because it remains available even when \((D,d)=1\).

This is a direct-terminal expansion, not a totality proof.  After explicitly
applying (54u), its nonterminal residual is the decidable but still-open
divisor-residue condition

\[
\boxed{
d=1
\quad\text{or}\quad
\{t\mid x_d:t\equiv-1\pmod {s_d}\}=\varnothing.
}
\tag{54w}
\]

No argument here proves that the displayed divisor set is nonempty.  Until
such a proof is found, (54u) supplies additional terminal candidates but
does not close QC1, TR1, or T6.

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

### 12.1 Every fixed \(m\)-shift has a finite resonant resultant gate

There is a uniform version of the two local contacts in (55)--(56).  Let
\(c\in\mathbb Z\), and put

\[
Q_c:=(g,m+c).
\tag{65a}
\]

The two defining congruences (50) and (52) give, modulo \(Q_c\),

\[
h^2-h-c\equiv0,
\qquad
\Phi(h)\equiv0.
\tag{65b}
\]

Reducing the quartic modulo the displayed quadratic gives the exact linear
remainder

\[
\Phi(X)\equiv(c+2)X+(c^2+3c+1)
\pmod {X^2-X-c}.
\tag{65c}
\]

Write

\[
A_c:=c^2+3c+1,
\qquad B_c:=c+2.
\tag{65d}
\]

Thus \(B_ch+A_c\equiv0\pmod {Q_c}\).  Multiplication of the first
congruence in (65b) by \(B_c^2\), followed by this linear relation, gives

\[
\begin{aligned}
0
&\equiv B_c^2(h^2-h-c)\\
&\equiv A_c^2+A_cB_c-cB_c^2\\
&=c^4+6c^3+12c^2+9c+3
\pmod {Q_c}.
\end{aligned}
\tag{65e}
\]

Consequently every fixed integer shift obeys the whole-composite bound

\[
\boxed{
(g,m+c)\mid F(c):=c^4+6c^3+12c^2+9c+3=\chi(-c).}
\tag{65f}
\]

For a quadratic terminal shift \(c=K(K-1)\), identity (65) specializes this
to

\[
\boxed{
\bigl(g,m+K(K-1)\bigr)
\mid F\bigl(K(K-1)\bigr)
=\Phi(K)\Phi(1-K).}
\tag{65g}
\]

Thus a fixed \(K\) can touch the resonant carrier only through the finite,
\(K\)-dependent prime set of \(\Phi(K)\Phi(1-K)\).  For example,
\(F(0)=3\) recovers \((g,m)=1\), while

\[
F(2)=133=7\cdot19
\tag{65h}
\]

is the whole-composite precursor of the exceptional \(m+2\) contact in
(56).  This does not say that a resonant carrier grows outside every fixed
finite set, nor does it rule out a variable \(K\).  It does prove that a
selector whose only resonant-carrier tests are finitely many fixed quadratic
\(m\)-shifts can consume only the corresponding finite union of prime
factors; any other factor requires a variable \(K\) or additional
cross-parameter input.

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

The quotient cofactor \(C\) cannot stay bounded on this resonant branch.
First, (71) gives \(p\ge4g+2\).  If \(C=1\), then (74) would instead give

\[
p=4g-s\le4g-3,
\]

which is impossible.  Hence \(C\ge2\).  Moreover \(g\mid d\mid
\eta+1\le e-1\), so \(e\ge g+1\).  If \(m\ge4C+1\), then (67) yields

\[
D\ge4Cp+2,
\]

and consequently

\[
\begin{aligned}
p^2-p+1
&\ge eD\\
&\ge(g+1)(4Cp+2)\\
&=\frac{p+s+4C}{4C}(4Cp+2)>p^2,
\end{aligned}
\]

a contradiction.  Thus

\[
\boxed{C\ge2,\qquad m\le4C.}
\tag{74a}
\]

There is also a scale consequence intrinsic to the actual resonance.  Write

\[
\chi(m)=\bigl(m(m-3)\bigr)^2+3m(m-3)+3.
\tag{74b}
\]

For \(m\ge3\) this is increasing in \(m\).  By (64) and (74a),

\[
g\le\chi(m)\le\chi(4C)<(4C)^4,
\tag{74c}
\]

where the last inequality follows from

\[
z^4-\chi(z)=3(z-1)(2z^2-2z+1)>0
\qquad(z=4C>1).
\]

Combining (74) and (74c) proves the useful growth barrier

\[
\boxed{p<1024C^5,
\qquad C>\left(\frac p{1024}\right)^{1/5}.}
\tag{74d}
\]

The same estimate makes the canonical gap quantitatively sublinear.  From
\(s\le4g-1\) and (74),

\[
p=4gC-s\ge4g(C-1)+1,
\]

so

\[
\boxed{
s\le\frac{p-1}{C-1}-1.
}
\tag{74e}
\]

In particular, for \(p\ge2^{15}\), (74d) gives
\(C-1>p^{1/5}/8\), and hence

\[
\boxed{s<8p^{4/5}.}
\tag{74f}
\]

Thus any hit of the canonical full linear fan below supplies a genuinely
sublinear-gap Type II certificate on the resonant branch.  This does not
force a residue hit, but it rules out treating \(C\) as a bounded auxiliary
factor in a putative all-\(p\) proof.

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
when \(s\mid g+1\).  Therefore a miss of this explicitly evaluated
whole-\(g\) fan forces

\[
\boxed{s\nmid g+1,}
\tag{79}
\]

and the only remaining question is whether some proper divisor
\(r\mid g\) lies in the single residue class \(r\equiv-g\pmod s\).
For prime \(g\), (79) is the complete description of failure of this fan.

The \(g\)-carrier subfan is not, however, the full linear-divisor layer at
this canonical gap.  Since (77) and \((s,g)=1\) give

\[
\boxed{(s,x)=1,}
\tag{80}
\]

let \(t\mid x\) and put \(d=x/t\).  Then \(d\mid x^2\), \(d\le x\), and

\[
x+d=d(t+1).
\]

Therefore

\[
\boxed{
t\mid x,
\qquad t\equiv-1\pmod s
\quad\Longrightarrow\quad
d=\frac{x}{t}\ \text{is a direct Type II certificate at gap }s.
}
\tag{81}
\]

Conversely, if \(d\mid x\) is a Type II certificate at this same gap, then
\(t=x/d\) is integral and \(s\mid d(t+1)\).  Equation (80) makes \(d\) a
unit modulo \(s\), so \(t\equiv-1\pmod s\).  Hence (81) is an exact
parameterization:

\[
\boxed{
\left\{d\mid x:s\mid x+d\right\}
=\left\{\frac{x}{t}:t\mid x,\ t\equiv-1\pmod s\right\}.
}
\tag{82}
\]

The earlier whole-\(g\) fan is the subfan \(t=g/r\) with \(r\mid g\): its
condition \(s\mid g+r\) is precisely \(t\equiv-1\pmod s\), because
\((s,r)=1\).  Formula (82) also permits divisors carried by \(C\), and mixed
divisors of \(gC\).  A deterministic terminal rule may take the least
\(t\mid x\) in this residue class.  It is finite and reads only the actual
state data, but its nonemptiness is not yet proved.

Thus, after explicitly applying the full linear fan (82), the remaining
resonant branch is: either \(g=1\), or

\[
\boxed{\{t\mid x:t\equiv-1\pmod s\}=\varnothing.}
\tag{83}
\]

No assertion here says that (83) cannot happen.  Its exclusion, or an
identity-lifted descent for its failure, is the still-open part of the
proper-root physicalization problem.  Until this direct rule is integrated
into the state contract, a pre-existing scoped terminal-first digest must
not be read as a recorded miss of (82).

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
