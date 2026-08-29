# 当前待证明问题组合与优先级

**整理日期：** 2026-08-29
**目的：** 用当前真实的证明依赖，而不是历史编号顺序，安排 standalone proposition
portfolio。本文是研究导航，不是任何 dossier 的逻辑前提，也不改变 F1、F2、F3、T6
或 Erdős--Straus 猜想的状态。

## 1. 关键重估

SP-05 的 complete-terminal package 给出两个决定性结论：

1. 对一个固定 \(p\)，完整排序 factor-pair schedule 可有限判定

\[
\mathsf{Sol}(4,p)\ne\varnothing
\quad\text{或}\quad
\mathsf{Sol}(4,p)=\varnothing;
\]

2. 因此，一条现实 complete-terminal-first q=1,G nonterminal edge 必须以
   \(\mathsf{Sol}(4,p)=\varnothing\) 为前提，即要求 Erdős--Straus 反例。

这不使 SP-05 的数学包无价值；它准确排除了错误路线。但它意味着“先构造一条实际
SP-05 nonterminal edge”不再是合理的主攻目标。递归证明只需要完整处理冻结 selector
policy 中位于 selected branch 之前的 actions，不需要先证明所有可能 terminal formulas
均不存在。SP-21 与 SP-22 正是据此新增。

## 2. 已解决与已澄清

| 项目 | 当前结论 | 对主线的意义 |
|---|---|---|
| SP-01 | 条件性的良基归纳逻辑核已写明；实际全局实例化仍未完成 | 不应作为主要数学攻关 |
| SP-02 | ESTABLISHED：有限良构模型中 constructor 分类与 UNKNOWN 不可达 | 只解决抽象 A0，不解决 concrete inventory |
| SP-04 | ESTABLISHED：M23 全除子 registered-prefix schedule | 可作为有限 policy action，不是 global terminal universe |
| SP-05 | complete-terminal decision 与条件 phase-root branch 已证；实际 edge 仍 OPEN | 明确排除 complete-MISS 作为 pilot 前提 |
| SP-21 | ESTABLISHED：abstract scope-bound safety；concrete policy instance 仍 OPEN | P0 从抽象安全证明转为实际 policy/authority 实例化 |
| T5 | 合同层 N7 良基势已闭合 | 为新 edge 提供 ticket grammar，不提供 edge existence |

当前仍有 20 个 OPEN_PROPOSITION：旧 SP-01/03/05--20 共 18 个，加上新的
SP-21、SP-22。它们的价值并不相同。

## 3. P0：必须先解决的合同问题

### P0.1 SP-21：concrete scope-bound terminal policy instance

抽象 safety theorem 已闭合；当前最高优先级是为一个实际 producer 证明其 concrete
policy instance。它必须建立：

\[
\text{all actions before a selected producer replayed}
\Longrightarrow
\text{terminal-preempt or valid successor},
\]

且不把 policy-relative MISS 写成 \(\mathsf{MISS\_COMPLETE}\)。

它直接解除当前 V1 structured receipt 的错误瓶颈：现有 schema 把 generic E1 绑定到
global terminal-universe MISS，因而把任何真实 nonterminal branch 绑成反例搜索。
SP-21 的已建立抽象结论仍要求所有 prior registered terminal/producer actions 的完整有序重放、
actual source、E1--E5 和 R；concrete registry/authority/replayer 缺失，故这不是降低证明标准。

### P0.2 SP-03 的 scoped 子目标：policy/no-bypass

SP-03 的原量词是全局 queue/no-bypass/re-entry，暂时过宽。先用 SP-21 的 policy registry
证明一个 selected branch 的唯一写入路径、policy pin、动作重排拒绝和 target re-entry。
在至少有一条真实 pilot branch 后，再把 SP-03 扩展为 all-producer theorem。

## 4. P1：能够产生首个真实闭合截面的任务

### P1.1 SP-22：actual q=1,G scoped phase-root pilot

这是 SP-05 的可行替代。其输入不是 counterexample-style complete MISS，而是已认证 source 的
policy-relative prior clearance。目标是把以下已知数学核接入真实对象：

