---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-complete-excess-stutter-reduction
title: q=1 高 C=2 19 相位 H4 a=1 q-bridge 的完整超额分解与单一 stutter 门
statement: >-
  在 actual H4 proper-overlap top-capacity a_alt=1 的 clean q bridge 中，原 bundle 写为
  z=Q delta，令 L0=lcm(M4,Q)/M4，并令 endpoint 为
  (x_q,y_q)=(R4-z/q,z/q)。则 y_q 的 maximal complete-excess block 精确为 Q_y=Q/q。
  对每个非 terminal endpoint，令 E_x=Q_x/gcd(M4,Q_x)，其中 Q_x 是 x_q 的 maximal
  block（Q_x=1 时 E_x=1）。若 M_q 是 endpoint 选用单侧或双色 payload 的 canonical
  support，则 L_q=M_q/M4=(L0/q)E_x；原 H4 top-capacity congruence 给
  c_q=-q*E_x^(-1) (mod p)。因此 Q_x=1 的非 terminal 单侧分支恒有
  c_q=p-q<=p-2；所有 arithmetic capacity stutter 精确收缩为 Q_x>1 且
  E_x=q (mod p)。Q_y=1 时这是既有单侧 payload 的唯一 stutter gate，Q_y>1 时这是
  atomic split payload 的唯一 stutter gate。该结果不证明此同余类为空，也不把 atomic
  schema 的条件性 E1--E4 自动登记为 verified edge。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - a-one
  - fresh-carrier
  - raw-path
  - complete-excess-bundle
  - atomic-split
  - carry-stutter
  - source-provenance
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: actual-clean-q-word-and-original-top-capacity
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-p-primary-endpoint-exclusion
    role: endpoint-p-free-domain
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: q-divides-original-multiplier
  - claim: type-I-path-anchored-atomic-split-complete-excess-admission
    role: colored-payload-and-high-support-capacity-contract
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: one-sided-residual-divisibility-gate
  - concept: denominator-escape-state-contract
    role: terminal-typed-lift-and-potential-contract
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge.py
    role: exact-q-block-factorization-and-stutter-gate-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 \(q\)-bridge 的完整超额分解与单一 stutter 门

## 1. 设置

沿用 actual H4 proper-overlap top-capacity \(a_{\rm alt}=1\) 的 clean \(q\) bridge。
写

\[
z=Q\delta,\qquad Q=Q_{K_4}(z),\qquad
(Q,\delta)=1,\qquad \delta\mid K_4,
\tag{1}
\]

\[
q\mid Q,\qquad (q,K_4)=(q,M_4)=1,
\qquad L_0=\frac{\operatorname{lcm}(M_4,Q)}{M_4}.
\tag{2}
\]

原 H4 renewal 正处于 top capacity，故

\[
c_4L_0^{-1}\equiv-1\pmod p.
\tag{3}
\]

q-word 的 actual primitive endpoint 是

\[
y_q=\frac zq,\qquad x_q=R_4-y_q.
\tag{4}
\]

此前的 endpoint exclusion 已给 \(p\nmid x_qy_q\)。令

\[
x_q=Q_x\beta_x,\qquad y_q=Q_y\beta_y
\tag{5}
\]

是相对 \(K_4\) 的 maximal complete-excess 分解。

## 2. 被剥掉的 q 恰从 y-block 中除去

### 引理 1

\[
\boxed{Q_y=\frac Qq,\qquad \beta_y=\delta.}
\tag{6}
\]

**证明。** 对任意素数 \(\ell\)，记 \(e=v_\ell(Q)\)、\(a=v_\ell(q)\)、
\(k=v_\ell(K_4)\)。若 \(a=0\)，\(y_q\) 的 \(\ell\)-指数不变：\(Q\) 中的完整
超额幂仍完整超额，\(\delta\) 中的幂仍不超额。若 \(a>0\)，clean-q lemma 给 \(k=0\)，
而 \(y_q\) 的指数变为 \(e-a\)。它大于零时完整进入 \(Q_y\)，等于零时不出现，二者
都正是 \(Q/q\) 的 \(\ell\)-指数。逐素数合并即得第一式；第二式随
\(y_q=(Q/q)\delta\) 与互素性得到。\(\square\)

特别地，(6) 不是样本中的经验观察，也不需要对 endpoint 再作因子猜测。

## 3. endpoint multiplier 的精确分解

由 \((q,M_4)=1\)，从 \(Q\) 中除去 \(q\) 不改变与 \(M_4\) 的 gcd：

