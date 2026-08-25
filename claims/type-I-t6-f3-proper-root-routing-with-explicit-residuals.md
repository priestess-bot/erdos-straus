---
kind: claim
claim_id: type-I-t6-f3-proper-root-routing-with-explicit-residuals
title: T6-F3 proper-root 的确定域路由与显式 residual 穷尽
statement: >-
  对每个带活动 ACTUAL_PERSISTENT admission receipt 的 PROPER_FACTOR_ROOT
  root-capacity state，先按固定 terminal-first 顺序处理 root terminal，再把 h>p 的
  endpoint 隔离为 HIGH_ENDPOINT_RESIDUAL；h=p 因 3|h 而 p=1 (mod 3) 不可能。
  只有在 2<=h<p 的 low-height 支才调用 k=1 空域、Eisenstein quotient、D_star 与
  QC1/TR1 结论。当前没有 QC1 或 TR1 physical serializer，故 low k>1 survivor
  恰落入原有六个 residual 之一。总 survivor 因而恰落入一个 HIGH residual 或六个
  low residual。该七分域分区是 established；HIGH、QC1、TR1、m=3 q=5 的 p^2 gate、
  F3 physicalization 和 T6 均保持 OPEN。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - t6-f3-proper-root-domain-v1
  - type-I-root-capacity-stutter-positive-definite-norm-bound
  - type-I-root-capacity-stutter-h-overlap-m-bound
  - type-I-root-capacity-stutter-k-one-universal-exclusion
  - type-I-root-capacity-stutter-common-divisor-alignment
  - type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
topics:
  - type-I
  - root-capacity
  - proper-root
  - t6-f3
  - routing
  - residual-exhaustion
  - proof-boundary
sources:
  - concept: t6-f3-proper-root-domain-v1
    role: quantified domain, proper semantics, and routing precedence
  - data: data/t6-f3-proper-root-routing-v1.json
    role: machine-readable route and residual registry
  - reproduction: reproductions/type_i_t6_f3_proper_root_routing.py
    role: symbolic partition and implementation consistency checks
visibility: public
last_checked: '2026-08-23'
---

# T6-F3 proper-root 的确定域路由与显式 residual 穷尽

## 1. 定理域

令 \(\mathcal P_{\rm PF}\) 是所有满足以下条件的 state：

1. 它带有活动 producer、serializer 与 enqueue gate 给出的 `ACTUAL_PERSISTENT` receipt；
2. 它的 actual root-capacity payload 满足
   \(M_0=(p^2+p+1)/3\)、\(0<u=(2r+1,M_0)<M_0\)、\(h=3u\)；
3. `proper` 使用总域的真因子义 `PROPER_FACTOR_ROOT`，没有预设 \(h<p\)；
4. terminal 检查按 receipt 中冻结的顺序重放。

只满足整数等式、只有 debug/workfile 记录、只有 conditional adapter control，或尚未入队的
root endpoint 都不属于 \(\mathcal P_{\rm PF}\)。

terminal-first miss 后，\(3\mid h\) 而 \(p\equiv1\pmod3\)，所以 \(h=p\) 不可能。
总域先分成 \(h>p\) 与 \(2\le h<p\)。只有在后一 low-height 支，才沿用

\[
D=mp+1-h,\qquad eD=ph+1,\qquad
a=em-h,\qquad b=e-1,
\]

\[
a^2-ab+b^2=hk,\qquad
D_*=D/(D,h^2-1).
\]

在 terminal-first miss 的 low-height 分支，已有 established 引理给出
\(m\ge3\)、\(D_*>1\) 和 \(k\ge1\)。
这些结论以及 \(k=1\) 空域定理都不外推到 \(h>p\)。

## 2. 路由定理

定义 route precedence：

\[
\mathrm{DOMAIN}\succ\mathrm{TERMINAL}\succ\mathrm{HEIGHT\_SPLIT}\succ
\mathrm{HIGH\_RESIDUAL}\succ\mathrm{K1\_EMPTY}\succ
\mathrm{ACTIVE\_QC1}\succ\mathrm{ACTIVE\_TR1}\succ\mathrm{RESIDUAL}.
\tag{1}
\]

这里 active QC1/TR1 要求一个当前 registry 中的 serializer ID，且该 serializer 对同一 state
提供完整 E1--E5。v1 两个 serializer 集均为空。

**定理。** 对每个 \(S\in\mathcal P_{\rm PF}\)：

1. 若 terminal-first 命中，则唯一返回该 terminal leaf；
2. 若全部 miss 且 \(h>p\)，则唯一进入 `HIGH_ENDPOINT_RESIDUAL`；
3. 若全部 miss 且 \(2\le h<p,k=1\)，则该输入与已建立的 low-height actual empty
   theorem 矛盾；
