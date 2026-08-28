---
kind: claim
claim_id: t6-sp02-finite-constructor-source-completeness
title: SP-02 有限良构模型中的 constructor 穷尽分类与 UNKNOWN 不可达
statement: >-
  对显式给出的有限状态、constructor、witness、solution 关系表，若关系已 canonicalize
  到固定 tie-break 后的输出，selector totality、VerifySol soundness、control 无后继、
  StateChangeRegistry 闭世界和跨 constructor 后继 owner 唯一性均作为良构输入证书成立，
  则首匹配诊断的四个实际输出类互斥且穷尽所有 constructor，并且 UNKNOWN 数为零。
  这是条件有限模型元引理，不是当前仓库 concrete constructor/source completeness 或 F1
  U-A0-01 的闭合证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - t6-f1-reachable-state-closed-world-v1
topics:
  - T6
  - F1
  - SP-02
  - constructor
  - reachable-state
  - finite-model
  - classification
  - proof-boundary
sources:
  - document: docs/standalone-proof-propositions-2026-08-28/SP-02-constructor-source-completeness.md
    role: complete self-contained statement and proof
  - reproduction: reproductions/sp02_constructor_source_completeness.py
    role: independent finite-model verifier and seven negative controls
  - test: tests/test_sp02_constructor_source_completeness.py
    role: focused fixed-point, registry and UNKNOWN controls
visibility: public
last_checked: '2026-08-28'
---

# SP-02 有限良构模型中的 constructor 穷尽分类

## 定理范围

本主张只量化有限集合
\(\mathcal X,\mathcal C,\mathcal W,\mathcal S\) 及其显式关系表。三张输出关系已经是
固定 tie-break 后的 canonical relations；若具体实现保留 raw candidates，必须先提供
可重放的 tie-break，再把选择结果投影为本模型的关系。另有显式有限
\(\mathcal G\subseteq\mathcal C\times\mathcal X\times\mathcal W\times\mathcal X\)，作为
全部 state-changing records 的注册表，并要求它等于 successor 表的并集。这个“没有
\(\mathcal G\) 之外的外部改变”是闭世界假设，不能从被省略的数据中自动发现。

良构条件还包括：terminal 输出绑定到 invocation 和 Legal source，并通过 sound 的
\(\operatorname{VerifySol}\)；successor 输出绑定到 invocation 且 target 合法；control
没有 successor；每个 reachable selector invocation 在 canonical 输出中恰有一个
terminal 或 successor；不同 constructor 不得从 reachable source 产生同一 target。

## 有效分支

令

\[
L(c)\iff\operatorname{LiveDom}(c)\ne\varnothing,\qquad
P(c)\iff\exists(S,w,T)\in\operatorname{Successor}_c,\ S\in\operatorname{LiveDom}(c),
\]

\[
Q(c)\iff\exists(S,w,s)\in\operatorname{Terminal}_c,\ S\in\operatorname{LiveDom}(c),
\qquad
K(c)\iff c\in\mathcal C_{\rm ctl}.
\]

首匹配后的五个有效谓词为

\[
\begin{aligned}
E_{\rm O}&=\neg L,\\
E_{\rm A}&=L\land P,\\
E_{\rm T}&=L\land\neg P\land Q,\\
E_{\rm N}&=L\land\neg P\land\neg Q\land K,\\
E_{\rm U}&=L\land\neg P\land\neg Q\land\neg K.
\end{aligned}
\]

这是布尔分割：

\[
\mathcal C=
E_{\rm O}\mathbin{\dot\cup}E_{\rm A}
\mathbin{\dot\cup}E_{\rm T}
\mathbin{\dot\cup}E_{\rm N}
\mathbin{\dot\cup}E_{\rm U}.
\tag{1}
\]

互斥性来自每个后续分支携带的前序否定；未经前序否定的 raw guards 不必互斥。

## Reach 最小不动点

定义

\[
\operatorname{Post}(A)=
\{T\in\operatorname{Legal}:\exists S\in A,\ c\in\mathcal C_{\rm sel},w,\\
(S,w,T)\in\operatorname{Successor}_c\}.
\]

