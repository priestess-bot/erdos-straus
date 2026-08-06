---
kind: claim
claim_id: type-I-high-anchor-direct-c1-finite-menu-exhaustion
title: 高锚点 direct c=1 回返的有限 action 菜单耗尽合同
statement: 对固定的高锚点 charged state \(S=(p,R,K;A)\)，在标准 direct cofactor 域内，算术上 \(h=0,c=1\) 的回返与满足 \(u\mid A\)、\(r=(K/A)u<p\)、\(C=A/u<p\)、\(R<4(K/A)u\) 的除子标签 \(u\) 一一对应，故算术标签至多 \(\tau(A)\) 个。该有限性本身不等于来源/provenance action 有限。若 action registry 在完整 state identity 上冻结为有限集 \(\mathcal A_S\)，且只在其 terminal/alternate 子菜单完成并得到已验证的无进展 c=1 结果后才把 action 记入 exhausted 集 \(E_S\)，则 \(\Xi=(\lfloor B_p/A\rfloor,\Omega(K/A),|\mathcal A_S\setminus E_S|)\) 对允许的非终端边严格下降：普通 direct 或已付款 outer-rank 边先降低前两坐标，c=1 stutter 只降低第三坐标。对 `high_R_path_anchored_bundle_v1`，H1 的完整超额公式唯一确定 \(Q_\ast\)，所以其冻结菜单至多一个 action；H2 的后续性质不足以定义该 singleton。该合同不声称已经为所有其它 adapter 给出有限完整菜单或全局 selector 证明。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-I-high-anchor-three-phase-nonreturn-window
  - type-I-high-anchor-direct-cofactor-lexicographic-rank
  - type-I-high-anchor-cofactor-outer-rank-composition
  - type-I-overflow-cofactor-r-chart-support
  - type-I-fixed-high-anchor-return-one-shot-exhaustion
  - denominator-escape-state-contract
topics:
  - type-I
  - high-carrier
  - r-chart
  - c1-return
  - complete-excess
  - action-menu
  - scheduler
  - well-founded-descent
  - proof-boundary
sources:
  - claim: type-I-high-anchor-three-phase-nonreturn-window
    role: direct cofactor phase identities and the h=0 return normal form
  - claim: type-I-overflow-cofactor-r-chart-support
    role: H1 complete-excess formula, H2 consequences, and the v1 high-R adapter
  - claim: type-I-high-anchor-cofactor-outer-rank-composition
    role: outer Lambda rank to which this card appends only the c=1 coordinate
  - reproduction: reproductions/type_i_high_anchor_direct_c1_finite_menu_exhaustion.py
    role: exact p=97, p=1657, and p=73 boundary replay without selector execution
  - result: reproductions/type-i-high-anchor-direct-c1-finite-menu-exhaustion-results.json
    role: frozen arithmetic labels and H1/H2 action-selection boundary
visibility: public
last_checked: '2026-08-06'
---

# 高锚点 direct c=1 回返的有限 action 菜单耗尽合同

## 1. 作用域：算术自环不是 action 自环

固定核心素数和 charged canonical 高锚点

\[
p\equiv1\pmod {24},\qquad pR+1=4K,\qquad A\mid K,
\qquad p<R<4A.
\tag{1}
\]

令 \(B=K/A\)。一个 direct cofactor 候选有

\[
1\le r,C<p,\qquad A_C=\operatorname{lcm}(A,C)\mid rC,
\tag{2}
\]

并按三相正规形定义

\[
h=\frac{rC-K}{pA},\qquad c=\frac{C}{(A,C)}.
\tag{3}
\]

本卡只处理完整 direct 分支中的零相位回返护栏 \(R<4r\)。它不把一个
\((r,C)\) 整数对自动升级为来源 action：一个 action 还携带 raw source、路径、
complete-excess 选择、父 charged ledger、terminal/alternate 检查及 verifier 版本。
因此，有限的算术标签是有限 action 菜单的必要输入，不能替代后者。

已有 outer-rank 卡已证明：除精确 \(c=1\) 外，允许入队的 direct 或已付款 outer
边会降低

\[
\Lambda_p(S)=\left(
 \Pi_p(A),\ \Omega(K/A)
\right),\qquad
\Pi_p(A)=\left\lfloor\frac{(p-1)^2/4}{A}\right\rfloor.
\tag{4}
\]

本卡不重证该两坐标下降；它只给出 \(\Lambda_p\) 不变时的精确 c=1 合同。

## 2. 精确的 c=1 除子标签分类

定义有限集合

\[
\mathcal U_{\rm arith}(S)=
\left\{
u:\ u\mid A,\quad Bu<p,\quad A/u<p,\quad R<4Bu
\right\}.
\tag{5}
\]

**引理（充要条件）。** 在 (1)--(3) 的 direct 域中，精确零相位回返
\(h=0,c=1\) 与 (5) 中的一个 \(u\) 一一对应；对应关系为

