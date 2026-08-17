---
kind: claim
claim_id: type-II-q-one-full-carrier-phase-root-entry
title: q=1 G 全载体 Type I 根的目标无关 phase-root 准入
statement: >-
  令 S 是一个 ordinary q=1 Type II G endpoint，且其 marked solution set 恰为 Sol(p)，
  p=24t+1。令 X=(p+3)/4，预先定义 R_X=16t+3、K_X=X(16t+1)。则 (R_X,K_X)
  是只依赖 p 的唯一低 full-carrier Type I chart，并有显式 universal raw source
  (p,R_X(p-1)-p,p-1) 到 anchor (1,R_X-1,1)。在只允许 Type II endpoint ->
  full-carrier Type I tree、禁止反向非终端返回的具名 phase policy 中，S 可经
  q_one_full_carrier_phase_root_entry_v1 确定性重索引为 fresh_source_tree_only root T_X；
  E1--E3 由 q=1 G certificate、chart 和 raw source 重放给出，E4 是 Sol(p) 上的恒等
  映射，E5 是 phase 2 -> 1 的严格下降。root 随后无条件执行一个严格 Type I 支撑步：
  t 奇时 A:1->16t+2 的 marked absorb；t 偶时先有显式 overflow，再以 A:1->9t/2 的
  fixed-n identity-lift edge。该结果闭合 ordinary q=1 G 到低 full-carrier Type I tree
  的 target-independent 准入及其首个严格段；它不证明后续 Type I selector 全称、
  非平凡 marked terminal membership、全局 G/Type I exit 或 Erdős--Straus 猜想。
claim_status: established
proof_provenance: repository_derivation
review_status: independent_review
depends_on:
  - type-II-relation-reach-gcd-shadow-endpoint-descent
  - type-II-q-one-type-I-carrier-rail-dispatch
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-overflow-determinant-fixed-n-dual-support-conflict
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - G-state
  - type-I
  - root-entry
  - phase-reindexing
  - universal-source
  - identity-lift
  - well-founded-potential
  - complete-excess
  - proof-boundary
sources:
  - claim: type-II-relation-reach-gcd-shadow-endpoint-descent
    role: ordinary-q-one-G-endpoint-and-Sol-p-semantics
  - claim: type-II-q-one-type-I-carrier-rail-dispatch
    role: unique-low-full-carrier-chart-and-first-dispatch
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: actual-target-side-universal-source
  - claim: type-I-overflow-determinant-fixed-n-dual-support-conflict
    role: even-t-fixed-n-identity-lift
  - concept: denominator-escape-state-contract
    role: E1-to-E5-and-fresh-root-scope
  - reproduction: reproductions/type_ii_q_one_full_carrier_phase_root_entry.py
    role: phase-root-admission-and-first-step-controls
visibility: public
last_checked: '2026-08-17'
---

# q=1 G 全载体 Type I 根的目标无关 phase-root 准入

## 1. 要解决的精确接口

设一个 ordinary Type II endpoint 已经通过 terminal-first 分派而仍需非终端处理，且其
状态为

\[
S=(p,q=1,\mathrm{G};W_S=\operatorname{Sol}(p)),
\qquad p=24t+1.
\tag{1}
\]

令

\[
U=\frac{p-1}{4}=6t,
\qquad X=U+1=\frac{p+3}{4}=6t+1.
\tag{2}
\]

q=1 的模数为 (3)。G 的精确含义是所有实际 source generators 都是 (1\pmod3)，
即每个 (X) 的素因子均为 (1\pmod3)。它只说明 Type II q=1 盒没有目标；不假定
\(\operatorname{Sol}(p)\) 非空。

本卡定义的不是把 Type II 的 raw word 伪装成 Type I raw word，而是一个**同方程、
同解集的有向重索引**。其唯一目标 Type I root 在任何 endpoint source 或 target
factorization 之前就由闭式规则 (mathcal R(p)) 声明，故不落入 universal p-parent 的
target-backward tautology。

## 2. 预声明的 full-carrier root family

对每个核心素数定义

