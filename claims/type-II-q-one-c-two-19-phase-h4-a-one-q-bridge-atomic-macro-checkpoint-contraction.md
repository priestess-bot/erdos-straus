---
kind: claim
claim_id: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-macro-checkpoint-contraction
title: H4 a=1 clean q 原子目标的 parent-anchored checkpoint 收缩宏
statement: >-
  设 P 是一个实际、已持久化的 q=1 high C=2 19-phase parent，并且其固定
  P=>H4 最大第四 anchor 宏、H4 proper-overlap top-capacity a_alt=1 选择和 clean q
  receipt 全部可重放。定义一个只以 P 为 source 的 versioned macro verifier：它重放
  P=>H4 的所有内部 checkpoint，再重放 H4 的 proper-overlap、q-word、双侧最大
  complete-excess payload 与 target 的 terminal-first hit/F/G 分类。直接 Bradford 或
  centered-hit 命中时输出 terminal；否则输出带不变 scope、唯一 macro owner 和完整
  typed fields 的 atomic pending target T。这个 verifier 不把 H4 当作独立入队 source，
  因而实际支付该 a=1 支路的 source/path、scope、owner、target normal form 与
  receipt serialization 的 E1--E4 子义务。并且
  Lambda_p^sharp(P)=(0,p-1)>(0,c_T)=Lambda_p^sharp(T)，因为实际 clean q endpoint
  强制 Q_x,Q_y>1、p 不整除 Q_x Q_y 且 c_T<=p-2。故该分支得到一条
  parent-anchored、phase-local 严格宏；它不声称已给出覆盖所有递归状态的全局势或
  F/G target 的后续出口。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
  - type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
  - type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-interior-terminal-localization
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-single-side-exclusion
  - type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-owner-epoch-locality
  - type-I-path-anchored-atomic-split-complete-excess-admission
  - type-I-path-anchored-atomic-split-total-typed-rechart
  - denominator-escape-state-contract
topics:
  - type-I
  - type-II
  - q-one
  - c-two
  - nineteen-phase
  - fourth-anchor
  - q-bridge
  - atomic-split
  - persistent-macro
  - internal-checkpoint
  - source-provenance
  - terminal-first
  - solution-lift
  - well-founded-rank
  - proof-boundary
sources:
  - claim: type-II-q-one-c-two-19-phase-maximal-fourth-anchor-completion
    role: actual-persistent-P-to-H4-macro-and-parent-rank
  - claim: type-II-q-one-c-two-19-phase-h4-proper-overlap-top-capacity-handoff
    role: actual-a-alt-one-proper-overlap-and-clean-q-entry
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-carrier-clean-raw-bridge
    role: canonical-clean-q-word-and-endpoint-capacity
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-interior-terminal-localization
    role: q-word-internal-full-excess-terminal-localization
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-universal-stutter-source-d-gate-closure
    role: strict-endpoint-capacity
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-single-side-exclusion
    role: forced-two-sided-atomic-payload
  - claim: type-II-q-one-c-two-19-phase-h4-a-one-q-bridge-atomic-owner-epoch-locality
    role: branch-local-owner-and-charge-conservation
  - claim: type-I-path-anchored-atomic-split-total-typed-rechart
    role: finite-terminal-first-target-dispatch
  - reproduction: reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_atomic_macro_checkpoint_contraction.py
    role: focused-suffix-schema-priority-and-provenance-refusal-controls
visibility: public
last_checked: '2026-08-17'
---

# H4 \(a=1\) clean \(q\) 原子目标的 parent-anchored checkpoint 收缩宏

## 1. 新关闭的不是一条裸 H4 边

此前 actual H4 \(a_{\rm alt}=1\) clean \(q\)-bridge 已把全部非终端算术端点
压到

\[
Q_x,Q_y>1,\qquad p\nmid Q_xQ_y,\qquad c_q\le p-2.
\tag{1}
\]

但若把 \(H_4\) 当作一张独立 queued state，仍需单独提供它的 source/state
validator、scope 连续性、terminal-first prefix 与 atomic target serializer。这正是
把一条已知的 parent macro 人为切断后产生的语义空位。