\[
\boxed{r=Bu,\qquad C=A/u.}
\tag{6}
\]

特别地，\(\lvert\mathcal U_{\rm arith}(S)\rvert\le\tau(A)\)。

**证明。** 若 \(h=0,c=1\)，则三相恒等式给出 \(rC=K\)，且 \(c=1\)
等价于 \(C\mid A\)。令 \(u=A/C\)。于是 \(u\mid A\)，且

\[
r=\frac K C=\frac KA\frac AC=Bu.
\tag{7}
\]

direct 域的 \(r,C<p\) 和回返护栏正好给出 (5)。

反过来，取 \(u\in\mathcal U_{\rm arith}(S)\)，并按 (6) 定义 \(r,C\)。则

\[
rC=(Bu)(A/u)=K,\qquad C\mid A,\qquad A_C=A\mid K=rC.
\tag{8}
\]

所以 gate 通过，\(h=0\)、\(c=1\)，并且 (5) 已给出完整 direct 域的大小和回返
护栏。两个构造互逆。证毕。

这里的结论故意只称为 `arithmetic label`：不同来源路径可以产生同一个 \(u\)，
也可以在同一算术 checkpoint 上携带不同的 terminal/alternate 证明能力。

## 3. H1 的 singleton 与 H2 的非唯一边界

### 3.1 `high_R_path_anchored_bundle_v1` 的完整超额 action

对固定的 high-\(R\) raw source/path，H1 的完整超额定义为

\[
Q_\ast=
\prod_{v_q(R-1)>v_q(K)}q^{v_q(R-1)},
\qquad \beta_\ast=\frac{R-1}{Q_\ast}.
\tag{9}
\]

素因子分解唯一，故 \(Q_\ast\) 和 \(\beta_\ast\) 唯一。给定 charged support \(A\)，

\[
M_\ast=\operatorname{lcm}(A,Q_\ast),\qquad
M_\ast\equiv r_\ast\pmod p,\qquad K_{M_\ast}=M_\ast C_\ast
\tag{10}
\]

也全由整数运算确定。因此，在 source/path adapter、其版本及 parent ledger 均已经
固定时，`high_R_path_anchored_bundle_v1` 的注册菜单只能是

\[
\mathcal A^{\rm H1,v1}_S=\varnothing
\quad\text{或}\quad
\{a_\ast\};
\qquad \lvert\mathcal A^{\rm H1,v1}_S\rvert\le1.
\tag{11}
\]

空集表示 adapter 前提、来源回放或已登记的验证器未通过；它不表示不存在其它未登记
的数学路径。

### 3.2 H2 不能替代 H1 的选择规则

H1 推出的 H2 性质可写为以下较弱谓词：对 \(Q\mid R-1\)、
\(\beta=(R-1)/Q\)，有

\[
Q>1,\quad \beta\mid K,\quad (Q,\beta)=1,\quad Q\nmid K,
\quad Q<R,\quad p\nmid Q.
\tag{12}
\]

(12) 不是完整超额的定义，也不唯一确定 \(Q\)。例如

\[
p=73,\quad R=159,\quad K=2902=2\cdot1451,\quad A=1451
\tag{13}
\]

有 \(R-1=2\cdot79\)。H1 给出唯一的

\[
Q_\ast=79,\quad \beta_\ast=2,
\tag{14}
\]

但 \(Q'=158\)、\(\beta'=1\) 也满足 (12)。所以不能用 H2 的检查结果把
`Q'=158` 静默合并到 H1 action，或从 H2 断言 action menu 是 singleton。若未来
H2 类 adapter 想把它登记为 action，必须提供独立的有限枚举/规范 tie-break 和完整
provenance；在此之前它是 `UNRESOLVED_ACTION`，不是 `STUTTER_EXHAUSTED`。

## 4. 冻结 action 状态合同

对一个 arithmetic checkpoint，状态 identity 至少必须包含

```text
arithmetic_state_id = (p, R, K, A, canonical_normal_form_version)
root_entry_digest
source_tree_scope
charged_parent_ledger_digest
adapter_registry_digest
terminal_alternate_menu_digest
action_menu_digest
sorted_action_ids
sorted_exhausted_action_ids
```

`arithmetic_state_id` 中的 \(A\) 不可省略：同一 \((p,R,K)\) 而不同 charged support
可以有不同的 \(c\)、不同 action menu 和不同 \(\Lambda_p\)。
`source_tree_scope=fresh_source_tree_only` 只能由具名 root-entry 创建并沿合法边原样
传播，不能由 charged history 的 c=1 回返重建。

每个 `action_id` 是其规范描述的 hash，至少冻结以下字段：

```text
adapter_name_and_version
canonical_raw_source_and_path_digest
complete_excess_descriptor = (Q, beta, factorization)
carrier_and_cofactor = (M, r, C)
charged_parent_ledger_digest
terminal_alternate_submenu_digest
verifier_version
```

