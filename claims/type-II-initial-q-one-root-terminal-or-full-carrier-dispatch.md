---
kind: claim
claim_id: type-II-initial-q-one-root-terminal-or-full-carrier-dispatch
title: 核心素数的规范 q=1 初始根 gap-3 终端--full-carrier 分派
statement: >-
  对每个核心素数 p congruent to 1 modulo 24，令
  X=(p+3)/4。规范初始化器先分解 X，并取最小的素因子 ell congruent to 2 modulo 3。
  若 ell 存在，则 (m,d)=(3,ell) 是可直接核验的 Type II root terminal；若不存在，
  则 q=1、m=3、x=X 是 ordinary Type II G root state，带有由 p 单独决定的
  initialization receipt、在声明的 endpoint-local scope 内完整的 gap-3 terminal miss，
  以及 canonical mod-3 separator。该 receipt 满足既有
  q_one_full_carrier_phase_root_entry_v1 的 ordinary q=1 G algebraic guard，
  但不声称所有根层 direct-certificate families 都已 miss。因而该 G 根有一条
  actual E1--E5 PHASE_DROP 到 target-independent fresh
  full-carrier Type I root。该命题闭合每个核心素数的初始状态 serializer 和首个
  terminal-or-edge dispatch；不证明 handoff 后 Type I totality、global reachable-state
  exhaustion 或 T6 totality。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - gap-three-criterion
  - type-II-p-minus-one-divisor-downset-prime-power-allocation
  - type-II-q-one-full-carrier-phase-root-entry
  - root-context-terminal-disjunctive-invariant
  - denominator-escape-state-contract
topics:
  - type-II
  - q-one
  - initial-state
  - root-serializer
  - terminal-first
  - type-II-terminal
  - G-handoff
  - E1-E5
  - T6
sources:
  - claim: gap-three-criterion
    role: exact gap-3 terminal versus G factorization dichotomy
  - claim: type-II-p-minus-one-divisor-downset-prime-power-allocation
    role: q=1 endpoint-domain legality
  - claim: type-II-q-one-full-carrier-phase-root-entry
    role: G-to-Type-I E1--E5 edge and first strict local segment
  - claim: root-context-terminal-disjunctive-invariant
    role: direct root-terminal result type
  - concept: concepts/denominator-escape-state-contract.md
    role: root-terminal and recursive-edge contracts
  - reproduction: reproductions/type_ii_initial_q_one_root_dispatch.py
    role: deterministic serialization, terminal reconstruction, and G-edge replay
visibility: public
last_checked: '2026-08-18'
---

# 核心素数的规范 \(q=1\) 初始根分派

## 1. 命题的作用域

固定一个核心素数

\[
p=24t+1,
\qquad
U=\frac{p-1}{4}=6t,
\qquad
X=U+1=\frac{p+3}{4}=6t+1.
\tag{1}
\]

这里 \(p\) 是冻结 proof run 的根素数。以下构造的是该 run 的**初始状态**，
不是从一个旧状态制造出来的递归 edge；因此它不伪造一条不存在的 incoming E1 path。
初始 provenance 是由 \(p\) 单独可重放的 `initial_q_one_root_dispatch_v1` receipt。

令

\[
\mathcal N(X)=\{\ell:\ell\mid X,\ \ell\text{ 是素数},\ \ell\equiv2\pmod3\}.
\tag{2}
\]

规范规则为：若 \(\mathcal N(X)\ne\varnothing\)，取其最小元素；若它为空，
构造下述 \(q=1\) G root。因子分解、排序和每个同余检查都只读取有限整数 \(X\)，
所以该规则可计算且不读取任何未知的 Erdős--Straus 分解。

## 2. \(q=1\) 端点的合法性

取

\[
q=1,
\qquad m=4q-1=3,
\qquad x=U+q=X.
\tag{3}
\]

这满足 \(4x=p+m\) 和 \((x,m)=1\)，因为 \(X\equiv1\pmod3\)。它也在
\(p-1\) Type II 的端点允许域内：\(1\mid U\)，而端点函数的定义给出
\(Q(U)\ge1\)，故

\[
1\in\mathcal C_U
=\{q:q\mid U,\ q\le Q(U/q)\}.
\tag{4}
\]

这一步只证明根状态的 normal form 和 endpoint-domain guard；它不是把任意
\(q\mid U\) 宣称为 actual endpoint。

## 3. 终端分支

设 \(\ell=\min\mathcal N(X)\) 存在，并令 \(d=\ell\)。则

\[
d\mid X\mid X^2,
\qquad d\le X,
\qquad X+d\equiv1+2\equiv0\pmod3.
\tag{5}
\]

所以 \((m,d)=(3,\ell)\) 是 Type II 除子证书。其显式分母为

\[
Y=\frac{p(X+d)}3,
\qquad
Z=\frac{p(X+X^2/d)}3.
\tag{6}
\]

第二个分母也是整数：写 \(X=dB\)，则 \(B\equiv2\pmod3\)，从而
\(X+X^2/d=X(1+B)\equiv0\pmod3\)。直接展开或调用短证书恒等式得到

\[
\frac4p=\frac1X+\frac1Y+\frac1Z.
\tag{7}
\]

该回执还满足状态合同的 Type II normal form：取

\[
A=1,
\qquad B=\frac Xd,
\qquad C=d,
\tag{8}
\]