\[
\mathcal R(p)=(R_X,K_X),
\qquad
R_X=16t+3=\frac{8X+1}{3},
\qquad
K_X=X(16t+1).
\tag{3}
\]

不依赖 (S) 的任何 raw node、charged support 或候选 target。已有 carrier rail 恒等式给出

\[
4K_X=pR_X+1,
\qquad
3\le R_X\le p-2,
\qquad
\gcd(X,K_X)=X,
\tag{4}
\]

且在全部低图表内

\[
3\le R\le p-2,
\qquad X\mid K
\Longleftrightarrow (R,K)=(R_X,K_X).
\tag{5}
\]

所以 (mathcal R(p)) 是一个一次性、target-independent 的 root family，而非从任意
Type I node 倒推出来的 p-parent。

它有同样预先定义的实际 source：

\[
(U_X,V_X,m_X)=\bigl(p,R_X(p-1)-p,p-1\bigr),
\tag{6}
\]

其中

\[
U_X+V_X=R_Xm_X,
\qquad (U_X,V_X)=1,
\qquad p\nmid K_X,
\tag{7}
\]

而唯一的 (p)-raw edge（shift (1)，无 gcd reduction）给出

\[
(U_X,V_X,m_X)\longmapsto(1,R_X-1,1).
\tag{8}
\]

式 (6)--(8) 是 target root 的 E1 source/path receipt；它不要求也不声称与 (S) 的
Type II raw word 连续。

## 3. root-only phase reindexing rule

定义具名规则

```text
q_one_full_carrier_phase_root_entry_v1
```

它只接受 (1) 的 ordinary q=1 G state，且只产生

```text
state_origin        = q_one_full_carrier_phase_root_entry_v1
source_tree_scope   = fresh_source_tree_only
normal_form         = type_i_full_carrier_low_root_v1
equation_target     = 4/p
marked_solution_set = Sol(p)
chart               = (p, R_X, K_X)
absorbed_support    = 1
```

规则不能由 `charged_history_only` state 调用，也不能以任意 Type I chart、任意
p-parent 或事后发现的 support 参数化。fresh scope 在后继中原样传播。

为了给它一个可审计的 E5，取下列不可回返的相位前缀：

\[
\operatorname{rank}_{\rm phase}
(\mathrm{Type\ II\ q=1\ G})=2,
\quad
\operatorname{rank}_{\rm phase}
(\mathrm{full\!\!\ carrier\ Type\ I})=1,
\quad
\operatorname{rank}_{\rm phase}
(n<p)=0.
\tag{9}
\]

该 policy 的非终端边只允许

\[
2\longrightarrow1,
\qquad 1\longrightarrow1,
\qquad 1\longrightarrow0;
\tag{10}
\]

在 full-carrier Type I tree 后看到的 Type II 证书只能登记为 terminal leaf，禁止
\(1\to2\) 的非终端 re-entry。它是对未来 selector 的限制，不是假称所有 Type I
边已经构造完毕。

取 (B_p=(p-1)^2/4)，则 handoff 的可扩展势前缀为

\[
\Pi(S)=(2,1,0),
\qquad
\Pi(T_X)=(1,B_p,K_X).
\tag{11}
\]

第一坐标严格下降，故 (10) 下

\[
\Pi(T_X)<\Pi(S).
\tag{12}
\]

## 4. E1--E5 的逐项证明

| 合同 | 可复核回执 |
|---|---|
| E1 | (S) 的 (q=1) G certificate，(3)--(8) 的 predeclared root、source、shift 与 anchor。 |
| E2 | 由 (p) 唯一计算 (t,X,R_X,K_X) 和完整 root state。 |
| E3 | 重算 (4)--(5)、source 正性/互素性、fresh scope、(A=1) 与 state digest。 |
| E4 | (W_S=W_{T_X}=\operatorname{Sol}(p))，所以 (Phi_{T_X\to S}(u)=u) 对每个 (u) 都定义并保持全部 ordinary 标签。 |
| E5 | (9)--(12) 及禁止 (1\to2) nonterminal re-entry 的 policy。 |

