---
kind: claim
claim_id: type-II-positive-q-G-full-carrier-phase-root-entry
title: ordinary positive-q G 到全载体 Type I 根的全称 phase-root 准入
statement: >-
  令 p=24t+1 为核心素数，q>1 属于 p-1 Type II 的端点允许下闭域，并令
  m=4q-1、x=(p+m)/4=(p-1)/4+q。任取一份 terminal-first 后实际存活的
  ordinary G endpoint state S，其 marked solution set 恰为 Sol(p)，且其
  G-empty certificate 按完整源子群重算。则不需要把 Type-II raw word 延续到
  Type I，也不需要先把 q 降到 1：由 p 单独预声明的 full-carrier root
  X=(p+3)/4、R_X=(8X+1)/3、K_X=X(R_X-2) 及 universal p-source 给出一条
  target-independent fresh phase reindexing。E1 重放实际 source state digest、
  canonical G separator 与 target universal raw source；E2--E3 重算唯一 p-only
  root、fresh scope 和 normal form；E4 是 Sol(p) 上的恒等映射；E5 由 T5 的
  TYPEII_G_HANDOFF -> TYPEI major-phase drop 支付。target state serialization
  不含 source q。root 后第一条 Type-I 边由 origin-normalized local rule 同时接受
  q_one_full_carrier_phase_root_entry_v1 与 positive_q_g_full_carrier_phase_root_entry_v1；
  它重放同一个 universal p-source、full-external bundle、parity target serialization、
  Sol(p) 恒等 lift 和 T5 LOCAL_DROP。该定理闭合 ordinary positive-q G handoff 及首条
  local edge 的相对接口，但不处理
  nontrivial marks、source-state existence 或首段之后的 Type-I totality。
claim_status: established
proof_provenance: repository_derivation
review_status: internal_review
depends_on:
  - type-II-p-minus-one-divisor-downset-prime-power-allocation
  - type-II-q-one-full-carrier-phase-root-entry
  - type-I-universal-p-source-capacity-anchor-orbit
  - type-I-t5-full-contract-level-global-well-foundedness
  - denominator-escape-state-contract
topics:
  - type-II
  - positive-q
  - G-state
  - type-I
  - full-carrier
  - phase-reindexing
  - universal-source
  - identity-lift
  - T5
  - E1-E5
  - T6
sources:
  - claim: type-II-p-minus-one-divisor-downset-prime-power-allocation
    role: positive-q endpoint domain and exact G/F/hit reconstruction
  - claim: type-II-q-one-full-carrier-phase-root-entry
    role: p-only target root, universal source, and first strict Type-I segment
  - claim: type-I-universal-p-source-capacity-anchor-orbit
    role: target-side universal p-source and actual raw edge
  - claim: type-I-t5-full-contract-level-global-well-foundedness
    role: canonical TYPEII_G_HANDOFF-to-TYPEI PHASE_DROP ticket
  - concept: concepts/denominator-escape-state-contract.md
    role: ordinary G state, fresh-source scope, and E1-E5 contract
  - reproduction: reproductions/type_ii_positive_q_g_full_carrier_phase_root_entry.py
    role: exact G separators, endpoint-downset receipt, conditional E1 schema, E2-E5, target confluence, and origin-normalized first-local-edge controls
visibility: public
last_checked: '2026-08-17'
---

# ordinary positive-\(q\) G 到全载体 Type I 根的全称准入

## 1. 输入域与结论

固定核心素数

\[
p=24t+1,
\qquad
U=\frac{p-1}{4}=6t.
\tag{1}
\]

令 \(q>1\) 属于 \(p-1\) Type II 的规范端点允许域

\[
\mathcal C_U
=\{d\mid U:d\le Q(U/d)\},
\tag{2}
\]

并定义

\[
m_q=4q-1,
\qquad
x_q=U+q.
\tag{3}
\]

本文的 source hypothesis 是一份**实际、terminal-first 后仍存活**的 ordinary G
endpoint state

\[
S_q=(p,q,m_q,x_q,\mathrm G;
W_{S_q}=\operatorname{Sol}(p)).
\tag{4}
\]

