---
kind: claim
claim_id: type-II-q-one-fresh-handoff-ordinary-closure
title: ordinary q=1 G 到 fresh full-carrier Type I 的相对闭包
statement: >-
  令 S=(p,q=1,G;W_S=Sol(p)) 为 ordinary q=1 Type II G endpoint，p=24t+1，
  X=(p+3)/4。预声明 R_X=16t+3、K_X=X(16t+1)。则 (R_X,K_X) 是低图表范围
  中唯一满足 X|K 的 Type I full-carrier chart；三元组
  (p,R_X(p-1)-p,p-1) 是 target-independent actual fresh p-source，并以 shift 1
  无 gcd reduction 到达 (1,R_X-1,1)。在禁止 Type I nonterminal 返回 q=1 Type II
  phase 的具名 policy 下，S -> T_X 逐项满足 E1--E5，E4 为 Sol(p) 上恒等映射，E5 为
  phase 2 -> 1。root 后令 M=R_X-1；gcd(M,K_X)=1，故完整超额强制首个严格 Type I
  segment：t 奇时直接到 (20t+3,(8t+1)(15t+1);16t+2)，t 偶时经显式 overflow
  determinant 与 fixed-n fold 到 (6t-1,(9t/2)(8t-1);9t/2)。因此 ordinary
  Fresh-G-Handoff 及其首个局部 strict segment 闭合。该结果不含 nontrivial marked
  membership、global well-foundedness、general Type I selector 或 Erdős--Straus 猜想。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-relation-reach-gcd-shadow-endpoint-descent
  - type-II-q-one-type-I-carrier-rail-dispatch
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - G-state
  - type-I
  - fresh-source
  - root-entry
  - identity-lift
  - well-founded-potential
  - proof-boundary
visibility: public
last_checked: '2026-08-17'
---

# ordinary q=1 G 到 fresh full-carrier Type I 的相对闭包

完整证明见本证明包根目录 `PROOF.md`。

核心闭式：

\[
X=\frac{p+3}{4}=6t+1,
\qquad
R_X=16t+3,
\qquad
K_X=X(16t+1).
\]

\[
4K_X=pR_X+1,
\qquad
3\le R_X\le p-2.
\]

唯一性：若 low Type I chart 满足 `X|K`，则

\[
3R\equiv1\pmod{4X},
\]

而 low interval 长度小于 `4X`，故只有 `R_X`。

fresh actual source：

\[
(p,R_X(p-1)-p,p-1)\to(1,R_X-1,1).
\]

普通状态两端均取 `Sol(p)`，故 E4 是 identity；phase `2 -> 1` 支付 E5。

root 后 `M=R_X-1` 且 `(M,K_X)=1`，因此首个 complete-excess bundle 无选择并严格增长 support。

本 claim 的结论是 **T4 ordinary relative closure**，不是 global selector closure。
