---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-fourth-anchor-terminal-gate
title: q=1 高 C=2 的 H3 有界终端—第四锚—q=1 掩码分派
statement: >-
  对 65 类 terminal-first 菜单留下的 q=1 high C=2 19 相位 31 个 u (mod 119) 类，设
  H3 的 capacity 为 c3=(1536+a(p)p)/2261，w=(p+1)/2，g=gcd(w,c3)。则
  gcd(R3-1,K3)=2g，且 H3 的 raw p-source 和 p-free bundle 门对所有这些相位素数均通过。
  g 的所有奇素因子均落在由 17*rad(|1536-a(p)|) 给出的、素数不超过 1523 的显式有限
  掩码中。若 g 有某个 3 (mod 4) 素因子 ell，则 (A,C,k)=(1,(ell+1)/4,1) 是直接
  Type II terminal；若 g=1，则 Q3=(R3-1)/2 是完整 p-free excess，第四 p-anchor 的
  canonical capacity c4 满足 1<=c4<=p-2，可在 terminal-first miss 后作为既有 P=>H3
  persistent macro 的严格 E1--E5 延长；其余唯一分支是 g>1 且全部素因子为 1 (mod 4)
  的有界 q=1 掩码。31 个 u 类中 11 个没有任何可能的 1 (mod 4) 掩码素因子，余 20 个
  才可能进入这个 hard branch。该简化分派把 q=1 mask 交给后续最大超额 fourth-anchor
  adapter；`type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion` 已关闭 H3 的
  该后继缺口。两张卡都不构成全局出口定理。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-refined-affine-terminal-boundary
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-II-q-one-c-two-19-phase-third-p-anchor-finite-capacity-split
  - type-II-affine-uniform-divisor-rigidity
  - type-II-raw-ray-certificate
  - type-I-universal-p-source-capacity-anchor-orbit
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - bounded-mask
  - terminal-first
  - short-certificate
  - persistent-macro
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-refined-affine-terminal-boundary
    role: exact-31-class-terminal-first-input
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: charged-P-to-H3-parent-and-lift-contract
  - claim: type-II-q-one-c-two-19-phase-third-p-anchor-finite-capacity-split
    role: c3-selector-and-H3-carrier-data
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate.py
    role: symbolic-residue-finite-factor-and-dispatch-receipt
visibility: public
last_checked: '2026-08-15'
---

# q=1 high \(C=2\) H3 的终端—第四锚—\(q=1\) 掩码分派

## 1. The H3 obstruction is a small gcd

Retain the 31 residue classes \(\mathcal U_{31}\) left after the refined
affine terminal menu. For a phase prime, let

\[
p=912u+769,
\qquad
c_3=\frac{1536+a(p)p}{2261},
\qquad
w=\frac{p+1}{2},
\qquad
g=(w,c_3).
\tag{1}
\]

The H3 chart has \(K_3=M_3c_3\) and \(pR_3+1=4K_3\). Since \(p\) is a
unit modulo \(K_3\),

\[
(R_3-1,K_3)=(p+1,K_3).
\tag{2}
\]

For every odd prime divisor of \(w\), reduction of the first three anchor
factors at \(p=-1\) gives

\[
M_0\equiv1,quad Q_0\equiv-4,quad Q_1\equiv\frac{16}{3},
\quad M_2\equiv-\frac{64}{3},
\quad Q_2\equiv\frac{128}{19}\pmod q.
\tag{3}
\]

Here \(q\ne3,19\), because \(p\equiv1\pmod3\) and \(p\equiv9\pmod{19}\).
Thus \((w,M_2Q_2)=1\). The phase has \(p\equiv1\pmod {16}\), so
\(v_2(p+1)=1\), while \(K_3\) is even. Consequently (2) becomes the exact
identity

\[
\boxed{(R_3-1,K_3)=2(w,c_3)=2g.}
\tag{4}
\]

This avoids factoring the degree-28 quantity \(R_3-1\).

## 2. A bounded obstruction mask

If an odd prime \(q\mid g\) does not divide \(2261=7\cdot17\cdot19\), then

\[
0\equiv2261c_3=ap+1536\equiv1536-a\pmod q.
\tag{5}
\]