“实际”要求 source state 已按状态合同保存其 provenance 和内容摘要；“ordinary”要求
标记集逐字为 \(\operatorname{Sol}(p)\)，而不是某个非平凡 marked fiber；“G”要求从
\((p,q)\) 的整数数据重新验证目标纤维为空。本文不声称每个 \(q\in\mathcal C_U\) 都会
产生 (4)，只证明每一份满足 (4) 的合法输入都有同一个确定性出口。

结论是具名 adapter

```text
positive_q_g_full_carrier_phase_root_entry_v1
```

给出一条完整 E1--E5 边

\[
S_q\longrightarrow T_X,
\tag{5}
\]

其中 \(T_X\) 只由 \(p\) 决定，完全不含 source \(q\)。

## 2. positive-\(q\) G source guard 可由当前整数重放

由 (2)--(3) 有 \(q\mid U\)，并且

\[
4x_q=p+m_q.
\tag{6}
\]

若正整数 \(d\mid(x_q,m_q)\)，则 (6) 给出 \(d\mid p\)。另一方面

\[
1\le m_q\le4U-1=p-2,
\]

所以 \(d\ne p\)，从而

\[
(x_q,m_q)=1.
\tag{7}
\]

因此 \(x_q\) 的全部素因子都给出 \(U(m_q)\) 中的真实 source generators。令

\[
H_q=
\left\langle
\ell\bmod m_q:\ell\mid x_q,\ \ell\text{ prime}
\right\rangle
\le U(m_q),
\qquad
\tau_q=-1\bmod m_q.
\tag{8}
\]

G 的精确定义是

\[
\tau_q\notin H_q.
\tag{9}
\]

这不是一个需要读取未知解的 oracle。分解 \(x_q\)、枚举有限群 \(U(m_q)\) 并验证
\(H_q\) 的乘法闭包，已经给出有限判定。若合同要求 character form，则对有限阿贝尔商

\[
A_q=U(m_q)/H_q
\]

使用字符分离：\(\bar\tau_q\ne1\) 蕴含存在
\(\chi_q\in\widehat A_q\) 满足
\(\chi_q(\bar\tau_q)\ne1\)。固定 $m_q$ 的素数幂 CRT 次序、奇素数幂上的最小本原根、
\(2^e\) 上的标准 \((-1,5)\) 坐标和 character weight 的字典序后（等价地也可用固定
Smith normal form），取第一张这样的 character；其 pullback 满足

\[
\chi_q(\ell)=1\quad(\ell\mid x_q),
\qquad
\chi_q(-1)\ne1.
\tag{10}
\]

式 (10) 是规范、有限、可重放的 G separator。source guard 保存

```text
source_state_id
endpoint = (p,q,m_q,x_q)
endpoint_downset_receipt
factorization(x_q)
canonical_G_separator
target_fiber.status = empty
signed_defect.status = not_applicable
terminal_first_receipt_digest
marked_solution_set = Sol(p)
```

所以 positive-\(q\) source predicate 与 E1 replay 都可从当前 state 和整数重建；这里没有
把 \(q=1\) 的模 3 特例当作假设。

## 3. 目标根完全不依赖 \(q\)

定义

\[
X=U+1=\frac{p+3}{4}=6t+1,
\qquad
R_X=16t+3=\frac{8X+1}{3},
\qquad
K_X=X(16t+1)=X(R_X-2).
\tag{11}
\]

这些等式不需要 \(q=1\) G 假设。直接展开得到

\[
4K_X=pR_X+1,
\qquad
3\le R_X\le p-2,
\qquad
(X,K_X)=X,
\tag{12}
\]

其中 \(R_X\le p-2\) 由 \(16t+3\le24t-1\) 得到，而
\((X,K_X)=X\) 由 (11) 立即得到。若另一低 Type-I chart 满足
\(4K=pR+1\) 与 \(X\mid K\)，利用 \(p=4X-3\) 有

\[
3R\equiv1\pmod{4X}.
\]

因为 \((3,4X)=1\)，且 \(R_X=(8X+1)/3\) 是区间 \(3\le R\le p-2<4X\) 内的一个解，
它就是该区间内唯一的解。因此 \(T_X\) 的 chart existence/uniqueness 对所有核心素数成立，
而不是从 q=1 source hypothesis 外推。

该目标再由通用 \(p\)-source theorem 得到预声明的 universal
raw source