\[
\text{actual source}
\to\text{scope clearance}
\to\text{E2}
\to\text{common E3}
\to\text{identity E4}
\to\text{PHASE_DROP}
\to\text{R}.
\]

完成 SP-22 可首次验证“policy-relative terminal-first 与 actual E1--E5 edge 能共存”。
它仍不等于 post-G totality 或 T6 closure。

### P1.2 SP-15：TR1 \(D^\ast\) fresh occurrence

这是最值得优先投入的纯数学 residual。它已经有完整 terminal menu 顺序、freshness/
capacity split 和 least-factor 选择框架；缺的是把 \(D^\ast\) 的条件性整数因子变成
actual source-forward occurrence。若完成，可给 proper-root \(k>1\) 提供真正的物理出口，
比继续扩展局部同余更接近 O2。

### P1.3 SP-14：QC1 integer occurrence

它与 SP-15 并列为 proper-root 的第二主路线。最有价值的子问题是：

\[
q_\perp\mid E
\Longrightarrow
\text{source-bound raw deflation with E1--E5},
\]

并单独处理 \(q_\perp\nmid E\) 的 endpoint-occurrence/terminal 二分。不要把 ideal
factor当作 E1。

### P1.4 SP-07：C8/H4 actual atomic closure

C8 有已经明确的 terminal / double-low / OTHER 三分割，且 OTHER 有 parent-anchored
second-full-excess fallback。真正缺口是 actual parent path、scope-bound terminal policy、
target classifier 与 common admission。它是 F2 中最具明确构造骨架的 totality 问题。

### P1.5 SP-16：\(m=3,q=5\) R1 runtime binding

这是 F3 的窄源路径任务。它本身不解决 q=5 后续残差，但若能把 transcript 接到一个真实
producer receipt，可为 SP-17--20 提供第一个非 synthetic E1 起点。

## 5. P2：保留但暂不主攻

| 问题 | 原因 |
|---|---|
| SP-06 post-G/C9 total dispatch | 汇总性命题；应在 SP-22 与 C8/post-G leaf 有真实 receipt 后再做 |
| SP-08 C=1 R=3-G | 是实质 hard core，但当前缺 actual source、E3 和 non-upward re-entry；先完成 shared policy/receipt |
| SP-09 C>1 empty-improvement | 仍是宽补集，已有控制已排除 bounded carry 捷径；不宜先攻 |
| SP-10 noncanonical grammar | 需要 future/legacy incoming producer grammar，适合在 active producer registry 成形后处理 |
| SP-11 high strict carry | 局部算术较强，但仍没有 target-independent actual high source path |
| SP-12, SP-13 high stutter | 分别面对 Pell/odd-high 无界族；目前缺可证明的 nonrecurrence invariant，风险最高 |
| SP-17--SP-20 q=5 后续叶 | 应在 SP-16 先得到 actual transcript 后按 nonminimal、regeneration、one-sided、two-sided顺序推进 |

SP-20 尤其不能提前主攻：已知 direct canonical \(p^2\) rechart 的 cofactor 为 \(p-1\)，
没有 E5 ticket；重复该图表不会产生进展。

## 6. 推荐执行链

\[
\boxed{
\text{SP-21 concrete policy instance}
\to
\text{SP-03 scoped policy/no-bypass}
\to
\text{SP-22}
\to
\text{SP-03 globalization}
\to
\text{SP-15}
\to
\text{SP-14}
\to
\text{SP-07}
\to
\text{SP-16}
}
\]

这条链的目标不是立即声称 T6。它依次解决：

1. successor 不再被错误的 global MISS 前提阻断；
2. 一条真实 q=1 pilot 可以被完整审计；
3. proper-root 的两个主要物理化出口获得可接入的 source/admission 语言；
4. C8 与 q=5 路线能开始贡献 actual family closure。

每完成一个节点，都必须保持以下边界：

\[
\mathsf{FAMILY\_EMPTY}
\quad\text{或}\quad
\mathsf{TERMINAL}
\quad\text{或}\quad
\mathsf{VERIFIED\_SUCCESSOR\_E1\text{-}E5\text{-}R}.
\]

局部恒等式、有限样本、未认证 source、analysis evidence、scope MISS 或 T5 draft 都不能
单独改变 F1/F2/F3/T6 状态。
