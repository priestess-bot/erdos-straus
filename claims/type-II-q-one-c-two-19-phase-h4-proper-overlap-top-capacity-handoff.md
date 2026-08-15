---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
title: q=1 高 C=2 19 相位 H4 proper-overlap 顶容量的 d=1 handoff
statement: >-
  在 q=1 high C=2 19-phase 的 actual persistent H4 receipt 中，设 R4=1 (mod p)，
  真实 p-primary peeling 与容量剥离到达 proper-overlap h<p+1，并以 p-free clean
  bundle Q 产生 M_alt=lcm(M4,Q) 和 c_alt=p-1。则 M_alt=(p n_alt-1)/4、
  R_alt=(p-1)n_alt-1，其中 n_alt>1、n_alt=1 (mod 4)，故是合法 full-product d=1
  state。写 (p+1)/2=g a_alt、(n_alt+1)/2=g b_alt、(a_alt,b_alt)=1。若 a_alt>1，
  则 d=1 regeneration countdown、raw-source repair 与 p-free small-anchor handoff
  在有限步后产生 residual capacity <=p-2；在所有 checkpoint 的 terminal-first、typed、
  source/path 与 serializer guards 通过时，它与现有 P=>H4 prefix 合成为从
  Lambda(P)=(0,p-1) 到 (0,c_T) 的 strict guarded macro，并以 Sol(p) identity lift
  提升全域解。唯一未被该组合清除的顶容量类是 a_alt=1（等价于 (p+1)/2|M_alt）的
  d=1 return；它不由原 H4 full-overlap 排除，也不在本卡中声称已获出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
  - type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion
  - type-II-q-one-c-two-19-phase-three-anchor-persistent-macro
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
  - type-I-chart-least-coprime-prime-anchor-source
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - proper-overlap
  - top-capacity
  - full-product
  - d-one
  - p-adic-regeneration
  - small-anchor
  - guarded-macro
  - solution-lift
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-h4-p-primary-small-anchor-renewal
    role: actual-proper-overlap-renewal-and-top-normal-form
  - claim: type-II-q-one-c-two-19-phase-h4-full-overlap-predecessor-exclusion
    role: actual-phase-p-free-proper-overlap-domain
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: full-product-d-one-countdown-and-strict-rank
  - claim: type-I-overflow-full-product-d-one-p-free-peeled-small-anchor
    role: a-greater-than-one-terminal-p-free-exit
  - claim: type-I-chart-least-coprime-prime-anchor-source
    role: raw-source-failure-repair
  - concept: denominator-escape-state-contract
    role: guarded-E1-to-E5-composition
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_proper_overlap_top_capacity_handoff.py
    role: d-one-normal-form-and-a-split-controls
visibility: public
last_checked: '2026-08-16'
---

# H4 proper-overlap 顶容量的 d=1 handoff

## 1. actual p-free renewal 的顶端是已有正规形

设 actual H4 p-primary receipt 已满足 \(R_4\equiv1\pmod p\)。经过真实 \(p\)-block
peeling 和同侧容量剥离，它到达 proper overlap

\[
h=(R_4-1,K_4)<p+1,
\qquad z=R_4-h,
\tag{1}
\]

并产生 path-anchored p-free complete-excess bundle \(Q\)。H4 full-overlap 实际前驱排除
保证 (1) 在本 19-phase receipt 域中总成立。写

\[
M_{\rm alt}=\operatorname{lcm}(M_4,Q),
\qquad
c_{\rm alt}\equiv c_4(M_{\rm alt}/M_4)^{-1}\pmod p.
\tag{2}
\]

现在只讨论顶容量分支 \(c_{\rm alt}=p-1\)。因为 \(M_{\rm alt}>M_4>B_p\) 且
\(4M_{\rm alt}\equiv-1\pmod p\)，定义

\[
n_{\rm alt}=\frac{4M_{\rm alt}+1}{p}.
\tag{3}
\]

则

\[
\boxed{
n_{\rm alt}>1,\qquad n_{\rm alt}\equiv1\pmod4,
\qquad M_{\rm alt}=\frac{pn_{\rm alt}-1}{4},
\qquad R_{\rm alt}=(p-1)n_{\rm alt}-1.
}
\tag{4}
\]

