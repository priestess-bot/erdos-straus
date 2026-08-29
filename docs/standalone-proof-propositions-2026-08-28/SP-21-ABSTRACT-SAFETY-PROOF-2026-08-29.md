# SP-21 Abstract Safety Proof

**Status:** ESTABLISHED as an abstract policy theorem.
**Scope:** A finite frozen action policy, deterministic replay, sound terminal certificates,
and an independently verified selected edge.
**Exclusions:** No concrete coordinator policy, actual repository source, external authority,
common admission implementation, queue action, F1/F2/F3/T6 closure, or conjecture closure.

## 1. Policy Semantics

Let \(\mathscr S\) be a state universe. Fix a finite ordered policy

\[
\mathcal P=(A_0,\ldots,A_N).
\]

Every action has exactly one kind:

\[
K_i\in\{\mathsf{terminal},\mathsf{producer},\mathsf{reject}\}.
\]

For a fixed state \(S\), replay is deterministic and returns exactly one typed value:

\[
r_i(S)\in
\begin{cases}
\{\mathsf{MISS}\}\cup\{\mathsf{HIT}(c)\},&
K_i=\mathsf{terminal},\\
\{\mathsf{FALSE}\}\cup\{\mathsf{TRUE}(T)\},&
K_i=\mathsf{producer},\\
\{\mathsf{REJECT}(\rho)\},&
K_i=\mathsf{reject}.
\end{cases}
\tag{1}
\]

Every terminal hit is sound:

\[
r_i(S)=\mathsf{HIT}(c)
\Longrightarrow
c\in\mathsf{Sol}(S).
\tag{2}
\]

Define the unique continuation predicate:

\[
\operatorname{Pass}_i(S)
\Longleftrightarrow
\begin{cases}
r_i(S)=\mathsf{MISS},&K_i=\mathsf{terminal},\\
r_i(S)=\mathsf{FALSE},&K_i=\mathsf{producer},\\
\bot,&K_i=\mathsf{reject}.
\end{cases}
\tag{3}
\]

The selected action \(A_j\) is reachable exactly when

\[
\operatorname{Reach}_{\mathcal P,j}(S)
\Longleftrightarrow
\forall i<j,\ \operatorname{Pass}_i(S).
\tag{4}
\]

Let \(\operatorname{PriorClear}_{\mathcal P,j}(S)\) mean that every earlier terminal
replays to MISS and every earlier producer replays to FALSE, with a complete,
ordered, subject-bound record. Let

\[
\operatorname{NoRejectBefore}_{\mathcal P,j}
\Longleftrightarrow
\forall i<j,\ K_i\ne\mathsf{reject}.
\tag{5}
\]

Then

\[
\boxed{
\operatorname{Reach}_{\mathcal P,j}(S)
\Longleftrightarrow
\operatorname{PriorClear}_{\mathcal P,j}(S)
\land
\operatorname{NoRejectBefore}_{\mathcal P,j}.}
\tag{6}
\]

The reverse implication is immediate from (3). The forward implication gives the
required terminal/producer outputs and excludes an earlier reject because a reject
cannot satisfy \(\operatorname{Pass}\).

## 2. Prefix Partition

Running the policy in order yields exactly one of the following first outcomes:

\[
\mathsf{CONTINUE},\qquad
\mathsf{TERMINAL}(i,c),\qquad
\mathsf{PRODUCER}(i,T),\qquad
\mathsf{REJECTED}(i,\rho).
\tag{7}
\]

This follows by induction on the finite prefix length. If no action has decided,
the next typed replay has exactly one of the cases in (1); if a decision already
occurred, later actions do not change the first decision. Thus the selected index
is unique.

In particular, if \(A_j\) is a producer and \(r_j(S)=\mathsf{TRUE}(T)\), then

\[
\operatorname{Sel}_{\mathcal P}(S)=j
\Longleftrightarrow
\operatorname{Reach}_{\mathcal P,j}(S).
\tag{8}
\]

## 3. Scope-Bound Safety Theorem

Assume a selected producer \(A_j\) has independently established:

\[
\mathsf{EdgeOK}_j(S,T,\Lambda),
\tag{9}
\]

where \(\mathsf{EdgeOK}\) includes actual source occurrence, deterministic target,
common typing/admission, E5 ticket, and recursive re-entry. Assume also its
universal lift:

\[
\mathsf{LiftOK}(S,T,\Lambda)
\Longleftrightarrow
\forall u\in\mathsf{Sol}(T),\
\Lambda(u)\in\mathsf{Sol}(S).
\tag{10}
\]

Then:

\[
\boxed{
\begin{aligned}
\operatorname{Reach}_{\mathcal P,i}(S)
\land r_i(S)=\mathsf{HIT}(c)
&\Longrightarrow
\mathsf{SelectorTerminal}_{\mathcal P}(S,c),\\
\operatorname{Reach}_{\mathcal P,j}(S)
\land r_j(S)=\mathsf{TRUE}(T)
\land\mathsf{EdgeOK}_j(S,T,\Lambda)
\land\mathsf{LiftOK}(S,T,\Lambda)
&\Longrightarrow
\mathsf{VerifiedSuccessor}^{\mathrm{safe}}_{\mathcal P,j}(S,T).
\end{aligned}}
\tag{11}
\]

