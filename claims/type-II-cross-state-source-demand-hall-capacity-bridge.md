---
kind: claim
claim_id: type-II-cross-state-source-demand-hall-capacity-bridge
title: Type II 跨状态源需求的 Hall q 进容量桥
statement: 将固定纤维顶层秩方向、primary 数字层需求或其它已证明的源需求单位组成请求集，将真实 q-adic 赋值层组成带容量的资源槽，并以 source-switch/SNF/标签合同定义兼容边。请求存在完整匹配时得到不重复收费的跨状态容量映射；不存在完整匹配时，Hall 定理给出一个请求子集及其资源邻域的严格容量缺口，作为 Type II 命中、源不相容或良基递降的分派输入。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-composition-kernel-role-rank-capacity-bridge
  - type-II-source-fiber-multiprimary-digit-terminal
  - type-II-shared-factor-q-adic-difference-bound
  - type-II-source-fiber-shared-q-ledger
topics:
  - type-II
  - cross-state
  - Hall
  - matching
  - q-adic
  - capacity
  - source-switch
  - SNF
  - descent
sources:
  - claim: type-II-composition-kernel-role-rank-capacity-bridge
    role: typed-source-demand
  - claim: type-II-source-fiber-multiprimary-digit-terminal
    role: digit-layer-demand
  - claim: type-II-shared-factor-q-adic-difference-bound
    role: q-adic-resource-slots
  - claim: type-II-source-fiber-shared-q-ledger
    role: repeated-q-deduplication
visibility: public
last_checked: '2026-08-05'
---

# Type II 跨状态源需求的 Hall q 进容量桥

## 1. 请求与资源槽

固定一个核心素数 \(p\) 和有限个参数纤维。把已经由 Fourier、合成列或
多-primary 数字终端证明必须支付的独立单位组成请求集

\[
\mathcal R=\{r_1,\ldots,r_m\}.
\tag{1}
\]

请求可以是：

* 顶层非恒相位角色的一个 \(\ell\)-初等方向；
* \(\mathrm{MULTIPRIMARY\_DIGIT\_DEFICIT}(\nu,k)\) 所需的一个合法层；
* 其它已经给出 source-switch、SNF 和整数回译的 typed 源需求。

对每个奇素数 \(q\)、层数 \(a\ge1\) 和来源状态 \(s\)，若
\(q^a\mid p+4s\)，则 q 进账本提供一个资源槽

\[
c=(s,q,a,\mathrm{label}),
\tag{2}
\]

其容量为一个独立单位；同一 q 的重复来源先按共同 q 账本合并，稳定子吸收层不
创建槽。若一个物理层允许服务 \(w_c>1\) 个独立请求，则将该槽复制为
\(w_c\) 个同类槽，或保留整数容量 \(w_c\)。

## 2. 兼容图

构造二部图

\[
\Gamma=(\mathcal R,\mathcal C;E),
\tag{3}
\]

其中 \(\mathcal C\) 是资源槽集合，边 \((r,c)\in E\) 只有在以下条件全部已证明时
才允许加入：

