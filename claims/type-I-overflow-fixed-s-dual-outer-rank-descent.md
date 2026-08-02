---
kind: claim
claim_id: type-I-overflow-fixed-s-dual-outer-rank-descent
title: overflow 对偶固定 s 图谱与 r 侧外层秩递降
statement: 设 overflow 满足 pn=4Md+1、M=kp+r、1≤r<p、A|M。令 s=(4rd+1)/p=n-4kd，L=lcm(A,r)。若 L|rd、L>A、R_L=4L-s>0、canonical_chart(p,L)=(R_L,K_L)，其中 K_L=L(p-rd/L)，且 floor(B_p/L)<floor(B_p/A)，则目标图表是完整 E1--E5 的 overflow_fixed_s_outer_rank_reset_v1 边；R_L<p 时为 marked absorb，R_L>p 时为严格降低 absorbed-support 秩的 overflow 后继。
claim_status: computationally_reproduced
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - type-I-overflow-fixed-n-overflow-rank-descent
  - type-I-overflow-outer-rank-reset
  - type-I-overflow-qadic-obstruction-transfer
topics:
- type-I
- overflow
- symmetric-dual
- fixed-s
- outer-rank
- charged-support
- well-founded-descent
- typed-receipt
- proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: fixed-s symmetric dual atlas and typed edges
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: focused 12-fixture fixed-s classification
visibility: public
last_checked: '2026-08-03'
---

# overflow 对偶固定 \(s\) 图谱与 \(r\) 侧外层秩递降

## 1. 对称恒等式

设来源 overflow 已有

\[
pn=4Md+1,
\qquad M=kp+r,
\qquad 1\le r<p.
\]

将 \(M=kp+r\) 代回可得

\[
p(n-4kd)=4rd+1.
\]

因此

\[
s:=n-4kd=\frac{4rd+1}{p}>0.
\]

这不是新的猜测条件：右端整除性由来源方程自动给出。它是 d 侧固定-\(n\) 图谱的
对称 r 侧坐标，满足

\[
ps=4rd+1.
\tag{1}
\]

## 2. 固定-\(s\) 外层秩边

给定旧 charged support \(A\mid M\)，取

\[
L=\operatorname{lcm}(A,r).
\]

如果 \(L\mid rd\)，则定义

\[
R_L^{(s)}=4L-s,
\qquad
K_L^{(s)}=L\left(p-\frac{rd}{L}\right)=Lp-rd.
\tag{2}
\]

由 (1) 直接得到

\[
4K_L^{(s)}
=4pL-4rd
=pR_L^{(s)}+1.
\tag{3}
\]

当 \(R_L^{(s)}>0\) 时，\(s>0\) 又保证 \(R_L^{(s)}<4L\)，所以 (3) 和
\(L\mid K_L^{(s)}\) 给出 canonical chart。由于 \(A\mid L\)，目标支撑已经包含旧
支撑；若再有 \(L>A\)，则

\[
\Pi_A(L)=\left\lfloor\frac{B_p}{L}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor=\Pi_A(A),
\qquad B_p=\frac{(p-1)^2}{4}.
\tag{4}
\]

于是恒等的 \(\operatorname{Sol}(p)\) 标记集给出 E4，(1)--(3) 给出 E1--E3，(4)
给出 E5。目标若 \(R_L^{(s)}<p\) 是 `marked_absorb`，若 \(R_L^{(s)}>p\) 则仍是
可以继续进入 overflow 选择器的递降后继。

注意这里的整除条件是

\[
L\mid rd
\quad\Longleftrightarrow\quad
\frac{A}{\gcd(A,r)}\mid d,
\]

它不同于直接 r 图表保持旧支撑所需的
\(A/\gcd(A,r)\mid(p-d)\)。因此固定-\(s\) 图谱是对旧 r 通道的补充分支，不能把
两种条件混写。

## 3. 聚焦回执

选择器对冻结的 12 个 overflow fixture 重算得到：

| 分类 | 数量 |
|---|---:|
| 固定-\(s\) fixture | 12 |
| 完整 E1--E5 边 | 7 |
| \(R_L^{(s)}<p\) 吸收目标 | 0 |
| \(R_L^{(s)}>p\) overflow 目标 | 7 |
| 拒绝 fixture | 5 |

其中 5 条与 d 侧固定-\(n\) 外层秩分支重叠，新增补上的两条是

- `reachable_conflict_bundle_1`：\(p=73,A=19,M=608,r=24,d=19\)，取
  \(s=25,L=456,R_L^{(s)}=1799\)；
- `symmetric_small_chart_support_conflict`：\(p=241,A=8,M=568,r=86,d=124\)，取
  \(s=177,L=344,R_L^{(s)}=1199\)。

因此 d/fixed-\(n\) 与 r/fixed-\(s\) 两个分支的并集在该冻结菜单中覆盖 11/12 个
fixture；唯一仍未覆盖的是 `accumulated_d_one_boundary`，其 \(d=1\) 且
\(\operatorname{lcm}(A,r)\nmid rd\)。

## 4. 逻辑边界

这是一条精确的对偶图谱恒等式和条件性良基边，不是所有 overflow 的存在性定理。它
仍要求 \(L\mid rd\)、正目标和严格势下降；拒绝行不能升级为递归边。它也没有解决
跨状态 Fourier/格证书如何强制 \(L\mid rd\)，或如何处理 d、r 两侧同时失败的状态。

重放命令：

```bash
python3 reproductions/type_i_representation_dual_capacity_selector.py --verify
```

结果位于
`reproductions/type-i-representation-dual-capacity-selector-results.json` 的
`overflow_fixed_s_outer_rank`。
