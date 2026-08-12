---
kind: claim
claim_id: type-I-path-anchored-atomic-split-complete-excess-admission
title: 双侧完整超额原子来源的条件准入 schema 与精确秩边界
statement: >-
  固定核心素数 p 及一个已入队、内容寻址且带真实 charged support A|K 的合法线性状态
  S=(p,R,K;A)。若一条与 S 绑定的可重放 raw path 到达 primitive node x+y=R，且相对
  K 的唯一完整超额分解 x=Q_x beta_x、y=Q_y beta_y 满足 Q_x,Q_y>1 与
  p 不整除 Q_xQ_y，则可定义新的
  path_anchored_atomic_split_complete_excess_v1 primitive：同一个 path/node occurrence
  只有一个 canonical owner tuple，Q_x,Q_y 是同一 action 内不可拆成两个旧 action 的
  有颜色 payload；这不自动声称跨 action 的全局 one-use。它唯一确定
  M=lcm(A,Q_x,Q_y)、L=M/A 及 canonical target。若 verifier 从 source/path 原样重算
  最大分解、canonical owner、lcm charge、scope 连续性，且项目通用 validator 独立接受
  两端完整 typed state，则该 receipt 条件性满足 E1--E3；两端都用图表无关的 Sol(p)
  标记时，恒等映射给出 E4。这是新 primitive 的条件表示定理，不是 persistent registry
  已实现的声明，也不是由旧单侧 E1/E3 推出的复合定理。完整超额块还有
  无因数分解公式 Q=gcd(v,(v/gcd(v,K))^N)，任取 N>=bit_length(v)，故 maximality 可由
  gcd 和模幂确定性重算。写 B_p=(p-1)^2/4、C=K/A，则该候选在既有
  Lambda_p^sharp 下通过 E5，当且仅当 A<=B_p，或 A>B_p 且
  c_M=<C L^(-1)>_p<C。特别地，高支撑 a=1,d=1 状态中 L!=1 (mod p) 恰通过 E5，
  L=1 (mod p) 恰为 standalone rank stutter；后者不能单独入队，只能保留为 evidence，
  或在从真实 persistent parent 一次重放且最终严格下降的 guarded macro 内作局部
  checkpoint。p=73,r=1
  给出 (0,72)->(0,67) 的严格控制，而 r=50 同时证明非最大分块可伪造 c=12、规范分块
  实为 c=72，且旧 p 进坐标前后同为 0。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-full-product-d-one-a-one-split-carrier-stutter-relay
  - type-I-overflow-full-product-d-one-a-one-two-sided-capacity-tree-no-go
  - type-I-bottom-sink-scc-complete-excess-bundle-selector
  - type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
  - type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
  - denominator-escape-state-contract
topics:
  - type-I
  - path-anchored
  - split-carrier
  - complete-excess-bundle
  - atomic-source
  - source-provenance
  - charged-support
  - solution-lift
  - well-founded-rank
  - carry-stutter
  - factorization-free
  - proof-boundary
sources:
  - claim: type-I-overflow-full-product-d-one-a-one-split-carrier-stutter-relay
    role: colored-source-identity-and-stutter-relay
  - claim: type-I-overflow-full-product-d-one-a-one-two-sided-capacity-tree-no-go
    role: old-single-side-admission-and-noncommutation-boundary
  - claim: type-I-bottom-sink-scc-complete-excess-bundle-selector
    role: complete-excess-and-lcm-support-semantics
  - claim: type-I-overflow-unbounded-same-chart-promotion-persistence-boundary
    role: sharp-parent-to-target-rank
  - claim: type-I-overflow-full-product-d-one-p-adic-regeneration-countdown
    role: existing-p-adic-rank-and-its-domain
  - concept: denominator-escape-state-contract
    role: e1-e5-state-and-lift-contract
  - reproduction: reproductions/type_i_atomic_split_s_zero_endpoint_boundary.py
    role: focused-strict-stutter-maximality-and-rank-controls
visibility: public
last_checked: '2026-08-13'
---

# 双侧完整超额原子来源的条件准入 schema 与精确秩边界

## 1. 定理的地位

本卡把上一张 split-carrier 卡留下的来源想法收敛为一个**条件准入 schema**，而不是声称
persistent registry 或统一 selector 已经实现。第 2 节给出完整超额块的唯一、无因数分解
重算公式；第 3--4 节定义新的、不可拆分双色 primitive，并证明：只要项目的通用
source/target validator 与本 adapter verifier 独立接受完整 receipt，它就满足 E1--E4。
第 6 节给出它通过既有全局秩 E5 的精确门。