因此同样的 \((r,C)\) 但不同 bundle、raw path 或 terminal capability 不是同一个
action。反过来，已经固定的 action 不能因再次调度而得到新字段。

令 \(\mathcal A_S\) 为进入状态时冻结的有限 action 集，
\(E_S\subseteq\mathcal A_S\) 为已耗尽 action 集，并定义

\[
\sigma(S)=\left|\mathcal A_S\setminus E_S\right|.
\tag{15}
\]

一个 arithmetic c=1 结果只有在下列全部条件完成后才能转为
`STUTTER_EXHAUSTED(a)`：

1. action \(a\) 的来源、gate 和 c=1 等式已由具名 verifier 重算；
2. action 自己冻结的 terminal/alternate 子菜单已完整执行；
3. 没有 terminal 或已验证严格 successor；
4. action 的全部 digest 与当前状态 identity 匹配。

此时只做 \(E_S\leftarrow E_S\cup\{a\}\)，不把它入递归队列，因此
\(\sigma\) 严格下降。`UNRESOLVED_ACTION`、缺少 verifier、未枚举的 alternate 或
未证明的 lift 一律不能进入 \(E_S\)；“已耗尽”只表示冻结菜单内的该 action 已检查，
不表示该算术状态的所有可能证明方式都不存在。

## 5. 有限菜单秩

在第 4 节的冻结前提下定义

\[
\boxed{
\Xi(S)=\left(
\Pi_p(A),\ \Omega(K/A),\ \sigma(S)
\right)
}
\tag{16}
\]

并使用字典序。允许的非终端转移只有三类：

| 类型 | 菜单规则 | \(\Xi\) 的支付 |
| --- | --- | --- |
| 非 c=1 direct \(D\) | target 可冻结新菜单 | 已有三相/outer-rank 论证使 \(\Lambda_p\) 严格下降 |
| 已付款 outer \(O\) | target 可冻结新菜单 | 必须显式有 \(\Pi_p(A_T)<\Pi_p(A_S)\) |
| c=1 stutter | 不得重置或扩张菜单；只耗尽当前 \(a\) | \(\sigma\mapsto\sigma-1\) |

于是每条允许的非终端边都严格降低 \(\Xi\)。特别地，只有在

\[
\Lambda_p(T)<_{\rm lex}\Lambda_p(S)
\tag{17}
\]

时，D/O 才能开启新 epoch、替换 `action_menu_digest` 或把 exhausted 集重置为空。
若一个算术 c=1 回返声称新增 capability、改变 adapter registry、切换 root scope 或
扩大 action menu，而又不满足 (17)，它不属于本图的合法递归边，必须停止为
`UNRESOLVED_ACTION` 或另行证明新的严格势。不能把这种变化藏在 `STUTTER_EXHAUSTED`
之后。

## 6. 可重放控制例

专用复现脚本只重算下列整数，不运行全局 selector。

### 6.1 实际的 c=1 自环：\(p=97\)

\[
p=97,\quad (R,K;A)=(99,2401;2401),\quad
Q_\ast=2,\quad M=4802,
\tag{18}
\]

给出 \(r=C=49\)、\(h=0\)、\(c=1\)。式 (5) 的唯一标签是 \(u=49\)，而
该 arithmetic checkpoint 完全回返。这证明第三坐标不是可选的装饰。

### 6.2 partial excess 的不可静默合并：\(p=1657\)

\[
p=1657,\quad (R,K;A)=(1991,824772;824772),
\quad R-1=2\cdot5\cdot199.
\tag{19}
\]

H1/v1 唯一选择 \(Q_\ast=995\)、\(\beta_\ast=2\)，给出

\[
M=820648140,\quad r=663,\quad C=1244,
\tag{20}
\]

并精确 c=1 回返。然而取 partial \(Q=5\) 也有

\[
M=4123860,\quad r=1244,\quad C=663,
\tag{21}
\]

同样满足 gate、\(h=0,c=1\) 并回到同一算术 state。它却不是 H1/v1 action：此时
\(\beta=398=2\cdot199\nmid K\)。所以算术上可见的 c=1 标签不能替代完整
excess/provenance digest。该 state 的六个 arithmetic 标签为

\[
u\in\{622,663,884,933,1244,1326\}.
\tag{22}
\]

## 7. 明确不声称的内容

本卡没有证明以下任何全称结论：

- H2 或任意 partial-excess 家族已有有限且完整的 action 枚举；
- 每个 `UNRESOLVED_ACTION` 都可终止或可转为严格递降；
- 所有 raw path、fresh root、RESET、跨 \(p\) 或 capability-changing c=1 回返已被
  \(\Xi\) 覆盖；
- 全局 selector 已满足 E1--E5 或 Erd\H{o}s--Straus 猜想已由此关闭。

它的用途是更窄也更严格：在已冻结、已验证的 action 宇宙内，不因同一算术 checkpoint
而错误丢弃新 action，也不因未证明的 action 而伪造一个可下降的 exhausted 标记。