4. 若全部 miss 且 \(2\le h<p,k>1\)，则不存在 v1 active QC1/TR1 route，并且
   \(S\) 恰落入 `R1`--`R6` 中一个 residual。

这里“唯一”指 route code 由 state 数据和固定 precedence 决定，不指 residual 已有唯一 physical
successor。

## 3. 证明

terminal-first 命中与 miss 互斥，且命中时 route 在读取任何 carrier 前已经返回，所以 terminal
与所有后续分支互斥。

在 miss 分支，\(h=3u\) 被 3 整除，而核心素数 \(p\equiv1\pmod3\)，故 \(h\ne p\)。
于是 \(h>p\) 或 \(2\le h<p\) 两支互斥且穷尽。前者立即给出 HIGH residual；
这一返回发生在读取 \(m,k,D_*\) 之前，所以没有把 low-height Eisenstein 结论外推。

只在 low-height 支，\(k\ge1\) 给出 \(k=1\) 或 \(k>1\) 的穷尽二分。前者由
`type-I-root-capacity-stutter-k-one-universal-exclusion` 证明在 actual low proper-height
域为空。因此所有实际 low-height survivor 都满足 \(k>1\)。

v1 machine registry 明确列出 active QC1/TR1 serializer 集为空。按 physical route 的定义，
没有 serializer 就没有 E2/E3 target、E4 lift 或 E5 ticket，因此不存在活动 QC1/TR1 branch。
这一步只读取活动 registry，不把 arithmetic carrier 当作 edge。

对剩余 low-height survivor 定义

\[
k_\perp=\prod_{q\mid k,\ q\nmid h}q^{v_q(k)}.
\]

由 \(m\ge3\)，恰有 \(m=3\) 或 \(m>3\)。若 \(m=3\)，恰有
\(5\mid D_*\) 或 \(5\nmid D_*\)。前者再由 receipt 的 `raw_path_bound` 恰分为 true/false，
得到 R1/R2；后者由 \(k_\perp>1\) 或 \(k_\perp=1\) 得 R3/R4。若 \(m>3\)，同一
\(k_\perp\) 二分给出 R5/R6。每个分支使用互补谓词，所以两两不交；上述二分没有遗漏，
所以并集等于全部 low-height \(k>1\) survivor。再与互斥的 HIGH residual 合并，
得到七类 residual 对总 survivor 域的互斥穷尽。证毕。

## 4. residual 的证明强度

| residual | 已建立事实 | 尚缺的 physical 内容 |
|---|---|---|
| HIGH | \(u<M_0,h>p\)，且已通过 total-domain actual/persistent 与 terminal-first guards | 不依赖 low \(k,D_*\) 的 family-empty、terminal 或 paid successor |
| R1 | \(m=3,5\mid D_*\) arithmetic slice；所需 path 尚未绑定 | actual source/path coverage 与完整 E1--E5 |
| R2 | raw suffix 已在外部 persistent receipt 中 source-bound | active target serializer、atomic/second-child、E2--E5 与 \(p^2\) gate |
| R3/R5 | 有确定的最小 quotient-only prime \(q_\perp\mid k_\perp\) | 把 arithmetic factor 变为 actual QC1 occurrence 和 E1--E5 edge |
| R4/R6 | \(k\) 的素支撑完全包含于 \(h\)，且 \(D_*>1\) | h-supported QC1 或 transverse TR1 的全称 physical serializer |

R2 中的 `path-bound` 只支付一段 suffix 的 source provenance，不等于 target 已入活动 grammar。
尤其 \(L_\omega\equiv1\pmod {p^2}\) 仍是 OPEN residual gate。

## 5. 状态边界

本卡建立的是

\[
\boxed{\text{proper-root v1 domain partition and residual exhaustion}}
\]

而不是

\[
\forall S\in\mathcal P_{\rm PF}\;
\operatorname{terminal}(S)\lor\exists T\operatorname{PhysicalE1toE5}(S,T).
\]

后一个式子仍未证明。准确状态为：

```text
T6_F3_PROPER_ROOT_DOMAIN_PARTITION = ESTABLISHED
T6_F3_PROPER_ROOT_PHYSICALIZATION = OPEN_MINIMAL_GAPS
HIGH_ENDPOINT_PHYSICALIZATION = OPEN
QC1_PHYSICAL_SERIALIZER = OPEN
TR1_PHYSICAL_SERIALIZER = OPEN
M3_Q5_P2_GATE = OPEN
T6_GLOBAL_SELECTOR_TOTALITY = OPEN
```

聚焦验证：

```bash
python3 reproductions/type_i_t6_f3_proper_root_routing.py --verify
python3 -m unittest tests.test_type_i_t6_f3_proper_root_routing -v
```