所以本卡不声称旧单侧 action 已经可以组合出 split，不用定义性 verifier 清单冒充 E1--E3
的独立实现，也不把 E5 失败的 stutter 登记为边。实际 `verified_edge` 还要求完整 E1--E4
receipt、terminal/alternate priority prefix 全部 miss、E5 通过，并把 target 以
`pending_dispatch` 入队。

## 2. 完整超额块的无因数分解公式

给定正整数 \(v,K\)，令

\[
d=(v,K),\qquad t=\frac vd,
\tag{1}
\]

并取任意 \(N\ge\operatorname{bitlength}(v)\)。这里取
\(\operatorname{bitlength}(1)=1\)。定义

\[
\boxed{Q_K(v)=(v,t^N),\qquad \beta_K(v)=v/Q_K(v).}
\tag{2}
\]

### 引理 1（无因数分解 complete-excess）

式 (2) 精确等于逐素数定义

\[
\boxed{Q_K(v)=\prod_{\nu_q(v)>\nu_q(K)}q^{\nu_q(v)}.}
\tag{3}
\]

**证明。** 写 \(e=\nu_q(v)\)、\(k=\nu_q(K)\)。则

\[
\nu_q(t)=e-\min(e,k)=(e-k)_+.
\tag{4}
\]

若 \(e\le k\)，则 \(q\nmid t\)，故 \(q\) 在 \((v,t^N)\) 中的指数为零。若
\(e>k\)，则 \(\nu_q(t)\ge1\)，而 \(q^e\le v\) 给出
\(e\le\lfloor\log_2v\rfloor<\operatorname{bitlength}(v)\le N\)。于是
\(\nu_q(t^N)\ge e\)，gcd 取回 \(v\) 中完整的 \(q^e\)。逐素数合并即得 (3)。
\(\square\)

实际 verifier 只需计算

\[
(v,t^N)=(v,t^N\bmod v),
\tag{5}
\]

所以只用整数 gcd、`bit_length` 和模幂，不依赖试除或概率素性。因数分解仍可用于状态的
其它字段，但 maximal colored block 本身已有确定性、高效的独立重算式。

## 3. 新的原子双色来源对象

固定核心素数 \(p\equiv1\pmod {24}\) 及已入队、内容寻址的合法线性状态

\[
S=(p,R,K;A,\sigma),\qquad 4K=pR+1,\qquad A\mid K,
\tag{6}
\]

其中 \(\sigma\) 是不可被重置的 `source_tree_scope`。source origin 必须是以下 tagged
union 之一：

1. `charged_history`：含真实 `parent_receipt_digest` 与 `ledger_digest`；
2. `named_fresh_root`：满足项目既有 fresh-root 入口约束，至少含 \(A=1\)、
   `state_origin=universal_raw_default_entry_v1`、
   `source_tree_scope=fresh_source_tree_only` 与 `root_entry_digest`。

两类 tag 及其字段都进入 `state_id`；单有整数四元组不算 persistent source。

设一条与 `S.state_id` 绑定的 raw path \(\pi\) 原样重放到有定向 primitive node

\[
x+y=R,\qquad (x,y)=1.
\tag{7}
\]

按 (2) 唯一定义

\[
x=Q_x\beta_x,\qquad y=Q_y\beta_y,
\tag{8}
\]

并要求

\[
Q_x,Q_y>1,\qquad p\nmid Q_xQ_y.
\tag{9}
\]

由 (7)--(8)，两种颜色支撑不交，且

\[
(Q_x,\beta_x)=(Q_y,\beta_y)=1,
\qquad \beta_x\beta_y\mid K.
\tag{10}
\]

令

\[
M=\operatorname{lcm}(A,Q_x,Q_y),\qquad L=M/A.
\tag{11}
\]

每个 \(q\mid Q_xQ_y\) 都满足
\(\nu_q(Q_i)>\nu_q(K)\ge\nu_q(A)\)，所以

\[
M>A,\qquad L\ge2,\qquad p\nmid M.
\tag{12}
\]

更精确地，charge conservation 是逐素数恒等式

\[
\boxed{
\nu_q(M)-\nu_q(A)
=\mathbf1_{\nu_q(x)>\nu_q(K)}(\nu_q(x)-\nu_q(A))
+\mathbf1_{\nu_q(y)>\nu_q(K)}(\nu_q(y)-\nu_q(A)).}
\tag{13}
\]

因 \((x,y)=1\)，右侧至多一项非零。式 (13) 排除了调用者另传一个希望得到的 \(M\)。

