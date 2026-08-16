---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-y-block-nonempty
title: H4 clean q-bridge 的 y 侧完整超额块必非空
statement: >-
  在 actual q=1 high C=2 19-phase H4 proper-overlap top-capacity a_alt=1 的 clean
  q bridge 中，令 endpoint 为 (x_q,y_q)=(R4-(R4-h)/q,(R4-h)/q)，并令
  Q_y=Q_K4(y_q)。则 h=2d、q=(p+1)/(2d)、hq=p+1，且高 H4 高度强制
  y_q>ph+1。因此 y_q 不整除 K4，故 Q_y>1。于是 actual endpoint 不可能是
  full-excess Type I sink，也不可能是 Q_y=1 的 x-side single-side payload；结合
  endpoint p-primary 排除与 first-stutter closure，剩余算术分派只有 Q_x=1<Q_y 的
  p-free y-side single-side payload，或 Q_x,Q_y>1 的 p-free atomic-split payload，且
  c_q<=p-2。该结果不支付任一 nonterminal payload 的 typed-state、priority、serializer、
  scope 或 atomic owner/ledger guard。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q-bridge
  - complete-excess-bundle
  - terminal-first
  - one-sided-payload
  - atomic-split
  - source-provenance
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: H4-carry-overlap-and-cubic-height-lower-bound
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-clean-q-word-and-endpoint-complete-excess-decomposition
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
    role: p-free-endpoint-domain
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
    role: strict-capacity-for-every-actual-nonterminal-endpoint
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: persistent-parent-rank-(0,p-1)
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_y_block_nonempty.py
    role: focused-prime-and-composite-q-height-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 clean \(q\)-bridge 的 \(y\) 侧完整超额块必非空

## 1. actual carrier 把 \(h\) 与 \(q\) 绑定

沿用 actual H4 clean \(q\)-bridge 的记号

\[
w=\frac{p+1}{2},\qquad d=(w,M_4),\qquad q=\frac wd,
\qquad h=(R_4-1,K_4),\qquad y_q=\frac{R_4-h}{q}.
\tag{1}
\]

这里 \(q>1\)。H4 carry-overlap 给出

\[
h=2e,\qquad e=(w,c_3-s_4),\qquad M_4=M_3L,\qquad (w,M_3)=1,
\tag{2}
\]

并且 \(Lc_4=c_3+ps_4\)。由于 \(p\equiv-1\pmod w\)，有

\[
d=(w,L)\mid (w,c_3-s_4)=e.
\tag{3}
\]

另一方面 \(e\mid h\mid K_4\)，而 clean carrier 给 \((q,K_4)=1\)，所以
\((e,q)=1\)。又 \(e\mid w=qd\)。合并 (3) 得 \(e\mid d\)，从而

\[
\boxed{h=2d,\qquad hq=p+1.}
\tag{4}
\]

这是 source carry 的结论，不是从 endpoint 的 complete-excess 分派反推的。

## 2. 高度强制 \(y_q\) 超过唯一可能的整除余数

proper-overlap 使 \(h\) 是 \(p+1\) 的真因子，因而

\[
h\le\frac{p+1}{2},\qquad q=\frac{p+1}{h}\le\frac{p+1}{2}.
\tag{5}
\]

H4 高度下界为

\[
R_4>\frac{p^3}{2}-\frac1p.
\tag{6}
\]

由 (1)、(5)--(6)，在核心域 \(p\ge73\) 有

\[
\begin{aligned}
y_q
&=\frac{R_4-h}{q}\\
&>\frac{p^3-p-1-2/p}{p+1}\\
&=p^2-p-\frac{1+2/p}{p+1}
>p^2-p-1\\
&>\frac{p^2+p+2}{2}
\ge ph+1.
\end{aligned}
\tag{7}
\]

最后一行只用 \(h\le(p+1)/2\) 及 \(p^2-3p-4>0\)。这给出的不是渐近估计，而是
actual H4 endpoint 上的严格不等式。

## 3. \(y\)-block 不可能为空

反设 \(Q_y=Q_{K_4}(y_q)=1\)。按 maximal complete-excess 的定义，这等价于

\[
y_q\mid K_4.
\tag{8}
\]

由 \(R_4=qy_q+h\) 及 \(pR_4+1=4K_4\)，有

\[
4K_4=pqy_q+ph+1.
\tag{9}
\]

式 (8) 遂强制 \(y_q\mid ph+1\)，这与 (7) 的

\[
0<ph+1<y_q
\tag{10}
\]

矛盾。因此

\[
\boxed{Q_y>1.}
\tag{11}
\]

特别地，\(Q_x=Q_y=1\) 的 full-excess sink 与 \(Q_y=1<Q_x\) 的 x-side
single-side payload 都不在 actual H4 high scope 中出现。前者的显式 Type I
serializer 仍是正确的条件公式，但这里的结论说明它在这个 scope 中没有触发实例。

## 4. 剩余分派与边界

endpoint p-primary exclusion 给 \(p\nmid Q_xQ_y\)，而 first-stutter closure 对每个
actual nonterminal endpoint 给 \(c_q\le p-2\)。配合 (11)，实际端点只剩：

| endpoint | 已支付的算术内容 | 未支付的内容 |
|---|---|---|
| \(Q_x=1<Q_y\) | p-free y-side single-side residual gate、\(c_q\le p-2\) | terminal/alternate priority、typed source/target、scope、serializer |
| \(Q_x,Q_y>1\) | p-free atomic payload、\(c_q\le p-2\) | 上述内容，加 atomic owner、ledger、adapter validator |

若这些独立 guards 以后通过，已有 persistent parent 的势仍从
\((0,p-1)\) 严格降到 \((0,c_q)\)。本卡不把该条件性宏登记为 verified edge，也不构造
新的 Type I/II certificate。

## 5. 聚焦回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_y_block_nonempty.py --verify
```

回执只重算既有 \(p=73,q=37\) 与 \(p=241,q=11^2\) 的两条 local H4 arithmetic
control 的 (4)、(7)、(9)--(11)。它不扫描素数、分母或历史 Reach，也不将这些 local
controls 视为 actual H3 predecessor。
