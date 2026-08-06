---
kind: claim
claim_id: type-I-overflow-dual-phase-tree-split-capacity
title: overflow 双通道相位树分裂的精确容量税
statement: 对 d/r 两个 q 进缺陷记录，单位相位的最大共同深度 \(s=\min(h_d,h_r,v_q(\eta_d-\eta_r))\) 完全决定两条相位树的层胞数：共同前缀层为一个胞，超过 \(s\) 且低于较小高度的层为两个胞，其余高层为一个胞。若相位标签落在长度 \(M\) 的整数区间、每个 q^k 胞的重复度不超过 \(\mu\)，则总高度受到带显式分裂税的容量上界；任何超出都给出双通道相位树容量缺口。该结论不假定 alternate 存在，且区分原始双债务与已证明的共同前缀去重。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-dual-channel-first-layer-phase-separation
  - type-I-cross-state-q-adic-capacity-bound
  - type-I-phase-clearing-cell-capacity-contract
topics:
- type-I
- overflow
- dual-channel
- phase-tree
- q-adic
- capacity
- split-tax
- source-switch
- proof-program
sources:
  - claim: type-I-overflow-dual-channel-first-layer-phase-separation
    role: dual-unit-phase-and-common-prefix
  - claim: type-I-cross-state-q-adic-capacity-bound
    role: nested-label-capacity
  - claim: type-I-phase-clearing-cell-capacity-contract
    role: multi-cell-phase-tree
visibility: public
last_checked: '2026-08-05'
---

# overflow 双通道相位树分裂的精确容量税

## 1. 两条 q 进相位记录

固定一个素数 q，并取 d/r 两个已经通过局部算术账本的缺陷记录：
\[
(h_d,\eta_d),\qquad (h_r,\eta_r),
\]
其中 \(h_d,h_r\ge1\)，且 \(\eta_d,\eta_r\) 是分别模
\(q^{h_d}\)、\(q^{h_r}\) 给出的 q-进单位。取整数代表并令
\[
m=\min(h_d,h_r),\qquad H=\max(h_d,h_r),
\]
\[
c=v_q(\eta_d-\eta_r),
\qquad
s=\min(m,c),
\tag{1}
\]
约定 \(\eta_d=\eta_r\) 时 \(c=+\infty\)。\(s\) 是两条单位相位能够共同满足
嵌套同余的最大深度。

令 \(D_k\) 为高度至少 \(k\) 的两条记录在模 \(q^k\) 下的不同相位残类数。则
\[
\boxed{
D_k=
\begin{cases}
1,&1\le k\le s,\\
2,&s<k\le m,\\
1,&m<k\le H.
\end{cases}}
\tag{2}
\]
第二行为空时取 0。

## 2. 分裂相位树容量上界

假设每条记录都通过一个已证明的整数相位映射得到标签，所有标签落在长度为
\(M\) 的整数区间内；在每一个模 \(q^k\) 相位胞中，标签重复度至多为 \(\mu\)。
则每个胞在第 \(k\) 层至多容纳
\[
C_k=\left\lfloor\frac{M}{q^k}\right\rfloor+1
\]
个不同标签（再乘重复度 \(\mu\)）。由层析恒等式，原始双通道高度满足
\[
\boxed{
h_d+h_r
\le
\mu\left[
\sum_{k=1}^{s}C_k
+2\sum_{k=s+1}^{m}C_k
+\sum_{k=m+1}^{H}C_k
\right].
}
\tag{3}
\]
相对于假定两个通道始终共用一个相位胞的粗界
\[
\mu\sum_{k=1}^{H}C_k,
\]
显式分裂税为
\[
\boxed{
\operatorname{Tax}_q(d,r)
=\mu\sum_{k=s+1}^{m}
\left(\left\lfloor\frac{M}{q^k}\right\rfloor+1\right).
}
\tag{4}
\]
若左端超过 (3)，输出
'DUAL_PHASE_TREE_CAPACITY_DEFICIT'；这表示即使允许每个分裂胞使用其全部
区间容量，也无法同时实现两条 q 进缺陷。

### 证明

