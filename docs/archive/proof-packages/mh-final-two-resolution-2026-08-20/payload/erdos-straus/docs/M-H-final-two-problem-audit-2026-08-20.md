# M/H“最后两个问题”精确审计（2026-08-20）

> 复核基线：`49e2e25a72f69015e7bbbcb556155363b08486a0`
>
> M：`CLOSED_BY_UNIVERSAL_VERIFIED_SUCCESSOR`（局部、独立产生的 marked F/G 域）
>
> H：`OPEN_REDUCED_TO_C1_PAID_RESET_OR_OUTER_DROP`
>
> F1：`OPEN`
>
> T6：`OPEN`

## 1. 结论先行

本轮把聊天中最后留下的两个简称作了完整的当前仓库复核：

\[
\mathbf M:
\text{terminal-free low/marked G 是否总有 paid exit},
\]

\[
\mathbf H:
\text{terminal-free high-support、}\mathcal I_\Sigma=\varnothing
\text{ 是否总有 paid exit}.
\]

严格结果是

\[
\boxed{\mathbf M=\mathrm{CLOSED}_{\rm local}},
\qquad
\boxed{\mathbf H=\mathrm{OPEN}}.
\]

M 的缺口是三条已建立定理此前没有组合；现在已经补成一个全称 E1--E5 theorem。
H 则出现了一个全称结构性底层：任何 $C=1$ high-support CHARGED 状态的固定 T5
local tuple 是 $(0,1,0,0)$，因此所有仍返回 CHARGED 的 bundle/total-cofactor finite
macro 都不可能严格下降。继续声称 H 已闭合，必须另外给出 root terminal、外层
$\rho$ 下降，或一条带递归 total target 的付费 protocol/phase reset；当前仓库没有该
定理。

还有一个比 M/H 更上游的版本事实：当前 main 已正式拒绝此前 F1 closure package，
`T6-F1-REACHABLE-STATE-EXHAUSTION` 保持 OPEN。因此 M/H 在当前规范 main 上并不是
整个 T6 的字面“最后两个问题”。本报告不沿用被拒绝包的 closed-world 可达性前提。

## 2. M 的完整关闭

设 actual persistent source

\[
S=(p,R,K;A,\sigma),
\qquad
4K=pR+1,
\quad
3\le R\le p-2,
\quad
A\mid K,
\quad
W_S=\operatorname{Sol}(4,p),
\]

在 terminal-first 后为 marked F/G。规范 universal source

\[
\bigl(p,R(p-1)-p,p-1\bigr)
\xrightarrow{q=p,t=1}
(1,R-1,1)
\]

给出唯一 anchor。若 $R-1\mid K$，直接输出 Type I root terminal；否则令

\[
R-1=Q\beta,
\qquad
Q=\prod_{v_q(R-1)>v_q(K)}q^{v_q(R-1)},
\qquad
M=\operatorname{lcm}(A,Q).
\]

则 $Q>1$、$\beta\mid K$、$(Q,\beta)=1$、$Q\nmid K$，并且 $M/A\ge2$。
唯一 canonical target 由

\[
1\le R'<4M,
\qquad
pR'\equiv-1\pmod{4M},
\qquad
K'=\frac{pR'+1}{4}
\]

确定。source 是 marked，所以

\[
A\le K\le B_p=\frac{(p-1)^2}{4}.
\]

因此

\[
\left\lfloor\frac{B_p}{M}\right\rfloor
<
\left\lfloor\frac{B_p}{A}\right\rfloor,
\]

直接支付 T5 `LOCAL_DROP`。E1 是 actual source、universal path 和完整超额 receipt；
E2 是唯一 target；E3 在 enqueue 前独立重算 hit/F/G/overflow 和 owner；E4 是
$\operatorname{Sol}(4,p)$ 恒等 lift；E5 是上述第一坐标严格下降。

所以对独立产生的合法 marked F/G 状态，得到

\[
\boxed{\text{root terminal}\ \lor\ \text{verified successor}.}
\]

完整证明见
[低支撑 marked F/G 的通用出口](../claims/type-I-marked-g-universal-anchor-complete-excess-exit.md)。

这只关闭 M 的 local exit quantifier。它不证明 source 的 semantic reachability，也不把
新 producer 偷塞进冻结 15-edge surface。实际接入 selector 时必须发布 versioned surface，
并重新重放 F1 producer/target-reentry。

## 3. H 的全称底层

对 high-support CHARGED 状态写

\[
A>B_p,
\qquad
C=K/A.
\]

固定 T5 local tuple 为

\[
\left(0,C,\eta_p,0\right).
\]

在 $C=1,\eta_p=0$ 时，它等于 $(0,1,0,0)$，是整个同协议层的最小元。任一
complete-excess target cofactor $c\in\{1,\ldots,p-1\}$：

\[
c=1\Rightarrow\text{stutter},
\qquad
c>1\Rightarrow\text{rise}.
\]

而且 $M/A\ge2$ 强制 $R_M>p$，所以 target 仍是 overflow，不能借 marked
reclassification 偷降 phase。任何有限个 unqueued intermediate bundle 也无效，因为 E5
比较真实 parent 和最终 persistent target，不比较内部峰值。整体余因子投影在 $C<p$
时又精确满足 $t=0$，即 identity。

