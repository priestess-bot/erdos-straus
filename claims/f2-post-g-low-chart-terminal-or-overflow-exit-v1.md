---
kind: claim
claim_id: f2-post-g-low-chart-terminal-or-overflow-exit-v1
title: post-G 低 Type-I chart 的有限 support-doubling 终端或 overflow 出口
statement: >-
  对任意 actual、terminal-first-surviving ordinary post-G Type-I state
  S=(p,R,K;A) with 3<=R<=p-2, A|K and mark Sol(p)，反复执行确定规则：从
  universal p-source 到 anchor (1,R-1,1)；若 R-1|K 则输出直接 Type-I terminal；
  否则取 R-1 相对 K 的唯一 maximal complete-excess block Q，令 M=lcm(A,Q)，
  并构造 M 的 canonical chart。每个非终止步骤满足 M>A 且 M/A>=2，数学上给出
  actual source/path、确定 target、Sol(p) identity lift 与 T5 LOCAL_DROP；只有
  target projection 经共享 E3 admission 后才成为完整 E1-E5 edge。若 target 仍是低
  chart，则 M<=B_p 且继续同一规则；
  support 每步至少翻倍，所以至多 floor(log_2(B_p/A))+1 步后必终止或进入
  R>p 的 A=M>1 overflow target。该结果把 post-G 低 chart 的 later-dispatch
  全称量词闭合为 direct terminal 或对既有 type_i_a_gt_one_overflow_residual family
  的确定 handoff；overflow 后的 totality 和共享 PersistentSelector admission 仍属
  其它 track/coordinator，故 F2 与 T6 保持 OPEN。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - type-I-factorization-free-centered-hit-terminal-serializer
  - denominator-escape-state-contract
topics:
  - F2
  - post-G
  - Type-I
  - universal-source
  - complete-excess
  - support-doubling
  - terminal
  - overflow
  - well-foundedness
  - proof-boundary
sources:
  - data: data/t6-wave1/f2-post-g-low-chart-exit-v1.json
    role: machine-readable-quantifier-and-handoff
  - reproduction: reproductions/f2_post_g_low_chart_exit.py
    role: focused-deterministic-orbit-replay
visibility: public
last_checked: '2026-08-24'
---

# post-G 低 chart 的有限 terminal-or-overflow 出口

## 1. 输入域

固定 actual persistent state

\[
S_0=(p,R_0,K_0;A_0,\sigma),
\qquad
4K_0=pR_0+1,
\qquad
3\le R_0\le p-2,
\qquad
A_0\mid K_0,
\tag{1}
\]

其中 (p\equiv1\pmod {24}) 为素数，mark 为图表无关的
(W_{S_0}=\operatorname{Sol}(p))，且完整 terminal-first prefix 已 miss。本定理适用于
full-carrier root、首 child、second-anchor 的 marked-absorb output，以及其后任何仍落在
低 chart 的 ordinary post-G descendant；它不要求这些 state 继承 source 的 F/G 标签。

由 (R_i\le p-2) 有

\[
K_i=\frac{pR_i+1}{4}\le\frac{(p-1)^2}{4}=:B_p,
\qquad
A_i\le K_i\le B_p.
\tag{2}
\]

## 2. 单步确定分派

对当前低 state (S_i=(p,R_i,K_i;A_i,\sigma))，取 universal p-source

\[
(p,R_i(p-1)-p,p-1)\xrightarrow{p}(1,R_i-1,1).
\tag{3}
\]

式 (3) 总是实际 primitive path：(p\nmid R_iK_i)。随后只有两类。

### 2.1 Terminal

若 (R_i-1\mid K_i)，则

\[
1\cdot(R_i-1)\mid K_i
\tag{4}
\]

给出 centered full-excess Type-I terminal。该 branch 不创建 target。

### 2.2 Canonical complete-excess target

若 (R_i-1\nmid K_i)，唯一写

\[
R_i-1=Q_i\beta_i,
\qquad
Q_i=Q_{K_i}(R_i-1)>1,
\qquad
\beta_i\mid K_i,
\qquad
(Q_i,\beta_i)=1.
\tag{5}
\]

令