这里不新增一个“裸 H4 source”。相反，令 \(P\) 是已经通过

\[
P\Longrightarrow H_0\Longrightarrow H_1\Longrightarrow H_2
\Longrightarrow H_3\Longrightarrow H_4
\tag{2}
\]

最大第四 anchor 宏的真实 persistent parent。式 (2) 的中间图表都是
macro-local checkpoint；本卡将 H4 proper-overlap、clean \(q\)-word 和 atomic
target 继续附在同一个 \(P\) 上。输出只有 terminal 或新的 typed target \(T\)，
而 \(H_4\) 不要求重新成为独立递归 source。

这是一条受限的 T1 关闭：它处理的正是 actual H4 proper-overlap
\(a_{\rm alt}=1\) 分支，不处理任意 raw Type I path，也不支付全局 selector 的势。

## 2. 输入与固定 terminal policy

宏输入是一个由已知 persistent macro verifier 接受的

\[
P=(p,R_P,K_P;A_P,\sigma),\qquad
\Lambda_p^\sharp(P)=(0,p-1),
\tag{3}
\]

以及其由 (2) 唯一重算的 H4 chart

\[
H_4=(p,R_4,K_4;M_4,\sigma).
\tag{4}
\]

调用只在 H4 proper-overlap selector 的下列分支成立时继续：

\[
c_{\rm alt}=p-1,\qquad a_{\rm alt}=1,\qquad h=(R_4-1,K_4)<p+1.
\tag{5}
\]

令

\[
d_4=\left(\frac{p+1}{2},M_4\right),\qquad
q=\frac{p+1}{2d_4}>1,\qquad
z=R_4-h.
\tag{6}
\]

已有 actual receipt 给出 \(q\mid z\)、\((q,K_4)=1\)，并按 \(q\) 的递增素因子
顺序定义 canonical raw word。其端点为

\[
(x_q,y_q)=\left(R_4-\frac zq,\frac zq\right).
\tag{7}
\]

本宏的 terminal-first policy 是一个固定、有限且可重放的 policy，而不是对所有可能
Egyptian-fraction 公式的虚假穷举：

1. 在 \(p\) 上枚举完整 Bradford Type I/II gap--square-divisor screen；
2. 重放 (2) 中各 checkpoint 已绑定的 versioned terminal/alternate prefix；
3. 重放 H4 proper-overlap selector 中优先于 (5) 的 terminal/strict-macro branches；
4. 检查 q-word 的 registered full-excess sink policy；
5. 构造 atomic target 后执行它的 direct-screen 与 centered hit/F/G dispatch。

第 4 项不需要沿每条 raw edge 额外搜索：clean-word 的任何真前缀都不是 full-excess
sink，端点又满足 \(Q_y>1\)。这是 interior-terminal localization 的精确作用域。
它不排除未来新增的、依赖 raw prefix 的其它 verifier；若将来注册，必须被版本化地加入
本 policy 后才能重用本宏。

## 3. 唯一 atomic target 与 macro-local normal form

由 (7) 的两侧最大 complete-excess 分解定义

\[
Q_x=Q_{K_4}(x_q),\qquad Q_y=Q_{K_4}(y_q).
\tag{8}
\]

式 (1) 使其成为不可拆成两个旧 token 的 atomic payload。定义

\[
A_T=\operatorname{lcm}(M_4,Q_x,Q_y),\qquad
c_T=\left\langle(4A_T)^{-1}\right\rangle_p,
\tag{9}
\]

\[
K_T=A_Tc_T,\qquad R_T=\frac{4K_T-1}{p}.
\tag{10}
\]

这里 \(A_T\) 是完整带指数的 lcm，而不是将 \(Q_x,Q_y\) 视为互素的乘积。
target typed field \(\tau_T\) 由 total rechart 的有限分派唯一给出：

\[
\tau_T\in
\{\text{direct terminal},\ \text{centered-hit terminal},\ \text{F},\ \text{G}\}.
\tag{11}
\]

前两种立即终止。后两种定义 macro 的 pending target

\[
T=(p,R_T,K_T;A_T,\sigma,\tau_T,\mathcal O_{P,H4,q}),
\tag{12}
\]

