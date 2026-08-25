# Agent 6 handoff: R4/R6 D-star freshness-capacity gate

## Baseline and ownership

- Baseline: 332c0f7ed48d453ca76d35639a618659d9b559ca.
- Track: F3-TR1 h-supported / transverse physicalization.
- Owned routes: R4_M3_NONQ5_H_SUPPORTED and R6_MGT3_H_SUPPORTED.
- This handoff does not edit shared frontier, README, theorem ledger, grammar, or generated index.

Preliminary artifacts:

- [scope freeze v2](../../data/t6-wave1/f3-tr1-scope-freeze-v2.json)
- [residual matrix v2](../../data/t6-wave1/f3-tr1-residual-matrix-v2.json)
- [target-shape proposal v2](../../data/interface-requests/f3-tr1-target-shapes-v2.json)
- [freshness-capacity claim](../../claims/type-I-t6-f3-tr1-dstar-freshness-capacity-gate.md)

## Exact scope

The quantified input is an actual persistent, low proper-root stutter receipt with

\[
2\le h=3u<p,\qquad k>1,\qquad k_\perp=1,\qquad D_*>1,
\]

after the complete terminal-first prefix and all preceding \(1<Q\mid u\) root menus
have been replayed and missed. The \(m=3,5\mid D_*\) branch, quotient-only branches,
high endpoints, and \(k=1\) are excluded.

The phrase “\(D_*\) factor” means a prime factor of the verified canonical maximal
receipt, not an arbitrary divisor satisfying the stutter congruence.

## New arithmetic result

For \(q\mid D_*\), set

\[
\delta=v_q(D),\quad
\tau=v_q(T),\quad
\zeta=v_q(R-h),\quad
a=v_q(A),\quad
c=v_q(p-1).
\]

The established theorem \(D_*\mid T\) implies \(q\mid T\) and \(q\mid A\). Canonical
maximality gives

\[
(v_q(D),v_q(E))=
\begin{cases}
(\zeta,0),&\zeta\le a+c,\\
(a,\zeta-a),&\zeta>a+c.
\end{cases}
\]

Therefore

\[
q\mid E\Longleftrightarrow \zeta>a+c,
\]

while

\[
q\nmid E\Longleftrightarrow \zeta=\delta\le a+c.
\]

The actual stutter multiplier gives an equivalent receipt-unit gate:

\[
E=1+p\sigma,\qquad
\sigma D=2T-(m+2r),
\]

and

\[
R-h=D+p(2T-(m+2r))=D(1+p\sigma).
\]

Hence

\[
q\mid E\Longleftrightarrow p\sigma\equiv-1\pmod q.
\]

This proves that a \(D_*\) divisor is not automatically a fresh consumable factor.

## Branch specializations

The two (p\pm1) overlap tables below are for odd (q) only. The (q=2)
factor is the separate R6 dyadic route and must use its dedicated 2-adic
normalization rather than these odd-prime formulas.

For \(q\mid m\), with
\(b=v_q(m)=v_q(p+1)=v_q(h-1)\) and \(t=v_q(D)-b\),

\[
q\mid E\Longleftrightarrow
v_q(T)=t\ \text{and}\ v_q(R-h)>b+t.
\]

For \(q\mid m+2\) and \(q\mid p-1\), with
\(b=v_q(m+2)=v_q(p-1)=v_q(h+1)\),

\[
q\mid E\Longleftrightarrow
v_q(T)=b+t\ \text{and}\ v_q(R-h)>2b+t.
\]

For the pure-\(T\) branch \(q\nmid p^2-1\),

\[
q\mid E\Longleftrightarrow v_q(R-h)>v_q(T).
\]

These are exact capacity tests, not sufficient source-path or admission theorems.

## Counter-boundaries

The focused pure-\(T\) relay controls at \(p=313,q=17,m=4\) realize both local
patterns:

\[
\begin{array}{c|cccc}
&v_q(T)&v_q(D_*)&v_q(E)&v_q(R-h)\\ \hline
\mathrm{T\text{-}slack}&2&1&0&1\\
\mathrm{high\text{-}excess\ E}&1&1&2&3
\end{array}
\]

They are explicitly synthetic q-primary controls: their height payload does not
satisfy the complete canonical root condition, and their \(D\) is a synthetic divisor.
They cannot be used as actual R4/R6 witnesses. A separate canonical \(p=283\) control
shows saturation outside the core-prime/low-height domain.

No actual R4/R6 capacity-saturated receipt has been claimed or found in this handoff.

## Consequences for TR1

The terminal-first residual must first exclude the established local terminal
subdomains

\[
q\mid(D_*,m), q\equiv3\pmod4
\quad	ext{and}quad
q\mid(D_*,m+2,2p+1), q\equiv5\pmod8.
\]

The first gives a direct Type-I certificate and the second a direct Type-II
certificate. Their complement, especially the (p-1,h+1) overlap and the
other pure-(T) residues, is not closed by this filter.

The full (W_y) word must use a frozen occurrence order and replay terminal-first
at every internal prefix. An internal terminal returns immediately; the initial
child MISS is not a receipt for all later prefixes. Subject to those prefix
receipts, the only valid deterministic selection rule is:

1. replay terminal-first and the complete \(1<Q\mid u\) root menu;
2. replay written \(D_*\) terminal menus;
3. recompute the freshness-capacity table from the actual maximal receipt;
4. reject capacity-saturated factors as raw labels;
5. choose the least factor with an independently replayable fresh integer occurrence;
6. only then attempt the common E1-E5 envelope and F1 re-entry.

Current status:

```text
R4 = OPEN_MINIMAL_RESIDUAL
R6 = OPEN_MINIMAL_RESIDUAL
TR1_INTEGER_RAW_OCCURRENCE = OPEN
OPEN_TR1_PHYSICAL_SERIALIZER = OPEN
F3 = OPEN
T6 = OPEN
```

This result proves neither FAMILY_EMPTY nor a terminal nor a verified successor. It
strictly removes the invalid shortcut \(q\mid D_*\Rightarrow q\mid E\).
