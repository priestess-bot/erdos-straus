---
kind: claim
claim_id: type-I-root-capacity-stutter-transverse-pure-t-checkpoint-suffix-crt-boundary
title: 横向 stutter 纯 T 侧 excess 对 checkpoint p-分派的 CRT 独立性
statement: >-
  对 actual L>1 low-gap negative-root pure-T-side complete-excess，若奇素数 q|D*
  还满足 q|E，写 E=1+p sigma、epsilon=v_q(E)>0，则
  q^epsilon 恰整除 1+p sigma。因 q 不等于 p，CRT 表明对每个 a mod p，存在正整数
  sigma 同时满足 sigma≡a mod p 与 v_q(1+p sigma)=epsilon。canonical a=1,d=1 checkpoint
  又有 E1≡sigma mod p，故 q-primary excess 本身与所有四种 p-suffix
  (0、1、-1、其它) 相容，分别对应 p-free failure、p-adic regeneration、raw
  p-source failure 与 strict carry。这个结论不构造完整 actual receipt；它严格表明
  任何从 pure-T q-primary 条件单独推出某一 checkpoint suffix 或严格出口的论证均缺少
  跨模/actual-provenance 输入。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
  - type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
  - type-I-root-capacity-stutter-transverse-pure-t-checkpoint-factorization-boundary
topics:
  - type-I
  - root-capacity
  - stutter
  - transverse-residual
  - negative-branch
  - pure-T-side
  - complete-excess
  - checkpoint-relay
  - CRT
  - p-adic
  - q-adic
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-single-endpoint-stutter-guarded-relay
    role: canonical-checkpoint-p-suffix-dispatch
  - claim: type-I-root-capacity-stutter-transverse-pure-t-complete-excess-relay
    role: actual-pure-T-q-excess-congruence
  - reproduction: reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py
    role: fixed-q-primary-controls-for-all-four-p-suffixes
visibility: public
last_checked: '2026-08-14'
---

# 横向 stutter 纯 \(T\) 侧 excess 对 checkpoint \(p\)-分派的 CRT 独立性

## 1. q-excess 留下的唯一 \(\sigma\) 同余

固定一个 actual \(L>1\) low-gap negative-root pure \(T\)-side complete-excess
情形。沿用

\[
E=1+p\sigma,
\qquad
\epsilon=v_q(E)>0,
\tag{1}
\]

其中 \(q\mid D_*\) 为奇素数。因为 \(q\mid D\mid ph+1\)，有 \(q\ne p\)；否则
\(ph+1\equiv1\pmod p\) 矛盾。由 \(q^\epsilon\parallel E\) 得到精确的 q-primary
约束

\[
\boxed{
p\sigma+1\equiv0\pmod {q^\epsilon},
\qquad
p\sigma+1\not\equiv0\pmod {q^{\epsilon+1}}.}
\tag{2}
\]

第一式等价于 \(\sigma\equiv-p^{-1}\pmod {q^\epsilon}\)；第二式只排除其在
\(q^{\epsilon+1}\) 层的唯一 lift。

## 2. 与 checkpoint 的 \(p\)-suffix 完全独立

由于 \((p,q^{\epsilon+1})=1\)，先取唯一的 \(b\pmod {q^{\epsilon+1}}\) 满足

\[
pb+1\equiv q^\epsilon\pmod {q^{\epsilon+1}}.
\tag{3}
\]

则 \(v_q(1+pb)=\epsilon\)。Chinese remainder theorem 给出满射

\[
\mathbb Z\longrightarrow
\mathbb Z/p\mathbb Z\times\mathbb Z/q^{\epsilon+1}\mathbb Z.
\tag{4}
\]

所以对每个 \(a\in\mathbb Z/p\mathbb Z\)，均存在正整数 \(\sigma\) 同时满足

\[
\boxed{
\sigma\equiv a\pmod p,
\qquad
v_q(1+p\sigma)=\epsilon.}
\tag{5}
\]

正性不增加限制：任取一个 CRT 解后加上足够大的 \(pq^{\epsilon+1}\) 倍数即可。

另一方面，canonical \(a=1,d=1\) checkpoint 的精确 relay 为

\[
B_0=2pr-1,
\qquad B_1=B_0E-\sigma,
\qquad E_1=(p-1)B_1-1,
\qquad E_1\equiv\sigma\pmod p.
\tag{6}
\]

故 pure \(T\)-side 的精确 q-excess 条件 (2) 与 checkpoint 的完整 \(p\)-suffix
四分派独立：

| \(\sigma\pmod p\) | \(E_1\pmod p\) | canonical suffix |
| --- | --- | --- |
| \(0\) | \(0\) | p-free failure |
| \(1\) | \(1\) | finite p-adic regeneration |
| \(-1\) | \(-1\) | raw p-source failure |
| 其它 | 其它 | strict carry |

特别地，\(q\mid E\) 不能单独排除任何一个 bad suffix，也不能单独强制 strict carry。

## 3. 证明边界

本结论不声称 (5) 的所有 CRT 解都能延拓为 actual proper-root stutter receipt。完整
root-height、maximality、\(D\mid ph+1\)、terminal-first 与 path provenance 可能对
\(\sigma\) 施加额外的跨模约束。

它所阻断的是更窄但常见的推理：只从 pure \(T\)-side 的 q-primary normal form、
\(q^\epsilon\parallel E\) 或其 checkpoint 因子继承，推断 \(\sigma\bmod p\) 落入 generic
strict-carry 行。任何有效的后续 adapter 必须明确使用一种不被 (2) 包含的 actual
provenance 条件，才能选择或排除上表中的 suffix。

这条所缺的 actual cross-mod 输入现可由
\(\sigma D=2T-(m+2r)\) 明确给出；详见
[横向 stutter 纯 \(T\) 侧的跨模 multiplier-quotient 赋值阶梯](type-I-root-capacity-stutter-transverse-pure-t-cross-mod-valuation-staircase.md)。

## 4. 聚焦复现

~~~bash
python3 reproductions/type_i_root_capacity_stutter_transverse_pure_t_complete_excess_relay.py --verify
~~~

脚本固定 \((p,q,s,L,h,m,r,D)=(313,17,3,5,12,4,15,17)\)，并以四个
\(v_{17}(E)=1\) 的 \(\sigma\) CRT 代表分别重放四种 \(p\)-suffix；另保留一个
\(v_{17}(E)=2\) 控制检查高 excess。它们保留相同的 pure \(T\) q-primary normal
form、精确 complete-excess 赋值、receipt-quotient bridge 和 checkpoint factorization，
但明确不冒充完整 actual root receipt，也不扫描范围。
