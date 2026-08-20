# T6 actual-reachable coverage audit：T2、T3 与 c=8

> 状态：独立审计草稿，2026-08-17。
> 本文没有证明 T6 totality。它只把“当前具名边的实际可达闭包”和“状态合同允许未来加入的
> 一切边”分开，并给出最小剩余量词。

## 1. 审计域

令 \(\mathcal E_{\rm named}\) 为
[`t5-full-transition-taxonomy-v2.json`](../data/t5-full-transition-taxonomy-v2.json) 的
`current_verified_edge_families` 中具有实际构造 claim 的边族。这里不把下列对象算作生成边：

- `legal smaller marked/equation source`：它只是状态合同的 admission class；
- `pending_dispatch`、raw macro checkpoint、standalone stutter；
- generalized-dyadic arithmetic evidence；
- 只有必要同余、Fourier 或商群数据的 candidate。

从 ordinary 根状态 \(W=\operatorname{Sol}(p)\) 出发，对
\(\mathcal E_{\rm named}\) 取保守的全边传递闭包，记为
\(\mathcal R_p^{\rm named}\)。它比某个确定性 selector 只选择一条边所得的可达域更大，
所以在该闭包中成立的不变量也适用于任何当前 selector 子图。

## 2. 当前具名边的 ordinary-mark 闭包

### 命题 1

对每个 \(S\in\mathcal R_p^{\rm named}\)，都有

\[
W_S=\operatorname{Sol}(p).
\]

### 逐行审计

这里的 “concrete generator” 只表示：一旦 claim 写明的 guard 已有可重放 receipt，它会确定构造
target 与 E1--E5。它不表示 guard 对每个状态成立。`guarded` 行不能被计作 T6 totality。