令 \(A_0=\mathcal R\cap\operatorname{Legal}\)，
\(A_{i+1}=A_i\cup\operatorname{Post}(A_i)\)。有限性使该递增链在至多
\(|\mathcal X|\) 次严格增长后稳定于 \(A_\ast\)。若 \(B\) 也包含根并对 Post 闭合，则
对 \(i\) 归纳有 \(A_i\subseteq B\)，所以 \(A_\ast\subseteq B\)。因此

\[
\boxed{\operatorname{Reach}=A_\ast}.
\tag{2}
\]

按层扫描 successor 邻接表的队列算法与 (2) 相同：每个状态至多入队一次，每条已注册
successor 至多扫描一次。

## UNKNOWN 的精确逻辑边界

定义 constructor-level selector coverage

\[
\mathrm{SC}_{\rm ctor}\iff
\forall c\in\mathcal C_{\rm sel},\quad
L(c)\Rightarrow P(c)\lor Q(c).
\tag{3}
\]

直接由有效分支定义得到

\[
\boxed{E_{\rm U}=\varnothing\Longleftrightarrow\mathrm{SC}_{\rm ctor}}.
\tag{4}
\]

良构条件中的逐调用 selector totality 是 \(\mathrm{SC}_{\rm ctor}\) 的充分条件，并额外提供唯一输出。若
\(E_{\rm U}(c)\) 成立，则 \(L(c)\) 给出 reachable selector invocation，而 totality
必须给出 terminal 或 successor，分别与 \(\neg Q(c)\) 或 \(\neg P(c)\) 矛盾。因此

\[
\boxed{\#\{c:\widehat\Delta(c)=\mathsf{UNKNOWN}\}=0}.
\tag{5}
\]

但 (4) 只说明 constructor-level coverage，不能反过来证明逐调用 selector totality。有限模型
\(\mathcal X=\{r\}\)、一个 selector、一个 reachable invocation、零输出，正是删除
totality 后的 UNKNOWN 反例。

## Owner、control 和复杂度

reachable successor 的调用绑定使其 constructor 有 live source 和 successor，control
条件排除 control owner；跨 constructor 唯一条件给出 owner 至多一个。control 没有
successor，unreachable constructor 的输出若来自 reachable source 会反推出 live source，
故两者都不能扩张 Reach。

设 \(n=|\mathcal X|,m=|\mathcal C|,q=|\mathcal W|,\sigma=|\mathcal S|\)，以及
\(N_I,N_E,N_T,N_V,N_G\) 分别为 Invoke、Successor、Terminal、VerifySol 和
\(\mathcal G\) 的表大小。哈希索引下验证、闭包和分类的精确输入复杂度为

\[
O(n+m+N_I+N_E+N_T+N_V+N_G).
\tag{6}
\]

只有在额外假设 \(\sigma=O(n)\) 且
\(N_V+N_G=O(mqn^2)\) 时，(6) 才可写成题目要求的
\(O(|\mathcal C||\mathcal W||\mathcal X|^2)\)。单独约束 \(N_T\) 不足以推出该粗界。

## 证据与边界

独立标准库 verifier 对完整有限示例得到
\(\operatorname{Reach}=\{r,a\}\)，分类为一个 active producer、一个 terminal-only、
一个 control 和一个 unreachable constructor；七个负控分别拒绝 rogue registry、同调用
双输出、owner 冲突、control successor、selector 无输出、未验证 terminal 和非法 target。
聚焦测试四项全部通过。

该定理的 established 状态只表示上述条件有限模型元引理及其 verifier 已完成。当前
仓库仍未证明 concrete constructor/source 关系表完整、selector totality、全 state-change
闭包或忠实抽象，因此不改变 U-A0-01/U-A0-02/U-A0-03/U-A0-08、F1、F2、F3 或 T6
状态；也不能把 SP-02 当作 active producer、E1--E5、queue 或 F1 closure 证据。