1. \(r\) 与槽 \(c\) 属于同一个保持参数纤维的 source-switch 状态；
2. \(q^a\) 的真实整数整除、来源标签和 \(B'>A\) 范围条件成立；
3. 若 \(r\) 是外部参数 Fourier 请求，其标签角色通过循环/有限阿贝尔 SNF；
4. 若 q 已在另一请求或状态中使用，重复层符合 shared-q ledger 的去重和差值上界。

因此边集不是“同一个 q 就可共享”的乐观关系，而是一个有限可复核的算术对象。

## 3. Hall 容量定理

把整数容量槽复制后，记 \(N(U)\) 为请求子集 \(U\subseteq\mathcal R\) 的资源邻域。
则存在一个把每个请求分配给不同资源槽的完整匹配，当且仅当

\[
\boxed{
|N(U)|\ge |U|
\qquad\text{对所有 }U\subseteq\mathcal R.
}
\tag{4}
\]

### 证明

这是有限二部图的 Hall 婚配定理。必要性来自匹配中 \(U\) 的不同请求必须落入
\(N(U)\) 的不同槽；充分性由 Hall 定理逐步增广，或等价地由单位容量最大流的
最小割判据得到。证毕。

若使用整数槽容量 \(w_c\)，条件改为

\[
\sum_{c\in N(U)}w_c\ge |U|.
\tag{5}
\]

## 4. 三种 typed 输出

对给定请求集和兼容图，统一选择器按下列三分：

1. **FULL\_MATCH**：满足 (4)，输出一个显式匹配
   \(f:\mathcal R\to\mathcal C\)。每个 q 进层只被收费一次，得到无重复的跨状态
   容量映射；若匹配后的 Kneser 活跃容量超过目标缺口，则直接输出 Type II。
2. **HALL\_DEFICIT**：存在 \(U\subseteq\mathcal R\) 使
   \[
   |U|>|N(U)|.
   \tag{6}
   \]
   该 \(U\) 和 \(N(U)\) 是严格的容量缺口证书；它不能自动称为猜想的反证，
   但迫使 \(U\) 中至少一个请求转向另一条 Type I/II 射线、源秩不一致或良基递降。
3. **EDGE\_OBSTRUCTED**：某个本应参与的边因 SNF、source-switch 或范围条件失败，
   记录最小算术障碍；不得把该请求计入邻域，也不得把空邻域误写成容量超载。

因此 Hall 缺口与 LIFT_OBSTRUCTED 是不同层次的回执：前者表示真实可用资源不足，
后者表示候选边根本不是合法来源。

## 5. 与 q 进层容量的接线

对于同一 q 的有限移位集 \(S\)，第 \(a\) 层可用槽数受

\[
\#\{s\in S:q^a\mid p+4s\}
\le C_a(S,q)
\tag{7}
\]

控制，其中 \(C_a(S,q)\) 是该层最大同余类容量。故任何请求子集 \(U\) 的邻域容量
都可由 shared-factor q-adic difference bound 和共同 q ledger 独立上界。若
\(|U|>|N(U)|\)，即使把所有合法边都纳入，也无法通过 q 进层支付该请求子集。

对于顶层核角色，请求首先按上一引理产生一个 \(\ell\)-初等方向；对于
MULTIPRIMARY_DIGIT_DEFICIT，则请求带有明确的 \((\nu,k)\) 层标签。这样 Hall
图同时保留角色类型、primary 层和 q 进来源，不把不同 primary 或不同参数纤维
直接池化。

## 6. 小型边界样例

### 完整匹配

有两个请求 \(r_1,r_2\) 和两个兼容槽
\(c_1,c_2\)，边为
\(r_1\!-\!c_1\)、\(r_2\!-\!c_2\)。所有请求子集满足 (4)，匹配
\(f(r_i)=c_i\) 是显式无重复收费证书。

### Hall 缺口

若两个请求都只能连接同一个槽 \(c_1\)，则
\(U=\{r_1,r_2\}\)、\(N(U)=\{c_1\}\)，
\(|U|-|N(U)|=1\)。这正是“两个状态要求同一 q 层但 shared ledger 只有一份”
的最小严格缺口；它应转交另一射线、SOURCE_RANK_INCONSISTENT 或递降，而不是
把同一层重复计算两次。

### \(p=433\) 的 q 进紧边界

取两条移位 \(S=\{16,100\}\)、\(q=7\)。已有逐层账本为

\[
C_1(S,7)=2,\qquad C_2(S,7)=1,
\]

而实际赋值为
\[
v_7(433+4\cdot16)=1,\qquad
v_7(433+4\cdot100)=2.
\]

若反事实地要求两个状态都支付 \(7^2\)，则第二层请求子集有两个元素，而第二层
资源邻域只有一个槽，Hall 缺口为 \(1\)。实际高度 \((1,2)\) 恰好用两个第一层
槽和一个第二层槽完成匹配，说明逐层容量等式与 Hall 完整匹配同时达到紧边界。

## 研究边界

Hall 桥把跨状态 q 进容量从总高度比较推进为带来源、带竞争的有限匹配问题，并能
输出显式匹配或严格缺口子集。它仍不证明当前所有 Fourier/数字需求都有合法兼容边；
真正闭合全局选择器还需证明：每个未命中状态的请求都能进入该图，且
FULL_MATCH 的剩余缺口或 HALL_DEFICIT 能转成 Type II 命中、SNF/源秩障碍或严格
良基递降。