故它不是新的 H4 特有图表，而是完整乘积 \(d=1\) 饱和行。proper-overlap 的 p-free
性质还给出 \(p\nmid M_{\rm alt}\)，所以 (4) 可进入既有的 d=1 state contract。

## 2. 顶容量按 a-coordinate 精确分派

写

\[
\alpha=\frac{p+1}{2}=g a_{\rm alt},
\qquad
v=\frac{n_{\rm alt}+1}{2}=g b_{\rm alt},
\qquad
(a_{\rm alt},b_{\rm alt})=1.
\tag{5}
\]

完整乘积正规形给出

\[
a_{\rm alt}=1
\quad\Longleftrightarrow\quad
\frac{p+1}{2}\mid M_{\rm alt}.
\tag{6}
\]

若 \(a_{\rm alt}>1\)，既有 d=1 handoff 的两个全称算术结论可逐项适用：

1. 若 canonical multiplier 不是 regeneration residue，目标容量立即为 \(\le p-2\)；
2. 若它是 regeneration residue，\(\eta=\nu_p(E-1)\) 每步恰减一，故有限步后离开
   regeneration；
3. 终行的 raw-source failure 由最小互素素数 source 同锚修复；终行的 p-free failure
   由真实 p-primary peeling--small-anchor route 产生 p-free bundle，且 \(a_{\rm alt}>1\)
   全称排除新的 top-capacity stutter。

于是存在一个有限 suffix 的终点 \(T\)，满足

\[
\boxed{c_T\le p-2.}
\tag{7}
\]

这一步不是把 generic theorem 静态贴到 H4 图表：其起点 (4) 已由 (1)--(3) 给出实际
path-anchored receipt，且每个 d=1 checkpoint 必须重新运行 terminal-first、typed
reclassification、source/path 与 serializer guards。

## 3. 与 persistent parent 的严格宏复合

令 \(P\) 是已有 q=1 high \(C=2\) persistent parent。其端点势为

\[
\Lambda_p^\sharp(P)=(0,p-1).
\tag{8}
\]

在 H4 renewal、(4) 以及通向 \(T\) 的每个 d=1 suffix checkpoint 都通过 guards 时，
宏的合同为：

| 合同 | 回执 |
|---|---|
| E1 | 既有 \(P\Rightarrow H4\) prefix；H4 p-peeling/capacity raw word；以及 d=1 suffix 的实际 source/path。 |
| E2 | (2)--(5) 的 lcm、canonical capacity 和 full-product normal form；每步 regeneration 或 small-anchor target 的重算。 |
| E3 | 每个 checkpoint 的 terminal-first、typed reclassification、state id、scope 和 serializer payload。 |
| E4 | 所有状态都是同一 \(4/p\) equation target，故 \(\operatorname{Sol}(p)\) 的 identity map 给出全域解提升。 |
| E5 | 由 (7)--(8)，\((0,p-1)>(0,c_T)\)。 |

所以 \(a_{\rm alt}>1\) 是一个真正的 strict guarded macro，而非单独顶容量 state 的
rank stutter。

## 4. 唯一保留的接口

若 \(a_{\rm alt}=1\)，则由 (6) \(w=(p+1)/2\mid M_{\rm alt}\)。这不蕴含
\(w\mid K_4\)：一般 H4 local chart 已有 proper-overlap、\(c_{\rm alt}=p-1\)、
\(a_{\rm alt}=1\) 的正控制。因此不能把刚排除的原 H4 full-overlap 偷换为此处的
full-product return。

本卡的推进是把 actual H4 p-primary top-capacity 分支从完整的 d=1 续接，收缩为唯一的
\(a_{\rm alt}=1\) return interface。它没有证明该 interface 不可达、必有短证书或必可
递降，因而仍不是 G/Type I 全局出口定理。

## 5. 定向回执

```bash
python3 reproductions/type_ii_q_one_c2_19_phase_h4_proper_overlap_top_capacity_handoff.py --verify
```

回执核对一个 \(a>1\) 的直接严格 d=1 行、一个 \(a>1\) 的 p-free small-anchor
handoff，以及 proper-overlap \(a_{\rm alt}=1\) 的一般 H4 正控制。它们不被声称为
actual 19-phase predecessors，也不扫描素数或分母。
