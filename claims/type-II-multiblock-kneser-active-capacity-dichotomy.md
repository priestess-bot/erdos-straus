---
kind: claim
claim_id: type-II-multiblock-kneser-active-capacity-dichotomy
title: Type II 多私有块的活跃容量—稳定子二分
statement: 设 P=A_0 B_1...B_r、B_i={1,g_i,...,g_i^{e_i}}，T=Stab_H(P)，并令 kappa_i=|B_iT/T|-1。多集合 Kneser 给出 |P| >= |A_0T|+|T| sum_i kappa_i。若目标 t 不在 P，则 sum_i kappa_i <= floor((|H|-1-|A_0T|)/|T|)；g_i 属于 T 的块满足 kappa_i=0 且投影后消失，g_i 不属于 T 的块至少支付一个 T-块增长。该结论把经证明的 q 进 relay 需求转成目标纤维活跃容量；它仍不自动给出算术状态递降。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
- type-II-shared-selector-kneser-target-fiber-terminal
- type-II-private-factor-kneser-growth-stabilizer-bridge
- type-I-fixed-layer-stabilizer-defect-reduction
topics:
- type-II
- multi-block
- Kneser
- active-capacity
- stabilizer
- target-fiber
- q-adic-relay
- proof-program
sources:
- paper: grynkiewicz_marchan_ordaz2009
  locator: Theorem C
  role: multi-set-Kneser-growth-input
- claim: type-II-shared-selector-kneser-target-fiber-terminal
  role: Type-II-target-product-and-defect
- claim: type-II-shared-factor-q-adic-difference-bound
  role: q-adic-relay-demand-source
visibility: public
last_checked: '2026-08-04'
---

# Type II 多私有块的活跃容量—稳定子二分

## 定理

令 \(H\) 为有限阿贝尔群，\(A_0\subseteq H\) 非空，并令

\[
B_i=\{1,g_i,g_i^2,\ldots,g_i^{e_i}\},\qquad
P=A_0B_1\cdots B_r,\qquad T=\operatorname{Stab}_H(P).
\]

定义第 \(i\) 个块相对于最终稳定子的活跃容量

\[
\kappa_i=|B_iT/T|-1
       =\frac{|B_iT|}{|T|}-1.
\]

则多集合 Kneser 不等式给出

\[
\boxed{
|P|\ge |A_0T|+|T|\sum_{i=1}^{r}\kappa_i.}
\tag{1}
\]

因此，若 \(t\in H\) 是目标且 \(t\notin P\)，则

\[
\boxed{
\sum_{i=1}^{r}\kappa_i
\le
\left\lfloor\frac{|H|-1-|A_0T|}{|T|}\right\rfloor.}
\tag{2}
\]

若 \(g_i\in T\)，则 \(B_i\subseteq T\)、\(\kappa_i=0\)，且该块在投影

\[
\pi:H\longrightarrow H/T
\]

后变成单位元；若 \(g_i\notin T\)，则 \(B_iT/T\) 至少有两个元素，故
\(\kappa_i\ge1\)，它至少支付一个 \(T\)-块的目标纤维增长。

特别地，若

\[
|A_0T|+|T|\sum_i\kappa_i\ge |H|,
\tag{3}
\]

则 \(P=H\)，任何 \(t\in H\) 都被命中。式 (2) 是其目标缺失时的严格反命中边界。

## 稳定子商中的精确分解

令

\[
I_T=\{i:g_i\notin T\},\qquad
J_T=\{i:g_i\in T\}.
\]

因为 \(B_i\subseteq T\) 对 \(i\in J_T\)，有精确投影恒等式

\[
\boxed{
\pi(P)=\pi(A_0)\prod_{i\in I_T}\pi(B_i).}
\tag{4}
\]

故未命中状态只有两个可区分的部分：活跃块受 (2) 的有限容量约束；被吸收块从商群
目标中完全消失，剩余问题位于 \(H/T\)。若 \(T\ne H\)，商群阶严格变小；若
\(T=H\)，则 \(P=H\)，属于命中分支。

## q 进 relay 的条件性推论

设某个跨状态 q 进 relay 已经给出非负需求 \(\delta_i\)，并且证明每一项需求必须由
对应目标块的活跃容量支付，即

\[
\delta_i\le \kappa_i
\quad\text{或至少}\quad
\Delta:=\sum_i\delta_i\le\sum_i\kappa_i.
\tag{5}
\]

则目标缺失强制

\[
\Delta\le
\left\lfloor\frac{|H|-1-|A_0T|}{|T|}\right\rfloor.
\tag{6}
\]

若已证明的 q 进需求违反 (6)，则直接得到目标纤维命中；若不违反，则所有满足
\(\kappa_i=0\) 的来源块必须转入 (4) 的稳定子商，不能继续作为原群中的独立容量项。
注意 (5) 是真实整数坐标到残数块的注入假设，不能由 q 进赋值或 Fourier 角色阶自动
推出；这正是当前跨状态证明的待闭合接口。

## 证明

多集合 Kneser 定理对 \(A_0,B_1,\ldots,B_r\) 及最终稳定子 \(T\) 给出

\[
|A_0B_1\cdots B_r|
\ge |A_0T|+\sum_{i=1}^{r}|B_iT|-r|T|.
\]

按 \(\kappa_i=|B_iT|/|T|-1\) 重排，即得 (1)。若 \(t\notin P\)，则
\(|P|\le|H|-1\)，代入 (1) 即得 (2)；若 (3) 成立，由 \(P\subseteq H\) 得
\(P=H\)。

当 \(g_i\in T\) 时，所有 \(g_i^z\) 属于 \(T\)，故 \(B_iT=T\)、\(\kappa_i=0\) 且
\(\pi(B_i)=\{T\}\)。对其余块保留投影，得到 (4)。最后，\(T\ne H\) 时
\(|H/T|<|H|\)，而 \(T=H\) 时非空的 \(T\)-周期集只能是 \(H\) 本身，故得到所述二分。
证毕。

## Type II 失败行的具体解释

在 \(p=33\,011\,449\)、\(m=63\)、\(j=16\) 的联合失败行中，取

\[
A_0=C=\Pi_{63}(E^2),\qquad
B_1=B_2=A=\{1,55\},\qquad
P=CAA.
\]

已有精确枚举给出

\[
|H|=36,\quad |P|=30,\quad |T|=6,\quad
|A_0T|=|CT|=30,\quad 55\in T.
\]

所以 \(\kappa_1=\kappa_2=0\)，而 (2) 的右端为

\[
\left\lfloor\frac{36-1-30}{6}\right\rfloor=0.
\]

这说明该行的 Type II 目标缺失不是由未支付的活跃私有方向造成的：两个私有块均被
稳定子吸收，剩余缺口完全位于 \(H/T\) 的固定碰撞层投影中。若另有一个新的私有块在
同一稳定子下保持活跃，则 (3) 立即给出 \(P=H\) 并命中；否则只能先处理阶为
\(|H/T|=6\) 的商群缺口。

## 限制与下一接口

该定理把“多条私有来源如何支付目标纤维容量”从逐因子叙述提升为一个总预算，但仍
没有证明 q 进需求满足 (5)，也没有把 \(H/T\) 的商群问题自动提升成更小的合法
Erdős--Straus 状态。要完成统一选择器，下一步必须给出真实 alternate/source-switch
恒等式，使 q 进 relay 需求注入 \(\kappa_i\)，或在商群中构造可提升的 Type I/II 证书。