其 normal form 包含下列全部可重算字段：

\[
\begin{array}{c}
\text{version},\ \operatorname{id}(P),\ \operatorname{digest}(P\Rightarrow H_4),\
(h,z,q,\text{ordered q-word},x_q,y_q),\\
(Q_x,Q_y),\ (A_T,c_T,R_T,K_T),\ \tau_T,\ \sigma .
\end{array}
\tag{13}
\]

macro owner 不是裸 \(H_4\) 的 state id，而是

\[
\boxed{
\mathcal O_{P,H4,q}=
(\texttt{h4\_a1\_atomic\_macro\_v1},
\operatorname{id}(P),
\operatorname{digest}(P\Rightarrow H_4),
\operatorname{digest}(h,z,q,\text{ordered q-word},x_q,y_q)).
}
\tag{14}
\]

其中 \(\sigma\) 原样从 \(P\) 传播到 \(T\)。因此同一个 physical q-word 即使被
显示为不同的 raw-edge 分组，也会先归一为 (6)--(7) 后才计算 owner；反过来，不含
\(\operatorname{id}(P)\) 和前缀 digest 的裸 H4 receipt 一律拒绝，不能借此新建
scope 或在队列中重放同一内部 checkpoint。

## 4. source-bound verifier 与 E1--E4

定义

\[
\texttt{verify\_h4\_a1\_atomic\_macro\_v1}(P,\rho).
\tag{15}
\]

\(\rho\) 是完整 macro receipt，而不是只含 \(H_4\) 坐标的缓存。它按下列确定顺序
重算；任一失败均为拒绝，任一 terminal 均立即返回，不构造 pending target。

1. 验证 persistent \(P\) 及其既有 \(P\Rightarrow H_4\) macro receipt，逐项重建
   \(H_0,\ldots,H_4\)，并检查所有内部 chart 的 scope 都是 \(\sigma\)；
2. 先执行已注册的 Bradford Type I/II screen，再重放前缀中已版本化的 terminal /
   alternate selector；若命中，输出该 terminal；
3. 重算 H4 proper-overlap selector，只有其优先分支均未命中且 (5) 成立时才接受
   clean-q 后缀；随后重算 (6)--(8) 和 canonical raw q-word；
4. 重放 registered q-word full-excess policy，并检查
   \(Q_x,Q_y>1\)、\(p\nmid Q_xQ_y\) 及 \(c_T\le p-2\)；
5. 由 (9)--(13) 重建 target，先运行 direct screen，再运行 total centered
   hit/F/G classifier；direct 或 hit 返回 terminal，F/G 则序列化 \(T\)。

这里的第 1--4 步是特意绑定 source 的：它们不能以单独的 H4 record、已有的
F/G 标签或先前因子分解替代。第 5 步的分类规则只使用重建的 \(K_T,R_T\)，并按
既有 total rechart 的最短再字典序规则选择 F witness 或 G separating character。

所得 macro-relative 回执逐项支付：

| 合同项 | 本宏的可重算内容 |
|---|---|
| E1 | persistent \(P\)、完整 \(P\Rightarrow H_4\) path、(5) 的 selector priority、canonical q-word、两侧 maximal complete-excess payload 及 p-free / positivity / coprimality guards。 |
| E2 | (6)--(10) 重建 \(q,x_q,y_q,Q_x,Q_y,A_T,c_T,K_T,R_T\)，并检查 \(A_T\mid K_T\) 与 \(pR_T+1=4K_T\)。 |
| E3 | (13)--(14) 与重算的 F/G/hit 字段、\(\sigma\)、source id、prefix digest 一起构成唯一 content-addressed macro target；不能继承 H4 的 typed fields。 |
| E4 | 所有 chart 的方程仍为 \(4/p\)，取 \(W_P=W_T=\operatorname{Sol}(p)\)，并显式用 \(\Phi_{T\to P}(u)=u\)。这不读取未知解。 |

因此，F/G 输出是一个已序列化的
\(\texttt{candidate\_transition}\)，而不是尚无来源的 raw arithmetic observation。
它能在未来统一 selector 接受时成为正规递归 target；在此之前，verifier 不把它错误标为
全局 \(\texttt{verified\_edge}\)。

