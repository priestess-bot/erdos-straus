# Agent 4 F3 High Endpoint Handoff

Track: F3-HIGH-ENDPOINT  
Branch: sol/f3-high-endpoint  
Base: 9215f8c92c53c0eb1081849b0a03e5cb922facad  
Conclusion: OPEN_MINIMAL_GAPS

## Exact Domain

\[
\mathrm{ACTUAL\_PERSISTENT}
\land\mathrm{PROPER\_FACTOR\_ROOT}
\land h>p
\land\mathrm{terminal\_first\_miss}.
\]

No arithmetic control, raw path, divisor, curve point, or finite scan is an
actual persistent witness.

## Established Reduction

Let

\[
C=p^2+p+1,\quad M=C/3,\quad u=(2r+1,M),\quad h=3u,\quad v=M/u.
\]

The high condition implies

\[
2\le v\le p-1,\qquad h=C/v,\qquad h-p-1>0.
\]

For an actual maximal receipt \(z=R-h=ED\), define

\[
c=\left\langle D(h-1)^{-1}\right\rangle_p.
\]

| Leaf | Established content | Exact blocker |
|---|---|---|
| HIGH_STRICT_CARRY | \(c\le p-2\). The rebase target \(M_{\rm ex}=\operatorname{lcm}(A,Q)=AE\), \(K_{\rm ex}=M_{\rm ex}c\), \(R_{\rm ex}=(4M_{\rm ex}c-1)/p\) has \(R_{\rm ex}>p\), so it is a Type-I overflow shape. | Common E3 normalizer, target owner/admission, and re-entry. E4 is identity and E5 is conditionally \((0,p-1)>(0,c)\). |
| HIGH_STUTTER_K1_PELL | \(c=p-1\), \(N=hk\), \(k=1\), and the Pell residual below. | Prove canonical-maximality, terminal-first, persistent points are empty, terminal, or paid. |
| HIGH_STUTTER_ODD_K_GE3 | \(c=p-1\), and high-domain \(k\) is odd. | High-valid bounded normal form or terminal/physical carrier theorem. |

For high stutter, the rederived identities are

\[
D=mp+1-h,\quad m\ge3,\quad eD=ph+1,\quad a=em-h>e,
\]

\[
N=a^2-a(e-1)+(e-1)^2=hk,\quad
m\mid a+3u,
\]

\[
L=am,\quad s=m-a,\quad
Lp=9u^2+3(a-1)u+s,\quad
u\mid L^2+Ls+s^2.
\]

These proofs do not import low-height \(a<e\), \(m<1+\sqrt h\),
\(0<N<e^2\), low \(k=1\) exclusion, \(D_*>1\), QC1, or TR1.

## K1 Pell Residual

When high \(k=1\), actual root algebra gives

\[
e=dx^2,\quad a=dxy-1,\quad (x,y)=1,\quad y>x,
\]

\[
d\equiv2\pmod3,\quad3\nmid x,\quad3\mid y,
\]

\[
y^2+xy-x^2=c_0(dxy-1),\qquad c_0\equiv1\pmod3.
\]

The core curve shadow \((d,x,y)=(11,101,1020)\) produces
\(p=115815206209\) and \(h=1169617882071>p\), but it is not in the
quantified domain: its curve divisor is not the canonical maximal receipt
divisor, and a gap-three Type-II terminal using factor \(8363\) preempts it.

## E1--E5 Boundary

| Item | Strict leaf | Stutter leaves |
|---|---|---|
| E1 | Assumed only through the exact actual-persistent quantifier. Fixed controls do not prove it. | Must replay actual receipt and path. |
| E2 | Deterministic rebase chart. | No target constructor. |
| E3 | Open shared normalizer, owner, and admission. | Open. |
| E4 | Identity on \(\operatorname{Sol}(4,p)\), conditional on admitted target scope. | Open. |
| E5 | Conditional local drop \((0,p-1)>(0,c)\). | Open absent a final target. |

The shared state contract currently gives each PROPER_ROOT state only a
proper_root_k split and no height-class fact. The coordinator must add an
exact high-source predicate or envelope before a high source is admitted; the
existing low family names cannot silently absorb this domain.

## Next Theorem

Prove either that every actual high \(k=1\) Pell point is noncanonical or
terminal, or that each has a deterministic E1--E5 successor. Then establish an
analogous high-valid reduction for odd \(k\ge3\). Every argument must retain
actual maximality, terminal-first priority, and the persistent source envelope.

## Commits

- b6ed66b: scope freeze, residual matrix, target proposal.
- 5a142b7: high normal form and strict overflow classification.
- 94b60ae: strict overflow owner refinement.
- d19e2d8: high \(k=1\) Pell residual.
- c3d00d2: final three-leaf high residual matrix.
