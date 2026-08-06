---
kind: claim
claim_id: type-I-fixed-high-anchor-return-one-shot-exhaustion
title: 固定高锚点回返的 complete-excess 单次耗尽
statement: 设固定高锚点满足 \(4K=pR+1\)，并由 \(M=\operatorname{lcm}(A,Q)=kp+r\) 的 complete-excess 路径产生 canonical overflow \(K_M=MC\)。若第一次 cofactor r-chart 是合法的严格支撑升级，且其 target \((p,R,K;A_1)\)、\(A_1=\operatorname{lcm}(A,C)\) 回返同一高锚点，则第二次使用同一 \(Q\) 的 carrier 为 \(M_1=\operatorname{lcm}(A_1,Q)=\operatorname{lcm}(M,C)\)，并满足 \(M_1\mid K_M\)、canonical_chart(p,M_1)=(R_M,K_M)、\(C_1=K_M/M_1=(M,C)\mid A_1\)。因此第二次 cofactor support \(\operatorname{lcm}(A_1,C_1)=A_1\)，不可能再支付严格支撑势下降；第二 gate 若不通过则路径更早停止。故固定高锚点的同 bundle 回返至多提供一次严格 cofactor 支撑升级，不是可迭代的全局递降机制。p=1201 的该第二轮失败，同时其形式低图表给出直接 Type I 终端。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-r-chart-support
  - type-I-overflow-same-chart-support-promotion
  - type-I-bounded-monotone-support-phase-rank
  - denominator-escape-state-contract
topics:
- type-I
- high-carrier
- complete-excess
- cofactor
- r-chart
- terminal
- well-founded-descent
- proof-boundary
sources:
  - reproduction: reproductions/type_i_high_r_chart_two_anchor.py
    role: one-shot exhaustion and direct terminal verifier
  - result: reproductions/type-i-high-r-chart-two-anchor-results.json
    role: p-1201 two-round and terminal receipt
visibility: public
last_checked: '2026-08-06'
---

# 固定高锚点回返的 complete-excess 单次耗尽

## 1. r 图表的余数分解

设一个 canonical overflow 满足

\[
4K_M=pR_M+1,\qquad K_M=MC,\qquad
M=kp+r,\qquad 1\le r<p,
\tag{1}
\]

并写 \(d=p-C\)。令

\[
s=\frac{4rd+1}{p},\qquad
R_r=4r-s,\qquad K_r=rC.
\tag{2}
\]

则

\[
4rC\equiv1\pmod p,\qquad
(R_r,K_r)=\operatorname{canonical\_chart}(p,r),
\tag{3}
\]

且有精确分解

\[
R_M=R_r+4kC,\qquad
K_M=K_r+kpC,\qquad
4M-R_M=s+4kd.
\tag{4}
\]

因此 r-chart target 只取决于 \(r=M\bmod p\)，不取决于高载体商 \(k\)。

令

\[
g=(A,C),\qquad a=A/g,\qquad A_1=\operatorname{lcm}(A,C)=Ca.
\tag{5}
\]

则

\[
A_1\mid K_r
\quad\Longleftrightarrow\quad
a\mid r.
\tag{6}
\]

在 (6) 成立时 \(K_r=A_1(r/a)\) 且 \(r/a<p\)，所以
\(\operatorname{canonical\_chart}(p,A_1)=(R_r,K_r)\)。严格支撑增长恰等价于
\(C\nmid A\)。

## 2. 单次耗尽引理

现设固定高锚点

\[
4K=pR+1,\qquad R>p,
\tag{7}
\]

当前 charged support 为 \(A\mid K\)。一个 complete-excess bundle \(Q\) 先给出

\[
M=\operatorname{lcm}(A,Q),\qquad K_M=MC.
\tag{8}
\]

假设第一次 cofactor 目标满足 (6)、严格 \(A<A_1\)，并回返到该固定锚点：

\[
\operatorname{canonical\_chart}(p,A_1)=(R,K),
\qquad A_1=\operatorname{lcm}(A,C).
\tag{9}
\]

再次从同一锚点使用 \(Q\)，新 carrier 为

\[
M_1=\operatorname{lcm}(A_1,Q)
=\operatorname{lcm}(\operatorname{lcm}(A,C),Q)
=\operatorname{lcm}(M,C).
\tag{10}
\]