## 5. 真正支付的 endpoint 容量下降

第四 anchor 宏给出

\[
M_4>B_p=\frac{(p-1)^2}{4},
\qquad
\Lambda_p^\sharp(P)=(0,p-1).
\tag{16}
\]

由 (9)，\(M_4\mid A_T\)，因而 \(A_T>B_p\)。clean-q bridge 的 actual
first-stutter closure 与 single-side exclusion 已将所有 live endpoint 压到

\[
1\le c_T=c_q\le p-2.
\tag{17}
\]

所以 macro 的两个真正 endpoint 满足

\[
\Lambda_p^\sharp(T)=(0,c_T)
<
(0,p-1)=\Lambda_p^\sharp(P).
\tag{18}
\]

这也是为何本卡比较 \(P\) 与 \(T\)，而不比较独立入队的 \(H_4\) 与 \(T\)。后者虽有
同样的数值容量不等式，却遗漏了 \(H_4\) 的 source/path 语义；前者同时保留既有
persistent macro 的已收费前缀。

式 (18) 是这个固定 phase 内的完整 E5 receipt。它还不是一个覆盖全部新 state type、
reset 或 selector re-entry 的良基势：若未来允许 \(T\) 进入能无成本返回更大容量的 phase，
单靠 (18) 不能排除循环。

## 6. 组合定理

**定理。** 对每个通过 (15) 的 actual persistent parent \(P\)，H4 proper-overlap
\(a_{\rm alt}=1\) 支路只有以下两种输出：

\[
\boxed{
\text{terminal}
\quad\text{或}\quad
P\Longrightarrow T
\text{ with E1--E4 and phase-local }\
\Lambda_p^\sharp(T)<\Lambda_p^\sharp(P).
}
\tag{19}
\]

**证明。** 第四 anchor completion 使 (2) 的实际前缀可重放，并将其中间 chart 限为
macro-local checkpoints。H4 handoff 在优先 branch 均未命中后给 (5)--(7) 的唯一
clean-q receipt。interior-terminal localization 排除 q-word 内部的 registered
full-excess terminal；first-stutter closure 和 single-side exclusion 给 (17) 所需的
双侧、p-free、严格容量 endpoint。

于是 (8)--(10) 是唯一的 atomic lcm construction，而 owner locality 保证 (14) 在同一
source 上没有竞争 action 或同幂重收费。第 4 节的有限 verifier 分别重建其 source、
construction、normal form 与 identity lift，故 E1--E4 成立。最后 (16)--(18) 给出
严格 endpoint 比较。所有早于 atomic construction 的 terminal 都已被 policy 抢占，
因此不可能同时把一个 terminal 和 F/G successor 记为同一 macro 输出。证毕。

## 7. 边界：没有被本卡偷渡的全局结论

本卡没有证明下列任一更强命题：

1. 每个 H4 selector branch 都属于 \(a_{\rm alt}=1\)；
2. F/G target 已有后续 terminal 或严格 exit；
3. (18) 可与其它 Type I / Type II phase 和 paid reset 合成全局良基势；
4. 一个不带 persistent \(P\) 前缀的 raw H4 fixture 可以被升级为实际递归边。

尤其是，外部局部算术控制若在 root Bradford screen 已直接命中，只说明 verifier 的
terminal-first 行为；它不构造一个实际 19-phase parent。这正是把 source-bound
macro 与无 provenance 的数值样例分开的原因。

## 8. 聚焦复核

~~~bash
PYTHONPATH=reproductions python3 \
  reproductions/type_ii_q_one_c2_19_phase_h4_a_one_q_bridge_atomic_macro_checkpoint_contraction.py --verify
~~~

复现器重放两个 local clean-q suffix control，检查 canonical q-word、atomic lcm target、
严格 capacity 和 direct-terminal priority；同时故意伪造一个缺少 persistent parent 的
receipt，确认 verifier 拒绝它。两个 control 都不是 actual 19-phase parent 的声称，
所以该检查不替代 (15) 对真实前缀的 replay。