\[
A_{i+1}=M_i=\operatorname{lcm}(A_i,Q_i).
\tag{6}
\]

因为 (A_i\mid K_i)，而 (Q_i) 至少含一个在 (R_i-1) 中指数严格超过 (K_i) 的
完整素数幂，所以

\[
M_i>A_i,
\qquad
\frac{M_i}{A_i}\ge2.
\tag{7}
\]

取唯一 canonical representative

\[
1\le R_{i+1}<4M_i,
\qquad
pR_{i+1}\equiv-1\pmod {4M_i},
\qquad
K_{i+1}=\frac{pR_{i+1}+1}{4}.
\tag{8}
\]

有 (R_{i+1}\equiv3\pmod4)、(M_i\mid K_{i+1})。由于
(p\equiv1\pmod4)，(R_{i+1}=p) 不可能。因此 target 唯一分成

\[
3\le R_{i+1}\le p-2
\quad\text{或}\quad
R_{i+1}>p.
\tag{9}
\]

第一类仍是 low marked state；第二类是 overflow target。

## 3. 每一步的数学合同与 E3 边界

| 合同 | 回执 |
|---|---|
| E1 | persistent (S_i)、terminal-first miss、(3) 的 actual p-source/path 与 (5) 的唯一 maximal block。 |
| E2 | (6)--(8) 唯一确定 target；无需 oracle 或事后选择 carrier。 |
| E3 | 数学 target shape 由 ((p,R_{i+1},K_{i+1},M_i,\sigma)) 唯一确定；F/G/hit、normal form 与 state identity 必须由 coordinator 的 common serializer 重算并 admission，本卡不宣称该 runtime 已接入。 |
| E4 | (W_{S_i}=W_{S_{i+1}}=\operatorname{Sol}(p))，lift 是 identity。 |
| E5 | source 为 low state，故 (A_i\le B_p)；由 (7)，
  \(\lfloor B_p/M_i\rfloor<\lfloor B_p/A_i\rfloor\)。 |

所以每个 nonterminal step 都有 `TYPEI/CHARGED LOCAL_DROP` 的数学 ticket；它只有在 common
E3 admission 成功后才是 active verified edge。若 target-local classifier
给 hit，则 terminal 优先并停止；否则 target 才有递归资格。

## 4. 有限性

只要 target 仍低，(2) 对 (A_{i+1}=M_i) 继续成立。由 (7) 归纳得到

\[
A_j\ge2^jA_0.
\tag{10}
\]

因此不可能连续有超过

\[
N=\left\lfloor\log_2\frac{B_p}{A_0}\right\rfloor+1
\tag{11}
\]

个 nonterminal low targets；否则 (A_N>B_p)，与低 chart 的 (A_N\le K_N\le B_p)
矛盾。故确定过程有限终止于：

1. direct/centered Type-I terminal；或
2. 一个 (R>p)、support (A=M>1) 的 overflow target。

这是 well-founded induction，不是有限素数扫描。

## 5. 对 post-G 缺口的含义

q=1 full-carrier handoff 的 root 与每个 marked-absorb descendant都满足 (1)，所以本定理
消除了“低 post-G tree 可能无限 later dispatch”的开放量词。若 overflow target 的 facts
不命中更专门 owner，它至少命中现有
`type_i_a_gt_one_overflow_residual`。因此 shared grammar 所需的 handoff 是

```text
POST_G_LOW_CHART
  -> TERMINAL
   | TYPE_I_A_GT_ONE_OVERFLOW_RESIDUAL
```

而不是一个新 family。Agent 2 仍须证明该 overflow family 的 terminal-or-successor totality；
coordinator 仍须把每步 serializer 接到 common gate。完成这两个外部依赖前，准确状态是：

```text
POST_G_LOW_CHART_TOTAL_EXIT = ESTABLISHED_RELATIVE_TO_COMMON_ADMISSION
POST_G_OVERFLOW_CONTINUATION = EXTERNAL_OPEN_DEPENDENCY
GAP_O1_POST_G_TYPE_I = NOT_YET_GLOBALLY_CLOSED
```

本卡不使用 fixture actualness，也不把局部 support drop 当成越过 overflow 后的全局出口。