### 3.1 单一 occurrence，而不是两个旧 token

先定义完整的 canonical owner tuple

\[
\operatorname{owner\_tuple}=(
\text{adapter version},\text{source state id},
\text{canonical physical-occurrence digest}).
\tag{14}
\]

其中 physical-occurrence serializer 保存每一步实际选择，却把同一无序 primitive node 的
显示方向规范化；左右颜色另存于 payload frame。相等语义由完整 tuple 决定，
`owner_id=H(owner_tuple)` 只作内容地址，不能用“hash 不碰撞”代替语义唯一性。因此交换
同一物理节点的显示顺序不能产生第二个 owner。一次 action occurrence
必须原子携带两个 payload

\[
(x\text{-side},Q_x,\beta_x),
\qquad(y\text{-side},Q_y,\beta_y),
\tag{15}
\]

并禁止本 action 导出两个单侧 action id。这个结论只保证**一次 atomic action 内不双重
收费**，不自动保证跨 action 或跨宏的全局 one-use。若证明需要后者，则
`owner_fresh`、ledger before/after 与原子 commit 必须成为强制 verifier 字段，且 owner
与 ledger digest 进入 target identity；若证明图不聚合不同出边的容量，则只把 owner
保存在不可变边回执中，不作全局消费声明。

这个新 normal form 命名为
`path_anchored_atomic_split_complete_excess_v1`。它是新的 hyperedge primitive，
不修改旧单侧 `path_anchored_complete_excess_bundle_v1`。

## 4. Canonical target 与 E1--E4 准入

由 (12) 定义唯一 canonical target

\[
c_M=\langle(4M)^{-1}\rangle_p,
\qquad K_M=Mc_M,
\qquad R_M=\frac{4K_M-1}{p}.
\tag{16}
\]

于是

\[
1\le c_M\le p-1,\quad
0<R_M<4M,\quad
R_M\equiv3\pmod4,\quad
4K_M=pR_M+1,\quad
M\mid K_M.
\tag{17}
\]

target 为

\[
T=(p,R_M,K_M;M,\sigma),
\tag{18}
\]

并必须从原始整数重新计算其因数分解、F/G/hit、target fiber、signed defect、normal
form、势和 `state_id`；任何 source chart 的局部分类或缓存都不得继承。

target provenance 按以下无环顺序构造：

1. 先由 source、canonical witness、adapter version 与 (11)--(18) 生成
   edge payload digest；该 payload 不含 target state id、edge receipt id 或最终 parent
   receipt digest；
2. 设置 target origin 为 charged history，令 parent link 由 source state id、adapter
   version 与 edge payload digest 组成，并连同 ledger after、\(\sigma\) 和 target 的
   全部 canonical typed fields 生成 target state id；
3. 最后由 source/target state ids、payload、guard 与 verifier digests 生成 edge
   receipt id。

因此 target 的 parent provenance 进入 state identity，却不引用尚未生成的 edge id。

### 定理 2（原子 split 的条件 E1--E4 表示定理）

若通用 `verify_state` 已独立接受 source 与 target，且具名 adapter verifier 完成下列
重放，则 (6)--(18) 定义的 receipt 满足状态合同的 E1--E4：

| 合同项 | 必须从原始字段重算的内容 |
|---|---|
| E1 | persistent `source_state_id`、上述 origin tagged union、scope、raw source 与每一步 path、(7)、(2)--(3) 的双色 maximality、(9)--(10)；candidate 不得由期望 target 反向生成。 |
| E2 | (11)--(18) 的唯一 lcm charge、canonical target、合法 support，以及通用 validator 已接受的完整 target typed state。 |
| E3 | adapter/verifier/selection-policy version、canonical physical path/occurrence、owner tuple、(13) 的守恒、source/target state hash、同一 scope，以及通用 normal-form validator 的成功回执。 |
| E4 | \(W_S=W_T=\operatorname{Sol}(p)\)，\(\Phi_{T\to S}(u)=u\)。 |

**证明。** 通用 validator 提供两端合法 typed state 与 persistent source provenance。
adapter 的 E1 witness 是从 exact persistent \(S\) 开始的真实 path occurrence；
\(Q_x,Q_y\) 由引理 1 唯一决定，而不是由 target 选择。式 (11)、(13)、(16)--(18)
是 source 与有限 witness 的纯函数，所以在 target validator 成功的前提下给出 E2。
canonical owner tuple、scope、版本、两端 state hash 与通用 validator receipt 使整条
hyperedge 可内容寻址地重放，故给出 E3。这是条件表示证明；它没有凭空构造 repository
尚未注册的 serializer、persistent ledger 或 F/G/hit classifier。