\[
(p,R_X(p-1)-p,p-1),
\tag{13}
\]

其唯一 \(p\)-edge（shift 1、gcd reduction 1）到达

\[
(1,R_X-1,1).
\tag{14}
\]

式 (11)--(14) 全部只读取 \(p\)。因此把目标序列化为

```text
state_origin        = positive_q_g_full_carrier_phase_root_entry_v1
source_tree_scope   = fresh_source_tree_only
normal_form         = type_i_full_carrier_low_root_v1
equation_target     = 4/p
marked_solution_set = Sol(p)
chart               = (p,R_X,K_X)
absorbed_support    = 1
```

时，target `state_id` 不记录 source \(q\)、旧 Type-II factorization、raw word 或 separator。
同一个 \(p\) 的不同 positive-\(q\) G inputs 因而严格汇合到同一个 \(T_X\)。

这条动作与已有 q=1 adapter 一样，是**有向 phase reindexing**，不是把 Type-II raw word
伪装成 Type-I raw word。旧 raw history 只证明 (4) 是 actual source；(13)--(14) 独立证明
\(T_X\) 有一份 actual fresh source tree。

## 4. E1--E5

| 合同 | 可复核回执 |
|---|---|
| E1 | (4) 的 actual-source provenance、source state digest 与 terminal-first digest 是输入假设的一部分；adapter 验证这些摘要并重放 (2)--(10) 的 endpoint/G guard 与 target universal source (13)--(14)。focused controls 只重放后两项，绝不制造前三项。 |
| E2 | 从 \(p\) 唯一计算 (11)，构造不含 source \(q\) 的 canonical target serialization。 |
| E3 | 重算 (12)、source 正性与互素性、\(A=1\mid K_X\)、`fresh_source_tree_only` 和 target state digest；不继承 source 的 F/G 标签。 |
| E4 | \(W_{S_q}=W_{T_X}=\operatorname{Sol}(p)\)，故 \(\Phi_{T_X\to S_q}(u)=u\) 对整个 target marked set 有定义。 |
| E5 | T5 的 `PHASE_DROP`：同一 equation rank 下从 `TYPEII_G_HANDOFF` 降到 `TYPEI/CHARGED`。 |

E4 不需要 \(\operatorname{Sol}(p)\) 已知非空。若该集合为空，恒等函数仍是从空集到空集的
全域函数；若非空，它逐个保持同一三分式。adapter 的定义和运行均不读取其中任何元素。

把 T5 七元势写全，source 与 target 分别为

\[
\Pi_{T5}(S_q)=(p,3,0,0,0,0,0),
\tag{15}
\]

\[
\Pi_{T5}(T_X)
=(p,2,4,B_p,K_X,0,0),
\qquad
B_p=\frac{(p-1)^2}{4}.
\tag{16}
\]

第二坐标 \(3>2\)，所以不论后续 Type-I protocol/local fields 如何重置，均有

\[
\Pi_{T5}(T_X)<\Pi_{T5}(S_q).
\tag{17}
\]

因此 (5) 是一条 `verified_edge`，而不是 `analysis_evidence`、pending normalization 或
无付款 reset。

这里统一使用 2026-08-17 T5 registry 的 canonical major-phase 编号

\[
\mathrm{TYPEII\_G\_HANDOFF}=3,
\qquad
\mathrm{TYPEI}=2.
\]

早先 q=1 claim 为自己的局部前缀写过 \(2\to1\)；那是同序的局部记号，不是当前

\(\Pi_{T5}\) 的字段值。本文的 claim、receipt 与 verifier 均只使用 (15)--(16) 的
\(3\to2\)，不把两套编号混入同一个 state digest。

## 5. root 后第一个段：origin-normalized local edge

既有 q=1 handoff 的第一个 Type-I segment 的整数构造只读取 (11) 的 root 与 \(t\) 的奇偶，
不读取 source endpoint 的 \(q\)。在 anchor (14) 令

\[
M=R_X-1=16t+2.
\]

complete-excess dispatch 在 \(t\) 为奇数时产生 support \(A_1=16t+2\) 的 marked absorb；
在 \(t\) 为偶数时经显式 overflow 产生 support \(A_1=9t/2\) 的 fixed-\(n\) identity-lift
edge。两者都满足 \(A_1>1\)、\(A_1\mid K_1\)，于是 CHARGED local rank 的首坐标严格下降：

