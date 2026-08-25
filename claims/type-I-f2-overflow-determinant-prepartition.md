---
kind: claim
claim_id: type-I-f2-overflow-determinant-prepartition
title: F2 A>1 overflow 的 determinant receipt 前置分拆与 p=409 异常处置
statement: >-
  设 S=(p,R,K;A,sigma) 是 actual、terminal-first-surviving 的 TYPEI/CHARGED
  overflow，A>1，并绑定 determinant receipt pn=4Md+1、R=4M-n>p、
  K=M(p-d)、M=Ab、1<=d<p。若 b>=2，则同图表支撑提升 A->M 以
  Lambda_p^sharp=(floor(B_p/A),K/A) 严格下降。若 b=1、A<=B_p 且 d>=2，
  则 full-product fixed-n 选择 L=Md=Ad 产生严格 outer-rank target
  (R_L,K_L;L)=((p-1)n-1,L(p-1);L)，且该 target 仍为 overflow。
  若 b=d=1 且 A<=B_p，则 5<=n<=p-4，d=1 complete-excess 的两条 p 门自动
  通过，唯一 support multiplier E>1 产生 M'=AE>p^2>B_p 的 overflow target，
  因而同样以第一 charged-rank 坐标严格下降。所以在这三类相对 adapter 完成共同
  E3 admission 后，带 determinant receipt 的 A>1 域只剩 b=1、A>B_p 的 canonical
  high-support C=p-d 分支；后者再精确分成 C=1 与 C>1。仓库 p=409,A=5
  记录目前因缺 predecessor 不属于 actual 域；若未来其精确
  (M,d,n)=(250,200,489) receipt 被实际绑定，则 b=50，必须由更早的同图表严格
  分支处理，而不能依靠自报 recursive eligibility 或 R=11 的错误 overflow 标签。
  此外在固定 precedence 中，total-cofactor 不存在独立 strict leaf：b>=2 时已被
  same-chart 分支抢占，b=1 时 source 已是 support A 的 canonical chart，投影精确
  t=0 stutter。
  本定理不证明每个 actual overflow 都已携带所需 determinant occurrence，也不补共同
  target serializer，故 F2 与 T6 仍开放。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - type-I-overflow-unbounded-full-product-quotient-fold
  - type-I-overflow-full-product-d-one-complete-excess-capacity-map
  - type-I-p409-a5-charged-history-parent-replay-boundary
  - type-I-t5-full-contract-level-global-well-foundedness
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - F2
  - determinant
  - charged-support
  - same-chart
  - full-product
  - high-support
  - p409
  - residual-partition
  - proof-boundary
sources:
  - claim: type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
    role: b-at-least-two same-chart strict edge
  - claim: type-I-overflow-unbounded-full-product-quotient-fold
    role: low-support b-one d-at-least-two full-product edge
  - claim: type-I-overflow-full-product-d-one-complete-excess-capacity-map
    role: low-support b-equals-d-equals-one complete-excess outer drop
  - claim: type-I-p409-a5-charged-history-parent-replay-boundary
    role: p409 missing-parent and noncanonical-anchor boundary
  - reproduction: reproductions/type_i_f2_overflow_determinant_prepartition.py
    role: exact branch and rank controls
visibility: public
last_checked: '2026-08-24'
---

# F2 (A>1) overflow 的 determinant receipt 前置分拆

## 1. 精确量词

固定核心素数

\[
p\equiv1\pmod {24},
\qquad
B_p=\frac{(p-1)^2}{4}.
\tag{1}
\]

令

\[
S=(p,R,K;A,\sigma)
\tag{2}
\]

是已经有 actual persistent parent、内容地址、scope \(\sigma\) 与 terminal-first miss 的
`TYPEI/CHARGED` overflow state，并假定同一个 source receipt 绑定

\[
pn=4Md+1,
\qquad
R=4M-n>p,
\qquad
K=M(p-d),
\tag{3}
\]

\[
M=Ab,
\qquad
A>1,
\qquad
b\ge1,
\qquad
1\le d<p.
\tag{4}
\]

这里 (3) 不是从一张裸 chart 事后挑出的代数分解。它必须是与 `source_state_id` 绑定的
实际 determinant/source occurrence；否则下述 E1 不成立。本卡因此关闭的是“已有绑定
determinant receipt 的 actual 子域”，不是全部裸 overflow chart。

## 2. (b\ge2)：同图表支撑提升先行

若 \(b\ge2\)，定义

\[
T_M=(p,R,K;M,\sigma).
\tag{5}
\]

因为 \(K=M(p-d)\)，有 \(M\mid K\)。source 与 target 的 T5 charged local rank 为

\[
\lambda(S)
=\left(\left\lfloor\frac{B_p}{A}\right\rfloor,b(p-d),0,0\right),
\tag{6}
\]

\[
\lambda(T_M)
=\left(\left\lfloor\frac{B_p}{M}\right\rfloor,p-d,0,0\right).
\tag{7}
\]