最后，两端方程目标都仍是 \(4/p\)。恒等映射不读取
\(\operatorname{Sol}(p)\) 的任何成员，不预设该集合非空，并对每个输入原样保持三个正
整数分母及单位分数恒等式，所以是全域 E4。F/G/hit 只是两张图表各自重算的
`certificate_context`，不改变这个图表无关标记集。\(\square\)

本 schema 只处理一个已给定的 canonical witness，不自动推出候选菜单有限。selector 若要
排序多个 occurrence，必须另行给出有限、版本化的候选域，或规定 deterministic shortest
simple path 与 tie-break；回执保存 `candidate_menu_digest`。禁止的是先指定 \(M\) 或
\(c_M\)，再反向重分块或寻找 path 来适配它。

## 5. 为什么这不是旧 action 的组合

### 5.1 双色恒等式单独没有来源信息

由 (6)--(10) 总有

\[
4\frac{K}{\beta_x\beta_y}\beta_x\beta_y
=pQ_x\beta_x+pQ_y\beta_y+1.
\tag{19}
\]

但 (19) 只是 \(4K=p(x+y)+1\) 的带颜色重写。若删除 maximality，它不能决定 target。

固定 \(p=73,r=50\) 的真实节点为

\[
x=38\,356\,274=19\,178\,137\cdot2,
\qquad
y=532\,725=177\,575\cdot3.
\tag{20}
\]

规范分解给出

\[
L=3\,405\,557\,677\,775\equiv1\pmod {73},
\qquad c_M=72.
\tag{21}
\]

若错误地取

\[
(Q_x^*,\beta_x^*)=(x,1),
\qquad (Q_y^*,\beta_y^*)=(y,1),
\tag{22}
\]

则 (19)、互素、\(\beta_x^*\beta_y^*\mid K\) 和 \(p\)-free 仍全部成立，却得到

\[
L^*=20\,433\,346\,066\,650\equiv6\pmod {73},
\qquad c_M^*=12.
\tag{23}
\]

原因是 \(2,3\) 的当前层并未超过 \(K\) 容量，必须留在 \(\beta\)。因此 maximal
valuation threshold 是 E1 的数学内容，不是实现细节。

### 5.2 不存在到两个旧单侧 action 的交换分解

若先把 \(x\) 侧剥到 \(h_x=(x,K)\)，另一侧变为

\[
y+h_x(E_x-1),\qquad E_x=x/h_x.
\tag{24}
\]

要保留原 \(Q_y\)，必须有 \(Q_y\mid E_x-1\)，从而 \(Q_y<Q_x\)。反向先处理
\(y\) 又要求 \(Q_x<Q_y\)。两种顺序不可能同时保留原双色 payload。因此一个把新
split 映到两个可独立序列化旧 action 的交换 trace refinement 不存在。动态重算后可能
出现其它真实 path，但那是另一个 occurrence，必须另给回执。

## 6. 精确 E5 边界

令

\[
B_p=\frac{(p-1)^2}{4},
\qquad C=K/A.
\tag{25}
\]

当前 sharp 支撑秩为

\[
\Lambda_p^\sharp(S)
=\left(\left\lfloor\frac{B_p}{A}\right\rfloor,C\right),
\qquad
\Lambda_p^\sharp(T)
=\left(\left\lfloor\frac{B_p}{M}\right\rfloor,c_M\right).
\tag{26}
\]

由 \(M=AL\) 与两张 chart 的模 \(p\) 等式，

\[
4AC\equiv1,\qquad 4ALc_M\equiv1\pmod p,
\]

所以

\[
\boxed{c_M=\langle C L^{-1}\rangle_p.}
\tag{27}
\]

### 定理 3（原子 split candidate 的必要充分 E5 门）

在固定势 (26) 下，候选严格下降当且仅当

\[
\boxed{
A\le B_p
\quad\text{或}\quad
A>B_p\ \text{且}\ c_M<C.}
\tag{28}
\]

**证明。** 由 \(L\ge2\)，若 \(A\le B_p\)，则

\[
\left\lfloor\frac{B_p}{AL}\right\rfloor
<\left\lfloor\frac{B_p}{A}\right\rfloor,
\]

第一坐标严格。若 \(A>B_p\)，两端第一坐标同为零，词典序严格性精确等价于
\(c_M<C\)。\(\square\)