direct-cofactor 也有现成的 sharp control：$p=97$ 的
$(R,K;A)=(99,2401;2401)$ 正是 universal $C=1$ chart；其冻结 action 完整回返
$c=1$，只能作为不入队的菜单耗尽记录。当前 T5-v2 势没有 action-menu 计数坐标，
所以该 stutter 不能升级为 persistent edge。

最小 canonical $C=1$ high chart 对每个核心 $p$ 都显式存在：

\[
A_1=K_1=\frac{(p+1)^2}{4}=B_p+p,
\qquad
R_1=p+2.
\]

其 universal anchor 的首个完整超额 bundle 固定为

\[
Q=2,
\qquad
\beta=\frac{p+1}{2},
\qquad
c=\frac{p+1}{2}>1,
\]

所以自然首步对每个核心 $p$ 都上升。其 determinant dual 虽给出小图表

\[
(R_d,K_d)=(p-2,B_p),
\qquad
(R_r,K_r)=\left(3,\frac{3p+1}{4}\right),
\]

却不保留旧 support $A_1$，不能按 joined-support CHARGED edge 准入。丢弃 support
必须另建 paid reset，并证明 reset target 的后续 totality。

完整定理和边界见
[C=1 局部最小元](../claims/type-I-high-support-empty-improvement-c1-local-minimum-boundary.md)。

## 4. 两-bundle 新证据没有关闭 H

对 $p=73$，可重放两段真实 raw path，并把中间 $C=6$ chart 留作不入队 checkpoint：

\[
(143,2610;1305)_{C=2}
\rightsquigarrow
(21023,383670;63945)_{C=6}
\rightsquigarrow
(10508003,191771055;191771055)_{C=1}.
\]

宏端点满足

\[
(0,2)>(0,1),
\]

所以它是“单个 bundle 全上升”之外的真实两步正控制，证明中间上升本身不是绝对障碍。
但是最终状态正落在 $C=1$ 底层；它没有 H 的下一条 paid exit。并且 $p=73$ 已有
Type II root terminal $(20,219,4380)$，实际 terminal-first 会优先结束。因此当前
replay 正确标为

```text
selector_status = analysis_evidence
recursive_edge_eligible = false
```

而不是 selector edge。

## 5. 严格剩余定理

H 现在被精确压缩为

\[
\boxed{
\begin{aligned}
&H\text{ actual, terminal-first miss, }A>B_p,C=1\\
&\quad\Longrightarrow
\text{OUTER\_RANK\_DROP}
\ \lor\
\text{paid lower-protocol target with recursively total owner},
\end{aligned}}
\]

或者证明该 actual family 为空。该命题需要新的数学；当前 complete-excess、
same-chart promotion、total-cofactor 和 determinant dual 不能组合出它。

若 terminal 的含义是任意可核验根证书，则 `terminal-first miss` 的语义全称版本与
`Sol(4,p)` 是否为空直接相关；若它只是一个冻结的有限 prefix，miss 更不能被当成
Erdős--Straus 反例。只有在 F1、全部 family totality、F3、F4 和 F5 都完成后，H 的
出口才能通过 T5 良基归纳参与全局猜想证明。

## 6. 仓库改动与验证

新增：

- `claims/type-I-marked-g-universal-anchor-complete-excess-exit.md`；
- `claims/type-I-high-support-empty-improvement-c1-local-minimum-boundary.md`；
- 两个 focused reproduction；
- 四个回归测试；
- `data/mh-final-two-problem-resolution-v1.json`。

同时修复了完整 checkout 中四处缺少反斜杠的 LaTeX 间距命令，它们此前使
`scripts/kb.py validate` 失败。

聚焦命令：

```bash
python reproductions/type_i_marked_g_universal_anchor_complete_excess_exit.py --verify
python reproductions/type_i_high_support_c1_local_minimum_boundary.py --verify
python -m unittest tests.test_type_i_mh_final_two_boundary -v
python scripts/kb.py validate
```

最终重放结果：

```text
knowledge-base validation: 1392 documents PASS
maintained focused suite:    60 / 60 PASS
M/H boundary tests:           4 / 4 PASS
T6 ledger + root dispatcher:  4 / 4 PASS
pre-T6 negative/audit suite:  16 / 16 PASS
CI E/F lint surface:          PASS
```

冻结面审计继续返回 16 个 families、15 条 edges、8 个 active mathematical gaps
与 5 个 open frontier theorems；本轮没有用 M 的局部定理篡改这个冻结账本。

本轮规范状态是：

| 对象 | 状态 |
|---|---|
| M local marked F/G exit | `CLOSED_BY_UNIVERSAL_VERIFIED_SUCCESSOR` |
| H nonempty-improvement branch | `CLOSED_CONDITIONALLY` |
| H $C=1$ CHARGED local bundle/cofactor exit | `IMPOSSIBLE_UNDER_FIXED_LOCAL_TICKET` |
| H paid reset / outer drop | `OPEN` |
| F1 semantic reachability exhaustion | `OPEN` |
| T6 / Erdős--Straus | `OPEN` |

因此不能诚实交付“两个都已 closed”的账本；可以交付的是一个真正关闭的 M，以及 H 的
全称局部 no-go、最小边界和唯一合法剩余接口。
