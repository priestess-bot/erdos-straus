---
kind: claim
claim_id: type-I-root-capacity-stutter-m-three-natural-fan-high-cofactor-barrier
title: proper-root m=3 natural-fan fan-miss 的 high-cofactor 与高端差 barrier
statement: >-
  在 actual proper-root m=3,d=13,s_d=3 natural-fan miss core 中，定义
  w=(p-h-1)/3。则 gcd(u,D(p+e))=1，且 exact high-end gates 为
  u divides 3w^2+3w+1、D=6u+9w+4 divides 9w^2+10w+4、
  52 divides 3u+3w+4。其 quotient barrier 给 R_w/u>=169，并可按
  beta=S_w/F 固定为有限 divisor-quadratic fiber，beta<75 全空。既有 primitive
  scale bounds further force C>=1993、w>=20779、p-h>=62338；在 even-z
  subbranch C>=11824、w>=127301、p-h>=381904。结论显著缩小 actual
  Diophantine residual，但不证明 high-C core 为空、fan hit、terminal、E1--E5 或 T6 closure。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-root-capacity-stutter-m-three-natural-fan-fixed-cofactor-second-norm-gate
  - type-I-root-capacity-stutter-m-three-natural-fan-small-cofactor-clearance
  - type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
topics:
  - type-I
  - f3
  - proper-root
  - m-three
  - natural-fan
  - high-cofactor
  - divisor-gate
  - scale-barrier
  - proof-boundary
sources:
  - claim: type-I-root-capacity-stutter-m-three-natural-fan-fixed-cofactor-second-norm-gate
    role: fixed fiber, second norm, and F/H identities
  - claim: type-I-root-capacity-stutter-m-three-natural-fan-small-cofactor-clearance
    role: initial C>=223 clearance
  - claim: type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
    role: primitive sigma, tau, theta, and z-parity scale bounds
visibility: public
last_checked: '2026-08-27'
---

# proper-root m=3 natural-fan fan-miss 的 high-cofactor 与高端差 barrier

## 1. Coprime factor carriers

Use the actual `m=3`, \(d=13\), \(s_d=3\) core. Put

\[
T=26C,
\qquad
N=3p^2+p+1=12T^2-34T+25,
\]

\[
P_0=\Phi_3(p)=p^2+p+1=4T^2-10T+7.
\]

The two exact identities

\[
N-3P_0=4(1-T),
\qquad
P_0-(T-1)(4T-6)=1
\tag{1}
\]

give \(\gcd(N,P_0)\mid4\). Both integers are odd, hence

\[
\boxed{\gcd(N,P_0)=1.}
\tag{2}
\]

The fixed fiber has \(F H=N\), while \(h=3u\mid P_0\). Therefore

\[
\boxed{\gcd(u,FH)=1.}
\tag{3}
\]

This is an arithmetic support separation: the height carrier cannot share a
prime with either fixed-fiber factor \(F=D\) or \(H=p+e\).

## 2. High-end difference normal form

Define

\[
w=\frac{p-h-1}{3}.
\tag{4}
\]

It is a positive integer. Indeed, \(w=0\) would make \(h=p-1\), but then
\(p-1\mid p^2+p+1\) would force \(p-1\mid3\), impossible for a core prime.
The defining identities become

\[
p=3u+3w+1,
\qquad
C=\frac{3u+3w+4}{52},
\tag{5}
\]

\[
F=D=6u+9w+4.
\tag{6}

\]

The second-norm gate has a high-end identity

\[
3P_0
=(52C-4-3w)(156C+9w-3)
+9(3w^2+3w+1).
\tag{7}
\]

Since \(52C-4-3w=3u\) and \((u,3)=1\), the fixed-fiber second norm is
equivalent to

\[
\boxed{u\mid R_w:=3w^2+3w+1.}
\tag{8}

\]

The first-norm identity \(AF=3u^2-u+1\) likewise gives

