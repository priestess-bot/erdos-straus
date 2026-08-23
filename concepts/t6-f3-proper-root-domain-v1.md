---
kind: concept
concept_id: t6-f3-proper-root-domain-v1
title: T6-F3 proper-root v1 真实研究域与路由合同
summary: 精确定义 F3 使用的 ACTUAL_PERSISTENT proper-factor root receipt、terminal-first 顺序、proper 的两种不同含义，以及 QC1/TR1 physical edge 与 arithmetic carrier 的区别；总域保留 u<M0 且 h>p 的 high endpoint，并只在 2<=h<p 的低高度子域使用 Eisenstein quotient，将 survivor 分成一个 high residual 与六个低高度 residual，而不声称 F3 或 T6 闭合。
topics:
  - type-I
  - root-capacity
  - proper-root
  - t6
  - selector
  - routing-contract
  - proof-boundary
used_by:
  - type-I-t6-f3-proper-root-routing-with-explicit-residuals
sources:
  - claim: type-I-root-capacity-stutter-positive-definite-norm-bound
    role: strict-height proper-root stutter equations and m lower bound
  - claim: type-I-root-capacity-stutter-h-overlap-m-bound
    role: nontrivial transverse divisor D-star
  - claim: type-I-root-capacity-stutter-k-one-universal-exclusion
    role: k-equals-one actual empty slice
  - claim: type-I-root-capacity-stutter-common-divisor-alignment
    role: h-supported versus quotient-only Eisenstein factors
  - claim: type-I-root-capacity-stutter-m-three-biquadratic-norm-reduction
    role: m-equals-three and q-equals-five arithmetic-only slice
  - concept: denominator-escape-state-contract
    role: E1--E5 and persistent admission semantics
  - data: data/t6-f3-proper-root-routing-v1.json
    role: machine-readable precedence and residual registry
visibility: public
last_checked: '2026-08-23'
---

# T6-F3 proper-root v1 真实研究域与路由合同

## 1. 本合同证明什么

本合同只固定 T6-F3 的量词域和路由语言。它的目标不是从现有算术直接制造一条边，而是消除
三种容易混淆的对象：

1. 满足若干整数等式的 analysis-only 元组；
2. 有 actual root arithmetic receipt、但没有进入 persistent queue 的端点；
3. 已由活动 producer、serializer 与 admission gate 接纳的 persistent state。

F3 的量词只覆盖第 3 类。总域使用 `PROPER_FACTOR_ROOT`，不能借改写术语把
\(u<M_0,h>p\) 的端点删除。域分区成立不蕴含任何 residual 已经 terminal，也不蕴含存在
QC1/TR1 physical edge。

## 2. `proper` 的两种含义

令

\[
M_0=\frac{p^2+p+1}{3},\qquad
u=(2r+1,M_0),\qquad h=3u.
\]

仓库历史上对 `proper-root` 使用过两个强度不同的条件。v1 必须显式区分。

### 2.1 `PROPER_FACTOR_ROOT`

它只表示 root-height 来自 \(M_0\) 的真因子：

\[
0<u<M_0,\qquad u\mid M_0,\qquad h=3u.
\tag{PF}
\]

这个条件排除 saturated height \(h=p^2+p+1\)，但不推出 \(h<p\)。因此只满足 (PF)
的端点不能自动使用正定范数界、\(m<1+\sqrt h\) 或 F3 的 proper-height 引理。

### 2.2 `STRICT_PROPER_HEIGHT`（低高度子域）

已有正定 Eisenstein 范数与 \(k=1\) 排除定理使用更强的条件

\[
2\le h<p.
\tag{PH}
\]

在 \(h\mid p^2+p+1\) 和 \(h=3u\) 下，(PH) 蕴含 (PF)，反之不成立。本合同的
**总域**始终使用 (PF)；只有明确写作 `LOW_PROPER_HEIGHT` 时才附加 (PH)。
特别地，\((p,r,h)=(313,90,543)\) 满足 \(M_0=32761=181^2\)、
\((2r+1,M_0)=u=181<M_0\)，
所以满足 (PF)，但 \(h>p\)。它是区分两义的 arithmetic routing control，不是
actual persistent witness。

## 3. `ACTUAL_PERSISTENT` receipt

一个 v1 F3 输入必须带有不可由算术字段自行伪造的 admission envelope：

```text
source_class              = ACTUAL_PERSISTENT
state_id                  = content-addressed active state id
producer_id               = active producer id
admission_id              = persistent enqueue/admission receipt id
source_path_digest         = digest of the replayable root-to-endpoint path
terminal_first_digest      = digest of the ordered terminal checks
maximal_receipt_digest     = digest of the canonical complete-excess receipt
```

这些字段的含义是：producer 已在活动源码中产生该 state，serializer 已完成活动 schema 的
序列化，admission gate 已经接纳它进入 persistent queue。仅写入字符串或由 verifier 构造一个
同形对象并不能在数学上证明 actualness；实现中的同形 fixtures 只检查路由程序，不是 actual
receipt 证据。