第一坐标不增加；若相等，则第二坐标由 \(b(p-d)\) 严格降到 \(p-d\)。所以

\[
\boxed{\lambda(T_M)<\lambda(S).}
\tag{8}
\]

这个论证同时覆盖 \(A\le B_p\) 与 \(A>B_p\)，也不要求 \(M\le B_p\)。它正是既有
same-chart theorem 的 guard；本卡只把该 guard 放到 F2 的第一个 determinant 分裂处。

## 3. (b=1,A\le B_p,d\ge2)：full-product 严格出口

现在设 \(b=1\)，所以 \(M=A\)。再设

\[
A\le B_p,
\qquad d\ge2.
\tag{9}
\]

取 fixed-\(n\) 完整乘积

\[
L=Md=Ad.
\tag{10}
\]

商为一，故 target determinant 为

\[
(M_T,d_T,n_T;A_T)=(L,1,n;L).
\tag{11}
\]

其图表坐标是

\[
R_T=4L-n=(p-1)n-1,
\qquad
K_T=L(p-1).
\tag{12}
\]

首先 \(n\ne1\)。否则 (3) 给出 \(p=4Ad+1\)，进而

\[
R=4A-1=\frac{p-1}{d}-1<p,
\]

与 source overflow 矛盾。又 \(n\equiv1\pmod4\)，故 \(n\ge5\)，从而

\[
R_T=(p-1)n-1>p.
\tag{13}
\]

所以这个 target 仍是 overflow，不会在这里引入一个未分类的低图表 target。

由 \(L/A=d\ge2\) 与 \(A\le B_p\)，既有无界 full-product 引理给出

\[
\left\lfloor\frac{B_p}{L}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{14}
\]

故即使 target 第二坐标变为 \(p-1\)，第一坐标已经严格支付 `LOCAL_DROP`。

## 4. 分拆后的精确 residual

在 terminal-first miss 之后，先执行第 2 节，再执行第 3 节。其补集满足 \(b=1\)，并且
恰落入以下三类之一：

### 4.1 低支撑饱和 (d=1) 也有 strict complete-excess 出口

\[
A\le B_p,
\qquad M=A,
\qquad d=1.
\tag{15}
\]

此时 \(K=A(p-1)\)，source 已是 support \(A\) 的 canonical capacity \(p-1\)，而
full-product 取 \(L=A\) 的确 stutter。但 source overflow 还给

\[
A=\frac{pn-1}{4},
\qquad
R=(p-1)n-1>p.
\tag{15a}
\]

由 \(n\equiv1\pmod4\) 与 \(R>p\) 有 \(n\ge5\)。又由 \(A\le B_p\) 得
\(n\le p-4\)，所以

\[
5\le n\le p-4.
\tag{15b}
\]

既有 d=1 complete-excess 定理令

\[
g=\gcd\left(\frac{p+1}{2},\frac{n+1}{2}\right),
\qquad
E=\frac{(p-1)n-2}{2g}>1,
\qquad
M'=AE.
\tag{15c}
\]

(15b) 使 primitive raw-source 与 p-free 两门自动通过，并且

\[
M'>p^2>B_p.
\tag{15d}
\]

其 canonical target \(T\) 强制仍有 \(R_T>p\)。无论 target capacity 是严格小于
\(p-1\)，还是处于后续 regeneration residue，真实 parent-to-target rank 的第一坐标已经满足