\[
12(3u^2-u+1)
=9(9w^2+10w+4)+F(104C-15w-14).
\tag{9}
\]

Here \(F\) is odd and \(F\equiv1\pmod3\), hence it is coprime to \(12\).
The first norm is therefore equivalently

\[
\boxed{F=6u+9w+4\mid S_w:=9w^2+10w+4.}
\tag{10}

\]

Thus the high-cofactor residual has the fully explicit necessary kernel

\[
u\mid R_w,
\qquad
6u+9w+4\mid S_w,
\qquad
52\mid3u+3w+4,
\tag{11}

\]

together with primality, fan-miss support, and the remaining primitive and
actual-receipt gates. The converse is not claimed.

## 3. A quantitative high-end barrier

From (10),

\[
6u+9w+4\le9w^2+10w+4,
\]

so (5) gives

\[
\boxed{104C\le9w^2+7w+8.}
\tag{12}

\]

Equivalently,

\[
w\ge
\left\lceil\frac{\sqrt{3744C-239}-7}{18}\right\rceil.
\tag{13}

\]

There is an independent stronger cofactor scale bound from the actual
primitive core. Write

\[
A=52t-1,\qquad
\sigma=37+54z,\qquad
\lambda=39\tau+\theta.
\]

The established bounds are

\[
t\ge13,\qquad \tau\ge\sigma+6,
\]

\[
\begin{array}{c|c|c}
z\bmod2&\sigma&\theta\\
\hline
1&\sigma\ge955&\theta\ge30\\
0&\sigma\ge5869&\theta\ge186
\end{array}
\tag{14}
\]

and the exact cofactor identity is

\[
52C=6A+65\sigma+2+\lambda.
\tag{15}
\]

Substitution of the lower bounds in (14)--(15) gives

\[
\boxed{z\text{ odd}\Longrightarrow C\ge1993,}
\tag{16}

\]

\[
\boxed{z\text{ even}\Longrightarrow C\ge11824.}
\tag{17}

\]

In particular every actual fan-miss core has \(C\ge1993\). Combining
(13) with (16)--(17) gives

\[
\boxed{
\begin{array}{c|c|c}
\text{branch}&w&p-h=3w+1\\
\hline
\text{all}&w\ge152&p-h\ge457\\
z\text{ even}&w\ge370&p-h\ge1111
\end{array}}
\tag{18}
\]

The estimates in (18) use only the norm-gate scale. The full primitive
parameterization gives a much stronger actual barrier. From (15),

\[
w=\frac{p-h-1}{3}=2\rho+\frac\lambda3.
\tag{19}
\]

The parity-dependent lower bounds in (14), together with
\(\lambda=39\tau+\theta\) and \(\tau\ge\sigma+6\), give

\[
\begin{array}{c|c|c|c|c}
z\bmod2&\sigma&\rho&\lambda&w\\
\hline
1&\ge955&\ge4138&\ge37509&\ge20779\\
0&\ge5869&\ge25432&\ge229311&\ge127301
\end{array}
\tag{20}
\]

Therefore

\[
\boxed{
\begin{array}{c|c|c}
\text{branch}&w&p-h=3w+1\\
\hline
\text{all}&w\ge20779&p-h\ge62338\\
z\text{ even}&w\ge127301&p-h\ge381904
\end{array}}
\tag{21}
\]

Thus the apparent short-distance high-end fan-miss region is family-empty.

## 4. Quotient Fiber

Put

\[
R_w=3w^2+3w+1=u\alpha,
\qquad
S_w=9w^2+10w+4=F\beta.
\tag{22}
\]

The identity \(S_w=3R_w+w+1\), together with (6), gives

\[
\boxed{
3u(\alpha-2\beta)=(9\beta-1)w+4\beta-1.}
\tag{23}
\]

Thus \(\alpha>2\beta\). The factor supports on the two sides are disjoint:

\[
S_w-3R_w=w+1,
\qquad R_w\equiv1\pmod {w+1},
\]

so \((R_w,S_w)=1\) and in particular \((u,F)=1\).

In the actual core, \(u\equiv11\pmod {13}\), while the \(52\)-gate in
(11) gives \(u+w\equiv16\pmod {52}\). Since \(u\) is odd, the two
possibilities modulo \(52\) are

\[
(u,w)\equiv(11,5)\quad\text{or}\quad(37,31)\pmod {52}.
\]

In either case \(R_w/u\equiv1\pmod4\). Also \(w\equiv5\pmod {13}\),
so \(13\mid R_w\), while \(13\nmid u\). Finally
\(R_w/u\equiv1\pmod3\). Consequently

\[
\alpha\equiv13\pmod {156}.
\tag{24}
\]

The six possible residues of \(w\) and \(\beta\) modulo \(156\) are

\[
\begin{array}{c|rrrrrr}
w\bmod156&5&31&57&83&109&135\\
\hline
\beta\bmod156&153&23&49&75&101&127
\end{array}
\tag{25}
\]

Combining (23)--(25) yields the unconditional actual quotient barrier

\[
\boxed{\alpha=\frac{R_w}{u}\ge169.}
\tag{26}
\]

It follows without the full primitive scale assumptions that

\[
3w^2+172w+1
\ge169\frac{52C-4}{3},
\tag{27}
\]

or equivalently

\[
w\ge
\left\lceil\frac{\sqrt{35152C+26868}-172}{6}\right\rceil.
\tag{28}
\]

For the already established \(C\ge1993\), this independently gives
\(w\ge1367\). It is weaker than (21), but needs only the quotient residue
data and is useful before the full primitive parameters have been reconstructed.

The same calculation yields a finite fiber at fixed \(\beta\). Let

\[
\delta=\alpha-2\beta,
\qquad A_\beta=9\beta-1,
\qquad B_\beta=4\beta-1,
\]

\[
Q_\beta=21\beta^2-3\beta+1.
\tag{29}
\]

Then (23) gives

\[
A_\beta w+B_\beta=3u\delta.
\tag{30}
\]

The polynomial identity

\[
A_\beta^2R_w-Q_\beta
=3\bigl(9\beta w+5\beta-w\bigr)
 \bigl(A_\beta w+B_\beta\bigr)
\tag{31}
\]

and \(u\mid R_w\) imply

\[
\boxed{u\mid Q_\beta.}
\tag{32}
\]

For each divisor \(u\mid Q_\beta\), equation (30) fixes
\(w=(3u\delta-B_\beta)/A_\beta\), and the remaining relation

\[
3(3u\delta-B_\beta)^2
+3A_\beta(3u\delta-B_\beta)+A_\beta^2
=(2\beta+\delta)uA_\beta^2
\tag{33}
\]

is a nondegenerate quadratic in \(\delta\). Hence fixed \(\beta\) gives a
finite divisor-quadratic fiber, not an unrestricted two-parameter search.

As a first exact clearance, the actual residue conditions make
\(\beta\equiv23\pmod {26}\). If \(\beta<75\), only \(\beta=23,49\) are
possible. But

\[
Q_{23}=11041=61\cdot181,
\qquad
Q_{49}=50275=5^2\cdot2011,
\]

and their positive divisor residues modulo \(13\) are respectively

\[
\{1,4,9,12\},
\qquad
\{1,4,5,6,9,12\}.
\]

Neither set contains the required \(u\equiv11\pmod {13}\). Therefore

\[
\boxed{\beta\ge75.}
\tag{34}
\]

This quotient clearance is still only a necessary arithmetic sieve.

## 5. Boundary

This is a necessary-core high-cofactor barrier. It does not prove that a
packet satisfying (11) exists, that all high fibers are empty, or that the
natural fan hits. It supplies no terminal, source path, E1--E5 bundle,
admission, re-entry, or global T6 conclusion.