在 envelope 之下，总域的 root payload 必须由上游 receipt verifier 重算：

\[
p\equiv1\pmod {24},\qquad p\text{ prime},\qquad
M_0=\frac{p^2+p+1}{3},\qquad
0<u=(2r+1,M_0)<M_0,\qquad h=3u,
\tag{A1}
\]

以及 active root-capacity endpoint 的实际 source/maximal-receipt 字段。terminal-first miss 后，
先比较 \(h\) 与 \(p\)。因为 \(3\mid h\) 而核心素数 \(p\equiv1\pmod3\)，
\(h=p\) 不可能。因此总域严格分成

\[
h>p
\qquad\text{或}\qquad
2\le h<p.
\tag{A2}
\]

第一支立即进入 `HIGH_ENDPOINT_RESIDUAL`。它不得读取下面的低高度字段作为已证约束。
只有第二支才能调用现有 low proper-height stutter receipt，并重算

\[
4K=pR+1,\qquad R-h=ED,\qquad D\mid K,\qquad (D,h)=1,
\tag{A3}
\]

\[
D=mp+1-h,\qquad eD=ph+1,\qquad a=em-h,\qquad b=e-1,
\tag{A4}
\]

\[
N=a^2-ab+b^2=hk,\qquad
D_* = \frac{D}{(D,h^2-1)}.
\tag{A5}
\]

对 terminal-first 后的 actual **low** proper-height stutter，已有定理给出

\[
m\ge3,\qquad D_*>1,\qquad k\ge1.
\tag{A6}
\]

低高度子域的未闭合量词进一步限制为 \(k>1\)。\(k=1\) actual low-height slice
已由无限下降证明为空。没有证据把 \(N=hk\)、\(k\ge1\)、\(k=1\) 空域、
\(D_*>1\) 或 quotient-only factorization 外推到 \(h>p\) 的 HIGH 支。

## 4. Terminal-first 的不可交换顺序

对每个已经通过域验证的 state，路由顺序固定为：

1. 重放 `terminal_first_digest` 指定的全部活动 terminal 检查；
2. 若命中，返回带 verifier 的 terminal certificate，不再读取 QC1、TR1 或 residual；
3. 只有全部 miss 后，才按 \(h>p\) 或 \(2\le h<p\) 分流；
4. \(h>p\) 立即返回 `HIGH_ENDPOINT_RESIDUAL`，不读取低高度 \(k,D_*\)；
5. 在低高度支，\(k=1\) 由 empty theorem 排除；
6. 低高度 \(k>1\) 才允许检查活动 QC1/TR1 serializer；
7. 当前无此 serializer，故进入六个低高度 residual。

因此 `terminal` 不是 residual 的一个可选标签，而是优先级更高、与所有 survivor residual
互斥的输出。

## 5. QC1/TR1 的物理含义

对 low-height survivor \(S\)，QC1 的 arithmetic carrier 是 \(q\mid k(S)\)，TR1 的 arithmetic
carrier 是 \(q\mid D_*(S)\)。二者只有在同一活动 serializer 连续给出以下全部内容时才是
physical route：

\[
\operatorname{E1}\land\operatorname{E2}\land\operatorname{E3}
\land\operatorname{E4}\land\operatorname{E5}.
\]

其中 E1 必须绑定实际 occurrence、source path、provenance 与 terminal priority；E2/E3 必须
产生确定、活动 schema 可读且有 owner 的 target；E4 是全 target solution set 的 lift；E5 是
真实 parent-to-final-target 的 T5 ticket。仅有 \(q\mid k\)、\(q\mid D_*\)、raw child、
strict formal cofactor 或 local chart 均不满足定义。

当前 v1 registry 的事实是：

```text
active QC1 serializers = empty
active TR1 serializers = empty
```

所以 v1 路由器绝不输出 `QC1_PHYSICAL_EDGE` 或 `TR1_PHYSICAL_EDGE`。HIGH 支同样没有
活动 physical serializer；它保留为一个独立 residual，而不是被强塞进未定义的 QC1/TR1。
这不是说这些 edge 不存在，而是说当前活动仓库尚未证明并登记它们。

## 6. quotient-only part

只在 `LOW_PROPER_HEIGHT` 支，为区分 QC1 的两种 provenance，定义

\[
k_\perp=\prod_{q\mid k,\ q\nmid h}q^{v_q(k)}.
\tag{Q}
\]

若 \(k_\perp>1\)，最小素因子 \(q_\perp\mid k_\perp\) 是确定的 quotient-only arithmetic
carrier；若 \(k_\perp=1\)，则 \(k\) 的所有素因子都已在 \(h\) 的素支撑上。公共因子对齐
定理说明这一区分是真实的 provenance 区分，但两支都还没有 physical serializer。

## 7. 七个互斥 residual

对总域中 terminal-first miss、无活动 physical serializer 的输入，按以下顺序分类。

