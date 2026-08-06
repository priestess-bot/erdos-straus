---
kind: claim
claim_id: type-I-p409-a5-charged-history-parent-replay-boundary
title: p=409, A=5 的 charged-history cofactor 父回放边界
statement: 冻结 selector 中 p=409、A=5 的 generic cofactor r-chart 算术控制不能由现有 verified parent receipt 升格为 parent-to-S 或 parent-to-H 回放：其记录的 H=(409,251,25665;5) 是 raw-source anchor 而非 A=5 的 canonical charged chart，且 parent receipt 为 null；现有 verified-edge 集合中没有以 H 或 S=(409,511,52250;5) 为 successor 的边，registry 也没有已注册 charged-parent adapter。因此该条仅保留为 local cofactor arithmetic / F-fibre evidence。要建立 charged-history bridge，必须另行给出一个具名的 noncanonical-low-anchor adapter，携带精确 verified parent、raw-anchor projection、H-to-S bundle、全状态 scope/hash 连续性和独立 E5 付款；不能由相同的 (p,R,K,A) 数值、fresh A=1 记录或已有 S 出边反推。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-cofactor-r-chart-support
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - r-chart
  - cofactor
  - charged-support
  - source-provenance
  - raw-anchor
  - proof-boundary
sources:
  - reproduction: reproductions/type_i_representation_dual_capacity_selector.py
    role: generic cofactor parent registry, canonical-chart verifier, and frozen fixture construction
  - result: reproductions/type-i-representation-dual-capacity-selector-results.json
    role: p=409 candidate and verified-edge endpoint audit
  - result: reproductions/type-i-universal-anchor-overflow-dual-results.json
    role: raw anchor and complete-excess bundle data
visibility: public
last_checked: '2026-08-06'
---

# p=409, A=5 的 charged-history cofactor 父回放边界

## 1. 已有的局部算术

冻结记录中的 raw anchor、bundle source 与 cofactor 状态分别是

\[
H_{\mathrm{raw}}=(p,R,K;A)=(409,251,25665;5),
\]
\[
S=(409,511,52250;5),\qquad
T=(409,511,52250;1045).
\tag{1}
\]

这里 (H_{\mathrm{raw}}) 只表示 universal raw \(p\)-source 的锚，并不表示一个
以 support \(5\) 规范化的 selector state。其完整超额 bundle 为

\[
R-1=250=Q\beta,\qquad Q=250,\quad\beta=1,
\qquad M=\operatorname{lcm}(5,250)=250.
\tag{2}
\]

故

\[
409\cdot489=4\cdot250\cdot200+1,
\qquad C=409-200=209,
\]
\[
(R_M,K_M)=(511,52250),\qquad 5\mid52250.
\tag{3}
\]

又 \(g=(5,209)=1\)、\(a=5\)、\(r=250\)，所以 \(a\mid r\)，并得到

\[
A_T=\operatorname{lcm}(5,209)=1045,
\qquad C_T=50,\qquad d_T=359,\qquad n_T=3669.
\tag{4}
\]

因此 \(T\) 的 overflow determinant、同图表 F witness
\((-1,0,-2,-1)\)，以及局部势

\[
\left\lfloor\frac{41616}{5}\right\rfloor=8323
\;>\;
39=\left\lfloor\frac{41616}{1045}\right\rfloor
\tag{5}
\]

都是真实的局部事实。这些事实不含 parent reachability。

## 2. H 不能充当现有 canonical 父状态

规范化函数定义为唯一的

\[
1\le R_A<4A,\qquad pR_A+1=4K_A,\qquad A\mid K_A.
\tag{6}
\]

对 \(p=409,A=5\)，直接重算给出

\[
\operatorname{canonical\_chart}(409,5)=(11,1125),
\tag{7}
\]

而非 \((251,25665)\)。特别地，尽管 \(5\mid25665\)，仍有

\[
251\notin[1,20),
\tag{8}
\]

所以 \(H_{\mathrm{raw}}\) 不是 support \(5\) 的 canonical charged chart。
它也不满足 high-anchor 宏所需的 \(p<R\)：此处 \(251<409\)。

这排除了两种不合法的简化：不能把 \(H_{\mathrm{raw}}\) 写作现有 high canonical
宏的 \(H\)，也不能把它作为 `overflow_same_chart_support_promotion_v1` 的 target。
后者只把一个已经 canonical 的 overflow chart 的 support 从其旧值提升至该 chart 的
carrier；它不构造任意 divisor support，更不把 canonical chart \((11,1125)\) 变成
raw anchor \((251,25665)\)。

这也不能靠“换一个 canonical support”修补。由
\(25665=3\cdot5\cdot29\cdot59\) 逐一枚举其 divisors，满足
\(\operatorname{canonical\_chart}(409,A)=(251,25665)\) 的最小 support 是
\(87\)（其余为 \(145,177,295,435,885,1711,5133,8555,25665\)）。但若保留
这个 \(A=87\) 进入同一 complete-excess 规则，(2) 中的 carrier 立即变为

