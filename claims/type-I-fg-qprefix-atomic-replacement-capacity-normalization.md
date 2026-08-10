---
kind: claim
claim_id: type-I-fg-qprefix-atomic-replacement-capacity-normalization
title: prefix-monotone q-prefix assignment 的残余容量替换与局部深度正规化
statement: >-
  对同一请求、同一 typed binding 且深度不减的旧、新 q-prefix assignments，扣除旧
  使用量后的逐资源不等式，是 active base-resource projection 可替换的充要条件；它
  本身不是完整 ledger commit 的充要条件。完整原子提交还须转移 occurrence backpointer，
  在显式有限依赖 DAG 中撤销全部旧后继、逐项验证新派生 receipt，并守恒已花费的不可逆
  effect。partial overlap 本身不是障碍。固定不可变候选菜单摘要后的严格增深替换由
  d_max-d 给出有限同状态正规化势，但不是全局 E5。对 p=557281 的精确孤立单请求快照，
  depth-2 与 depth-3 assignments 只共享 target layers 2,3；基础载荷、owner 与 occurrence
  转移均通过，旧 assignment 的七节点后继闭包可全部重算，且快照明确没有 successor、
  E4、E5 或已花费 price。因此得到 depth 2 到 depth 3 的原子替换证书；active labelled
  prefix-depth 从 (2,0) 更新到 (3,0)，conditional ambient-kernel defect 从 (1,2) 更新到
  (0,2)，局部势从 1 降到 0。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-fg-qprefix-block-bound-first-overflow-terminal
  - type-I-fg-qprefix-depth3-replacement-lineage
  - type-I-fg-qprefix-kernel-depth-neutral-cargo-capacity
  - type-I-raw-certified-q-layer-charge-key-nonreuse
topics:
  - type-I
  - F-state
  - q-prefix
  - occurrence-ledger
  - atomic-replacement
  - residual-capacity
  - owner-map
  - dependency-closure
  - capacity-map
  - well-founded-normalization
  - constructive-certificate
sources:
  - claim: type-I-fg-qprefix-depth3-replacement-lineage
    role: old-new-assignments-and-standalone-depth-three-witness
  - claim: type-I-raw-certified-q-layer-charge-key-nonreuse
    role: one-charge-key-owner-prefix-and-price-nonreuse
  - reproduction: reproductions/type_i_fg_qprefix_atomic_replacement_capacity_normalization.py
    role: residual-load-owner-transfer-and-p557-normalization-certificate
visibility: public
last_checked: '2026-08-10'
---

# prefix-monotone q-prefix assignment 的残余容量替换与局部深度正规化

## 1. active ledger，而不是不可变历史

现有 q-prefix 准入合同对一次普通插入只允许两种情形：全部 occurrence keys fresh，或
同一 assignment 的完整 replay。这个规则正确地拒绝了“旧 assignment 保持 active，
同时再插入一个部分重叠的新 assignment”。它没有判定另一种操作：在一个线性化点上
撤销旧 assignment 的 active 使用量，并以同一请求的新 assignment 取代它。

为把两者分开，令 \(\mathcal X\) 是 occurrence 与 shallow resources 的有限不交并，
每个 \(x\in\mathcal X\) 有容量

\[
b(x)\in\mathbb N.
\tag{1}
\]

assignment \(a\) 的使用向量为

\[
u_a\in\mathbb N^{\mathcal X}.
\tag{2}
\]

若 \(A(\Lambda)\) 是 ledger \(\Lambda\) 的 active assignment 集，定义 active load

\[
L_\Lambda(x)=\sum_{a\in A(\Lambda)}u_a(x).
\tag{3}
\]

有效性要求同一 request id 至多有一个 active assignment，并且

\[
0\le L_\Lambda(x)\le b(x)\qquad(x\in\mathcal X).
\tag{4}
\]

不可变历史可以同时保存旧、新 receipt；只有 active projection (3) 消费容量。
因此 tombstone 不是第二份负载，也不是 replay 许可。

## 2. prefix-monotone 基础资源替换定理

设 \(a^-\in A(\Lambda)\) 是请求 \(r\) 当前唯一 active assignment，\(a^+\) 是同一
请求的完整新 typed assignment，二者深度分别为 \(d^-\)、\(d^+\)。本卡只处理
prefix-monotone 方向

