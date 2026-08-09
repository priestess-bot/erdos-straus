---
kind: claim
claim_id: type-I-overflow-total-cofactor-typed-projection-dispatch
title: 整体余因子 canonical 投影的全域 typed 分派与条件性 E1--E5 准入
statement: >-
  设一个真实入队、内容寻址的 charged state S 绑定 determinant receipt
  pn=4Md+1、M=Ab，并取图表无关标记集 Sol(4,p)。整体余因子折叠的 canonical
  目标中，arithmetic/fiber core 由 (p,A) 唯一决定；含 scope 与 verifier version 的完整
  状态则由新 adapter 内容寻址。中心平方除子谱的 hit/F/G 完备三分可有限地重算
  分类字段：hit 为直接 Type I 终端，F 取规范无界目标见证与 signed defect，
  G 取有限商分离角色。因而在新 adapter 的验证合同下，source 与 target 独立重算、
  scope 原样传播后，恒等映射 Sol(4,p)->Sol(4,p) 给出 E4；结合 determinant
  provenance 条件性支付 E1--E3，结合 t>0 时既有 (floor(B_p/A),K/A) 秩得 E5。
  类型不能从 source 继承：p=73 有严格的
  F->G、G->F 和 F->hit 三种折叠。定理只适用于真实 persistent source；内部
  transient receipt 必须比较 parent->target，p=1201 的已知替代总折叠仍精确返回
  parent，不能登记为递归边。仓库尚无通用 charged-chart normal-form verifier，也未把
  一般 SNF 分离角色和完整 receipt hash 序列化为统一 selector adapter，故本卡证明
  条件性准入定理但不伪称已有全局 `verified_edge`。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-overflow-total-cofactor-canonical-projection-persistence-rank
  - type-I-overflow-cofactor-mod-p-fold-r-descent
  - type-I-general-b-centered-square-spectrum
  - type-I-f-g-fourier-obstruction-certificate
  - type-I-high-anchor-cofactor-macro-e1-e4-admission
  - denominator-escape-state-contract
topics:
  - type-I
  - overflow
  - total-cofactor
  - canonical-projection
  - F-state
  - G-state
  - typed-dispatch
  - solution-lift
  - persistence-gate
  - verified-edge-admission
sources:
  - reproduction: reproductions/type_i_overflow_total_cofactor_typed_projection_dispatch.py
    role: focused-type-change-terminal-and-transient-boundary-controls
visibility: public
last_checked: '2026-08-09'
---

# 整体余因子 canonical 投影的全域 typed 分派与条件性 E1--E5 准入

## 1. 合法 source 与唯一算术 target

固定核心素数 \(p\equiv1\pmod {24}\)。设

\[
S=(p,R_S,K_S;A,\sigma)
\tag{1}
\]

是一个已经通过具名 verifier、内容寻址且实际进入递归队列的合法 charged-chart
和类型；其 `state_class` 必须是 `marked_absorb` 或 `overflow`，不能把
\(R>p\) 的 source 冒充只接受低图表的 `linear_absorbed_support_v1`。这里 \(\sigma\) 是
`source_tree_scope`，并要求 source receipt 精确绑定

\[
pn=4Md+1,\qquad M=Ab,\qquad1\le d<p,
\tag{2}
\]

\[
R_S=4M-n,\qquad K_S=M(p-d),\qquad A\mid K_S.
\tag{3}
\]

状态的 equation target 与标记集为

\[
\texttt{equation\_target}=4/p,
\qquad
W_S=\operatorname{Sol}(4,p).
\tag{4}
\]

令

\[
C_A=\langle(4A)^{-1}\rangle_p,\qquad
K_A=AC_A,\qquad
R_A=\frac{4AC_A-1}{p},
\tag{5}
\]

并定义

\[
d_A=p-C_A,\qquad n_A=4A-R_A.
\tag{6}
\]

已有 canonical 投影定理给出

\[
pR_A+1=4K_A,\qquad
pn_A=4Ad_A+1,\qquad
A\mid K_A,\qquad R_A\equiv3\pmod4.
\tag{7}
\]