\[
\operatorname{lcm}(87,250)=21750\ne250.
\tag{8a}
\]

故一个 canonical \((251,25665;87)\) state 既不是所需的 charged \(A=5\) anchor，
也不能产生现有的 \(S\)。把 support 从 \(87\) 无凭据地降到 \(5\) 会是一次未支付的
history reset。

## 3. 现有回执的严格缺口

candidate 的 provenance 中保存的是

```text
parent_state = {
  equation_target: [4, 409], R: 251, K: 25665,
  selected_absorbed_support: 5, serialized_anchor_support: 5,
  state_origin: "", state_scope: "",
  charged_support_parent_status: "missing_charged_support_parent",
  charged_support_parent_receipt: null
}
```

这不是一个 edge receipt，也不是完整 selector state。它没有 parent source、edge ID、
adapter/verifier version、E1--E5、typed-fibre certificate、state ID 或可传播的
`source_tree_scope`。

更精确地，现有 `registered_cofactor_charged_parent_replay` 只有在一个已注册的 parent
receipt 直接满足

\[
\mathsf{parent.successor}=S
\tag{9}
\]

时才可能接受；目前它在完成形状检查后仍显式返回 `False`。即使事后塞入一个
\(P\to H_{\mathrm{raw}}\) 的对象，它的 successor 仍不是 cofactor verifier 所需的
\(S\)，因而不是该 v1 adapter 的回放。

对冻结 `type-i-representation-dual-capacity-selector-results.json` 的 endpoint 审计也给出：

\[
\#\{E\in\mathrm{verified\_edges}:\operatorname{succ}(E)=H_{\mathrm{raw}}\}=0,
\]
\[
\#\{E\in\mathrm{verified\_edges}:\operatorname{succ}(E)=S\}=0.
\tag{10}
\]

虽然恰有一条 verified fixed-\(n\) receipt 以 \(S\) 为 **source**，这只表明冻结
overflow atlas 使用 \(S\) 作为输入；它不提供任何到达 \(S\) 的 predecessor。将一条
outgoing edge 倒置为 parent 是方向错误。上游 raw-anchor 文件中所有
`charged_support_parent_receipt` 也均为 `null`。

## 4. 为什么算术端点不能补出历史

相同的 \((p,R,K,A,Q,\beta,M)\) 不决定 selector history：
`source_tree_scope`、typed fibre、parent adapter/version 和 parent digest 都参与
state/edge 的语义身份，但不出现在 (1)--(4) 中。例如同一 raw numeric anchor 的
\(A=1\) 版本只能创建 `fresh_source_tree_only` 根；该 scope 不能被改名为
`charged_history_only` 后用于清除既有 support。反过来，当前 \(A=5\) 记录的 scope
为空，不能由它推断出一个合法 charged-history 祖先。

因此 (5) 的局部下降不等于 E3。它至多说明：**一旦**存在合规的 charged-history
bridge，cofactor 半段可重新使用已有的局部正规形计算；它不能制造该 bridge。

## 5. 最小的新 adapter 合同

若要研究这一条，而不改变旧 generic `S -> T` verifier，最小对象应是一个新的
`noncanonical_low_anchor_charged_history_v1` 宏 adapter：

\[
P\xrightarrow{\text{verified parent}}J
\xRightarrow{\text{raw-anchor projection}}H_{\mathrm{raw}}
\xRightarrow{\text{low-anchor bundle}}S
\xrightarrow{\text{cofactor}}T.
\tag{11}
\]

它至少必须逐项提供并重放：

1. 一张 E1--E5 已验证、方向正确的 \(P\to J\) receipt，以及完整 successor state；
2. 一个具名且确定性的 \(J\Rightarrow H_{\mathrm{raw}}\) projection，说明为何可从
   canonical charged state 进入非 canonical raw-anchor role，且不合成/抹除 scope；
3. 由该精确 \(H_{\mathrm{raw}}\) 重算 (2)--(3) 的 low-anchor bundle，明确其为
   transient construction 而不是普通递归 state；
4. \(J,H_{\mathrm{raw}},S,T\) 的内容摘要、角色标签、scope 传播和逐图表 F/G
   重新分类；
5. 独立的 terminal/alternate menu 与 E5 付款。现有 high-anchor \(\Lambda_p\) 定理
   不能自动支付 (11)，因为此处 raw anchor 既非 canonical 又不满足 \(p<R\)。

在这五项中，第 2 项是本例特有的真正新增数学/语义工作；第 1 项目前也没有冻结
receipt。故当前正确状态是 `analysis_evidence`，而不是 candidate 或 recursive edge。