在固定层 \(k\)，相同模 \(q^k\) 残类中的两个不同整数相差至少 \(q^k\)，故每个胞
至多有 \(C_k\) 个标签。由 (1)，两单位相位在模 \(q^k\) 相同当且仅当
\(k\le c\)；两条记录同时存在当且仅当 \(k\le m\)，所以胞数正是 (2)。
每个高度 \(h\) 等于其层指标 \(1,\ldots,h\) 的总数，对各层的胞容量求和得到 (3)；
减去单胞基线即得 (4)。证毕。

## 3. 共同前缀去重的类型边界

式 (3) 计数的是两条原始通道债务，默认每条记录的每层都需要一个独立标签。
如果另有一个已证明的 'SHARED_PHASE_PREFIX' 映射，允许同一标签同时支付共同前缀，
则可将前 \(s\) 层去重，得到联合需求
\[
\boxed{
h_{\mathrm{joint}}=h_d+h_r-s.
}
\tag{5}
\]
但 (5) 不能从 \(\eta_d\equiv\eta_r\pmod{q^s}\) 单独推出；还必须证明两个 determinant
标签确实拉回同一个整数来源、标记集和 E1--E5 合同。若该映射没有给出，选择器只能
使用原始账本 (3)，并输出
'DUAL_PHASE_SHARED_PREFIX_UNPROVED'，不得擅自减去 \(s\)。

因此同一输入有三种严格回执：

1. 'DUAL_PHASE_TREE_CAPACITY_DEFICIT'：即使分裂胞完全装箱，(3) 仍超载；
2. 'DUAL_PHASE_SHARED_PREFIX_UNPROVED'：相位有共同前缀，但没有整数去重映射；
3. 'DUAL_PHASE_SPLIT_CAPACITY_BOUND'：容量未超载，保存 \(D_k\)、税 (4) 和后续
   alternate/source-switch 搜索所需的分裂胞。

## 4. 奇 q 和二进特例

若奇 q 同时整除 d、r 且两通道都留下债务，首层分离引理给出
\(s=0\)，所以 \(D_1=2\)，分裂税至少包含
\[
\mu\left(\left\lfloor\frac Mq\right\rfloor+1\right).
\tag{6}
\]
若 q=2，则首层可能相同；前缀深度正是
\[
s_2=\min(h_d,h_r,v_2(\eta_d-\eta_r)),
\]
与上一引理的二进账本一致。

在实际例
\[
(p,M,d,n,A,q^a)=(73,96,23,121,8,2^3)
\]
中 \(h_d=h_r=2\)、\(s_2=1\)，故
\[
D_1=1,\qquad D_2=2,\qquad
\operatorname{Tax}_2=C_2.
\]
这明确说明第二层必须承担两个相位胞的装箱，而非把两侧债务当作同一条高度链。

## 5. 对统一选择器的接口

在 q 不整除 d、r 且两侧标签赋值相同的分支，\(s\) 可以直接由
[overflow 双通道单位相位的 \(2p-r-d\) 精确间隙判据](type-I-overflow-dual-phase-gap-criterion.md)
计算；因此 (3)--(4) 的相位胞和分裂税可以从 \((p,r,d,A)\) 的整数坐标直接生成。

这条引理将双通道 q 账本接到跨状态容量的可计算切割：
\[
\text{双对偶缺陷}
\longrightarrow
(\eta_d,\eta_r,s,D_k,\operatorname{Tax}_q)
\longrightarrow
\text{容量缺口或带分裂胞的候选后继}.
\]
若容量缺口成立，但相位映射来自未证明的 alternate，则输出
'DUAL_PHASE_SOURCE_MAP_OBSTRUCTED'，不能将容量缺口直接称为猜想的反证。若
source-switch、标记集和 E1--E5 已闭合，(3) 的超载才可升级为 Type I/II 短证书或
可提升递降。

该接口还与 outer-rank RESET 兼容：每个分裂胞可以单独尝试固定-\(n\)、固定-\(s\)
或 joined-support rank；成功的胞记录严格势下降，失败的胞保留其 \((h,\eta)\)
并进入 Fourier/广义 \(2^j\) 分支，禁止以另一胞的容量抵销。

## 6. 研究边界

本主张完成了双通道相位分裂的精确层胞计数和容量税，但仍不证明任意 overflow 都有
合法整数相位映射，也不保证容量超载发生。全局闭合仍需从这些分裂胞中构造 alternate、
外层秩递降或 F/G 规范终端；这正是当前统一选择器的剩余存在性问题。
