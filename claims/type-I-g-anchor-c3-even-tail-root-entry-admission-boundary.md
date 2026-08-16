---
kind: claim
claim_id: type-I-g-anchor-c3-even-tail-root-entry-admission-boundary
title: c=3 偶侧 seed 的 fresh root-entry 准入边界
statement: 对 c=3 full-Q complement seed 的条件性 target-source raw receipt，现有 universal_raw_default_entry、r-chart cofactor verifier 和 high-anchor macro 均不能直接把其偶侧 t=1 node 登记为 overflow 状态：前者的 complete-excess carrier Q 必整除 R-1 而不可能等于 M=26h+1，后两者分别具有不相容的 target type 和 charged-parent 形状。可行的最小对象只能是一个 root-only、fresh_source_tree_only 的 raw-to-determinant entry receipt：它保留有序 raw word、even-tail、相位和 determinant seed 的完整内容摘要，并在 entry 后才调用既有 A=1 d=3 dual-RESET。独立 verifier 已对四个 prime-label 控制及一个复合因子块控制实现此类 E1--E3 分析回执；它们不注册全局 edge。现有 q=1 G source-lineage phase relay 已在“预声明 source + 有效 raw lineage + terminal-first”条件下把此类 receipt 接为两条 E1--E5 边，但不使任意 c=3 receipt 自动成为 recursive edge，也不证明 receipt 的全称存在。raw word 本身不能逐边承担 E5。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-g-anchor-c3-affine-prime-target-source-template
  - type-I-g-anchor-c3-two-intermediate-target-source-template
  - type-I-g-anchor-even-tail-complement-source-switch
  - type-I-g-anchor-complement-seed-m1-interface-rigidity
  - type-I-g-anchor-full-q-complement-r11-reset-boundary
  - type-I-overflow-a-one-dual-outer-rank-reset
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - denominator-escape-state-contract
topics:
  - type-I
  - G-anchor
  - c3
  - even-tail
  - root-entry
  - source-provenance
  - E3
  - E4
  - E5
  - dual-reset
  - proof-boundary
sources:
  - claim: type-I-g-anchor-c3-affine-prime-target-source-template
    role: conditional-target-source-raw-receipt
  - claim: type-I-g-anchor-c3-two-intermediate-target-source-template
    role: generalized-raw-receipt-family
  - claim: type-I-g-anchor-even-tail-complement-source-switch
    role: even-side-determinant-decoding
  - claim: type-I-g-anchor-full-q-complement-r11-reset-boundary
    role: conditional-d3-reset-target
  - claim: type-I-high-anchor-cofactor-macro-e1-e4-admission
    role: composite-E1-to-E4-interface-pattern
  - concept: denominator-escape-state-contract
    role: state-and-edge-admission-contract
visibility: public
last_checked: '2026-08-16'
---

# \(c=3\) 偶侧 seed 的 fresh root-entry 准入边界

本卡只处理从 target raw source 到 complement seed 的**状态准入**问题。它不把
raw path 分解为递归边，也不声称已经得到一个 `verified_edge`。

## 1. 目标 seed 与已知 raw receipt

令

\[
p=24h+1,
\qquad
h\not\equiv2\pmod3,
\tag{1}
\]

并取 \(c=3\) complement chart

\[
R=104h-9,
\qquad
M=26h+1,
\qquad
C=x=p-3,
\qquad
K=MC.
\tag{2}
\]

它满足

\[
pR+1=4K,
\qquad
R=4M-13>p,
\qquad
pn=4Md+1
\quad(d,n)=(3,13).
\tag{3}
\]

在 [affine-prime target-source 模板](type-I-g-anchor-c3-affine-prime-target-source-template.md)
及其 [双中间节点推广](type-I-g-anchor-c3-two-intermediate-target-source-template.md)
的条件性素数族中，target 自身的 universal \(p\)-source 有一条实际 raw word 到达

\[
N_R(x)=\{x,R-x\}.
\tag{4}
\]

偶侧解码为

\[
(C,M,t)=\left(x,26h+1,1\right),
\qquad
(x,K)=x,
\qquad
4M>R.
\tag{5}
\]

所以它确实是 physical overflow determinant seed。最后两条强制 \(2\)-边还保存精确尾

\[
(C,t,\Theta)=(x,4,-M)
\longmapsto(x,2,-2M)
\longmapsto(x,1,-13)\pmod R.
\tag{6}
\]

三点的未标记 determinant 行相同，因而 \(t\)、方向和相位不能被从 raw receipt 中丢弃。

## 2. 现有入口不能直接复用

### 默认 complete-excess root 不匹配

既有 `universal_raw_default_entry_v1` 的 carrier 是某个
\(Q\mid R-1\)，而旧支撑为 \(A=1\) 时新 carrier 必为 \(Q\)。若它要产生 (2) 的
seed，必须有 \(Q=M\)。但

\[
R-1=4M-14,
\qquad
M=26h+1>14,
\tag{7}
\]

故 \(M\nmid R-1\)。因此该 complete-excess entry 不可能把 target raw source
直接登记为 carrier \(M\)。这不是缺少一个标志位，而是 carrier 算术不相容。

### r-chart 与 high-anchor 宏的类型不匹配