\[
\left\lfloor\frac{B_p}{A_1}\right\rfloor
<B_p
=\left\lfloor\frac{B_p}{1}\right\rfloor.
\tag{18}
\]

定义具名规则

```text
full_carrier_first_local_dispatch_origin_normalized_v1
```

其 parent-origin 白名单恰为

```text
q_one_full_carrier_phase_root_entry_v1
positive_q_g_full_carrier_phase_root_entry_v1
```

规则不按 origin 选择算术；它先投影到下列完整语义 guard：fresh scope、
`type_i_full_carrier_low_root_v1`、equation target、ordinary mark、chart、support (1)、
carrier 和 universal raw-source digest。两种 origin 的投影逐字相同，再按 (t) 的奇偶
产生唯一 target 和新 state digest。

| 合同 | 首条 local edge 的回执 |
|---|---|
| E1 | 重放 parent actual state、universal (p)-source 到 ((1,R_X-1,1)) 的 raw edge，以及 (M=R_X-1) 的 full-external bundle occurrence。 |
| E2 | (t) 奇时唯一序列化 marked-absorb target；(t) 偶时保存 overflow receipt 后序列化 fixed-(n) target。 |
| E3 | 重算 (3\le R_1\le p-2)、(4K_1=pR_1+1)、(A_1>1) 和 (A_1\mid K_1)，并绑定 parent semantic digest。 |
| E4 | parent 与 target 都逐字使用 (W=\operatorname{Sol}(p))，故全域 lift 为恒等映射。 |
| E5 | (18) 给出 canonical `TYPEI/CHARGED` 的 `LOCAL_DROP`。 |

focused controls 没有制造 positive-\(q\) 的 actual parent receipt，所以其 E1 仍正确标为
`complete=false`、`recursive_edge_eligible=false`。相对 theorem 的输入一旦提供 actual
handoff root，E1 的最后一个 hypothesis 即满足；E2--E5 与 target serialization 不再含
q=1-only guard。(p=241) 同时重放两种 origin，并验证它们具有相同 semantic-root digest、
target chart 与 support。

## 6. 精确闭合范围

本文建立

\[
\boxed{
\text{actual terminal-first ordinary positive-}q\text{ G}
\Longrightarrow
\text{p-only fresh full-carrier Type-I root verified edge}.}
\tag{19}
\]

与既有 (q=1) full-carrier phase-root theorem 合并，立即得到 ordinary G 接口的完整
二分闭合：

\[
\boxed{
q\ge1\text{ 的每个 actual terminal-first ordinary G endpoint}
\Longrightarrow
\text{同一个 p-only }T_X.}
\tag{20}
\]

它删除了 ordinary positive-(q) G adapter 这一 T6 接口缺口，但没有证明：

1. 某个 particular positive-(q) endpoint 必在更早的 terminal-first 分支后仍实际可达；
2. (W_S\subsetneq\operatorname{Sol}(p)) 的 nontrivial mark 可使用同一 E4；
3. 首条 origin-normalized local edge 之后的 Type-I selector 全称有定义；
4. T6 的其它 H4、F、marked 或 high-support state family 已闭合。

聚焦 verifier 构造 exact finite-abelian G separator 和显式 endpoint-downset receipt，重放
\((p,q)=(97,3),(241,4),(577,8),(937,13)\) 的 endpoint arithmetic、target universal
source、E2--E5、首条 local edge 的 E1--E5 schema 与 T5 payment，并在
(p=1009) 的 (q=2,4,7,9,18) 五张 G endpoint 上验证 target `state_id` 完全相同：

```bash
python3 reproductions/type_ii_positive_q_g_full_carrier_phase_root_entry.py --verify
```

这些 controls 明确输出 `conditional_adapter_control`、
`recursive_edge_eligible=false`：它们没有 actual source-state receipt 或 terminal-first digest，
所以 E1 保持 `complete=false`。它们只验证：一旦 (4) 的三份实际摘要由 persistent source
state 提供，剩余 E1 arithmetic 与 E2--E5 都是确定且可重放的；有限 controls 不替代该
actual/terminal-first hypothesis。
