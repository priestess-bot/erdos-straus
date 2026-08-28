---
kind: claim
claim_id: t6-sp05-complete-terminal-decision-boundary
title: SP-05 完整 terminal 判定与现实非终止边的反例边界
statement: >-
  对每个固定正整数 p，按排序首分母 x 的有限区间和约分 residual a/b 的完整
  因子对恒等式 (ay-b)(az-b)=b^2 构成的确定算法，返回 HIT 当且仅当
  4/p 存在正整数三分母解，返回 MISS_COMPLETE 当且仅当该解集为空。因而对于
  complete-terminal-first 的 ordinary q=1,G phase-root 分支，任何现实 nonterminal
  verified edge 都蕴含一个 Erdős--Straus 反例；在额外给定 exact-HEAD actual source、
  complete-MISS、E1--E5、admission 和 re-entry authority 时，canonical phase-root
  target 是唯一的。该 claim 不断言存在 such complete-MISS source，也不授予 production
  registry、queue、F1/F2/F3/T6 或猜想闭合权限。
claim_status: established
proof_provenance: mixed
review_status: internal_review
topics:
  - T6
  - SP-05
  - complete-terminal-decision
  - factor-pairs
  - terminal-first
  - q-one
  - proof-boundary
  - Erdos-Straus
sources:
  - document: reproductions/sp05_complete_terminal_decision/SP-05-complete-proof.md
    role: self-contained proof of finite coverage and conditional branch theorem
  - reproduction: reproductions/sp05_complete_terminal_decision/sp05_constructor.py
    role: constructive complete factor-pair scheduler
  - reproduction: reproductions/sp05_complete_terminal_decision/sp05_independent_replayer.py
    role: independent replay without constructor imports
  - data: reproductions/sp05_complete_terminal_decision/evidence/status-boundary.json
    role: machine-readable established and unissued boundary
  - test: tests/test_t6_sp05_complete_terminal_package.py
    role: package replay and counterexample-boundary controls
visibility: public
last_checked: '2026-08-29'
---

# SP-05 Complete Terminal Boundary

## Finite Decision

For a fixed \(p\), sort any prospective solution as \(x\le y\le z\). Then

\[
\left\lfloor\frac p4\right\rfloor+1
\le x\le
\left\lfloor\frac{3p}{4}\right\rfloor.
\]

For each \(x\), reduce

\[
\frac4p-\frac1x=\frac ab,
\qquad (a,b)=1.
\]

The equation \(a/b=1/y+1/z\) is equivalent to

\[
(ay-b)(az-b)=b^2.
\]

Every sorted solution therefore corresponds to exactly one positive factor pair

\[
d e=b^2,\qquad d\le e,
\qquad a\mid b+d,\qquad a\mid b+e,
\]

with \(y=(b+d)/a\), \(z=(b+e)/a\), and conversely. Both the \(x\)-range and
each factor-pair set are finite. Thus the schedule terminates and its exact
outcome is

\[
\operatorname{CompleteSchedule}(p)=\mathsf{HIT}
\Longleftrightarrow
\mathsf{Sol}(4,p)\ne\varnothing.
\]

## SP-05 Consequence

The source and target use the same equation \(4/p\). A complete terminal-first
phase-root branch may construct its canonical Type-I target only after source
and target `MISS_COMPLETE` results. Hence a concrete actual nonterminal branch
implies \(\mathsf{Sol}(4,p)=\varnothing\), an Erdős--Straus counterexample.

The canonical arithmetic remains valid under that conditional premise:

\[
R=16t+3,\qquad K=(6t+1)(16t+1),\qquad 4K=pR+1,
\]

with the frozen T5 vectors

\[
\Pi(S)=(p,3,0,0,0,0,0),\qquad
\Pi(T)=\left(p,2,4,\frac{(p-1)^2}{4},K,0,0\right).
\]

This is a `PHASE_DROP`. The claim remains a boundary theorem: no counterexample
or production authority is supplied, so it does not create a concrete SP-05
verified successor.