\[
d^+\ge d^-.
\tag{5}
\]

任意降深或无 prefix embedding 的 revoke-and-replace 不在本定理范围内。要求：

1. `expected_epoch` 和 active-set digest 与 \(\Lambda\) 相符，且 \(a^-\) 仍 active；
2. \(a^-\)、\(a^+\) 绑定同一 outer state、request id、target fiber、\(q,J\)、
   Fourier digest、named edge、elementary role 与高阶 phase；source witness、
   canonical base、assignment id 和 lineage id 允许改变；
3. \(a^+\) 独立通过 candidate binding、source map、role、range、owner-prefix 与
   shallow-capacity 等全部局部门；
4. 旧、新 raw atoms 之间有保持相对层 \(r\mapsto r\) 的 injection
   \[
   \iota:\mathcal A^-\hookrightarrow\mathcal A^+,
   \tag{6}
   \]
   且存在 charge rekey \(\theta\)，使两个 owner maps 满足
   \[
   \boxed{\theta\circ\alpha^-=\alpha^+\circ\iota;}
   \tag{7}
   \]
5. 若 \(\beta^-\)、\(\beta^+\) 把 owner token 映到它负责的 occurrence 集，则所有
   shared keys 的 backpointer 沿 \(\theta\) 转移，old-only keys 被删除，new-only keys
   被创建；新 active incidence 中不得再含旧 assignment 或 lineage id；
6. transaction digest 的重复提交是 no-op，tombstoned \(a^-\) 不得再次 replay。

定义外部负载

\[
E(x)=L_\Lambda(x)-u_{a^-}(x).
\tag{8}
\]

**基础资源替换定理。** 在上述身份、typed、owner 与 occurrence 条件下，替换后的
active base-resource projection