故 \(M_1\mid MC=K_M\)。又 \(R_M<4M\le4M_1\)，且
\(pR_M+1=4K_M\)，所以 canonical 唯一性给出

\[
\operatorname{canonical\_chart}(p,M_1)=(R_M,K_M).
\tag{11}
\]

第二次的 cofactor 因而是

\[
C_1=\frac{K_M}{M_1}
=\frac{MC}{\operatorname{lcm}(M,C)}
=(M,C).
\tag{12}
\]

它满足

\[
C_1\mid C\mid A_1,
\qquad
\operatorname{lcm}(A_1,C_1)=A_1.
\tag{13}
\]

所以第二次 cofactor 支撑绝不严格增长。若第二次的 \(A_1/(A_1,C_1)\mid
M_1\bmod p\) gate 通过，也只能得到零支撑进展；若 gate 失败，则该路线直接停止。
这证明固定锚点、同一 bundle 的回返不是无限递降机制。

该引理不要求 \(Q\) 与 \(K\) 互素。若额外 \(Q\perp K\)，则

\[
M_1=\frac{C}{(A,C)}M,\qquad C_1=(A,C),
\tag{14}
\]

是 (10)--(12) 的简化式。

## 3. \(p=1201\) 的耗尽与支撑墙

第一次高 \(R\) 路径数据为

\[
(p,R,K;A)=(1201,1839,552160;986),\qquad Q=919,
\]
\[
M=906134,\qquad K_M=862639568=M\cdot952,
\]
\[
r=580,\qquad A_1=\operatorname{lcm}(986,952)=27608.
\tag{15}
\]

第一次 target 的确回返 \((1839,552160)\)。由 (10)--(12)，第二轮为

\[
M_1=25371752,\qquad
(R_M,K_M)=(2873071,862639568),\qquad C_1=34,
\tag{16}
\]

\[
M_1=21125\cdot1201+627,\qquad
\frac{27608}{(27608,34)}=812\nmid627,
\tag{17}
\]

并且

\[
\operatorname{lcm}(27608,34)=27608.
\tag{18}
\]

所以第二 gate 失败，且即使忽略它也没有严格势下降。形式 r-chart 是

\[
(R_r,K_r)=(71,21318).
\tag{19}
\]

任何合法 canonical target support 都必须整除 \(21318\)，故必有

\[
A'\le21318<27608,\qquad
\left\lfloor\frac{360000}{A'}\right\rfloor\ge16>13.
\tag{20}
\]

这是一面实际的 charged-support 墙：把 (19) 作为后继必须遗忘已收费支撑，不能冒充
non-resetting 递归边。

## 4. 形式低图表的直接 Type I 终端

尽管 (19) 不是合法 charged 后继，它提供一个全局有效的 Type I 证书。取

\[
(m,A,B,C,H,K)=(1043,1,33,17,38,21318).
\tag{21}
\]

直接核验

\[
1201=4ABC-m,\qquad
1043\cdot71=4B^2C+1,\qquad
H=\frac{B p+A}{m}=38,\qquad K=BCH.
\tag{22}
\]

等价地，\(x=ABC=561\) 的目标平方除子为

\[
e=B^2C=18513\mid x^2,\qquad
e\equiv-\frac14\pmod {71}.
\tag{23}
\]

故正规形给出

\[
\boxed{
\frac4{1201}
=\frac1{ABC}+\frac1{ACH}+\frac1{pK}
=\frac1{561}+\frac1{646}+\frac1{25602918}.}
\tag{24}
\]

这张证书终止 \(p=1201\) 本身；它不把形式低图表伪造成带 \(A=27608\) 的递归状态。

## 5. 边界

单次耗尽只排除“固定高锚点 + 同一 complete-excess bundle + 回返”的重复使用。它不排除
不同锚点、不同 bundle、fixed-\(n\)、fixed-\(s\)、Type II 或其它已验证外层秩。
反之，若忘记 (9) 中的首次严格增长，甚至第一次也可能没有进展；例如纯算术数据

\[
p=73,\quad R=135,\quad K=2464,\quad Q=67,\quad A=88
\]

有 \(M=5896\)、\(C=44\)、\(\operatorname{lcm}(A,C)=A\)。这不是可达性反例，
只说明严格支撑增长必须作为独立门核验。