现有 \(r\)-side cofactor normal form 在 \(A=1\) 时产生的载体为

\[
r=M\bmod p=2h,
\qquad
R_r=8h-1,
\qquad
K_r=2h(p-3),
\tag{8}
\]

并非本 seed 的 \(d\)-dual。后者是

\[
(R_d,K_d;A')=(11,3(22h+1);3).
\tag{9}
\]

更一般地，\(r\)-chart target 的 \(K_r\) 必被 \(C=p-3\) 整除，而对 \(h\ge3\)，

\[
2C<3(22h+1)<3C,
\tag{10}
\]

故 \(C\nmid K_d\)。所以不能把 (9) 重命名为已有 \(r\)-side state。

high-anchor cofactor macro 还要求已收费 parent 结束于
\(p<R<4A\)。本 seed 的 \(A=1\) 与 \(R>p\) 使该不等式不可能成立；它没有可复用的
charged-parent 形状。

## 3. 最小的 root-entry receipt

因而所需对象不是对旧 adapter 的放宽，而是一个只允许在顶层创建的具名入口，例如

```text
c3_affine_prime_even_tail_root_entry_v1
```

它的输出是一个带 \(A=1\) 的 overflow 状态，而非从 charged history 发出的递归边：

```text
state_origin       = c3_affine_prime_even_tail_root_entry_v1
source_tree_scope  = fresh_source_tree_only
normal_form        = c3_even_tail_overflow_seed_v1
equation_target    = 4/p
chart              = (p, R, K)
absorbed_support   = 1
marked_solution_set = Sol(p)
potential_record   = not_a_transition
```

其内容寻址 receipt 至少保存：

```text
h and a primality witness for p; factorizations and raw-capacity data for all labels
ordered source; selected coordinate, q, shift, excess height,
gcd reduction, and ordered output for every raw step
even orientation; (C,M,t); t=4->2->1 tail; prefix and full phase
seed state id; typed F/G/hit reclassification digest; scope and versions
```

现有的 type_i_c3_affine_prime_even_tail_root_entry.py 已以
verify_c3_affine_prime_even_tail_root_entry_v1 对四个 prime-label 控制从原始整数重新检查
(2)--(6)、source 的 unit/primitive 条件、所有 raw 边、\(C=(x,K)=x\)、
\(d=p-C=3\)、\(n=4M-R=13\)，以及 (3) 的 determinant。若类型为 G，还必须
重建 separating character；不能继承缓存的 F/G 标签。

复合标签版本 type_i_c3_factor_block_even_tail_root_entry.py 已把每个标签展开为
逐素因子 raw word，并对 \(h=297\) 的非平凡控制重放同一类 root-only E1--E3 回执。

若将来需要从这个 raw mark 再发出动作，\(t\)、方向、相位和 raw-entry digest 都必须
进入 state ID。若 entry 后立即只作 (9) 的 RESET，它们可以留在一次性 receipt 中，
但 verifier 仍须核对它们。

## 4. E4 与 E5 的正确拼接位置

一旦第 3 节的 root entry 真实创建了状态，(3) 的 \(d=3\) dual 可复用已有 A=1 RESET：

\[
(p,R,K;1)
\Longrightarrow
\bigl(p,11,3(22h+1);3\bigr).
\tag{11}
\]

两端必须都以图表无关的标记集定义为

\[
W_{\rm seed}=W_{11}=\operatorname{Sol}(p),
\qquad
\Phi_{11\to\rm seed}=\operatorname{id}.
\tag{12}
\]

这给出完整 E4：每个分母、单位分数恒等式及 `equation_only` 标签都原样保留。它不预设
\(\operatorname{Sol}(p)\) 非空；F/G 只是在两张图表上分别重算的辅助分类。

raw word 本身不能给 E5。它在 \(m=1\) 层会交替增减 canonical 坐标，而 (6) 的三点又有
同一未标记物理行；有限群相位不是良基势。正确的严格支付发生在 (11)：

\[
B_p=\frac{(p-1)^2}{4}=144h^2,
\qquad
\left\lfloor\frac{B_p}{3}\right\rfloor=48h^2<B_p.
\tag{13}
\]

因此 \(A:1\to3\) 的 joined-support 外层秩下降可以承载 E5。terminal-first 的全部
direct Type I/II 检查必须在 root entry 前运行；命中时直接输出 terminal leaf，不进入
这个候选宏。

## 5. 精确状态

本卡已经确定了旧接口的算术/类型障碍，以及新 entry 必须携带的最小回执字段。独立
prime-label 与 factor-block verifier 已实现 root-only E1--E3 分析回执。

对同时满足 ordinary `q=1 G`、预声明 universal source、有效 source-lineage transcript 和
terminal-first 的子域，新的
[q=1 G c=3 source-lineage phase relay](type-II-q-one-c3-source-lineage-phase-root-entry.md)
已经把 root scope、\(R=11\) typed classification、(11) 的 identity lift 与全局 phase/outer-rank
势接入为两条 E1--E5 边。它并不改变本卡的通用边界：任意 c=3 raw receipt 仍不能仅凭
存在 raw word、formal \(p\)-parent 或 charged history 成为 recursive edge；也尚未证明这些
receipt 对所有相关 \(p\) 存在，或在 RESET 后有全称递归闭包。