所以 \(R_A\ne p\)。目标按 \(R_A<p\) 或 \(R_A>p\) 唯一归入
`marked_absorb` 或 `overflow`，不存在第三种算术 state class。目标的算术/fiber core
只依赖 \((p,A)\)；完整 typed target 还依赖继承的 scope、schema/verifier version，
以及这些字段共同生成的 state ID。这里不能借用一个现成的通用 `normal_form`
verifier：仓库中的 normal form 都是 adapter-specific；本定理要求新 adapter 对 source
和 target 分别定义、重算并验证自己的 normal form。

## 2. 每个 target 都有完备的 typed 三分

分解

\[
K_A=\prod_{i=1}^r q_i^{\nu_i}
\tag{8}
\]

并令

\[
H_A=\langle q_1,\ldots,q_r\rangle\le U(R_A),
\qquad
B_\nu=\prod_i[-\nu_i,\nu_i]\cap\mathbb Z^r.
\tag{9}
\]

由 (7) 有 \((K_A,R_A)=1\)。下列三类互斥且穷尽：

\[
\begin{array}{c|l}
\texttt{hit}
&\exists z\in B_\nu:\ \prod_iq_i^{z_i}\equiv-1\pmod {R_A},\\
\texttt{F}
&-1\in H_A\ \text{但盒内没有目标点},\\
\texttt{G}
&-1\notin H_A.
\end{array}
\tag{10}
\]

`hit` 的盒内见证恢复中心平方除子和直接 Type I 终端。`F` 中，以有限 Cayley 图的
最短路选择 \(\ell_1\) 最小、再字典序最小的无界指数见证；这给出合法
`target_fiber.status=nonempty`，并相对 \(\nu_i\) 重算全局定向的
\(D^-,D^+\)。`G` 中，有限阿贝尔商 \(U(R_A)/H_A\) 的对偶性给出角色

\[
\psi(q_i)=1\quad(1\le i\le r),
\qquad
\psi(-1)\ne1.
\tag{11}
\]

用固定 CRT/SNF 编码按角色阶和相位字典序选择规范分离角色，并记录
`signed_defect.status=not_applicable`。因此 (10)--(11) 是一个有限、确定且对所有
target 有定义的分类器；它不需要假设 target 与 source 类型相同。

同一个分类器还必须重新执行在 source 上。source receipt 中缓存的因子分解、F/G/hit、
见证或角色均不能直接搬到 target。

## 3. E1--E4 typed 投影定理

固定 schema/verifier version (v)，并定义目标状态

\[
T=T_{p,A,\sigma,v}
=(p,R_A,K_A;A,\sigma,v),
\qquad
W_T=\operatorname{Sol}(4,p).
\tag{12}
\]

未来具名 adapter `total_cofactor_typed_projection_v1` 必须执行：

```text
verify persistent source state_id and queued provenance
verify determinant receipt binds (M,d,n,A) to the exact source
recompute source factorization and hit/F/G fields
construct (C_A,R_A,K_A,d_A,n_A)
propagate source_tree_scope without changing it
recompute target factorization and hit/F/G fields
verify adapter-specific source/target normal forms and both content-addressed state IDs
bind all inputs, verifier versions and classification digests into edge_id
```

任一实际回执通过这些检查时，E1--E4 全部成立：

1. **E1** 由作为输入假设的真实 queued `source_state_id`、绑定的 determinant receipt、
   charged support 与原样传播的 \(\sigma\) 支付；determinant 本身不能制造这些字段；
2. **E2** 由 (5)--(7) 的完整 target 构造支付；
3. **E3** 由 source/target 的独立三分、新 adapter 的通用 charged-chart normal-form
   verifier、state/receipt hash 重算支付；该 verifier 是待实现合同，不是现有 helper；
4. **E4** 取
   \[
   \boxed{\Phi_{T\to S}(u)=u:
   \operatorname{Sol}(4,p)\longrightarrow\operatorname{Sol}(4,p).}
   \tag{13}
   \]

式 (13) 保持三个正整数分母和同一方程。F/G/hit 只是 chart-local
`certificate_context`，不限制这个图表无关标记集。若把 \(W\) 改成中心目标纤维或
其它 chart-dependent 子集，(13) 一般不再成立。

terminal-first 分派仍有优先权：若 source 为 `hit`，不应进入本菜单；若 target 为
`hit`，由其盒内见证直接返回 Type I 终端，而不把已经解决的素数继续入队。

## 4. E5 与 persistence 的精确门

写