在 \(a=1,d=1\) 高支撑状态中 \(C=p-1\equiv-1\pmod p\)。由 (27)，

\[
\boxed{
L\not\equiv1\pmod p\Longleftrightarrow c_M<p-1,
\qquad
L\equiv1\pmod p\Longleftrightarrow c_M=p-1.}
\tag{29}
\]

所以 (29) 分别是“通过 E5”与 standalone rank stutter 的精确条件，不只是充分条件。
完整边的必要充分条件还包括：E1--E4 receipt 完整、priority prefix 全部 miss，以及 target
带 `pending_dispatch`；若任一 guard 抢占，就不生成该 split edge。

固定 \(p=73,r=1\) 的规范 receipt 给出

\[
(A,R,K)=(195804,772487,14097888),
\]

\[
(Q_x,\beta_x)=(761905,1),
\qquad (Q_y,\beta_y)=(143,74),
\]

\[
M=21\,333\,318\,666\,660,\qquad c_M=67,
\]

故该 candidate 通过 E5：

\[
\Lambda_{73}^\sharp:(0,72)\longmapsto(0,67).
\tag{30}
\]

这是一张新 adapter 的严格算术控制；它不单独证明完整 `verified_edge`，实际入队仍须通过
第 4 节的 persistent/typed-state validator 与 priority verifier。

## 7. Stutter 只能作为 guarded checkpoint

固定 \(p=73,r=50\) 的规范 split 满足 (21)，所以该 schema 的 E1--E4 前提可以同时
满足，而 E5 必失败。已有
\(p\)-进再生坐标也不能普遍补账：source 普通超额 \(E\) 与条件性 split target 的
\(E'\) 在该例满足

\[
\nu_{73}(E-1)=\nu_{73}(E'-1)=0.
\tag{31}
\]

因此旧扩展秩前后都是 \((0,72,0)\)，不能把再生倒计时挪来支付 split 本身。

合法处理方式是把 split target \(U\) 保存为**不入队的 macro-local typed checkpoint**。
它不能作为 standalone persistent source 独立支付 E1。只有一个具名宏 verifier 从原
persistent \(S\) 连续重放 \(S\Rightarrow U\Rightarrow V\)，suffix 提供自己的局部算术、
normal form 与 lift，且宏回执同时满足：

1. \(S,U,V\) 的 state/scope/content hash 连续；
2. source 与 checkpoint 的 terminal/alternate priority prefix 均重放且 miss；
3. 解提升按 \(V\to U\to S\) 全域组合；
4. 真实持久 parent 与 final target 满足
   \(\Lambda_p^\sharp(V)<\Lambda_p^\sharp(S)\)，且 \(V\) 标为 `pending_dispatch`；

才可登记整体 \(S\Rightarrow V\)。E1 由 persistent \(S\) 与整条连续 lineage 支付，不能
把 \(U\to V\) 称为独立 E1 edge；split leg 也不能先伪装成 edge 后再补 E5。stutter 还
可能被 terminal/alternate guard 抢占；否则若没有上述 suffix，只能保持
`analysis_evidence`、`candidate_transition` 或 `internal_checkpoint`。

## 8. 当前证明边界

本卡关闭了双色 arithmetic normal form、条件准入 schema 与精确 E5 门，但没有证明：

- 每个双侧节点都有这样的 \(p\)-free split；
- 每个 split stutter 都有严格 suffix；
- terminal-first 在任意困难状态都 miss；
- 新 adapter 已注册进统一 selector 实现；
- 通用 persistent serializer、F/G/hit classifier 与 ledger 已由本卡实现。

特别地，\(L\equiv1\pmod {p^2}\) 的 \(s=0\) 支仍可能把 endpoint 重新送入
\(p\)-block 容量树。其精确正规形、小 endpoint 出口与固定深度 no-go 见
[s=0 二阶回返、小容量端点出口与固定深度 no-go](type-I-overflow-full-product-d-one-a-one-s-zero-endpoint-boundary.md)。

## 9. 聚焦回执

运行 `python3 reproductions/type_i_atomic_split_s_zero_endpoint_boundary.py --verify`。

脚本只重放 \(p=73,r=1\) 的严格控制、\(r=50\) 的 maximality/stutter 控制及后续
\(s=0\) 定点边界；它使用 (2) 的 gcd/模幂公式，不扫描素数、分母、selector history、
完整证书菜单或历史测试。脚本只支撑 arithmetic/maximality/rank controls；第 4 节是带
通用 validator 前提的表示定理，脚本不伪造 persistent registry、完整 F/G 分类或全局
one-use ledger。