The first line follows from the prefix partition and (2). The second follows
from (8): the policy selects \(A_j\), while (9)--(10) supply the independent
edge and lift obligations.

No step of this proof assumes

\[
\mathsf{Sol}(S)=\varnothing
\tag{12}
\]

or that every imaginable terminal formula has been replayed. An unregistered
terminal certificate may exist without changing a fixed policy's earlier replay
records, the selected edge, or its universal lift. The theorem is a safety and
policy-fidelity result; global selector completeness still needs family totality
and well-founded induction.

## 4. Coordinator-Relative Version

Let a coordinator freeze a priority relation \(\prec_C\), action identities,
implementation/proof identifiers, owner/domain scope, branch index, and subject
binding outside the selected producer. For an earlier terminal \(A_i\) and
selected producer \(A_j\), require:

\[
\begin{aligned}
\mathsf{Overlap}(i,j)\land i\prec_Cj&\Longrightarrow i<j,\\
i\not<j&\Longrightarrow
\mathsf{Disjoint}(i,j)\ \lor\ j\prec_C i.
\end{aligned}
\tag{13}
\]

Together with common admission/re-entry and disjoint encodings of scope clearance
and global miss, (6) and (11) prove:

\[
\operatorname{PriorClear}_{\mathcal P,j}(S)
\land\operatorname{NoRejectBefore}_{\mathcal P,j}
\land r_j(S)=\mathsf{TRUE}(T)
\land\mathsf{EdgeOK}_j
\land\mathsf{LiftOK}
\Longrightarrow
\mathsf{VerifiedSuccessor}^{\mathrm{safe}}_{\mathcal P,j}(S,T).
\tag{14}
\]

The clearance receipt has the exact scope

\[
\mathsf{MISS\_HIGHER\_PRIORITY\_POLICY\_COMPLETE},
\qquad
\mathsf{coverage}=
\mathsf{REGISTERED\_HIGHER\_PRIORITY\_ONLY},
\qquad
\mathsf{global\_exhaustion}=\mathrm{false}.
\tag{15}
\]

It cannot be serialized as \(\mathsf{MISS\_COMPLETE}\).

## 5. Finite q=1 Control

For a fixed odd gap \(g\), put

\[
x_g=\frac{p+g}{4},
\qquad
D_g=px_g.
\]

The residual equation is

\[
\frac4p-\frac1{x_g}=\frac g{D_g}.
\]

For positive \(y,z\),

\[
\frac g{D_g}=\frac1y+\frac1z
\Longleftrightarrow
(gy-D_g)(gz-D_g)=D_g^2.
\tag{16}
\]

Hence a terminal action with first denominator \(x_g\) is finite and complete:
enumerate all positive divisors \(a\mid D_g^2\), set \(b=D_g^2/a\), and accept
exactly when

\[
a\equiv b\equiv-D_g\pmod g.
\tag{17}
\]

For

\[
p=21169,\qquad
X=\frac{p+3}{4}=5293=67\cdot79,
\]

Pocklington's criterion applies to

\[
p-1=21168=2^4 3^3 7^2
\]

with witness \(13\):

\[
13^{21168}\equiv1,\quad
13^{10584}\equiv-1,\quad
13^{7056}\equiv10710,\quad
13^{3024}\equiv20207
\pmod p,
\]

and

\[
\gcd(21167,p)=\gcd(10709,p)=\gcd(20206,p)=1.
\]

The complete residue checks for \(M_{23}=\{3,7,11,15,19,23\}\) are:

| \(g\) | \(-D_g\bmod g\) | \(\{a\bmod g:a\mid D_g^2\}\) |
|---:|---:|---|
| 3 | 2 | \(\{1\}\) |
| 7 | 5 | \(\{1,2,4\}\) |
| 11 | 2 | \(\{1,3,4,5,9\}\) |
| 15 | 11 | \(\{1,2,4,8\}\) |
| 19 | 12 | \(\{1,2,3,7,9,10,11,15,16\}\) |
| 23 | 20 | \(\{1,2,3,4,6,8,9,12,13,16,18\}\) |

Thus no row satisfies even the first congruence in (17), so all six finite
actions MISS. But for \(g=31\),

\[
x_{31}=5300,\qquad
\frac4{21169}
=\frac1{5300}+\frac1{3619899}+\frac1{19185464700}.
\tag{18}
\]

The M23 clearance is therefore a valid finite scope clearance, but it is not
a global terminal-universe miss. A policy may use it before a selected producer
only when the policy itself fixes that order and all the hypotheses of (14) are
separately established.

## 6. Exact Boundary

The abstract theorem in (11)--(15) is established. It does not establish:

1. an exact concrete coordinator policy;
2. external authority for that policy or any source;
3. an actual source-bound E1 receipt;
4. a repository successor-admission or queue action;
5. a concrete q=1 edge, F1/F2/F3/T6 totality, or the Erdős--Straus conjecture.

The submitted proof is retained at
docs/archive/proof-submissions/2026-08-29/SP-21-submitted-proof-2026-08-29.md;
the tracked copy differs from the submitted bytes only by removal of one final
blank line. Both SHA-256 values are recorded in that archive directory's README.