\[
\frac{K_S}{A}=C_A+pt,\qquad t\in\mathbb N_0.
\tag{14}
\]

则

\[
K_S-K_A=Ap\,t,\qquad R_S-R_A=4A\,t.
\tag{15}
\]

若 \(t=0\)，target 与 source 是同一 canonical state，adapter 必须抑制 stutter。
若 \(t>0\)，且 (1) 确为真实 persistent source，则既有固定 \(p\) 秩

\[
\Lambda_p^\sharp(S)
=\left(
\left\lfloor\frac{(p-1)^2}{4A}\right\rfloor,
\frac{K_S}{A}
\right)
\tag{16}
\]

在本边保持第一坐标并严格降低第二坐标。因此，在只允许既有 paid outer、direct
cofactor 与 support-preserving charged descent 的 scheduler 中，(13) 的 E1--E4
加上 \(t>0\) 完整支付 E5。

内部 determinant receipt 不满足 (1) 的 persistence 假设。此时必须构造真实
parent-to-target 宏，并比较 parent 与 target 的 (16)，不能用 transient-to-target 的
数值差付款。

## 5. 类型继承失败的三个严格控制

以下都是 \(p=73\)、\(t>0\) 的合法严格算术折叠；它们用于证明 target 类型必须重算，
不冒充已有 queued provenance，也不声称这些 source 在 terminal-first scheduler 中实际可达。

| \((A;M,d,n)\) | source \((R,K;A)\) | target \((R,K;A)\) | 类型变化 |
|---|---|---|---|
| \((3;45,15,37)\) | \((143,2610;3)\) | \((11,201;3)\) | F \(\to\) G |
| \((22;220,18,217)\) | \((663,12100;22)\) | \((47,858;22)\) | G \(\to\) F |
| \((5;40,26,57)\) | \((103,1880;5)\) | \((3,55;5)\) | F \(\to\) hit |

首例 target 的 Legendre 角色模 \(11\) 在 \(3,67\) 上平凡、在 \(-1\) 上非平凡。
第二例 source 可由
\((\cdot/3)(\cdot/13)\) 分离，而 target 有无界 F 见证
\((-2,1,-1,0)\)，对应素因子顺序 \((2,3,11,13)\)。第三例 target 有盒内见证
\((-1,0)\)，并直接恢复

\[
\frac4{73}=\frac1{22}+\frac1{110}+\frac1{4015}.
\tag{17}
\]

三例同时排除“只实现 F/hit”与“直接继承 source fiber”两种错误 adapter；但
\(p=73\) 已被更早的终端证书解决，所以它们只是严格的类型变化控制，不是 queued
reachability 证据。

## 6. 已知 transient 返 parent 边界

仓库 \(p=1201\) 的 high-anchor 宏具有 persistent anchor

\[
H=(1839,552160;986)
\tag{18}
\]

与内部 transient determinant

\[
S_{\rm int}=(2873071,862639568;986).
\tag{19}
\]

若在 (19) 上另行尝试总折叠，虽然临时容量为
\(874888\to560\)，target 却精确等于 (18)。所以真实宏端点是

\[
H\longrightarrow H,
\tag{20}
\]

即 stutter，而不是递归下降。这一例证明 `persistence_source_state_id` 是定理假设，
不是可由 determinant 算术自动推出的字段。

## 7. 证明推进与实现边界

本卡消除了“canonical target 可能没有完备 typed 分类或 E4”的数学缺口：对任何真实
queued strict source，(10)--(16) 已给出终端或 E1--E5 的条件性准入模板；只有新 adapter 的
具名回执通过第 3 节合同后，才能成为 verified edge。它没有声称当前统一 selector 已经
注册任意这样的边。生产回执仍须实现一般 CRT/SNF G 分离角色、规范 F 最短见证、
通用 charged-chart normal-form verifier、完整 source/target state hash 和 terminal-first
dispatcher。当前通用 selector 顺序尚无 total-fold 分支，既有 overflow G profile 也未
携带本合同要求的任意分离角色；
聚焦复现器只核验
三种类型变化和 transient persistence 边界。

因此现阶段的准确标签是“全称 adapter 准入定理已建立，统一序列化实现仍待接入”，
不能仅凭本页把旧 `candidate_transition` JSON 批量改写为 `verified_edge`。