| 当前 persistent edge family | generator status | E4 / mark 处理 |
|---|---|---|
| Type-II proper endpoint descent | guarded；需 proper node | 两端取 \(\operatorname{Sol}(p)\)，恒等 lift |
| Type-II gcd-shadow descent | declared \(q>1\) source 上 total | ordinary 定理两端取 \(\operatorname{Sol}(p)\)，恒等 lift |
| q=1 G full-carrier root entry | ordinary q=1 G source 上 total | source guard 明确要求 \(W=\operatorname{Sol}(p)\)，恒等 lift |
| positive-q G full-carrier root entry | actual ordinary positive-q G source 上 total | source guard 明确要求 \(W=\operatorname{Sol}(p)\)，恒等 lift |
| q=1 G c=3 conditional relay | guarded；需 source-lineage receipt | source guard明确要求 ordinary mark，恒等 lift |
| same-chart support promotion | declared persistent overflow source 上 total | 两端取图表无关 \(\operatorname{Sol}(4,p)\)，恒等 lift |
| joined-support outer reset | guarded；需合法 \(A'\) | 两端取图表无关 \(\operatorname{Sol}(p)\)，恒等 lift |
| A=1 dual reset | declared A=1 overflow source 上 total | 两端取 \(\operatorname{Sol}(p)\)，恒等 lift |
| fixed-n bounded-divisor descent | guarded；需 selector 接受的 \(L\) | 两端取 \(\operatorname{Sol}(p)\)，恒等 lift |
| high-support rank-aware sink bundle | guarded；需 improvement set 非空 | 复用 path-anchored receipt 的 \(\operatorname{Sol}(p)\) 恒等 lift |
| q=1 d=1 relay / regeneration | declared immediate receiver 上 total | 两端取 \(\operatorname{Sol}(p)\)，恒等 lift |
| high-C=2 three-anchor macro | guarded；需 priority miss 与 macro receipts | 所有 chart 取 \(\operatorname{Sol}(p)\)，恒等 lift |
| T2 H4 atomic macro | guarded；需 actual H4 arm | \(W_P=W_T=\operatorname{Sol}(p)\)，恒等 lift |
| T2 c=8 double-low macro | guarded；需 actual double-low | \(W_P=W_T=\operatorname{Sol}(p)\)，恒等 lift |
| legal smaller marked/equation source | contract schema；不是 generator | 没有 E1--E4 source/target receipt |

表中的 \(\operatorname{Sol}(4,p)\) 与其它卡片缩写的 \(\operatorname{Sol}(p)\) 都表示根方程
\(4/p\) 的同一个全解集；前者只是显式写出分子，不引入新的 mark 谓词。

证明只是对路径长度归纳：根的 mark 是 \(\operatorname{Sol}(p)\)；表中每个能实际生成
persistent target 的具名边都保持该 mark；最后一行不能凭状态合同自行生成一条边。终端没有
successor，nonrecursive evidence 也不进入闭包。故结论成立。

### 对 T3 的含义

当前 \(\mathcal R_p^{\rm named}\) 中没有 nontrivial-mark seed。因此
“nontrivial marked terminal membership”不是**当前具名 T6 可达域**的 live state family。
另外，若 Type-II endpoint 已给出直接核验 \(4/p\) 的证书，
[root-context terminal disjunction](../claims/root-context-terminal-disjunctive-invariant.md)
允许它进入根证书分支，不必伪称属于当前 mark。

这不把旗舰 T3 的抽象命题改写为“对任意未来 mark 已证明”。准确结论是：

\[
\boxed{
\text{T3 nontrivial-mark branch is unreachable in the current named graph.}
}
\]

若未来加入 generalized-dyadic、scaled-tail 或其它会创建非平凡 \(W_T\) 的实际边，新增边必须
同时提供有限 mark serializer、非空性和 E4；届时本审计须扩表。不能把一个尚未出现的 future
edge 当作当前 T6 的先决缺口。

## 3. 当前 atomic surface 已由 T2 v1 穷尽

当前 T5 taxonomy 中具名 atomic persistent families 恰为：

1. H4 `a=1` clean-q parent-anchored macro；
2. c=8 double-low parent-anchored conditional macro。

这与
[T2 v1 finite grammar](../claims/type-I-atomic-admission-v1-finite-grammar-integration.md)
的两个 arm 完全相同：

```text
h4_a1_clean_q_atomic_v1
c8_double_low_parent_atomic_v1
```

generic path-anchored atomic schema 只说明“给定一个已经注册的 source/path occurrence 时，怎样
重算 payload 与条件 E1--E4”；它不是第三个 executable arm。raw checkpoint 和 standalone
stutter 又被 taxonomy 明确排除为 nonrecursive surface。

因此可冻结较旗舰“任意 raw legal path”更窄但对当前图足够的结论：

\[
\boxed{
\text{T2 admission is closed on the current named atomic surface.}
}
\]

完整 T2 的开放量词只在 T6 决定调用一个新 atomic arm 时重新成为义务。c=8 是否出现
double-low 是 outgoing-candidate existence，属于 T6；它不是已出现 receipt 的 T2 admission
失败。

## 4. c=8 / \(q_\star=103\) 的精确分派

保留 terminal-first 已 miss 的 ordinary q=1 d=1 parent \(P\)，以及由既有 strict relay
重放出的 c=8 arithmetic checkpoint

\[
H=(p,R,8M;M),\qquad p=48s+1.
\]

实际 \(q_\star=103\) 还要求 rough selection，不只是
\(s\equiv86\pmod {103}\)。在 zero-\(k\)、\((c,j,g)=(8,11,1)\) 与 gap-7
terminal-first residual 中，写 \(s=86+103u\)，必须有

\[
u\equiv1,6\pmod7.
\]

当前出口逐行如下。

| 分支 | 当前处理 | 是否覆盖 |
|---|---|---:|
| parent 或 target terminal-first hit | direct root terminal | 是 |
| actual high-\(q\)，且 \(1\le c_a,c_\Sigma\le7\) | c=8 parent-anchored atomic macro；terminal 或 strict pending target | 是 |
| 上一行中的 zero-carry marker \((D,c,c_\Sigma,\epsilon,g_b)=(1,1,4,0,47)\) | 同一 strict macro 的子例 | 是；无需排除 marker |
| 第二个 full-excess block | 强制 \(c_1>8\)，不能支付当前 capacity E5 | no-go，仅排除该 action |
| 两个 named structured \(m=1\) 节点 | 强制 carry \(>8\)，且尚无独立 E1 source | no-go，仅排除该 action |
| 只使用“存在某个 non-\(p\) V-side raw prime” | 尚不能保证 \(q>2(p-1)\) 或 double-low | 开放 |
| high-\(q\) 但 \(c_a\ge8\) 或 \(c_\Sigma\ge8\) | 当前没有 T5 ticket | 开放 |

这里最容易误判的是 marker。局部 character 与 full-source nonexclusion 说明 marker 的局部条件
彼此相容；但若 marker 真正出现，它已经满足 double-low，并由现有 macro 给出 strict edge。
所以 marker 不是 dead end。真正缺的是一个**全称选择定理**，保证每个 terminal-first-surviving
parent 至少有一个 double-low label，或有另一个 terminal / verified edge。

### 最小剩余量词

令 \(\mathcal Q_V(P)\) 为 checkpoint 的全部 actual V-side excess prime labels。现有结果只给出
\(\mathcal Q_V(P)\setminus\{p\}\ne\varnothing\)。T6 所需而未证明的是：

\[
\boxed{
\operatorname{terminal}(P)
\ \lor
\exists q\in\mathcal Q_V(P):
q>2(p-1),\quad 1\le c_a(q),c_\Sigma(q)\le7
\ \lor
\exists T\;\operatorname{verified\_edge}_{\rm other}(P,T).
}
\]

否定这一析取所需的最小 dead-end receipt 必须同时包含：actual persistent parent、完整
terminal-first miss、真实 \(q_\star=103\) rough receipt、全部 V-side label 的因子分解与逐项
capacity 分类，以及所有其它 registered action 的 miss/rejection。当前仓库没有这样的 receipt。

## 5. 为什么现有数值点不是 dead end

原 c=8 arithmetic control \(p=157393\) 有直接根证书

\[
\frac4{157393}
=\frac1{39375}
+\frac1{57920624}
+\frac1{2280624570000},
\]

所以被 terminal-first 抢占。

进一步，对 frozen necessary predicates 作从 \(u=0\) 开始的精确有限扫描，第一条同时满足

- \(u\equiv1,6\pmod7\)；
- exact \(q_\star=103\) roughness；
- \(p=48s+1\) 为素数；
- \(12s+1\) 的素因子全部为 \(1\pmod3\)

的 arithmetic candidate 是

\[
u=48,\quad s=5030,\quad p=241441,
\]

且

\[
6s-1=103\cdot293,
\qquad
12s+1=7\cdot8623.
\]

但它同样有直接 Type I terminal。取

\[
(A,B,C,H,m)=(468,1,129,5147,47),
\]

则 \(p=4ABC-m\)、\(K=BCH=663963\)，并有

\[
\frac4{241441}
=\frac1{60372}
+\frac1{310734684}
+\frac1{160307890683}.
\]

所以该最小 candidate 也不是 persistent c=8 dead end。有限扫描只用于防止把一个
terminal-preempted control 误报成反例；它不证明后续无限射线全部被抢占。

## 6. 可重放审计

运行：

```bash
python3 reproductions/type_i_t6_actual_reachable_coverage_audit.py --verify
```

脚本检查：

1. 当前 14 个 concrete edge generators 的 ordinary-mark E4 anchor，以及 generic marked 行没有
   concrete generator；
2. 当前 atomic taxonomy 与 T2-v1 两个 arm 精确相等；
3. \(u\le48\) 的最小 residual candidate 和 \(p=241441\) 的直接 Type I identity；
4. \(p=157393\) 的 terminal-preempted identity。

脚本只是防止 taxonomy、claim identity、status 和 E4 anchors 静默漂移；它不以字符串出现代替
上表逐条引用的数学证明。ordinary-mark closure 的证明是前述对 14 张 edge claim 的 E4 检查加
路径长度归纳。

若 taxonomy 新增实际 marked edge 或 atomic arm，脚本会拒绝并要求更新本 coverage audit。

## 7. 审计结论

本审计从当前 T6 live blockers 中删除了两个过宽表述：

- 不需要先证明“任意 future raw path”的完整 T2；当前 named atomic surface 已由 v1 覆盖。
- 不需要为当前可达域处理 nontrivial T3 mark；当前 named edge closure 中没有这种 seed。

仍未关闭的是 c=8 parent 的全称 outgoing-existence，以及 atomic target 后续 F/G、一般
\(A>1\) overflow 和其它 T6 state families。因此准确状态仍是：

```text
T6_GLOBAL_SELECTOR_TOTALITY = OPEN
T2_CURRENT_NAMED_ATOMIC_SURFACE = CLOSED
T3_NONTRIVIAL_MARK_IN_CURRENT_NAMED_REACHABILITY = UNREACHABLE
C8_ACTUAL_PARENT_OUTGOING_TOTALITY = OPEN
```
