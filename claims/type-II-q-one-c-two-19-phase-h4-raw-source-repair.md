---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-raw-source-repair
title: q=1 高 C=2 19 相位 H4 的零残数 raw-source 修复
statement: >-
  在 q=1 high C=2 19 相位的既有 persistent P=>H4 maximal-complete-excess
  receipt 中，设 H4 已通过 terminal-first 和 typed guards，且 R4=0 (mod p)。令
  Q5=Q_K4(R4-1)，M5=lcm(M4,Q5)，c5 为其 canonical capacity，并令 q_star 是
  不整除 R4 K4 (R4-1) 的最小素数。则
  (q_star,R4(q_star-1)-q_star,q_star-1) 是一条实际 primitive source/path receipt，
  其 q_star-edge 的唯一 shift 到同一 anchor (1,R4-1,1)；Q5 非平凡、p-free，且 q_star 不整除 Q5。
  因而 source 替换不改变 Q5、M5 或 c5。若 c5<=p-2，原 persistent parent 有 strict
  H5 endpoint；若 c5=p-1，既有 H5 d=1 handoff 与 a5=1 finite-sieve completion 给出
  capacity 小于 p-1 的最终 endpoint。故在所有 source/path、terminal-first、typed 和
  serializer guards 通过时，R4=0 (mod p) 不再是 fifth-anchor macro 的算术例外，而有
  P 的 E1--E5 guarded strict exit。该结论不处理 R4=1 (mod p)，也不创建 fresh root
  或证明整个 G/Type I 全局出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
  - type-II-q-one-c-two-19-phase-h5-top-capacity-d-one-handoff
  - type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-sieve-completion
  - type-I-chart-least-coprime-prime-anchor-source
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - fifth-anchor
  - raw-source
  - least-coprime-prime
  - p-free
  - complete-excess
  - capacity-map
  - guarded-macro
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
    role: existing-persistent-parent-and-parent-rank
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: actual-H3-to-H4-maximal-complete-excess-receipt
  - claim: type-II-q-one-c-two-19-phase-h4-carry-overlap-boundary
    role: H4-height-and-anchor-overlap-bound
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: same-anchor-source-substitution
  - claim: type-II-q-one-c-two-19-phase-h5-top-capacity-d-one-handoff
    role: top-capacity-suffix-dispatch
  - claim: type-II-q-one-c-two-19-phase-h5-a-one-full-overlap-sieve-completion
    role: actual-a5-one-top-capacity-residual-exclusion
  - concept: denominator-escape-state-contract
    role: path-anchored-E1-to-E5-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_raw_source_repair.py
    role: exact-zero-residue-source-substitution-controls
visibility: public
last_checked: '2026-08-15'
---

# H4 \(R_4\equiv0\pmod p\) 的同锚 source 修复

## 1. 问题只在原来的 source 标签

保留 H3 \(\Rightarrow\) H4 maximal complete-excess receipt 的记号：

\[
K_4=M_4c_4,
\qquad
pR_4+1=4K_4,
\qquad
1\le c_4\le p-2.
\tag{1}
\]

它已经附在一个 persistent parent \(P\) 上，满足

\[
\Lambda_p^\sharp(P)=(0,p-1).
\tag{2}
\]

H4 的 height 和 overlap 结论给出

\[
R_4-1>p+1,
\qquad
(R_4-1,K_4)\le p+1,
\qquad
p\nmid K_4.
\tag{3}
\]

现在只考虑原 universal \(p\)-source 失去 primitive 性的情形

\[
R_4\equiv0\pmod p.
\tag{4}
\]

式 (4) 并不使 fifth-anchor carrier 失去 p-free 性；恰好相反，

\[
R_4-1\equiv-1\pmod p.
\tag{5}
\]

令

\[
V=R_4-1,
\qquad
Q_5=Q_{K_4}(V),
\qquad
M_5=\operatorname{lcm}(M_4,Q_5).
\tag{6}
\]

由 (3)，\(V\nmid K_4\)，所以 \(Q_5>1\)；由 (5)，

\[
\boxed{p\nmid Q_5.}
\tag{7}
\]

因此 (4) 只破坏旧 source 的 primitive 性，并未破坏 maximal complete-excess
bundle 的 p-free 前提。

## 2. 规范同锚替换

取

\[
q_\star=\min\{q:q\text{ 是素数且 }q\nmid R_4K_4(R_4-1)\}.
\tag{8}
\]

特别地，\(q_\star\ne p\)，因为 (4) 使 \(p\mid R_4\)。定义

\[
(U_\star,V_\star,m_\star)
=\bigl(q_\star,\ R_4(q_\star-1)-q_\star,\ q_\star-1\bigr).
\tag{9}
\]

