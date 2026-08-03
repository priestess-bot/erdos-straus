---
kind: claim
claim_id: type-I-overflow-fixed-s-bounded-divisor-saturation
title: overflow 对偶 fixed-s 的有界除子外层秩递降
statement: 设 verified overflow 满足 pn=4Md+1、M=kp+r、1≤r<p、1≤d<p，并令 s=(4rd+1)/p。若当前 absorbed support 满足 1≤A≤B_p=(p-1)^2/4，且存在 L|rd 使 A<L≤B_p、4L>s、floor(B_p/L)<floor(B_p/A)，则 R_L=4L-s、K_L=L(p-rd/L) 给出保持 Sol(p) 恒等提升、完整 E1--E5 和严格外层势下降的 overflow_fixed_s_bounded_divisor_outer_rank_v1 边；若 R_L<p 则为 marked absorb，否则仍为 overflow。A|L 不是必要条件：若 A∤L，严格外层势显式支付 support reset。该存在性条件不对所有 overflow 自动成立。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-fixed-s-dual-outer-rank-descent
  - type-I-overflow-fixed-n-bounded-divisor-saturation
topics:
- type-I
- overflow
- determinant
- fixed-s
- bounded-divisor
- support-reset
- outer-rank
- well-founded-descent
- typed-receipt
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: bounded fixed-s divisor selector and E1--E5 verifier
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused 12-fixture bounded-dual classification
visibility: public
last_checked: '2026-08-04'
---

# overflow dual fixed-s bounded-divisor outer-rank descent

## 1. 算术恒等式

设已验证 overflow 状态满足 pn=4Md+1，M=kp+r，1≤r<p，1≤d<p。

由 M=kp+r 消去 k 得 p*s=4*r*d+1，其中 s=(4*r*d+1)/p。

因此 s 是正整数。对任意 L|r*d 定义 R_L=4L-s、K_L=L*(p-r*d/L)。
若 4L>s，则 R_L>0；直接计算得 4*K_L=p*R_L+1，且 L|K_L。

同样，若 2A≤r*d≤B_p，则取 L=r*d。此时 s<4*r*d，
Pi(r*d)<Pi(A)，并且 K_L=r*d*(p-1)，所以这是另一个无样本的完整 fixed-s 边。
前述三条充分条件共同把简单饱和子族之外的部分压到
\(r<2A\)、\(d<2A\) 或 \(d>B_p\)，并且 \(r*d>B_p\) 或 \(r*d<2A\)；
这只是双通道算术边界的结构收缩，剩余部分仍需因子、容量或 alternate 论证。

还存在一个此前未单列的 d-饱和子族。若

\[
2A\le d\le B_p,
\]

则直接取 \(L=d\)。因为 \(d\mid r*d\)，且

\[
s=\frac{4rd+1}{p}<4d
\]

（\(1\le r<p\)），所以 \(R_L=4d-s>0\)。同时 \(d\ge2A\) 且 \(d\le B_p\)
给出

\[
\Pi(d)=\left\lfloor\frac{B_p}{d}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor=\Pi(A),
\]

并且 \(K_L=d(p-r)\)。因此该条件同样给出完整的 fixed-s 恒等提升边；它在
\(r<2A\) 而 \(d\) 较大时补上 product-saturation 子族未覆盖的部分。它仍不处理
\(d=1\) 或 \(d>B_p\) 的余项。

还可以把一般复合 \(r*d\) 压成一个规范 cofactor。令
\(\ell=\operatorname{spf}(r*d)\) 为 \(r*d\) 的最小素因子，并令

\[
L=\frac{r*d}{\ell}.
\]

若

\[
2A\le L\le B_p,
\]

则 \(\ell<p\)，且 \(d,r<p\) 保证 \(r*d\ge\ell\)。因此

\[
s=\frac{4r*d+1}{p}<\frac{4r*d}{\ell}=4L,
\qquad
K_L=L(p-\ell)>0.
\]

再结合 \(L\mid r*d\)、\(L\ge2A\) 和 \(L\le B_p\)，得到
\(\Pi(L)<\Pi(A)\) 以及

\[
4K_L=p(4L-s)+1.
\]

所以 \(L=r*d/\operatorname{spf}(r*d)\) 是一个规范的 fixed-s 恒等提升边。该条件
覆盖 \(r,d>1\) 且乘积较大的残余；它仍是充分条件，不声称所有 overflow 都满足。

## 2. 支持势与完整边

令 B_p=(p-1)^2/4，Pi(A)=floor(B_p/A)。

若 1≤A≤B_p、A<L≤B_p 且 Pi(L)<Pi(A)，则 Sol(p) 是图表无关的标记集，
可用恒等映射作解提升。E1--E3 来自行列式恒等式和 L|r*d，E4 来自恒等提升，
E5 正是 Pi(L)<Pi(A)。

如果 L 不包含旧支撑 A，这并不破坏边的合法性；状态记录把严格势下降标记为
`support_reset_paid`，不再声称旧支撑包含于后继支撑。若 A|L，则同时保留旧支撑。

当 R_L<p 时后继是 `marked_absorb`；当 R_L>p 时后继仍是 overflow，但
absorbed-support 势已经严格下降。选择器取所有合格 L 中的最大者，只用于消除
选择歧义，不承担存在性证明。

一个无样本充分子族可直接读出：若 r≥2A，则取 L=r。核心素数范围满足
r≤p-1≤B_p；又 d≤p-1，所以 s=(4rd+1)/p<4r。因为 r≥2A，
floor(B_p/r)<floor(B_p/A)，故 L=r 自动满足所有固定-s 有界除子条件。
因此任意递归可达 overflow 若未进入该子族，必满足 r<2A；这只是余项的结构收缩，
不等于该余项已经有容量或 alternate 证明。

## 3. 适用边界与回放

该引理只对给定的有界除子 L|r*d 提供完整递降边；它不声称每个 overflow 都有这样的 L。
当前 12 个冻结 overflow 回放中，选择器得到 11 条 verified edge，其中 1 条为
R_L<p 的 marked absorb，10 条仍为 overflow；唯一拒绝项是
`reachable_conflict_bundle_3`，其对偶载体 r=1 且没有合格 L。

复现命令：

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

结果位于 `reproductions/type-i-representation-dual-capacity-selector-results.json` 的
`overflow_fixed_s_bounded_divisor_outer_rank` 分支。该回放收缩了双通道的有限余项，
但没有关闭递归可达 A>1 overflow 的全称存在性。
