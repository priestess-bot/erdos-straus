---
kind: claim
claim_id: type-I-overflow-fixed-n-bounded-divisor-saturation
title: overflow 固定 n 的有界除子外层秩递降
statement: 设 verified overflow 满足 pn=4Md+1，S=Md=(pn-1)/4，并携带 A|M、1≤A≤B_p=(p-1)^2/4 的 charged support。若存在除子 L|S 使 A<L≤B_p、4L>n 且 floor(B_p/L)<floor(B_p/A)，则 R_L=4L-n、K_L=L(p-S/L) 给出保持 Sol(p) 恒等提升、完整 E1--E5 和严格外层势下降的 overflow_fixed_n_bounded_divisor_outer_rank_v1 边；若 A|L 则旧支撑被保留，若 A∤L 则该同一严格势显式支付支撑重置。R_L<p 时目标为 marked absorb，否则仍为可递归 overflow。特别地，若 S/A≥2 且 S≤B_p（等价于 n≤p-2），可取 L=S；此时 R_S=(p-1)n-1，n=1 时吸收，n≥2 时为严格秩下降的 overflow。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-fixed-n-overflow-rank-descent
  - type-I-marked-support-accumulation-rechart-saturation
topics:
- type-I
- overflow
- determinant
- fixed-n
- bounded-divisor
- support-reset
- outer-rank
- charged-support
- well-founded-descent
- typed-receipt
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: bounded fixed-n divisor selector and E1--E5 verifier
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused 12-fixture bounded-divisor classification
visibility: public
last_checked: '2026-08-03'
---

# overflow 固定 \(n\) 的有界除子外层秩递降

## 1. 精确引理

设已有 source/path/node provenance 的 overflow 状态满足

\[
pn=4Md+1,
\qquad
S=Md=\frac{pn-1}{4},
\qquad
A\mid M,
\qquad
1\le A\le B_p:=\frac{(p-1)^2}{4}.
\tag{1}
\]

若某个除子 \(L\mid S\) 满足

\[
A<L\le B_p,
\qquad
4L>n,
\qquad
\left\lfloor\frac{B_p}{L}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor,
\tag{2}
\]

则定义

\[
R_L=4L-n,
\qquad
K_L=L\left(p-\frac SL\right).
\tag{3}
\]

这里 \(L\mid S\) 使 \(S/L\) 为整数，而 \(4L>n\) 与 (1) 给出

\[
\frac SL=\frac{pn-1}{4L}<p,
\tag{4}
\]

所以 \(K_L>0\)。直接消元得到

\[
pR_L+1=4pL-pn+1=4(pL-S)=4K_L,
\tag{5}
\]

并且 \(L\mid K_L\)。由于 \(n\equiv1\pmod4\)，有

\[
R_L\equiv3\pmod4.
\tag{6}
\]

因此 \((p,R_L,K_L;L)\) 是合法的 canonical chart，且旧解集
\(\operatorname{Sol}(p)\) 通过恒等映射提升到后继。条件 (2) 的最后一项正是

\[
\Pi_A(L):=\left\lfloor\frac{B_p}{L}\right\rfloor
<\Pi_A(A),
\tag{7}
\]

故该边同时满足 E1--E5，类型为
`overflow_fixed_n_bounded_divisor_outer_rank_v1`。若 \(R_L<p\)，目标是
`marked_absorb`；若 \(R_L>p\)，目标仍标记为 `overflow`，但其外层支撑势已严格下降。

选择器用“最大合格 \(L\)”作为规范规则；该规则只消除同一状态中的选择歧义，不是
存在性假设。若候选集为空，回执必须保留 `analysis_evidence`，不能把较小的对偶
载体直接写成后继。

这里必须区分两种支撑语义：若 \(A\mid L\)，后继继续保留旧 charged support；若
\(A\nmid L\)，后继不声称支撑包含关系，而是把
\(\Pi_A(L)<\Pi_A(A)\) 作为显式的外层秩重置支付。后一类仍具有合法 E4，因为标记集
\(W_T=W_S=\operatorname{Sol}(p)\) 与图表无关；但它不是当前 phase 的
support-preserving 边，回执必须将 support_reset_paid 置为真。

## 2. 低互补量的饱和推论

若

\[
\frac SA\ge2,
\qquad
S\le B_p,
\tag{8}
\]

则可取 \(L=S\)。第一项给出 \(A<L\)，且
\(\lfloor B_p/S\rfloor\le\lfloor B_p/(2A)\rfloor<\lfloor B_p/A\rfloor\)；第二项给出
有界性。又因为 \(4S=pn-1>n\)（\(p>2\)、\(n\ge1\)），正性条件也成立。因此

\[
R_S=4S-n=(p-1)n-1,
\qquad
K_S=S(p-1).
\tag{9}
\]

由 \(S=(pn-1)/4\)，整数 \(n\) 下

\[
S\le B_p
\iff
pn-1\le(p-1)^2
\iff
n\le p-2.
\tag{10}
\]

所以 \(n\le p-2\) 且 \(S/A\ge2\) 的 overflow 都有一个显式的固定-\(n\) 支撑
饱和边。\(n=1\) 时 \(R_S=p-2<p\) 为吸收目标；\(n\ge2\) 时
\(R_S=(p-1)n-1>p\)，该边提供严格递归 overflow，而不是直接终端。

## 3. 聚焦复现与边界

统一选择器对现有 12 个 overflow fixture 枚举所有 \(L\mid S\)，施加 (2)，并取最大
合格除子。结果为

| 分类 | 数量 |
|---|---:|
| fixture | 12 |
| verified edge | 12 |
| 其中保留 \(A\mid L\) | 8 |
| 其中由外层势支付 \(A\nmid L\) 的重置 | 4 |
| \(R_L<p\) 的吸收目标 | 0 |
| \(R_L>p\) 的 overflow 目标 | 12 |
| 被拒绝 fixture | 0 |

这些回执同时重算 \(M,d,S,L,R_L,K_L\)、canonical chart、恒等解提升和 E1--E5；它们
是引理的可重放证据，不是对所有 \(A>1\) overflow 的有限扫描证明。当前真正的全称
边界是：对递归可达的 overflow，尚未证明总存在满足 (2) 的 \(L\)，也未证明没有该
除子时必有 source/path/node alternate、直接 Type I/II 终端或另一个良基外层秩。

重放命令：

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```