The residual 31 classes have \(p\bmod7\in\{1,2,4\}\), so \(7\nmid p+1\).
The primes 3 and 19 cannot divide \(p+1\); the only denominator exception is
17. Therefore

\[
\boxed{
\operatorname{rad}(g)\mid17\,\operatorname{rad}(|1536-a|).
}
\tag{6}
\]

Since \(a=13+19k\) with \(0\le k\le118\), every possible obstruction prime
is at most 1523. This is a bounded per-residue mask, not a factorization of a
large H3 residual.

There are 11 residue classes with no possible \(1\pmod4\) prime in (6):

\[
\{1,8,36,41,43,68,85,90,99,103,111\}.
\tag{7}
\]

Only the complementary 20 classes can enter the nonterminal \(q=1\) mask.

## 3. Source and endpoint gates at H3

Exact polynomial reduction gives

\[
\begin{aligned}
197955072R_3&\equiv57(2261a-8470528)\pmod p,\\
197955072(R_3-1)&\equiv57(2261a-11943424)\pmod p,
\end{aligned}
\tag{8}
\]

where

\[
197955072=2^9\cdot3^2\cdot7\cdot17\cdot19^2.
\tag{9}
\]

For each of the 31 fixed \(u\) classes, factorization of the two bounded
right sides in (8) has no prime in its own phase progression. Hence

\[
p\nmid R_3(R_3-1).
\tag{10}
\]

Thus the H3 universal \(p\)-source is primitive and its candidate excess is
always \(p\)-free.

When \(g=1\), (4) makes

\[
Q_3=\frac{R_3-1}{2},
\qquad (Q_3,K_3)=1.
\tag{11}
\]

It is therefore the complete-excess block. Let

\[
M_4=M_3Q_3,
\qquad
c_4\equiv c_3Q_3^{-1}\pmod p,
\qquad 1\le c_4\le p-1.
\tag{12}
\]

The top value \(c_4=p-1\) would force \(p\) to divide the fixed
\(a\)-dependent constant

\[
3072\cdot197955072+2261\cdot57(2261a-11943424).
\tag{13}
\]

The same exact finite phase-factor check finds no such prime in any of the
31 progressions. Therefore

\[
\boxed{1\le c_4\le p-2\quad(g=1).}
\tag{14}
\]

Conditional on the existing terminal-first guard and typed reclassification
at H3, (10)--(14) supply the universal source, path, complete block,
canonical target, identity solution lift, and strict endpoint needed to append
H3 \(\Rightarrow\) H4 to the already persistent \(P\Rightarrow H_3\) macro.

## 4. Exact three-way dispatch

The bounded gcd produces the following selector.

| H3 condition | Output |
|---|---|
| Some \(\ell\mid g\) has \(\ell\equiv3\pmod4\) | Type II terminal with \((A,C,k)=(1,(\ell+1)/4,1)\) and \(B=(p+1)/\ell\) |
| \(g=1\) | Strict fourth \(p\)-anchor macro with endpoint capacity \(c_4\le p-2\) |
| \(g>1\), all prime factors \(1\pmod4\) | Bounded \(q=1\) mask handoff to maximal-excess H4 |

The first row is a direct raw Type II certificate because
\(4ACk-1=\ell\mid p+1\). The last row is unresolved only by the present
clean-\(Q_3\) p-anchor formula, and its primes come from the explicit list (6).
The [maximal complete-excess fourth-anchor completion](type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion.md)
uses the actual block relative to \(K_3\), rather than pretending that the
whole \((R_3-1)/2\) is excess, and gives its strict H4 handoff.

Controls show all three outcomes: \(p=18097\) is clean and has \(c_4=13680\);
\(p=14449\) reaches the mask \(g=5\); and \(p=402049\) has \(g=11\) and the
direct terminal

\[
\frac4{402049}
=\frac1{109650}+\frac1{1206147}+\frac1{44084672850}.
\tag{15}
\]

This is a genuine terminal/clean-macro/mask-handoff dispatch. Its successor
eliminates the H3 mask as a missing fourth-anchor construction, but H4 still
needs a terminal-first selector; therefore it remains far short of a global
exit theorem.

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_fourth_anchor_terminal_gate.py --verify
```