由 (8)，\(q_\star\nmid R_4K_4\)，而

\[
\begin{aligned}
U_\star+V_\star&=R_4m_\star,\\
(U_\star,V_\star)&=(q_\star,R_4)=1,\\
V_\star&=(q_\star-1)R_4-q_\star>0,\\
\nu_{q_\star}(U_\star V_\star)&=1>0=\nu_{q_\star}(K_4).
\end{aligned}
\tag{10}
\]

\(q_\star\)-edge 的唯一可用 shift 是 \(t=1\)，所以没有额外 gcd 约分的 raw output 为

\[
\left(
\frac{U_\star}{q_\star},
\frac{V_\star+R_4}{q_\star},
\frac{m_\star+1}{q_\star}
\right)
=(1,R_4-1,1).
\tag{11}
\]

这正是原 fifth-anchor 所需的同一个 anchor。又因 \(q_\star\nmid R_4-1\)，

\[
q_\star\nmid Q_5.
\tag{12}
\]

所以新 source 标签既不与 \(K_4\) 容量冲突，也不与 bundle occurrence 冲突。\(Q_5\)
由 \((V,K_4)\) 唯一决定，故 source 替换保持

\[
\boxed{(Q_5,M_5,c_5)\ \text{不变}.}
\tag{13}
\]

这里不在 H4 后倒造一条 fresh root：\(P\Rightarrow H4\) 已是 existing persistent
macro，(9)--(11) 只给其最后一个 checkpoint 补足 `path_anchored` E1 provenance。

## 3. 两个容量分派

若

\[
c_5\le p-2,
\tag{14}
\]

则 (7)、(11)、(13) 将原 fifth-anchor parent-macro 的唯一 source 缺口补齐。终端优先
和 H4/H5 typed reclassification 均通过时，其 E1--E5 为：

| 合同 | 回执 |
|---|---|
| E1 | 已有 \(P\Rightarrow H4\) 前缀，加 (9)--(11) 的 primitive same-anchor raw path。 |
| E2 | (6) 的唯一 maximal \(Q_5\)、lcm carrier 及 canonical \(c_5\)。 |
| E3 | H4/H5 的 terminal-first、typed 和 serializer payload 重新核验。 |
| E4 | 全程取 \(W=\operatorname{Sol}(p)\)，故解提升为恒等映射。 |
| E5 | \((0,p-1)>(0,c_5)\)。 |

故 (14) 给出 strict guarded macro。

若 \(c_5=p-1\)，(7)、(11) 已满足 H5 \(d=1\) handoff 所需的 source/path 与
p-free 入门条件，而 (13) 保证其算术 H5 row 没有变化。该 handoff 的非 \(a_5=1\)
分支给出严格 capacity；其唯一 \(a_5=1\) p-free return 已由 actual H3 \(\Rightarrow\)
H4 receipt 的 finite-sieve completion 排除。因此仍存在一个最终 endpoint \(T\) 满足

\[
\Lambda_p^\sharp(P)=(0,p-1)>(0,c_T)=\Lambda_p^\sharp(T),
\qquad c_T\le p-2.
\tag{15}
\]

这一步没有把 fixed-integer sieve 的超集参数误作 source 证明：它只在 (9)--(13) 已将
H4 entry 修复为 actual path-anchored receipt 后，调用对同一 H3--H4 arithmetic receipt
已经完成的 H5 residual 排除。

## 4. H4 残余的收缩

H4 p-adic finite bound 原先把

\[
R_4\equiv0,1\pmod p
\tag{16}
\]

压到有限范围。上面的修复对 (4) 不需要任何 \(p\) 上界，故在本 q=1 high \(C=2\)
19-phase persistent domain 中，真正尚未支付的 H4 算术 gate 只剩

\[
\boxed{R_4\equiv1\pmod p.}
\tag{17}
\]

这不是宣称 (17) 是全局 Erdős--Straus 唯一缺口：它只是本 fifth-anchor macro 内、在
H3 residual phase 和全部既定 guards 已固定后的唯一 source/p-free 残余。

## 5. 范围

本卡不证明 \(R_4\equiv1\pmod p\) 空，也不跳过 H4/H5 terminal-first、typed
reclassification、serializer 或 persistent-parent 的实际存在。它尤其不把 formal raw
source 变成新 root entry，也不替代 G/Type I 全局选择器或 \(n<p\) 的全域递降。

Focused verification:

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_raw_source_repair.py --verify
```

该回执只检查两个满足 H4 局部整数条件的零残数图表：一个直接得到 \(c_5=p-2\)，一个
先到 \(c_5=p-1\) 再由 d=1 正规形直接离开顶容量。它们不是实际 19-phase H3 ancestors，
因此不替代上述条件性证明。
