# F2 C8 Scope Freeze (2026-08-25)

> Track: `F2-C8-ATOMIC`
>
> This is an independent track handoff. It does not modify the shared frontier,
> README, family registry, or generated index.

## Exact Quantifier

Let `C8_ACTUAL` be the set of states \(P\) satisfying all of the following:

1. \(P\) is an actually admitted persistent ordinary \(q=1\), \(d=1\),
   full-carrier parent.
2. Its replayed even fixed-\(n\) macro has the zero-\(k\) \(c=8,j=11,g=1\)
   shape and selects the actual \(q_\star=103\) phase.
3. The complete terminal-first policy has been replayed and returned `MISS`.
4. The parent-to-checkpoint path, source scope, and raw occurrence are bound by
   a replayable receipt.

The arithmetic necessary source normal form is

\[
\begin{array}{c|c|c}
\text{ray}&s&p\\
\hline
 +&189+721v&9073+34608v\\
 -&704+721v&33793+34608v
\end{array}
\qquad v\ge 0,
\]

with the exact roughness condition

\[
25\nmid(42v+c),
\qquad
\ell\nmid(42v+c)\quad(7\le\ell<103,
\ell\text{ prime}),
\]

where \(c=11\) on the plus ray and \(c=41\) on the minus ray.

Core primality, ordinary \(q=1\ G\), complete terminal-first `MISS`, and the
parent/path receipt are separate guards; none may be inferred from the ray
congruence alone.

## Owned Partition

This track owns only:

- C8 outgoing selection after a real complete terminal-first `MISS`;
- C8 `DOUBLE_LOW` versus `OTHER` arithmetic target shapes;
- target-local terminal / centered-hit / F / G recomputation for an already
  source-bound atomic payload.

It does not own:

- F1 reachable-state exhaustion or common admission implementation;
- H4 non-atomic branches and high-support C1 residuals;
- F3 proper-root states;
- global T6 selector closure or the conjecture itself.

## Acceptance Boundary

An output is a `VERIFIED_SUCCESSOR` only with E1--E5 and selector re-entry.
In particular, a ray member, a finite congruence control, a caller-supplied
terminal receipt, a pending atomic target, or a local capacity drop is not an
accepted successor. The arithmetic second-full-excess fallback is retained only
relative to an actual \(P\in\texttt{C8_ACTUAL}\); its E1 and E3 are still external
obligations.