| code | 精确 predicate | principal open route |
|---|---|---|
| `HIGH_ENDPOINT_RESIDUAL` | `PROPER_FACTOR_ROOT` 且 \(h>p\) | high endpoint 的 terminal/physicalization 定理；禁止读取 low-height \(k,D_*\) |
| `R1_M3_Q5_PATH_UNBOUND` | \(m=3,\ 5\mid D_*\)，且 actual persistent receipt 未绑定所需 raw suffix | TR1 source/path coverage |
| `R2_M3_Q5_PATH_BOUND_NO_SERIALIZER` | \(m=3,\ 5\mid D_*\)，且 raw suffix 已 source-bound | TR1 target/serializer/E2--E5 |
| `R3_M3_NONQ5_QUOTIENT_ONLY` | \(m=3,\ 5\nmid D_*,\ k_\perp>1\) | QC1 quotient-only physicalization |
| `R4_M3_NONQ5_H_SUPPORTED` | \(m=3,\ 5\nmid D_*,\ k_\perp=1\) | h-supported QC1 or transverse TR1 |
| `R5_MGT3_QUOTIENT_ONLY` | \(m>3,\ k_\perp>1\) | QC1 quotient-only physicalization |
| `R6_MGT3_H_SUPPORTED` | \(m>3,\ k_\perp=1\) | h-supported QC1 or transverse TR1 |

互斥性先来自 \(h>p\) 或 \(2\le h<p\) 的高度二分；等号不可能。HIGH 支到此返回，
所以不使用 \(m,k,D_*\)。低高度支再由 \(k=1\) empty theorem 排除 closed slice；
对低高度 \(k>1\)，互斥性来自三次二分：\(m=3\) 或 \(m>3\)；在 \(m=3\) 中
\(5\mid D_*\) 或否；在其余支中 \(k_\perp>1\) 或 \(k_\perp=1\)。q=5 支再按
`raw_path_bound` 的布尔值分开。由 (A6)，低高度没有第三种 \(m\) 或退化 \(D_*\)
情形。因此一个 HIGH residual 与六个 low residual 两两不交，且穷尽总 survivor 域。
这个结论不声称 HIGH 非空；它只证明任何 actual HIGH 输入都不会被定义排除或误投到
低高度定理。

## 8. \(m=3,q=5\) 的准确位置

`m=3,q=5` 不是 F3 总域，也不是整个 low-height \(m=3\) slice。它精确位于

\[
\{S:m(S)=3,\ 5\mid D_*(S)\}
\subseteq \{S\in\mathcal D_{F3}^{\rm low}:m(S)=3\}
\subseteq\mathcal D_{F3}^{\rm low}
\subseteq\mathcal D_{F3}^{\rm PF}.
\]

这些是 predicate inclusion，不声称任一集合非空。HIGH 支不在这些集合中，也没有定义可用的
q=5/Eisenstein routing payload。

现有定理在该 slice 内建立了 \(5\)-进管、pure-\(T\) carrier、raw deflation policy、
canonical channel partition 与 \(L_\omega\equiv1\pmod {p^2}\) hard gate 的算术归约。
它们都标为 arithmetic-only：

- 未证明每个 ACTUAL_PERSISTENT state 保存所需 source-bound raw path；
- 即使 path 已绑定，也没有活动 target serializer；
- atomic/second-child typing、全域 lift 与 parent-to-final-target E5 尚未连续完成；
- \(L_\omega\equiv1\pmod {p^2}\) 尚未证明为空、terminal 或 paid successor。

所以这条 slice 只能落入 R1/R2，不能进入 `covered slice` 或 physical TR1 branch。

## 9. 已覆盖切片与仍开放的最小命题

v1 中真正完成的 low-height proper-root 路由叶只有：

1. terminal-first 命中的 root terminal；
2. \(k=1\) actual low-height family-empty theorem。

HIGH endpoint 没有已覆盖出口。\(k=3\) primitive fiber、\(m=3\) 双二次范数、
q=5 raw policy 和 \(p^2\) gate 都只是 low residual 上的 established arithmetic tags，
不是已覆盖出口。

当前最小开放命题是：

1. 对 HIGH endpoint 证明 family-empty、terminal 或完整 paid successor；
2. 为一个全称 low-height QC1 family 建立活动 E1--E5 serializer；
3. 为一个全称 low-height TR1 family 建立活动 E1--E5 serializer；
4. 在 q=5 slice 证明 source-path coverage，并连续完成 target serializer、atomic/second-child
   与全域 lift；
5. 把 \(L_\omega\equiv1\pmod {p^2}\) 证明为 empty、terminal 或 paid successor；
6. 在 F1 grammar freeze 后证明每个新 target 的 owner 与 recursive re-entry。

在这些命题完成前，唯一正确的总状态是：

```text
T6_F3_PROPER_ROOT_DOMAIN_PARTITION = ESTABLISHED
T6_F3_PROPER_ROOT_PHYSICALIZATION = OPEN_MINIMAL_GAPS
T6_GLOBAL_SELECTOR_TOTALITY = OPEN
```