因此，这是一条有显式全域 lift 的 phase-reindexing edge。它没有把“同方程”偷换为常值
映射：E4 是在事先声明且完全相同的集合 (operatorname{Sol}(p)) 上的恒等函数，且不读取
任何未知的目标解。

## 5. root 后第一个严格 Type I 段

在 (8) 的 anchor，令

\[
M=R_X-1=16t+2.
\tag{13}
\]

有 (gcd(M,K_X)=1)，故 complete-excess bundle 强制 (A:1\to M)。其后：

\[
\begin{array}{c|c|c|c}
\text{条件}&\text{chart}&\text{新 support}&\text{已有局部 edge}\\ \hline
t\ \text{奇}&(R,K)=(20t+3,(8t+1)(15t+1))&M=16t+2&\text{marked absorb}\\
t\ \text{偶}&(R,K)=(6t-1,\frac{9t}{2}(8t-1))&d=\frac{9t}{2}&\text{fixed-}n\ \text{identity lift}
\end{array}
\tag{14}
\]

偶数行先经过

\[
R_M=52t+7,
\quad n=12t+1,
\quad pn=4M\frac{9t}{2}+1,
\tag{15}
\]

再由固定-(n) 因子图谱到达表中 chart。两行均有 (A_1>1)、(A_1\mid K_1)，所以

\[
\left(1,B_p,K_X\right)
>
\left(1,\left\lfloor\frac{B_p}{A_1}\right\rfloor,\frac{K_1}{A_1}\right).
\tag{16}
\]

故 handoff 之后并非停在一个无支付的 root：它无条件接上一条已具 source/path
provenance、Sol(p) 恒等 lift 和严格 local support potential 的 Type I 边。

## 6. 控制与边界

聚焦 verifier 复算 (p=73,241,2521,118801,76129) 的 q=1 G 端点、root、实际 raw
source、phase potential 和首个 Type I edge；最后一个控制还有

\[
X=19033=7\cdot2719,
\qquad R_X=50755.
\tag{17}

```bash
python3 reproductions/type_ii_q_one_full_carrier_phase_root_entry.py --verify
```

本结果的严格范围是 ordinary q=1 G handoff 的 E1--E5 与首个 local segment。尚未证明：

1. full-carrier Type I tree 的每个后继都有 terminal 或严格边；
2. 非平凡 marked solution set 的 terminal membership；
3. 整个 Type I phase 的全称 selector 与最终 (n<p) 出口。

因此它缩小了 G/Type I 全局出口的接口缺口，但不把 phase policy 的存在或有限控制误称为
全局出口定理。

首个 local segment 之后也不能直接重复 low marked-absorb。其第二 anchor 的完整超额
rechart 在两个 parity branch 都被严格迫入 high overflow；证明见
[q=1 full-carrier 首 child 的第二 anchor 低重图表严格 no-go](type-II-q-one-full-carrier-second-anchor-overflow.md)。
该 high-overflow interface 随后由
[第二 anchor overflow 的固定-\(n\) 严格宏出口](type-II-q-one-full-carrier-second-anchor-fixed-n-macro.md)
给出一条闭式、严格支付的后继；这仍只延长该 q=1 子树，而不等于全域 Type I selector。

## 7. 独立冻结证明包复核

冻结于 `47fedc2` 的独立证明包重新给出本卡的代数推导，并以不导入仓库 module 的 Python
verifier 重放 root、source、E1--E5 shape 与首段公式。其内嵌的本卡、state contract 和
flagship 快照与当前版本逐字一致；审计、完整性 caveat、重放命令和边界见
[q=1 fresh handoff 证明包审计](../docs/q1-fresh-handoff-proof-package-audit-2026-08-17.md)，
完整独立推导见
[q=1 fresh handoff 完整证明](../docs/q1-fresh-handoff-proof-2026-08-17.md)。

这构成 `independent_review`，但不改变本卡的证明范围：有限 scan 和局部 verifier 不替代
ordinary scope、phase policy 或后续 selector 的全称证明。