则 \(X=ABC\)、\(d=A^2C\)、\(A\le B\) 且 \(3\mid A+B\)。使用允许的
自然短界 \(H(p)=p-2\) 时，\(3\le p-2\)。因此这是一个
`root_terminal_leaf`；由根证书析取不变量，它直接关闭根方程，不要求把该三元组
错误地证明为某个后续严格 mark 的成员。

## 4. G 分支与稳定序列化

现在设 \(\mathcal N(X)=\varnothing\)。由于 \(3\nmid X\)，\(X\) 的每个素因子
都为 \(1\pmod3\)。故完整源子群在

\[
U(3)=\{1,-1\}
\tag{9}
\]

中恰为 \(\{1\}\)，而目标 \(-1\) 不在其中。于是 (3) 是 ordinary Type II G
endpoint；gap-3 的 Type I/II terminal 也确实不存在，反向方向正是
`gap-three-criterion`。

初始状态固定为

```text
state_origin              = initial_q_one_root_dispatch_v1
root_context              = p
state_scope               = type_ii_endpoint_only
equation_target           = 4/p
marked_solution_set       = Sol(p)
endpoint                  = (q=1, gap=3, first_denominator=X, U)
endpoint_downset_receipt  = (1 | U, 1 <= Q(U))
source_factorization      = factorization(X)
terminal_prefix           = complete_gap_three_direct_I_II_miss
terminal_first_digest     = (scope=q1_gap3_direct_I_II, outcome=miss, complete_within_scope=true)
terminal_scope_boundary   = does_not_assert_all_root_direct_certificate_families
target_fiber.status       = empty
canonical_G_separator     = nontrivial character of U(3)
```

`terminal_first_digest` 的范围是该 \(q=1\) endpoint 的完整 direct Type I/II predicate，
不是一个未经证明的“所有缺口已扫描”断言。它记录的是此 edge 所声明的 endpoint-local
terminal priority，而不是断言根层的每个短证书族都已穷尽。更高层 root scheduler 可以在
调用本 initializer 前加入其它 direct terminal rule；那类 terminal 可以更早结束 proof run，
但一个未被该局部谓词查询的证书不会使已核验的 G edge 失效。

## 5. 从初始 G 根到已有 full-carrier edge

第 4 节的状态给出
`type-II-q-one-full-carrier-phase-root-entry` 所需的 ordinary \(q=1\) G algebraic
source、\(\operatorname{Sol}(p)\) 标记集和声明的 endpoint-local terminal digest；它不把
这个 digest 夸张为根层所有 direct-certificate families 的 miss。该已有定理因此给出唯一的
p-only target

\[
R_X=16t+3,
\qquad
K_X=X(16t+1),
\tag{10}
\]

以及 fresh full-carrier Type I root。对这里的 root source，E1--E5 分别为：

| 项 | 初始分派提供的回执 |
|---|---|
| E1 | 初始 state digest 重放 (1)--(4)、在声明 scope 内完整的 gap-3 miss 与 (9) 的 G separator；已有 handoff 重放 target 的 universal \(p\)-source。初始状态是冻结基例，所以没有被伪造的 incoming raw word。 |
| E2 | 既有 handoff 由 \(p\) 唯一计算 (10) 与 target serialization。 |
| E3 | 既有 handoff 重算 \(4K_X=pR_X+1\)、low-chart guards、fresh scope 和 source digest。 |
| E4 | 两端都是 \(\operatorname{Sol}(p)\)，故 lift 是 \(u\mapsto u\)。 |
| E5 | 既有 `q_one_full_carrier_phase_root_entry_v1` 的 `PHASE_DROP`。 |

所以 G 分支不是仅有数值公式的 control：它的 ordinary source receipt 由这个 p-only
initialization 实际提供。其 target 属于既有 `type_i_full_carrier_post_g` family，并可
继续执行该定理已给出的第一条严格 Type I local edge。

## 6. 初始归纳与边界

令 \(\mathcal R_p\) 的 base construction 为本卡的 canonical initializer。对每个核心
\(p\)，它确定地输出且只输出：

1. 第 3 节的 root terminal；或
2. 第 4--5 节的合法初始 G state 及一条 complete E1--E5 successor。

因此 `initial_core_root` 的 serializer 和首个 terminal-or-edge dispatch 已闭合。
这里采用的是状态合同当前的 scoped terminal-priority 解释：若未来把 `terminal-first`
重定义为“穷尽所有根层 direct-certificate family 后才能走 edge”，则本卡不能自动继承该
更强语义，必须以那份全局 registry 重新审计。当前结论只使用并核验已经声明的
q=1、gap-3 predicate。
这**不**是 O1 的全局 reachable-state exhaustion：第 5 节的 Type I target 后续仍由
`GAP-O1-POST-G-TYPE-I` 覆盖；一般 overflow、high-support、proper-root、c=8 和
atomic target 的量词均未改变。特别地，本卡不将
`T6_GLOBAL_SELECTOR_TOTALITY` 从 `OPEN` 改为其它状态。

## 聚焦复现

```bash
python3 reproductions/type_ii_initial_q_one_root_dispatch.py --verify
python3 -m unittest tests/test_type_ii_initial_q_one_root_dispatch.py
```

控制包含 gap-3 terminal 与 G 两支，并重放 root terminal 的三分母、G separator、
已有 handoff 的 E1--E5 及 T5 `PHASE_DROP`。有限 controls 仅作回归；上面的
素因子二分和既有 full-carrier theorem 承担全称证明。