\[
A(\Lambda')=(A(\Lambda)\setminus\{a^-\})\cup\{a^+\}
\tag{9}
\]

满足全部基础资源容量，当且仅当

\[
\boxed{
0\le L_\Lambda(x)-u_{a^-}(x)+u_{a^+}(x)\le b(x)
\quad(\forall x\in\mathcal X).}
\tag{10}
\]

此时任何 shared key 都只作 owner transfer：

\[
u_{a^-}(x)=u_{a^+}(x)=1
\Longrightarrow
L_{\Lambda'}(x)=L_\Lambda(x).
\tag{11}
\]

old-only keys 被释放，new-only keys 只按外部负载 (8) 取得容量。请求数与 active
lineage 数均不增加；旧 charge 被撤销，新 charge 只登记一次。若两个 assignments
都是 `UNPRICED`，price 转换仍为 `UNPRICED`，而不是零价格与另一价格的和。

**证明。** 必要性由 (9) 的 active load 逐坐标投影得到 (10)。反过来，在一个
compare-and-swap 线性化点上以 (9) 更新 active projection；式 (10) 逐资源给出 (4)，
所以没有“先释放、被第三方占用、再写入”的中间状态。式 (7) 及 backpointer 条件
保证 shared obligations 沿相同相对层转移，新出现的层由 \(a^+\) 负责，故恰得到一个
有效的 base-resource projection。证毕。

**完整 ledger 提交推论。** 再设 active ledger 有显式有限依赖 DAG，边从依赖项指向
派生项。若从 \(a^-\) 出发的全部后继闭包被撤销，每个新派生节点都以 \(a^+\) 重新计算
并通过自身 validator，全部 derived-resource loads 仍在容量内，且每个已消费不可逆
effect 都有保持语义与总预算的 carry，那么上述基础资源替换可原子提交为有效完整
ledger。反之，任何仍引用旧 id 的 retained 后继、失效的新派生节点、超额派生载荷或
未守恒的不可逆 effect，都会否定完整提交。因而 (10) 单独不能推出完整 ledger 有效。

因此 partial overlap 既不是 all-fresh，也不是 replay，但它也不是数学 no-go；真正的
障碍是 (10)、occurrence 转移、依赖重算或不可逆 effect。

## 3. 为什么 stabilizer 与 price 必须进入闭包

stabilizer 不是 request 的常量。以加法群 \(C_6\) 为严格控制，

\[
D^- =\{0,2\},\qquad D^+=\{0,2,4\}
\tag{12}
\]

分别满足

\[
\operatorname{Stab}(D^-)=\{0\},
\qquad
\operatorname{Stab}(D^+)=\{0,2,4\}.
\tag{13}
\]

所以即使 source/target keys 的替换通过，沿用旧 snapshot 也会在错误的商上收费。
同理，若旧 charge 已支付 Kneser/tower price，则“撤销旧 assignment”不自动撤销已经
用于另一个 active successor 的预算；必须把该 successor 一并 rollback，或给出保持
语义与总预算的 carry map。

本条件不是软件实现偏好，而是不重计定理的必要部分。只检查 (10) 能证明基础资源
可行，不能证明派生价格仍正确。

## 4. 严格增深的局部正规化势

固定 \((p,x,q,J)\) 以及一个不可变有限候选宇宙版本摘要 \(\nu\)。令该版本中通过
全部 typed 局部门的候选集为 \(\mathcal C_\nu\)，并令最大深度为

\[
d_{\max}(\nu)=\max_{a\in\mathcal C_\nu}d(a)
\le v_q(p+4x)-J.
\tag{14}
\]

对 active assignment 定义

\[
\boxed{\mu_{\rm pref}=d_{\max}(\nu)-d_{\rm active}\in\mathbb N.}
\tag{15}
\]

只允许保持同一 \(\nu\)、通过 (10) 且严格增加 depth 的 replacement 作为
normalization rewrite，并禁止 tombstoned assignment 复活或以另一菜单版本重置势，
则每步有

\[
\mu_{\rm pref}'<\mu_{\rm pref}.
\tag{16}
\]

因此这个同状态 preprocessing 有限终止。`ledger_epoch` 不能作势，因为它可在没有
数学进展时增长；\(|K^-\triangle K^+|\) 也不能作势，因为正反替换取值相同。

式 (15)--(16) 不是全局 E5：它不改变方程状态，不提供 marked-solution lift，也不保证
以后跨状态操作不能丢弃这条 q-prefix。它只说明 selector 在进入 successor 分派前可以
把一个有限、隔离且可替换的 request ledger 正规化到最大已证深度。

## 5. \(p=557281\) 的原子替换证书

固定 actual-F request

\[
p=557281,\qquad x=182,\qquad q=3,\qquad J=1,
\tag{17}
\]

旧、新 assignments 分别使用

\[
(s_0^-,s_1^-,D_0^-)=(19838,138866,19838),
\tag{18}
\]

\[
(s_0^+,s_1^+,D_0^+)=(14924,104468,7462).
\tag{19}
\]

前者已有 depth \(2\)，后者已独立证明为保持同一 digest、named edge、初等值 \(1\)
和完整 \(C_9\) phase \(4\) 的 depth \(3\) typed assignment。写

\[
t_j=(\mathsf T,182,3,j),\qquad
u_j=(\mathsf S_-,19838,3,j),\qquad
v_j=(\mathsf S_+,14924,3,j).
\tag{20}
\]

q-layer bundles 为

\[
K_O^- =\{u_2,u_3,t_2,t_3\},
\qquad
K_O^+ =\{v_2,v_3,v_4,t_2,t_3,t_4\}.
\tag{21}
\]

shallow keys 是

\[
h^-=(\mathsf S_-,e_{(2)},138866,19838),\qquad
h^+=(\mathsf S_+,e_{(2)},104468,7462).
\tag{22}
\]

因此完整资源集合满足

\[
K^-\cap K^+=\{t_2,t_3\},
\tag{23}
\]

\[
K^-\setminus K^+=\{u_2,u_3,h^-\},
\qquad
K^+\setminus K^-=\{v_2,v_3,v_4,t_4,h^+\}.
\tag{24}
\]

在只含旧 assignment 的 unit-capacity legacy ledger 中，shared、old-only 与 new-only
三类 keys 的 (10) 分别是

\[
1-1+1=1,\qquad1-1+0=0,\qquad0-0+1=1.
\tag{25}
\]

旧 owner prefix \(r=1,2\) 按 \(r\mapsto r\) 嵌入新 prefix \(r=1,2,3\)，并把旧
charge rekey 到新 charge，所以 (7) 成立。对 shared target keys，旧、新 token 的
occurrence backpointer 相同；提交后的所有 active incidence 都指向新 assignment，
不存在旧 assignment id 的悬空引用。两个积块

\[
B^- =\{1,3,9\},\qquad B^+=\{1,3,9,27\}
\tag{26}
\]

都有

\[
\operatorname{Stab}_{U(728)}(B^-)
=\operatorname{Stab}_{U(728)}(B^+)=\{1\}.
\tag{27}
\]

这里的完整提交只在精确快照 `P557_ISOLATED_SINGLE_REQUEST_LEDGER_V1` 上断言。它的
persistent inputs 恰为 outer state、request、target fiber、exact factor box、\(\eta\)
role、factor target-miss 与 `FIBER_REALIZED=false` gate。旧 assignment 的后继闭包恰含
assignment、lineage、owner prefix、occurrence incidence、kernel section、labelled
depth 和 price status 七个节点。除 lineage 边外，kernel section 还依赖 fiber 与
\(\eta\)，labelled depth 还依赖 factor box 与 \(\eta\)，price status 还依赖 factor
target-miss 与 realization gate。完整 DAG 已验证无环，且从 assignment 出发的后继恰为
这七个节点。快照显式声明 successor、E4、E5、spent-price、derived-resource load 与
irreversible carry 均为空。撤销闭包后，新 assignment 对应的七个节点逐项通过 binding、
lineage、owner、occurrence、kernel、depth 与 price validators，且新 DAG 中不存在旧
assignment id。

固定因子盒严格 target-miss，故两侧均为 `UNPRICED`；在这个精确快照内没有已消费
Kneser/tower price。assignment-specific kernel receipt 在同一闭包内重算为

\[
S_{-1}(B^-)=\{727\}
\longrightarrow
S_{-1}(B^+)=\{701,727\},
\tag{28}
\]

Fourier energy 从 \(95\) 更新为 \(188\)。于是得到构造性证书

\[
\boxed{\texttt{P557\_ISOLATED\_SINGLE\_REQUEST\_Q3\_DEPTH2\_TO\_DEPTH3\_ATOMIC\_REPLACEMENT}.}
\tag{29}
\]

active labelled prefix-depth 与 conditional ambient-kernel defect 原子更新为

\[
c:(2,0)\longrightarrow(3,0),
\qquad
\delta:(1,2)\longrightarrow(0,2).
\tag{30}
\]

令 \(\nu_{557}\) 是验证器对 schema version、\((p,x,q,J,M)\)、四个上游 receipt 的
规范数值 payloads 及本次固定的两候选 normalization menu 作 canonical JSON
serialization 后计算的 SHA-256 摘要。旧、新
assignment nodes 都显式绑定同一 \(\nu_{557}\)；又因 \(v_3(p+4x)=4\)，绝对上界给出
\(d_{\max}(\nu_{557})=4-1=3\)，所以

\[
\boxed{\mu_{\rm pref}:1\longrightarrow0.}
\tag{31}
\]

## 6. 精确边界

式 (29) 只属于 `P557_ISOLATED_SINGLE_REQUEST_LEDGER_V1`。若更大的 ledger 在 new-only
keys 上已有外部负载，必须重新检查 (10)；若旧 receipt 已被 successor、price 或 E5
effect 消费，必须给出完整 rollback/carry closure。不能从本例外推“任何替代
assignment 都可迁移”。

本定理关闭的是此前在这个孤立快照上保留的 scoped blocker
`P557_ISOLATED_SINGLE_REQUEST_ATOMIC_REPLACEMENT_UNPROVED`，并把 active labelled q=3 depth
正规化为三；任意更大的共享 legacy ledger 仍是条件性的。
它不证明 \(83\) neutral cargo 的物理 membership、typed product synthesis、
`FIBER_REALIZED`、E4 或全局 E5，也不把局部势 (31) 当作核心素数递归势。

## 聚焦验证

```bash
python3 reproductions/type_i_fg_qprefix_atomic_replacement_capacity_normalization.py --verify
```

验证器只重算一般 partial-overlap 与 residual-capacity 控制、stabilizer 依赖反例、
\(p=557281\) 的完整 key 分区、owner 与 occurrence 转移、精确依赖 DAG、active load、
kernel section、不可变候选菜单摘要与局部势；
不运行历史测试。