\[
(M_4,Q)=(M_4,Q/q).
\tag{7}
\]

因此 y-side 的新增倍率为

\[
E_y:=\frac{Q_y}{(M_4,Q_y)}=\frac{L_0}{q}.
\tag{8}
\]

定义 x-side 的 canonical新增倍率

\[
E_x:=\frac{Q_x}{(M_4,Q_x)},
\tag{9}
\]

并约定 \(Q_x=1\) 时 \(E_x=1\)。endpoint primitive 性使 \((Q_x,Q_y)=1\)，故无论
\(Q_y=1\) 时使用单侧 payload，还是 \(Q_x,Q_y>1\) 时使用双色 payload，非 terminal
target 的 support multiplier 都是

\[
\boxed{
L_q=\frac{\operatorname{lcm}(M_4,Q_x,Q_y)}{M_4}
=E_xE_y=\frac{L_0}{q}E_x.
}
\tag{10}
\]

若 \(Q_x=1,Q_y>1\)，右式仍成立，且就是 y-side 单侧 support；若 \(Q_y=1,Q_x>1\)，
则 (6) 给 \(Q=q\)，右式仍是 x-side 单侧 support。两块皆空是 Type I terminal，
不适用 (10)。

## 4. 容量门只剩 \(E_x\equiv q\)

endpoint p-free，故 (10) 的 canonical capacity 存在。由 (3) 及 (10)，

\[
\boxed{
c_q\equiv c_4L_q^{-1}
\equiv-qE_x^{-1}\pmod p.
}
\tag{11}

\]

于是

\[
\boxed{
c_q=p-1
\quad\Longleftrightarrow\quad
E_x\equiv q\pmod p.
}
\tag{12}
\]

如果 \(Q_x=1\) 而端点非 terminal，则 \(E_x=1\)，所以

\[
\boxed{c_q=p-q\le p-2.}
\tag{13}
\]

这条 single-side payload 的 residual gate 自动通过：\(Q_x=1\) 给 \(x_q\mid K_4\)，
而 \(\beta_y=\delta\mid K_4\)，故 \(x_q\delta\mid K_4\)。因此它在 terminal-first、
typed 与 serializer guards 通过时可直接附回 persistent parent，支付
\((0,p-1)>(0,p-q)\)。

若 \(Q_x>1\)，则 \(E_x>1\)。此时：

| y-block | payload | strict 门 | 唯一 capacity stutter |
|---|---|---|---|
| \(Q_y=1\) | 既有 x-side 单侧 payload | \(E_x\not\equiv q\pmod p\) | \(E_x\equiv q\pmod p\) |
| \(Q_y>1\) | 条件性 atomic split payload | \(E_x\not\equiv q\pmod p\) | \(E_x\equiv q\pmod p\) |

第二行仍需要 atomic source/target validator 与 owner 语义；(12) 只给 E5 的精确算术门，
不把它提升为 verified edge。

## 5. 两个固定回执

| \(p\) | \(q\) | \(Q\) | \(Q_y=Q/q\) | \(E_x\) | \(L_0\) | \(L_q\) | \(c_q\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 73 | 37 | 245717 | 6641 | 119539 | 245717 | 793858499 | 24 |
| 241 | 121 | 7202525 | 59525 | 3571501 | 7202525 | 212593597025 | 80 |

两行都直接核验 (6)、(10) 与 (11)，并且 \(E_x\not\equiv q\pmod p\)，所以是严格
atomic controls；它们不构造或排除 (12) 的 stutter residue。

## 6. 范围

本卡将 clean q bridge 的非 terminal 算术余项从一个没有分解的 \(L_q\equiv-c_4\pmod p\)
条件，压成一侧完整超额倍率的单一同余

\[
\boxed{Q_x>1,\qquad E_x\equiv q\pmod p.}
\tag{14}
\]

后继的[首层容量 stutter 全域 source \(D\)-gate 关闭](type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure.md)
现已在整个 actual 19-phase H4 scope 中排除 (14)。因此每个 actual nonterminal
endpoint 的算术容量都严格满足 \(c_q\le p-2\)。本卡仍不处理 terminal-first 抢占、
typed reclassification 或 atomic adapter 的持久化实现；这些语义门不能由容量严格性替代。

## 7. 定向回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_carrier_clean_raw_bridge.py --verify
```

回执只重放两个固定 local H4 arithmetic controls，不扫描 prime ranges、分母或历史 Reach。