\[
\left\lfloor\frac{B_p}{M'}\right\rfloor=0
<
\left\lfloor\frac{B_p}{A}\right\rfloor.
\tag{15e}
\]

所以该分支是 `LOW_SUPPORT_D_ONE_COMPLETE_EXCESS_OUTER_DROP`，不是 residual。

### 4.2 高支撑 canonical (C=1)

若 \(A>B_p\)，由 \(b=1\) 定义

\[
C=\frac KA=p-d\in\{1,\ldots,p-1\}.
\tag{16}
\]

源图表已经是 support \(A\) 的 canonical chart，因为

\[
4AC=4K\equiv1\pmod p,
\qquad
C=\langle(4A)^{-1}\rangle_p.
\tag{17}
\]

当 \(C=1\) 时，T5 local tuple 是 \((0,1,0,0)\) 的同协议最小元。它必须转交独立的
C=1 terminal、outer-rank、lower-protocol/phase 或 family-empty 证明，不能复用一个同层 route。

### 4.3 高支撑 canonical (C>1)

当 \(C>1\) 时，source 转交 rank-aware high-support routing。complete-excess improvement
set 非空时可取严格 \(c_Q<C\) target；空集时仍是本 track 的主要 residual，不能由 C=1
no-go 代替。

这里不需要为 high-support complete-excess target 预留一个低图表 owner。若一个合法
bundle 有 \(M>A>B_p\)，其 canonical target 满足 \(M\mid K_M\)。若反设
\(R_M<p\)，则 \(R_M\equiv3\pmod4\) 与 \(p\equiv1\pmod4\) 给

\[
R_M\le p-2,
\qquad
K_M=\frac{pR_M+1}{4}\le B_p<M,
\tag{17a}
\]

矛盾于 \(M\mid K_M\)。故

\[
\boxed{A>B_p,\ M>A\Longrightarrow R_M>p.}
\tag{17b}
\]

因此 high-support rank-aware/M target 始终留在 `TYPEI/CHARGED` overflow owner；只有
低支撑 rechart 可能需要 `TYPEI/ABSORB` protocol drop。

因此 relative determinant 子域被严格压成

\[
\boxed{
b\ge2\ \Longrightarrow\ \text{same-chart strict};
}
\tag{18}
\]

\[
\boxed{
b=1,\ A\le B_p,\ d\ge2
\ \Longrightarrow\ \text{full-product strict};
}
\tag{19}
\]

并且 \(b=1,A\le B_p,d=1\) 由 (15a)--(15e) 也严格退出。因此 relative determinant
子域的所有低支撑 leaf 都有 strict 算术出口；真正 residual 只剩 (16)--(17) 的两个
high-support canonical leaf。不存在未命名的第四类 determinant leaf。

## 5. (p=409,A=5) 的精确处置

仓库旧控制包含

\[
H_{\rm raw}=(409,251,25665;5),
\qquad
S=(409,511,52250;5),
\tag{20}
\]

以及 \(S\) 的算术 determinant

\[
(M,d,n)=(250,200,489).
\tag{21}
\]

活动边界定理已经证明：没有 verified predecessor 到达 \(H_{\rm raw}\) 或 \(S\)，所以当前
record 不属于本卡的 actual source 域。它不能用 `recursive_edge_eligible=True` 自我认证。

若未来另一个 theorem 真正提供到 \(S\) 的方向正确 parent receipt，并把 (21) 绑定到
`source_state_id`，则

\[
b=M/A=50.
\]

因此按 precedence 必须先走第 2 节：

\[
(409,511,52250;5)
\longrightarrow
(409,511,52250;250),
\tag{22}
\]

且 rank 从

\[
(8323,10450)\longrightarrow(166,209)
\tag{23}
\]

严格下降。旧 p=409 fixed-\(n\) control 的另一个 \((R,K,A)=(11,1125,125)\) target
满足 \(R<p\)，所以任何仍称其为 `overflow` 的 serializer 都不满足 E3；(22) 不依赖这个
错误标签。

这给出完整二分：当前 p=409 record 因缺 actual parent 而域外；一旦 actualness 被独立补齐，
它由更早的 same-chart guard 处置，而不是成为新的例外 family。

## 6. ordered total-cofactor strict leaf 为空

任一能够调用 total-cofactor adapter 的 actual source 都必须携带 (3)--(4) 的绑定
determinant receipt。若 \(b\ge2\)，第 2 节已经给出 precedence 更高的 strict same-chart
target，因此 scheduler 不会到达 total-cofactor。若 \(b=1\)，则

\[
K=A(p-d),
\qquad
4A(p-d)=4K\equiv1\pmod p.
\tag{24}
\]

由于 \(1\le p-d<p\)，support \(A\) 的 canonical cofactor 正是

\[
C_A=\langle(4A)^{-1}\rangle_p=p-d.
\tag{25}
\]

所以 total-cofactor target 与 source 的 \((R,K;A)\) 完全相同，容量分解中的
\(t=0\)，必须按 adapter 既有规则拒绝为 canonical stutter。由此得到

\[
\boxed{
\text{ordered total-cofactor strict branch}=\varnothing.
}
\tag{26}
\]

该结论不是说 total-cofactor 算术 adapter 无用；它仍是 target retyping 的独立 reference
control。结论只是：在本 track 固定的 actual determinant precedence 中，它不需要成为一个
新的递归 producer。

## 7. 尚未闭合的合同层

第 2--4.1 节的 E1 仍依赖输入中真实绑定的 source/determinant receipt；它们没有证明每个 actual
overflow 都携带此 occurrence。三个 strict target 类型还必须投影到 coordinator 的共同
`PersistentSelectorStateV1`，独立重算 hit/F/G、owner 与 state ID，并通过唯一 admission gate。

所以本卡的准确状态是：

```text
F2_DETERMINANT_RECEIPT_PREPARTITION = ESTABLISHED
F2_DETERMINANT_RECEIPT_LOW_SUPPORT_ARITHMETIC_TOTALITY = ESTABLISHED_RELATIVE
P409_CURRENT_RECORD = OUTSIDE_ACTUAL_DOMAIN
P409_IF_ACTUAL_WITH_EXACT_RECEIPT = SAME_CHART_STRICT
ORDERED_TOTAL_COFACTOR_STRICT_BRANCH = EMPTY
F2_A_GT_ONE_TOTALITY = OPEN
F2_HIGH_SUPPORT_TOTALITY = OPEN
T6 = OPEN
```

聚焦复现：

```bash
python3 reproductions/type_i_f2_overflow_determinant_prepartition.py --verify
python3 -m unittest tests.test_type_i_f2_overflow_determinant_prepartition -v
```
